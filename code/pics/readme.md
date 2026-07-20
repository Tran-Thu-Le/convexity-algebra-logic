# PICS (Polar Idempotent Commutative Semiring)

Machine-checked verification (Prover9/Mace4) of the PICS axiom system — an idempotent commutative semiring equipped with a polarity operation `*`.

## Structure

- `prover9/pics-theorems.md` — the 11 axioms (M0-M3, S1-S3, SM1-SM2, P, PM) plus 20 derived theorems (De Morgan identities, dual semiring, partial order...). The `.in`/`.out` files are the Prover9 input/output used to prove these theorems.
- `mace4-generator/generator2.py` — generates the Mace4 `.in` files: `PICS_full.in` (full axiom set) and 11 `without_X.in` files (each axiom X removed, for independence testing).
- `mace4_inputs/` — the generated input files.
- `mace4-outputs/` — Mace4 run results.

## Results

- `mace4-output-full.txt`: a model of domain size 2 was found → **the PICS axiom system is consistent**.
- The 11 `mace4-output-{axiom name}.txt` files: each run found a counter-model → **all 11 axioms are independent** (none is derivable from the other 10).

## Usage

1. Edit/add axioms in `generator2.py` → run `python generator2.py` to regenerate the `.in` files in `mace4_inputs/`.
2. Run Mace4: `mace4 -f mace4_inputs/PICS_full.in > mace4-outputs/mace4-output-full.txt` (similarly for each `without_X.in`).
3. To reproduce `pics-theorems.out` with Prover9, see below.

## Reproducing `pics-theorems.out` (Prover9)

`pics-theorems.in` holds 20 self-contained blocks (axioms + one goal each, for Theorems 1-20), separated by `% ==== Theorem N: ... ====` markers. `pics-theorems.out` is the saved output ("THEOREM PROVED" for all 20).

1. **Build Prover9** (not in apt; build from source):
   ```bash
   git clone --depth 1 https://github.com/ai4reason/Prover9.git
   cd Prover9 && make all   # binary at Prover9/bin/prover9
   ```
2. **Split into 20 blocks** (Prover9 runs one `formulas(goals)` per call):
   ```bash
   csplit -z -f block_ -b '%02d.in' pics-theorems.in '/^% ==== Theorem/' '{*}'
   ```
3. **Run each block**:
   ```bash
   for f in block_*.in; do echo "=== $f ==="; ./Prover9/bin/prover9 -f "$f"; done > my-output.out
   ```
4. **Check**: `grep -c "THEOREM PROVED" my-output.out` should be 20, with no `fatal`/`search failed` lines.

*(Reference build: Prover9 LADR-2017-11A, mirrored at `ai4reason/Prover9` on GitHub.)*
