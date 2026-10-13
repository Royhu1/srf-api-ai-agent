**Role: tool** · Tier: shared · Status: active

# srf-api-ai-agent

A [Claude Code](https://claude.com/claude-code) skill, `srf-data`, that lets Claude query the
[SRF data platform](https://data.csrf.ac.uk) (Centre for Sustainable Road Freight) through the
official Python client [`srf-client`](https://pypi.org/project/srf-client/): vehicles, trips, legs,
telemetry (fuel, speed, GPS, CAN data), EV chargers and charging transactions, routes, fleets and more.

You need your own SRF platform API key. None is included in this repository.

## Install

1. Copy the skill into a project (`<project>/.claude/skills/`) or into your user-level
   skills (`~/.claude/skills/`):

   ```bash
   cp -r .claude/skills/srf-data <target>/.claude/skills/
   ```

   Alternatively, download `srf-data.skill` from the Releases page and unzip it there.

2. Install the dependencies in the Python environment Claude will use:

   ```bash
   pip install -r requirements.txt
   ```

3. Provide the key, either as the environment variable `SRF_API_KEY` or in a `.env` file
   at the project root (see `.env.example`).

Restart Claude Code. The skill triggers on questions about SRF/CSRF data, vehicle telemetry,
fuel or energy consumption, or EV charging.

## Contents

| Path | Purpose |
|---|---|
| `.claude/skills/srf-data/SKILL.md` | Skill instructions: setup, data model, query patterns, pitfalls |
| `.claude/skills/srf-data/scripts/vehicle_lookup.py` | Vehicle lookup by registration/VIN or by fuel, make and type |
| `.claude/skills/srf-data/scripts/list_data_types.py` | Lists telemetry type codes for `get_data()` |
| `.claude/skills/srf-data/references/api_reference.md` | Full `srf-client` API reference |
| `tests/test_skill_e2e.py` | End-to-end test against the live API (needs a key and two test vehicles) |

## Attribution

`references/api_reference.md` reproduces the `srf-client` documentation
(<https://data.csrf.ac.uk/python/docs>), © James Howe, MIT License.

## Licence

MIT. See `LICENSE`.
