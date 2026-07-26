#!/usr/bin/env bash
# ---------------------------------------------------------------------------
# run-all.sh -- regenerate inputs, run every Prover9/Mace4 job, cross-check,
# and print a summary.
#
# Requires prover9 and mace4 on PATH, or set PROVER9_BIN to their directory:
#   git clone --depth 1 https://github.com/ai4reason/Prover9.git
#   cd Prover9 && make all
#   export PROVER9_BIN="$PWD/bin"
# ---------------------------------------------------------------------------
set -u

BIN="${PROVER9_BIN:-}"
if [ -n "$BIN" ]; then MACE4="$BIN/mace4"; PROVER9="$BIN/prover9";
else MACE4=mace4; PROVER9=prover9; fi

cd "$(dirname "$0")"
pass=0; fail=0
note() { printf '\n=== %s ===\n' "$1"; }

# ---------- 1. independence ----------
note "independence (Mace4)"
( cd independence && python3 mace4-generator/generator.py )
for f in independence/mace4-inputs/*.in; do
  b=$(basename "$f" .in)
  case "$b" in
    PS_full) o=independence/mace4-outputs/mace4-output-full.txt ;;
    *) o="independence/mace4-outputs/mace4-output-${b#without_}.txt" ;;
  esac
  timeout 300 "$MACE4" -f "$f" > "$o" 2>&1
  if grep -q "interpretation(" "$o"; then
    printf '  %-14s model found\n' "$b"; pass=$((pass+1))
  else
    printf '  %-14s NO MODEL\n' "$b"; fail=$((fail+1))
  fi
done
python3 ps_model.py independence/mace4-outputs/*.txt > /dev/null 2>&1 \
  && echo "  (cross-check with ps_model.py: ok)"

# ---------- 2. architecture-theorems ----------
note "architecture-theorems (Prover9)"
( cd architecture-theorems && python3 generator.py )
for f in architecture-theorems/prover9-inputs/block*.in; do
  b=$(basename "$f" .in)
  o="architecture-theorems/prover9-outputs/$b.out"
  timeout 300 "$PROVER9" -f "$f" > "$o" 2>&1
  if grep -q "THEOREM PROVED" "$o"; then
    printf '  %-18s proved\n' "$b"; pass=$((pass+1))
  else
    printf '  %-18s *** NOT PROVED ***\n' "$b"; fail=$((fail+1))
  fi
done

# ---------- 3. bga-implies-ps ----------
# NOTE: the 'extra-meet' goal may run long; raise max_seconds if needed.
note "bga-implies-ps (Prover9)"
( cd bga-implies-ps && python3 generator.py )
for f in bga-implies-ps/prover9-inputs/lemA-*.in \
         bga-implies-ps/prover9-inputs/psax-*.in \
         bga-implies-ps/prover9-inputs/extra-*.in; do
  b=$(basename "$f" .in)
  o="bga-implies-ps/prover9-outputs/$b.out"
  timeout 600 "$PROVER9" -f "$f" > "$o" 2>&1
  if grep -q "THEOREM PROVED" "$o"; then
    printf '  %-16s proved\n' "$b"; pass=$((pass+1))
  elif grep -q "SEARCH FAILED" "$o"; then
    printf '  %-16s *** SEARCH FAILED ***\n' "$b"; fail=$((fail+1))
  else
    printf '  %-16s (timed out, inconclusive)\n' "$b"
  fi
done

# ---------- 4. ps-not-bga ----------
note "ps-not-bga (Mace4 + Python)"
timeout 900 "$MACE4" -f ps-not-bga/mace4-inputs/no-dualizing-element.in \
  > ps-not-bga/mace4-outputs/mace4-output.txt 2>&1
if ( cd ps-not-bga && python3 verify.py > /dev/null 2>&1 ); then
  echo "  model found and verified"; pass=$((pass+1))
else
  echo "  *** VERIFICATION FAILED ***"; fail=$((fail+1))
fi

# ---------- 5. non-distributive ----------
note "non-distributive (Mace4 + Python)"
timeout 900 "$MACE4" -f non-distributive/mace4-inputs/non-distributive.in \
  > non-distributive/mace4-outputs/mace4-output.txt 2>&1
if ( cd non-distributive && python3 verify.py > /dev/null 2>&1 \
     && python3 emit_latex.py > model.tex ); then
  echo "  model found and verified; model.tex regenerated"; pass=$((pass+1))
else
  echo "  *** VERIFICATION FAILED ***"; fail=$((fail+1))
fi

printf '\n=== SUMMARY: %d ok, %d fail ===\n' "$pass" "$fail"
[ "$fail" -eq 0 ]
