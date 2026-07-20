# PICS (Polar Idempotent Commutative Semiring)

Machine-checked verification (Prover9/Mace4) of the PICS axiom system — an idempotent commutative semiring equipped with a polarity operation `*`.

## Structure

- `prover9/pics-theorems.md` — the 10 axioms (M0-M3, S1-S3, SM1-SM2, P, PM) plus 20 derived theorems (De Morgan identities, dual semiring, partial order...). The `.in`/`.out` files are the Prover9 input/output used to prove these theorems.
- `mace4-generator/generator2.py` — generates the Mace4 `.in` files: `PICS_full.in` (full axiom set) and 11 `without_X.in` files (each axiom X removed, for independence testing).
- `mace4_inputs/` — the generated input files.
- `mace4-outputs/` — Mace4 run results.

## Results

- `mace4-output-full.txt`: a model of domain size 2 was found → **the PICS axiom system is consistent**.
- The 11 `mace4-output-{axiom name}.txt` files: each run found a counter-model → **all 11 axioms are independent** (none is derivable from the other 10).

## Usage

1. Edit/add axioms in `generator2.py` → run `python generator2.py` to regenerate the `.in` files in `mace4_inputs/`.
2. Run Mace4: `mace4 -f mace4_inputs/PICS_full.in > mace4-outputs/mace4-output-full.txt` (similarly for each `without_X.in`).
3. To prove theorems: edit `pics-theorems.in`, run Prover9, check `pics-theorems.out`.
