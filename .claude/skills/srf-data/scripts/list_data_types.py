"""List the SRF measurement data-type codes used by get_data()/get_data_frame().

Usage (run with the project venv python):
    list_data_types.py                 # all type codes
    list_data_types.py --search fuel   # types whose code/description matches
    list_data_types.py --raw           # types for get_raw_data() instead

Prints JSON: {code: {description, fields: [{name, unit}]}}
"""
import argparse
import json
import sys

from srf_common import make_client

sys.stdout.reconfigure(encoding="utf-8", errors="replace")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--search", help="case-insensitive substring filter on code/description/fields")
    ap.add_argument("--raw", action="store_true", help="list get_raw_data() types instead")
    args = ap.parse_args()

    srf = make_client()
    types = srf.get_types(raw=args.raw)

    out = {}
    for code, dt in sorted(types.items()):
        blob = f"{code} {dt.description} " + " ".join(f.name for f in dt.fields)
        if args.search and args.search.lower() not in blob.lower():
            continue
        out[code] = {
            "description": dt.description,
            "fields": [{"name": f.name, "unit": f.unit} for f in dt.fields],
        }

    json.dump(out, sys.stdout, indent=2, ensure_ascii=False)
    print()


if __name__ == "__main__":
    main()
