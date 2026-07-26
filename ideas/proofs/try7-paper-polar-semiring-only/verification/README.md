# Machine verification for *Polar Semirings*

This directory contains the [Prover9 and Mace4](https://www.cs.unm.edu/~mccune/prover9/)
scripts that machine-check the results of the paper *Polar Semirings*. Every
input file uses the paper's notation, in which the primitives are
`v` (join, ∨), `*` (tensor, ⊗), `star()` (polarity, ᐟ), `ev` (e∨), and
`eo` (e⊗); the operations `meet` (∧), `plus` (⊕), `ew` (e∧), and `ep` (e⊕)
are derived.

## Layout

| Folder | Tool | Question | Result |
|---|---|---|---|
| [`independence/`](independence/) | Mace4 | Are the 11 axioms consistent and mutually independent? | Consistent; all 11 independent (largest countermodel: 5 elements) |
| [`architecture-theorems/`](architecture-theorems/) | Prover9 | Do the Section 3 propositions hold? | 40 / 40 goals proved |
| [`bga-implies-ps/`](bga-implies-ps/) | Prover9 | Does every bounded Girard algebra satisfy the 11 PS axioms? | 11 / 11 axioms + 5 lemmas proved; 1 auxiliary goal inconclusive |
| [`ps-not-bga/`](ps-not-bga/) | Mace4 + Python | Is there a PS that is not a BGA? | Yes — a 3-element model |
| [`non-distributive/`](non-distributive/) | Mace4 + Python | Must the induced lattice be distributive? | No — a 5-element model (the diamond M₃) |

Shared module: [`ps_model.py`](ps_model.py) parses a Mace4 output file, rebuilds
the finite model, and brute-force checks the 11 axioms independently of the
solver.

Extended commentary — cross-references to specific paper locations, notable
findings, and two corrections to the original task specification — is collected
in [`NOTES.md`](NOTES.md).

## Requirements

Prover9 and Mace4 must be on the `PATH`, or set `PROVER9_BIN` to their
directory:

```sh
git clone --depth 1 https://github.com/ai4reason/Prover9.git
cd Prover9 && make all
export PROVER9_BIN="$PWD/bin"
```

The Python scripts require only the standard library (Python 3.6+).

## Reproducing

```sh
./run-all.sh
```

`run-all.sh` regenerates every `.in` file, runs every Prover9/Mace4 job, runs
the cross-checking Python scripts, and prints a summary. The committed `.out`
and `.txt` files are the reference outputs from the authors' run; `run-all.sh`
overwrites them in place.

To run a single folder, see the `README.md` inside it.

## Notation reference

| Role | ASCII token | Primitive? |
|---|---|:---:|
| join ∨ | `v` (infix) | yes |
| tensor ⊗ | `*` (infix) | yes |
| polarity ᐟ | `star(x)` | yes |
| e∨ | `ev` | yes |
| e⊗ | `eo` | yes |
| meet ∧ | `meet(x,y) = star(star(x) v star(y))` | derived |
| plus ⊕ | `plus(x,y) = star(star(x) * star(y))` | derived |
| e∧ | `ew = star(ev)` | derived |
| e⊕ | `ep = star(eo)` | derived |
| residual → | `res(x,y)` | BGA only, absent from PS |

The order is encoded as `x <= y  :<->  x v y = y`. The residual `res` appears
only in [`bga-implies-ps/`](bga-implies-ps/), where the bounded Girard algebra
axioms are stated.

## License

Released under the MIT License; see [`LICENSE`](LICENSE).
