# Random Index (RI) for the AHP consistency ratio: which table to pin

Research note for HiveDecide (AHP criterion weights, `CR = CI / RI`,
`CI = (λmax − n)/(n − 1)`, AHP allowed for n ≤ 10 per `docs/plan.md`).

Verification legend used below:

- **[P]** checked against the primary source itself (full text read).
- **[S: X]** only checked through secondary source X; the primary was not accessible.
- **[U]** not verified at all; stated from general knowledge and must not be cited as is.

## 1. Summary and recommendation

**Pin Saaty (2008), RACSAM 102(2), 251–318, Table 6** [R8]. It is Saaty's own
table, it is open access, its method is described in the same passage (50,000
random reciprocal matrices per order, entries drawn uniformly from the 17 values
{1/9, …, 1, …, 9}), it covers n = 1..15, and the same paper explains the
CR ≤ 0.10 rule [P].

| n  | 1 | 2 | 3    | 4    | 5    | 6    | 7    | 8    | 9    | 10   |
|----|---|---|------|------|------|------|------|------|------|------|
| RI | 0 | 0 | 0.52 | 0.89 | 1.11 | 1.25 | 1.35 | 1.40 | 1.45 | 1.49 |

Source: Saaty 2008, Table 6 "Random index", p. 263 [R8] [P].
(Orders 11–15 in the same table: 1.52, 1.54, 1.56, 1.58, 1.59 [P]. Not needed here.)

Suggested code constant (`core`):

```python
# Saaty, T. L. (2008). RACSAM 102(2), 251-318, Table 6. doi:10.1007/BF03191825
RANDOM_INDEX = {
    1: 0.0,
    2: 0.0,
    3: 0.52,
    4: 0.89,
    5: 1.11,
    6: 1.25,
    7: 1.35,
    8: 1.40,
    9: 1.45,
    10: 1.49,
}
CR_THRESHOLD = 0.10  # accept iff CR <= 0.10 (Saaty 2008, p. 264; Saaty 1990, p. 13)
```

The thesis currently uses the older 1980 values (0.58, 0.90, 1.12) — see §5.

## 2. The sources

### 2.1 Saaty (1977), J. Math. Psychology — no RI table of the familiar kind

Saaty, T. L. (1977). A scaling method for priorities in hierarchical structures.
*Journal of Mathematical Psychology*, 15(3), 234–281. doi:10.1016/0022-2496(77)90033-5 [R1].

- Table 2 ("Measure of inconsistency μ") gives the average `(λmax − n)/(n − 1)`
  over **a sample of size 50** per order, for scales 1–5, 1–7, 1–9, 1–15, 1–20,
  1–90, n = 2..15 (pp. 248–249) [P]. Entries were "any of the integers 1–9 or their
  reciprocals at random", reciprocal in the transpose position [P].
- Row for the 1–9 scale, n = 2..10: 0.000, 0.416, 0.851, 1.115, 1.150, 1.345,
  1.334, 1.315, 1.420 [P]. These are **not** the 0.58/0.90/1.12 values.
- The acceptance rule is informal: "we can require the ratio to be very small;
  e.g., of the order of 0.1" (p. 249) [P]. The term "consistency ratio" does not
  appear; Wedley (2017) also says Saaty proposed CR "later" [R14] [P].
- Consequence: secondary sources that label 0.58, 0.90, 1.12, … as
  "Saaty (1977)" — e.g. Ishizaka & Labib (2011), Table 3 [R13] [P] — misattribute
  them. Do not cite 1977 for the RI table.

### 2.2 Saaty (1980), *The Analytic Hierarchy Process* (McGraw-Hill) — the classic table

Saaty, T. L. (1980). *The Analytic Hierarchy Process: Planning, Priority Setting,
Resource Allocation*. New York: McGraw-Hill. (No DOI.) [R2]

- Values usually reproduced, n = 3..10: 0.58, 0.90, 1.12, 1.24, 1.32, 1.41, 1.45,
  1.49; n = 1, 2: 0 [S: Alonso & Lamata 2006, Table 1, "Wharton 500" column, citing
  the 1980 book] [S: Tummala & Wan 1994, Table 1, citing the 1988 RWS reprint].
  n = 11: 1.51 [S: same].
- Derivation: a composite of two simulations, Saaty at Wharton (500 matrices) and
  Uppuluri at Oak Ridge National Laboratory (100 matrices) [S: Alonso & Lamata
  2006, p. 449; Tummala & Wan 1994, p. 216, both citing Saaty 1980/1988].
  The Oak Ridge run alone gave 0.382, 0.946, 1.220, 1.032, 1.468, 1.402, 1.350,
  1.464 for n = 3..10 [S: same tables] — visibly non-monotone, i.e. noisy.
- The book itself was not accessible; page number of the table **[U]**.
  The often-seen extension n = 12..15 = 1.48, 1.56, 1.57, 1.59 matches the
  Oak Ridge column rounded (1.476, 1.564, 1.568, 1.586) [S: Alonso & Lamata], so
  it presumably comes from the composite, but that is my inference **[U]**.

### 2.3 Saaty (1990), EJOR "How to make a decision" — no RI table

Saaty, T. L. (1990). How to make a decision: The analytic hierarchy process.
*European Journal of Operational Research*, 48(1), 9–26.
doi:10.1016/0377-2217(90)90057-I [R3].

- Defines CI = (λmax − n)/(n − 1) and CR as CI divided by the same index averaged
  over "a large number of reciprocal matrices of the same order whose entries are
  random"; accept if CR is "carefully specified to be about 10% or less" (p. 13) [P].
- Theorem 2: A is consistent iff λmax = n (p. 13) [P].
- **Contains no numeric RI table** (all 18 pages checked) [P]. Not citable for values.

### 2.4 Saaty's later recomputation — 0.52, 0.89, 1.11, …

- **Saaty (2008)**, RACSAM 102(2), 251–318, doi:10.1007/BF03191825 [R8].
  Section on consistency, pp. 263–264: "choose the entries of A above the main
  diagonal at random from the 17 values {1/9, 1/8, …, 1, 2, …, 8, 9}. Then fill in
  the entries of A below the diagonal by taking reciprocals. Put ones down the main
  diagonal and compute the consistency index. Do this 50,000 times and take the
  average, which we call the random index." Table 6, orders 1–15: 0, 0, 0.52, 0.89,
  1.11, 1.25, 1.35, 1.40, 1.45, 1.49, 1.52, 1.54, 1.56, 1.58, 1.59, plus first-order
  differences [P]. Same page argues the allowable CR "should be not more than about
  0.10" and why 10% cannot be made smaller [P]. (The text refers to "Table 5" once;
  it is a typo for Table 6 [P].)
- Saaty (2003), EJOR 145(1), 85–91, doi:10.1016/S0377-2217(02)00227-8 [R7]: uses
  CR in an example (C.R. = 0.083) but prints **no RI table** in the copy read [P].
- The same 0.52… values are widely said to appear in Saaty's *Fundamentals of
  Decision Making and Priority Theory* (RWS, 1994/2000) and in Saaty & Vargas,
  *Models, Methods, Concepts & Applications of the AHP* (Springer, 2001/2012);
  one secondary search snippet says Saaty notes there that the values "were
  recently recalculated" **[U]** — books not accessed.
- Size-dependent thresholds (CR ≤ 0.05 for n = 3, ≤ 0.08 for n = 4, ≤ 0.10 for
  n ≥ 5) are commonly attributed to Saaty (1994) **[U]**; secondary sources even
  disagree on the n = 4 value (0.08 vs 0.09). Not recommended for this project.

### 2.5 Independent recomputations

All values from Alonso & Lamata (2006), Table 1 [R11] unless noted; where a
primary was read it is marked [P].

| Source (runs per n) | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | Status |
|---|---|---|---|---|---|---|---|---|---|
| Uppuluri, Oak Ridge (100) | 0.382 | 0.946 | 1.220 | 1.032 | 1.468 | 1.402 | 1.350 | 1.464 | [S: R11, R10] |
| Saaty, Wharton (500) = 1980 table | 0.58 | 0.90 | 1.12 | 1.24 | 1.32 | 1.41 | 1.45 | 1.49 | [S: R11, R10] |
| Golden & Wang 1989 (1000) | 0.5799 | 0.8921 | 1.1159 | 1.2358 | 1.3322 | 1.3952 | 1.4537 | 1.4882 | [S: R11, R10] |
| Lane & Verdini 1989 (2500) | 0.52 | 0.87 | 1.10 | 1.25 | 1.34 | 1.40 | 1.45 | 1.49 | [S: R11, R10] |
| Forman 1990 (17,672–77,487) | 0.5233 | 0.8860 | 1.1098 | 1.2539 | 1.3451 | – | – | – | [S: R11] |
| Noble 1990 (5000) | 0.49 | 0.82 | 1.03 | 1.16 | 1.25 | 1.31 | 1.36 | 1.39 | [S: R11, R10] |
| Tummala & Wan 1994 (470,000 → 12,500) | 0.500 | 0.834 | 1.046 | 1.178 | 1.267 | 1.326 | 1.369 | 1.406 | [P: R10, Table 4] |
| Aguarón & Moreno-Jiménez 2003 (100,000) | 0.525 | 0.882 | 1.115 | 1.252 | 1.341 | 1.404 | 1.452 | 1.484 | [S: R11] |
| Alonso & Lamata 2006 (500,000) | 0.5247 | 0.8816 | 1.1086 | 1.2479 | 1.3417 | 1.4057 | 1.4499 | 1.4854 | [P: R11, Table 2] |
| Bozóki & Rapcsák 2008 | – | 0.884 | 1.109 | 1.249 | 1.341 | 1.404 | 1.451 | 1.486 | [S: Ágoston & Csató 2022, R16] |
| **Saaty 2008 (50,000)** | **0.52** | **0.89** | **1.11** | **1.25** | **1.35** | **1.40** | **1.45** | **1.49** | **[P: R8]** |

Bibliographic details and remarks:

- **Golden & Wang (1989)**, "An alternate measure of consistency", in Golden,
  Wasil & Harker (eds.), *The Analytic Hierarchy Process: Applications and
  Studies*, Springer, pp. 68–81, doi:10.1007/978-3-642-50244-6_5 [R4]
  (Crossref-verified metadata). 1000 runs per n [S: R10, R11]. Golden & Wang also
  propose a different consistency measure with its own cut-offs [S: Wedley 1993,
  R15].
- **Lane & Verdini (1989)**, "A consistency test for AHP decision makers",
  *Decision Sciences*, 20(3), 575–590, doi:10.1111/j.1540-5915.1989.tb01568.x [R5].
  2500 runs [S: R10, R11]. They argue the 10% rule is too restrictive because the
  SD of random CI is small [S: R11, p. 448].
- **Forman (1990)**, "Random indices for incomplete pairwise comparison
  matrices", *EJOR*, 48(1), 153–155, doi:10.1016/0377-2217(90)90072-J [R6].
  Complete-matrix values for n = 3..7 [S: R11]; the paper's main subject is
  incomplete matrices. Alonso & Lamata say the RI used with "Saaty only accepts …
  CR < 0.1" is the one "obtained by Forman" (p. 447) [P] — note Expert Choice uses
  Forman's indices [S: Ishizaka & Labib 2011, R13].
- **Noble (1990)**: values come from E. E. Noble, *Consistency in the Analytic
  Hierarchy Process*, Master's thesis, Eastern Michigan University, 1990
  [S: R10, ref. 4]. Alonso & Lamata instead cite Noble & Sanchez, *Theory and
  Decision* 34 (1990) 99–108 [R11]; Crossref shows that article is **1993**,
  34(2), 99–108, doi:10.1007/BF01074896 [R9]. Values not verified in either primary.
- **Tummala & Wan (1994)**. Read: "On the sampling distribution of the random
  consistency index of AHP", *Proc. ISAHP 1994*, pp. 215–222,
  doi:10.13033/isahp.y1994.034 [R10] [P]. Uses the power method; sample sizes
  N = 470,000 (n = 3) down to 12,500 (n = 10) (Table 4) [P]. The journal paper
  "On the mean random inconsistency index of AHP", *Computers & Industrial
  Engineering*, 27(1–4), 401–404, doi:10.1016/0360-8352(94)90319-0 [R10b] was not
  read; that its values equal the proceedings version is **[U]**.
- **Donegan & Dodd (1991)**, "A note on Saaty's random indexes", *Mathematical
  and Computer Modelling*, 15(10), 135–137, doi:10.1016/0895-7177(91)90098-R [R12]
  (Crossref metadata only). Values and method **[U]** — not accessed.
- **Aguarón & Moreno-Jiménez (2003)**, "The geometric consistency index:
  Approximated thresholds", *EJOR*, 147(1), 137–145,
  doi:10.1016/S0377-2217(02)00255-2 [R17]. 100,000 matrices; RI for n ≤ 16
  [S: R11, R16]. Primary not read.
- **Alonso & Lamata (2006)**, "Consistency in the analytic hierarchy process: a
  new approach", *Int. J. Uncertainty, Fuzziness and Knowledge-Based Systems*,
  14(4), 445–459, doi:10.1142/S0218488506004114 [R11] [P]. 100,000 and 500,000
  matrices per n, Saaty scale {1/9 … 9} uniform, EV method; also reports SDs
  (e.g. n = 3: 0.697; n = 10: 0.207) (Table 2, p. 450) [P]. Proposes a regression
  criterion on λmax instead of CR.

## 3. Why the published values differ

1. **Sample size.** 50 matrices (1977) [R1], 100 / 500 (1980 composite), 1000–5000
   (1989–90), 50,000 (Saaty 2008), 10⁵–5·10⁵ (2003–2006) [R1, R8, R10, R11]. With
   SD(CI) ≈ 0.70 at n = 3 [R11, Table 2], the standard error of a 500-sample mean is
   ≈ 0.70/√500 ≈ 0.031 and of a 100-sample mean ≈ 0.07 (own calculation). That
   alone explains 0.58 vs ≈0.525 at n = 3 and the non-monotone Oak Ridge column.
   Alonso & Lamata name "the simulation method and the number of generated
   matrices" as the cause [R11, p. 449] [P].
2. **How entries are drawn.** 1977 drew "integers 1–9 or their reciprocals"
   [R1, p. 248] — read literally that is 18 outcomes with 1 counted twice; later
   work draws uniformly from the 17 distinct values [R8, R11]. RI also depends on
   the largest scale value (Bozóki & Rapcsák 2008, as summarised in [R16]); compare
   the 1–5 … 1–90 rows of 1977 Table 2 [R1].
3. **Eigenvalue computation.** Tummala & Wan attribute part of the spread to
   numerically unstable λmax computation (Saaty's normalise-at-the-end powering),
   which "will overstate the value of the mean" (pp. 217, 221, endorsing Noble)
   [R10] [P]. Their own and Noble's values are the lowest in the table.
4. **Rounding and compositing.** Saaty's tables are 2-decimal; the 1980 table merges
   two different experiments [S: R11, R10].
5. **Later revision by Saaty himself.** The 2008 table replaces 0.58/0.90/1.12/1.24/
   1.32/1.41 with 0.52/0.89/1.11/1.25/1.35/1.40, keeping 1.45/1.49 [R8] [P]; the
   revised values sit close to the large independent runs (Alonso & Lamata,
   Aguarón) [R11].
6. **n = 1, 2.** Every 1×1 and 2×2 reciprocal matrix is consistent (a₁₂·a₂₁ = 1), so
   λmax = n and CI = 0 [R3, Theorem 2]; RI is listed as 0 [R8, Table 6]. CR = 0/0 is
   undefined, so the convention is to skip the check (CR := 0). This is not a
   difference between sources, only a definitional gap code must handle.

## 4. Why Saaty (2008) for HiveDecide

- **Saaty's own and current.** It is the inventor's revised table, not a third-party
  recomputation, so the thesis can still say "Saaty's table" as `docs/plan.md` does.
- **Verifiable.** Open-access PDF at the journal site (rac.es), DOI, page, table
  number, and the simulation procedure are all in one place [R8]. The 1980 table
  can only be checked through secondary sources here, and the frequently-cited
  "1977" attribution is wrong (§2.1).
- **Method is reproducible.** 17-value uniform scale, 50,000 runs — the same set-up
  a reviewer would use; matches 5·10⁵-run recomputations to within ~0.01 except
  n = 7 (1.35 vs 1.342) [R8, R11].
- **Covers n ≤ 10** (indeed ≤ 15), so the plan's limit is fully covered.
- **Threshold in the same source.** CR ≤ 0.10, justified on p. 264 [R8]; the 1990
  EJOR paper gives the same "about 10% or less" [R3].
- Trade-off to state in the thesis: the 1980 values are the ones most reproduced in
  textbooks and tools; the 2008 RIs are smaller for n = 3–5, so CR is slightly
  larger (stricter) for the same judgments (e.g. ~11% higher at n = 3).

Alternative, if the author prefers to keep the thesis as written: Saaty (1980) is
defensible and widely used, but cite the book (not 1977), and note that its values
could only be checked via Alonso & Lamata (2006).

**Threshold wording.** Saaty (2008) says "not more than about 0.10" [R8]; the thesis
says "CR ≤ 0,1" and the plan rejects when "CR > 0,1". These agree with each other.
A strict "CR < 0.10" (as phrased in the research request) would differ only at
CR = 0.10 exactly; use `<=` to match Saaty and the thesis.

## 5. Check against the thesis text

File: `docs/thesis/Дипломна работа – Система с методи за групово решаване на задачи на многокритериалния анализ.txt`

- **Line 170**: "За k = 3, 4 и 5 стойностите на RI са съответно 0,58; 0,90 и 1,12
  [29]" with [29] = Saaty (1980), McGraw-Hill (line 699). These are the 1980 values
  — **mismatch** with the recommended 2008 table (0.52; 0.89; 1.11). If Saaty (2008)
  is pinned, change the values and add the reference:
  Saaty, T. L. (2008). Relative measurement and its generalization in decision
  making… *RACSAM*, 102(2), 251–318. https://doi.org/10.1007/BF03191825
- **Line 171** (worked example, A = [[1, 2, 1/2], [1/2, 1, 1/3], [2, 3, 1]]): own
  recomputation gives λmax ≈ 3.0092, CI ≈ 0.0046, w ≈ (0.297; 0.163; 0.540).
  CR = 0.0046/0.58 ≈ 0.008 (as written) but **≈ 0.009** with RI = 0.52. The thesis
  rounds CI to 0.005; 0.005/0.52 ≈ 0.0096, so write "CR ≈ 0,009". Conclusion
  ("далеч под прага 0,1") is unaffected.
- **Line 170** "CR ≤ 0,1" and "при един или два критерия … проверка не е нужна":
  consistent with Saaty [R3, R8] and with `docs/plan.md`.
- No other RI values or RI-specific citations were found in the thesis text.

## References

- [R1] Saaty, T. L. (1977). A scaling method for priorities in hierarchical
  structures. *Journal of Mathematical Psychology*, 15(3), 234–281.
  https://doi.org/10.1016/0022-2496(77)90033-5 — read via Web Archive copy of
  superdecisions.com/sd_resources/Paper_ScalingMethod.pdf.
- [R2] Saaty, T. L. (1980). *The Analytic Hierarchy Process: Planning, Priority
  Setting, Resource Allocation*. New York: McGraw-Hill. — not accessed.
- [R3] Saaty, T. L. (1990). How to make a decision: The analytic hierarchy process.
  *EJOR*, 48(1), 9–26. https://doi.org/10.1016/0377-2217(90)90057-I — full text read
  (vpp.sbuf.se copy).
- [R4] Golden, B. L., & Wang, Q. (1989). An alternate measure of consistency. In
  B. L. Golden, E. A. Wasil, & P. T. Harker (Eds.), *The Analytic Hierarchy Process:
  Applications and Studies* (pp. 68–81). Springer.
  https://doi.org/10.1007/978-3-642-50244-6_5 — not accessed.
- [R5] Lane, E. F., & Verdini, W. A. (1989). A consistency test for AHP decision
  makers. *Decision Sciences*, 20(3), 575–590.
  https://doi.org/10.1111/j.1540-5915.1989.tb01568.x — not accessed.
- [R6] Forman, E. H. (1990). Random indices for incomplete pairwise comparison
  matrices. *EJOR*, 48(1), 153–155. https://doi.org/10.1016/0377-2217(90)90072-J —
  not accessed.
- [R7] Saaty, T. L. (2003). Decision-making with the AHP: Why is the principal
  eigenvector necessary. *EJOR*, 145(1), 85–91.
  https://doi.org/10.1016/S0377-2217(02)00227-8 — full text read (uchicago.edu copy).
- [R8] Saaty, T. L. (2008). Relative measurement and its generalization in decision
  making. Why pairwise comparisons are central in mathematics for the measurement of
  intangible factors. The analytic hierarchy/network process. *RACSAM – Rev. R. Acad.
  Cien. Serie A. Mat.*, 102(2), 251–318. https://doi.org/10.1007/BF03191825 — full
  text read: https://rac.es/ficheros/doc/00576.PDF (Table 6, p. 263; threshold p. 264).
- [R9] Noble, E. E., & Sanchez, P. P. (1993). A note on the information content of a
  consistent pairwise comparison judgment matrix of an AHP decision maker. *Theory
  and Decision*, 34(2), 99–108. https://doi.org/10.1007/BF01074896 — not accessed.
- [R10] Tummala, V. M. R., & Wan, Y. W. (1994). On the sampling distribution of the
  random consistency index of analytic hierarchy process (AHP). *Proceedings of the
  International Symposium on the AHP (ISAHP 1994)*, 215–222.
  https://doi.org/10.13033/isahp.y1994.034 — full text read
  (isahp.org/uploads/215-on-the-sampling.pdf; OCR of Table 1 partly garbled).
- [R10b] Tummala, V. M. R., & Wan, Y. W. (1994). On the mean random inconsistency
  index of analytic hierarchy process (AHP). *Computers & Industrial Engineering*,
  27(1–4), 401–404. https://doi.org/10.1016/0360-8352(94)90319-0 — not accessed.
- [R11] Alonso, J. A., & Lamata, M. T. (2006). Consistency in the analytic hierarchy
  process: A new approach. *IJUFKS*, 14(4), 445–459.
  https://doi.org/10.1142/S0218488506004114 — full text read (CiteSeerX preprint).
- [R12] Donegan, H. A., & Dodd, F. J. (1991). A note on Saaty's random indexes.
  *Mathematical and Computer Modelling*, 15(10), 135–137.
  https://doi.org/10.1016/0895-7177(91)90098-R — metadata only.
- [R13] Ishizaka, A., & Labib, A. (2011). Review of the main developments in the
  analytic hierarchy process. *Expert Systems with Applications*, 38(11),
  14336–14345. https://doi.org/10.1016/j.eswa.2011.04.143 — preprint read.
- [R14] Wedley, W. C. (2017). Saaty 1977: The building blocks. *IJAHP*, 9(3),
  starts p. 311 (end page **[U]**). https://doi.org/10.13033/ijahp.v9i3.532 — full text read.
- [R15] Wedley, W. C. (1993). Relative measure of the consistency ratio. *Proc. ISAHP
  1993* (isahp.org/uploads/185-relative.pdf) — skimmed only.
- [R16] Ágoston, K. Cs., & Csató, L. (2022). Inconsistency thresholds for incomplete
  pairwise comparison matrices. *Omega*, 108, 102576 (arXiv:2102.10558) — arXiv
  version read; journal details **[U]**.
- [R17] Aguarón, J., & Moreno-Jiménez, J. M. (2003). The geometric consistency index:
  Approximated thresholds. *EJOR*, 147(1), 137–145.
  https://doi.org/10.1016/S0377-2217(02)00255-2 — not accessed.
