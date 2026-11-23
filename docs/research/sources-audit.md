# Audit of older sources, constants and rules used by HiveDecide and the thesis

Research note for HiveDecide. Scope: every number, threshold, scale, formula
variant, tie rule or definition in `docs/plan.md` and in the thesis text
(`docs/thesis/Дипломна работа – … .txt`, cited below as "thesis, line N") that
comes from a specific source, with the question "is there a newer or better
verified alternative?". The Random Index table is settled in
`docs/research/saaty-ri-table.md` and is not redone here.

Verification legend (same as `saaty-ri-table.md`):

- **[P]** checked against the primary source itself (full text read).
- **[S: X]** only checked through secondary source X; the primary was not accessible.
- **[U]** not verified at all; stated from general knowledge and must not be cited as is.

Reference keys in square brackets with a `B` prefix (e.g. [B12]) point to the
combined list in §4. Thesis bibliography numbers are written "thesis ref. [N]".
Page numbers of the Handbook of Computational Social Choice [B40] are the printed
page numbers of the open PDF.

## 1. Summary

| # | Item | Current source (thesis / plan) | Recommendation | Priority |
|---|------|------------------------------|----------------|----------|
| 1 | AHP 1–9 scale | Saaty 1980 (thesis line 162) | Keep the scale; cite Saaty 2008 Table 1, p. 256 for the verbal labels ("extreme", not "absolute") | low |
| 2 | AHP priority derivation | Principal eigenvector, RGM as approximation (lines 163–167; plan §5) | Keep the eigenvector. Add one sentence: for k = 3 EV and RGM give exactly the same vector (Saaty 2008, p. 263) | low |
| 3 | AHP consistency threshold | CR ≤ 0.10 (line 170; plan §5) | Keep. Optionally mention GCI (Aguarón & Moreno-Jiménez 2003) and size-dependent thresholds as alternatives | low |
| 4 | AHP group aggregation (AIJ/AIP) | Forman & Peniwati 1996 (lines 172, 230) | Keep; claim and page range verified [P]. Add the ISAHP DOI or cite the EJOR 1998 version | low |
| 5 | Rank reversal | Belton & Gear 1983 (line 172) | Keep; add a modern review (Maleki & Zahir 2013) and note that the frozen WSM normalization is HiveDecide's own guard | low |
| 6 | WSM normalization | x/max, min/x (lines 129–132, 157; plan §5) | Keep; add a verifiable citation for the min/x cost variant (Krishnan 2022, Table 2, "N4") | low |
| 7 | Borda points and ties | Borda 1784 (lines 311–316; plan §5 "Равенства") | Keep the rule (average positions). **Fix text**: the identity B = Σ N(aᵢ, aⱼ) in (2.16) fails with ties; cite Zwicker 2016 for the tie-aware form | medium |
| 8 | Copeland scoring and citation | Copeland 1951 mimeo (line 350) | Keep +1/−1/0 scoring (≡ "Copeland^0.5"); add Zwicker 2016, p. 28 and Saari & Merlin 1996 as citable sources | medium |
| 9 | Rank correlation with ties | Spearman 1904, Kendall 1938 (lines 472–479; plan §5; ADR-0002) | **Switch** the Kendall distance/τ tie rule to Kemeny–Snell / Emond–Mason τₓ (tie-vs-strict pair = ½ disagreement). Decide Spearman explicitly (see §2.9). Current rule gives τ = 1 for non-identical rankings | **high** |
| 10a | Arrow's conditions | Arrow 1951 (lines 394–400) | Conditions as listed (with Pareto) are the 1963 2nd-edition form; cite 1963 (or 3rd ed. 2012) | medium |
| 10b | Black, single-peakedness | Black 1948 (line 401) | Add "for an odd number of DMs" | low |
| 10c | Nanson | Nanson 1882 (line 273) | Nanson's own rule drops candidates "not above" the average (≤), not "below"; publication year is 1883 | low |
| 10d | Condorcet, maximin, Kemeny, Dodgson, May, Harsanyi, Fishburn 1977/1982 | lines 262, 269–273, 404–414, 467 | Claims correct as far as verified; add Handbook [B40] as accessible companion citation | low |
| 11 | GCBIM / BIMBee1 | Andonov 2006, 2009, 2012 | Nothing to replace. Andonov 2006 is pp. 3–8 in print (thesis: 3–9). Parameters t, τ (= q) and the "b < τ" rule verified [P] | low |
| 12 | Thesis-internal | line 131 vs lines 89, 128 | "scale 1 to 9" vs "1 to 10" for qualitative criteria contradict each other | low |

High-priority finding in one sentence: with the current tie rule (plan §5
"Равенства", thesis line 479, ADR-0002) a pair tied in only one ranking counts as
agreement, so a DM whose strict ranking differs from a partially or fully tied
group ranking can get d = 0 and τ = 1; this already happens in the thesis's own
BIMBee1 example (Table 2.11, iteration 2) — see §2.9.

## 2. Items

### 2.1 AHP fundamental 1–9 scale

**Current use.** Thesis line 162: 1 equal, 3 moderate, 5 strong, 7 very strong,
9 "абсолютно превъзходство", even values intermediate, reciprocals for the reverse,
cited to Saaty (1980) (thesis ref. [29]). Plan §5 "Итерация": comparisons on
"скалата на Саати (1–9 и реципрочните им)".

**Original sources.**

- Saaty (1977) [B1], Table 1: 1 equal importance, 3 weak importance, 5 essential
  or strong, 7 demonstrated, 9 absolute importance [S: as summarised in
  `saaty-ri-table.md` and Wedley 2017; the table labels were not re-read here,
  treat exact 1977 wording as **[U]**].
- Saaty (1980) [B2]: book not accessed **[U]**.
- Saaty (2008) [B3], Table 1 "Fundamental Scale of Absolute Numbers", p. 256 [P]:
  1 Equal importance; 2 Weak or slight; 3 Moderate importance; 4 Moderate plus;
  5 Strong importance; 6 Strong plus; 7 Very strong or demonstrated importance;
  8 Very, very strong; 9 **Extreme importance**; 1.1–1.9 for very close
  activities; reciprocals "a logical assumption". Same page: the scale is "derived
  from basic principles … obtaining a functional equation" [P].
- Attribution: correct in substance. The label "absolute" for 9 matches the 1977
  wording, "extreme" is Saaty's later wording [P for 2008].

**Alternatives.**

- Lootsma (1993) geometric scale, used in multiplicative AHP/SMART [B4]
  (Crossref-verified metadata; content **[U]**).
- Salo & Hämäläinen (1997) "balanced scale" [B5] (metadata only; content **[U]**).
- Comparative studies: Dong et al. (2008) [B6]; Ishizaka, Balkenborg & Kaplan
  (2011) [B7]; Franek & Kresta (2014) (not checked). Their conclusions were not
  read **[U]**.

**Pros and cons.**

| Criterion | Saaty 1–9 (keep) | Geometric (Lootsma) / balanced (Salo–Hämäläinen) |
|---|---|---|
| Method quality | Criticised for uneven spacing at the top end [U] | Designed to fix spacing/sensitivity [U] |
| Accessibility | Saaty 2008 open access, Table 1 p. 256 [P] | Journal papers, paywalled |
| Adoption | Default in Expert Choice, SuperDecisions, textbooks [U] | Niche |
| Impact on HiveDecide | none | Changes all AHP weights; **RI values in the plan are only valid for 1–9** (Saaty 2008 simulated entries from {1/9 … 9}, p. 263 [P]) |
| Complexity | trivial | needs a new RI table or a different consistency index |

**Recommendation: keep.** The RI table (plan §5) and CR ≤ 0.10 are calibrated on
the 1–9 scale, so changing the scale breaks the consistency check. Text change
(optional): cite Saaty (2008) Table 1, p. 256 next to [29] and write "9 – изключително
(extreme) превъзходство". No code change.

### 2.2 AHP priority derivation: eigenvector vs row geometric mean

**Current use.** Thesis lines 163–167: weights are the principal eigenvector (2.6),
RGM (2.7) is "често използвано приближение"; line 171 says (2.7) "дава същите
стойности" for the example. Plan §5: "Теглата са собственият вектор (2.6)"; plan §2
"собствен вектор за AHP".

**Original sources.**

- Saaty (1977) [B1] and (1980) [B2] introduce the eigenvector method (book **[U]**).
- Saaty (2003) "why is the principal eigenvector necessary" (EJOR 145(1)) — read in
  the RI note [P there].
- Saaty (2008) [B3], p. 263 [P]: for a 3×3 reciprocal matrix with entries a, b, c
  above the diagonal, λmax = 1 + d + 1/d with d = (ac/b)^(1/3) and
  w₁ = bd/(1 + bd + c/d), w₂ = c/(d(1 + bd + c/d)), w₃ = 1/(1 + bd + c/d).
  Own check: these ratios w₁/w₃ = bd and w₂/w₃ = c/d are exactly the ratios of the
  row geometric means, i.e. **for n = 3 EV and RGM coincide exactly**. Numerical
  check on the thesis example (line 171): both give (0.29696, 0.16342, 0.53961),
  λmax = 3.00920 (own computation with NumPy).
- RGM / logarithmic least squares: Crawford & Williams (1985) [B8] (metadata
  verified; content [S: Aguarón et al. 2020, B12, p. 3, "The most extended
  prioritisation procedure is the Row Geometric Mean (RGM) or Logarithmic Least
  Square (LLS) method"]).

**Alternatives and the debate.**

- Saaty & Vargas (1984) compare EV, LLS and LS [B9] (metadata only **[U]** content).
- Barzilai (1997) argues only the geometric mean is consistent with his axioms
  [B10] (metadata; content **[U]**). Note: a later preprint, "The Fundamental
  Theorem of Barzilai does not hold" (arXiv:1912.05968), disputes this — not read **[U]**.
- Csató (2018) characterises the RGM ranking by anonymity, responsiveness and
  "aggregation invariance" (geometric-mean group consensus) [B11]
  [S: arXiv:1706.07256 abstract]. Relevant if the thesis wants an argument that RGM
  composes cleanly with geometric-mean group aggregation (item 4).

| Criterion | Eigenvector (keep) | RGM / LLS |
|---|---|---|
| Method quality | Saaty's original; CI/CR/RI are defined on λmax | Axiomatically characterised [B11]; pairs naturally with GCI and geometric group aggregation |
| Accessibility | Saaty 2008 open access [P] | Crawford & Williams paywalled; Aguarón et al. 2020 open access [B12] |
| Adoption | Expert Choice, SuperDecisions [U] | Many textbooks, R/Python packages [U] |
| Impact on HiveDecide | — | Identical for k ≤ 3; small differences for k ≥ 4; the CR check would have to move to GCI |
| Complexity | NumPy `eig` + Perron vector selection | Closed form, no eigen-solver |

**Recommendation: keep the eigenvector.** The plan's CR check and the 2008 RI table
are defined on λmax; switching to RGM would also mean switching the consistency
measure (item 3). Add one sentence to line 171: "За k = 3 собственият вектор и
средното геометрично съвпадат точно (Saaty 2008, с. 263)", which turns "дава
същите стойности" from an empirical observation into a cited fact. Code: no change;
a core test can assert EV == RGM for random 3×3 reciprocal matrices.

### 2.3 AHP consistency threshold and measure

**Current use.** Thesis line 170: "Сравненията се приемат, ако CR ≤ 0,1"; plan §5:
accept at CR ≤ 0.10, reject with CR > 0.1, skip for k ≤ 2.

**Original source.** Saaty (2008) [B3], p. 264 [P]: "our allowable consistency
ratio should be not more than about 0.10. The requirement of 10% cannot be made
smaller such as 1% or 0.1% without trivializing the impact of inconsistency."
Saaty (1990) "about 10% or less", p. 13 [P in RI note]. Attribution correct
(thesis cites [30] = Saaty 2008).

**Alternatives.**

- Size-dependent thresholds 5% (n = 3), 8% (n = 4), 10% (n > 4), attributed to
  Saaty (1994), *Interfaces* 24(6), 19–43 [B13] [S: Aguarón, Escobar,
  Moreno-Jiménez & Turón 2020, B12, p. 3]. The Interfaces paper itself was not read
  **[U]**.
- Geometric Consistency Index (GCI) for RGM priorities, Aguarón & Moreno-Jiménez
  (2003) [B14]: GCI = 2/((n−1)(n−2)) Σᵢ<ⱼ log² (aᵢⱼ wⱼ/wᵢ); thresholds 0.31 (n = 3),
  0.35 (n = 4), 0.37 (n > 4), obtained "by analogy with the Saaty CR"
  [S: B12, pp. 3 and 6]. One secondary source (Tomashevskii, arXiv:1410.0823, p. 9)
  prints 0.0314 / 0.0352 / 0.037, but the same page then calls GCI₅ = 0.27 acceptable
  against 0.037, so that rendering is internally inconsistent; the 0.31/0.35/0.37
  values from the method's own authors [B12] are the ones to use. Primary not read.
- Surveys of other indices (Koczkodaj 1993 [B15]; Bozóki & Rapcsák 2008 [B16];
  Brunelli 2018 [B17]) — metadata only.
- For the thesis example (line 171): GCI = 0.0276 (own computation), far below 0.31;
  CR ≈ 0.0088. Both measures accept.

| Criterion | CR ≤ 0.10 (keep) | Size-dependent CR | GCI (with RGM) |
|---|---|---|---|
| Method quality | Heuristic, but the inventor's rule, argued on p. 264 [B3] | Stricter for small k [S] | Has a statistical interpretation [U]; tied to RGM |
| Accessibility | Open access, same paper as the RI table | Interfaces paper not read | Open-access restatement [B12] |
| Adoption | Universal default | Some tools [U] | Common in RGM-based work |
| Impact | — | Rejects more 3×3 and 4×4 matrices | Needs RGM; different accept/reject boundary |
| Complexity | trivial | trivial | trivial |

**Recommendation: keep CR ≤ 0.10**, matching the eigenvector method and the 2008
RI table, both from the same paper. Optionally add one sentence that stricter
size-dependent thresholds and the GCI exist (cite [B12]/[B14]). No code change.

### 2.4 AHP group aggregation: AIJ vs AIP, geometric vs arithmetic mean

**Current use.** Thesis line 172: matrices of several DMs "могат да се обединят, като
за всяко сравнение се вземе средната геометрична на отговорите им [16]"; line 230:
group AHP "осредняват сравненията по двойки или получените приоритети [16]".
HiveDecide does **not** implement this (each DM keeps own weights; aggregation is
ordinal). Thesis ref. [16] = Forman & Peniwati (1996), ISAHP, pp. 383–391.

**Original source.** Forman & Peniwati (1996) [B18], read in full [P]:

- Defines AIJ (aggregating individual judgments into an "aggregate hierarchy") and
  AIP (synthesising each individual's hierarchy and aggregating the priorities),
  p. 383 [P].
- Geometric mean required for AIJ because only it preserves reciprocity, citing
  Aczél & Saaty (1983) [B19], p. 385 [P]; AIP may use arithmetic or geometric mean,
  p. 386 [P]; AIJ can violate Pareto, AIP cannot, pp. 386–387 [P]; conclusions
  p. 390 [P].
- Page range 383–391 (references end on p. 391) — **thesis page range correct** [P].
  DOI exists: 10.13033/isahp.y1996.009 (Crossref).
- Journal version: Forman & Peniwati (1998), EJOR 108(1), 165–169 [B20]
  (Crossref-verified).
- Saaty (2008) [B3], §17 "Group Decision Making", p. 304 [P]: "It has been proved
  that the geometric mean is the unique way to do that" (reciprocal-preserving
  synthesis of judgments), with the Aczél–Saaty conditions listed.

**Alternatives.** Ramanathan & Ganesh (1994) [B21] (weighted arithmetic mean of
priorities); Ossadnik, Schinke & Kaspar (2016) comparative review [B22]; Csató (2018)
[B11]. None overturns the AIJ = geometric mean rule.

| Criterion | Forman & Peniwati 1996 (proceedings) | Forman & Peniwati 1998 (EJOR) | Aczél & Saaty 1983 |
|---|---|---|---|
| Accuracy | Claim verified [P] | Same content [U: not read, same title/authors] | Original theorem |
| Accessibility | Open PDF at isahp.org; DOI | DOI, paywalled, indexed everywhere | Paywalled |
| Adoption | Less cited | Standard citation for AIJ/AIP | Standard for the GM theorem |
| Impact on HiveDecide | none (not implemented) | none | none |

**Recommendation: keep**, add the DOI to ref. [16], or replace by the EJOR 1998
version (more citable). Optionally add Saaty 2008 p. 304 for "geometric mean is
the unique reciprocal-preserving aggregator". No code impact.

### 2.5 Rank reversal in AHP

**Current use.** Thesis line 172: adding or removing an alternative may change the
order of the others (rank reversal) [6]; does not affect HiveDecide because AHP is
used only for criterion weights. Line 185: full AHP "податлив на обръщане на рангове".
Line 184: TOPSIS also susceptible.

**Original source.** Belton & Gear (1983), Omega 11(3), 228–230 [B23]
(Crossref-verified; full text not read; that the paper shows a reversal after adding
a copy of an alternative is [S: Saaty 2008, §16, p. 302 discusses "copies or near
copies"; Maleki & Zahir 2013 title/abstract]). Attribution correct.

**Later answers.**

- Saaty & Vargas (1984) "The legitimacy of rank reversal" [B24] (metadata).
- Millet & Saaty (2000) distributive vs ideal mode [B25] (metadata).
- Saaty (2008) [B3], §16, pp. 302–303 [P]: rank reversal "can never happen when the
  objects are compared with respect to one criterion and the judgments are
  consistent"; rank can be preserved with the ratings approach or ideal mode;
  "rank reversal occurs on the average only 8% of the time" [P, citing his ref. 16].
- Reviews: Maleki & Zahir (2013) [B26]; Wang & Luo (2009) on rank reversal in other
  MCDM methods [B27] (metadata).

**HiveDecide-specific point.** The analogue in HiveDecide is WSM with x/max
normalization when BIMBee1 removes alternatives: if the max were recomputed, scores
of the remaining alternatives could change. Plan §5 and thesis line 157 freeze the
normalization on the initial set, which makes every DM's WSM order of the remaining
alternatives invariant under deletion. This is the same idea as Belton & Gear's
"divide by the maximum of a fixed reference" and is worth stating explicitly.

**Recommendation: keep** the citation; add one modern review ([B26]) and one sentence
connecting the frozen normalization to the rank-reversal literature. No code change.

### 2.6 WSM normalization

**Current use.** Thesis lines 129–131, (2.4): rᵢⱼ = xᵢⱼ / max xₗⱼ (benefit),
rᵢⱼ = min xₗⱼ / xᵢⱼ (cost); positive scores required; line 132 mentions min-max and
vector normalization; line 157 and plan §5: normalization fixed per method (linear
for WSM, vector for TOPSIS), computed once on the initial set. Line 175 cites
Fishburn (1967) [13] and Triantaphyllou (2000) [33] for WSM being the oldest and
most used method; line 128 cites [33] for "result depends on normalization".

**Original sources.**

- Fishburn (1967), *Operations Research* 15(3), 537–542, published as a "Letter to
  the Editor" (Crossref title) [B28]. It is the usual citation for WSM; content not
  read **[U]**.
- Hwang & Yoon (1981) [B29], "linear scale transformation" — book not accessed;
  page for x/max and min/x **[U]**.
- Triantaphyllou (2000) [B30] — book not accessed **[U]**.
- A verifiable open source for both formulas: Krishnan (2022), *Frontiers in Big
  Data* 5, 990699, Table 2: "N4 (maximum II)" benefit x/max, cost min/x; "N3
  (maximum I)" cost 1 − x/max; N2 min-max; N6 vector [S: PMC full text, B31].
  The survey does not name a best method for SAW/WSM [S: B31].

**Alternatives.** 1 − x/max for cost (N3), min-max (N2), sum (N1), vector (N6)
[B31]; empirical comparisons Jahan & Edwards (2015) [B32], Vafaei, Ribeiro &
Camarinha-Matos (2016, 2018) [B33, B34] (metadata only; conclusions **[U]**).

| Criterion | x/max, min/x (keep) | 1 − x/max for cost | min-max |
|---|---|---|---|
| Method quality | Ratio-preserving (cost ratios inverted); best gets 1; requires x > 0 | Linear in cost; worst cost not 0 unless 2× best | Stretches small differences to [0, 1] (thesis line 132) |
| Accessibility | Krishnan 2022 open access, Table 2 | same | same |
| Adoption | Common default (e.g. "linear max") | Common alternative | Common in VIKOR [S: B31] |
| Impact on HiveDecide | — | Changes Table 2.2 (e.g. a₁ cost 0.67 → 0.25) and possibly rankings | Changes all numbers |
| Complexity | trivial | trivial | needs max ≠ min |

**Recommendation: keep.** Add Krishnan (2022) as a verifiable citation for the exact
formula pair, since Hwang & Yoon's page could not be checked. No code change.

### 2.7 Borda count: points and ties

**Current use.** Thesis lines 311–316: Borda presented the method in 1770, printed
1784 [8]; n − 1 points for first place … 0 for last; (2.16)
B(aᵢ) = Σₑ (n − rₑ(aᵢ)) = Σⱼ≠ᵢ N(aᵢ, aⱼ); weighted (2.17). Plan §5 "Равенства":
tied alternatives get the average of their positions and that fractional rank is used
in B = Σ(n − r); ADR-0002.

**Original source.** Borda, "Mémoire sur les élections au scrutin", *Mémoires de
l'Académie Royale des Sciences*, année 1781, pp. 657–665, printed 1784 [B35]
[P via English translation by R. J. Pulskamp]:

- Footnote 2: ideas "presented to the Academy fourteen years ago, 16 June 1770"
  [P, transl. p. 3]. Thesis claim (1770 / 1784) correct.
- Points: last place a, second-to-last a + b, …, first a + (n − 1)b; "the
  superiority of the first position over the second … must be counted equal"
  [P, transl. p. 4]. With a = 0, b = 1 this is exactly n − 1 … 0. Correct.
- Borda treats strict rankings only; no tie rule [P, as far as the translation goes].
- The thesis reference omits pages; the memoir is in the *Mémoires* part of the
  1781 volume (pp. 657–665); an "Analysis" of it appears in the *Histoire* part,
  pp. 31–34 [P, transl. header].

**Ties (modern definition).** Zwicker (2016), Handbook [B40], ch. 2, p. 28,
eq. (2.3): symmetric Borda score Σ_y Net_P(x > y), affinely equivalent to the usual
(m − 1, …, 0) scores; p. 29: the symmetric form "is well-defined for profiles of weak
preferences, yielding plausible extensions of the Borda and Copeland rules" [P].
Own derivation: with average positions, n − r̄(x) = #{below x} + ½ #{tied with x},
so the plan's rule is exactly Zwicker's symmetric Borda on weak orders (each tied
pair gives ½ point to each side). Other variants for partial ballots exist (Emerson
2013 [B36]; Black 1976 [B37], metadata only).

**Finding (text).** The second equality in (2.16), B = Σⱼ N(aᵢ, aⱼ), holds only for
strict rankings. With ties it becomes B = Σⱼ [N(aᵢ, aⱼ) + ½ T(aᵢ, aⱼ)], where
T(aᵢ, aⱼ) is the number of DMs who tie the two. Ties in individual WSM rankings are
rare but allowed by plan §5 (scores within 1e-9).

| Criterion | Borda 1784 + average positions (keep) | "0 points for ties" / pessimistic | Emerson's modified Borda |
|---|---|---|---|
| Method quality | Neutral; matches Zwicker's tie-aware definition [P] | Penalises ties asymmetrically | Designed for partial ballots, not ties |
| Accessibility | Translation + Handbook open | various | paywalled |
| Impact | — | Different totals with ties | Not applicable (ballots are complete) |

**Recommendation: keep the rule**, change the text: after (2.16) add "при подредби
без равенства" to the second equality, and in §2.9/plan cite Zwicker (2016, p. 29)
for the average-position (½ per tie) extension. Add pages 657–665 to thesis ref. [8].
No code change.

### 2.8 Copeland: scoring of ties and the citation

**Current use.** Thesis line 350: proposed by A. Copeland in 1951 [10]; (2.18)
C = wins − losses, a tied duel changes nothing; ties in C broken by Borda (line 353;
plan §5). Thesis ref. [10]: Copeland (1951), mimeo, University of Michigan.

**Original source.** Copeland (1951) is mimeographed seminar notes; not accessible
**[U]**. The citation itself is the standard one [P: Faliszewski et al. 2009 [B38],
ref. [Cop51]: "Mimeographed notes from a Seminar on Applications of Mathematics to
the Social Sciences, University of Michigan, 1951"].

**What the literature says about ties.**

- Faliszewski, Hemaspaandra, Hemaspaandra & Rothe (2009) [B38], §1.1 [P, arXiv v2,
  pp. 2–3]: winner of a head-to-head contest gets 1, loser 0, ties "(in the most
  common interpretation of Copeland's meaning) awarded half a point"; 0 points for
  ties is "less common"; they define Copeland^α (ties get α); Copeland¹ is Ramon
  Llull's 13th-century system.
- Zwicker (2016) [B40], p. 28, eq. (2.2) [P]: "symmetric Copeland score"
  Copeland(x) = |{y : x >μ y}| − |{y : y >μ x}| — **identical to thesis (2.18)** —
  with footnote 12: it is affinely equivalent to wins + ½ ties and so always picks
  the same winners; wins-only (Copeland⁰) "can differ".
- Saari & Merlin (1996) [B39] (Crossref-verified; content not read).

So the thesis scoring is Copeland^0.5, the most common reading. Breaking Copeland
ties by Borda is HiveDecide's own rule (plan §5); it is in the spirit of Black's rule
(Condorcet winner, else Borda) [S: Brandt et al. in B40, ch. 4] but not a named method.

| Criterion | Copeland 1951 mimeo only | + Zwicker 2016 (Handbook ch. 2) | + Saari & Merlin 1996 |
|---|---|---|---|
| Accessibility | unpublished | Open PDF, exact formula on p. 28 | Journal, DOI |
| Verifiability | none | [P] | [U] |
| Impact | — | none (same rule) | none |

**Recommendation: mention both.** Keep "Copeland (1951)" for priority and add
"(дефиницията е по Zwicker 2016, с. 28)". Optionally add one sentence that the
±1/0 scoring is equivalent to 1/½/0 (Copeland^0.5) and differs from wins-only.
No code change.

### 2.9 Rank correlation and distance with ties (Spearman, Kendall)

**Current use.**

- Thesis line 472–473: ρ = 1 − 6 Σ d² / (n(n² − 1)) (2.21), cited to Spearman
  (1904) [32].
- Lines 475–478: d = number of strictly discordant pairs (2.22),
  τ = 1 − 4d/(n(n − 1)) (2.23), cited to Kendall (1938) [22].
- Line 479 and plan §5 "Равенства": with ties, average positions in (2.21); in
  (2.22) "двойка, която е равна в едната подредба, не се брои за разминаване".
- ADR-0002: implement these formulas instead of `scipy.stats` because `spearmanr`
  is Pearson on ranks and `kendalltau` is τ-b.

**Original sources.**

- Spearman (1904) [B41] [P, archive.org OCR of the JSTOR scan]: rank correlation
  is computed by applying the product-moment method to ranks ("simply substituting
  the inverse ranks … for the performances", pp. 79–80); the separate "method of
  rank differences" (p. 87) uses the sum of **absolute** rank differences, not
  squared ones; its footnote says "This formula becomes slightly incorrect, whenever
  two or more individuals are bracketed as having precisely the same rank" (p. 87).
  The closed form 1 − 6Σd²/(n(n² − 1)) does not appear in the OCR text (searched);
  it is the algebraic simplification of Pearson-on-ranks for untied ranks
  (standard; e.g. Kendall & Gibbons 1990 [B44] — book not accessed **[U]** page).
  So the attribution "Spearman 1904" is correct for the coefficient, but the
  formula as printed is exact only without ties.
- Kendall (1938) [B42]: τ for untied rankings (Crossref-verified; content [S]).
  Ties are treated in Kendall (1945) [B43], which introduces the tie-corrected τ-b
  (metadata verified; content [S]).

**Finding (high priority).** With the current tie rule, a pair tied in exactly one of
the two rankings counts as agreement. Then:

- If Pᴳ ties two alternatives that a DM orders strictly, the DM can have d = 0 and
  τ = 1 although the rankings differ.
- Thesis Table 2.11, iteration 2 (BIMBee1, Borda points a₂: 1, a₃: 4, a₄: 4, so
  Pᴳ = a₃ ∼ a₄ ≻ a₂). Own computation:

  | DM | ranking | d (thesis) | τ (thesis) | τₓ (Emond–Mason) | τ-b | ρ (thesis formula) | ρ (Pearson on mid-ranks) |
  |---|---|---|---|---|---|---|---|
  | E₁, E₃ | a₄ ≻ a₃ ≻ a₂ | 0 | **1.000** | 0.667 | 0.816 | 0.875 | 0.866 |
  | E₂ | a₃ ≻ a₂ ≻ a₄ | 1 | 0.333 | 0.000 | 0.000 | 0.125 | 0.000 |

  The thesis's τ reports perfect agreement for E₁ and E₃ with a group ranking that is
  not theirs.
- Extreme case, the three-DM cycle of thesis line 270 (x ≻ y ≻ z, y ≻ z ≻ x,
  z ≻ x ≻ y): Borda and Copeland both tie all three (line 355), so Pᴳ = x ∼ y ∼ z;
  every DM gets d = 0, τ = 1, mean τ = 1 ("full agreement" for a perfectly
  symmetric conflict). τ-b and Pearson are undefined (0/0); τₓ = 0; the thesis ρ
  formula gives 0.5 (own computation).

**Better alternatives.**

- Kemeny–Snell distance / Emond & Mason (2002) τₓ [B45]: score matrix aᵢⱼ = 1 if i is
  ranked ahead of **or tied with** j, −1 if behind, 0 on the diagonal;
  τₓ = Σ aᵢⱼ bᵢⱼ / (n(n − 1)); "equivalent to Kendall's τ when ties are not allowed"
  [S: Amodio, D'Ambrosio & Siciliano, arXiv:1502.06498, p. 8, eqs. (4)–(5)]; τₓ is the
  unique correlation coefficient equivalent to the Kemeny–Snell distance, and the
  authors argue τ-b should not be used for weak orders [S: abstract via search,
  B45]. Own derivation: τₓ = 1 − 4 d′/(n(n − 1)) with
  **d′ = (#strictly discordant pairs) + ½ (#pairs tied in exactly one ranking)**.
  It is always defined (no 0/0), equals the thesis τ when there are no ties, and
  keeps the shape of (2.22)–(2.23).
- Fagin, Kumar, Mahdian, Sivakumar & Vee (2006) [B46]: Kendall distance with penalty
  p for pairs tied in one ranking only, K^(p); a metric for 1/2 ≤ p ≤ 1, not a
  distance for p = 0 [S: secondary descriptions found by search; paper not read].
  The current HiveDecide rule is p = 0; Kemeny–Snell is p = 1/2.
- Kendall's τ-b [B43] (scipy default): standard in statistics, but undefined when one
  ranking is fully tied and not a distance.
- For Spearman: Pearson correlation on mid-ranks is Spearman's own definition
  (p. 79–80 [B41]) and equals scipy's `spearmanr`; it is undefined when one ranking
  is fully tied. The thesis formula is defined but is not a correlation under ties.

| Criterion | Current (p = 0, Spearman shortcut with mid-ranks) | Kemeny–Snell / τₓ (+ d′) | τ-b / Pearson on mid-ranks (scipy) |
|---|---|---|---|
| Correctness with ties | τ = 1 and d = 0 for different rankings (shown above) | Metric; τₓ = 1 only for identical rankings | Correct correlations, but 0/0 when Pᴳ fully tied |
| Accessibility | Spearman 1904 open (JSTOR/archive); Kendall 1938 paywalled | Emond & Mason paywalled; open restatement in arXiv:1502.06498 | Kendall 1945 paywalled; scipy docs |
| Adoption | Textbook formula for untied data | Standard in consensus-ranking literature [S] | Standard in statistics packages |
| Impact on HiveDecide | — | Changes d, τ and mean τ only when ties occur (BIMBee1 boundary ties, Copeland ties); untied thesis tables 2.9, 2.10 unchanged | Same, plus undefined cases need a convention |
| Complexity | trivial | trivial (count one-sided ties, add ½) | trivial, plus special case |

**Recommendation: switch the Kendall part, decide Spearman explicitly.**

1. Kendall/distance: replace the tie rule by d′ = D + ½·T₁ (T₁ = pairs tied in exactly
   one of the two rankings) and keep τ = 1 − 4d′/(n(n − 1)); cite Emond & Mason (2002)
   and Kemeny & Snell. Thesis line 479: replace "двойка, която е равна в едната
   подредба, не се брои за разминаване" with "двойка, която е равна само в едната
   подредба, се брои за половин разминаване (разстояние на Кемени–Снел [Emond & Mason
   2002])", and note that "d is the minimal number of adjacent swaps" (line 477) holds
   only without ties. Plan §5 "Равенства" and ADR-0002 need the same change; because
   of ADR-0001 snapshots, decide before any task is closed in production.
2. Spearman: either (a) keep (2.21) and say explicitly that with ties it is
   Spearman's footnoted approximation (p. 87), or (b) use Pearson on mid-ranks
   (Spearman's definition; matches scipy, so tied cases also get an oracle) with the
   convention ρ := 0 when one ranking is fully tied. (b) is the more defensible
   choice; (a) is acceptable if documented. Either way, ADR-0002's wording ("scipy's
   variants") should not suggest the shortcut formula is the "real" Spearman.

### 2.10 Classic social-choice citations

| Claim in thesis | Line | Source | Verdict | Better accessible citation |
|---|---|---|---|---|
| Condorcet's principle, Condorcet winner, paradox | 269–270 | Condorcet 1785 [thesis ref. 9] | Correct [S: B38 §1.1; B40 ch. 2] | McLean & Urken (1995), *Classics of Social Choice* [B47] (English translations) |
| Fishburn calls min_j N(aᵢ, aⱼ) the "Condorcet function" | 271–272 | Fishburn 1977 [14] | Name not checked in primary **[U]**. Same rule is "Simpson (Simpson–Kramer, minimax)" in Zwicker 2016, p. 36 [P], defined there on Net_P; equivalent to N for complete strict rankings (own) | add "известна и като правило на Симпсън (maximin)" + [B40] |
| Nanson eliminates alternatives "под средното" | 273 | Nanson 1882 [25] | **Imprecise.** Nanson [B48] [P, archive.org scan]: three candidates: "all candidates who are not above the average are at once rejected" (p. 213); general case: candidates who "have not more than the average number of votes polled … are excluded" (p. 223) — i.e. ≤ average. Zwicker 2016, p. 37 [P] and Brandt et al. in [B40] ch. 4 use "below-average" (strict), citing Nanson and Niou (1987) [B49]. Both forms are Condorcet extensions [P: B40 p. 38] | Write "с точки по Борда, не по-високи от средното" (Nanson's own rule), or keep "под средното" and cite Niou/Zwicker for that variant |
| Kemeny: ranking with fewest pairwise disagreements | 273, 477 | Kemeny 1959 [21] | Correct [S: B40 p. 45]; Daedalus 88(4), 577–591, JSTOR 20026529 [S: BibBase]. Axiomatic characterisation: Young & Levenglick (1978) [B50] (Theorem 2.9 in B40, p. 45 [P]) | add Young & Levenglick 1978 or [B40] |
| Dodgson: fewest adjacent swaps to Condorcet winner | 273 | Dodgson 1876 [12] | Correct [P: B40 p. 45, "minimizing d_K"]; pamphlet, Clarendon Press 1876 [P: B40 ch. 5, p. 103] | McLean & Urken (1995) reprint [B47]; [B40] ch. 5 |
| Dodgson non-monotonic for ≥ 4 alternatives | 467 | Fishburn 1982 [15] | **Correct** [S: Caragiannis, Hemaspaandra & Hemaspaandra in B40, ch. 5, p. 122: "monotonic when there are at most three candidates and … nonmonotonic for each number of candidates greater than or equal to four (Fishburn, 1982, p. 132)"] | — |
| Dodgson not homogeneous | 467 | Fishburn 1977 [14] | **Correct** [S: B40 p. 46, "failing even to be homogeneous (Fishburn, 1977)"] | — |
| Copeland, Borda monotonic; Borda not Condorcet | 348, 355, Table 2.8 | Fishburn 1977 [14] | Correct [P: B40 p. 41 "Copeland, Simpson, and all proper scoring rules are monotonic"; Copeland Condorcet extension p. 36] | add [B40] |
| Arrow: five conditions incl. Pareto, ≥ 3 alternatives, ≥ 2 DMs | 394–400 | Arrow 1951 [5] | Theorem correct. The list with weak Pareto is the **1963 second-edition** form: "Arrow restated the conditions in the second edition" [P: SEP "Arrow's Theorem", §3]; the 1951 statement included a monotonicity ("positive association"/"non-negative responsiveness") condition later dropped [S: Wikipedia "Arrow's impossibility theorem"]; Blau (1957) [B51] is the usual reference for the 1951 flaw **[U]** content | Cite Arrow (1963), 2nd ed., or (2012) 3rd ed., Yale UP, doi:10.12987/9780300186987 |
| Black: single-peaked ⇒ Condorcet winner exists | 401 | Black 1948 [7] | **Needs "odd number of DMs"**: "if n is odd then P ∈ D_Condorcet" [P: B40, Theorem 2.21, p. 51]; SEP "Social Choice Theory" §3.3.1: "(assuming n is odd)" [P]. With even m only weak Condorcet winners are guaranteed [P: B40 fn. 81] | add "(при нечетен брой ЛВР)" |
| May: anonymity, neutrality, decisiveness, positive responsiveness ⇒ simple majority | 404, 408, 414 | May 1952 [23] | Correct [S: SEP "Social Choice Theory" §2.2; U. Endriss lecture slides: May's names "always decisive, egalitarian, neutral, positively responsive"]. "Равнопоставеност на гласуващите" ≈ May's "egalitarian" [S] | — |
| Harsanyi: weighted-sum group utility | 262 | Harsanyi 1955 [19] | Correct as commonly stated **[U]** (paper not read); bibliographic data verified | — |

Recommendation for the whole group: **keep** the classic references (they are the
correct priority citations) and add the Handbook of Computational Social Choice
(Brandt et al. 2016 [B40], open PDF) as the accessible, verifiable companion. Make the
three wording fixes above (Arrow 1963, Black odd n, Nanson ≤). No code impact
(Nanson, Kemeny, Dodgson are theory only, plan §1).

### 2.11 GCBIM and BIMBee1 (Andonov 2006, 2009, 2012)

No replacements sought. What comes from these sources and whether it is accessible:

| Rule / parameter | Thesis lines | Source | Status |
|---|---|---|---|
| GCBIM for "individual consultative" style; leader chooses ranking closest to aggregated or own; Borda aggregation; first alternative of chosen ranking is reference for next iteration | 531–533 | Andonov 2006 [B52], pp. 3–4 | [P] |
| Original distance: min over rankings of max over alternatives of |aᵢⱼ − aᵢc| / δᵢ (δᵢ = spread of positions), "maximal Tchebyshev distance" | 533 ("разликите … разделени на разсейването") | Andonov 2006, p. 4 | [P]; thesis description correct |
| Bee-inspired method (2006 name "GCBIM-bee1", later BIMBee1); lowest Borda alternatives dropped; stops below a threshold number | 566 | Andonov 2006, p. 4; dissertation §2.4 | [P]. Note: in 2006 each DM votes for **one** alternative, repeated votes lose 15% weight, Borda accumulated across iterations (p. 4) — later replaced by full rankings in the dissertation |
| Parameters t (alternatives in the last iteration) and τ (number dropped per iteration); rule Aⁱᵗᵉʳ = Aⁱᵗᵉʳ⁻¹ \ {aᵢ : bᵢ < τ} | 567–570 | Andonov 2012 [B53], §2.4.2–2.4.3, pp. 75–76 | [P]. Thesis line 570 ("q е означено с τ … праг върху точките") is accurate |
| Dissertation's Borda example gives n points to first place (1..n), thesis uses n − 1..0 | 312 vs diss. pp. 76–77 | Andonov 2012 | [P]; order-equivalent, no impact |
| Honeybee nest-site selection | 566 | Seeley & Visscher 2004 [thesis 31]; Andonov 2006 cites Seeley, Visscher & Passino 2006 (*American Scientist* 94) | thesis citation fine |
| Group Multichoice: VB client, Python server, methods list | 632 | Andonov 2012 | consistent with avtoreferat [P] |

Accessibility: Andonov 2006 open at iict.bas.bg/pecr/2006/57/3-8.pdf [P]; the
dissertation (169 pp.) and avtoreferat open at iict.bas.bg/konkursi/2012/F_Andonov/
[P]; Andonov 2009 (KDS 2009) only via an academia.edu upload (not read) — pages
25–30 from the author's own publication list [S: avtoreferat, p. 48, reference list item 5].

Bibliographic finding: the printed 2006 paper occupies **pp. 3–8** (six pages, page
numbers 3–8 on the scan, file name 3-8.pdf) [P]; the thesis (line 673) and the
author's own publication list (avtoreferat, items 6 and 3) give 3–9.

### 2.12 Thesis-internal inconsistency (found while auditing)

Line 131: "качествените критерии се оценяват по скала от 1 до 9, а не от 0".
Lines 89 and 128 and Table 2.1: quality and support "по скала от 1 до 10" (Table 2.1
contains the value 10). Pick one (1–10 fits the table). Low priority.

## 3. Bibliography corrections for the thesis

| Thesis line | Ref. | Correction | Basis |
|---|---|---|---|
| 673 | [3] Andonov 2006 | pages **3–8** (not 3–9); add URL https://www.iict.bas.bg/pecr/2006/57/3-8.pdf | [P] scan |
| 674 | [4] Andonov 2009 | pages 25–30 per author's list; publisher/series (ITHEA) **[U]** | [S: avtoreferat] |
| 675 | [5] Arrow 1951 | the conditions in the text are the 1963 form; cite Arrow, K. J. (1963). *Social Choice and Individual Values* (2nd ed.). New York: Wiley — or 3rd ed. (2012), Yale UP, https://doi.org/10.12987/9780300186987 | [P: SEP]; Crossref |
| 676 | [6] Belton & Gear | add https://doi.org/10.1016/0305-0483(83)90047-6 | Crossref |
| 677 | [7] Black 1948 | add https://doi.org/10.1086/256633 | Crossref |
| 678 | [8] Borda | add pp. 657–665; it is in the *Mémoires* part of the 1781 volume (printed 1784) | [P: Pulskamp transl.] |
| 683 | [13] Fishburn 1967 | journal title prefix "Letter to the Editor—"; otherwise correct | Crossref |
| 685 | [15] Fishburn 1982 | add https://doi.org/10.1016/0166-218X(82)90070-1 | Crossref |
| 686 | [16] Forman & Peniwati 1996 | pages 383–391 correct; add https://doi.org/10.13033/isahp.y1996.009 or replace by EJOR 108(1), 165–169 (1998), https://doi.org/10.1016/S0377-2217(97)00244-0 | [P]; Crossref |
| 687 | [17] Forman & Selly 2001 | add https://doi.org/10.1142/4281 | Crossref |
| 689 | [19] Harsanyi 1955 | add https://doi.org/10.1086/257678 | Crossref |
| 690 | [20] Hwang & Yoon 1981 | add series: Lecture Notes in Economics and Mathematical Systems (vol. 186 **[U]**) | Crossref (series name) |
| 691 | [21] Kemeny 1959 | no DOI; optionally add JSTOR 20026529 | [S: BibBase] |
| 693 | [23] May 1952 | add https://doi.org/10.2307/1907651 | Crossref |
| 695 | [25] Nanson | published **1883** (read 12 Oct 1882), vol. 19, pp. 197–240 | [P: scan title page "Read 12th October, 1882"; archive.org metadata year 1883] |
| 697 | [27] Rezaei 2015 | add https://doi.org/10.1016/j.omega.2014.11.009 | Crossref |
| 702 | [32] Spearman 1904 | correct; note that the shortcut formula (2.21) is not printed in it (§2.9) | [P] |
| 703 | [33] Triantaphyllou 2000 | add series Applied Optimization (vol. 44 **[U]**) | Crossref (series name) |
| 704 | [34] Zaraté et al. 2017 | add LNBIP volume (274 **[U]**) | Crossref (no volume field) |

Verified correct as written (Crossref): [11] de Almeida, Morais & Nurmi 2019, pp.
199–212; [14] Fishburn 1977, 33(3), 469–489; [18] Hansen & Ombler 2008, 15(3–4),
87–107; [22] Kendall 1938, 30(1/2), 81–93; [24] Mustajoki & Hämäläinen 2000, 38(3),
208–220; [30] Saaty 2008, 102(2), 251–318; [31] Seeley & Visscher 2004, 56(6),
594–601; [34] Zaraté et al. 2017, pp. 31–42.

## 4. Combined reference list

Access status: "read" = full text read in this audit; "metadata" = Crossref record
only; "not accessed".

- [B1] Saaty, T. L. (1977). A scaling method for priorities in hierarchical structures. *J. Math. Psychology*, 15(3), 234–281. https://doi.org/10.1016/0022-2496(77)90033-5 — read for the RI note, not re-read here.
- [B2] Saaty, T. L. (1980). *The Analytic Hierarchy Process*. New York: McGraw-Hill. — not accessed.
- [B3] Saaty, T. L. (2008). Relative measurement and its generalization in decision making … *RACSAM*, 102(2), 251–318. https://doi.org/10.1007/BF03191825 — read (https://rac.es/ficheros/doc/00576.PDF): Table 1 p. 256; 3×3 formulas p. 263; CR p. 264; rank reversal §16 pp. 302–303; group decisions §17 p. 304.
- [B4] Lootsma, F. A. (1993). Scale sensitivity in the multiplicative AHP and SMART. *J. Multi-Criteria Decision Analysis*, 2(2), 87–110. https://doi.org/10.1002/mcda.4020020205 — metadata.
- [B5] Salo, A. A., & Hämäläinen, R. P. (1997). On the measurement of preferences in the analytic hierarchy process. *JMCDA*, 6(6), 309–319. https://doi.org/10.1002/(SICI)1099-1360(199711)6:6<309::AID-MCDA163>3.0.CO;2-2 — metadata.
- [B6] Dong, Y., Xu, Y., Li, H., & Dai, M. (2008). A comparative study of the numerical scales and the prioritization methods in AHP. *EJOR*, 186(1), 229–242. https://doi.org/10.1016/j.ejor.2007.01.044 — metadata.
- [B7] Ishizaka, A., Balkenborg, D., & Kaplan, T. (2011). Influence of aggregation and measurement scale on ranking a compromise alternative in AHP. *JORS*, 62(4), 700–710. https://doi.org/10.1057/jors.2010.23 — metadata.
- [B8] Crawford, G., & Williams, C. (1985). A note on the analysis of subjective judgment matrices. *J. Math. Psychology*, 29(4), 387–405. https://doi.org/10.1016/0022-2496(85)90002-1 — metadata.
- [B9] Saaty, T. L., & Vargas, L. G. (1984). Comparison of eigenvalue, logarithmic least squares and least squares methods in estimating ratios. *Mathematical Modelling*, 5(5), 309–324. https://doi.org/10.1016/0270-0255(84)90008-3 — metadata.
- [B10] Barzilai, J. (1997). Deriving weights from pairwise comparison matrices. *JORS*, 48(12), 1226–1232. https://doi.org/10.1057/palgrave.jors.2600474 — metadata.
- [B11] Csató, L. (2018). Characterization of the row geometric mean ranking with a group consensus axiom. *Group Decision and Negotiation*, 27(6), 1011–1027. https://doi.org/10.1007/s10726-018-9589-3 — abstract only (arXiv:1706.07256).
- [B12] Aguarón, J., Escobar, M. T., Moreno-Jiménez, J. M., & Turón, A. (2020). The Triads Geometric Consistency Index in AHP-pairwise comparison matrices. *Mathematics*, 8(6), 926. https://doi.org/10.3390/math8060926 — read (zaguan.unizar.es/record/129619).
- [B13] Saaty, T. L. (1994). How to make a decision: The analytic hierarchy process. *Interfaces*, 24(6), 19–43. https://doi.org/10.1287/inte.24.6.19 — metadata.
- [B14] Aguarón, J., & Moreno-Jiménez, J. M. (2003). The geometric consistency index: Approximated thresholds. *EJOR*, 147(1), 137–145. https://doi.org/10.1016/S0377-2217(02)00255-2 — metadata.
- [B15] Koczkodaj, W. W. (1993). A new definition of consistency of pairwise comparisons. *Math. Comput. Modelling*, 18(7), 79–84. https://doi.org/10.1016/0895-7177(93)90059-8 — metadata.
- [B16] Bozóki, S., & Rapcsák, T. (2008). On Saaty's and Koczkodaj's inconsistencies of pairwise comparison matrices. *J. Global Optimization*, 42(2), 157–175. https://doi.org/10.1007/s10898-007-9236-z — metadata.
- [B17] Brunelli, M. (2018). A survey of inconsistency indices for pairwise comparisons. *Int. J. General Systems*, 47(8), 751–771. https://doi.org/10.1080/03081079.2018.1523156 — metadata.
- [B18] Forman, E., & Peniwati, K. (1996). Aggregating individual judgments and priorities with the analytic hierarchy process. *Proc. ISAHP 1996*, Vancouver, 383–391. https://doi.org/10.13033/isahp.y1996.009 — read (isahp.org/uploads/383-aggregating.pdf).
- [B19] Aczél, J., & Saaty, T. L. (1983). Procedures for synthesizing ratio judgements. *J. Math. Psychology*, 27(1), 93–102. https://doi.org/10.1016/0022-2496(83)90028-7 — metadata.
- [B20] Forman, E., & Peniwati, K. (1998). Aggregating individual judgments and priorities with the analytic hierarchy process. *EJOR*, 108(1), 165–169. https://doi.org/10.1016/S0377-2217(97)00244-0 — metadata.
- [B21] Ramanathan, R., & Ganesh, L. S. (1994). Group preference aggregation methods employed in AHP … *EJOR*, 79(2), 249–265. https://doi.org/10.1016/0377-2217(94)90356-5 — metadata.
- [B22] Ossadnik, W., Schinke, S., & Kaspar, R. H. (2016). Group aggregation techniques for AHP and ANP: A comparative analysis. *Group Decision and Negotiation*, 25(2), 421–457. https://doi.org/10.1007/s10726-015-9448-4 — metadata.
- [B23] Belton, V., & Gear, T. (1983). On a short-coming of Saaty's method of analytic hierarchies. *Omega*, 11(3), 228–230. https://doi.org/10.1016/0305-0483(83)90047-6 — metadata.
- [B24] Saaty, T. L., & Vargas, L. G. (1984). The legitimacy of rank reversal. *Omega*, 12(5), 513–516. https://doi.org/10.1016/0305-0483(84)90052-5 — metadata.
- [B25] Millet, I., & Saaty, T. L. (2000). On the relativity of relative measures … *EJOR*, 121(1), 205–212. https://doi.org/10.1016/S0377-2217(99)00040-5 — metadata.
- [B26] Maleki, H., & Zahir, S. (2013). A comprehensive literature review of the rank reversal phenomenon in the analytic hierarchy process. *JMCDA*, 20(3–4), 141–155. https://doi.org/10.1002/mcda.1479 — metadata.
- [B27] Wang, Y.-M., & Luo, Y. (2009). On rank reversal in decision analysis. *Math. Comput. Modelling*, 49(5–6), 1221–1229. https://doi.org/10.1016/j.mcm.2008.06.019 — metadata.
- [B28] Fishburn, P. C. (1967). Letter to the Editor—Additive utilities with incomplete product sets: Application to priorities and assignments. *Operations Research*, 15(3), 537–542. https://doi.org/10.1287/opre.15.3.537 — metadata.
- [B29] Hwang, C.-L., & Yoon, K. (1981). *Multiple Attribute Decision Making*. Lecture Notes in Economics and Mathematical Systems. Berlin: Springer. https://doi.org/10.1007/978-3-642-48318-9 — not accessed.
- [B30] Triantaphyllou, E. (2000). *Multi-Criteria Decision Making Methods: A Comparative Study*. Applied Optimization. Dordrecht: Kluwer. https://doi.org/10.1007/978-1-4757-3157-6 — not accessed.
- [B31] Krishnan, A. R. (2022). Past efforts in determining suitable normalization methods for multi-criteria decision-making: A short survey. *Frontiers in Big Data*, 5, 990699. https://doi.org/10.3389/fdata.2022.990699 — read via PMC (Table 2).
- [B32] Jahan, A., & Edwards, K. L. (2015). A state-of-the-art survey on the influence of normalization techniques in ranking … *Materials & Design*, 65, 335–342. https://doi.org/10.1016/j.matdes.2014.09.022 — metadata.
- [B33] Vafaei, N., Ribeiro, R. A., & Camarinha-Matos, L. M. (2016). Normalization techniques for multi-criteria decision making: AHP case study. *DoCEIS 2016*, IFIP AICT, 261–269. https://doi.org/10.1007/978-3-319-31165-4_26 — metadata.
- [B34] Vafaei, N., Ribeiro, R. A., & Camarinha-Matos, L. M. (2018). Selection of normalization technique for weighted average multi-criteria decision making. *DoCEIS 2018*, IFIP AICT, 43–52. https://doi.org/10.1007/978-3-319-78574-5_4 — metadata.
- [B35] Borda, J.-C. de (1784). Mémoire sur les élections au scrutin. *Mémoires de l'Académie Royale des Sciences*, année 1781, 657–665. English transl. R. J. Pulskamp (2009), https://gtfp.cs.rhul.ac.uk/pulskamp/Borda/voting.pdf — translation read.
- [B36] Emerson, P. (2013). The original Borda count and partial voting. *Social Choice and Welfare*, 40(2), 353–358. https://doi.org/10.1007/s00355-011-0603-9 — metadata.
- [B37] Black, D. (1976). Partial justification of the Borda count. *Public Choice*, 28(1), 1–15. https://doi.org/10.1007/BF01718454 — metadata.
- [B38] Faliszewski, P., Hemaspaandra, E., Hemaspaandra, L. A., & Rothe, J. (2009). Llull and Copeland voting computationally resist bribery and constructive control. *JAIR*, 35, 275–341. https://doi.org/10.1613/jair.2697 — read (arXiv:0809.4484v2, §1.1).
- [B39] Saari, D. G., & Merlin, V. R. (1996). The Copeland method I: Relationships and the dictionary. *Economic Theory*, 8(1), 51–76. https://doi.org/10.1007/BF01212012 — metadata.
- [B40] Brandt, F., Conitzer, V., Endriss, U., Lang, J., & Procaccia, A. D. (Eds.) (2016). *Handbook of Computational Social Choice*. Cambridge University Press. https://doi.org/10.1017/CBO9781107446984 — read (open PDF, cgi.cse.unsw.edu.au/~haziz/comsoc.pdf): Zwicker, W. S., ch. 2 "Introduction to the theory of voting", pp. 23–56, https://doi.org/10.1017/CBO9781107446984.003; Brandt, Brill & Harrenstein, ch. 3 "Tournament solutions", pp. 57–84, https://doi.org/10.1017/CBO9781107446984.004; Caragiannis, Hemaspaandra & Hemaspaandra, ch. 5 "Dodgson's rule and Young's rule".
- [B41] Spearman, C. (1904). The proof and measurement of association between two things. *American J. Psychology*, 15(1), 72–101. https://doi.org/10.2307/1412159 — read (archive.org OCR, item jstor-1412159; formulas partly garbled by OCR).
- [B42] Kendall, M. G. (1938). A new measure of rank correlation. *Biometrika*, 30(1–2), 81–93. https://doi.org/10.1093/biomet/30.1-2.81 — metadata.
- [B43] Kendall, M. G. (1945). The treatment of ties in ranking problems. *Biometrika*, 33(3), 239–251. https://doi.org/10.1093/biomet/33.3.239 — metadata.
- [B44] Kendall, M. G., & Gibbons, J. D. (1990). *Rank Correlation Methods* (5th ed.). London: Edward Arnold. — not accessed (edition confirmed via JASA review, https://doi.org/10.2307/2290477).
- [B45] Emond, E. J., & Mason, D. W. (2002). A new rank correlation coefficient with application to the consensus ranking problem. *JMCDA*, 11(1), 17–28. https://doi.org/10.1002/mcda.313 — metadata; definition read in Amodio, D'Ambrosio & Siciliano, arXiv:1502.06498.
- [B46] Fagin, R., Kumar, R., Mahdian, M., Sivakumar, D., & Vee, E. (2006). Comparing partial rankings. *SIAM J. Discrete Math.*, 20(3), 628–648. https://doi.org/10.1137/05063088X — metadata (conference version PODS 2004, https://doi.org/10.1145/1055558.1055568).
- [B47] McLean, I., & Urken, A. B. (Eds.) (1995). *Classics of Social Choice*. University of Michigan Press. https://doi.org/10.3998/mpub.12736 — metadata.
- [B48] Nanson, E. J. (1883). Methods of election. *Transactions and Proceedings of the Royal Society of Victoria*, 19, 197–240 (read 12 Oct 1882). — read (archive.org item biostor-258022).
- [B49] Niou, E. M. S. (1987). A note on Nanson's rule. *Public Choice*, 54(2), 191–193. https://doi.org/10.1007/BF00123006 — metadata.
- [B50] Young, H. P., & Levenglick, A. (1978). A consistent extension of Condorcet's election principle. *SIAM J. Applied Math.*, 35(2), 285–300. https://doi.org/10.1137/0135023 — metadata.
- [B51] Blau, J. H. (1957). The existence of social welfare functions. *Econometrica*, 25(2), 302–313 (end page **[U]**). https://doi.org/10.2307/1910256 — metadata.
- [B52] Andonov, F. (2006). An interactive method for group decision making. *Problems of Engineering Cybernetics and Robotics*, 57, 3–8. https://www.iict.bas.bg/pecr/2006/57/3-8.pdf — read.
- [B53] Андонов, Ф. (2012). *Методи за групово решаване на задачи на многокритериалния анализ* (дисертация). ИИКТ–БАН. https://iict.bas.bg/konkursi/2012/F_Andonov/disertacia.pdf — §2.4 read; avtoreferat read for the publication list.
- Also cited from other sources in this note: Arrow, K. J. (2012). *Social Choice and Individual Values* (3rd ed.). Yale UP. https://doi.org/10.12987/9780300186987 (Crossref lists 2017 online date) — metadata; Black, D. (1948). On the rationale of group decision-making. *J. Political Economy*, 56(1), 23–34. https://doi.org/10.1086/256633 — metadata; May, K. O. (1952). *Econometrica*, 20(4), 680–684. https://doi.org/10.2307/1907651 — metadata; Harsanyi, J. C. (1955). *J. Political Economy*, 63(4), 309–321. https://doi.org/10.1086/257678 — metadata; Fishburn, P. C. (1977). *SIAM J. Applied Math.*, 33(3), 469–489. https://doi.org/10.1137/0133030 — metadata; Fishburn, P. C. (1982). *Discrete Applied Math.*, 4(2), 119–134. https://doi.org/10.1016/0166-218X(82)90070-1 — metadata; Stanford Encyclopedia of Philosophy, entries "Arrow's Theorem" and "Social Choice Theory" — read (sections cited above).
