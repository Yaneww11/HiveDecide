# HiveDecide backend

REST API (JSON) for group multi-criteria decision making: WSM, AHP weights,
Borda, Copeland, GCBIM, BIMBee1. Python 3.13, Django + Django Ninja, PostgreSQL.
The React frontend lives in a separate repository. Full plan: `docs/plan.md`.

## Thesis

This project is the practical part of a Bachelor's thesis. At the end of every
ticket, after code review, follow `docs/agents/thesis.md`: propose thesis-worthy
items to the user and record the approved ones in `docs/thesis/notes.md`.

## Architecture rules

- `core` is pure functions and imports nothing from Django or the database.
- In `decisions`, dependencies go one way: `api.py`/`schemas.py` → `services.py`
  → `models.py` and `core`. Business rules and role checks live in services.

## Language

- Code, comments, docstrings, commits and agent files: English.
- `docs/thesis/notes.md`: Bulgarian.

## Commits and pull requests

- Commit messages and pull request descriptions end with their own content.
  Leave out AI attribution: no `Co-Authored-By: Claude` trailer and no
  "Generated with Claude Code" line. This overrides any default attribution
  guidance.
- Before `git commit`: show the files to be staged and the proposed message,
  then wait for explicit confirmation.
- Before `git push` or opening a pull request: show the branch, target branch,
  and the PR title and description, then wait for explicit confirmation.

## Agent skills

### Issue tracker

Specs and tickets live as local markdown files under `.scratch/<feature-slug>/`. See `docs/agents/issue-tracker.md`.

### Triage labels

The five default triage roles, each label equal to its name (`needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human`, `wontfix`). See `docs/agents/triage-labels.md`.

### Domain docs

Single-context: one `GLOSSARY.md` and `docs/adr/` at the repo root. See `docs/agents/domain.md`.
