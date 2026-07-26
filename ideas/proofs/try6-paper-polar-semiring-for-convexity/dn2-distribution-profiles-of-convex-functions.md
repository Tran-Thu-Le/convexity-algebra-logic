# Distribution Counterexamples for Convex Functions

## 1. Four operations on closed convex functions

Let $\Gamma_0(\mathbb{R}^n)$ denote the class of proper, lower semicontinuous, convex functions
$f:\mathbb{R}^n\to(-\infty,+\infty]$.

We use the following four operations.

| Name | Symbol | Definition |
|---|---|---|
| tensor | $f\otimes g$ | $(f\otimes g)(x):=f(x)+g(x)$ |
| plus | $f\oplus g$ | $(f\oplus g)(x):=\max\{f(x),g(x)\}$ |
| with | $f\mathbin{\&}g$ | $f\mathbin{\&}g:=\operatorname{cl\,conv}\bigl(\min\{f,g\}\bigr)$ |
| parr | $f\parr g$ | $f\parr g:=\operatorname{cl}(f\square g)$ |

Here the infimal convolution is

$$
(f\square g)(x)
:=
\inf_{\substack{y,z\in\mathbb{R}^n\\y+z=x}}
\bigl(f(y)+g(z)\bigr)
=
\inf_{y\in\mathbb{R}^n}
\bigl(f(y)+g(x-y)\bigr).
$$

The operation $\operatorname{cl\,conv}$ denotes the lower-semicontinuous convex envelope.

The pointwise identity

$$
f+\max\{g,h\}
=
\max\{f+g,f+h\}
$$

shows that tensor distributes over plus:

$$
f\otimes(g\oplus h)
=
(f\otimes g)\oplus(f\otimes h).
$$

The remaining five possible distributive laws considered below are false.

---

## 2. Indicator functions

For a nonempty closed convex set $A\subseteq\mathbb{R}^n$, define its indicator function by

$$
\delta_A(x)
:=
\begin{cases}
0, & x\in A,\\
+\infty, & x\notin A.
\end{cases}
$$

Then $\delta_A\in\Gamma_0(\mathbb{R}^n)$.

For nonempty closed convex sets $A,B\subseteq\mathbb{R}^n$, the four operations reduce to the following set operations whenever the resulting Minkowski sum is closed:

$$
\delta_A\otimes\delta_B
=
\delta_A+\delta_B
=
\delta_{A\cap B},
$$

$$
\delta_A\oplus\delta_B
=
\max\{\delta_A,\delta_B\}
=
\delta_{A\cap B},
$$

$$
\delta_A\mathbin{\&}\delta_B
=
\delta_{\operatorname{cl\,conv}(A\cup B)},
$$

and

$$
\delta_A\parr\delta_B
=
\delta_{A+B},
$$

where

$$
A+B:=\{a+b:a\in A,\ b\in B\}.
$$

Thus, on pure indicator functions, both tensor and plus reduce to set intersection. This is why the failure of plus distributing over tensor requires vertically shifted indicator functions.

---

## 3. Tensor does not distribute over with

Consider the distributive law

$$
f\otimes(g\mathbin{\&}h)
\stackrel{?}{=}
(f\otimes g)\mathbin{\&}(f\otimes h).
$$

For indicator functions, this would imply

$$
A\cap\operatorname{conv}(B\cup C)
=
\operatorname{conv}\bigl((A\cap B)\cup(A\cap C)\bigr).
$$

Work in $\mathbb{R}^2$ and choose

$$
A:=\{(x,y)\in\mathbb{R}^2:x^2+y^2\le 1\},
$$

$$
B:=\{(-1,t):-1\le t\le 1\},
\qquad
C:=\{(1,t):-1\le t\le 1\}.
$$

Since

$$
\operatorname{conv}(B\cup C)=[-1,1]^2,
$$

we have

$$
A\cap\operatorname{conv}(B\cup C)=A.
$$

On the other hand,

$$
A\cap B=\{(-1,0)\},
\qquad
A\cap C=\{(1,0)\},
$$

and therefore

$$
\operatorname{conv}\bigl((A\cap B)\cup(A\cap C)\bigr)
=
[-1,1]\times\{0\}.
$$

Hence

$$
A\cap\operatorname{conv}(B\cup C)
\neq
\operatorname{conv}\bigl((A\cap B)\cup(A\cap C)\bigr).
$$

Taking $f=\delta_A$, $g=\delta_B$, and $h=\delta_C$, we obtain

$$
\boxed{
f\otimes(g\mathbin{\&}h)
\neq
(f\otimes g)\mathbin{\&}(f\otimes h).
}
$$

Thus tensor does not distribute over with.

---

## 4. Tensor does not distribute over parr

Consider

$$
f\otimes(g\parr h)
\stackrel{?}{=}
(f\otimes g)\parr(f\otimes h).
$$

For indicator functions, this would imply

$$
A\cap(B+C)
=
(A\cap B)+(A\cap C).
$$

Work in $\mathbb{R}$ and choose

$$
A=[0,1],
\qquad
B=[-1,0],
\qquad
C=[1,2].
$$

Then

$$
B+C=[0,2],
$$

so

$$
A\cap(B+C)=[0,1].
$$

However,

$$
A\cap B=\{0\},
\qquad
A\cap C=\{1\},
$$

and hence

$$
(A\cap B)+(A\cap C)
=
\{0\}+\{1\}
=
\{1\}.
$$

Therefore

$$
A\cap(B+C)
\neq
(A\cap B)+(A\cap C).
$$

Taking $f=\delta_A$, $g=\delta_B$, and $h=\delta_C$, we get

$$
\boxed{
f\otimes(g\parr h)
\neq
(f\otimes g)\parr(f\otimes h).
}
$$

Thus tensor does not distribute over parr.

---

## 5. Plus does not distribute over tensor

Consider

$$
f\oplus(g\otimes h)
\stackrel{?}{=}
(f\oplus g)\otimes(f\oplus h).
$$

Pure indicator functions cannot distinguish these two sides because both tensor and plus reduce to set intersection. We therefore use a vertical translation of an indicator function.

Let

$$
K:=\{0\}\subseteq\mathbb{R},
$$

and define

$$
f:=1+\delta_K,
\qquad
g:=\delta_K,
\qquad
h:=\delta_K.
$$

Since

$$
g\otimes h
=
\delta_K+\delta_K
=
\delta_K,
$$

the left-hand side is

$$
f\oplus(g\otimes h)
=
\max\{1+\delta_K,\delta_K\}
=
1+\delta_K.
$$

Moreover,

$$
f\oplus g=1+\delta_K,
\qquad
f\oplus h=1+\delta_K.
$$

Thus the right-hand side is

$$
(f\oplus g)\otimes(f\oplus h)
=
(1+\delta_K)+(1+\delta_K)
=
2+\delta_K.
$$

Since

$$
1+\delta_K\neq 2+\delta_K,
$$

we conclude that

$$
\boxed{
f\oplus(g\otimes h)
\neq
(f\oplus g)\otimes(f\oplus h).
}
$$

Thus plus does not distribute over tensor.

---

## 6. Plus does not distribute over with

Consider

$$
f\oplus(g\mathbin{\&}h)
\stackrel{?}{=}
(f\oplus g)\mathbin{\&}(f\oplus h).
$$

For indicator functions, this would again imply

$$
A\cap\operatorname{conv}(B\cup C)
=
\operatorname{conv}\bigl((A\cap B)\cup(A\cap C)\bigr).
$$

Work in $\mathbb{R}^2$ and choose

$$
A:=\{(x,y)\in\mathbb{R}^2:|x|+|y|\le 1\},
$$

$$
B:=\{(-1,t):-1\le t\le 1\},
\qquad
C:=\{(1,t):-1\le t\le 1\}.
$$

Since

$$
\operatorname{conv}(B\cup C)=[-1,1]^2,
$$

we obtain

$$
A\cap\operatorname{conv}(B\cup C)=A.
$$

But

$$
A\cap B=\{(-1,0)\},
\qquad
A\cap C=\{(1,0)\},
$$

and hence

$$
\operatorname{conv}\bigl((A\cap B)\cup(A\cap C)\bigr)
=
[-1,1]\times\{0\}.
$$

Therefore

$$
A\cap\operatorname{conv}(B\cup C)
\neq
\operatorname{conv}\bigl((A\cap B)\cup(A\cap C)\bigr).
$$

Taking $f=\delta_A$, $g=\delta_B$, and $h=\delta_C$, we obtain

$$
\boxed{
f\oplus(g\mathbin{\&}h)
\neq
(f\oplus g)\mathbin{\&}(f\oplus h).
}
$$

Thus plus does not distribute over with.

---

## 7. Plus does not distribute over parr

Consider

$$
f\oplus(g\parr h)
\stackrel{?}{=}
(f\oplus g)\parr(f\oplus h).
$$

For indicator functions, this would imply

$$
A\cap(B+C)
=
(A\cap B)+(A\cap C).
$$

Work in $\mathbb{R}$ and choose

$$
A=[-1,1],
\qquad
B=[-2,-1],
\qquad
C=[1,2].
$$

Then

$$
B+C=[-1,1],
$$

so

$$
A\cap(B+C)=[-1,1].
$$

On the other hand,

$$
A\cap B=\{-1\},
\qquad
A\cap C=\{1\},
$$

and therefore

$$
(A\cap B)+(A\cap C)
=
\{-1\}+\{1\}
=
\{0\}.
$$

Hence

$$
A\cap(B+C)
\neq
(A\cap B)+(A\cap C).
$$

Taking $f=\delta_A$, $g=\delta_B$, and $h=\delta_C$, we get

$$
\boxed{
f\oplus(g\parr h)
\neq
(f\oplus g)\parr(f\oplus h).
}
$$

Thus plus does not distribute over parr.

---

## 8. Distribution profile

Order the six distributive laws as

$$
\bigl(
\otimes\to\oplus,\;
\otimes\to\mathbin{\&},\;
\otimes\to\parr
\ ;\
\oplus\to\otimes,\;
\oplus\to\mathbin{\&},\;
\oplus\to\parr
\bigr).
$$

Tensor distributes over plus, while the five remaining laws fail. Therefore the distribution profile of $\Gamma_0(\mathbb{R}^n)$ is

$$
\boxed{
\operatorname{DP}(\Gamma_0)
=
(1,0,0\ ;\ 0,0,0).
}
$$
