"""Look up vehicles on the SRF data platform.

Usage (run with the project venv python):
    vehicle_lookup.py --reg "AB12 CDE"            # single vehicle by registration/VIN
    vehicle_lookup.py --fuel ELECTRIC --limit 5   # filter by fuel type
    vehicle_lookup.py --make Volvo --type ARTIC   # filter by make and/or type
    vehicle_lookup.py --reg "AB12 CDE" --trips    # include recent trips
    vehicle_lookup.py --reg "AB12 CDE" --dvla     # external (DVLA) class lookup

Prints JSON to stdout.
"""
import argparse
import json
import os
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")


def make_client():
    try:
        from dotenv import load_dotenv
        # project root = three levels above this scripts/ dir
        load_dotenv(Path(__file__).resolve().parents[3] / ".env")
        load_dotenv()  # also pick up a .env in the CWD, if any
    except ImportError:
        pass
    api_key = os.environ.get("SRF_API_KEY")
    if not api_key:
        sys.exit("SRF_API_KEY not set (expected in environment or project .env)")
    from srf_client import SRFData
    return SRFData(api_key=api_key)


def vehicle_dict(v):
    return {
        "uri": v.uri,
        "registration": v.registration,
        "vin": v.vin,
        "make": v.make,
        "model": v.model,
        "type": v.type,
        "fuel": v.fuel,
        "weight_class_t": v.weight_class,
        "euro_standard": v.euro_standard,
        "outfit_weight_kg": v.outfit_weight,
        "country": v.country,
        "calibrated": v.calibrated,
        "description": v.description,
    }


def trip_dict(t):
    return {
        "uri": t.uri,
        "source": t.source,
        "start_time": str(t.start_time) if t.start_time else None,
        "end_time": str(t.end_time) if t.end_time else None,
        "distance": str(t.distance) if t.distance else None,
        "consumption_l": t.consumption,
        "data_types": sorted(t.types),
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--reg", help="registration, VIN or internal ID (exact lookup)")
    ap.add_argument("--fuel", help="DIESEL|PETROL|CNG|LNG|H2|ELECTRIC")
    ap.add_argument("--make", help="manufacturer, e.g. Volvo")
    ap.add_argument("--type", dest="vtype", help="RIGID|ARTIC|VAN|BUS|CAR")
    ap.add_argument("--limit", type=int, default=10, help="max vehicles to return")
    ap.add_argument("--trips", action="store_true", help="include up to 5 recent trips per vehicle")
    ap.add_argument("--dvla", action="store_true", help="also query external (DVLA) vehicle class lookup")
    args = ap.parse_args()

    srf = make_client()
    out = {"query": {k: v for k, v in vars(args).items() if v}, "vehicles": []}

    if args.reg:
        v = srf.vehicles.get(obj_id=args.reg)
        vehicles = [v] if v else []
        if not v:
            out["note"] = f"no vehicle found for {args.reg!r}"
    else:
        from srf_client import eq
        filters = {}
        if args.fuel:
            filters["fuel"] = eq(args.fuel.upper())
        if args.make:
            filters["make"] = eq(args.make)
        if args.vtype:
            filters["type"] = eq(args.vtype.upper())
        page = srf.vehicles.find_all(**filters)
        out["total_matching"] = page.total
        vehicles = list(page.items)[: args.limit]

    for v in vehicles:
        d = vehicle_dict(v)
        if args.trips:
            trips = v.get_trips()
            d["total_trips"] = trips.total
            d["recent_trips"] = [trip_dict(t) for t in list(trips.items)[:5]]
        if args.dvla and v.registration:
            ext = srf.vehicle_classes.lookup(v.registration)
            d["dvla_lookup"] = (
                {
                    "make": ext.make, "model": ext.model, "type": ext.type,
                    "fuel": ext.fuel, "fuel_capacity": ext.fuel_capacity,
                    "fuel_efficiency": ext.fuel_efficiency,
                    "weight_class": ext.weight_class,
                    "euro_standard": ext.euro_standard,
                    "description": ext.description,
                }
                if ext else None
            )
        out["vehicles"].append(d)

    json.dump(out, sys.stdout, indent=2, ensure_ascii=False)
    print()


if __name__ == "__main__":
    main()
