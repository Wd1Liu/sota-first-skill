#!/usr/bin/env bash
set -euo pipefail

scope="user"
repo_path="$PWD"
force="false"

usage() {
  cat <<'USAGE'
Usage: ./scripts/install.sh [--scope user|repo] [--repo PATH] [--force]

Examples:
  ./scripts/install.sh
  ./scripts/install.sh --scope repo --repo /path/to/project
  ./scripts/install.sh --force
USAGE
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --scope)
      scope="${2:-}"
      shift 2
      ;;
    --repo)
      repo_path="${2:-}"
      shift 2
      ;;
    --force)
      force="true"
      shift
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "Unknown argument: $1" >&2
      usage >&2
      exit 2
      ;;
  esac
done

if [[ "$scope" != "user" && "$scope" != "repo" ]]; then
  echo "--scope must be 'user' or 'repo'" >&2
  exit 2
fi

script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
root_dir="$(cd -- "$script_dir/.." && pwd)"
source_dir="$root_dir/skills/sota-first"

if [[ ! -f "$source_dir/SKILL.md" ]]; then
  echo "Could not find the source skill at $source_dir" >&2
  exit 1
fi

if [[ "$scope" == "user" ]]; then
  target="$HOME/.agents/skills/sota-first"
else
  repo_path="$(cd -- "$repo_path" && pwd)"
  target="$repo_path/.agents/skills/sota-first"
fi

if [[ -e "$target" ]]; then
  if [[ "$force" != "true" ]]; then
    echo "Target already exists: $target. Re-run with --force to replace it." >&2
    exit 1
  fi
  rm -rf -- "$target"
fi

mkdir -p -- "$(dirname -- "$target")"
cp -R -- "$source_dir" "$target"

echo "Installed sota-first to $target"
echo "Restart Codex if the skill does not appear automatically."
