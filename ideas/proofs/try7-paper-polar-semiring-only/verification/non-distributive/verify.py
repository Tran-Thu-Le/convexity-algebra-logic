#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verify.py -- doc lai model Mace4, kiem tra brute-force 11 tien de, liet ke
MOI bo (x,y,z) pha vo tinh phan phoi, va in lai bang toan tu o dang doc duoc
(nhan chu: bottom/top/middle) de dan thang vao bai bao.

Re-read the Mace4 model, brute-force check the 11 axioms, list every triple
witnessing failure of distributivity, and print the operation tables with
readable element names for direct use in the paper.

Cach dung / usage:
    python3 verify.py [mace4-outputs/mace4-output.txt]
"""

import os
import sys
from itertools import product

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                ".."))
from ps_model import parse_mace4, check_axioms, AXIOM_ORDER   # noqa: E402


def order_pairs(M):
    """Tra ve quan he <= / return the order relation as a set of pairs."""
    return {(a, b) for a in range(M.n) for b in range(M.n) if M.leq(a, b)}


def nice_names(M):
    """Dat ten cho phan tu theo vi tri trong thu tu / name elements by rank."""
    D = list(range(M.n))
    bottom = [a for a in D if all(M.leq(a, b) for b in D)]
    top = [a for a in D if all(M.leq(b, a) for b in D)]
    names = {}
    for a in D:
        if a in bottom:
            names[a] = "bot"
        elif a in top:
            names[a] = "top"
    mids = [a for a in D if a not in names]
    for i, a in enumerate(mids):
        names[a] = chr(ord("a") + i)
    return names


def main(argv):
    here = os.path.dirname(os.path.abspath(__file__))
    path = argv[1] if len(argv) > 1 else os.path.join(
        here, "mace4-outputs", "mace4-output.txt")

    M = parse_mace4(path)
    if M is None:
        print("KHONG doc duoc model / no model found in %s" % path)
        return 1

    names = nice_names(M)
    D = range(M.n)

    print("=" * 70)
    print("MODEL do Mace4 tim duoc / model found by Mace4: |X| = %d" % M.n)
    print("=" * 70)
    print(M.tables())
    print()
    print("Ten phan tu / element names: "
          + ", ".join("%d = %s" % (a, names[a]) for a in D))
    print("ev = %s, eo = %s, ew = %s, ep = %s"
          % (names[M.ev], names[M.eo], names[M.ew], names[M.ep]))

    print()
    print("Quan he thu tu <= (cac cap that su, bo phan xa) /")
    print("strict order pairs a < b:")
    for a, b in sorted(order_pairs(M)):
        if a != b:
            print("    %s < %s" % (names[a], names[b]))

    print()
    print("-" * 70)
    print("(1) Kiem tra 11 tien de PS / brute-force check of the 11 axioms")
    print("-" * 70)
    res = check_axioms(M)
    for a in AXIOM_ORDER:
        print("    %-4s : %s" % (a, "OK" if res[a] else "*** FAIL ***"))
    all_ok = all(res.values())

    print()
    print("-" * 70)
    print("(2) Cac bo (x,y,z) pha vo phan phoi cua \\/ tren /\\ /")
    print("    triples witnessing failure of  x v (y ^ z) = (x v y) ^ (x v z)")
    print("-" * 70)
    fails = []
    for x, y, z in product(D, D, D):
        lhs = M.join(x, M.meet(y, z))
        rhs = M.meet(M.join(x, y), M.join(x, z))
        if lhs != rhs:
            fails.append((x, y, z, lhs, rhs))
    for x, y, z, lhs, rhs in fails[:12]:
        print("    x=%-3s y=%-3s z=%-3s : LHS=%-3s  RHS=%-3s"
              % (names[x], names[y], names[z], names[lhs], names[rhs]))
    if len(fails) > 12:
        print("    ... va %d bo khac / and %d more" % (len(fails) - 12,
                                                       len(fails) - 12))
    print("    Tong so bo pha vo / total witnesses: %d" % len(fails))

    # Kiem tra them: chieu con lai cua phan phoi (de bao cao day du)
    # Extra: the other distributive law, for completeness.
    dual_fails = sum(
        1 for x, y, z in product(D, D, D)
        if M.meet(x, M.join(y, z)) != M.join(M.meet(x, y), M.meet(x, z)))
    print("    (chieu doi ngau /\\ tren \\/ cung hong o %d bo / the dual law "
          "also fails at %d triples)" % (dual_fails, dual_fails))

    print()
    print("=" * 70)
    if all_ok and fails:
        print("KET LUAN / CONCLUSION:")
        print("  Ton tai Polar Semiring %d phan tu co lattice KHONG phan phoi."
              % M.n)
        print("  There is a %d-element Polar Semiring whose lattice is NOT "
              "distributive," % M.n)
        print("  xac nhan cau 'possibly non-distributive' trong "
              "prop:order-structure.")
        rc = 0
    else:
        print("*** KIEM TRA THAT BAI / VERIFICATION FAILED ***")
        rc = 1
    print("=" * 70)
    return rc


if __name__ == "__main__":
    sys.exit(main(sys.argv))
