# Two Kinds of "Closed" for Convex Functions: Where Geometric Intuition Lies to You

There's a quiet belief that most people who learn convex analysis carry around, even after they've gotten comfortable with Fenchel conjugates, subgradients, and Lagrangian duality: that "closed convex function" is a single notion, and that its three usual descriptions — geometric (the epigraph has no gaps), topological (lower semicontinuity), and algebraic (invariance under taking the dual twice) — are just three ways of saying the same thing.

This post shows that belief is wrong, and wrong in a fairly interesting way: one of these three descriptions is strictly stronger than the other two, and the gap between them isn't a minor technicality. It's the reason convex analysis textbooks quietly attach the word "proper" to almost every important theorem.

## 1. Four properties, two ways to bundle them

Let $f:\mathbb R^n\to\overline{\mathbb R}=[-\infty,+\infty]$ be an arbitrary function, with epigraph $\operatorname{epi}(f):=\{(x,r): r\ge f(x)\}$. Consider four properties:

- U — upward closed in each fiber. If $r\in\operatorname{epi}(f)$ at $x$ and $r'\ge r$, then $(x,r')$ is in the epigraph too.
- C — convex. $\operatorname{epi}(f)$ is a convex set in $\mathbb R^n\times\mathbb R$.
- T — topologically closed. $\operatorname{epi}(f)$ is closed, equivalently $f$ is lower semicontinuous.
- B — bipolar closed. $f=f^{**}$, where $f$ equals its own double Fenchel conjugate:
$$f^*(y):=\sup_{x}\big(\langle x,y\rangle-f(x)\big),\qquad f^{**}(x):=\sup_y\big(\langle x,y\rangle-f^*(y)\big).$$

Note that U holds automatically for every function — it's just the definition of an epigraph, not a real constraint. So the two natural definitions of "closed" one could write down are:

$$\text{UCT-closed} :\iff U\wedge C\wedge T\qquad\text{versus}\qquad\text{bipolar-closed} :\iff B.$$

UCT-closed is the geometric/topological definition: convex, with no holes in the epigraph. Bipolar-closed is the algebraic definition: a fixed point of double conjugation.

Are these two the same?

## 2. One direction holds for free

Theorem. If $f=f^{**}$, then $f$ automatically satisfies U, C, and T.

The proof requires almost nothing. U holds automatically as noted. And $f^{**}(x)=\sup_y(\langle x,y\rangle-f^*(y))$ is a supremum of a family of functions that are affine in $x$ — for each fixed $y$, $x\mapsto\langle x,y\rangle-f^*(y)$ is affine (the coefficient $-f^*(y)$ may be $\pm\infty$, which just gives a degenerate affine function, still convex and lsc). A supremum of a family of convex, lsc functions is always convex and lsc, since the epigraph of a supremum is the intersection of the individual epigraphs — each of which is a half-space here — and an intersection of closed convex sets is closed and convex. Since $f=f^{**}$, $f$ inherits both C and T.

In other words, any function that arises as a bipolar always has the shape "intersection of the half-spaces supporting it," and that shape is automatically convex and closed. This direction is free, using no additional assumptions.

## 3. The other direction — and a somewhat surprising counterexample

The real question is whether UCT-closed implies bipolar-closed. Intuition says yes — "convex and not gappy" sounds like it should already guarantee that a function "matches" its double dual perfectly. Consider, with $n=1$:

$$f(x):=\begin{cases}-\infty & \text{if } x\in[0,1]\\ +\infty & \text{if } x\notin[0,1]\end{cases}$$

Check the three properties. U holds automatically. C holds: $\operatorname{epi}(f)=[0,1]\times\mathbb R$, a product of two convex sets, hence convex. T holds: $[0,1]\times\mathbb R$ is a product of two closed sets, hence closed in $\mathbb R\times\mathbb R$.

So $f$ is perfectly valid as a UCT-closed function: convex, with a closed epigraph, nothing suspicious geometrically or topologically.

Now compute the conjugate. For any $y$, pick $x_0\in[0,1]$; then $f^*(y)\ge\langle x_0,y\rangle-f(x_0)=\langle x_0,y\rangle-(-\infty)=+\infty$. So $f^*\equiv+\infty$ for every $y$. From there, $f^{**}(x)=\sup_y(\langle x,y\rangle-\infty)=-\infty$ for every $x$, not just $x\in[0,1]$.

So $f^{**}\equiv-\infty$, while $f$ equals $+\infty$ everywhere outside $[0,1]$. Clearly $f^{**}\ne f$. B fails, despite U, C, and T all holding without exception.

Why intuition misfires here: looking at the epigraph of $f$ — a vertical strip $[0,1]\times\mathbb R$ — it looks like an entirely ordinary closed convex set. But double conjugation only sees a function through its affine minorants (supporting half-spaces from below). A vertical strip that's unbounded in the $r$ direction has no genuine affine minorant other than the constant function $-\infty$: any affine minorant with finite slope drifts to $-\infty$ as $x$ moves along the strip, yet it also needs to stay $\le f(x)=+\infty$ the moment $x$ leaves $[0,1]$ — which no non-degenerate affine function can do. Since the bipolar closure can only see $-\infty$ in the interior and no minorant distinguishes inside from outside $[0,1]$, it flattens everything to the constant $-\infty$, losing all information about $f$ being $+\infty$ outside the strip.

## 4. Conclusion of part one: strict inclusion, not equivalence

$$\{\text{bipolar-closed}\}\ \subsetneq\ \{\text{UCT-closed}\}.$$

The inclusion is strict — the example above is the witness. Bipolar-closed is genuinely stronger, not just an alternative phrasing of the same idea.

## 5. How Rockafellar sidesteps the gap

If bipolar-closed is strictly stronger than UCT-closed, then the familiar statement "$f$ convex, $f$ closed $\Rightarrow f^{**}=f$" — usually filed under the name Fenchel–Moreau — must be hiding some unstated condition. It is.

First, a simpler theorem that explains exactly why the example in section 3 fails at B:

Theorem (global collapse). If $f=f^{**}$ and there is a point $x_0$ with $f(x_0)=-\infty$, then $f\equiv-\infty$ on all of $\mathbb R^n$.

Proof. $f(x_0)=-\infty$ gives, for every $y$: $f^*(y)\ge\langle x_0,y\rangle-(-\infty)=+\infty$, so $f^*\equiv+\infty$. Then $f^{**}(x)=\sup_y(\langle x,y\rangle-\infty)=-\infty$ for every $x$, not just $x_0$. Since $f=f^{**}$, $f\equiv-\infty$ everywhere. $\blacksquare$

Nothing here uses convexity, topology, or separation theorems — it's pure algebra of the sup operation. The statement says: if a function is bipolar-closed and has even one point equal to $-\infty$, it's forced to be the constant $-\infty$ everywhere — there's no way to be $-\infty$ in one place and $+\infty$ elsewhere, as in the example above. Conversely, since that example violates this conclusion (it has a $-\infty$ point without being globally constant), it was doomed from the start to fail B — now for a structural reason rather than just a direct computation.

### "Proper" as a fence, not a consequence

Here Rockafellar makes a deft move. He defines:

$$f \text{ proper} :\iff f(x)>-\infty\ \text{ for all } x\ \wedge\ f\not\equiv+\infty.$$

And when he states what "closed convex function" means, he doesn't say "convex, with closed epigraph" outright. He defines it as: proper and lsc, or the constant $\equiv+\infty$, or the constant $\equiv-\infty$ — exactly three cases, nothing more. The function from section 3 — which has a $-\infty$ point but isn't globally constant, and isn't proper either — falls into none of the three cases. It's excluded from the scope of the theory by definition, before the question "does it satisfy $f^{**}=f$" ever gets asked.

It's worth being precise about what kind of move this is. It is not a theorem saying every UCT-closed convex function automatically falls into one of the three cases — that statement is false, and section 3 is the counterexample. It's a definitional choice: Rockafellar restricts attention to exactly the region where B and UCT coincide, and calls that region "closed." The price, rarely spelled out explicitly in textbooks, is that there exist convex functions with a perfectly closed epigraph that get excluded from the theory purely because they're locally $-\infty$ without being globally constant.

## 6. The main theorem, stated with its actual scope

Putting this together gives the precise version of what people usually call Fenchel–Moreau:

Theorem. For proper $f$: $f$ is convex and lower semicontinuous if and only if $f=f^{**}$.

The two directions carry very different weight.

The direction from bipolar-closed to convex-and-lsc is free — it was proved in full in section 2, without needing proper or anything else. Proper here just narrows the scope; it contributes nothing to the proof.

The direction from convex-and-lsc to bipolar-closed is the real substance of Fenchel–Moreau. It needs a separation theorem for convex sets — a finite-dimensional Hahn–Banach: if $f^{**}(x_0)<f(x_0)$ at some point, separate the point $(x_0,\beta)$ (for $\beta$ strictly between the two values) from the closed convex epigraph of $f$ by a hyperplane; that hyperplane produces exactly an affine minorant exceeding the assumed value of $f^{**}(x_0)$ — a contradiction.

This is exactly where proper is genuinely needed, not just convenient. If $f$ isn't proper — if it has a $-\infty$ point without being a global constant — the separation argument breaks down from the first step, because there's no guarantee of a clean separating hyperplane once the epigraph mixes a $-\infty$ point with a $+\infty$ region the way section 3's example does. That same example, a counterexample to the direction without properness, shows proper isn't a tidy add-on — it's a condition the separation argument actually depends on.

## 7. Takeaways

Three things worth remembering.

"Closed" in convex analysis isn't one notion — it's two: a geometric/topological one (UCT) and an algebraic one (bipolar), with the algebraic one strictly stronger. The strong direction, bipolar implies UCT, is entirely free, resting on nothing deeper than the fact that a supremum of affine functions is always convex and lower semicontinuous.

The gap between the two notions is closed by a definitional decision — the word proper — not by a theorem proving they coincide automatically. Many textbooks move past this too quickly, leaving the impression that proper is a harmless technical adjective, when in fact it's quietly cutting an entire class of functions — the ones that are locally $-\infty$ without being globally constant — out of the theory.

The real cost of Fenchel–Moreau sits entirely in the hard direction, convex-and-lsc implies bipolar, and properness is exactly what lets the separation theorem apply cleanly there. The easy direction is close to free, barely deserving to be called part of the theorem at all — it's just the observation that a bipolar always has the shape of an intersection of half-spaces.

Next time you see the line "since $f$ is convex, closed, and proper, $f^{**}=f$," it might be worth pausing for a second: those three adjectives aren't standing next to each other by accident. Proper is quietly doing the heaviest lifting of the three.
