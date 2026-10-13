**Role: tool** · Tier: shared · Status: active

# srf-api-ai-agent

An agent skill, `srf-data`, for [Claude Code](https://claude.com/claude-code) and
[Codex](https://developers.openai.com/codex) that lets the agent query the
[SRF data platform](https://data.csrf.ac.uk) (Centre for Sustainable Road Freight), both through the
official Python client [`srf-client`](https://pypi.org/project/srf-client/) and through the platform's
REST API directly: vehicles, trips, legs, telemetry (fuel, speed, GPS, CAN data), road gradient,
land elevation, reverse geocoding, EV chargers, charger status and charging transactions, routes,
fleets and more.

You need your own SRF platform API key. None is included in this repository.

## Install

1. Install the skill. From a clone of this repository:

   ```bash
   python tools/install_skill.py
   ```

   This copies `.claude/skills/srf-data` to `~/.claude/skills/` (Claude Code) and
   `~/.codex/skills/` (Codex). Use `--agent claude` or `--agent codex` for one of them, or
   `--project <dir>` to install into a single project instead (`<dir>/.claude/skills/` and
   `<dir>/.agents/skills/`). Alternatively, download `srf-data.skill` from the Releases page and
   unzip it into one of those folders.

2. Install the dependencies in the Python environment the agent will use:

   ```bash
   pip install -r requirements.txt
   ```

3. Provide the key, either as the environment variable `SRF_API_KEY` or in a `.env` file
   at the project root (see `.env.example`).

Start a new Claude Code or Codex session. The skill triggers on questions about SRF/CSRF data,
vehicle telemetry, fuel or energy consumption, EV charging, or elevation and gradient; it can
also be invoked explicitly (`/srf-data` in Claude Code, `$srf-data` in Codex).

## Contents

| Path | Purpose |
|---|---|
| `.claude/skills/srf-data/SKILL.md` | Skill instructions: setup, data model, client patterns, REST endpoints and filters, pitfalls |
| `.claude/skills/srf-data/scripts/vehicle_lookup.py` | Vehicle lookup by registration/VIN or by fuel, make and type |
| `.claude/skills/srf-data/scripts/list_data_types.py` | Lists telemetry type codes for `get_data()` |
| `.claude/skills/srf-data/scripts/api_request.py` | Raw call to any REST endpoint (JSON or CSV, paging, POST) |
| `.claude/skills/srf-data/scripts/srf_common.py` | Shared key loading and client/session construction |
| `.claude/skills/srf-data/references/api_reference.md` | Full `srf-client` API reference |
| `tools/install_skill.py` | Installs the skill for Claude Code and/or Codex |
| `tests/test_skill_e2e.py` | End-to-end test against the live API (needs a key and two test vehicles) |
| `AGENTS.md` | Instructions for Codex and other agents working in this repository |

The platform's own REST API documentation is only available after login, so it is not
redistributed here. The skill summarises the endpoints in its own words; if you have access, a
local transcription saved as `.claude/skills/srf-data/references/platform_api.md` is picked up
by the skill and ignored by git.

## Attribution

`references/api_reference.md` reproduces the `srf-client` documentation
(<https://data.csrf.ac.uk/python/docs>), © James Howe, MIT License.

## Licence

MIT. See `LICENSE`.
