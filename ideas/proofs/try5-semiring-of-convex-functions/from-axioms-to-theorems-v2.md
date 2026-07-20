# Polar Idempotent Commutative Semiring (PICS)

## 1. Primitive Operations

A **Polar Idempotent Commutative Semiring (PICS)** is a structure

$$
(X,\wedge,+,*,e_\wedge,e_+)
$$

consisting of

- a binary operation $\wedge$ (meet),
- a binary operation $+$ (sum),
- a unary operation $*$ (polar),
- constants $e_\wedge$ and $e_+$,

satisfying the following axioms.

### Meet

**(M0)**

$$
a\wedge a=a.
$$

**(M1)**

$$
(a\wedge b)\wedge c=a\wedge(b\wedge c).
$$

**(M2)**

$$
a\wedge b=b\wedge a.
$$

**(M3)**

$$
a\wedge e_\wedge=a.
$$

---

### Sum

**(S1)**

$$
(a+b)+c=a+(b+c).
$$

**(S2)**

$$
a+b=b+a.
$$

**(S3)**

$$
a+e_+=a.
$$

---

### Semiring

**(SM1)**

$$
a+(b\wedge c)
=
(a+b)\wedge(a+c).
$$

**(SM2)**

$$
a+e_\wedge=e_\wedge.
$$

---

### Polar

**(P)**

$$
a^{**}=a.
$$

**(PM)**

$$
a\wedge b=a
\iff
b^*\wedge a^*=b^*.
$$

---

# 2. Derived Operations

The following operations are derived from the primitive ones.

### Order

$$
a\le b
\iff
a\wedge b=a.
$$

### Join

$$
a\vee b
=
(a^*\wedge b^*)^*.
$$

### Multiplication

$$
a\times b
=
(a^*+b^*)^*.
$$

### Derived identities

$$
e_\vee=e_\wedge^*,
$$

$$
e_\times=e_+^*.
$$

---

# 3. Derived Theory

## 3.1. De Morgan Identities

### Theorem 1

$$
(a\vee b)^*
=
a^*\wedge b^*.
$$

### Theorem 2

$$
(a\times b)^*
=
a^*+b^*.
$$

### Theorem 3

$$
(a\wedge b)^*
=
a^*\vee b^*.
$$

### Theorem 4

$$
(a+b)^*
=
a^*\times b^*.
$$

### Theorem 5

$$
e_\vee^*=e_\wedge,
\qquad
e_\times^*=e_+.
$$

---

## 3.2. The Dual Semiring

### Theorem 6 (Join)

The algebra

$$
(X,\vee,e_\vee)
$$

is an idempotent commutative monoid:

$$
a\vee a=a,
$$

$$
(a\vee b)\vee c
=
a\vee(b\vee c),
$$

$$
a\vee b
=
b\vee a,
$$

$$
a\vee e_\vee=a.
$$

---

### Theorem 7 (Multiplication)

The algebra

$$
(X,\times,e_\times)
$$

is a commutative monoid:

$$
(a\times b)\times c
=
a\times(b\times c),
$$

$$
a\times b
=
b\times a,
$$

$$
a\times e_\times=a.
$$

---

### Theorem 8 (Distributivity)

$$
a\times(b\vee c)
=
(a\times b)\vee(a\times c),
$$

$$
(a\vee b)\times c
=
(a\times c)\vee(b\times c).
$$

---

### Theorem 9 (Absorbing element)

$$
a\times e_\vee
=
e_\vee.
$$

---

### Theorem 10 (Polar compatibility)

$$
(a\vee b)^*
=
a^*\wedge b^*,
$$

$$
(a\times b)^*
=
a^*+b^*.
$$

---

## 3.3. Order Induced by Meet

### Theorem 11

The relation

$$
\le
$$

is a partial order.

---

### Theorem 12

The element

$$
e_\wedge
$$

is the greatest element:

$$
a\le e_\wedge.
$$

---

### Theorem 13

The element

$$
e_\vee
$$

is the least element:

$$
e_\vee\le a.
$$

---

### Theorem 14 (Monotonicity of Meet)

If

$$
a\le b,
$$

then

$$
a\wedge c
\le
b\wedge c.
$$

---

### Theorem 15 (Monotonicity of Sum)

If

$$
a\le b,
$$

then

$$
a+c
\le
b+c.
$$

---

### Theorem 16 (Order Reversal)

$$
a\le b
\iff
b^*\le a^*.
$$

---

## 3.4. Order Induced by Join

Define

$$
a\le_\vee b
\iff
a\vee b=b.
$$

### Theorem 17

The relation

$$
\le_\vee
$$

is a partial order.

---

### Theorem 18

The element

$$
a\vee b
$$

is the least upper bound (supremum) of
$a$ and $b$ with respect to $\le$.

---

### Theorem 19

The two induced orders coincide:

$$
\le
=
\le_\vee.
$$

---

### Theorem 20 (Absorption Laws)

$$
a\wedge(a\vee b)=a,
$$

$$
a\vee(a\wedge b)=a.
$$