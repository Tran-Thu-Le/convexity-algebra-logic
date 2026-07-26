# Distribution Profile of Polar Semirings

## Motivation

A polarized semiring is equipped with four binary operations

$$
(\otimes,\ \oplus,\ \mathbin{\&},\ \parr)
$$

together with an involutive polarity satisfying the eleven axioms introduced previously.

The polarity identifies two dual pairs of operations,

$$
\otimes^{*}=\parr,
\qquad
\oplus^{*}=\mathbin{\&}.
$$

Consequently, every algebraic identity automatically produces a dual identity by applying the polarity.

This observation greatly reduces the number of independent distributive laws that need to be verified.

---

## Independent distributive laws

Among the four operations, only

$$
\otimes
\quad\text{and}\quad
\oplus
$$

need to be considered as source operations.

Indeed, every distributive law whose source is either

$$
\parr
\quad\text{or}\quad
\mathbin{\&}
$$

is simply the polarity dual of one of the laws below.

Therefore, there are exactly six independent distributive laws:

$$
\begin{aligned}
&\otimes\rightarrow\oplus, &&
\otimes\rightarrow\mathbin{\&}, &&
\otimes\rightarrow\parr,\\
&\oplus\rightarrow\otimes, &&
\oplus\rightarrow\mathbin{\&}, &&
\oplus\rightarrow\parr.
\end{aligned}
$$

The remaining six distributive laws are obtained automatically by polarity and therefore contain no additional independent information.

---

## Definition

**Definition (Distribution Profile).**

Let $S$ be a polarized semiring.

The **distribution profile** of $S$ is the binary vector

$$
\operatorname{DP}(S)
=
(d_1,d_2,d_3,d_4,d_5,d_6)
\in
\{0,1\}^6,
$$

where

$$
\begin{aligned}
d_1&=[\otimes\rightarrow\oplus],\\
d_2&=[\otimes\rightarrow\mathbin{\&}],\\
d_3&=[\otimes\rightarrow\parr],\\
d_4&=[\oplus\rightarrow\otimes],\\
d_5&=[\oplus\rightarrow\mathbin{\&}],\\
d_6&=[\oplus\rightarrow\parr].
\end{aligned}
$$

Each coordinate equals

- $1$ if the corresponding distributive law holds;
- $0$ otherwise.

---

## Interpretation

The distribution profile is a canonical six-bit invariant of a polarized semiring.

It records all independent distributivity phenomena because every other distributive law follows from these six by polarity.

Therefore, two polarized semirings satisfying the same eleven axioms may nevertheless have different distribution profiles.

The distribution profile thus serves as an **algebraic fingerprint**, allowing different models of polarized semirings to be classified and compared according to their distributive behavior.

---

## Example

For the polarized semiring of closed convex functions,

$$
(\Gamma_0,\otimes,\oplus,\mathbin{\&},\parr),
$$

the distribution profile is computed by checking only the above six laws.

The remaining six distributive laws are then obtained automatically by applying Fenchel polarity.
