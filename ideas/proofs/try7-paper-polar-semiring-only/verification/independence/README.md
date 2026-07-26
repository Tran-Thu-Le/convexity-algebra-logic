# independence/

Mace4 check that the 11 Polar Semiring axioms are **consistent** and
**mutually independent** (no axiom follows from the other ten).

## Files

- `mace4-generator/generator.py` — generates the 12 input files below.
- `mace4-inputs/PS_full.in` — all 11 axioms; a model proves consistency.
- `mace4-inputs/without_<AX>.in` — the other 10 axioms plus the negation of
  `<AX>`; a model proves `<AX>` is independent.
- `mace4-outputs/mace4-output-*.txt` — reference Mace4 outputs.

## Running

```sh
python3 mace4-generator/generator.py
for f in mace4-inputs/*.in; do mace4 -f "$f"; done
python3 ../ps_model.py mace4-outputs/*.txt   # solver-independent cross-check
```

## Results

`PS_full.in` has a model at domain size 2, so the axioms are **consistent**.
Each `without_<AX>.in` has a model, so every axiom is **independent**:

| Axiom | Countermodel found | Smallest size |
|---|:---:|:---:|
| J0 join idempotence | yes | 3 |
| J1 join associativity | yes | 4 |
| J2 join commutativity | yes | 2 |
| J3 join unit | yes | 2 |
| T1 tensor associativity | yes | 4 |
| T2 tensor commutativity | yes | 3 |
| T3 tensor unit | yes | 2 |
| TJ1 distributivity | yes | 3 |
| TJ2 absorbing element | yes | 2 |
| P involution | yes | **5** |
| PJ polarity | yes | 2 |

The largest countermodel has **5** elements. Mace4 searches from
`start_size = 2` upward, so each size is the true minimum.

`../ps_model.py` re-reads each output, rebuilds the model, and brute-force
checks all 11 axioms: every countermodel satisfies exactly ten axioms and
violates its one target axiom.

See [`../NOTES.md`](../NOTES.md) for how these numbers map to the paper.
