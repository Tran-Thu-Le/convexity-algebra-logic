#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verify.py -- doc lai model Mace4 vua tim duoc, in bang toan tu, va kiem tra
BRUTE-FORCE, doc lap voi solver:
  (1) ca 11 tien de Polar Semiring deu thoa;
  (2) voi MOI q trong domain, ton tai (a,b) pha vo tuong duong
      a (x) b <= q  <->  b <= a^*   (tuc (dagger), eq:dagger, doc4-compare.tex).

Re-read the model Mace4 found, print the operation tables, and brute-force
check -- independently of the solver -- that all 11 PS axioms hold and that
no element of the domain is a dualizing element.

Cach dung / usage:
    python3 verify.py [mace4-outputs/mace4-output.txt]
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                ".."))
from ps_model import parse_mace4, check_axioms, AXIOM_ORDER   # noqa: E402


def sweep_dualizing(M):
    """Voi moi q, tim phan vi du (a,b) / for each q, find a counterexample."""
    D = range(M.n)
    report = []
    for q in D:
        witness = None
        for a in D:
            for b in D:
                lhs = M.leq(M.tensor(a, b), q)     # a (x) b <= q
                rhs = M.leq(b, M.star(a))          # b <= a^*
                if lhs != rhs:
                    witness = (a, b, lhs, rhs)
                    break
            if witness:
                break
        report.append((q, witness))
    return report


def main(argv):
    here = os.path.dirname(os.path.abspath(__file__))
    path = argv[1] if len(argv) > 1 else os.path.join(
        here, "mace4-outputs", "mace4-output.txt")

    M = parse_mace4(path)
    if M is None:
        print("KHONG doc duoc model / no model found in %s" % path)
        return 1

    print("=" * 68)
    print("MODEL do Mace4 tim duoc / model found by Mace4: |X| = %d" % M.n)
    print("=" * 68)
    print(M.tables())

    print()
    print("-" * 68)
    print("(1) Kiem tra 11 tien de PS / brute-force check of the 11 axioms")
    print("-" * 68)
    res = check_axioms(M)
    for a in AXIOM_ORDER:
        print("    %-4s : %s" % (a, "OK" if res[a] else "*** FAIL ***"))
    all_ok = all(res.values())
    print("    => %s" % ("day la mot Polar Semiring / this IS a Polar Semiring"
                         if all_ok else "*** KHONG phai PS / NOT a PS ***"))

    print()
    print("-" * 68)
    print("(2) Quet moi q: co phan tu nao la dualizing element khong?")
    print("    Sweep over q: is any element a dualizing element?")
    print("    Dieu kien can / required:  a (x) b <= q  <->  b <= a^*")
    print("-" * 68)
    report = sweep_dualizing(M)
    for q, w in report:
        if w is None:
            print("    q = %d : *** LA dualizing element / IS one ***" % q)
        else:
            a, b, lhs, rhs = w
            print("    q = %d : hong tai (a,b) = (%d,%d)  "
                  "[a(x)b <= q] = %-5s  [b <= a^*] = %-5s"
                  % (q, a, b, str(lhs), str(rhs)))
    none_works = all(w is not None for _, w in report)

    print()
    print("=" * 68)
    if all_ok and none_works:
        print("KET LUAN / CONCLUSION:")
        print("  Mo hinh %d phan tu nay la mot Polar Semiring KHONG co "
              "dualizing element." % M.n)
        print("  This %d-element structure is a Polar Semiring with NO "
              "dualizing element," % M.n)
        print("  hence PS =/=> BGA.  Xac nhan doc lap cho Theorem 4.2 "
              "(thm:impossibility).")
        rc = 0
    else:
        print("*** KIEM TRA THAT BAI / VERIFICATION FAILED ***")
        rc = 1
    print("=" * 68)
    return rc


if __name__ == "__main__":
    sys.exit(main(sys.argv))
