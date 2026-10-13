"""Install the srf-data skill for Claude Code and/or Codex.

The repository keeps one copy of the skill (.claude/skills/srf-data); this
script copies it to where each agent looks for skills:

    user level (all projects)   Claude: ~/.claude/skills/   Codex: ~/.codex/skills/
    project level (--project)   Claude: <dir>/.claude/skills/   Codex: <dir>/.agents/skills/

Usage:
    python tools/install_skill.py                          # both agents, user level
    python tools/install_skill.py --agent codex
    python tools/install_skill.py --project D:/path/to/other-project

An existing installed copy is replaced. Files that exist only locally (such as
the gitignored platform API reference) are copied too.
"""
import argparse
import shutil
from pathlib import Path

SKILL_NAME = "srf-data"
SOURCE_DIR = Path(__file__).resolve().parents[1] / ".claude" / "skills" / SKILL_NAME


def target_dirs(agent, project):
    if project:
        base = Path(project).resolve()
        roots = {"claude": base / ".claude" / "skills", "codex": base / ".agents" / "skills"}
    else:
        home = Path.home()
        roots = {"claude": home / ".claude" / "skills", "codex": home / ".codex" / "skills"}
    agents = ["claude", "codex"] if agent == "both" else [agent]
    return [roots[a] / SKILL_NAME for a in agents]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--agent", choices=["claude", "codex", "both"], default="both")
    ap.add_argument("--project", help="install into this project instead of the user-level folders")
    args = ap.parse_args()

    for dest in target_dirs(args.agent, args.project):
        if dest.resolve() == SOURCE_DIR:
            print(f"skip {dest} (this is the source copy)")
            continue
        if dest.exists():
            shutil.rmtree(dest)
        shutil.copytree(SOURCE_DIR, dest, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
        print(f"installed {dest}")
    print("Start a new Claude Code / Codex session for the skill to appear.")


if __name__ == "__main__":
    main()
