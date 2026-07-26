# bga-implies-ps/

Prover9 check of the main theorem of Section 4
(`thm:bga-implies-ps`, `doc4-compare.tex`): every bounded Girard algebra, with
its polarity defined from the residual by `star(x) = res(x, ep)` and the
residual then discarded, satisfies all eleven Polar Semiring axioms.

This is the direction BGA ⇒ PS; the converse (impossibility) is in
[`../ps-not-bga/`](../ps-not-bga/).

## Notation

This is the only folder in which the residual appears. It is written `res(x,y)`
and is a BGA primitive with no counterpart in PS. Everything else uses PS
notation: `v` (join), `mt(x,y)` (meet), `*` (tensor), `eo`/`ep`/`ew`, with
`star(x) = res(x, ep)` and `ev = star(ew)` derived. The five BGA axioms
(`def:bga`) are expanded into 15 formulas.

## Files

- `generator.py` — generates the 19 goal files plus `all-blocks.in`.
- `prover9-inputs/lemA-*.in` — the four residuation lemmas (`lem:res-toolkit`).
- `prover9-inputs/psax-*.in` — the eleven PS axioms as goals.
- `prover9-inputs/extra-*.in` — three additional consequences.
- `prover9-outputs/*.out` — reference Prover9 outputs.

## Running

```sh
python3 generator.py
for f in prover9-inputs/*.in; do prover9 -f "$f"; done
```

## Results

**Residuation lemmas (`lem:res-toolkit`) — 5 / 5 proved**, using only
BGA1–BGA3 plus the definition of `star` (BGA5 unused).

| File | Statement | Result |
|---|---|:---:|
| `lemA-1` | a ≤ b ⇔ e⊗ ≤ res(a,b) | proved |
| `lemA-2` | b ⊗ res(b,c) ≤ c | proved |
| `lemA-3` | a ≤ b ⇒ a ⊗ c ≤ b ⊗ c | proved |
| `lemA-4` | a ≤ b ⇒ res(b,z) ≤ res(a,z) | proved |
| `lemA-5` | z := e⊕: star is antitone | proved |

**The eleven PS axioms — 11 / 11 proved**, including the four the paper marks
"needs proof" (J3, TJ1, TJ2, PJ). This confirms the derivation table
`tab:eleven` in full.

**Additional consequences:**

| File | Statement | Result |
|---|---|:---:|
| `extra-ev-least` | ev is the least element | proved |
| `extra-order` | the two lattice orders agree | proved |
| `extra-meet` | derived meet = lattice meet | **inconclusive** |

`extra-meet` did not finish within its time budget — neither proved nor
refuted. Details and a suggested continuation are in [`../NOTES.md`](../NOTES.md).
