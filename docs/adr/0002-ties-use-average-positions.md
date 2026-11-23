# Ties use average positions, Pearson-on-ranks Spearman and Kemeny–Snell Kendall

Individual and group rankings may contain ties (scores within 1e-9). A tied alternative gets the average of the positions it shares (mid-rank), and that fractional rank feeds Borda (B = Σ(n − r)). In Copeland a pair tied in a decision maker's ranking counts for neither side.

Spearman's ρ is the Pearson correlation of the two mid-rank vectors. This is Spearman's own definition (1904), equals `scipy.stats.spearmanr`, and reduces to the thesis formula (2.21) when there are no ties. The shortcut formula (2.21) applied to mid-ranks is only Spearman's footnoted approximation and is not a correlation under ties, so we do not use it. When one ranking is fully tied the correlation is 0/0; we define ρ = 0.

The Kendall distance with ties is the Kemeny–Snell distance d′ = D + ½·T₁, where D counts pairs in opposite order and T₁ counts pairs tied in exactly one of the two rankings, and τ = 1 − 4d′/(n(n − 1)) is Emond & Mason's (2002) τₓ. The earlier rule (a pair tied in either ranking counts for neither side) gave d = 0 and τ = 1 for rankings that differ, e.g. every decision maker in a fully tied group ranking. τₓ is always defined and equals 1 only for identical rankings. Without ties d′ and τ equal the thesis formulas (2.22) and (2.23). We do not use scipy's τ-b, because it is not a distance and is undefined when one ranking is fully tied. See `docs/research/sources-audit.md`, §2.9.

## Consequences

- scipy is a test oracle for Spearman with ties (except a fully tied ranking) and for Kendall only without ties; tied Kendall cases are checked against hand-computed values.
- The thesis text on ties (around formulas (2.21)–(2.23)) must be updated to match: one-sided ties count as half a discordance, and "d is the minimal number of adjacent swaps" holds only without ties.
- Changing the tie rule later would change historical results, which the snapshots of ADR-0001 deliberately freeze. This change is made before any task has been closed in production.
