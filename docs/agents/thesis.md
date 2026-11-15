# Thesis notes procedure

This project is the practical part of a Bachelor's thesis. The notes in
`docs/thesis/notes.md` are raw material for the thesis chapter on architecture
and implementation. The user writes the final text.

## When

At the end of each ticket, after code review and before the final commit.
Run in the main session; never inside a subagent, because the user must approve.

## Steps

1. List candidates from this ticket (see "What counts as a candidate").
2. Show the list to the user and ask which to record. Record nothing unapproved.
3. Write approved entries under the matching section of the notes. Update an
   existing entry instead of adding a duplicate.
4. Add or update the description of each component the ticket implemented
   (see "Component descriptions").

## What counts as a candidate

- A choice between real alternatives (library, pattern, schema, algorithm).
- A deviation from `docs/plan.md` or from the original method in the literature.
- A non-obvious implementation: concurrency, tie handling, numerical tolerance.
- A good practice applied with a visible effect (a test that caught a bug,
  a constraint that prevents invalid data).

Not candidates: routine CRUD, formatting, renames, anything ruff enforces.

## Entry format (Bulgarian, impersonal form)

- **Тема**, дата, тикет
- **Решение**
- **Разгледани алтернативи** и защо са отхвърлени
- **Обосновка**
- **Къде е в кода** (module and function names, not line numbers)
- **Връзка с теорията** (formula or section, if any)

## Component descriptions

Scope: every public function of the `core` package in full; the key models and
services of `decisions` and `accounts` briefly (role and main rules only).

Format: роля, вход и изход, стъпки на алгоритъма, връзка с формулата, тест,
който го проверява. No code listings; name the function so a snippet can be
chosen later. When code changes, update the description in place.

## Rules

- Bulgarian terms. An English term with no Bulgarian equivalent is written in
  Latin script and explained once. No transliteration.
- Every decision records the alternatives it was compared against.
- Use `GLOSSARY.md` terms. Link to ADRs in `docs/adr/` instead of restating them.
- Reference theses may be read for ideas only. Never copy their text, structure
  or style.
