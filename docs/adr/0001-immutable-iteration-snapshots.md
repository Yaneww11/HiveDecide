# Iteration outcomes are immutable JSONB snapshots

Inputs (matrix, criteria, alternatives, participants, submitted weights) are relational and in 3NF, but everything computed from them is stored once as JSONB and never updated: the normalised matrix on `Task` at start, each submission's computed results on `Submission`, and the iteration's outcome (group results, group ranking, per-participant ρ, τ and d, average coefficients, BIMBee1 eliminations) on `Iteration.snapshot` when the iteration closes. We chose this over recomputing on read so that closed iterations stay exactly as the group saw them even if `core` changes later, and so history pages never redo eigenvector or correlation work.

## Consequences

- The agreement measures live in the iteration snapshot keyed by participant, not on `Submission`, because they only exist after the iteration closes and a submission is final when sent.
- The final result is not stored: it is derived from the last resolved iteration (GCBIM: the leader's chosen ranking; BIMBee1: the group ranking restricted to the remaining alternatives).
- JSON vectors and matrices are keyed by alternative and criterion ids, never by position.
