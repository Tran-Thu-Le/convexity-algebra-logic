# Positioning of Section 3 (Architecture)

Section 3 studies the eleven axioms not as a flat list but as a cumulative
sequence, adding the two polarity axioms one at a time on top of the eight
semiring axioms. Each part isolates exactly what the newly added axiom
generates.

## Part 1 — The semiring base (8 axioms)

The eight axioms make the structure an idempotent commutative semiring: an
idempotent commutative monoid under the join, a commutative monoid under the
tensor, with the tensor distributing over the join. The idempotent commutative
monoid under the join induces a partial order in the standard way
(a <= b iff a v b = b), with the join as least upper bound. No negation is
present yet; this is the polarity-free algebraic layer.

## Part 2 — Adding the involution P (8 + P)

Adding the involution axiom alone equips the structure with a primitive
negation satisfying P. From the involution the dual operations are defined by
conjugation, and this generates a second idempotent commutative semiring — the
dual — together with the De Morgan laws, at no further axiomatic cost. The
negation is at this stage a form of antitone map between the structure and its
dual, but the involution by itself does not yet tie the negation to the order
of Part 1: on 8 + P the negation need not be antitone with respect to the
induced order (for instance the identity remains admissible).

## Part 3 — Adding the polarity–join axiom PJ (8 + P + PJ)

Adding PJ makes the negation order-compatible: it forces the reflected order
carried by the dual to coincide with the induced order of Part 1. This
unification of the two orders is what upgrades the structure to a lattice,
supplying the meet as the conjugate of the join and making the negation
genuinely antitone with respect to a single, well-defined order.

## Fundamental Structure Theorem

Putting the three parts together: every Polar Semiring canonically induces a
dual Polar Semiring, the polarity is an isomorphism onto this dual, and the
order induced by the join coincides with the order reflected through the
polarity. The passage from 8 + P to 8 + P + PJ is thus the passage from a
merely involutive structure to an order-compatible, self-dual one, and it costs
exactly one axiom.
