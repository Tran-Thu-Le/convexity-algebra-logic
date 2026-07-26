#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sinh toàn bộ file .in cho Mace4 — kiểm tra tính nhất quán (consistency) và
tính độc lập (independence) của 11 tiên đề Polar Semiring.
Generate all Mace4 .in files testing consistency and independence of the
11 Polar Semiring axioms.

Ký hiệu / Notation (khớp paper-polar-semiring/head-tools.tex Block 7):
    v      join         (nguyên thủy / primitive)
    *      tensor       (nguyên thủy / primitive)
    star() polarity     (nguyên thủy / primitive)
    ev     e_join       (nguyên thủy / primitive)
    eo     e_tensor     (nguyên thủy / primitive)

Sinh ra / produces:
    mace4-inputs/PS_full.in          -- cả 11 tiên đề, tìm model => CONSISTENT
    mace4-inputs/without_<AX>.in     -- 10 tiên đề + phủ định của <AX>
                                        (11 file, mỗi tiên đề một file)
"""

import os

# ---------------------------------------------------------------------------
# 11 tiên đề PS / the 11 PS axioms.
# Mỗi mục: (code, mô tả, dạng khẳng định, dạng PHỦ ĐỊNH dùng làm assumption).
# Each entry: (code, description, positive form, NEGATED form used as
# an assumption in the without_<AX> files).
# ---------------------------------------------------------------------------
AXIOMS = [
    ("J0", "join idempotence",
     "x v x = x.",
     "exists x (x v x != x)."),
    ("J1", "join associativity",
     "(x v y) v z = x v (y v z).",
     "exists x exists y exists z ((x v y) v z != x v (y v z))."),
    ("J2", "join commutativity",
     "x v y = y v x.",
     "exists x exists y (x v y != y v x)."),
    ("J3", "join unit",
     "x v ev = x.",
     "exists x (x v ev != x)."),
    ("T1", "tensor associativity",
     "(x * y) * z = x * (y * z).",
     "exists x exists y exists z ((x * y) * z != x * (y * z))."),
    ("T2", "tensor commutativity",
     "x * y = y * x.",
     "exists x exists y (x * y != y * x)."),
    ("T3", "tensor unit",
     "x * eo = x.",
     "exists x (x * eo != x)."),
    ("TJ1", "tensor distributes over join",
     "x * (y v z) = (x * y) v (x * z).",
     "exists x exists y exists z (x * (y v z) != (x * y) v (x * z))."),
    ("TJ2", "ev absorbing for tensor",
     "x * ev = ev.",
     "exists x (x * ev != ev)."),
    ("P", "involution",
     "star(star(x)) = x.",
     "exists x (star(star(x)) != x)."),
    ("PJ", "polarity / order-compatibility",
     "(x v y = y) <-> (star(y) v star(x) = star(x)).",
     "exists x exists y (-((x v y = y) <-> (star(y) v star(x) = star(x))))."),
]

HEADER = """% ==========================================================
% {title}
% ==========================================================
% Ky hieu / Notation:
%   v      = join   (\\vee),    primitive
%   *      = tensor (\\otimes), primitive
%   star() = polarity (^*),     primitive
%   ev     = e_\\vee,            primitive
%   eo     = e_\\otimes,         primitive
% Dan xuat / derived (khong dung o file nay / unused here):
%   meet(x,y) = star(star(x) v star(y)),  plus(x,y) = star(star(x) * star(y))
% ==========================================================

assign(start_size, {start}).
assign(end_size, {end}).
assign(max_models, 1).

op(400, infix, "v").
op(450, infix, "*").

"""


def render(title, kept, extra_assumptions, start=2, end=10):
    """Dung noi dung mot file .in / build the content of one .in file."""
    out = HEADER.format(title=title, start=start, end=end)
    out += "formulas(assumptions).\n\n"
    for code, desc, pos, _neg in kept:
        out += "  %% %s: %s\n  %s\n\n" % (code, desc, pos)
    for comment, formula in extra_assumptions:
        out += "  %% %s\n  %s\n\n" % (comment, formula)
    out += "end_of_list.\n"
    return out


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    outdir = os.path.join(here, "..", "mace4-inputs")
    outdir = os.path.normpath(outdir)
    os.makedirs(outdir, exist_ok=True)

    # --- 1. PS_full.in : ca 11 tien de, tim model => he tien de NHAT QUAN ---
    full = render(
        "PS_full.in -- all 11 PS axioms; a model proves CONSISTENCY",
        AXIOMS, [])
    with open(os.path.join(outdir, "PS_full.in"), "w") as f:
        f.write(full)

    # --- 2. without_<AX>.in : 10 tien de + PHU DINH cua tien de bi bo ---
    # Mace4 tim model => tien de bi bo KHONG suy ra duoc tu 10 tien de con lai.
    # A model proves the dropped axiom is NOT a consequence of the other ten.
    for code, desc, _pos, neg in AXIOMS:
        kept = [a for a in AXIOMS if a[0] != code]
        title = ("without_%s.in -- the other 10 axioms + negation of %s;\n"
                 "%% a model proves %s is independent of the rest"
                 % (code, code, code))
        content = render(title, kept,
                         [("NEGATION of %s (%s)" % (code, desc), neg)])
        with open(os.path.join(outdir, "without_%s.in" % code), "w") as f:
            f.write(content)

    print("Generated %d files in %s" % (len(AXIOMS) + 1, outdir))


if __name__ == "__main__":
    main()
