# non-distributive/

A concrete witness that the lattice induced by a Polar Semiring need not be
distributive (`prop:order-structure`, `doc3-structures.tex`).

## Files

- `mace4-inputs/non-distributive.in` — the 11 PS axioms plus the negation of
  the distributive law, all as assumptions.
- `mace4-outputs/mace4-output.txt` — reference Mace4 output.
- `verify.py` — rebuilds the model, brute-force checks the 11 axioms, and lists
  every triple witnessing the failure of distributivity.
- `emit_latex.py` — emits the model as a LaTeX snippet (uses the paper's macros).
- `model.tex` — the emitted snippet, ready to paste into the paper.

## Running

```sh
mace4 -f mace4-inputs/non-distributive.in > mace4-outputs/mace4-output.txt
python3 verify.py
python3 emit_latex.py > model.tex
```

## Result — the diamond M₃ (5 elements)

Mace4 exhausts sizes 2–4 and finds a model at size 5, so **5 is minimal**
(consistent with the smallest non-distributive lattice having 5 elements). The
lattice is exactly M₃: e∨ < a, b, c < e∧ with a, b, c pairwise incomparable.
The polarity swaps e∨ and e∧ and fixes a, b, c; the tensor has e⊗ = a.

Distributivity fails at 6 triples, for example
a ∨ (b ∧ c) = a ∨ e∨ = a while (a ∨ b) ∧ (a ∨ c) = e∧ ∧ e∧ = e∧.
`verify.py` confirms all 11 axioms hold and lists the witnesses.

`model.tex` is ready to drop in as an `\begin{example}` replacing the paper's
`\noteAI` marker; see [`../NOTES.md`](../NOTES.md).

## Note on the input encoding

The negated distributive law is placed in `formulas(assumptions)`, not
`formulas(goals)`: Mace4 negates goals, so a goal here would search for the
opposite property. See [`../NOTES.md`](../NOTES.md).
