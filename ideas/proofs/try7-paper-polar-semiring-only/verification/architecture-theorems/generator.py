#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sinh file .in cho Prover9 — chung minh cac Proposition/Theorem trong
paper-polar-semiring/doc3-structures.tex, voi DUNG gia thiet toi thieu ma
bai bao dung cho tung khoi (KHONG dung ca 11 tien de cho moi goal).

Generate Prover9 .in files proving the propositions of doc3-structures.tex,
each with exactly the minimal hypotheses the paper uses for that block.

Sinh ra / produces:
    prover9-inputs/blockN-<slug>.in   -- mot file cho moi goal / one per goal
    prover9-inputs/all-blocks.in      -- ban gop nhieu-khoi de doc / reading copy
"""

import os

# ---------------------------------------------------------------------------
# Cac nhom gia thiet / hypothesis groups
# ---------------------------------------------------------------------------
J0 = [("J0", "join idempotence", "x v x = x.")]
JOIN_MONOID = [
    ("J1", "join associativity", "(x v y) v z = x v (y v z)."),
    ("J2", "join commutativity", "x v y = y v x."),
    ("J3", "join unit", "x v ev = x."),
]
TENSOR_MONOID = [
    ("T1", "tensor associativity", "(x * y) * z = x * (y * z)."),
    ("T2", "tensor commutativity", "x * y = y * x."),
    ("T3", "tensor unit", "x * eo = x."),
]
TJ = [
    ("TJ1", "tensor distributes over join",
     "x * (y v z) = (x * y) v (x * z)."),
    ("TJ2", "ev absorbing for tensor", "x * ev = ev."),
]
INVOL = [("P", "involution", "star(star(x)) = x.")]
POLAR = [("PJ", "polarity / order-compatibility",
          "(x v y = y) <-> (star(y) v star(x) = star(x)).")]

# Dinh nghia toan tu dan xuat / definitions of the derived operations
# (doc2-polar-semiring.tex, Definition 2.2, eq:derived-ops)
DEFS = [
    ("D-meet", "a /\\ b := (a^* v b^*)^*",
     "meet(x,y) = star(star(x) v star(y))."),
    ("D-plus", "a (+) b := (a^* * b^*)^*",
     "plus(x,y) = star(star(x) * star(y))."),
    ("D-ew", "e_/\\ := (e_v)^*", "ew = star(ev)."),
    ("D-ep", "e_(+) := (e_*)^*", "ep = star(eo)."),
]

ALL11 = J0 + JOIN_MONOID + TENSOR_MONOID + TJ + INVOL + POLAR

# ---------------------------------------------------------------------------
# 5 khoi / the five blocks.  (label LaTeX, ten, gia thiet, danh sach goal)
# ---------------------------------------------------------------------------
BLOCKS = [
    dict(
        num=1,
        name="Duality laws",
        label="prop:duality (doc3-structures.tex)",
        hyps=JOIN_MONOID + TENSOR_MONOID + INVOL + DEFS,
        note="Chi (P) + hai monoid — KHONG co J0/TJ1/TJ2/PJ. "
             "Only (P) plus the two monoids; no J0/TJ1/TJ2/PJ.",
        goals=[
            ("RD1", "De Morgan for meet",
             "star(meet(x,y)) = star(x) v star(y)."),
            ("RD2", "De Morgan for plus",
             "star(plus(x,y)) = star(x) * star(y)."),
            ("RD3", "De Morgan for join",
             "star(x v y) = meet(star(x),star(y))."),
            ("RD4", "De Morgan for tensor",
             "star(x * y) = plus(star(x),star(y))."),
            ("RD5a", "duality of units: star(ev) = ew", "star(ev) = ew."),
            ("RD5b", "duality of units: star(ew) = ev", "star(ew) = ev."),
            ("RD5c", "duality of units: star(eo) = ep", "star(eo) = ep."),
            ("RD5d", "duality of units: star(ep) = eo", "star(ep) = eo."),
        ]),
    dict(
        num=2,
        name="Reflected modules",
        label="prop:reflected-modules (doc3-structures.tex)",
        hyps=J0 + JOIN_MONOID + TENSOR_MONOID + INVOL + DEFS,
        note="Nhu Block 1, cong them J0 (chi can cho muc idempotence). "
             "As Block 1 plus J0 (needed only for the idempotence goal).",
        goals=[
            ("RS1a", "meet associative",
             "meet(meet(x,y),z) = meet(x,meet(y,z))."),
            ("RS1b", "meet commutative", "meet(x,y) = meet(y,x)."),
            ("RS1c", "ew is a unit for meet", "meet(x,ew) = x."),
            ("RS1d", "meet idempotent (needs J0)", "meet(x,x) = x."),
            ("RS2a", "plus associative",
             "plus(plus(x,y),z) = plus(x,plus(y,z))."),
            ("RS2b", "plus commutative", "plus(x,y) = plus(y,x)."),
            ("RS2c", "ep is a unit for plus", "plus(x,ep) = x."),
        ]),
    dict(
        num=3,
        name="Order compatibility",
        label="prop:order-compat (doc3-structures.tex)",
        hyps=ALL11 + DEFS,
        note="Du 11 tien de (bai bao: 'in the presence of the other ten "
             "axioms'). All 11 axioms.",
        goals=[
            ("OC1", "join/meet compatibility",
             "(x v y = y) <-> (meet(y,x) = x)."),
            ("OC2", "order reversal  a <= b  <->  b^* <=^* a^*",
             "(x v y = y) <-> (meet(star(y),star(x)) = star(y))."),
            ("OC3a", "absorption 1", "meet(x, x v y) = x."),
            ("OC3b", "absorption 2", "x v meet(x,y) = x."),
        ]),
    dict(
        num=4,
        name="Order structure",
        label="prop:order-structure (doc3-structures.tex)",
        hyps=ALL11 + DEFS,
        note="Du 11 tien de. All 11 axioms.",
        goals=[
            ("OS1", "antisymmetry of <=",
             "((x v y = y) & (y v x = x)) -> x = y."),
            ("OS2", "transitivity of <=",
             "((x v y = y) & (y v z = z)) -> (x v z = z)."),
            ("OS3", "the two orders coincide:  <=  =  <=^*",
             "(x v y = y) <-> (meet(x,y) = x)."),
            ("OS4", "ev is least:  ev <= x", "ev v x = x."),
            # LUU Y: dang dung la  x v ew = ew  (tuc x <= ew), KHONG phai
            # 'x v ew = x' -- xem readme.md muc 'sua loi so voi prompt'.
            # NOTE: the correct form is x v ew = ew (i.e. x <= ew).
            ("OS5", "ew is greatest:  x <= ew", "x v ew = ew."),
            ("OS6", "monotonicity of meet",
             "(x v y = y) -> (meet(x,z) v meet(y,z) = meet(y,z))."),
            ("OS7", "monotonicity of plus",
             "(x v y = y) -> (plus(x,z) v plus(y,z) = plus(y,z))."),
            ("OS8", "join is the least upper bound",
             "((x v z = z) & (y v z = z)) -> ((x v y) v z = z)."),
            ("OS9", "meet is the greatest lower bound",
             "((z v x = x) & (z v y = y)) -> (z v meet(x,y) = meet(x,y))."),
        ]),
    dict(
        num=5,
        name="Fundamental Structure Theorem (dual structure)",
        label="thm:fundamental (doc3-structures.tex)",
        hyps=ALL11 + DEFS,
        note="Du 11 tien de tren cau truc goc; moi goal la ban dich cua mot "
             "tien de sang cau truc doi ngau (v:=meet, *:=plus, ev:=ew, "
             "eo:=ep). All 11 axioms on the original structure; each goal is "
             "one axiom translated to the dual structure.",
        goals=[
            ("DJ0", "dual of J0", "meet(x,x) = x."),
            ("DJ1", "dual of J1",
             "meet(meet(x,y),z) = meet(x,meet(y,z))."),
            ("DJ2", "dual of J2", "meet(x,y) = meet(y,x)."),
            ("DJ3", "dual of J3 (unit ew)", "meet(x,ew) = x."),
            ("DT1", "dual of T1",
             "plus(plus(x,y),z) = plus(x,plus(y,z))."),
            ("DT2", "dual of T2", "plus(x,y) = plus(y,x)."),
            ("DT3", "dual of T3 (unit ep)", "plus(x,ep) = x."),
            ("DTJ1", "dual of TJ1",
             "plus(x, meet(y,z)) = meet(plus(x,y), plus(x,z))."),
            ("DTJ2", "dual of TJ2 (ew absorbing for plus)",
             "plus(x, ew) = ew."),
            ("DP", "dual of P (unchanged)", "star(star(x)) = x."),
            ("DPJ", "dual of PJ",
             "(meet(x,y) = y) <-> (meet(star(y),star(x)) = star(x))."),
        ]),
]

# --- Khoi tuy chon: chieu nguoc cua Prop order-compat ----------------------
# Bo PJ khoi gia thiet, thay bang 2 luat hap thu, roi lay PJ lam goal.
# Optional: drop PJ, assume the two absorption laws instead, prove PJ.
CONVERSE = dict(
    num=6,
    name="OPTIONAL: converse direction (absorption ==> PJ)",
    label="prop:order-compat, converse (4)==>(1)",
    hyps=(J0 + JOIN_MONOID + TENSOR_MONOID + TJ + INVOL + DEFS
          + [("OC3a", "absorption 1 (assumed instead of PJ)",
              "meet(x, x v y) = x."),
             ("OC3b", "absorption 2 (assumed instead of PJ)",
              "x v meet(x,y) = x.")]),
    note="PJ da bi BO khoi gia thiet. PJ has been REMOVED from the "
         "hypotheses; the absorption laws replace it.",
    goals=[("PJ-conv", "recover PJ from absorption",
            "(x v y = y) <-> (star(y) v star(x) = star(x)).")],
)

HEADER = """%% ==== Block {num}.{sub}: {name} -- goal {code} ====
%% Bai bao / paper: {label}
%% Goal: {desc}
%% Gia thiet / hypotheses: {note}
%% Ky hieu / notation: v = join, * = tensor, star() = polarity,
%%   ev = e_join, eo = e_tensor; meet/plus/ew/ep are DEFINED below.

assign(max_seconds, 60).

op(400, infix, "v").
op(450, infix, "*").

formulas(assumptions).

"""


def render(block, sub, code, desc, goal):
    out = HEADER.format(num=block["num"], sub=sub, name=block["name"],
                        label=block["label"], code=code, desc=desc,
                        note=block["note"])
    for c, d, f in block["hyps"]:
        out += "  %% %s: %s\n  %s\n\n" % (c, d, f)
    out += "end_of_list.\n\nformulas(goals).\n\n"
    out += "  %% %s: %s\n  %s\n\n" % (code, desc, goal)
    out += "end_of_list.\n"
    return out


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    outdir = os.path.join(here, "prover9-inputs")
    os.makedirs(outdir, exist_ok=True)

    allblocks, n = [], 0
    for block in BLOCKS + [CONVERSE]:
        for sub, (code, desc, goal) in enumerate(block["goals"], start=1):
            content = render(block, sub, code, desc, goal)
            fname = "block%d-%s.in" % (block["num"], code)
            with open(os.path.join(outdir, fname), "w") as f:
                f.write(content)
            allblocks.append(content)
            n += 1

    # Ban gop de doc / concatenated reading copy (tach lai bang csplit:
    #   csplit -z -f block_ -b '%02d.in' all-blocks.in '/^% ==== Block/' '{*}')
    with open(os.path.join(outdir, "all-blocks.in"), "w") as f:
        f.write("\n\n".join(allblocks))

    print("Generated %d goal files + all-blocks.in in %s" % (n, outdir))


if __name__ == "__main__":
    main()
