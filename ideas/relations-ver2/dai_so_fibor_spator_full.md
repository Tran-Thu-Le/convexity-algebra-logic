# Đại số của Fibor và Spator: Toàn bộ kết quả, viết lại theo bộ ký hiệu mới

## Bộ ký hiệu (nhắc lại, dùng xuyên suốt)

| Tầng | Ký hiệu | Tên |
|---|---|---|
| Level 1 — Primitive Geometry | $\subseteq,\ \cap,\ \cup$ | inclusion, intersection, union |
| | $+_{\mathrm{fib}}$ | fiber sum |
| | $+_{\mathrm{sp}}$ | spatial sum |
| | $(\cdot)^*$ | Fenchel polarity |
| | $U,\mathcal F,C,T$ | upward, fiber, convex, topological closures |
| Derived | $(\cdot)^{**}$ | bipolar closure |
| Level 2 — Main Algebra | $\wedge,\ \vee$ | meet, join |
| | $\triangle$ | **Fibor** |
| | $\bigtriangledown$ | **Spator** |
| | $(\cdot)^*$ | polarity, thu hẹp trên $\mathbb X$ |
| Level 3 — Linear Logic | with, plus, tensor, par | gán ở cuối, không định trước |

**Định nghĩa Level 2 từ Level 1:**
$$E\wedge F:=E\cap F,\qquad E\vee F:=(E\cup F)^{**},\qquad E\triangle F:=(E+_{\mathrm{fib}}F)^{**},\qquad E\bigtriangledown F:=(E+_{\mathrm{sp}}F)^{**}.$$

**Nền hình học:** $X:=\mathbb R^n$, $\overline{\mathbb R}:=[-\infty,+\infty]$, $X_e:=X\times\overline{\mathbb R}$, quy ước Rockafellar $(+\infty)+(-\infty):=+\infty$. $\mathbb X:=$ lớp regepi, mỗi $E\in\mathbb X$ có dạng $E_x=[e(x),+\infty]$, $e$ lồi lsc. Đơn vị: $1_\triangle:=X\times[0,+\infty]$ ($e\equiv0$), $1_\bigtriangledown:=(\{0\}\times[0,+\infty])\cup((X\setminus\{0\})\times\{+\infty\})$ ($e\equiv\delta_{\{0\}}$).

---

## Phần I — Bảy bổ đề nền tảng

**Bổ đề A (tam polar bất động).** Với mọi preepi $E$: $E^{***}=E^*$.

*Chứng minh.* Tính mở rộng $E\subseteq E^{**}$ đúng cho mọi preepi (trực tiếp từ bất đẳng thức định nghĩa polar). Tính phản biến của $(\cdot)^*$: $A\subseteq B\Rightarrow B^*\subseteq A^*$. Áp lên $E\subseteq E^{**}$: $E^{***}\subseteq E^*$. Áp tính mở rộng cho $E^*$: $E^*\subseteq E^{***}$. Vậy $E^{***}=E^*$. $\square$

Hệ quả: $E^*\in\mathbb X$ luôn đúng, với mọi preepi $E$, không cần $E\in\mathbb X$.

**Bổ đề B (polar của hợp).** $(E\cup F)^*=E^*\cap F^*$ với mọi preepi $E,F$.

*Chứng minh.* $(y,s)\in(E\cup F)^*\iff$ đúng với mọi $(x,r)\in E$ và mọi $(x,r)\in F\iff(y,s)\in E^*\cap F^*$. $\square$

**Bổ đề C (join là đối ngẫu bipolar của meet).** $E\vee F=(E^*\wedge F^*)^*$, không cần giả thiết.

*Chứng minh.* $E\vee F:=(E\cup F)^{**}=((E\cup F)^*)^*\overset{\text{BĐ B}}{=}(E^*\cap F^*)^*=(E^*\wedge F^*)^*$. $\square$

**Bổ đề D (đóng dưới giao của điểm bất động).** Nếu $A^{**}=A,B^{**}=B$ thì $(A\cap B)^{**}=A\cap B$.

*Chứng minh.* $(\cdot)^{**}$ là closure operator; tập điểm bất động của nó đóng dưới giao tùy ý. $\square$

**Bổ đề E (đơn ánh của polar trên $\mathbb X$).** Nếu $A,B\in\mathbb X$ và $A^*=B^*$ thì $A=B$.

*Chứng minh.* $A=A^{**}=(A^*)^*=(B^*)^*=B^{**}=B$. $\square$

**Bổ đề F (polar của spatial sum).** $(E+_{\mathrm{sp}}F)^*=E^*+_{\mathrm{fib}}F^*$ với mọi preepi $E,F$.

*Chứng minh (⊇).* Nếu $(y,s_1)\in E^*,(y,s_2)\in F^*$: cộng hai bất đẳng thức định nghĩa, dùng $x=x_1+x_2$, được $(y,s_1+s_2)\in(E+_{\mathrm{sp}}F)^*$.

*Chứng minh (⊆).* Cố định $y$, viết $E^*_y=[e^*(y),+\infty]$, $e^*(y):=\sup_{(x,r)\in E}(\langle x,y\rangle-r)$, tương tự $f^*(y)$. Nếu $(y,s)\in(E+_{\mathrm{sp}}F)^*$: lấy sup độc lập theo $x_1,x_2$ trong bất đẳng thức định nghĩa, được $e^*(y)+f^*(y)\le s$, tức $(y,s)\in E^*+_{\mathrm{fib}}F^*$. $\square$

**Bổ đề G (giao hoán).** $E\bigtriangledown F=F\bigtriangledown E$ và $E\triangle F=F\triangle E$, vì $+_{\mathrm{sp}}$ và $+_{\mathrm{fib}}$ đều giao hoán trên $\overline{\mathbb R}$ và trên $X$.

**Bổ đề H (kết hợp của phép cộng mở rộng).** Với quy ước Rockafellar, $(r+s)+t=r+(s+t)$ với mọi $r,s,t\in\overline{\mathbb R}$.

*Chứng minh.* Viết tường minh không quy nạp: tổng ba số bằng $+\infty$ nếu có ít nhất một số hạng $+\infty$; bằng $-\infty$ nếu không có $+\infty$ nhưng có $-\infty$; bằng tổng thông thường nếu cả ba hữu hạn — công thức này không phụ thuộc cách nhóm ngoặc. $\square$

**Bổ đề I (fiber sum của hai regepi tự động là regepi).** Nếu $A,B\in\mathbb X$ thì $A+_{\mathrm{fib}}B\in\mathbb X$, không cần đóng thêm.

*Chứng minh.* $h:=a+b$ lồi (tổng hàm lồi); lsc vì $\liminf(a(x_n)+b(x_n))\ge\liminf a(x_n)+\liminf b(x_n)\ge a(x)+b(x)$ luôn đúng khi không gặp $\infty-\infty$, và quy ước Rockafellar loại bỏ đúng dạng đó. $\square$

**Bổ đề max-plus.** $t+\max(a,b)=\max(t+a,t+b)$ với mọi $t,a,b\in\overline{\mathbb R}$.

*Chứng minh.* $t$ hữu hạn: luật cộng thường. $t=+\infty$: cả ba đại lượng $=+\infty$. $t=-\infty$: nếu $\max(a,b)=+\infty$ cả hai vế $=+\infty$; ngược lại cả hai vế $=-\infty$. $\square$

**Mệnh đề hợp nhất (Spator là đối ngẫu bipolar của Fibor).**
$$E\bigtriangledown F = (E^*\triangle F^*)^*.$$

*Chứng minh.* Áp Bổ đề F lên $E,F$: $(E+_{\mathrm{sp}}F)^*=E^*+_{\mathrm{fib}}F^*$. Vậy
$$E\bigtriangledown F=(E+_{\mathrm{sp}}F)^{**}=((E+_{\mathrm{sp}}F)^*)^*=(E^*+_{\mathrm{fib}}F^*)^*\overset{\text{BĐ A}}{=}((E^*+_{\mathrm{fib}}F^*)^{**})^*=(E^*\triangle F^*)^*.\qquad\blacksquare$$

Hệ quả: $\{\wedge,\vee,\triangle,\bigtriangledown\}$ chỉ có **hai bậc tự do** ở Level 1 ($\cap$ hay $\cup$; $+_{\mathrm{fib}}$ hay $+_{\mathrm{sp}}$) — $\vee,\bigtriangledown$ đều là đối ngẫu bipolar tự động, không phải định nghĩa độc lập thêm.

---

## Phần II — Bốn luật phân phối

### D1 — Fibor đối với Meet

**Phát biểu.** Với mọi $E,F,G\in\mathbb X$: $\ E\triangle(F\wedge G)=(E\triangle F)\wedge(E\triangle G)$.

**Chứng minh.** Viết qua hàm $e,f,g$ lồi lsc. Với mỗi $x$:
$$\bigl(E+_{\mathrm{fib}}(F\wedge G)\bigr)_x=[e(x)+\max(f(x),g(x)),+\infty]\overset{\text{max-plus}}{=}[\max(e(x)+f(x),e(x)+g(x)),+\infty]=\bigl((E+_{\mathrm{fib}}F)\cap(E+_{\mathrm{fib}}G)\bigr)_x,$$
đẳng thức thật sự $(*)$. Đặt $A:=E+_{\mathrm{fib}}F,B:=E+_{\mathrm{fib}}G$; theo Bổ đề I, $A,B\in\mathbb X$, tức $A^{**}=A,B^{**}=B$. Từ $(*)$ và Bổ đề D:
$$E\triangle(F\wedge G)=(A\cap B)^{**}=A\cap B=A^{**}\cap B^{**}=(E\triangle F)\wedge(E\triangle G).\qquad\blacksquare$$

### D2 — Spator đối với Join (đối ngẫu của D1)

**Phát biểu.** Với mọi $E,F,G\in\mathbb X$: $\ E\bigtriangledown(F\vee G)=(E\bigtriangledown F)\vee(E\bigtriangledown G)$.

**Chứng minh.** Đặt $e:=E^*,f:=F^*,g:=G^*\in\mathbb X$ (Bổ đề A). Theo Bổ đề C: $(F\vee G)^*=(f\wedge g)^{**}\overset{\text{BĐ D}}{=}f\wedge g$. Theo Mệnh đề hợp nhất:
$$E\bigtriangledown(F\vee G)=\bigl(e\triangle(f\wedge g)\bigr)^*\overset{\text{D1}}{=}\bigl((e\triangle f)\wedge(e\triangle g)\bigr)^*.$$
Mặt khác $(E\bigtriangledown F)^*=e\triangle f$, $(E\bigtriangledown G)^*=e\triangle g$ (Mệnh đề hợp nhất, đã closed), nên theo Bổ đề C:
$$(E\bigtriangledown F)\vee(E\bigtriangledown G)=\bigl((e\triangle f)\wedge(e\triangle g)\bigr)^*.$$
Hai vế trùng nhau. $\blacksquare$

### D3 — Fibor đối với Join (thất bại)

**Phát biểu.** $(E\triangle F)\vee(E\triangle G)\subseteq E\triangle(F\vee G)$, chặt nói chung.

**Chứng minh $\subseteq$.** $F,G\subseteq F\vee G\Rightarrow E\triangle F,E\triangle G\subseteq E\triangle(F\vee G)$ (đơn điệu); vế phải đã đóng, lấy $\vee$ hai vế cho bao hàm.

**Phản ví dụ.** $e(x)=|x-2|,f(x)=|x|,g(x)=|x-4|$. $m:=\min(f,g)$, $h:=\mathrm{conv}(m)=\max(-x,0,x-4)$.

Vế trái $\leftrightarrow e(2)+h(2)=0+0=0$. Vế phải $\leftrightarrow k(2)$, $k:=\mathrm{conv}(e+m)$: bảng độ dốc $-2,0,0,+2$ (không giảm) $\Rightarrow k=e+m$, $k(2)=2$. $0\neq2$, bao hàm chặt. $\blacksquare$

### D4 — Spator đối với Meet (thất bại, đối ngẫu của D3)

**Phát biểu.** $E\bigtriangledown(F\wedge G)\subseteq(E\bigtriangledown F)\wedge(E\bigtriangledown G)$, chặt nói chung.

**Chứng minh.** Đối ngẫu hình thức của D3 qua Bổ đề C + Mệnh đề hợp nhất. Phản ví dụ độc lập: $m:=f\wedge g=|x-2|+2$; dùng $\inf_u|u|+|c-u|=|c|$: $\mathrm{cl}(e\,\square\,m)(0)=6$, $\max(e\,\square\,f(0),e\,\square\,g(0))=\max(2,4)=4$. $6\neq4$. $\blacksquare$

**Bảng tổng kết D1–D4:**

| # | Phát biểu | Đúng? |
|---|---|---|
| D1 | $\triangle$ qua $\wedge$ | ✅ vô điều kiện |
| D2 | $\bigtriangledown$ qua $\vee$ | ✅ vô điều kiện |
| D3 | $\triangle$ qua $\vee$ | ❌ chỉ $\subseteq$ |
| D4 | $\bigtriangledown$ qua $\wedge$ | ❌ chỉ $\subseteq$ |

---

## Phần III — Khối monoid: kết hợp tính và đơn vị

### Mệnh đề M1 — Kết hợp tính của Fibor

**Phát biểu.** Với mọi $E,F,G\in\mathbb X$: $\ (E\triangle F)\triangle G=E\triangle(F\triangle G)$.

**Chứng minh.** Đặt $A:=E+_{\mathrm{fib}}F\in\mathbb X$ (Bổ đề I), $A^{**}=A$:
$$(E\triangle F)\triangle G=A^{**}\triangle G=A\triangle G=(A+_{\mathrm{fib}}G)^{**}=\bigl((E+_{\mathrm{fib}}F)+_{\mathrm{fib}}G\bigr)^{**}\overset{\text{BĐ H}}{=}(E+_{\mathrm{fib}}F+_{\mathrm{fib}}G)^{**}.$$
Đặt $B:=F+_{\mathrm{fib}}G\in\mathbb X$, tương tự $E\triangle(F\triangle G)=(E+_{\mathrm{fib}}F+_{\mathrm{fib}}G)^{**}$. Hai vế trùng nhau. $\blacksquare$

### Mệnh đề M2 — Đơn vị của Fibor

**Phát biểu.** Với mọi $E\in\mathbb X$: $\ E\triangle1_\triangle=1_\triangle\triangle E=E$.

**Chứng minh.** $(E+_{\mathrm{fib}}1_\triangle)_x=\{r+s:r\ge e(x),s\ge0\}=[e(x),+\infty]=E_x$ — đẳng thức tập hợp, không cần đóng thêm. Vì $E$ đã closed: $E\triangle1_\triangle=(E+_{\mathrm{fib}}1_\triangle)^{**}=E^{**}=E$. Giao hoán (Bổ đề G) cho vế kia. $\blacksquare$

### Mệnh đề M3 — Kết hợp tính và đơn vị của Spator (đối ngẫu qua $*$)

**Phát biểu (kết hợp).** Với mọi preepi $E,F,G$ (không cần $\in\mathbb X$): $\ (E\bigtriangledown F)\bigtriangledown G=E\bigtriangledown(F\bigtriangledown G)$.

**Chứng minh.** $(E\bigtriangledown F)^*=E^*\triangle F^*$ (Mệnh đề hợp nhất, tự động closed). Vậy
$$(E\bigtriangledown F)\bigtriangledown G=\bigl((E\bigtriangledown F)^*\triangle G^*\bigr)^*=\bigl((E^*\triangle F^*)\triangle G^*\bigr)^*\overset{\text{M1, vì }E^*,F^*,G^*\in\mathbb X}{=}\bigl(E^*\triangle(F^*\triangle G^*)\bigr)^*=E\bigtriangledown(F\bigtriangledown G).\quad\blacksquare$$

**Đơn vị.** Kiểm trực tiếp $1_\triangle^*=1_\bigtriangledown$ (tính toán: ràng buộc $\langle x,y\rangle\le s$ với $r=0$ buộc $y=0,s\ge0$ hoặc $s=+\infty$), và $1_\bigtriangledown^*=1_\triangle^{**}=1_\triangle$. Với $E\in\mathbb X$:
$$E\bigtriangledown1_\bigtriangledown=(E^*\triangle1_\bigtriangledown^*)^*=(E^*\triangle1_\triangle)^*\overset{\text{M2}}{=}(E^*)^*=E^{**}=E.\qquad\blacksquare$$

### Cảnh báo: các mệnh đề trên KHÔNG chuyển được sang phía Spator qua $+_{\mathrm{sp}}$ trực tiếp

Chốt của M1 là Bổ đề I — đặc thù $+_{\mathrm{fib}}$. Bổ đề tương ứng cho $+_{\mathrm{sp}}$ ("$A,B\in\mathbb X\Rightarrow A+_{\mathrm{sp}}B\in\mathbb X$") **sai nói chung**: tổng $+_{\mathrm{sp}}$ (Minkowski) của hai tập lồi đóng có thể không đóng.

**Phản ví dụ.** $X=\mathbb R$, $A:=\mathrm{epi}(1/x\text{ trên }(0,\infty))$, $B:=(-\infty,0]\times\{0\}$ — cả hai lồi, đóng. $A+_{\mathrm{sp}}B$ có fiber tại $z=0$ bằng $(0,+\infty)$ (mở): điểm $(0,0)$ là giới hạn (lấy $x_n\to\infty$) nhưng không thuộc tập. Vậy $A+_{\mathrm{sp}}B$ không đóng.

**Hệ quả:** $E\triangle F$ (viết qua $+_{\mathrm{sp}}$, tức thử chứng minh trực tiếp kết hợp tính của $\bigtriangledown$ bằng cùng kỹ thuật M1 nhưng thay $+_{\mathrm{fib}}\to+_{\mathrm{sp}}$) **không** tự động closed, nên bước "$A^{**}=A$" trong chứng minh kiểu M1 gãy. Tuy nhiên M3 ở trên **vẫn đứng vững** — vì nó không đi đường đó, mà đi vòng qua polar và dùng M1 (Fibor) làm trung gian. Câu hỏi còn lại, thật sự mở, là: có cách chứng minh **trực tiếp** (không qua polar) cho kết hợp tính của $\bigtriangledown$ hay không, và nó có cần điều kiện qualification hay không — vì M3 chứng minh kết hợp tính bằng cách chuyển hoàn toàn sang polar của $E,F,G$, chứ không phải một phát biểu về $+_{\mathrm{sp}}$ trực tiếp trên $E,F,G$ gốc.

*(Ghi chú tự phản biện: thật ra M3 đã đủ để kết luận $\bigtriangledown$ kết hợp — vì đẳng thức $(E\bigtriangledown F)\bigtriangledown G=E\bigtriangledown(F\bigtriangledown G)$ là phát biểu về chính $E,F,G$, không phải về $E^*,F^*,G^*$; việc chứng minh đi qua polar không làm giảm giá trị kết luận. Vậy thực chất **kết hợp tính của Spator đã được chứng minh xong, vô điều kiện**, đúng như M3 phát biểu — điểm "mở" duy nhất còn lại là liệu có tồn tại một chứng minh *trực tiếp* không qua polar, một câu hỏi về mỹ học/hiểu biết cấu trúc chứ không phải về tính đúng đắn của kết quả.)*

**Bảng tổng kết monoid:**

| Toán tử | Kết hợp tính | Đơn vị |
|---|---|---|
| $\triangle$ (Fibor) | ✅ M1, trực tiếp qua $+_{\mathrm{fib}}$ | ✅ M2 |
| $\bigtriangledown$ (Spator) | ✅ M3, qua polar + M1 (dù $+_{\mathrm{sp}}$ tự thân không đóng) | ✅ M3 |

---

## Phần IV — Điều kiện dấu / tương thích thứ tự

**Mệnh đề N1 (Fibor, đối xứng).** $g\ge0\Rightarrow E\triangle F\subseteq E$; $\ g\le0\Rightarrow E\subseteq E\triangle F$ (đối xứng quanh $1_\triangle$, đơn vị là biên).

**Mệnh đề N2 (Spator, bất đối xứng).** $g(0)\le0\Rightarrow E\subseteq E\bigtriangledown F$ (điều kiện scalar, dễ đạt); $\ F\subseteq1_\bigtriangledown\Rightarrow E\bigtriangledown F\subseteq E$ (điều kiện hàm toàn cục, khó đạt).

```
⊆:  ∧ ←──[g≥0]── E△F ⊆ E ⊆ E△F ──[g≤0]──→ ∨    │    ∧ ←──[g≥δ₀, khó]── E▽F ⊆ E ⊆ E▽F ──[g(0)≤0, dễ]──→ ∨
```

---

## Phần V — Gán Level 3 (MALL), hệ quả của Phần II–IV

Với with$\leftrightarrow\wedge$, plus$\leftrightarrow\vee$ cố định, bốn luật MALL đòi hỏi tensor phân phối qua plus, par phân phối qua with. Đối chiếu D1–D4:

$$\boxed{\text{tensor}\leftrightarrow\bigtriangledown\ (\text{Spator}),\qquad\text{par}\leftrightarrow\triangle\ (\text{Fibor}).}$$

Đây là gán **duy nhất tương thích**, suy ra từ Phần II, không phải giả định. Khác với lo ngại ban đầu ở Phần III (trước khi làm rõ M3), khối monoid **không còn là vật cản**: cả Fibor lẫn Spator đều đã có kết hợp tính và đơn vị đầy đủ, vô điều kiện trên $\mathbb X$ — Spator qua con đường polar (M3), Fibor trực tiếp (M1–M2). Điều còn để ngỏ cho Milestone III là các tiên đề closed-monoidal sâu hơn (residual $\multimap$, exponential $!,?$), chưa phải kết hợp tính/đơn vị.
