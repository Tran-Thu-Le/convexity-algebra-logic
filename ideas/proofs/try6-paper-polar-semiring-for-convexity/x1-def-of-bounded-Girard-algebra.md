# bounded-girard-algebra.md

# Bounded Girard Algebra

## Reference

The definitions below follow the standard presentation in:

> **Paolo Aglianò**, *An Algebraic Investigation of Linear Logic*, Archive for Mathematical Logic, 2025.

This paper proves that **bounded Girard algebras** are the equivalent algebraic semantics of MALL.

---

# 1. Commutative residuated lattice

A structure

$$
(A,\vee,\wedge,\cdot,\rightarrow,1)
$$

is a **commutative residuated lattice** if

1. $(A,\vee,\wedge)$ is a lattice;

2. $(A,\cdot,1)$ is a commutative monoid;

3. the residuation law holds:

$$
a\cdot b\le c
\iff
a\le b\rightarrow c.
$$

---

# 2. Girard algebra

A structure

$$
(A,\vee,\wedge,\cdot,\rightarrow,0,1)
$$

is called a **Girard algebra** if

1. $(A,\vee,\wedge,\cdot,\rightarrow,1)$ is a commutative residuated lattice;

2. $0$ is an involutive element:

$$
(x\rightarrow0)\rightarrow0=x,
\qquad
\forall x\in A.
$$

---

## Negation

Negation is **defined**, not primitive:

$$
\neg x:=x\rightarrow0.
$$

From the axioms one derives

- involution

$$
\neg\neg x=x;
$$

- antitonicity

$$
x\le y
\Longrightarrow
\neg y\le\neg x;
$$

- De Morgan laws

$$
\neg(x\vee y)=\neg x\wedge\neg y,
$$

$$
\neg(x\wedge y)=\neg x\vee\neg y;
$$

- contraposition

$$
\neg(a\cdot\neg b)=a\rightarrow b.
$$

Hence

$$
\rightarrow
\quad\Longrightarrow\quad
\neg.
$$

---

## Derived par operation

The multiplicative disjunction is defined by

$$
a\parr b
=
\neg(\neg a\cdot\neg b).
$$

Thus

$$
\cdot,\neg
\quad\Longrightarrow\quad
\parr.
$$

---

# 3. Bounded Girard algebra

A **bounded Girard algebra** is a Girard algebra together with a constant

$$
\top
$$

satisfying

$$
x\rightarrow\top=1,
\qquad
\forall x\in A.
$$

The bottom element is then defined by

$$
\bot:=\neg\top.
$$

---

# Primitive signature

The primitive operations are

$$
(\vee,\wedge,\cdot,\rightarrow),
$$

together with constants

$$
0,\;1,\;\top.
$$

Negation and par are **derived**, not primitive.

---

# Logical interpretation

After introducing

$$
\neg x=x\rightarrow0,
$$

and

$$
a\parr b
=
\neg(\neg a\cdot\neg b),
$$

the algebra contains all four connectives of MALL:

| MALL connective | Algebraic operation |
|-----------------|--------------------|
| $\otimes$ | $\cdot$ |
| $\parr$ | $\neg(\neg a\cdot\neg b)$ |
| $\&$ | $\wedge$ |
| $\oplus$ | $\vee$ |

---

# Important structural properties

Every bounded Girard algebra satisfies:

- distributive lattice;
- tensor preserves joins:

$$
a\cdot(b\vee c)
=
(a\cdot b)\vee(a\cdot c);
$$

- similarly on the left;

- tensor is monotone;

- tensor generally **does not** distribute over meet.

---

# Comparison with Polar Semiring

Bounded Girard algebra is organized as

$$
\text{Residual}
\Longrightarrow
\text{Negation}
\Longrightarrow
\text{Par}.
$$

By contrast, Polar Semiring is intended to start from

$$
\text{Polarity}
\Longrightarrow
\text{Join}
\Longrightarrow
\text{Tensor, Par},
$$

without assuming the existence of any residual.