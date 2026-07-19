
File này là phần tiếp theo của [[ideas/relations-ver2/second-proofs/old/from-geometry-to-algebra]]
## 12. Kết nối với Convex Analysis

Ta nhắc lại: $\mathbb X = \{E\subseteq\overline X : E=E^{**}\}$ là họ regepi, trang bị
$$\textbf{meet: } E\wedge F = E\cap F \quad(\text{Mệnh đề }4.1), \qquad \textbf{fibor: } E+_{fib}^{c}F = (E+_{fib}^{(s)}F)^{**}.$$
Ký hiệu $X:=\mathbb R^n$, $\overline{\mathbb R}:=(-\infty,+\infty]$, và
$$\mathrm{Conv}(X) := \{e : X\to\overline{\mathbb R}\ \text{chính thường (proper), lồi, nửa liên tục dưới (lsc/đóng)}\}.$$

Toàn bộ mục này dựa trên một bổ đề cầu nối duy nhất, kết nối polar tập hợp $E^*$ (Định nghĩa 1.1.3) với **liên hợp Fenchel** hàm số $e^*(y):=\sup_{x\in X}\big(\langle x,y\rangle - e(x)\big)$.

---

### 12.0. Bổ đề cầu nối: polar của epigraph = epigraph của liên hợp

**Bổ đề 12.0.1.** Với mọi $g: X \to \overline{\mathbb R}$ chính thường:
$$\mathrm{epi}(g)^* = \mathrm{epi}(g^*).$$

*Chứng minh.* Theo định nghĩa polar (Định nghĩa 1.1.3), với $p=(y,s)$:
$$p \in \mathrm{epi}(g)^* \iff \forall (x,r)\in\mathrm{epi}(g),\ \langle x,y\rangle \le r+s \iff \forall x\in\mathrm{dom}(g)\ \forall r\ge g(x),\ \langle x,y\rangle \le r+s.$$
Với $x$ cố định, ràng buộc chặt nhất xảy ra tại $r=g(x)$ (giá trị nhỏ nhất được phép), nên điều kiện trên tương đương:
$$\forall x\in X,\ \langle x,y\rangle \le g(x)+s \iff \forall x,\ s \ge \langle x,y\rangle - g(x) \iff s \ge \sup_x\big(\langle x,y\rangle-g(x)\big) = g^*(y).$$
Vậy $p\in\mathrm{epi}(g)^* \iff s\ge g^*(y) \iff p\in\mathrm{epi}(g^*)$. $\blacksquare$

**Hệ quả 12.0.2.** $\mathrm{epi}(g)^{**} = \mathrm{epi}(g^{**})$.

*Chứng minh.* Áp Bổ đề 12.0.1 hai lần: $\mathrm{epi}(g)^{**} = \big(\mathrm{epi}(g^*)\big)^* = \mathrm{epi}(g^{**})$. $\blacksquare$

**Bổ đề 12.0.3 (Sandwich cho bipolar closure).** Nếu $A\subseteq B\subseteq \overline A^{\,top}$ (đóng theo tô pô thường trên $\overline X$) thì $A^{**}=B^{**}$.

*Chứng minh.* Mỗi tập $\{e=(x,r): e\sim p\}=\{(x,r):\langle x,y\rangle\le r+s\}$ (với $p=(y,s)$ cố định) đóng theo tô pô, vì đây là miền $\le$ của một hàm liên tục $\langle x,y\rangle - r$ trên $\overline X$. Do đó $A^{**}=(A^*)^*=\bigcap_{p\in A^*}\{e:e\sim p\}$ là giao các tập đóng, nên **đóng theo tô pô**. Kết hợp $A\subseteq A^{**}$ (Bổ đề 3.2): $A^{**}$ là một tập đóng chứa $A$, nên $\overline A^{\,top}\subseteq A^{**}$. Vậy
$$A\subseteq B\subseteq \overline A^{\,top}\subseteq A^{**}.$$
Áp $(-)^{**}$ (đơn điệu, Bổ đề 3.4b) vào $B\subseteq A^{**}$: $B^{**}\subseteq A^{****}=A^{**}$ (dùng lũy đẳng, Bổ đề 3.4c). Áp vào $A\subseteq B$: $A^{**}\subseteq B^{**}$. Hai chiều cho $A^{**}=B^{**}$. $\blacksquare$

---

### 12.1. Định lý 1 — Song ánh regepi $\leftrightarrow$ hàm lồi đóng chính thường

**Định lý 12.1.1.** Ánh xạ
$$\Phi:\mathrm{Conv}(X)\longrightarrow \mathbb X\setminus\{\emptyset,\overline X\}, \qquad \Phi(e):=\mathrm{epi}(e)$$
là một song ánh, với ánh xạ ngược
$$\Psi(E)(x):=\inf\{r:(x,r)\in E\}.$$

*Chứng minh.*

**(a) $\Phi$ nhận giá trị trong $\mathbb X$.** Vì $e$ lồi đóng chính thường trên $X=\mathbb R^n$, định lý tách (separating hyperplane) cổ điển cho $e$ có ít nhất một hàm affine chặn dưới, nên $e^*$ chính thường; $e^*$ luôn lồi và lsc (là $\sup$ của các hàm affine liên tục theo $y$). Định lý Fenchel–Moreau cổ điển cho $e^{**}=e$. Kết hợp Hệ quả 12.0.2:
$$\Phi(e)^{**} = \mathrm{epi}(e)^{**} = \mathrm{epi}(e^{**}) = \mathrm{epi}(e) = \Phi(e),$$
vậy $\Phi(e)\in\mathbb X$; rõ ràng $\Phi(e)\ne\emptyset$ (vì $e$ chính thường) và $\Phi(e)\ne\overline X$ (vì $e\not\equiv-\infty$, thật ra $e$ không nhận $-\infty$).

**(b) Đơn ánh.** Nếu $\mathrm{epi}(e)=\mathrm{epi}(f)$ thì với mọi $x$: $\{r:r\ge e(x)\}=\{r:r\ge f(x)\}$, suy ra $e(x)=f(x)$.

**(c) Toàn ánh.** Lấy $E\in\mathbb X$, $E\ne\emptyset,\overline X$. Vì $E=E^{**}=(E^*)^*$, $E$ có dạng "polar của một tập", nên theo cùng lập luận ở Bổ đề 12.0.3: $E$ là giao của các nửa-không-gian $\{(x,r):\langle x,y\rangle\le r+s\}$ ($p=(y,s)\in E^*$) — mỗi nửa-không-gian này lồi (miền $\le$ của hàm affine theo $(x,r)$), đóng tô pô, và **upward** theo $r$ (nếu $(x,r)$ thỏa thì $(x,r')$ với $r'\ge r$ cũng thỏa). Do đó $E$ lồi, đóng, và mỗi thớ $E_x:=\{r:(x,r)\in E\}$ là một tia $[\Psi(E)(x),+\infty]$ hoặc rỗng — tức $E=\mathrm{epi}(\Psi(E))$ đúng nghĩa tập hợp. Vì $E$ lồi $\Rightarrow \Psi(E)$ lồi; $E$ đóng $\Rightarrow \Psi(E)$ lsc; $E\ne\emptyset\Rightarrow\Psi(E)\not\equiv+\infty$; $E\ne\overline X$ (và các thớ là tia đóng có đáy hữu hạn-hoặc-rỗng, không thể toàn bộ $(-\infty,+\infty]$) $\Rightarrow \Psi(E)$ không nhận $-\infty$. Vậy $\Psi(E)\in\mathrm{Conv}(X)$, và $\Phi(\Psi(E))=\mathrm{epi}(\Psi(E))=E$. $\blacksquare$

---

### 12.2. Định lý 2 — Join là closure của hợp epigraph, ứng với bao lồi đóng của $\min$

**Định nghĩa 12.2.1.** $E\vee F := (E^*\wedge F^*)^*$ (như Định nghĩa 5.2), và gọi đây là **join**.

**Định lý 12.2.2 (Join).** Với $E=\mathrm{epi}(e), F=\mathrm{epi}(f)\in\mathbb X$:
$$E\vee F = (E\cup F)^{**} = \mathrm{epi}\big(\mathrm{cl\,conv}(\min(e,f))\big),$$
tức **join là closure (bipolar) của hợp hai epigraph thông thường**, và ở tầng hàm, chính là **bao lồi đóng (closed convex hull) của $\min(e,f)$**.

*Chứng minh.*

**Bước 1 (đã có, Định lý 5.3): $E\vee F=(E\cup F)^{**}$.** Nhắc lại: $E^*\wedge F^*\overset{\text{Mệnh đề }4.1}{=}E^*\cap F^*\overset{\text{Bổ đề }3.3}{=}(E\cup F)^*$, áp $*$ hai vế cho kết quả.

**Bước 2 (hợp epigraph = epigraph của min, đẳng thức tập hợp, không cần đóng).**
$$(x,r)\in E\cup F \iff r\ge e(x)\ \text{hoặc}\ r\ge f(x) \iff r\ge\min(e(x),f(x)).$$
Vậy $E\cup F = \mathrm{epi}(\min(e,f))$ **chính xác**, đây là một đẳng thức tập hợp thuần túy, không có "mất mát" nào.

**Bước 3 (đóng bipolar = biconjugate hàm số).** Theo Hệ quả 12.0.2:
$$(E\cup F)^{**} = \mathrm{epi}(\min(e,f))^{**} = \mathrm{epi}\Big(\big(\min(e,f)\big)^{**}\Big).$$

**Bước 4 (Fenchel–Moreau tổng quát, cho hàm có thể không lồi).** Với $g:X\to\overline{\mathbb R}$ chính thường và bị chặn dưới bởi một hàm affine (ở đây $g=\min(e,f)$, bị chặn dưới bởi $\min$ của các affine-minorant của $e,f$ — vẫn affine từng đoạn nhưng không cần affine toàn cục, chỉ cần tồn tại **một** affine minorant chung, ví dụ minorant của $e$ nếu nó cũng minorize $f$, hoặc lấy min của hai affine minorant — điều này đủ để $g^*$ chính thường):
$$g^{**} = \mathrm{cl\,conv}(g),$$
bao lồi đóng — hàm lồi-đóng lớn nhất bị trội bởi $g$ (định lý cổ điển: $g^{**}(x)=\sup\{a(x): a\text{ affine}, a\le g\}$, và vế phải chính là đặc trưng affine-minorant của $\mathrm{cl\,conv}(g)$, qua định lý tách).

Áp cho $g=\min(e,f)$ (nói chung **không lồi**, dù $e,f$ lồi — đây là lý do cần "bao lồi", không chỉ "đóng"):
$$\big(\min(e,f)\big)^{**} = \mathrm{cl\,conv}\big(\min(e,f)\big).$$

Kết hợp Bước 1, 3, 4:
$$E\vee F = (E\cup F)^{**} = \mathrm{epi}\big(\mathrm{cl\,conv}(\min(e,f))\big). \qquad\blacksquare$$

---

### 12.3. Định lý 3 — Spator là closure của Minkowski sum, ứng với closure của inf-convolution

**Định nghĩa 12.3.1.** $E\,{+_{sp}}\,F := \{(x_1+x_2,r_1+r_2): (x_1,r_1)\in E,(x_2,r_2)\in F\}$ (spatial/Minkowski sum, đã có ở tex gốc). Định nghĩa **spator**, song song với join:
$$E\,\mathrm{spator}\,F := \big(E^*+_{fib}^{c}F^*\big)^*.$$

**Định nghĩa 12.3.2 (Inf-convolution).** $(e\,\square\,f)(z):=\inf_{x+y=z}\big(e(x)+f(y)\big)$.

**Bổ đề 12.3.3 ($e\square f$ lồi khi $e,f$ lồi).** *Chứng minh.* Lấy $z_1,z_2\in X$, $\lambda\in[0,1]$, $z_\lambda:=\lambda z_1+(1-\lambda)z_2$. Với $\varepsilon>0$, chọn $x_i+y_i=z_i$ ($i=1,2$) sao cho $e(x_i)+f(y_i)\le (e\square f)(z_i)+\varepsilon$. Đặt $x_\lambda:=\lambda x_1+(1-\lambda)x_2$, $y_\lambda:=\lambda y_1+(1-\lambda)y_2$; khi đó $x_\lambda+y_\lambda=z_\lambda$, và tính lồi của $e,f$ cho
$$(e\square f)(z_\lambda)\le e(x_\lambda)+f(y_\lambda)\le \lambda\big(e(x_1)+f(y_1)\big)+(1-\lambda)\big(e(x_2)+f(y_2)\big)\le \lambda(e\square f)(z_1)+(1-\lambda)(e\square f)(z_2)+\varepsilon.$$
Cho $\varepsilon\to0$. $\blacksquare$

**Bổ đề 12.3.4 (Công thức liên hợp của inf-convolution — luôn đúng, không cần đóng).** $(e\square f)^* = e^*+f^*$.

*Chứng minh.*
$$(e\square f)^*(y) = \sup_z\Big(\langle z,y\rangle - \inf_{x+w=z}\big(e(x)+f(w)\big)\Big) = \sup_{x,w}\Big(\langle x+w,y\rangle - e(x)-f(w)\Big)$$
$$= \sup_x\big(\langle x,y\rangle-e(x)\big) + \sup_w\big(\langle w,y\rangle-f(w)\big) = e^*(y)+f^*(y). \qquad\blacksquare$$

**Định lý 12.3.5 (Spator).** Với $E=\mathrm{epi}(e), F=\mathrm{epi}(f)\in\mathbb X$ ($e,f\in\mathrm{Conv}(X)$, $\mathrm{dom}(e^*)\cap\mathrm{dom}(f^*)\ne\emptyset$):
$$E\,\mathrm{spator}\,F = (E+_{sp}F)^{**} = \mathrm{epi}\big(\mathrm{cl}(e\square f)\big),$$
tức **spator chính là closure (bipolar) của Minkowski sum thông thường của hai tập**, và ở tầng hàm, chính là **closure của inf-convolution thông thường** (không cần bao lồi thêm, vì $e\square f$ đã lồi theo Bổ đề 12.3.3).

*Chứng minh.*

**Bước 1 (tầng hàm, đi qua $E^*,F^*$).** Theo Bổ đề 12.0.1: $E^*=\mathrm{epi}(e^*)$, $F^*=\mathrm{epi}(f^*)$. Theo Bổ đề 8.2.3 và 8.2.4 (áp cho $e^*,f^*$, với giả thiết miền xác định giao nhau khác rỗng): $E^*+_{fib}^cF^* = \mathrm{epi}(e^*+f^*)$ (đóng thừa, như đã thấy ở mục 8.2(c)). Áp Bổ đề 12.0.1 lần nữa:
$$E\,\mathrm{spator}\,F = \big(E^*+_{fib}^cF^*\big)^* = \mathrm{epi}(e^*+f^*)^* = \mathrm{epi}\big((e^*+f^*)^*\big).$$

**Bước 2 (tính $(e^*+f^*)^*$ qua Bổ đề 12.3.4 và Fenchel–Moreau).** Áp Bổ đề 12.3.4 cho cặp $(e,f)$: $(e\square f)^*=e^*+f^*$. Lấy liên hợp hai vế:
$$(e\square f)^{**} = (e^*+f^*)^*.$$
Theo Fenchel–Moreau tổng quát (Bước 4, mục 12.2) và Bổ đề 12.3.3 ($e\square f$ đã lồi):
$$(e\square f)^{**} = \mathrm{cl\,conv}(e\square f) = \mathrm{cl}(e\square f)$$
(bao lồi đóng của một hàm đã lồi chỉ còn là phép đóng thông thường). Vậy
$$(e^*+f^*)^* = \mathrm{cl}(e\square f), \qquad \Rightarrow \qquad E\,\mathrm{spator}\,F = \mathrm{epi}\big(\mathrm{cl}(e\square f)\big). \tag{$\star$}$$

**Bước 3 (đối chiếu với $E+_{sp}F$: quan hệ sandwich).** Ta có, theo định nghĩa:
$$(z,u)\in E+_{sp}F \iff \exists x,y:\ x+y=z,\ u\ge e(x)+f(y).$$

*Chiều 1: $E+_{sp}F \subseteq \mathrm{epi}(e\square f)$.* Nếu $\exists(x,y)$ với $u\ge e(x)+f(y)$ thì $u\ge (e\square f)(z)$ (vì $(e\square f)(z)$ là infimum, nên $\le e(x)+f(y)$).

*Chiều 2: $\mathrm{epi}(e\square f)\subseteq \overline{E+_{sp}F}^{\,top}$.* Nếu $u > (e\square f)(z)$ (chặt), theo định nghĩa infimum tồn tại $(x,y)$, $x+y=z$, với $e(x)+f(y) < u$, tức $(z,u)\in E+_{sp}F$ trực tiếp. Nếu $u=(e\square f)(z)$ đúng bằng (biên, có thể infimum không đạt được), thì với mọi $\varepsilon>0$, $(z,u+\varepsilon)\in E+_{sp}F$ theo lập luận trên, và $(z,u+\varepsilon)\to(z,u)$ khi $\varepsilon\to0^+$ theo tô pô thường trên $\overline X$. Vậy $(z,u)\in \overline{E+_{sp}F}^{\,top}$.

Kết hợp hai chiều:
$$E+_{sp}F \ \subseteq\ \mathrm{epi}(e\square f) \ \subseteq\ \overline{E+_{sp}F}^{\,top}.$$

**Bước 4 (áp Bổ đề sandwich 12.0.3).** Với $A:=E+_{sp}F$, $B:=\mathrm{epi}(e\square f)$: $A\subseteq B\subseteq\overline A^{\,top}$, nên
$$(E+_{sp}F)^{**} = \mathrm{epi}(e\square f)^{**} \overset{\text{HQ }12.0.2}{=} \mathrm{epi}\big((e\square f)^{**}\big) = \mathrm{epi}\big(\mathrm{cl}(e\square f)\big).$$

**Kết luận.** So với $(\star)$:
$$E\,\mathrm{spator}\,F = \mathrm{epi}\big(\mathrm{cl}(e\square f)\big) = (E+_{sp}F)^{**}. \qquad\blacksquare$$

---

### 12.4. Tổng kết đối xứng meet/fibor $\leftrightarrow$ join/spator

| | Định nghĩa qua polar | = Closure của phép toán tập hợp thô | Ở tầng hàm |
|---|---|---|---|
| **meet** | $E\wedge F$ | $=E\cap F$ (không cần đóng, Mệnh đề 4.1) | $\max(e,f)$ (Bổ đề 8.2.3, đã lồi-đóng sẵn) |
| **join** | $(E^*\wedge F^*)^*$ | $=(E\cup F)^{**}$ (Định lý 5.3) | $\mathrm{cl\,conv}\big(\min(e,f)\big)$ — **cần bao lồi** vì $\min$ không lồi |
| **fibor** | $E+_{fib}^{c}F$ | $=(E+_{fib}^{(s)}F)^{**}$, thực ra $=E+_{fib}^{(s)}F$ khi proper (mục 8.2c) | $e+f$ (đã lồi-đóng sẵn) |
| **spator** | $(E^*+_{fib}^cF^*)^*$ | $=(E+_{sp}F)^{**}$ (Định lý 12.3.5) | $\mathrm{cl}(e\square f)$ — **chỉ cần đóng**, vì $e\square f$ đã lồi (Bổ đề 12.3.3) |

Điểm bất đối xứng thú vị: **join** cần bao lồi đóng đầy đủ (vì $\min$ phá vỡ tính lồi), trong khi **spator** chỉ cần đóng thông thường (vì inf-convolution bảo toàn tính lồi) — phản ánh đúng hiện tượng cổ điển trong convex analysis rằng $\wedge,+$ ("$\max$", "$+$") giữ nguyên regularity của regepi, còn các đối ngẫu $\vee,+_{sp}$ ("$\min$", inf-convolution) chỉ giữ được lồi tính (đối với spator) hoặc mất cả lồi tính lẫn tính đóng (đối với join, vì $\min$ của hai hàm lồi không lồi) và cần đóng bipolar để phục hồi.