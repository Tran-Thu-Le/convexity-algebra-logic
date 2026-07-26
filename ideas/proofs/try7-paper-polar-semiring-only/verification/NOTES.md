# Notes

Extended commentary for the machine-verification directory: paper
cross-references, notable findings, task-specification corrections, and the
one incomplete goal. Concise per-folder documentation lives in each folder's
`README.md`; this file holds everything that is discussion rather than
instruction.

## Contents

- [Mapping to `\noteAI` markers in the paper](#mapping-to-noteai-markers-in-the-paper)
- [Notable findings](#notable-findings)
- [Corrections to the original task specification](#corrections-to-the-original-task-specification)
- [The one inconclusive goal](#the-one-inconclusive-goal)
- [Scope](#scope)

## Mapping to `\noteAI` markers in the paper

Three `\noteAI` markers in the LaTeX source are answered by results here. This
table is the checklist for editing the manuscript once the outputs have been
reviewed.

| `\noteAI` location | Note content | Answering folder | Edit to make |
|---|---|---|---|
| `doc2-polar-semiring.tex`, `thm:independence` | "fill in the maximal cardinality"; "decide: appendix or supplementary"; and the request to re-run under the new notation | `independence/` | Fill in **5**; put the 11-row table in the body and the detailed model tables in an appendix or supplement; delete the marker |
| `doc4-compare.tex`, end of the `thm:impossibility` proof | "perform your own final check (and, if desired, a Mace4 confirmation on a finite subchain)" | `ps-not-bga/` | Add a short remark about the 3-element model; delete the marker |
| `doc3-structures.tex`, end of the `prop:order-structure` proof | "add the diamond M₃ with a suitable involution ... otherwise the claim should be softened" | `non-distributive/` | Paste `non-distributive/model.tex` as an `\begin{example}`; change the closing sentence to "...fails in general (\Cref{ex:nondistributive})"; delete the marker |

The remaining `\noteAI` markers (author name, subtitle, MSC codes, the
Aglianò 2025 citation, the ±∞ convention in `ex:tropical`) are outside the
scope of this directory and require manual attention.

## Notable findings

1. **The non-distributive countermodel is exactly M₃.** The paper only
   *suggests* using the diamond M₃; Mace4 finds precisely M₃ and confirms that
   5 is the minimum size. The involution fixes all three middle elements and
   swaps bottom with top.

2. **The PS-not-BGA model needs only 3 elements**, smaller than the
   4-element model of the earlier archived draft. It is a 3-element chain with
   `tensor = meet`, a mechanism quite different from the continuous `[0,1]`
   model of the paper (where the tensor is ordinary multiplication), so it
   serves as an independent second example rather than a shrunk copy.

3. **The minimality claim about J0 holds.** Re-running the reflected-modules
   block with J0 removed: the six monoid goals still prove, and only
   "meet idempotent" fails — matching the paper's split of
   `prop:reflected-modules` into the free parts (1)(2) and the J0-dependent
   part (3). See `architecture-theorems/prover9-minimality/`.

4. **The converse direction of `prop:order-compat` also proves.** Dropping PJ
   and assuming the two absorption laws instead, Prover9 recovers PJ (optional
   block 6). Together with block 3 this shows statements (1)–(4) are genuinely
   equivalent.

5. **The eleven-row derivation table `tab:eleven` is fully confirmed.** In
   `bga-implies-ps/`, every PS axiom follows from the BGA axioms once the
   polarity is defined by `star(x) = res(x, ep)`, including the four rows the
   paper marks "needs proof" (J3, TJ1, TJ2, PJ). The four residuation lemmas
   prove **without** using BGA5, exactly as the paper states.

## Corrections to the original task specification

Two instructions in the original task description were incorrect and were
changed after empirical checking.

1. **Mace4 negates goals.** The task suggested placing an existential formula
   such as `exists x y z (...)` in `formulas(goals)`. Mace4 searches for a
   counterexample to a goal, so a goal of that form would make Mace4 look for a
   model in which distributivity *always holds* — the opposite of the intent.
   The negated property is therefore placed in `formulas(assumptions)` in
   `independence/`, `ps-not-bga/`, and `non-distributive/`.

2. **The "ew is greatest" goal was stated backwards.** The task gave
   `x v ew = x`; the correct form is `x v ew = ew`, since
   `a <= ew  iff  a v ew = ew`. The corrected form is used in
   `architecture-theorems/prover9-inputs/block4-OS5.in`. The form `x v ew = x`
   would instead assert that `ew` is the *least* element.

## The one inconclusive goal

Exactly one goal in this directory did not finish:
`bga-implies-ps/prover9-outputs/extra-meet.out` (the derived meet coincides
with the lattice meet, `star(star(x) v star(y)) = mt(x,y)`). Prover9 was cut
off when its time budget expired; it returned neither `THEOREM PROVED` nor
`SEARCH FAILED`. **This is not a negative result.** The partial output is kept
for continuation.

Suggested next step: raise `assign(max_seconds, ...)`, or prove it in two
steps as the paper does — use the antitonicity lemma plus the bijectivity of
`star` to show that `star(star(x) v star(y))` is the greatest lower bound,
rather than attacking the equation directly. This is the final sentence of the
`thm:bga-implies-ps` proof, which the paper argues order-theoretically; it is
likely hard for an equational prover rather than false.

## Scope

Nothing in this directory modifies the LaTeX sources in the paper directory.
The scripts only generate solver inputs, run the solvers, and parse their
outputs. Incorporating the numerical results into the manuscript (the
cardinality, the M₃ example, the `(†)` confirmation) is a separate step, to be
done after the outputs have been reviewed.
