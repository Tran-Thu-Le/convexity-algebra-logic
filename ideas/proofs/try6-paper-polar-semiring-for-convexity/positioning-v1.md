# Introduction (Motivation)

Convex analysis is built around a remarkably stable class of objects: proper closed convex functions. Within this class, many of the fundamental constructions—Fenchel conjugation, epigraphs, duality, and infimal convolution—interact through elegant geometric and analytic principles.

However, a striking phenomenon appears throughout the theory. Many natural operations fail to preserve this class. Pointwise maxima generally lose convexity, infimal convolutions may fail to be lower semicontinuous, and pointwise minima almost never remain convex. As a consequence, convex analysis repeatedly invokes regularization procedures:

* convexification,
* lower-semicontinuous closure,
* bipolarization,
* biconjugation.

Expressions such as
[
\operatorname{conv}(\max(f,g))
\quad\text{and}\quad
\operatorname{cl}(f\square g)
]
are ubiquitous in the literature. These regularizations are usually regarded as technical devices that repair operations so that their outputs remain inside the category of closed convex functions.

This paper proposes a different viewpoint.

Our central observation is that the ubiquity of regularization is unlikely to be accidental. Rather than indicating deficiencies of individual operators, it suggests that convex analysis is being expressed at a representation level where the natural algebraic operations are no longer primitive.

We argue that the regularized operators themselves are the genuine primitives. More precisely, operations such as
[
\operatorname{conv}(\max(\cdot,\cdot))
\quad\text{and}\quad
\operatorname{cl}(\square)
]
should not be viewed as compositions of elementary operators followed by repair. Instead, they arise as representations, at the function level, of primitive algebraic operations defined in a higher abstraction layer.

To make this viewpoint precise, we introduce an abstract algebraic structure called a **Polar Idempotent Commutative Semiring (PICS)**. Within this structure, the regularization procedures disappear from the primitive language. The induced operations are intrinsically closed, satisfy natural duality relations through Fenchel conjugation, and recover the classical regularized constructions only after interpretation back to convex functions.

Consequently, regularization is reinterpreted not as an additional mathematical operation, but as a representation artifact. What appears at the function level as convexification or lower-semicontinuous closure is simply the shadow of a primitive operation living in a higher algebraic layer.

This perspective suggests a modular organization of convex analysis. Convex functions constitute only one representation layer. Above them lies an algebraic layer where the essential identities become transparent, and many classical regularization procedures are absorbed into the primitive operations themselves. This paper develops that algebraic layer and establishes it as a bridge between convex analysis and the multiplicative-additive fragment of linear logic.
