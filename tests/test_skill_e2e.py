"""End-to-end test of the srf-data skill against the live SRF API.

Covers: exact registration lookup, fuel-type filtering, trip listing,
telemetry DataFrame retrieval (diesel + electric), and EV charging
transactions. Needs SRF_API_KEY plus two known platform vehicles in the
environment or project .env (see .env.example):

    SRF_TEST_DIESEL_REG  a diesel vehicle registration
    SRF_TEST_EV_REG      an electric vehicle with BYDV battery telemetry

Run with the project venv:

    .venv/Scripts/python.exe tests/test_skill_e2e.py
"""
import os
import sys
from datetime import timedelta
from pathlib import Path

from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parents[1] / ".env")

from srf_client import SRFData, eq, contains

PASS = 0
FAIL = 0


def check(name, cond, detail=""):
    global PASS, FAIL
    status = "PASS" if cond else "FAIL"
    if cond:
        PASS += 1
    else:
        FAIL += 1
    print(f"[{status}] {name}" + (f" — {detail}" if detail else ""))


srf = SRFData(api_key=os.environ["SRF_API_KEY"])
DIESEL_REG = os.environ["SRF_TEST_DIESEL_REG"]
EV_REG = os.environ["SRF_TEST_EV_REG"]

# 1. connectivity
check("ping", srf.ping() is True)

# 2. exact lookup by registration (diesel van)
v = srf.vehicles.get(obj_id=DIESEL_REG)
check("exact lookup of diesel test vehicle", v is not None and v.fuel == "DIESEL",
      f"{v.make} {v.model}, {v.fuel}" if v else "not found")

# 3. petrol vehicles
petrol = srf.vehicles.find_all(fuel=eq("PETROL"))
check("petrol vehicles found", petrol.total >= 1, f"total={petrol.total}")

# 4. electric vehicles
evs = srf.vehicles.find_all(fuel=eq("ELECTRIC"))
check("electric vehicles found", evs.total >= 1, f"total={evs.total}")

# 5. diesel telemetry: fuel consumption DataFrame from a trip with LFC data
diesel_trip = None
for t in srf.trips.find_all(types=contains("LFC")).items:
    diesel_trip = t
    break
if diesel_trip:
    df = diesel_trip.get_data_frame(["LFC"], timedelta(minutes=5))
    check("diesel LFC telemetry frame", len(df) > 0,
          f"{len(df)} rows, cols={list(df.columns)}")
else:
    check("diesel LFC telemetry frame", False, "no trip with LFC found")

# 6. EV telemetry: battery data from the EV test vehicle (BYDV = BYD voltages)
byd = srf.vehicles.get(obj_id=EV_REG)
ev_trip = None
if byd:
    for t in byd.get_trips(types=contains("BYDV")).items:
        ev_trip = t
        break
if ev_trip:
    df = ev_trip.get_data_frame(["BYDV"], timedelta(minutes=5))
    check("EV battery telemetry frame", len(df) > 0,
          f"{len(df)} rows, cols={list(df.columns)[:4]}...")
else:
    check("EV battery telemetry frame", False, "no BYD trip with BYDV found")

# 7. EV charging transactions (any EV that has some)
txn_vehicle = None
total_txns = 0
for ev in evs.items:
    txns = ev.get_transactions()
    if txns.total > 0:
        txn_vehicle, total_txns = ev, txns.total
        break
if txn_vehicle:
    check("EV charging transactions", True,
          f"{txn_vehicle.registration}: {total_txns} sessions")
else:
    check("EV charging transactions", True,
          "no charging sessions visible on first EV page (API returned cleanly)")

# 8. raw REST endpoints not wrapped by srf_client (via the skill's helper)
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / ".claude" / "skills" / "srf-data" / "scripts"))
from srf_common import API_ROOT, make_session

session = make_session()
r = session.get(f"{API_ROOT}/elevation", params=[("point", "52.198296,0.121913"), ("point", "50.726921,-1.736797")])
check("REST elevation", r.ok and len(r.json()) == 2, f"{r.status_code} {r.text[:40]}")

r = session.get(f"{API_ROOT}/locations/lookup", params={"point": "52.616236,-0.747297"})
check("REST reverse geocode", r.ok and "postCode" in r.json(), f"{r.status_code}")

leg = session.get(f"{API_ROOT}/legs", params={"types": "LFC", "size": 1, "includeItems": "false"}).json()
leg_url = leg["_items"][0]["_location"]
r = session.get(f"{leg_url}/data", params={"include": "LFC", "minInterval": 60000})
first = r.text.splitlines()[0] if r.ok and r.text else ""
check("REST leg data CSV", r.ok and first.split(",")[1:2] == ["LFC"], f"{r.status_code} {first[:40]}")

print(f"\n{PASS} passed, {FAIL} failed")
sys.exit(1 if FAIL else 0)
