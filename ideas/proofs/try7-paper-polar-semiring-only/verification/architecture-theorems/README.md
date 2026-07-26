# architecture-theorems/

Prover9 proofs of the propositions of Section 3 of the paper
(`doc3-structures.tex`), each with the minimal hypotheses the paper uses for
that block. The blocks follow the paper's three-layer structure
(Algebraic / Reflection / Integration).

## Files

- `generator.py` — generates the 40 goal files plus `all-blocks.in`.
- `prover9-inputs/block*.in` — one file per goal; the header of each file
  records its hypotheses and the corresponding paper label.
- `prover9-inputs/all-blocks.in` — a concatenated reading copy; split with
  `csplit -z -f block_ -b '%02d.in' all-blocks.in '/^% ==== Block/' '{*}'`.
- `prover9-outputs/*.out` — reference Prover9 outputs.
- `prover9-minimality/` — the reflected-modules block re-run with J0 removed.

## Running

```sh
python3 generator.py
for f in prover9-inputs/block*.in; do prover9 -f "$f"; done
```

## Results — 40 / 40 goals proved

| Block | Proposition (label) | Hypotheses | Goals | Result |
|:---:|---|---|:---:|:---:|
| 1 | `prop:duality` | J1–J3, T1–T3, P + definitions (no J0/TJ1/TJ2/PJ) | 8 | all proved |
| 2 | `prop:reflected-modules` | block 1 + J0 | 7 | all proved |
| 3 | `prop:order-compat` | all 11 axioms | 4 | all proved |
| 4 | `prop:order-structure` | all 11 axioms | 9 | all proved |
| 5 | `thm:fundamental` (dual structure) | all 11 axioms | 11 | all proved |
| 6 | *(optional)* converse of `prop:order-compat` (4)⇒(1) | 10 axioms, PJ replaced by absorption | 1 | proved |

Block 5 proves all eleven dual-structure goals, confirming part (1) of the
Fundamental Structure Theorem.

### Minimality check

`prover9-minimality/` re-runs block 2 without J0. Six monoid goals still prove;
only "meet idempotent" (RS1d) fails, confirming that J0 is needed for exactly
that one goal.

See [`../NOTES.md`](../NOTES.md) for further discussion, including a correction
to the OS5 goal ("ew is greatest").
