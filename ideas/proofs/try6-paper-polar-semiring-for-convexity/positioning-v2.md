# 1. Observation: Regularization is Everywhere

One of the most striking features of convex analysis is the ubiquity of regularization. Fundamental operations such as pointwise maxima, pointwise minima, and infimal convolution do not generally preserve the class of closed convex functions. Consequently, the theory repeatedly introduces additional operators such as convexification, lower-semicontinuous closure, and biconjugation:
[
\operatorname{conv}(\max(f,g)),\qquad
\operatorname{cl}(f\square g),\qquad
f^{**}.
]
These constructions appear throughout convex analysis and are usually regarded as technical devices for restoring regularity.

# 2. A Different Viewpoint

This paper proposes a different interpretation. Rather than viewing regularization as a repair mechanism, we regard it as evidence that convex analysis is being expressed at an inappropriate level of abstraction. The repeated need for regularization suggests the existence of a missing algebraic layer in which the natural operations are already closed and no additional correction is required.

# 3. The Missing Algebraic Layer

We introduce an abstract algebraic structure, the **Polar Idempotent Commutative Semiring (PICS)**, whose primitive operations are intrinsically closed. Classical operations such as
[
\operatorname{conv}(\max(f,g))
\quad\text{and}\quad
\operatorname{cl}(f\square g)
]
are no longer primitive constructions but become representations of single algebraic operations (join and parr) in this higher layer.

# 4. Regularization as a Representation Phenomenon

The key insight is that regularization does not belong to the primitive algebra itself. Instead, it appears only after interpreting the abstract algebra inside the category of convex functions.

In particular, every derived operation in PICS is constructed from the involution
[
(\cdot)^*.
]
When interpreted as the Fenchel conjugate, this involution automatically maps arbitrary functions to closed convex functions. Consequently, the regularity of all derived operations is inherited from the representation of the duality operator itself, rather than from the operations individually.

# 5. Regularization is not Primitive

Under this viewpoint, convexification and lower-semicontinuous closure are no longer regarded as independent mathematical operations. They are representation artifacts: they arise only because primitive algebraic operations are expressed through convex functions. In the abstract algebraic layer, these regularization procedures disappear from the primitive language altogether.

# 6. A Modular View of Convex Analysis

This leads to a modular organization of convex analysis:
[
\text{Convex Functions}
\longrightarrow
\text{Regepis}
\longrightarrow
\text{Polar Semiring}
\longrightarrow
\text{Linear Logic}.
]

Each layer isolates a different level of structure.

* The function layer studies analytic representations.
* The geometric layer studies epigraph-like objects.
* The algebraic layer captures the intrinsic operations responsible for duality.
* The logical layer interprets these algebraic structures within multiplicative-additive linear logic.

This decomposition provides a conceptual explanation for why regularization repeatedly appears in convex analysis: it is not a fundamental operation, but the shadow of primitive operations living in a higher algebraic layer.
