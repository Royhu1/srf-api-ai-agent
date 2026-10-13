---
name: srf-data
description: Query the SRF (Centre for Sustainable Road Freight) data platform at data.csrf.ac.uk through its Python client (srf_client). Covers vehicles, vehicle classes, fleets, trips, legs, telemetry measurements (fuel consumption, speed, GPS, CAN data), EV chargers and charging transactions, routes, orders, locations, trailers, trials and organisations. Use whenever the user asks about SRF/CSRF data, freight/fleet vehicle data, truck/bus/van/car telemetry, fuel or energy consumption analysis, EV charging sessions, or looking up vehicles by registration, VIN, fuel type or make.
---

# SRF Data Platform

## Setup

Requires Python with `srf-client`, `pandas`, `python-dotenv`
(`pip install srf-client pandas python-dotenv`). If the project has a venv
(e.g. `.venv/Scripts/python.exe` on Windows), use it for all Python here.
The API key is read from the `SRF_API_KEY` environment variable or a `.env`
file at the project root. Standard bootstrap:

```python
import os
from dotenv import load_dotenv
load_dotenv()  # or pass an explicit path to the project .env
from srf_client import SRFData
srf = SRFData(api_key=os.environ["SRF_API_KEY"])
srf.ping()  # True if reachable & authenticated
```

API root defaults to `https://data.csrf.ac.uk/api`. The client is read-only for
normal use; `post()` requires write scope.

## Ready-made scripts

Prefer these for one-shot lookups instead of writing new code
(run with the venv python; both print JSON):

- `scripts/vehicle_lookup.py` — vehicles by `--reg` (exact registration/VIN),
  or filtered by `--fuel/--make/--type`, with `--trips` (recent trips) and
  `--dvla` (external DVLA class lookup) options.
- `scripts/list_data_types.py` — telemetry type codes for `get_data()`,
  with `--search <substring>`. Run this before requesting measurement data:
  type codes are short opaque strings (e.g. `13` = ambient pressure, `LFC`,
  `VDHR`) and must not be guessed.

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

## Full API reference

`references/api_reference.md` holds the complete client docs (v2.8 Sphinx dump).
Grep it rather than reading whole: section anchors look like
`## srf_client.<module>.html`; useful searches: `class Vehicle`, `class Trip`,
`class Leg`, `get_data_frame`, `ChargerTransaction`, `class Route`,
`find_by_`, `lookup`.
