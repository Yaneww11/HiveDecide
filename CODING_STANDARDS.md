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

## ORM and queries

- A queryset that is iterated and touches related objects uses `select_related` or `prefetch_related`.
- No queries inside loops. Building the decision matrix loads alternatives, criteria and scores in a fixed number of queries, whatever the matrix size.
- Use `Prefetch("rel", queryset=...)` when a prefetched relation needs filtering or ordering, for example only the alternatives still active in an iteration.
- Use `.exists()` / `.count()`, not `len(queryset)` or `if queryset:`, to test or count.
- Fields with a fixed set of values (task state, group method, aggregation, criterion direction) are `TextChoices` enums. Code compares against the enum member, never a literal string.
- Raw SQL needs a reason in a comment, lives in a service, and is always parameterized, never built with string formatting or f-strings.

## Schemas

- Response schemas list their fields explicitly. No `fields = "__all__"` on a `ModelSchema`: a new model column would leak into the API.
- Input and output schemas are separate. Server-set values (ids, timestamps, coordinator, state, join code, computed results) never appear in an input schema.
- When two views of the same object need different payloads (list and detail, or coordinator, leader and participant), each gets its own schema rather than one schema with optional fields.

## API

- Errors use the single format `{"code", "detail", "errors"}` with a stable code.
- State conflicts return 409.

## Migrations

- One migration per logical change.
- Never edit a migration that is already on `main`; add a new one.
- Rename generated names to something descriptive.
- `RunPython` data migrations are reversible, or say in a comment that they are not.

## Tests

- Tests check external behaviour, not implementation details.
- New tests are plain pytest functions, not `TestCase`.
- Tests live in the package's `tests/` folder, in `test_<module>.py`.
- Use `@pytest.mark.django_db` only when the test touches the database. Core tests never do.
- Core tests use the 3×4×3 example; Spearman and Kendall are checked against scipy.
- Database tests run on PostgreSQL, never SQLite.
- New service logic needs a test.
- A bug fix needs a regression test that fails without the fix.

## Security

- Secrets come from the environment, never from source.
- Every route requires authentication except registration and token issue.
- A service checks that the caller is the coordinator or a participant of the task before reading or changing it.
- A response never contains another participant's ranking or weights unless the caller's role allows it.

## Style

- English names, comments and docstrings.
- Comments explain why, not what.
- No abbreviations in names except established method names (WSM, AHP, CR).
