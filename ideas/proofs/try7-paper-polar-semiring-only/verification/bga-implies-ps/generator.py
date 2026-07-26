#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sinh file .in cho Prover9 — chung minh Theorem 4.3 cua bai bao
(`thm:bga-implies-ps`, paper-polar-semiring/doc4-compare.tex):

    Moi Bounded Girard Algebra, sau khi dinh nghia polarity qua residual
        star(x) := res(x, ep)
    va bo han residual khoi signature, deu thoa DU 11 tien de Polar Semiring.

    Every bounded Girard algebra, with polarity defined from the residual,
    satisfies all eleven Polar Semiring axioms.

Sinh ra / produces:
    prover9-inputs/lemA-*.in   -- 4 bo de trung gian (Lemma `lem:res-toolkit`)
    prover9-inputs/psax-*.in   -- 11 tien de PS lam goal
    prover9-inputs/extra-*.in  -- cac he qua phu (meet dan xuat = meet lattice)
    prover9-inputs/all-blocks.in
"""

import os

# ---------------------------------------------------------------------------
# Tien de BGA / the BGA axioms, viet bang ky hieu PS.
# Nguyen thuy / primitives: v (join), mt (meet), * (tensor), res (residual),
#                           eo, ep, ew.
# Dan xuat / derived: star(x) := res(x,ep),  ev := star(ew).
# Thu tu / order: u <= w  :<->  u v w = w.
# ---------------------------------------------------------------------------
BGA1 = [
    ("BGA1a", "join idempotent", "x v x = x."),
    ("BGA1b", "join commutative", "x v y = y v x."),
    ("BGA1c", "join associative", "(x v y) v z = x v (y v z)."),
    ("BGA1d", "meet idempotent", "mt(x,x) = x."),
    ("BGA1e", "meet commutative", "mt(x,y) = mt(y,x)."),
    ("BGA1f", "meet associative", "mt(mt(x,y),z) = mt(x,mt(y,z))."),
    ("BGA1g", "absorption 1", "x v mt(x,y) = x."),
    ("BGA1h", "absorption 2", "mt(x, x v y) = x."),
]
BGA2 = [
    ("BGA2a", "tensor associative", "(x * y) * z = x * (y * z)."),
    ("BGA2b", "tensor commutative", "x * y = y * x."),
    ("BGA2c", "tensor unit eo", "x * eo = x."),
]
BGA3 = [
    ("BGA3", "residuation:  a (x) b <= c  <->  b <= a -> c",
     "((x * y) v z = z) <-> (y v res(x,z) = res(x,z))."),
]
BGA4 = [
    ("BGA4a", "polarity defined from the residual", "star(x) = res(x, ep)."),
    ("BGA4b", "the polarity is involutive", "star(star(x)) = x."),
]
BGA5 = [
    ("BGA5", "ew is the greatest element", "x v ew = ew."),
]
DERIVED = [
    ("D-ev", "least element ev := star(ew)", "ev = star(ew)."),
]

BGA_ALL = BGA1 + BGA2 + BGA3 + BGA4 + BGA5 + DERIVED

# ---------------------------------------------------------------------------
# Cac goal / the goals
# ---------------------------------------------------------------------------

# (a) 4 bo de trung gian cua bai bao / the paper's four residuation lemmas
#     (Lemma `lem:res-toolkit`, doc4-compare.tex).  Chi dung BGA1-BGA3.
LEMMAS = [
    ("lemA-1", "Lemma (1):  a <= b  <->  eo <= res(a,b)",
     "(x v y = y) <-> (eo v res(x,y) = res(x,y))."),
    ("lemA-2", "Lemma (2):  b (x) res(b,c) <= c",
     "(y * res(y,z)) v z = z."),
    ("lemA-3", "Lemma (3):  a <= b  ==>  a (x) c <= b (x) c",
     "(x v y = y) -> ((x * z) v (y * z) = (y * z))."),
    ("lemA-4", "Lemma (4):  a <= b  ==>  res(b,z) <= res(a,z)",
     "(x v y = y) -> (res(y,z) v res(x,z) = res(x,z))."),
    ("lemA-5", "Lemma (4) with z := ep:  star is antitone",
     "(x v y = y) -> (star(y) v star(x) = star(x))."),
]

# (b) 11 tien de PS lam goal / the eleven PS axioms as goals.
#     Cot cuoi: bai bao xep dong nay la "immediate" hay "proof below"
#     (bang tab:eleven trong doc4-compare.tex).
PS_AXIOMS = [
    ("psax-J0", "J0: join idempotence", "x v x = x.", "immediate"),
    ("psax-J1", "J1: join associativity",
     "(x v y) v z = x v (y v z).", "immediate"),
    ("psax-J2", "J2: join commutativity", "x v y = y v x.", "immediate"),
    ("psax-J3", "J3: join unit", "x v ev = x.", "needs proof"),
    ("psax-T1", "T1: tensor associativity",
     "(x * y) * z = x * (y * z).", "immediate"),
    ("psax-T2", "T2: tensor commutativity", "x * y = y * x.", "immediate"),
    ("psax-T3", "T3: tensor unit", "x * eo = x.", "immediate"),
    ("psax-TJ1", "TJ1: tensor distributes over join",
     "x * (y v z) = (x * y) v (x * z).", "needs proof"),
    ("psax-TJ2", "TJ2: ev absorbing for tensor", "x * ev = ev.",
     "needs proof"),
    ("psax-P", "P: involution", "star(star(x)) = x.", "immediate"),
    ("psax-PJ", "PJ: polarity / order-compatibility",
     "(x v y = y) <-> (star(y) v star(x) = star(x)).", "needs proof"),
]

# (c) He qua phu / additional consequences claimed in the same theorem.
EXTRAS = [
    ("extra-meet", "the derived meet coincides with the lattice meet: "
     "star(star(x) v star(y)) = mt(x,y)",
     "star(star(x) v star(y)) = mt(x,y)."),
    ("extra-ev-least", "ev is the least element:  ev <= x",
     "ev v x = x."),
    ("extra-order", "the two lattice orders agree:  x v y = y  <->  mt(x,y) = x",
     "(x v y = y) <-> (mt(x,y) = x)."),
]

HEADER = """%% ==== Block {tag}: {desc} ====
%% Bai bao / paper: thm:bga-implies-ps (doc4-compare.tex){status}
%% Gia thiet / hypotheses: {hypnote}
%%
%% Ky hieu / notation (tat ca viet bang ky hieu PS, tru residual):
%%   v        = join   (\\vee)          nguyen thuy cua BGA / BGA primitive
%%   mt(x,y)  = meet   (\\wedge)        nguyen thuy cua BGA / BGA primitive
%%   *        = tensor (\\otimes)       nguyen thuy cua BGA / BGA primitive
%%   res(x,y) = residual (\\to)         nguyen thuy cua BGA -- KHONG co trong PS
%%   eo, ep, ew                        nguyen thuy cua BGA / BGA primitives
%%   star(x)  = res(x,ep)              DAN XUAT / derived
%%   ev       = star(ew)               DAN XUAT / derived
%%   Thu tu / order:  u <= w  :<->  u v w = w.

assign(max_seconds, 300).

op(400, infix, "v").
op(450, infix, "*").

formulas(assumptions).

"""


def render(tag, desc, goal, hyps, hypnote, status=""):
    out = HEADER.format(tag=tag, desc=desc, status=status, hypnote=hypnote)
    for c, d, f in hyps:
        out += "  %% %s: %s\n  %s\n\n" % (c, d, f)
    out += "end_of_list.\n\nformulas(goals).\n\n"
    out += "  %% %s\n  %s\n\n" % (desc, goal)
    out += "end_of_list.\n"
    return out


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    outdir = os.path.join(here, "prover9-inputs")
    os.makedirs(outdir, exist_ok=True)
    allblocks = []

    # --- (a) bo de trung gian: chi dung BGA1-BGA3 (chua can P/BGA5) ---
    lemma_hyps = BGA1 + BGA2 + BGA3 + BGA4  # BGA4a needed to unfold star
    for tag, desc, goal in LEMMAS:
        note = ("BGA1-BGA3 (+ dinh nghia star); KHONG dung BGA5. "
                "BGA1-BGA3 plus the definition of star; BGA5 unused.")
        c = render(tag, desc, goal, lemma_hyps, note)
        open(os.path.join(outdir, tag + ".in"), "w").write(c)
        allblocks.append(c)

    # --- (b) 11 tien de PS: dung day du tien de BGA ---
    for tag, desc, goal, status in PS_AXIOMS:
        note = "day du tien de BGA (BGA1-BGA5). all BGA axioms."
        st = "\n%%%% Bang tab:eleven xep dong nay la: %s" % status
        c = render(tag, desc, goal, BGA_ALL, note, st)
        open(os.path.join(outdir, tag + ".in"), "w").write(c)
        allblocks.append(c)

    # --- (c) he qua phu ---
    for tag, desc, goal in EXTRAS:
        note = "day du tien de BGA (BGA1-BGA5). all BGA axioms."
        c = render(tag, desc, goal, BGA_ALL, note)
        open(os.path.join(outdir, tag + ".in"), "w").write(c)
        allblocks.append(c)

    open(os.path.join(outdir, "all-blocks.in"), "w").write(
        "\n\n".join(allblocks))
    print("Generated %d goal files + all-blocks.in in %s"
          % (len(allblocks), outdir))


if __name__ == "__main__":
    main()
