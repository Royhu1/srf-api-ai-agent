# AGENTS.md

**Role: tool** · Tier: shared · Status: active

This repository is the `srf-data` agent skill for the SRF data platform
(https://data.csrf.ac.uk). The skill lives in `.claude/skills/srf-data/` and is
the single source for every agent: Claude Code loads it from there; Codex and
other agents should read `.claude/skills/srf-data/SKILL.md` before answering any
question about SRF/CSRF data, vehicle telemetry, charging or elevation, and run
its scripts from `.claude/skills/srf-data/scripts/`.

- Install for other projects or user-wide: `python tools/install_skill.py`
  (Claude `~/.claude/skills/`, Codex `~/.codex/skills/`; `--project DIR` for one project).
- The API key comes from `SRF_API_KEY` or `.env` (see `.env.example`). Never print,
  log or commit it.
- `references/platform_api.md` is a local transcription of login-only
  documentation and is gitignored: never commit it or quote it at length in
  committed files.
- Everything committed is in British English; commit messages follow
  Conventional Commits.
- Run the end-to-end test with `.venv/Scripts/python.exe tests/test_skill_e2e.py`.
