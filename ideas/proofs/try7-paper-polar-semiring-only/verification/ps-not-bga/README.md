# ps-not-bga/

Machine evidence for PS ⇏ BGA (`thm:impossibility`, `doc4-compare.tex`):
Mace4 searches for a finite Polar Semiring admitting no dualizing element, and
`verify.py` re-checks the model it finds.

## Files

- `mace4-inputs/no-dualizing-element.in` — the 11 PS axioms together with the
  negation of the dualizing condition `(†)` (`eq:dagger`), all as assumptions.
- `mace4-outputs/mace4-output.txt` — reference Mace4 output.
- `verify.py` — rebuilds the model and brute-force checks (1) the 11 axioms and
  (2) that no element is a dualizing element.

## Running

```sh
mace4 -f mace4-inputs/no-dualizing-element.in > mace4-outputs/mace4-output.txt
python3 verify.py
```

## Result — a 3-element model

Mace4 exhausts domain size 2 and finds a model at size 3, so **3 is minimal**.
Naming the chain e∨ < m < e∧: the polarity swaps e∨ and e∧ and fixes m; the
tensor coincides with meet, with e⊗ = e∧.

`verify.py` confirms all 11 axioms hold and that no `q` is a dualizing element:

| q | witness (a, b) | a ⊗ b ≤ q | b ≤ aᐟ |
|:---:|:---:|:---:|:---:|
| 0 | (0, 0) | true | false |
| 1 | (2, 2) | false | true |
| 2 | (0, 2) | true | false |

Hence PS ⇏ BGA. This is a finite, independent supplement to the paper's
analytic proof on the continuous `[0,1]` model; the two use different tensors.
See [`../NOTES.md`](../NOTES.md).

## Note on the input encoding

The negated dualizing condition is placed in `formulas(assumptions)`, not
`formulas(goals)`: Mace4 negates goals, so a goal here would search for the
opposite property. See [`../NOTES.md`](../NOTES.md).
