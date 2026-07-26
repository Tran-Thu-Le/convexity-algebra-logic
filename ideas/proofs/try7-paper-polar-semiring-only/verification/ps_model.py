#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ps_model.py -- doc file output cua Mace4, dung lai mo hinh, va kiem tra
brute-force 11 tien de Polar Semiring MOT CACH DOC LAP voi solver.

Parse a Mace4 output file, rebuild the finite model, and brute-force check
the 11 Polar Semiring axioms independently of the solver.

Dung chung boi ca 3 folder Mace4 / shared by all three Mace4 folders.
"""

import re
import sys
from itertools import product


# ---------------------------------------------------------------------------
# 1. Doc model tu output Mace4 / parse a Mace4 interpretation block
# ---------------------------------------------------------------------------
class Model(object):
    """Mot mo hinh huu han / one finite model on domain {0,...,n-1}."""

    def __init__(self, n, consts, unary, binary):
        self.n = n
        self.consts = consts      # {'ev': 1, 'eo': 0, ...}
        self.unary = unary        # {'star': [..n values..]}
        self.binary = binary      # {'v': [[..]], '*': [[..]]}

    # --- toan tu nguyen thuy / primitive operations ---
    def join(self, a, b):
        return self.binary["v"][a][b]

    def tensor(self, a, b):
        return self.binary["*"][a][b]

    def star(self, a):
        return self.unary["star"][a]

    @property
    def ev(self):
        return self.consts["ev"]

    @property
    def eo(self):
        return self.consts["eo"]

    # --- toan tu dan xuat / derived operations ---
    def meet(self, a, b):
        return self.star(self.join(self.star(a), self.star(b)))

    def plus(self, a, b):
        return self.star(self.tensor(self.star(a), self.star(b)))

    @property
    def ew(self):
        return self.star(self.ev)

    @property
    def ep(self):
        return self.star(self.eo)

    def leq(self, a, b):
        """Thu tu join / join order: a <= b iff a v b = b."""
        return self.join(a, b) == b

    # --- in bang toan tu / print operation tables ---
    def tables(self):
        n, out = self.n, []
        hdr = "    | " + " ".join("%2d" % j for j in range(n))
        sep = "----+" + "-" * (3 * n)
        for name, fn in (("v (join)", self.join), ("* (tensor)", self.tensor),
                         ("meet", self.meet), ("plus", self.plus)):
            out.append("%s:" % name)
            out.append(hdr)
            out.append(sep)
            for i in range(n):
                out.append(" %2d | " % i
                           + " ".join("%2d" % fn(i, j) for j in range(n)))
            out.append("")
        out.append("star: " + " ".join("%d->%d" % (i, self.star(i))
                                       for i in range(n)))
        out.append("ev = %d,  eo = %d,  ew = star(ev) = %d,  ep = star(eo) = %d"
                   % (self.ev, self.eo, self.ew, self.ep))
        return "\n".join(out)


def parse_mace4(path):
    """Tra ve model DAU TIEN trong file / return the first model in the file."""
    text = open(path).read()
    m = re.search(r"interpretation\(\s*(\d+).*?\n\]\)\.", text, re.S)
    if not m:
        return None
    n = int(m.group(1))
    body = m.group(0)

    consts, unary, binary = {}, {}, {}
    for fm in re.finditer(r"function\(\s*([^,(]+?)\s*(\(_[,_]*\))?\s*,\s*\[(.*?)\]\s*\)",
                          body, re.S):
        name = fm.group(1).strip()
        arity_mark = fm.group(2)
        vals = [int(v) for v in re.findall(r"-?\d+", fm.group(3))]
        if arity_mark is None:                       # hang so / constant
            consts[name] = vals[0]
        elif arity_mark.count("_") == 1:             # 1 ngoi / unary
            unary[name] = vals
        else:                                        # 2 ngoi / binary
            binary[name] = [vals[i * n:(i + 1) * n] for i in range(n)]
    return Model(n, consts, unary, binary)


# ---------------------------------------------------------------------------
# 2. Kiem tra 11 tien de / brute-force check of the 11 axioms
# ---------------------------------------------------------------------------
def check_axioms(M):
    """Tra ve dict {ma tien de: True/False} / returns {axiom code: bool}."""
    D = range(M.n)
    r = {}
    r["J0"] = all(M.join(x, x) == x for x in D)
    r["J1"] = all(M.join(M.join(x, y), z) == M.join(x, M.join(y, z))
                  for x, y, z in product(D, D, D))
    r["J2"] = all(M.join(x, y) == M.join(y, x) for x, y in product(D, D))
    r["J3"] = all(M.join(x, M.ev) == x for x in D)
    r["T1"] = all(M.tensor(M.tensor(x, y), z) == M.tensor(x, M.tensor(y, z))
                  for x, y, z in product(D, D, D))
    r["T2"] = all(M.tensor(x, y) == M.tensor(y, x) for x, y in product(D, D))
    r["T3"] = all(M.tensor(x, M.eo) == x for x in D)
    r["TJ1"] = all(M.tensor(x, M.join(y, z))
                   == M.join(M.tensor(x, y), M.tensor(x, z))
                   for x, y, z in product(D, D, D))
    r["TJ2"] = all(M.tensor(x, M.ev) == M.ev for x in D)
    r["P"] = all(M.star(M.star(x)) == x for x in D)
    r["PJ"] = all(M.leq(x, y) == M.leq(M.star(y), M.star(x))
                  for x, y in product(D, D))
    return r


AXIOM_ORDER = ["J0", "J1", "J2", "J3", "T1", "T2", "T3",
               "TJ1", "TJ2", "P", "PJ"]


def main(argv):
    if len(argv) < 2:
        print("usage: ps_model.py <mace4-output.txt> [...]")
        return 1
    for path in argv[1:]:
        M = parse_mace4(path)
        print("=" * 66)
        print(path)
        if M is None:
            print("  KHONG co model / no model found")
            continue
        print("  domain size = %d" % M.n)
        res = check_axioms(M)
        holds = [a for a in AXIOM_ORDER if res[a]]
        fails = [a for a in AXIOM_ORDER if not res[a]]
        print("  thoa / holds : " + (", ".join(holds) or "-"))
        print("  sai  / fails : " + (", ".join(fails) or "-"))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
