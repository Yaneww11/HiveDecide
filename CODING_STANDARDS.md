# Coding standards

Read during code review. Anything ruff or mypy enforces is not repeated here.

## Layering

- `core` imports nothing from Django, the ORM or the other apps.
- `api.py` and `schemas.py` contain no business rules; they call services.
- Role and state checks live in `services.py`.
- Services use the ORM directly; there is no repository layer.

## Core

- Pure functions: no I/O, no global state, inputs are not mutated.
- Full type annotations; `core` passes mypy.
- NumPy is used for linear algebra only; the algorithms are written by hand.
- Score comparisons use the shared 1e-9 tolerance, never `==`.
- Each public function's docstring names the method and its formula source.

## Services and data

- Each non-CRUD action is one service function and one transaction.
- Closing an iteration locks the iteration row (`select_for_update`).
- Invariants are also enforced by database constraints, not only in code.
- Snapshot JSONB fields are written once and never updated.

## API

- Errors use the single format `{"code", "detail", "errors"}` with a stable code.
- State conflicts return 409.

## Tests

- Tests check external behaviour, not implementation details.
- Core tests use the 3×4×3 example; Spearman and Kendall are checked against scipy.
- Database tests run on PostgreSQL, never SQLite.

## Style

- English names, comments and docstrings.
- Comments explain why, not what.
- No abbreviations in names except established method names (WSM, AHP, CR).
