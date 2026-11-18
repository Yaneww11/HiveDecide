# Ties use average positions and the thesis formulas, not scipy's variants

Individual and group rankings may contain ties (scores within 1e-9). A tied alternative gets the average of the positions it shares, and that fractional rank feeds Borda (B = Σ(n − r)) and Spearman (2.21); in Copeland and in the Kendall distance (2.22) a pair tied in either ranking counts for neither side. We implement the thesis formulas (2.16), (2.18), (2.21)–(2.23) directly rather than delegating to `scipy.stats`, because with ties `spearmanr` computes a Pearson correlation of ranks and `kendalltau` computes τ-b, which would make the system's numbers disagree with the thesis tables.

## Consequences

- scipy is a test oracle only for tie-free cases; tied cases are checked against hand-computed values.
- Changing the tie rule later would change historical results, which the snapshots of ADR-0001 deliberately freeze.
