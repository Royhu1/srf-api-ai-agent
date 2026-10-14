"""Shared helpers for the srf-data skill scripts: API key loading and clients.

The key is read from the SRF_API_KEY environment variable, else from the
nearest .env found by walking up from the current directory (the project
root, wherever the skill itself is installed: .claude/skills, ~/.codex/skills).
"""
import os
import sys

API_ROOT = "https://data.csrf.ac.uk/api"


def load_api_key():
    if not os.environ.get("SRF_API_KEY"):
        try:
            from dotenv import find_dotenv, load_dotenv
            load_dotenv(find_dotenv(usecwd=True))
        except ImportError:
            pass
    api_key = os.environ.get("SRF_API_KEY")
    if not api_key:
        sys.exit("SRF_API_KEY not set (expected in environment or a project .env)")
    return api_key


def make_client():
    """srf_client.SRFData instance (high-level, typed access)."""
    from srf_client import SRFData
    return SRFData(api_key=load_api_key())


def make_session():
    """requests.Session with the Bearer token set (raw REST access)."""
    import requests
    session = requests.Session()
    session.headers["Authorization"] = "Bearer " + load_api_key()
    session.headers["Accept"] = "application/json, text/csv;q=0.9, */*;q=0.8"
    return session
