---
name: srf-data
description: Query the SRF (Centre for Sustainable Road Freight) data platform at data.csrf.ac.uk, through its Python client (srf_client) or its REST API directly. Covers vehicles, vehicle classes, fleets, trips, legs, telemetry measurements (fuel consumption, speed, GPS, CAN data), road gradient, land elevation, reverse geocoding, EV chargers, charger status and charging transactions, routes, orders, locations, trailers, trials and organisations. Use whenever the user asks about SRF/CSRF data, freight/fleet vehicle data, truck/bus/van/car telemetry, fuel or energy consumption analysis, EV charging sessions, elevation or gradient along a route, or looking up vehicles by registration, VIN, fuel type or make.
---

# SRF Data Platform

Works the same in Claude Code and Codex: paths below are relative to this
skill's folder (`.claude/skills/srf-data/`, `~/.codex/skills/srf-data/`, ...).

## Setup

Requires Python with `srf-client`, `pandas`, `python-dotenv`, `requests`
(`pip install srf-client pandas python-dotenv requests`). If the project has a
venv (e.g. `.venv/Scripts/python.exe` on Windows), use it for all Python here.
The API key is read from the `SRF_API_KEY` environment variable, else from the
nearest `.env` above the current directory. Never print the key. Standard
bootstrap:

```python
import os
from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv(usecwd=True))
from srf_client import SRFData
srf = SRFData(api_key=os.environ["SRF_API_KEY"])
srf.ping()  # True if reachable & authenticated; False usually means an expired key
```

The key is a Bearer token (a temporary read-only token from the platform's
Manage Access page, or an OAuth 2.0 client token). API root:
`https://data.csrf.ac.uk/api`; `GET /api` returns `{"version": "1.14.4"}`.
Write operations (e.g. `POST legs/{id}/gradient`) need a token with write scope.

## Ready-made scripts

Prefer these for one-shot lookups instead of writing new code
(run with the venv python; all print to stdout):

- `scripts/vehicle_lookup.py` — vehicles by `--reg` (exact registration/VIN),
  or filtered by `--fuel/--make/--type`, with `--trips` (recent trips) and
  `--dvla` (external DVLA class lookup) options.
- `scripts/list_data_types.py` — telemetry type codes for `get_data()`,
  with `--search <substring>`. Run this before requesting measurement data:
  type codes are short opaque strings (e.g. `13` = ambient pressure, `LFC`,
  `VDHR`) and must not be guessed.
- `scripts/api_request.py <path> [key=value ...]` — any REST endpoint, raw.
  JSON is pretty-printed, CSV passed through; `--all` follows paging,
  `--post` sends parameters as a form body, `--out FILE` saves the body.
  Give the path without a leading slash (`legs/42/data`, not `/legs/42/data`):
  Git Bash on Windows rewrites `/x` into a filesystem path.

## Data model in one page

Sub-clients on `srf`: `vehicles`, `vehicle_classes`, `fleets`, `trips`, `legs`,
`chargers`, `transactions` (EV charging), `routes`, `orders`, `locations`,
`trailers`, `trials`, `organisations`. All support `find_all(**filters)`;
most support `find_by_<parent>(parent_obj)`.

Hierarchy: **Vehicle → Trip (one journey/day) → Leg (ignition-on section)**.
Telemetry hangs off trips and legs. EV charging: **Charger → ChargerTransaction
(one session) → meter readings**; transactions link to both charger and vehicle.

Key `Vehicle` fields: `registration`, `vin`, `make`, `model`,
`type` (`RIGID|ARTIC|VAN|BUS|CAR`), `fuel` (`DIESEL|PETROL|CNG|LNG|H2|ELECTRIC`),
`weight_class` (t), `euro_standard`, `country`.

## Core patterns

```python
from srf_client import eq, prefix, contains, between, any_of, near, asc, desc
from srf_client.paging import paged_items

# exact lookup by registration / VIN / internal id
v = srf.vehicles.get(obj_id="AB12 CDE")          # None if not found

# filtered listing — filter values MUST be Operator objects, not bare strings
page = srf.vehicles.find_all(fuel=eq("ELECTRIC"), sort=asc("make"))
page.total                # total matches (all pages)
list(page.items)          # current page only (~20); NOT the full result set
for v in paged_items(page): ...   # iterate ALL matches across pages

# traverse related entities in filters (dict syntax required)
trips = srf.trips.find_all(**{"vehicle.fuel": eq("ELECTRIC")})

# trips / legs for a vehicle
trips = v.get_trips()                     # Page[Trip]
legs  = trip.get_legs()

# telemetry → DataFrame (columns named "{TYPE} {field}", e.g. "LFC trip fuel")
from datetime import timedelta
df = trip.get_data_frame(["LFC", "VDHR"], timedelta(minutes=1))
# raw measurements: trip.get_data(include={"VIN"}) → Measurement(timestamp, type, data)

# EV charging sessions for a vehicle
txns = v.get_transactions()               # Page[ChargerTransaction]
df = txn.get_data_frame()                 # meter readings time-series

# external DVLA lookup (works for any UK registration, even off-platform)
ext = srf.vehicle_classes.lookup("AB12 CDE")   # ExternalVehicleClass or None
```

## Pitfalls

- `page.items` is one page only — use `page.total` for counts and
  `paged_items(page)` to fetch everything. `page.last.items[-1]` gets the
  final item.
- A trip/leg only has data for the type codes in its `.types` frozenset;
  filter candidates with `find_all(types=contains("LFC"))`.
- `Measurement.data` values are strings; convert with
  `pd.to_numeric(..., errors="coerce")`. Timestamps are epoch milliseconds
  (`pd.to_datetime(ts, unit="ms")`). `get_data_frame` handles both already.
- `find_all(lazy=True)` returns URI-only proxies — fast for counting or
  passing to `find_by_*`, but attribute access triggers per-object fetches.
- Fetching full telemetry for long trips is slow; pass `min_interval=`
  (get_data) or a coarse `resolution` (get_data_frame) to downsample.
- Not every vehicle has trips, and only ELECTRIC vehicles have charging
  transactions; check `.total` before iterating.

## REST API (when srf_client is not enough)

srf_client wraps most entities, but the REST API exposes more options. Use
`scripts/api_request.py`, or `requests` with `Authorization: Bearer <key>`.

**Response envelope.** Lists return `{"_items": [{"_item": {...}, "_location": url}],
"_total", "_first", "_prev", "_next", "_last"}`; links to related entities are
`{"_location": url}` objects (e.g. `vehicle._location`). Single GETs return the
object itself. Paging: `page` (from 0), `size` (default 25), `sort=field,asc|desc`;
`includeItems=false` returns only the `_location`s (fast counting and id listing).

**Filtering** (list endpoints; repeat a parameter to combine; filters AND together):

| Field type | Syntax |
|---|---|
| String | `make=Volvo`; wildcard `vin=XR*`; OR by repeating, `fuel=DIESEL&fuel=CNG` |
| Number / Date / Period | equality `field=v`; range `field=min&field=max` (periods like `duration=2h&duration=1d`) |
| Array (e.g. `types`) | contains all: `types=12&types=LFC` |
| Point | near: `point=(lat,lon),radius_km` |
| Related entity | dotted path: `vehicle.fuel=ELECTRIC`, `organisation.name=...`, `depot.postCode=...` |

**Endpoints** (all `GET` unless noted; `{id}` is the internal numeric id):

| Area | Endpoints |
|---|---|
| Types | `types` (telemetry type codes and CSV field units); `types?raw=true` (raw-data types) |
| Vehicles | `vehicles`, `vehicles/{id}`, `vehicles/{registration-or-VIN}`, `vehicles/{id}/trips`, `vehicles/{id}/transactions` |
| Vehicle classes | `vehicle_classes`, `vehicle_classes/{id}`, `vehicle_classes/{id}/routes`, `vehicle_classes/lookup?registration=...` (public vehicle data; rate-limited, may return 429, may be inaccurate) |
| Trips | `trips`, `trips/{id}`, `trips/{id}/legs` |
| Legs | `legs`, `legs/{id}`, `legs/{id}/data` (CSV), `legs/{id}/raw` (CSV, source-specific), `legs/{id}/gradient` (CSV), `POST legs/{id}/gradient` (schedule computation; write scope; returns 202) |
| Elevation | `elevation?point=lat,lon&point=...` returns a JSON array of metres (or `null`) in the same order; use `--post` for many points (form, JSON `[{"lat","lon"}]` and CSV bodies are accepted) |
| Locations | `locations`, `locations/{id}`, `locations/{id}/chargers`, `locations/{id}/routes`, `locations/lookup?point=lat,lon` (reverse geocode: area name and nearest postcode) |
| Chargers | `chargers`, `chargers/{id}`, `chargers/{id}/status` (per-connector status history, `connector=` filter), `chargers/{id}/transactions` |
| Transactions (EV charging sessions) | `transactions`, `transactions/{id}`, `transactions/{id}/data` (meter readings, CSV) |
| Fleets | `fleets`, `fleets/{id}`, `fleets/{id}/entries` |
| Routes / orders | `routes`, `routes/{id}`, `routes/{id}/orders`, `orders`, `orders/{id}` |
| Trailers / trials / organisations | `trailers`, `trailers/{id}`, `trailers/{id}/trips`, `trials`, `trials/{id}`, `trials/{id}/trips`, `organisations`, `organisations/{id}` |

**Leg data CSV** (`legs/{id}/data`): one measurement per line,
`epoch_ms,TYPE,field1,field2,...`, with the fields of that type in the order
listed by `types` (units there too). Lines of different types have different
lengths, so this is not RFC 4180 CSV: split on the type column. Missing values
appear as `NaN`. Options: `include=TYPE` (repeatable), `minInterval=<ms>`
(downsample; CAN sources such as SRFLOGGER only), `includeCanSource=true`
(adds a CAN source-device column after the type). `legs/{id}/raw` is the
logger's own format (depends on `trip.source`), with a header line when
unfiltered.

**Gradient CSV** (`legs/{id}/gradient`): type `9` lines,
`epoch_ms,9,distance_m,elevation_m,gradient_deg`. A 404 means it has not been
computed for that leg. It is derived from today's road network and elevation
data, so road changes since the recording can cause large errors.

Units of entity fields: distances and odometers km, consumption L (fuel) or
kWh (electric), weights kg, `maxPower` kW, `weightClass` t. Measurement axes
follow ISO 8855 (X forward, Y left, Z up). Leg `weightSource` is `CVW`,
`AXLE`, `WEIGHBRIDGE` or `ESTIMATE`.

## Full references

Grep these rather than reading them whole:

- `references/api_reference.md` — the srf_client Python docs (v2.8). Section
  anchors look like `## srf_client.<module>.html`; useful searches:
  `class Vehicle`, `class Trip`, `class Leg`, `get_data_frame`,
  `ChargerTransaction`, `class Route`, `find_by_`, `lookup`.
- `references/platform_api.md` — the platform REST API docs (v1.14.4): every
  endpoint with parameter and response-field tables and examples. Present only
  in local installs: it comes from the login-only documentation and is not in
  the public repository. If it is missing, use the summary above and
  `scripts/api_request.py` to inspect live responses. Useful searches:
  `### 5.3` (leg data), `#### Response fields`, `#### Query parameters`, or an
  endpoint such as `GET /api/chargers`.
