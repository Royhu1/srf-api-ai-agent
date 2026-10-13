"""Raw request against the SRF platform REST API (https://data.csrf.ac.uk/api).

Use for endpoints srf_client does not wrap (leg data options, gradient,
elevation, reverse geocoding, charger status ...), or to see the exact JSON.
CSV endpoints (legs/{id}/data, legs/{id}/raw, legs/{id}/gradient,
transactions/{id}/data) are printed as text; use --out to save them.

Usage (run with the project venv python):
    api_request.py vehicles size=5 fuel=ELECTRIC
    api_request.py vehicles --all --max-items 200       # follow _next links
    api_request.py https://data.csrf.ac.uk/api/legs/123  # absolute URLs work too
    api_request.py legs/123/data include=2 include=LFC --out leg123.csv
    api_request.py elevation point=52.2,0.12 point=51.5,-0.1 --post   # many points

Give the path without a leading slash: Git Bash on Windows rewrites "/x" into
a filesystem path. Parameters are key=value pairs passed as query parameters
(repeat a key to send it twice). Prints JSON to stdout; for --all, a single
object {"_total": n, "_items": [...]} merged across pages.
"""
import argparse
import json
import sys
from pathlib import Path

from srf_common import API_ROOT, make_session

sys.stdout.reconfigure(encoding="utf-8", errors="replace")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("path", help="path under /api without a leading slash (e.g. vehicles/123; Git Bash rewrites /paths) or an absolute URL")
    ap.add_argument("params", nargs="*", help="query parameters as key=value")
    ap.add_argument("--all", action="store_true", help="follow _next links and merge _items")
    ap.add_argument("--max-items", type=int, default=1000, help="stop --all after this many items")
    ap.add_argument("--post", action="store_true", help="send the parameters as a POST form body (e.g. large elevation queries)")
    ap.add_argument("--out", help="write the response body to this file instead of stdout")
    args = ap.parse_args()

    url = args.path if args.path.startswith("http") else API_ROOT + "/" + args.path.lstrip("/")
    params = [tuple(p.split("=", 1)) for p in args.params]
    session = make_session()

    if args.post:
        response = session.post(url, data=params, timeout=300)
    else:
        response = session.get(url, params=params, timeout=300)
    if not response.ok:
        sys.exit(f"HTTP {response.status_code} for {response.url}\n{response.text[:2000]}")

    if "json" not in response.headers.get("Content-Type", ""):
        if args.out:
            Path(args.out).write_bytes(response.content)
            print(f"wrote {len(response.content)} bytes to {args.out}")
        else:
            sys.stdout.write(response.text)
        return
    body = response.json()

    if args.all and isinstance(body, dict) and "_items" in body:
        items = list(body["_items"])
        next_url = body.get("_next")
        while next_url and len(items) < args.max_items:
            page = session.get(next_url, timeout=120)
            page.raise_for_status()
            page_body = page.json()
            items.extend(page_body.get("_items", []))
            next_url = page_body.get("_next")
        body = {"_total": body.get("_total"), "_items": items[: args.max_items]}

    if args.out:
        Path(args.out).write_text(json.dumps(body, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"wrote JSON to {args.out}")
    else:
        json.dump(body, sys.stdout, indent=2, ensure_ascii=False)
        print()


if __name__ == "__main__":
    main()
