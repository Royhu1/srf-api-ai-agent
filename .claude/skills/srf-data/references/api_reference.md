# SRF Python Client — Documentation (local reference copy)

> Generated 2026-06-25 by scraping the login-gated Sphinx docs at
> `https://data.csrf.ac.uk/python/docs/` through an authenticated browser session (Playwright over CDP).
> External/copyrighted source — keep for local development use only.

## Contents

- [index.html](#index)
- [srf_client.html](#srf_client)
- [srf_client.client.html](#srf_client-client)
- [srf_client.oauth.html](#srf_client-oauth)
- [srf_client.model.html](#srf_client-model)
- [srf_client.filter.html](#srf_client-filter)
- [srf_client.sort.html](#srf_client-sort)
- [srf_client.paging.html](#srf_client-paging)
- [srf_client.vehicles.html](#srf_client-vehicles)
- [srf_client.vehicle_classes.html](#srf_client-vehicle_classes)
- [srf_client.fleets.html](#srf_client-fleets)
- [srf_client.legs.html](#srf_client-legs)
- [srf_client.trips.html](#srf_client-trips)
- [srf_client.trials.html](#srf_client-trials)
- [srf_client.routes.html](#srf_client-routes)
- [srf_client.locations.html](#srf_client-locations)
- [srf_client.transactions.html](#srf_client-transactions)
- [srf_client.chargers.html](#srf_client-chargers)
- [srf_client.orders.html](#srf_client-orders)
- [srf_client.trailers.html](#srf_client-trailers)
- [srf_client.organisations.html](#srf_client-organisations)

---

<a id="index"></a>

## index.html

*Source: https://data.csrf.ac.uk/python/docs/index.html*

# CSRF Python client Documentation

Version 2.8, generated Oct 15, 2025.

Contents:

* [srf\_client package](srf_client.html)
  + [Examples](srf_client.html#examples)
  + [Submodules](srf_client.html#submodules)
    - [srf\_client.chargers module](srf_client.chargers.html)
      * [`ChargersClient`](srf_client.chargers.html#srf_client.chargers.ChargersClient)
    - [srf\_client.client module](srf_client.client.html)
      * [`ApiKeyAuth`](srf_client.client.html#srf_client.client.ApiKeyAuth)
      * [`LogRetry`](srf_client.client.html#srf_client.client.LogRetry)
      * [`SRFData`](srf_client.client.html#srf_client.client.SRFData)
    - [srf\_client.filter module](srf_client.filter.html)
      * [`AnyOf`](srf_client.filter.html#srf_client.filter.AnyOf)
      * [`Between`](srf_client.filter.html#srf_client.filter.Between)
      * [`Contains`](srf_client.filter.html#srf_client.filter.Contains)
      * [`Equals`](srf_client.filter.html#srf_client.filter.Equals)
      * [`Near`](srf_client.filter.html#srf_client.filter.Near)
      * [`Operator`](srf_client.filter.html#srf_client.filter.Operator)
      * [`Prefix`](srf_client.filter.html#srf_client.filter.Prefix)
      * [`any_of`](srf_client.filter.html#srf_client.filter.any_of)
      * [`between`](srf_client.filter.html#srf_client.filter.between)
      * [`contains`](srf_client.filter.html#srf_client.filter.contains)
      * [`eq`](srf_client.filter.html#srf_client.filter.eq)
      * [`near`](srf_client.filter.html#srf_client.filter.near)
      * [`prefix`](srf_client.filter.html#srf_client.filter.prefix)
    - [srf\_client.fleets module](srf_client.fleets.html)
      * [`FleetEntriesClient`](srf_client.fleets.html#srf_client.fleets.FleetEntriesClient)
      * [`FleetsClient`](srf_client.fleets.html#srf_client.fleets.FleetsClient)
    - [srf\_client.legs module](srf_client.legs.html)
      * [`LegsClient`](srf_client.legs.html#srf_client.legs.LegsClient)
    - [srf\_client.locations module](srf_client.locations.html)
      * [`LocationsClient`](srf_client.locations.html#srf_client.locations.LocationsClient)
    - [srf\_client.model module](srf_client.model.html)
      * [`BaseLocation`](srf_client.model.html#srf_client.model.BaseLocation)
      * [`Calibration`](srf_client.model.html#srf_client.model.Calibration)
      * [`Charger`](srf_client.model.html#srf_client.model.Charger)
      * [`ChargerMeter`](srf_client.model.html#srf_client.model.ChargerMeter)
      * [`ChargerStatus`](srf_client.model.html#srf_client.model.ChargerStatus)
      * [`ChargerTransaction`](srf_client.model.html#srf_client.model.ChargerTransaction)
      * [`DataType`](srf_client.model.html#srf_client.model.DataType)
      * [`ExternalLocation`](srf_client.model.html#srf_client.model.ExternalLocation)
      * [`ExternalVehicleClass`](srf_client.model.html#srf_client.model.ExternalVehicleClass)
      * [`FieldDef`](srf_client.model.html#srf_client.model.FieldDef)
      * [`Fleet`](srf_client.model.html#srf_client.model.Fleet)
      * [`FleetEntry`](srf_client.model.html#srf_client.model.FleetEntry)
      * [`Leg`](srf_client.model.html#srf_client.model.Leg)
      * [`Location`](srf_client.model.html#srf_client.model.Location)
      * [`Measurement`](srf_client.model.html#srf_client.model.Measurement)
      * [`Order`](srf_client.model.html#srf_client.model.Order)
      * [`Organisation`](srf_client.model.html#srf_client.model.Organisation)
      * [`Route`](srf_client.model.html#srf_client.model.Route)
      * [`Trailer`](srf_client.model.html#srf_client.model.Trailer)
      * [`Trial`](srf_client.model.html#srf_client.model.Trial)
      * [`Trip`](srf_client.model.html#srf_client.model.Trip)
      * [`Vehicle`](srf_client.model.html#srf_client.model.Vehicle)
      * [`VehicleClass`](srf_client.model.html#srf_client.model.VehicleClass)
    - [srf\_client.oauth module](srf_client.oauth.html)
      * [Single-user CLI](srf_client.oauth.html#single-user-cli)
      * [Multi-user webapp](srf_client.oauth.html#multi-user-webapp)
      * [Client-only access](srf_client.oauth.html#client-only-access)
      * [`SRFDataOAuth`](srf_client.oauth.html#srf_client.oauth.SRFDataOAuth)
      * [`discover_urls()`](srf_client.oauth.html#srf_client.oauth.discover_urls)
      * [`make_urls()`](srf_client.oauth.html#srf_client.oauth.make_urls)
    - [srf\_client.orders module](srf_client.orders.html)
      * [`OrdersClient`](srf_client.orders.html#srf_client.orders.OrdersClient)
    - [srf\_client.organisations module](srf_client.organisations.html)
      * [`OrganisationsClient`](srf_client.organisations.html#srf_client.organisations.OrganisationsClient)
    - [srf\_client.paging module](srf_client.paging.html)
      * [`Page`](srf_client.paging.html#srf_client.paging.Page)
      * [`PagingClient`](srf_client.paging.html#srf_client.paging.PagingClient)
      * [`paged_items()`](srf_client.paging.html#srf_client.paging.paged_items)
    - [srf\_client.routes module](srf_client.routes.html)
      * [`RoutesClient`](srf_client.routes.html#srf_client.routes.RoutesClient)
    - [srf\_client.sort module](srf_client.sort.html)
      * [`Ascending`](srf_client.sort.html#srf_client.sort.Ascending)
      * [`Descending`](srf_client.sort.html#srf_client.sort.Descending)
      * [`Sort`](srf_client.sort.html#srf_client.sort.Sort)
      * [`asc`](srf_client.sort.html#srf_client.sort.asc)
      * [`desc`](srf_client.sort.html#srf_client.sort.desc)
    - [srf\_client.trailers module](srf_client.trailers.html)
      * [`TrailersClient`](srf_client.trailers.html#srf_client.trailers.TrailersClient)
    - [srf\_client.transactions module](srf_client.transactions.html)
      * [`TransactionsClient`](srf_client.transactions.html#srf_client.transactions.TransactionsClient)
    - [srf\_client.trials module](srf_client.trials.html)
      * [`TrialsClient`](srf_client.trials.html#srf_client.trials.TrialsClient)
    - [srf\_client.trips module](srf_client.trips.html)
      * [`TripsClient`](srf_client.trips.html#srf_client.trips.TripsClient)
    - [srf\_client.vehicle\_classes module](srf_client.vehicle_classes.html)
      * [`VehicleClassesClient`](srf_client.vehicle_classes.html#srf_client.vehicle_classes.VehicleClassesClient)
    - [srf\_client.vehicles module](srf_client.vehicles.html)
      * [`VehiclesClient`](srf_client.vehicles.html#srf_client.vehicles.VehiclesClient)

# Indices and tables

* [Index](genindex.html)
* [Module Index](py-modindex.html)
* [Search Page](search.html)

<a id="srf_client"></a>

## srf_client.html

*Source: https://data.csrf.ac.uk/python/docs/srf_client.html*

# srf\_client package

Python library for interacting with the SRF’s core data platform.

Note

The `SRFData` implementation is designed for personal scripting use only.
If you wish to use API access on behalf of others as part of some
service, see the `oauth` module and contact SRF technical support.

## Examples

```
# initialise client for personal scripting use
from srf_client import SRFData
srf = SRFData(api_key='...')

# use a file-based http cache
from cachecontrol.caches import SeparateBodyFileCache
srf = SRFData(api_key='...',
              cache=SeparateBodyFileCache('/var/cache/srf_client'))

# get last recorded leg
leg = srf.legs.find_all().last.items[-1]

# plot ambient pressure for leg
import pandas as pd
df = pd.DataFrame(leg.get_data('13'))
df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
df['data'] = pd.to_numeric(df['data'], errors='coerce')
df.plot('timestamp', 'data')

# get vehicle and driver id
vin = di = None
for measurement in leg.get_data({'VIN', 'DI'}):
    if measurement.type == 'VIN':
        vin = measurement.data
    if measurement.type == 'DI':
        di = measurement.data.split(',')[0]
    if vin and di:
        break

# list all DAF trucks
from srf_client import prefix
page = srf.vehicles.find_all(vin=prefix('XLR'))

# plot total fuel consumption against total distance for recent trip
from srf_client import contains
trip = srf.trips.find_all(types=contains('LFC', 'VDHR')).last.items[0]
df = trip.get_data_frame(['LFC', 'VDHR'], timedelta(minutes=1))
df.plot.scatter('VDHR hr total vehicle distance',
                'LFC engine total fuel used')
```

## Submodules

* [srf\_client.chargers module](srf_client.chargers.html)
  + [`ChargersClient`](srf_client.chargers.html#srf_client.chargers.ChargersClient)
* [srf\_client.client module](srf_client.client.html)
  + [`ApiKeyAuth`](srf_client.client.html#srf_client.client.ApiKeyAuth)
  + [`LogRetry`](srf_client.client.html#srf_client.client.LogRetry)
  + [`SRFData`](srf_client.client.html#srf_client.client.SRFData)
* [srf\_client.filter module](srf_client.filter.html)
  + [`AnyOf`](srf_client.filter.html#srf_client.filter.AnyOf)
  + [`Between`](srf_client.filter.html#srf_client.filter.Between)
  + [`Contains`](srf_client.filter.html#srf_client.filter.Contains)
  + [`Equals`](srf_client.filter.html#srf_client.filter.Equals)
  + [`Near`](srf_client.filter.html#srf_client.filter.Near)
  + [`Operator`](srf_client.filter.html#srf_client.filter.Operator)
  + [`Prefix`](srf_client.filter.html#srf_client.filter.Prefix)
  + [`any_of`](srf_client.filter.html#srf_client.filter.any_of)
  + [`between`](srf_client.filter.html#srf_client.filter.between)
  + [`contains`](srf_client.filter.html#srf_client.filter.contains)
  + [`eq`](srf_client.filter.html#srf_client.filter.eq)
  + [`near`](srf_client.filter.html#srf_client.filter.near)
  + [`prefix`](srf_client.filter.html#srf_client.filter.prefix)
* [srf\_client.fleets module](srf_client.fleets.html)
  + [`FleetEntriesClient`](srf_client.fleets.html#srf_client.fleets.FleetEntriesClient)
  + [`FleetsClient`](srf_client.fleets.html#srf_client.fleets.FleetsClient)
* [srf\_client.legs module](srf_client.legs.html)
  + [`LegsClient`](srf_client.legs.html#srf_client.legs.LegsClient)
* [srf\_client.locations module](srf_client.locations.html)
  + [`LocationsClient`](srf_client.locations.html#srf_client.locations.LocationsClient)
* [srf\_client.model module](srf_client.model.html)
  + [`BaseLocation`](srf_client.model.html#srf_client.model.BaseLocation)
  + [`Calibration`](srf_client.model.html#srf_client.model.Calibration)
  + [`Charger`](srf_client.model.html#srf_client.model.Charger)
  + [`ChargerMeter`](srf_client.model.html#srf_client.model.ChargerMeter)
  + [`ChargerStatus`](srf_client.model.html#srf_client.model.ChargerStatus)
  + [`ChargerTransaction`](srf_client.model.html#srf_client.model.ChargerTransaction)
  + [`DataType`](srf_client.model.html#srf_client.model.DataType)
  + [`ExternalLocation`](srf_client.model.html#srf_client.model.ExternalLocation)
  + [`ExternalVehicleClass`](srf_client.model.html#srf_client.model.ExternalVehicleClass)
  + [`FieldDef`](srf_client.model.html#srf_client.model.FieldDef)
  + [`Fleet`](srf_client.model.html#srf_client.model.Fleet)
  + [`FleetEntry`](srf_client.model.html#srf_client.model.FleetEntry)
  + [`Leg`](srf_client.model.html#srf_client.model.Leg)
  + [`Location`](srf_client.model.html#srf_client.model.Location)
  + [`Measurement`](srf_client.model.html#srf_client.model.Measurement)
  + [`Order`](srf_client.model.html#srf_client.model.Order)
  + [`Organisation`](srf_client.model.html#srf_client.model.Organisation)
  + [`Route`](srf_client.model.html#srf_client.model.Route)
  + [`Trailer`](srf_client.model.html#srf_client.model.Trailer)
  + [`Trial`](srf_client.model.html#srf_client.model.Trial)
  + [`Trip`](srf_client.model.html#srf_client.model.Trip)
  + [`Vehicle`](srf_client.model.html#srf_client.model.Vehicle)
  + [`VehicleClass`](srf_client.model.html#srf_client.model.VehicleClass)
* [srf\_client.oauth module](srf_client.oauth.html)
  + [Single-user CLI](srf_client.oauth.html#single-user-cli)
  + [Multi-user webapp](srf_client.oauth.html#multi-user-webapp)
  + [Client-only access](srf_client.oauth.html#client-only-access)
  + [`SRFDataOAuth`](srf_client.oauth.html#srf_client.oauth.SRFDataOAuth)
  + [`discover_urls()`](srf_client.oauth.html#srf_client.oauth.discover_urls)
  + [`make_urls()`](srf_client.oauth.html#srf_client.oauth.make_urls)
* [srf\_client.orders module](srf_client.orders.html)
  + [`OrdersClient`](srf_client.orders.html#srf_client.orders.OrdersClient)
* [srf\_client.organisations module](srf_client.organisations.html)
  + [`OrganisationsClient`](srf_client.organisations.html#srf_client.organisations.OrganisationsClient)
* [srf\_client.paging module](srf_client.paging.html)
  + [`Page`](srf_client.paging.html#srf_client.paging.Page)
  + [`PagingClient`](srf_client.paging.html#srf_client.paging.PagingClient)
  + [`paged_items()`](srf_client.paging.html#srf_client.paging.paged_items)
* [srf\_client.routes module](srf_client.routes.html)
  + [`RoutesClient`](srf_client.routes.html#srf_client.routes.RoutesClient)
* [srf\_client.sort module](srf_client.sort.html)
  + [`Ascending`](srf_client.sort.html#srf_client.sort.Ascending)
  + [`Descending`](srf_client.sort.html#srf_client.sort.Descending)
  + [`Sort`](srf_client.sort.html#srf_client.sort.Sort)
  + [`asc`](srf_client.sort.html#srf_client.sort.asc)
  + [`desc`](srf_client.sort.html#srf_client.sort.desc)
* [srf\_client.trailers module](srf_client.trailers.html)
  + [`TrailersClient`](srf_client.trailers.html#srf_client.trailers.TrailersClient)
* [srf\_client.transactions module](srf_client.transactions.html)
  + [`TransactionsClient`](srf_client.transactions.html#srf_client.transactions.TransactionsClient)
* [srf\_client.trials module](srf_client.trials.html)
  + [`TrialsClient`](srf_client.trials.html#srf_client.trials.TrialsClient)
* [srf\_client.trips module](srf_client.trips.html)
  + [`TripsClient`](srf_client.trips.html#srf_client.trips.TripsClient)
* [srf\_client.vehicle\_classes module](srf_client.vehicle_classes.html)
  + [`VehicleClassesClient`](srf_client.vehicle_classes.html#srf_client.vehicle_classes.VehicleClassesClient)
* [srf\_client.vehicles module](srf_client.vehicles.html)
  + [`VehiclesClient`](srf_client.vehicles.html#srf_client.vehicles.VehiclesClient)

<a id="srf_client-client"></a>

## srf_client.client.html

*Source: https://data.csrf.ac.uk/python/docs/srf_client.client.html*

# srf\_client.client module

Core HTTP client.

*class* ApiKeyAuth(*api\_key*)
:   Bases: `AuthBase`

*class* LogRetry(*\*args*, *\*\*kwargs*)
:   Bases: `Retry`

*class* SRFData(*root: str = 'https://data.csrf.ac.uk/api'*, *cache: Optional[BaseCache] = None*, *retries: Optional[Union[Retry, int]] = None*, *\*\*kwargs*)
:   Bases: `object`

    SRF Data client. Provides basic access to the REST API.

    Access to objects is via typed attributes.
    Most users should only need the `find_*` methods.

    Parameters:
    :   * **chargers** –

          Access to chargers API.

          New in version 2.1.
        * **fleets** – Access to fleets API.
        * **legs** – Access to legs API.
        * **locations** – Access to locations API.
        * **orders** – Access to orders API.
        * **organisations** – Access to organisations API.
        * **routes** – Access to routes API.
        * **trailers** – Access to trailers API.
        * **transactions** –

          Access to transactions API.

          New in version 2.1.
        * **trials** – Access to trials API.
        * **trips** – Access to trips API.
        * **vehicle\_classes** – Access to vehicles classes API.
        * **vehicles** – Access to vehicles API.

    Initialise a new instance.

    Parameters:
    :   * **api\_key** – Personal authentication token for the API
        * **root** – (optional) API root URL
        * **cache** – (optional) provide a cache implementation
        * **retries** –

          (optional) provide alternate retry logic

          New in version 2.5.

    Changed in version 2.3: By default no cache is configured, to avoid OOM issues or
    conflicts with other cache systems.

    *class* DataType(*type*, *description*, *fields*)
    :   Bases: `tuple`

        Create new instance of DataType(type, description, fields)

        description
        :   Alias for field number 1

        fields
        :   Alias for field number 2

        type
        :   Alias for field number 0

    get(*url*, *\*\*kwargs*) → Response
    :   Perform a raw GET request.

        Parameters:
        :   * **url** – Request URL. Will be resolved relative to the API root.
            * **kwargs** – Additional options for request

    get\_elevation(*points: Iterable[Point]*) → Iterable[Optional[float]]
    :   Lookup elevation for given points.

        Parameters:
        :   **points** – (latitude, longitude) points to query

        Returns:
        :   iterable of corresponding elevation in metres

    get\_types(*raw: bool = False*) → Mapping[str, [DataType](srf_client.model.html#srf_client.model.DataType "srf_client.model.DataType")]
    :   Get the `type` definitions for the `get_data` measurements.

        Parameters:
        :   **raw** – Return the types for `get_raw_data` instead..

    ping(*timeout=2*) → bool
    :   Check whether the service is reachable.

        May fail due to server-side errors, invalid authentication,
        or incorrect configuration.

        Parameters:
        :   **timeout** – Time in seconds to wait for a response.

    post(*url*, *\*\*kwargs*) → Response
    :   Perform a raw POST request. Probably requires write scope.

        Parameters:
        :   * **url** – Request URL. Will be resolved relative to the API root.
            * **kwargs** – Additional options for request

        New in version 1.4.

<a id="srf_client-oauth"></a>

## srf_client.oauth.html

*Source: https://data.csrf.ac.uk/python/docs/srf_client.oauth.html*

# srf\_client.oauth module

OAuth2-based client for more advanced applications.

See also

RFC 6749

## Single-user CLI

This method is suitable for testing or where indefinite authentication is
required, for example a long-running service.
In general, regular single-user applications should instead take the user’s
personal API key and use the simple client.

```
# Initialise client with basic defaults
from srf_client import *
srf = SRFDataOAuth(client_id='...', client_secret='...')

# Start a browser login session
import webbrowser
webbrowser.open_new_tab(srf.start_login())

# Receive auth code
code = input('Enter authorization code: ')
srf.login_with_code(code)

# Test connection
srf.ping()
```

## Multi-user webapp

Each user must use their own separate authenticated session.
This can be achieved with multiple client instances, or by switching the token
of a single instance before each request.

This is a basic flask example. A robust app will need more state and error
handling.

```
from flask import Flask, jsonify, redirect, request, session
from srf_client.oauth import *

app = Flask(__name__)
srf_config = {'client_id': '...',
              'client_secret': '...',
              'redirect_uri': 'https://example.com/oauth_callback'}

def save_oauth_token(token):
    session['oauth_token'] = token

def get_client():
    srf_client = SRFDataOAuth(save_token=save_oauth_token, **srf_config)
    if 'oauth_token' in session:
        srf_client.login_with_token(session['oauth_token'])
    return srf_client

@app.route('/login')
def login():
    return redirect(get_client().start_login())

@app.route('/oauth_callback')
def callback():
    get_client().login_with_callback(request.url)
    return redirect('/')

@app.route('/logout')
def logout():
    get_client().logout()
    session.pop('oauth_token')
    return redirect('/')

@app.route('/')
def index():
    return jsonify(get_client().ping())
```

## Client-only access

New in version 1.1.

Some APIs provide access to shared data and do not require user authorization.
If your app only uses these then configure a single scope of `CLIENT`.
Saving the token is not necessary, as a new one will be fetched whenever
needed.

```
from srf_client import *

srf = SRFDataOAuth(client_id='...', client_secret='...', scope=('CLIENT',))
srf.login_with_client()
srf.ping()
```

*class* SRFDataOAuth(*client\_id: str*, *client\_secret: str*, *scope: Sequence[str] = ('USER',)*, *redirect\_uri=None*, *save\_token: Optional[Callable[[Mapping], None]] = None*, *authorization\_endpoint='https://data.csrf.ac.uk/oauth/authorize'*, *token\_endpoint='https://data.csrf.ac.uk/oauth/token'*, *revocation\_endpoint='https://data.csrf.ac.uk/oauth/revoke'*, *introspection\_endpoint='https://data.csrf.ac.uk/oauth/check\_token'*, *\*\*kwargs*)
:   Bases: [`SRFData`](srf_client.client.html#srf_client.client.SRFData "srf_client.client.SRFData")

    SRF Data client. Provides OAuth2-based access to the REST API.

    Initialise a new instance.

    Parameters:
    :   * **client\_id** – Registered client ID
        * **client\_secret** – Registered client secret
        * **scope** – (optional) Request additional authorisation
        * **redirect\_uri** – (optional) Callback URL to receive auth result
        * **save\_token** – (optional) Callback function to save token state
          e.g. in a web session
        * **root** – (optional) API root URL
        * **authorization\_endpoint** – (optional) Override OAuth URL
        * **token\_endpoint** – (optional) Override OAuth URL
        * **revocation\_endpoint** – (optional) Override OAuth URL
        * **introspection\_endpoint** – (optional) Override OAuth URL

    Changed in version 2.2: Adjusted `*_endpoint` arg names to match RFC 8414 metadata.

    introspect() → Mapping[str, Any]
    :   Introspect the current auth state.

        New in version 2.2.

        See also

        RFC 7662

    *property* logged\_in*: bool*
    :   Whether the client is currently authenticated.

        Does not make a remote call to check for e.g. expiration.
        Use `ping()` for an active check.

    login\_with\_callback(*response\_callback: str*) → None
    :   Complete a login session using a received callback URL.

        Parameters:
        :   **response\_callback** – Full callback URL

    login\_with\_client() → None
    :   Login as a non-user client.

        New in version 1.1.

    login\_with\_code(*authorization\_code: str*) → None
    :   Complete a login session using a hand-entered code.

        Parameters:
        :   **authorization\_code** – User’s auth code

    login\_with\_token(*token: Mapping*) → None
    :   Restore auth state from a saved token.

        Parameters:
        :   **token** – object previously received via `save_token`

    logout() → None
    :   Invalidate the current auth state.

        Saved tokens will not be reusable.

        See also

        RFC 7009

    start\_login() → str
    :   Begin an interactive login session.

        Complete with either `login_with_callback` or `login_with_code`.

        Returns:
        :   The URL that the user should visit.

discover\_urls(*server\_root*)
:   Discover keyword arguments for a non-standard server root.

    New in version 2.2.

    See also

    RFC 8414

make\_urls(*server\_root*) → Mapping[str, str]
:   Build keyword arguments for a non-standard server root.

    Useful for testing:

    ```
    srf = SRFDataOAuth(client_id='TEST', client_secret='TEST',
                       **make_urls('https://localhost:8443')
    ```

    New in version 1.2.

    Changed in version 2.2: Mapping keys now align with RFC 8414.

<a id="srf_client-model"></a>

## srf_client.model.html

*Source: https://data.csrf.ac.uk/python/docs/srf_client.model.html*

# srf\_client.model module

Data model for the API.

Changed in version 2.6: Object equality is now defined by the *uri* property, where present.
More functions also return transparent smart proxies to avoid unnecessary
remote requests.

*class* BaseLocation
:   Bases: `ABC`

    A geographic location.

    New in version 2.7.

    *abstract property* name*: Optional[str]*
    :   Name for this location.

    *abstract property* point*: Optional[Point]*
    :   Coordinates of the location.

    *abstract property* post\_code*: Optional[str]*
    :   Location’s postal code.

*class* Calibration(*\**, *forward: tuple*, *left: tuple*, *up: tuple*, *inv\_gravity: tuple*)
:   Bases: `object`

    Leg calibration data for vehicle dynamics.

    Parameters:
    :   * **forward** – Unit vector pointing in the direction of forward travel
        * **left** – Lateral unit vector (forward × up)
        * **up** – Unit vector pointing against the action of gravity
        * **inv\_gravity** – Inverse gravitational acceleration in device’s basis

    Method generated by attrs for class Calibration.

*class* Charger(*\**, *uri: str*, *client: [SRFData](srf_client.client.html#srf_client.client.SRFData "srf_client.client.SRFData")*, *org\_uri: str*, *location\_uri: str*, *label: str*)
:   Bases: `UriObject`

    An electric vehicle charging station.

    Parameters:
    :   * **uri** – URI for this charger
        * **organisation** – Owning organisation
        * **location** – Location of the charger
        * **label** – Identity label of this charger

    New in version 2.1.

    Method generated by attrs for class Charger.

    get\_status(*\*\*kwargs*) → [Page](srf_client.paging.html#srf_client.paging.Page "srf_client.paging.Page")[[ChargerStatus](#srf_client.model.ChargerStatus "srf_client.model.ChargerStatus")]
    :   Fetch status for charger.

        Parameters:
        :   **kwargs** – Additional field filters

    get\_transactions(*lazy: bool = False*, *\*\*kwargs*) → [Page](srf_client.paging.html#srf_client.paging.Page "srf_client.paging.Page")[[ChargerTransaction](#srf_client.model.ChargerTransaction "srf_client.model.ChargerTransaction")]
    :   Fetch transactions for charger.

        Parameters:
        :   * **lazy** – Defer fetching of the ChargerTransaction objects
            * **kwargs** – Additional field filters

*class* ChargerMeter(*timestamp*, *value*)
:   Bases: `tuple`

    Create new instance of ChargerMeter(timestamp, value)

    timestamp
    :   Alias for field number 0

    value
    :   Alias for field number 1

*class* ChargerStatus(*connector*, *timestamp*, *status*, *error*, *message*)
:   Bases: `tuple`

    Create new instance of ChargerStatus(connector, timestamp, status, error, message)

    connector
    :   Alias for field number 0

    error
    :   Alias for field number 3

    message
    :   Alias for field number 4

    status
    :   Alias for field number 2

    timestamp
    :   Alias for field number 1

*class* ChargerTransaction(*\**, *uri: str*, *client: [SRFData](srf_client.client.html#srf_client.client.SRFData "srf_client.client.SRFData")*, *charger\_uri: str*, *vehicle\_uri: str*, *connector: str*, *start\_time: datetime*, *start\_meter: float*, *end\_time: Optional[datetime] = None*, *end\_meter: Optional[float] = None*)
:   Bases: `UriObject`

    An EV charging session.

    Parameters:
    :   * **uri** – URI for this transaction
        * **charger** – Charger for this transaction
        * **vehicle** – Vehicle for this transaction
        * **connector** – Charger connector ID
        * **start\_time** – When the charging session started
        * **end\_time** – When the charging session ended
        * **start\_meter** – Meter reading when charging started
        * **end\_meter** – Meter reading when charging ended

    New in version 2.1.

    Method generated by attrs for class ChargerTransaction.

    get\_data() → Iterable[[ChargerMeter](#srf_client.model.ChargerMeter "srf_client.model.ChargerMeter")]
    :   Fetch meter readings for transaction.

    get\_data\_frame() → pandas.DataFrame
    :   Return meter readings as a time-series `DataFrame`.

        New in version 2.1.

*class* DataType(*type*, *description*, *fields*)
:   Bases: `tuple`

    Create new instance of DataType(type, description, fields)

    description
    :   Alias for field number 1

    fields
    :   Alias for field number 2

    type
    :   Alias for field number 0

*class* ExternalLocation(*\**, *name: Optional[str] = None*, *post\_code: Optional[str] = None*, *point: Optional[Point] = None*)
:   Bases: [`BaseLocation`](#srf_client.model.BaseLocation "srf_client.model.BaseLocation")

    Location from an external lookup.

    New in version 2.7.

    Method generated by attrs for class ExternalLocation.

*class* ExternalVehicleClass(*\**, *description: Optional[str] = None*, *make: Optional[str] = None*, *model: Optional[str] = None*, *type: Optional[str] = None*, *fuel: Optional[str] = None*, *fuel\_capacity: Optional[float] = None*, *fuel\_efficiency: Optional[float] = None*, *weight\_class: Optional[float] = None*, *euro\_standard: Optional[int] = None*, *drive\_power: Optional[float] = None*, *fridge\_power: Optional[float] = None*)
:   Bases: `object`

    A specific make/model/configuration of vehicle from an external system.

    See [`VehicleClass`](#srf_client.model.VehicleClass "srf_client.model.VehicleClass").

    Method generated by attrs for class ExternalVehicleClass.

*class* FieldDef(*name*, *unit*)
:   Bases: `tuple`

    Create new instance of FieldDef(name, unit)

    name
    :   Alias for field number 0

    unit
    :   Alias for field number 1

*class* Fleet(*\**, *uri: str*, *client: [client.SRFData](srf_client.client.html#srf_client.client.SRFData "srf_client.client.SRFData")*, *org\_uri: str*, *name: str*, *entries: Sequence[[FleetEntry](#srf_client.model.FleetEntry "srf_client.model.FleetEntry")]*)
:   Bases: `UriObject`

    Set of vehicles available for operations.

    Parameters:
    :   * **uri** – URI for this fleet
        * **organisation** – Owning organisation
        * **name** – Name of this fleet
        * **entries** – Fleet composition

    Method generated by attrs for class Fleet.

*class* FleetEntry(*\**, *client: [SRFData](srf_client.client.html#srf_client.client.SRFData "srf_client.client.SRFData")*, *location\_uri: str*, *vehicle\_class\_uri: str*, *count: int*)
:   Bases: `object`

    Component of a fleet.

    Parameters:
    :   * **location** – Vehicle home location
        * **vehicle\_class** – Vehicle description
        * **count** – Number of vehicles of this type at this location

    Method generated by attrs for class FleetEntry.

*class* Leg(*\**, *uri: str*, *client: [SRFData](srf_client.client.html#srf_client.client.SRFData "srf_client.client.SRFData")*, *trip\_uri: str*, *start\_time: datetime*, *end\_time: datetime*, *types: frozenset = frozenset({})*, *start\_location: Optional[Point] = None*, *end\_location: Optional[Point] = None*, *start\_distance: Optional[Distance] = None*, *end\_distance: Optional[Distance] = None*, *consumption: Optional[float] = None*, *fuel\_level: Optional[float] = None*, *weight: Optional[int] = None*, *weight\_source: Optional[str] = None*, *destination: Optional[str] = None*)
:   Bases: `UriObject`

    A largely arbitrary section of a vehicle’s journey.

    The boundary conditions depend on the sources of the data.
    For example, `SRFLOGGER_V2` uses ignition on/off events, while
    `SRFLOGGER_V1` tracks the vehicle’s movement.

    Parameters:
    :   * **uri** – URI for this leg
        * **trip** – Parent trip
        * **start\_time** – First recorded timestamp
        * **end\_time** – Last recorded timestamp
        * **types** – Set of available data types
        * **start\_location** – Location at start of leg
        * **end\_location** – Location at end of leg
        * **start\_distance** – Odometer reading at start of leg
        * **end\_distance** – Odometer reading at end of leg
        * **consumption** – Fuel usage over the leg (litres)
        * **fuel\_level** – Fuel level at end of leg (percent)
        * **calibration** – Calibration data
        * **weight** – Gross vehicle weight during the leg (kilograms)
        * **weight\_source** – Source of the weight value

    Method generated by attrs for class Leg.

    get\_data(*include: Optional[Union[str, Collection]] = None*, *include\_can\_source: bool = False*, *min\_interval: Optional[timedelta] = None*) → Iterable[[Measurement](#srf_client.model.Measurement "srf_client.model.Measurement")]
    :   Return available measurements.

        Parameters:
        :   * **include** – Data types to include. By default, all are included.
            * **include\_can\_source** –

              Include additional field with CAN data.

              New in version 2.3.
            * **min\_interval** –

              Minimum interval between returned measurements
              in the same channel.

              New in version 2.8.

    get\_data\_frame(*data\_types: ~typing.Union[str, ~typing.Collection[str]], resolution: ~typing.Optional[~typing.Union[str, ~datetime.timedelta]] = None, conversion: ~typing.Optional[~typing.Callable[[str], ~typing.Any]] = <function to\_numeric>, include\_can\_source: ~typing.Optional[bool] = None*) → pandas.DataFrame
    :   Return available measurements as a time-series `DataFrame`.

        `Series` will be named `{TYPE}_{FIELD}` in the order given
        by `data_types`.

        Data will be interpolated to the specified resolution.

        Parameters:
        :   * **data\_types** – Data types to fetch.
            * **resolution** – Target resolution. If `None` (the default) then
              it will use the approximate resolution of the first requested type.
            * **conversion** – Conversion to apply to all values. If `None`
              then all values will be strings.
            * **include\_can\_source** – Include and partition by multiple CAN sources.

        Changed in version 2.3: Added `include_can_source` parameter.

    get\_gradient(*\*\*kwargs*) → Iterable[[Measurement](#srf_client.model.Measurement "srf_client.model.Measurement")]
    :   Return computed gradient data for the leg.

        Parameters:
        :   * **leg** – Parent leg object
            * **generate** – Request and wait for generation if not available
            * **timeout** – How long to wait if requesting generation

        New in version 1.4.

    get\_gradient\_frame(*\*\*kwargs*) → pandas.DataFrame
    :   Return computed gradient data as a time-series `DataFrame`.

        Parameters:
        :   * **generate** – Request and wait for generation if not available
            * **timeout** – How long to wait if requesting generation

        New in version 1.4.

    get\_raw\_data(*include: Optional[Union[str, Collection]] = None*) → Iterable[[Measurement](#srf_client.model.Measurement "srf_client.model.Measurement")]
    :   Return the raw measurements.

        Parameters:
        :   **include** – Data types to include. By default, all are included.

*class* Location(*\**, *uri: str*, *client: [SRFData](srf_client.client.html#srf_client.client.SRFData "srf_client.client.SRFData")*, *org\_uri: str*, *name: Optional[str] = None*, *post\_code: Optional[str] = None*, *point: Optional[Point] = None*)
:   Bases: `UriObject`, [`BaseLocation`](#srf_client.model.BaseLocation "srf_client.model.BaseLocation")

    Logistics location.

    Parameters:
    :   * **uri** – URI for this location
        * **organisation** – Owning organisation

    Method generated by attrs for class Location.

    get\_chargers(*lazy: bool = False*, *\*\*kwargs*) → [Page](srf_client.paging.html#srf_client.paging.Page "srf_client.paging.Page")[[Charger](#srf_client.model.Charger "srf_client.model.Charger")]
    :   Fetch chargers for location.

        Parameters:
        :   * **lazy** – Defer fetching of the Charger objects
            * **kwargs** – Additional field filters

        New in version 2.1.

    get\_routes(*lazy: bool = False*, *\*\*kwargs*) → [Page](srf_client.paging.html#srf_client.paging.Page "srf_client.paging.Page")[[Route](#srf_client.model.Route "srf_client.model.Route")]
    :   Fetch routes for location.

        Parameters:
        :   * **lazy** – Defer fetching of the Route objects
            * **kwargs** – Additional field filters

*class* Measurement(*timestamp*, *type*, *data*)
:   Bases: `tuple`

    Create new instance of Measurement(timestamp, type, data)

    data
    :   Alias for field number 2

    timestamp
    :   Alias for field number 0

    type
    :   Alias for field number 1

*class* Order(*\**, *uri: str*, *client: [SRFData](srf_client.client.html#srf_client.client.SRFData "srf_client.client.SRFData")*, *route\_uri: str*, *pickup: str*, *destination: str*, *time\_window\_start: Optional[datetime] = None*, *time\_window\_end: Optional[datetime] = None*, *pickup\_arrive: Optional[datetime] = None*, *pickup\_depart: Optional[datetime] = None*, *destination\_arrive: Optional[datetime] = None*, *destination\_depart: Optional[datetime] = None*, *distance: Optional[Distance] = None*, *ambient: Optional[float] = None*, *chilled: Optional[float] = None*, *frozen: Optional[float] = None*, *weight: Optional[float] = None*)
:   Bases: `UriObject`

    Transported cargo.

    Parameters:
    :   * **uri** – URI for this order
        * **route** – Route transporting this cargo
        * **pickup** – Postal code of pickup location
        * **destination** – Postal code of destination location
        * **time\_window\_start** – Start of the delivery window
        * **time\_window\_end** – End of the delivery window
        * **pickup\_arrive** – Arrival at pickup location
        * **pickup\_depart** – Departure from pickup location
        * **destination\_arrive** – Arrival at destination
        * **destination\_depart** – Departure from destination
        * **distance** – Distance travelled for delivery
        * **ambient** – Number of ambient units
        * **chilled** – Number of chilled units
        * **frozen** – Number of frozen units
        * **weight** – Weight of order (kilograms)

    Method generated by attrs for class Order.

*class* Organisation(*\**, *uri: str*, *client: [SRFData](srf_client.client.html#srf_client.client.SRFData "srf_client.client.SRFData")*, *name: str*)
:   Bases: `UriObject`

    An affiliated or former organisation.

    Parameters:
    :   * **uri** – URI for this organisation
        * **name** – Name of the organisation

    Method generated by attrs for class Organisation.

    get\_chargers(*lazy: bool = False*) → [Page](srf_client.paging.html#srf_client.paging.Page "srf_client.paging.Page")[[Charger](#srf_client.model.Charger "srf_client.model.Charger")]
    :   Fetch chargers for organisation.

        Parameters:
        :   **lazy** – Defer fetching of the Charger objects

        New in version 2.1.

    get\_fleets(*lazy: bool = False*) → [Page](srf_client.paging.html#srf_client.paging.Page "srf_client.paging.Page")[[Fleet](#srf_client.model.Fleet "srf_client.model.Fleet")]
    :   Fetch fleets for organisation.

        Parameters:
        :   **lazy** – Defer fetching of the Fleet objects

    get\_routes(*lazy: bool = False*) → [Page](srf_client.paging.html#srf_client.paging.Page "srf_client.paging.Page")[[Route](#srf_client.model.Route "srf_client.model.Route")]
    :   Fetch routes for organisation.

        Parameters:
        :   **lazy** – Defer fetching of the Route objects

    get\_trailers(*lazy: bool = False*) → [Page](srf_client.paging.html#srf_client.paging.Page "srf_client.paging.Page")[[Trailer](#srf_client.model.Trailer "srf_client.model.Trailer")]
    :   Fetch trailers for organisation.

        Parameters:
        :   **lazy** – Defer fetching of the Trailer objects

    get\_trials(*lazy: bool = False*) → [Page](srf_client.paging.html#srf_client.paging.Page "srf_client.paging.Page")[[Trial](#srf_client.model.Trial "srf_client.model.Trial")]
    :   Fetch trials for organisation.

        Parameters:
        :   **lazy** – Defer fetching of the Trial objects

    get\_vehicle\_classes(*lazy: bool = False*) → [Page](srf_client.paging.html#srf_client.paging.Page "srf_client.paging.Page")[[VehicleClass](#srf_client.model.VehicleClass "srf_client.model.VehicleClass")]
    :   Fetch vehicle classes for organisation.

        Parameters:
        :   **lazy** – Defer fetching of the VehicleClass objects

    get\_vehicles(*lazy: bool = False*) → [Page](srf_client.paging.html#srf_client.paging.Page "srf_client.paging.Page")[[Vehicle](#srf_client.model.Vehicle "srf_client.model.Vehicle")]
    :   Fetch vehicles for organisation.

        Parameters:
        :   **lazy** – Defer fetching of the Vehicle objects

*class* Route(*\**, *uri: str*, *client: [SRFData](srf_client.client.html#srf_client.client.SRFData "srf_client.client.SRFData")*, *org\_uri: str*, *start\_location\_uri: str*, *end\_location\_uri: str*, *depot\_uri: str*, *vehicle\_class\_uri: str*, *plan: bool*, *start\_time: datetime*, *end\_time: datetime*, *distance: Optional[Distance] = None*, *shift\_start: Optional[datetime] = None*, *shift\_end: Optional[datetime] = None*, *registration: Optional[str] = None*, *orders: int = 0*, *total\_units: Optional[float] = None*, *total\_weight: Optional[float] = None*)
:   Bases: `UriObject`

    A logistics operation route, planned or completed.

    Parameters:
    :   * **uri** – URI for this route
        * **organisation** – Owning organisation
        * **start\_location** – Start of the route
        * **end\_location** – End of the route
        * **depot** – Operational base location
        * **vehicle\_class** – Type of vehicle used
        * **plan** – Whether this route describes a planned or an actual route
        * **start\_time** – Start time
        * **end\_time** – End time
        * **distance** – Total distance travelled
        * **shift\_start** – Start of driver’s shift
        * **shift\_end** – End of driver’s shift
        * **registration** – Specific vehicle that was used
        * **orders** – Total number of orders involved
        * **total\_units** – Total number of units moved
        * **total\_weight** – Total weight of goods moved (kilograms)

    Method generated by attrs for class Route.

    get\_orders(*lazy: bool = False*, *\*\*kwargs*) → [Page](srf_client.paging.html#srf_client.paging.Page "srf_client.paging.Page")[[Order](#srf_client.model.Order "srf_client.model.Order")]
    :   Fetch orders for route.

        Parameters:
        :   * **lazy** – Defer fetching of the Order objects
            * **kwargs** – Additional field filters

*class* Trailer(*\**, *uri: str*, *client: [SRFData](srf_client.client.html#srf_client.client.SRFData "srf_client.client.SRFData")*, *org\_uri: str*, *serial: str*, *length: Optional[float] = None*, *make: Optional[str] = None*, *model: Optional[str] = None*, *type: Optional[str] = None*, *axles: Optional[int] = None*, *tires\_per\_axle: Optional[int] = None*, *description: Optional[str] = None*)
:   Bases: `UriObject`

    A towed vehicle or container.

    Parameters:
    :   * **uri** – URI for this trailer
        * **serial** – Trailer serial number
        * **length** – Length of trailer chassis (m)
        * **make** – Trailer manufacturer
        * **model** – Manufacturer’s model designation
        * **type** – Trailer classification (e.g. `SINGLE`, `HIGH`, `DOUBLE`,
          `TEARDROP`, `LONG`, `SLOPED`, `TANK`)
        * **axles** – Number of axles
        * **tires\_per\_axle** – Number of tires per axle
        * **description** – Additional description/notes

    Method generated by attrs for class Trailer.

    get\_trips(*lazy: bool = False*, *\*\*kwargs*) → [Page](srf_client.paging.html#srf_client.paging.Page "srf_client.paging.Page")[[Trip](#srf_client.model.Trip "srf_client.model.Trip")]
    :   Fetch trips for trailer.

        Parameters:
        :   * **lazy** – Defer fetching of the Trip objects
            * **kwargs** – Additional field filters

*class* Trial(*\**, *uri: str*, *client: [SRFData](srf_client.client.html#srf_client.client.SRFData "srf_client.client.SRFData")*, *org\_uri: str*, *description: str*, *active: bool*)
:   Bases: `UriObject`

    A specific project investigation.

    Parameters:
    :   * **uri** – URI for this trial
        * **description** – Description of the trial
        * **active** – Whether data collection is ongoing

    Method generated by attrs for class Trial.

    get\_trips(*lazy: bool = False*, *\*\*kwargs*) → [Page](srf_client.paging.html#srf_client.paging.Page "srf_client.paging.Page")[[Trip](#srf_client.model.Trip "srf_client.model.Trip")]
    :   Fetch trips for trial.

        Parameters:
        :   * **lazy** – Defer fetching of the Trip objects
            * **kwargs** – Additional field filters

*class* Trip(*\**, *uri: str*, *client: [SRFData](srf_client.client.html#srf_client.client.SRFData "srf_client.client.SRFData")*, *trailer\_uri: str*, *trial\_uri: str*, *vehicle\_uri: str*, *source: str*, *types: frozenset = frozenset({})*, *start\_time: Optional[datetime] = None*, *end\_time: Optional[datetime] = None*, *consumption: Optional[float] = None*, *distance: Optional[Distance] = None*)
:   Bases: `UriObject`

    A single journey.

    Can be defined manually, or as all the legs that begin on a particular day.

    Parameters:
    :   * **uri** – URI for this trip
        * **source** – System that recorded the trip data
        * **types** – Set of available data types
        * **start\_time** – First recorded timestamp
        * **end\_time** – Last recorded timestamp
        * **consumption** – Fuel usage over the trip (litres)
        * **distance** – Distanced travelled over the trip

    Method generated by attrs for class Trip.

    get\_data(*include: Optional[Union[str, Collection]] = None*, *include\_can\_source: bool = False*, *min\_interval: Optional[timedelta] = None*) → Iterable[[Measurement](#srf_client.model.Measurement "srf_client.model.Measurement")]
    :   Return available measurements.

        Parameters:
        :   * **include** – Data types to include. By default all are included.
            * **include\_can\_source** –

              Include additional field with CAN data.

              New in version 2.3.
            * **min\_interval** –

              Minimum interval between returned measurements
              in the same channel.

              New in version 2.8.

    get\_data\_frame(*data\_types: ~typing.Union[str, ~typing.Collection[str]], resolution: ~typing.Optional[~typing.Union[str, ~datetime.timedelta]] = None, conversion: ~typing.Optional[~typing.Callable[[str], ~typing.Any]] = <function to\_numeric>, include\_can\_source: ~typing.Optional[bool] = None*) → pandas.DataFrame
    :   Return available measurements as a time-series `DataFrame`.

        `Series` will be named `{TYPE}_{FIELD}` in the order given
        by `data_types`.

        Data will be interpolated to the specified resolution.

        Parameters:
        :   * **data\_types** – Data types to fetch.
            * **resolution** – Target resolution. If `None` (the default) then
              it will use the approximate resolution of the first requested type.
            * **conversion** – Conversion to apply to all values. If `None`
              then all values will be strings.
            * **include\_can\_source** – Include and partition by multiple CAN sources.

        Changed in version 2.3: Added `include_can_source` parameter.

    get\_legs(*lazy: bool = False*, *\*\*kwargs*) → [Page](srf_client.paging.html#srf_client.paging.Page "srf_client.paging.Page")[[Leg](#srf_client.model.Leg "srf_client.model.Leg")]
    :   Fetch legs for trip.

        Parameters:
        :   * **lazy** – Defer fetching of the Leg objects
            * **kwargs** – Additional field filters

*class* Vehicle(*\**, *uri: str*, *client: [SRFData](srf_client.client.html#srf_client.client.SRFData "srf_client.client.SRFData")*, *org\_uri: str*, *registration: Optional[str] = None*, *vin: Optional[str] = None*, *calibrated: bool = False*, *make: Optional[str] = None*, *model: Optional[str] = None*, *type: Optional[str] = None*, *fuel: Optional[str] = None*, *weight\_class: Optional[float] = None*, *euro\_standard: Optional[int] = None*, *description: Optional[str] = None*, *outfit\_weight: Optional[int] = None*, *country: Optional[str] = None*)
:   Bases: `UriObject`

    A motor vehicle.

    Parameters:
    :   * **uri** – URI for this vehicle
        * **registration** – Vehicle registration (number plate)
        * **vin** – Vehicle identification number (ISO 3779)
        * **calibrated** – Whether the app was calibrated on installation.
          If missing then data types 11 and 12 are in an arbitrary basis.
        * **make** – Vehicle manufacturer
        * **model** – Manufacturer’s model designation
        * **type** – Vehicle classification (e.g. `RIGID`, `ARTIC`, `VAN`,
          `BUS`, `CAR`)
        * **fuel** – Fuel type (e.g. `DIESEL`, `PETROL`, `CNG`, `LNG`,
          `H2`, `ELECTRIC`)
        * **weight\_class** – Max weight class (tonnes)
        * **euro\_standard** – European emission standard
        * **description** – Additional description/notes
        * **outfit\_weight** –

          Unloaded weight in standard configuration

          New in version 1.2.
        * **country** –

          Registration country (ISO 3166-1 alpha-2)

          New in version 1.6.

    Method generated by attrs for class Vehicle.

    get\_transactions(*lazy: bool = False*, *\*\*kwargs*) → [Page](srf_client.paging.html#srf_client.paging.Page "srf_client.paging.Page")[[ChargerTransaction](#srf_client.model.ChargerTransaction "srf_client.model.ChargerTransaction")]
    :   Fetch charging transactions for vehicle.

        Parameters:
        :   * **lazy** – Defer fetching of the ChargerTransaction objects
            * **kwargs** – Additional field filters

        New in version 2.1.

    get\_trips(*lazy: bool = False*, *\*\*kwargs*) → [Page](srf_client.paging.html#srf_client.paging.Page "srf_client.paging.Page")[[Trip](#srf_client.model.Trip "srf_client.model.Trip")]
    :   Fetch trips for vehicle.

        Parameters:
        :   * **lazy** – Defer fetching of the Trip objects
            * **kwargs** – Additional field filters

*class* VehicleClass(*\**, *uri: str*, *client: [SRFData](srf_client.client.html#srf_client.client.SRFData "srf_client.client.SRFData")*, *org\_uri: str*, *description: Optional[str] = None*, *make: Optional[str] = None*, *model: Optional[str] = None*, *type: Optional[str] = None*, *fuel: Optional[str] = None*, *fuel\_capacity: Optional[float] = None*, *fuel\_efficiency: Optional[float] = None*, *weight\_class: Optional[float] = None*, *euro\_standard: Optional[int] = None*, *drive\_power: Optional[float] = None*, *fridge\_power: Optional[float] = None*, *limits: Mapping[str, float] = immutabledict({})*)
:   Bases: `UriObject`

    A specific make/model/configuration of road vehicle.

    Parameters:
    :   * **uri** – URI for this vehicle class
        * **organisation** – Owning organisation
        * **description** – Additional description/notes
        * **make** – Vehicle manufacturer
        * **model** – Manufacturer’s model designation
        * **type** – Vehicle classification (e.g. `RIGID`, `ARTIC`, `VAN`,
          `BUS`, `CAR`)
        * **fuel** – Fuel type (e.g. `DIESEL`, `PETROL`, `CNG`, `LNG`,
          `H2`, `ELECTRIC`)
        * **fuel\_capacity** – Full fuel capacity (L or kg or kWh)
        * **fuel\_efficiency** – Fuel usage over distance (L/km or kg/km or kWh/km)
        * **weight\_class** – Max weight class (tonnes)
        * **euro\_standard** – European emission standard
        * **drive\_power** – Power output of the drive system (kilowatts)
        * **fridge\_power** – Power output of the cargo cooling system (kilowatts)
        * **limits** – Various numeric limits for constraint problems

    Method generated by attrs for class VehicleClass.

    get\_routes(*lazy: bool = False*, *\*\*kwargs*) → [Page](srf_client.paging.html#srf_client.paging.Page "srf_client.paging.Page")[[Route](#srf_client.model.Route "srf_client.model.Route")]
    :   Fetch routes for vehicle class.

        Parameters:
        :   * **lazy** – Defer fetching of the Route objects
            * **kwargs** – Additional field filters

<a id="srf_client-filter"></a>

## srf_client.filter.html

*Source: https://data.csrf.ac.uk/python/docs/srf_client.filter.html*

# srf\_client.filter module

Use with listing methods to filter the results.

> ```
> srf.trips.find_all(distance=between(0, 50))
> ```

Related entities can be traversed, which requires using dict syntax:

> ```
> srf.trips.find_all(**{'vehicle.make': eq('Scania')})
> ```

Warning

Using unsupported operators for a field type will give unexpected
results.

*class* AnyOf(*\*args: [Operator](#srf_client.filter.Operator "srf_client.filter.Operator")*)
:   Bases: [`Operator`](#srf_client.filter.Operator "srf_client.filter.Operator")

    String field matches any of these operators.

*class* Between(*v1: Any*, *v2: Any*)
:   Bases: [`Operator`](#srf_client.filter.Operator "srf_client.filter.Operator")

    Field is between two values (inclusive).

*class* Contains(*\*values: Any*)
:   Bases: [`Operator`](#srf_client.filter.Operator "srf_client.filter.Operator")

    Array field contains value(s).

*class* Equals(*value: Any*)
:   Bases: [`Operator`](#srf_client.filter.Operator "srf_client.filter.Operator")

    Field equals value.

*class* Near(*point: Point*, *distance: Distance*)
:   Bases: [`Operator`](#srf_client.filter.Operator "srf_client.filter.Operator")

    Point is within region centred on point.

*class* Operator(*\*values: str*)
:   Bases: `ABC`

*class* Prefix(*value: Union[str, bytes]*)
:   Bases: [`Operator`](#srf_client.filter.Operator "srf_client.filter.Operator")

    String field starts with value.

any\_of
:   alias of [`AnyOf`](#srf_client.filter.AnyOf "srf_client.filter.AnyOf")

between
:   alias of [`Between`](#srf_client.filter.Between "srf_client.filter.Between")

contains
:   alias of [`Contains`](#srf_client.filter.Contains "srf_client.filter.Contains")

eq
:   alias of [`Equals`](#srf_client.filter.Equals "srf_client.filter.Equals")

near
:   alias of [`Near`](#srf_client.filter.Near "srf_client.filter.Near")

prefix
:   alias of [`Prefix`](#srf_client.filter.Prefix "srf_client.filter.Prefix")

<a id="srf_client-sort"></a>

## srf_client.sort.html

*Source: https://data.csrf.ac.uk/python/docs/srf_client.sort.html*

# srf\_client.sort module

Can be passed with field filters to control the sort order.

> ```
> srf.organisations.find_all(sort=asc('name'))
> ```

*class* Ascending(*field: str*)
:   Bases: [`Sort`](#srf_client.sort.Sort "srf_client.sort.Sort")

    Ascending sort order.

    Parameters:
    :   **field** – Field to sort by

*class* Descending(*field: str*)
:   Bases: [`Sort`](#srf_client.sort.Sort "srf_client.sort.Sort")

    Descending sort order.

    Parameters:
    :   **field** – Field to sort by

*class* Sort(*field: str*, *direction: str*)
:   Bases: `ABC`

asc
:   alias of [`Ascending`](#srf_client.sort.Ascending "srf_client.sort.Ascending")

desc
:   alias of [`Descending`](#srf_client.sort.Descending "srf_client.sort.Descending")

<a id="srf_client-paging"></a>

## srf_client.paging.html

*Source: https://data.csrf.ac.uk/python/docs/srf_client.paging.html*

# srf\_client.paging module

*class* Page(*\**, *client: [PagingClient](#srf_client.paging.PagingClient "srf_client.paging.PagingClient")[T]*, *items: Sequence[T]*, *total: int*, *first: str*, *last: str*, *next: Optional[str] = None*, *prev: Optional[str] = None*)
:   Bases: `Generic`[`T`], `Iterable`[`T`], `Sized`

    A page of results.

    Parameters:
    :   * **items** – Sequence of result items
        * **total** – Total number of available items
        * **first** – First page of results
        * **last** – Last page of results
        * **next** – Next page of results
        * **prev** – Previous page of results

    Changed in version 2.4: Now supports the `Iterable` and `Sized` interfaces.

    Method generated by attrs for class Page.

*class* PagingClient(*client*, *fragment*)
:   Bases: `Generic`[`T`], `ABC`

    Base class for paging support.

    Parameters:
    :   **page\_size** – the default page size

    Construct base class.

    Parameters:
    :   * **client** – root SRFData client
        * **fragment** – URI path fragment

    find\_by(*parent*, *lazy=False*, *\*\*kwargs*) → [Page](#srf_client.paging.Page "srf_client.paging.Page")[T]
    :   Get a page of child objects.

        Parameters:
        :   * **parent** – Parent object of any related type
            * **lazy** – Defer fetching of the T objects
            * **kwargs** – Additional field filters

        Changed in version 2.1: Pulled up from subclasses.

    get(*\**, *uri=None*, *obj\_id=None*) → Optional[T]
    :   Get a single object by its URI or ID.

        In general IDs are not exposed to clients.
        The `find_*` methods should be used instead.

    get\_page(*uri*, *params=None*) → [Page](#srf_client.paging.Page "srf_client.paging.Page")[T]
    :   Get a page of objects.

        In general this method should not be used directly.
        Access is via `find_*` methods and attributes of `Page`.

paged\_items(*page: [Page](#srf_client.paging.Page "srf_client.paging.Page")[T]*) → Iterable[T]
:   Iterate over all items in all further pages.

    Parameters:
    :   **page** – Page to start from

<a id="srf_client-vehicles"></a>

## srf_client.vehicles.html

*Source: https://data.csrf.ac.uk/python/docs/srf_client.vehicles.html*

# srf\_client.vehicles module

*class* VehiclesClient(*client*)
:   Bases: [`PagingClient`](srf_client.paging.html#srf_client.paging.PagingClient "srf_client.paging.PagingClient")[[`Vehicle`](srf_client.model.html#srf_client.model.Vehicle "srf_client.model.Vehicle")]

    Access to vehicles API.

    Acquire an instance via `SRFData.vehicles`.

    Construct base class.

    Parameters:
    :   * **client** – root SRFData client
        * **fragment** – URI path fragment

    find\_all(*lazy=False*, *\*\*kwargs*) → [Page](srf_client.paging.html#srf_client.paging.Page "srf_client.paging.Page")[[Vehicle](srf_client.model.html#srf_client.model.Vehicle "srf_client.model.Vehicle")]
    :   Find all known vehicles.

        Parameters:
        :   * **lazy** – Defer fetching of the Vehicle objects
            * **kwargs** – Additional field filters

    get(*\**, *uri=None*, *obj\_id=None*) → Optional[[Vehicle](srf_client.model.html#srf_client.model.Vehicle "srf_client.model.Vehicle")]
    :   Get a single vehicle by its URI or unique identifier.

        Parameters:
        :   * **uri** – Uniform resource locator
            * **obj\_id** – Vehicle registration, VIN, or internal ID.

<a id="srf_client-vehicle_classes"></a>

## srf_client.vehicle_classes.html

*Source: https://data.csrf.ac.uk/python/docs/srf_client.vehicle_classes.html*

# srf\_client.vehicle\_classes module

*class* VehicleClassesClient(*client*)
:   Bases: [`PagingClient`](srf_client.paging.html#srf_client.paging.PagingClient "srf_client.paging.PagingClient")[[`VehicleClass`](srf_client.model.html#srf_client.model.VehicleClass "srf_client.model.VehicleClass")]

    Access to VehicleClass API.

    Acquire an instance via `SRFData.vehicle_classes`.

    Construct base class.

    Parameters:
    :   * **client** – root SRFData client
        * **fragment** – URI path fragment

    find\_all(*lazy=False*, *\*\*kwargs*) → [Page](srf_client.paging.html#srf_client.paging.Page "srf_client.paging.Page")[[VehicleClass](srf_client.model.html#srf_client.model.VehicleClass "srf_client.model.VehicleClass")]
    :   Find all known vehicle\_classes.

        Parameters:
        :   * **lazy** – Defer fetching of the VehicleClass objects
            * **kwargs** – Additional field filters

    lookup(*registration: str*) → Optional[[ExternalVehicleClass](srf_client.model.html#srf_client.model.ExternalVehicleClass "srf_client.model.ExternalVehicleClass")]
    :   Lookup vehicle details from an external system, e.g. the DVLA.

        Parameters:
        :   **registration** – Vehicle registration to find

<a id="srf_client-fleets"></a>

## srf_client.fleets.html

*Source: https://data.csrf.ac.uk/python/docs/srf_client.fleets.html*

# srf\_client.fleets module

*class* FleetEntriesClient(*client*)
:   Bases: [`PagingClient`](srf_client.paging.html#srf_client.paging.PagingClient "srf_client.paging.PagingClient")[[`FleetEntry`](srf_client.model.html#srf_client.model.FleetEntry "srf_client.model.FleetEntry")]

    Internal access to Fleet Entries API.

    Construct base class.

    Parameters:
    :   * **client** – root SRFData client
        * **fragment** – URI path fragment

    find\_by\_fleet(*fleet\_uri: str*) → [Page](srf_client.paging.html#srf_client.paging.Page "srf_client.paging.Page")[[FleetEntry](srf_client.model.html#srf_client.model.FleetEntry "srf_client.model.FleetEntry")]
    :   Get fleet composition entries.

        Parameters:
        :   **fleet\_uri** – Fleet to enumerate

*class* FleetsClient(*client*)
:   Bases: [`PagingClient`](srf_client.paging.html#srf_client.paging.PagingClient "srf_client.paging.PagingClient")[[`Fleet`](srf_client.model.html#srf_client.model.Fleet "srf_client.model.Fleet")]

    Access to Fleets API.

    Acquire an instance via `SRFData.fleets`.

    Construct base class.

    Parameters:
    :   * **client** – root SRFData client
        * **fragment** – URI path fragment

    find\_all(*lazy=False*, *\*\*kwargs*) → [Page](srf_client.paging.html#srf_client.paging.Page "srf_client.paging.Page")[[Fleet](srf_client.model.html#srf_client.model.Fleet "srf_client.model.Fleet")]
    :   Find all known fleets.

        Parameters:
        :   * **lazy** – Defer fetching of the Fleet objects
            * **kwargs** – Additional field filters

<a id="srf_client-legs"></a>

## srf_client.legs.html

*Source: https://data.csrf.ac.uk/python/docs/srf_client.legs.html*

# srf\_client.legs module

*class* LegsClient(*client*)
:   Bases: [`PagingClient`](srf_client.paging.html#srf_client.paging.PagingClient "srf_client.paging.PagingClient")[[`Leg`](srf_client.model.html#srf_client.model.Leg "srf_client.model.Leg")]

    Access to legs API.

    Acquire an instance via `SRFData.trips`.

    Construct base class.

    Parameters:
    :   * **client** – root SRFData client
        * **fragment** – URI path fragment

    find\_all(*lazy=False*, *\*\*kwargs*) → [Page](srf_client.paging.html#srf_client.paging.Page "srf_client.paging.Page")[[Leg](srf_client.model.html#srf_client.model.Leg "srf_client.model.Leg")]
    :   Find all recorded legs.

        Parameters:
        :   * **lazy** – Defer fetching of the Leg objects
            * **kwargs** – Additional field filters

    find\_by\_trip(*trip: [Trip](srf_client.model.html#srf_client.model.Trip "srf_client.model.Trip")*, *lazy=False*, *\*\*kwargs*) → [Page](srf_client.paging.html#srf_client.paging.Page "srf_client.paging.Page")[[Leg](srf_client.model.html#srf_client.model.Leg "srf_client.model.Leg")]
    :   Find all legs for the given trip.

        Parameters:
        :   * **trip** – Parent trip object
            * **lazy** – Defer fetching of the Leg objects
            * **kwargs** – Additional field filters

    get\_calibration(*leg: [Leg](srf_client.model.html#srf_client.model.Leg "srf_client.model.Leg")*) → [Calibration](srf_client.model.html#srf_client.model.Calibration "srf_client.model.Calibration")
    :   Return the raw calibration data for a given leg.

    get\_data(*leg: [Leg](srf_client.model.html#srf_client.model.Leg "srf_client.model.Leg")*, *include: Optional[Union[str, Collection]] = None*, *include\_can\_source: bool = False*, *min\_interval: Optional[timedelta] = None*) → Iterable[[Measurement](srf_client.model.html#srf_client.model.Measurement "srf_client.model.Measurement")]
    :   Return available measurements.

        Parameters:
        :   * **leg** – Parent leg object
            * **include** – Data types to include. By default, all are included.
            * **include\_can\_source** –

              Include additional field with CAN data.

              New in version 2.3.
            * **min\_interval** –

              Minimum interval between returned measurements
              in the same channel.

              New in version 2.8.

    get\_gradient(*leg: [Leg](srf_client.model.html#srf_client.model.Leg "srf_client.model.Leg")*, *generate: bool = False*, *timeout: timedelta = datetime.timedelta(seconds=300)*) → Iterable[[Measurement](srf_client.model.html#srf_client.model.Measurement "srf_client.model.Measurement")]
    :   Return computed gradient data for the leg.

        Parameters:
        :   * **leg** – Parent leg object
            * **generate** – Request and wait for generation if not available
            * **timeout** – How long to wait if requesting generation

        New in version 1.4.

    get\_raw\_data(*leg: [Leg](srf_client.model.html#srf_client.model.Leg "srf_client.model.Leg")*, *include: Optional[Union[str, Collection]] = None*) → Iterable[str]
    :   Return the raw data. Format depends on source.

        Parameters:
        :   * **leg** – Parent leg object
            * **include** – Data types to include. By default, all are included.

<a id="srf_client-trips"></a>

## srf_client.trips.html

*Source: https://data.csrf.ac.uk/python/docs/srf_client.trips.html*

# srf\_client.trips module

*class* TripsClient(*client*)
:   Bases: [`PagingClient`](srf_client.paging.html#srf_client.paging.PagingClient "srf_client.paging.PagingClient")[[`Trip`](srf_client.model.html#srf_client.model.Trip "srf_client.model.Trip")]

    Access to trips API.

    Acquire an instance via `SRFData.trips`.

    Construct base class.

    Parameters:
    :   * **client** – root SRFData client
        * **fragment** – URI path fragment

    find\_all(*lazy=False*, *\*\*kwargs*) → [Page](srf_client.paging.html#srf_client.paging.Page "srf_client.paging.Page")[[Trip](srf_client.model.html#srf_client.model.Trip "srf_client.model.Trip")]
    :   Find all recorded trips.

        Parameters:
        :   * **lazy** – Defer fetching of the Trip objects
            * **kwargs** – Additional field filters

    find\_by\_trailer(*trailer: [Trailer](srf_client.model.html#srf_client.model.Trailer "srf_client.model.Trailer")*, *lazy=False*, *\*\*kwargs*) → [Page](srf_client.paging.html#srf_client.paging.Page "srf_client.paging.Page")[[Trip](srf_client.model.html#srf_client.model.Trip "srf_client.model.Trip")]
    :   Find all trips for the given trailer.

        Parameters:
        :   * **trailer** – Parent trailer object
            * **lazy** – Defer fetching of the Trip objects
            * **kwargs** – Additional field filters

    find\_by\_trial(*trial: [Trial](srf_client.model.html#srf_client.model.Trial "srf_client.model.Trial")*, *lazy=False*, *\*\*kwargs*) → [Page](srf_client.paging.html#srf_client.paging.Page "srf_client.paging.Page")[[Trip](srf_client.model.html#srf_client.model.Trip "srf_client.model.Trip")]
    :   Find all trips for the given trial.

        Parameters:
        :   * **trial** – Parent trial object
            * **lazy** – Defer fetching of the Trip objects
            * **kwargs** – Additional field filters

    find\_by\_vehicle(*vehicle: [Vehicle](srf_client.model.html#srf_client.model.Vehicle "srf_client.model.Vehicle")*, *lazy=False*, *\*\*kwargs*) → [Page](srf_client.paging.html#srf_client.paging.Page "srf_client.paging.Page")[[Trip](srf_client.model.html#srf_client.model.Trip "srf_client.model.Trip")]
    :   Find all trips for the given vehicle.

        Parameters:
        :   * **vehicle** – Parent vehicle object
            * **lazy** – Defer fetching of the Trip objects
            * **kwargs** – Additional field filters

<a id="srf_client-trials"></a>

## srf_client.trials.html

*Source: https://data.csrf.ac.uk/python/docs/srf_client.trials.html*

# srf\_client.trials module

*class* TrialsClient(*client*)
:   Bases: [`PagingClient`](srf_client.paging.html#srf_client.paging.PagingClient "srf_client.paging.PagingClient")[[`Trial`](srf_client.model.html#srf_client.model.Trial "srf_client.model.Trial")]

    Access to Trials API.

    Acquire an instance via `SRFData.trials`.

    Construct base class.

    Parameters:
    :   * **client** – root SRFData client
        * **fragment** – URI path fragment

    find\_all(*lazy=False*, *\*\*kwargs*) → [Page](srf_client.paging.html#srf_client.paging.Page "srf_client.paging.Page")[[Trial](srf_client.model.html#srf_client.model.Trial "srf_client.model.Trial")]
    :   Find all known trials.

        Parameters:
        :   * **lazy** – Defer fetching of the Trial objects
            * **kwargs** – Additional field filters

<a id="srf_client-routes"></a>

## srf_client.routes.html

*Source: https://data.csrf.ac.uk/python/docs/srf_client.routes.html*

# srf\_client.routes module

*class* RoutesClient(*client*)
:   Bases: [`PagingClient`](srf_client.paging.html#srf_client.paging.PagingClient "srf_client.paging.PagingClient")[[`Route`](srf_client.model.html#srf_client.model.Route "srf_client.model.Route")]

    Access to Routes API.

    Acquire an instance via `SRFData.routes`.

    Construct base class.

    Parameters:
    :   * **client** – root SRFData client
        * **fragment** – URI path fragment

    find\_all(*lazy=False*, *\*\*kwargs*) → [Page](srf_client.paging.html#srf_client.paging.Page "srf_client.paging.Page")[[Route](srf_client.model.html#srf_client.model.Route "srf_client.model.Route")]
    :   Find all known routes.

        Parameters:
        :   * **lazy** – Defer fetching of the Route objects
            * **kwargs** – Additional field filters

    find\_by\_location(*location: [Location](srf_client.model.html#srf_client.model.Location "srf_client.model.Location")*, *lazy=False*, *\*\*kwargs*) → [Page](srf_client.paging.html#srf_client.paging.Page "srf_client.paging.Page")[[Route](srf_client.model.html#srf_client.model.Route "srf_client.model.Route")]
    :   Find all routes involving the given location.

        Parameters:
        :   * **location** – Parent location object
            * **lazy** – Defer fetching of the Route objects
            * **kwargs** – Additional field filters

    find\_by\_vehicle\_class(*vehicle\_class: [VehicleClass](srf_client.model.html#srf_client.model.VehicleClass "srf_client.model.VehicleClass")*, *lazy=False*, *\*\*kwargs*) → [Page](srf_client.paging.html#srf_client.paging.Page "srf_client.paging.Page")[[Route](srf_client.model.html#srf_client.model.Route "srf_client.model.Route")]
    :   Find all routes using the given vehicle class.

        Parameters:
        :   * **vehicle\_class** – Parent vehicle class object
            * **lazy** – Defer fetching of the Route objects
            * **kwargs** – Additional field filters

<a id="srf_client-locations"></a>

## srf_client.locations.html

*Source: https://data.csrf.ac.uk/python/docs/srf_client.locations.html*

# srf\_client.locations module

*class* LocationsClient(*client*)
:   Bases: [`PagingClient`](srf_client.paging.html#srf_client.paging.PagingClient "srf_client.paging.PagingClient")[[`Location`](srf_client.model.html#srf_client.model.Location "srf_client.model.Location")]

    Access to Locations API.

    Acquire an instance via `SRFData.locations`.

    Construct base class.

    Parameters:
    :   * **client** – root SRFData client
        * **fragment** – URI path fragment

    find\_all(*lazy=False*, *\*\*kwargs*) → [Page](srf_client.paging.html#srf_client.paging.Page "srf_client.paging.Page")[[Location](srf_client.model.html#srf_client.model.Location "srf_client.model.Location")]
    :   Find all known locations.

        Parameters:
        :   * **lazy** – Defer fetching of the Location objects
            * **kwargs** – Additional field filters

    lookup(*point: Point*) → Optional[[ExternalLocation](srf_client.model.html#srf_client.model.ExternalLocation "srf_client.model.ExternalLocation")]
    :   Lookup location details from an external system, e.g. the ONS.

        Parameters:
        :   **point** – (latitude, longitude) point to query

        Returns:
        :   details of nearest postcode, if found

        New in version 2.7.

<a id="srf_client-transactions"></a>

## srf_client.transactions.html

*Source: https://data.csrf.ac.uk/python/docs/srf_client.transactions.html*

# srf\_client.transactions module

*class* TransactionsClient(*client*)
:   Bases: [`PagingClient`](srf_client.paging.html#srf_client.paging.PagingClient "srf_client.paging.PagingClient")[[`ChargerTransaction`](srf_client.model.html#srf_client.model.ChargerTransaction "srf_client.model.ChargerTransaction")]

    Access to transactions API.

    Acquire an instance via `SRFData.transactions`.

    New in version 2.1.

    Construct base class.

    Parameters:
    :   * **client** – root SRFData client
        * **fragment** – URI path fragment

    find\_all(*lazy=False*, *\*\*kwargs*) → [Page](srf_client.paging.html#srf_client.paging.Page "srf_client.paging.Page")[[ChargerTransaction](srf_client.model.html#srf_client.model.ChargerTransaction "srf_client.model.ChargerTransaction")]
    :   Find all recorded charging transactions.

        Parameters:
        :   * **lazy** – Defer fetching of the ChargerTransaction objects
            * **kwargs** – Additional field filters

    find\_by\_charger(*charger: [Charger](srf_client.model.html#srf_client.model.Charger "srf_client.model.Charger")*, *lazy=False*, *\*\*kwargs*) → [Page](srf_client.paging.html#srf_client.paging.Page "srf_client.paging.Page")[[ChargerTransaction](srf_client.model.html#srf_client.model.ChargerTransaction "srf_client.model.ChargerTransaction")]
    :   Find all transactions for the given charger.

        Parameters:
        :   * **charger** – Parent charger object
            * **lazy** – Defer fetching of the ChargerTransaction objects
            * **kwargs** – Additional field filters

    find\_by\_vehicle(*vehicle: [Vehicle](srf_client.model.html#srf_client.model.Vehicle "srf_client.model.Vehicle")*, *lazy=False*, *\*\*kwargs*) → [Page](srf_client.paging.html#srf_client.paging.Page "srf_client.paging.Page")[[ChargerTransaction](srf_client.model.html#srf_client.model.ChargerTransaction "srf_client.model.ChargerTransaction")]
    :   Find all transactions for the given vehicle.

        Parameters:
        :   * **vehicle** – Parent vehicle object
            * **lazy** – Defer fetching of the ChargerTransaction objects
            * **kwargs** – Additional field filters

    get\_data(*transaction: [ChargerTransaction](srf_client.model.html#srf_client.model.ChargerTransaction "srf_client.model.ChargerTransaction")*) → Iterable[[ChargerMeter](srf_client.model.html#srf_client.model.ChargerMeter "srf_client.model.ChargerMeter")]
    :   Fetch meter readings for transaction.

        Parameters:
        :   **transaction** – Parent transaction object

<a id="srf_client-chargers"></a>

## srf_client.chargers.html

*Source: https://data.csrf.ac.uk/python/docs/srf_client.chargers.html*

# srf\_client.chargers module

*class* ChargersClient(*client*)
:   Bases: [`PagingClient`](srf_client.paging.html#srf_client.paging.PagingClient "srf_client.paging.PagingClient")[[`Charger`](srf_client.model.html#srf_client.model.Charger "srf_client.model.Charger")]

    Access to chargers API.

    Acquire an instance via `SRFData.chargers`.

    New in version 2.1.

    Construct base class.

    Parameters:
    :   * **client** – root SRFData client
        * **fragment** – URI path fragment

    find\_all(*lazy=False*, *\*\*kwargs*) → [Page](srf_client.paging.html#srf_client.paging.Page "srf_client.paging.Page")[[Charger](srf_client.model.html#srf_client.model.Charger "srf_client.model.Charger")]
    :   Find all known chargers.

        Parameters:
        :   * **lazy** – Defer fetching of the Charger objects
            * **kwargs** – Additional field filters

    find\_by\_location(*location: [Location](srf_client.model.html#srf_client.model.Location "srf_client.model.Location")*, *lazy=False*, *\*\*kwargs*) → [Page](srf_client.paging.html#srf_client.paging.Page "srf_client.paging.Page")[[Charger](srf_client.model.html#srf_client.model.Charger "srf_client.model.Charger")]
    :   Find all chargers at the given location.

        Parameters:
        :   * **location** – Parent location object
            * **lazy** – Defer fetching of the Trip objects
            * **kwargs** – Additional field filters

    find\_status(*charger: [Charger](srf_client.model.html#srf_client.model.Charger "srf_client.model.Charger")*, *\*\*kwargs*) → [Page](srf_client.paging.html#srf_client.paging.Page "srf_client.paging.Page")[[ChargerStatus](srf_client.model.html#srf_client.model.ChargerStatus "srf_client.model.ChargerStatus")]
    :   Get charger status.

        Parameters:
        :   * **charger** – Charger to query
            * **kwargs** – Additional field filters

<a id="srf_client-orders"></a>

## srf_client.orders.html

*Source: https://data.csrf.ac.uk/python/docs/srf_client.orders.html*

# srf\_client.orders module

*class* OrdersClient(*client*)
:   Bases: [`PagingClient`](srf_client.paging.html#srf_client.paging.PagingClient "srf_client.paging.PagingClient")[[`Order`](srf_client.model.html#srf_client.model.Order "srf_client.model.Order")]

    Access to Orders API.

    Acquire an instance via `SRFData.orders`.

    Construct base class.

    Parameters:
    :   * **client** – root SRFData client
        * **fragment** – URI path fragment

    find\_all(*lazy=False*, *\*\*kwargs*) → [Page](srf_client.paging.html#srf_client.paging.Page "srf_client.paging.Page")[[Order](srf_client.model.html#srf_client.model.Order "srf_client.model.Order")]
    :   Find all known orders.

        Parameters:
        :   * **lazy** – Defer fetching of the Order objects
            * **kwargs** – Additional field filters

    find\_by\_route(*route: [Route](srf_client.model.html#srf_client.model.Route "srf_client.model.Route")*, *lazy=False*, *\*\*kwargs*) → [Page](srf_client.paging.html#srf_client.paging.Page "srf_client.paging.Page")[[Order](srf_client.model.html#srf_client.model.Order "srf_client.model.Order")]
    :   Find all orders for the given route.

        Parameters:
        :   * **route** – Parent route object
            * **lazy** – Defer fetching of the Leg objects
            * **kwargs** – Additional field filters

<a id="srf_client-trailers"></a>

## srf_client.trailers.html

*Source: https://data.csrf.ac.uk/python/docs/srf_client.trailers.html*

# srf\_client.trailers module

*class* TrailersClient(*client*)
:   Bases: [`PagingClient`](srf_client.paging.html#srf_client.paging.PagingClient "srf_client.paging.PagingClient")[[`Trailer`](srf_client.model.html#srf_client.model.Trailer "srf_client.model.Trailer")]

    Access to trailers API.

    Acquire an instance via `SRFData.trailers`.

    Construct base class.

    Parameters:
    :   * **client** – root SRFData client
        * **fragment** – URI path fragment

    find\_all(*lazy=False*, *\*\*kwargs*) → [Page](srf_client.paging.html#srf_client.paging.Page "srf_client.paging.Page")[[Trailer](srf_client.model.html#srf_client.model.Trailer "srf_client.model.Trailer")]
    :   Find all known trailers.

        Parameters:
        :   * **lazy** – Defer fetching of the Vehicle objects
            * **kwargs** – Additional field filters

<a id="srf_client-organisations"></a>

## srf_client.organisations.html

*Source: https://data.csrf.ac.uk/python/docs/srf_client.organisations.html*

# srf\_client.organisations module

*class* OrganisationsClient(*client*)
:   Bases: [`PagingClient`](srf_client.paging.html#srf_client.paging.PagingClient "srf_client.paging.PagingClient")[[`Organisation`](srf_client.model.html#srf_client.model.Organisation "srf_client.model.Organisation")]

    Access to Organisations API.

    Acquire an instance via `SRFData.organisations`.

    Construct base class.

    Parameters:
    :   * **client** – root SRFData client
        * **fragment** – URI path fragment

    find\_all(*lazy=False*, *\*\*kwargs*) → [Page](srf_client.paging.html#srf_client.paging.Page "srf_client.paging.Page")[[Organisation](srf_client.model.html#srf_client.model.Organisation "srf_client.model.Organisation")]
    :   Find all known organisations.

        Parameters:
        :   * **lazy** – Defer fetching of the Organisation objects
            * **kwargs** – Additional field filters
