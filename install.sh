#!/usr/bin/env bash
# install.sh - link (or copy) the rocket-fuel skill into ~/.claude/skills/
#
#   ./install.sh              symlink the skill (updates follow git pull)
#   ./install.sh --copy       install an independent copy instead
#   ./install.sh --project    install into ./.claude/skills/ of the current dir
#   ./install.sh --force      replace an existing install (backs it up first)

set -euo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILLS=(rocket-fuel)
MODE=link
TARGET="$HOME/.claude/skills"
FORCE=0

while [[ $# -gt 0 ]]; do
  case "$1" in
    --copy)    MODE=copy ;;
    --project) TARGET="$PWD/.claude/skills" ;;
    --force)   FORCE=1 ;;
    -h|--help) sed -n '2,8p' "$0" | sed 's/^# \{0,1\}//'; exit 0 ;;
    *) echo "unknown option: $1" >&2; exit 2 ;;
  esac
  shift
done

mkdir -p "$TARGET"
echo "installing into $TARGET (mode: $MODE)"

for skill in "${SKILLS[@]}"; do
  src="$REPO/skills/$skill"
  dst="$TARGET/$skill"

  if [[ -e "$dst" || -L "$dst" ]]; then
    if [[ "$FORCE" -eq 0 ]]; then
      echo "  SKIP $skill: already exists at $dst"
      echo "       re-run with --force to replace it (a backup is kept)"
      continue
    fi
    backup="$dst.bak.$(date +%Y%m%d%H%M%S)"
    mv "$dst" "$backup"
    echo "  backed up existing $skill to $(basename "$backup")"
  fi

  if [[ "$MODE" == link ]]; then
    ln -s "$src" "$dst"
    echo "  linked $skill"
  else
    cp -R "$src" "$dst"
    echo "  copied $skill"
  fi
done

cat <<EOF

done. verify with:
  ls -la $TARGET | grep rocket-fuel

requires the Codex CLI (npm i -g @openai/codex@latest && codex login).
see skills/rocket-fuel/SKILL.md for the full workflow.
EOF
