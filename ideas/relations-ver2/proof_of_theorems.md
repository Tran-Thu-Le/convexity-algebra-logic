# Định lý tầng Đại số: xây dựng chỉ từ API Lemmas và Main Operators

## Quy ước

Chỉ dùng: bốn main operator $\wedge,\vee,\triangle,\bigtriangledown$, phép $(\cdot)^{**}$ (và $(\cdot)^*$ thu hẹp trên $\mathbb X$), cùng **API lemmas** đã thiết lập: **L.A, L.B, L.C, L.D, L.E, L.F, L.G, L.H, L.MP, L.I, L.UD, P.U** (xem `api_lemmas_day_du.md`). Bất cứ chỗ nào chứng minh cần vượt xuống tầng dưới (toán tử/closure nguyên thủy $\cap,\cup,+_{\rm fib},+_{\rm sp},U,\mathcal F,C,T$ dùng trực tiếp, hoặc biểu diễn hàm số $e,f,g$ lồi/lsc), điều đó được ghi **Remark** ngay sau chứng minh.

---

## T0 — Đơn điệu của $\triangle,\bigtriangledown$

**Phát biểu.** Nếu $F\subseteq F'$ thì $E\triangle F\subseteq E\triangle F'$ và $E\bigtriangledown F\subseteq E\bigtriangledown F'$.

**Chứng minh.** $F\subseteq F'\Rightarrow E+_{\rm fib}F\subseteq E+_{\rm fib}F'$ (mọi phần tử $(x,r+s)$ với $(x,s)\in F$ cũng có $(x,s)\in F'$). Áp $(\cdot)^{**}$ đơn điệu lên bao hàm này. Tương tự cho $+_{\rm sp}$. $\blacksquare$

**Remark (tầng dưới).** Bước đầu dùng trực tiếp định nghĩa nguyên thủy của $+_{\rm fib},+_{\rm sp}$ (không qua API lemma nào). Tính đơn điệu của $(\cdot)^{**}$ tự nó không phải một API lemma được đặt tên riêng — nó là hệ quả của P2 (phản biến của $(\cdot)^*$) áp hai lần, một bước nằm *bên trong* chứng minh của L.D chứ không được liệt kê thành lemma độc lập. Vậy T0 cần đi xuống đúng một bậc dưới API-lemma tier.

---

## T1 — Idempotence của $\wedge,\vee$

**Phát biểu.** $E\wedge E=E$, $\ E\vee E=E$.

**Chứng minh ($\wedge$).** $E\wedge E=E\cap E=E$.

**Chứng minh ($\vee$).** $E\vee E\overset{\text{L.C}}{=}(E^*\wedge E^*)^*=(E^*\cap E^*)^*=(E^*)^*=E^{**}=E$ (dùng $E\in\mathbb X\Rightarrow E^{**}=E$). $\blacksquare$

**Remark (tầng dưới).** $E\cap E=E$ là tính idempotent nguyên thủy của $\cap$, không phải một API lemma — dùng ngầm ở cả hai chứng minh.

---

## T2 — Giao hoán của $\wedge,\vee,\triangle,\bigtriangledown$

**Phát biểu.** Cả bốn toán tử đều giao hoán.

**Chứng minh ($\triangle,\bigtriangledown$).** Chính là **L.G**, dùng trực tiếp, không cần thêm gì. $\blacksquare$

**Chứng minh ($\wedge$).** $E\wedge F=E\cap F=F\cap E=F\wedge E$.

**Chứng minh ($\vee$).** $E\vee F\overset{\text{L.C}}{=}(E^*\wedge F^*)^*=(F^*\wedge E^*)^*\overset{\text{L.C}}{=}F\vee E$, dùng giao hoán của $\wedge$ ở giữa. $\blacksquare$

**Remark (tầng dưới).** Phần $\wedge$ dùng giao hoán nguyên thủy của $\cap$, không phải API lemma. Phần $\triangle,\bigtriangledown$ hoàn toàn sạch (chỉ L.G).

---

## T3 — Kết hợp tính của $\wedge,\vee$

**Phát biểu.** $(E\wedge F)\wedge G=E\wedge(F\wedge G)$, $\ (E\vee F)\vee G=E\vee(F\vee G)$.

**Chứng minh ($\wedge$).** $(E\cap F)\cap G=E\cap(F\cap G)$.

**Chứng minh ($\vee$).** Trước hết $(E\vee F)^*=E^*\wedge F^*$: áp $(\cdot)^*$ lên L.C, $(E\vee F)^*=\bigl((E^*\wedge F^*)^*\bigr)^*=(E^*\wedge F^*)^{**}\overset{\text{L.D}}{=}E^*\wedge F^*$ (vì $E^*,F^*\in\mathbb X$, L.D áp được). Vậy
$$(E\vee F)\vee G\overset{\text{L.C}}{=}\bigl((E\vee F)^*\wedge G^*\bigr)^*=\bigl((E^*\wedge F^*)\wedge G^*\bigr)^*=(E^*\wedge F^*\wedge G^*)^*$$
(dùng kết hợp tính của $\wedge$ vừa chứng minh). Tương tự $E\vee(F\vee G)=(E^*\wedge F^*\wedge G^*)^*$. Hai vế trùng nhau. $\blacksquare$

**Remark (tầng dưới).** Kết hợp tính nguyên thủy của $\cap$ (dùng ở cả phần $\wedge$ và bên trong phần $\vee$).

*(Kết hợp tính của $\triangle,\bigtriangledown$ là **M1, M3** — xem mục riêng bên dưới.)*

---

## T4 — Hấp thụ (absorption)

**Phát biểu.** $E\wedge(E\vee F)=E$, $\ E\vee(E\wedge F)=E$.

**Chứng minh phần 1.** $E\subseteq E\cup F\subseteq(E\cup F)^{**}=E\vee F$ (bao hàm thứ hai là P1 áp cho $E\cup F$). Vì $E\subseteq E\vee F$: $E\wedge(E\vee F)=E\cap(E\vee F)=E$.

**Chứng minh phần 2.** $E\wedge F\subseteq E$ (trực tiếp). Theo T0, $E\vee(E\wedge F)\subseteq E\vee E\overset{\text{T1}}{=}E$. Mặt khác $E\subseteq E\cup(E\wedge F)\subseteq\bigl(E\cup(E\wedge F)\bigr)^{**}=E\vee(E\wedge F)$ (lại P1). Kết hợp hai chiều: $E\vee(E\wedge F)=E$. $\blacksquare$

**Remark (tầng dưới).** Cả hai phần dùng **P1** (mở rộng của polar) trực tiếp — đây là thành phần bên trong chứng minh L.A, không phải bản thân L.A (L.A chỉ phát biểu $E^{***}=E^*$, không phải $E\subseteq E^{**}$ trực tiếp). Cũng dùng T0 (đã tự mang remark riêng).

---

## T5 — Tương thích thứ tự với $\wedge,\vee$

**Phát biểu.** Với $E,F\in\mathbb X$: $\ E\subseteq F\iff E\wedge F=E\iff E\vee F=F$.

**Chứng minh ($E\subseteq F\Rightarrow E\wedge F=E$).** $E\subseteq F\Rightarrow E\cap F=E$ (elementary).

**Chứng minh ($E\wedge F=E\Rightarrow E\subseteq F$).** $E=E\cap F\subseteq F$ (elementary).

**Chứng minh ($E\subseteq F\Rightarrow E\vee F=F$).** Từ T4 phần 1 áp cho cặp $(F,E)$: $F\wedge(F\vee E)=F$ luôn đúng, không cần $E\subseteq F$. Cần chiều khác: nếu $E\subseteq F$, $E\vee F\overset{\text{T4 dạng khác}}{=}$... trực tiếp hơn: $F\subseteq E\vee F$ (từ P1 áp cho $E\cup F$, như T4). Và $E\vee F\subseteq F\vee F=F$ nhờ T0 (đơn điệu, dùng $E\subseteq F$) và T1. Kết hợp: $E\vee F=F$.

**Chứng minh ($E\vee F=F\Rightarrow E\subseteq F$).** $E\subseteq E\cup F\subseteq(E\cup F)^{**}=E\vee F=F$ (dùng P1 lần nữa). $\blacksquare$

**Remark (tầng dưới).** Toàn bộ phần liên quan $\vee$ dùng lại P1 (như T4) và T0; phần $\wedge$ hoàn toàn sơ cấp (không cần API lemma).

---

## T6 — Polar là song ánh nghịch đảo thứ tự trên $\mathbb X$

**Phát biểu.** $(\cdot)^*:\mathbb X\to\mathbb X$ là song ánh, phản biến, và $(E^*)^*=E$.

**Chứng minh.** Toàn ánh + đơn ánh: với $E\in\mathbb X$, $E^*\in\mathbb X$ (hệ quả L.A) và $(E^*)^*=E^{**}=E$ (định nghĩa $\mathbb X$), nên $(\cdot)^*$ là nghịch đảo của chính nó trên $\mathbb X$ — một đối hợp, do đó song ánh. Tính đơn ánh cũng chính là **L.E**. Tính phản biến: cần với mọi $A,B\in\mathbb X$, $A\subseteq B\Rightarrow B^*\subseteq A^*$. $\blacksquare$

**Remark (tầng dưới).** Tính phản biến dùng trực tiếp **P2**, không phải một API lemma riêng (nó là nguyên liệu bên trong L.A, chưa được phát biểu độc lập trong danh sách API).

---

## T7 (= D1) — Fibor phân phối qua Meet

**Phát biểu.** Với mọi $E,F,G\in\mathbb X$: $\ E\triangle(F\wedge G)=(E\triangle F)\wedge(E\triangle G)$.

**Chứng minh.** Viết $E,F,G$ qua hàm $e,f,g$. Với mỗi $x$: dùng **L.MP** (max-plus) để có $e(x)+\max(f(x),g(x))=\max(e(x)+f(x),e(x)+g(x))$, suy ra đẳng thức tập hợp $E+_{\rm fib}(F\wedge G)=(E+_{\rm fib}F)\cap(E+_{\rm fib}G)$. Đặt $A:=E+_{\rm fib}F,B:=E+_{\rm fib}G$; theo **L.I**, $A,B\in\mathbb X$. Áp **L.D**:
$$E\triangle(F\wedge G)=(A\cap B)^{**}\overset{\text{L.D}}{=}A\cap B=A^{**}\cap B^{**}=(E\triangle F)\wedge(E\triangle G).\qquad\blacksquare$$

**Remark (tầng dưới).** Bước đầu (dịch qua max-plus theo từng thớ) làm việc trực tiếp với biểu diễn hàm $e,f,g$ và thớ nguyên thủy, chưa thuần túy ở tầng $\wedge,\triangle$ trừu tượng. **L.I** được dùng nguyên vẹn như một API lemma, nhưng nhắc lại: thành phần $\mathcal F,C,T$ của L.I tự nó có điều kiện "proper" (xem file API lemmas) — điều kiện đó thấm xuống T7.

---

## T8 (= D2) — Spator phân phối qua Join

**Phát biểu.** Với mọi $E,F,G\in\mathbb X$: $\ E\bigtriangledown(F\vee G)=(E\bigtriangledown F)\vee(E\bigtriangledown G)$.

**Chứng minh.** Đặt $e:=E^*,f:=F^*,g:=G^*\in\mathbb X$ (L.A). Theo L.C: $(F\vee G)^*=(f\wedge g)^{**}\overset{\text{L.D}}{=}f\wedge g$. Theo **P.U**:
$$E\bigtriangledown(F\vee G)=\bigl(e\triangle(f\wedge g)\bigr)^*\overset{\text{T7}}{=}\bigl((e\triangle f)\wedge(e\triangle g)\bigr)^*.$$
Mặt khác $(E\bigtriangledown F)^*=e\triangle f$, $(E\bigtriangledown G)^*=e\triangle g$ (P.U, đã closed), nên theo L.C:
$$(E\bigtriangledown F)\vee(E\bigtriangledown G)=\bigl((e\triangle f)\wedge(e\triangle g)\bigr)^*.$$
Hai vế trùng nhau. $\blacksquare$

**Remark.** Hoàn toàn trong tầng API lemma (L.A, L.C, L.D, P.U, T7) — không cần đi xuống tầng dưới, ngoại trừ kế thừa điều kiện "proper" ẩn trong T7 (qua L.I).

---

## T9 (= D3) — Fibor KHÔNG phân phối qua Join

**Phát biểu.** $(E\triangle F)\vee(E\triangle G)\subseteq E\triangle(F\vee G)$, chặt nói chung.

**Chứng minh $\subseteq$.** $F,G\subseteq F\vee G$ (T4/T5) $\Rightarrow E\triangle F,E\triangle G\subseteq E\triangle(F\vee G)$ (T0). Vế phải đã đóng (ảnh $(\cdot)^{**}$), nên $(E\triangle F)\cup(E\triangle G)\subseteq E\triangle(F\vee G)\Rightarrow$ lấy $(\cdot)^{**}$ hai vế (đơn điệu, P4) và dùng vế phải bất động: $(E\triangle F)\vee(E\triangle G)\subseteq E\triangle(F\vee G)$.

**Phản ví dụ (đẳng thức thất bại).** $e(x)=|x-2|,f(x)=|x|,g(x)=|x-4|$: $e(2)+\bigl((f\vee g)\text{ tại }2\bigr)=0\neq2=\bigl((e\triangle f)\vee(e\triangle g)\text{ tại }2\bigr)$ (chi tiết tính toán: xem file trước). $\blacksquare$

**Remark (tầng dưới).** Chiều $\subseteq$ hoàn toàn trong tầng API (T0, T4/T5, P4). Nhưng **phản ví dụ bắt buộc phải đi xuống tầng hàm số cụ thể** $e,f,g$ (piecewise-linear, tính $\mathrm{conv}$, độ dốc) — không thể chỉ dùng $\wedge,\vee,\triangle,\bigtriangledown$ trừu tượng để chỉ ra một *thất bại*, vì phủ định một đẳng thức phổ quát đòi hỏi một mô hình cụ thể.

---

## T10 (= D4) — Spator KHÔNG phân phối qua Meet

**Phát biểu.** $E\bigtriangledown(F\wedge G)\subseteq(E\bigtriangledown F)\wedge(E\bigtriangledown G)$, chặt nói chung.

**Chứng minh.** Đối ngẫu hình thức của T9 qua L.C + P.U (đúng cơ chế T8 dùng để suy từ T7). $\blacksquare$

**Remark (tầng dưới).** Chiều bao hàm: thuần API. Phản ví dụ tường minh ($6\neq4$, cùng $e,f,g$): lại cần tầng hàm số cụ thể, như T9.

---

## T11 (= M1) — Kết hợp tính của Fibor

**Phát biểu.** Với mọi $E,F,G\in\mathbb X$: $\ (E\triangle F)\triangle G=E\triangle(F\triangle G)$.

**Chứng minh.** Đặt $A:=E+_{\rm fib}F$; theo **L.I**, $A\in\mathbb X$. Vậy
$$(E\triangle F)\triangle G=A^{**}\triangle G=A\triangle G=(A+_{\rm fib}G)^{**}=\bigl((E+_{\rm fib}F)+_{\rm fib}G\bigr)^{**}\overset{\text{L.H}}{=}(E+_{\rm fib}F+_{\rm fib}G)^{**}.$$
Đặt $B:=F+_{\rm fib}G\in\mathbb X$ (L.I), tương tự $E\triangle(F\triangle G)=(E+_{\rm fib}F+_{\rm fib}G)^{**}$. Trùng nhau. $\blacksquare$

**Remark (tầng dưới).** Bước "$A^{**}\triangle G=A\triangle G$" dùng $A\triangle G:=(A+_{\rm fib}G)^{**}$, tức truy cập trực tiếp định nghĩa nguyên thủy của $\triangle$ qua $+_{\rm fib}$ (không thể tránh, vì $\triangle$ *được định nghĩa* bằng $+_{\rm fib}$). L.I mang theo điều kiện "proper" như đã nêu.

---

## T12 (= M2) — Đơn vị của Fibor

**Phát biểu.** Với mọi $E\in\mathbb X$: $\ E\triangle1_\triangle=1_\triangle\triangle E=E$.

**Chứng minh.** $(E+_{\rm fib}1_\triangle)_x=\{r+s:r\ge e(x),s\ge0\}=[e(x),+\infty]=E_x$ — đẳng thức tập hợp trực tiếp (đạt tại $r=e(x),s=0$). Vì $E$ đã closed: $E\triangle1_\triangle=(E+_{\rm fib}1_\triangle)^{**}=E^{**}=E$. T2 cho vế kia. $\blacksquare$

**Remark (tầng dưới).** Toàn bộ chứng minh làm việc trực tiếp trên thớ nguyên thủy của $+_{\rm fib}$ — không đi qua bất kỳ API lemma nào (đây là một tính toán primitive thuần túy, không phải hệ quả trừu tượng của $\triangle$).

---

## T13 (= M3) — Kết hợp tính và đơn vị của Spator

**Phát biểu.** Với mọi preepi $E,F,G$: $\ (E\bigtriangledown F)\bigtriangledown G=E\bigtriangledown(F\bigtriangledown G)$; với mọi $E\in\mathbb X$: $\ E\bigtriangledown1_\bigtriangledown=E$.

**Chứng minh (kết hợp).** $(E\bigtriangledown F)^*=E^*\triangle F^*$ (P.U, đã closed). Vậy
$$(E\bigtriangledown F)\bigtriangledown G\overset{\text{P.U}}{=}\bigl((E\bigtriangledown F)^*\triangle G^*\bigr)^*=\bigl((E^*\triangle F^*)\triangle G^*\bigr)^*\overset{\text{T11, vì }E^*,F^*,G^*\in\mathbb X}{=}\bigl(E^*\triangle(F^*\triangle G^*)\bigr)^*=E\bigtriangledown(F\bigtriangledown G).$$

**Chứng minh (đơn vị).** Theo L.UD, $1_\bigtriangledown^*=1_\triangle$. Với $E\in\mathbb X$:
$$E\bigtriangledown1_\bigtriangledown\overset{\text{P.U}}{=}(E^*\triangle1_\bigtriangledown^*)^*=(E^*\triangle1_\triangle)^*\overset{\text{T12}}{=}(E^*)^*=E^{**}=E.\qquad\blacksquare$$

**Remark.** Hoàn toàn trong tầng API (P.U, T11, T12, L.UD, L.A) — không cần đi xuống tầng dưới trực tiếp, chỉ kế thừa gián tiếp điều kiện "proper" của T11/L.I qua $E^*,F^*,G^*$.

---

## T14 — Hệ quả phân phối kèm đơn vị

**Phát biểu.** Với mọi $E,F\in\mathbb X$:
$$E\triangle(F\wedge1_\triangle)=(E\triangle F)\wedge E,\qquad E\bigtriangledown(F\vee1_\bigtriangledown)=(E\bigtriangledown F)\vee E.$$

**Chứng minh.** Áp T7 với $G:=1_\triangle$, dùng T12: $E\triangle(F\wedge1_\triangle)=(E\triangle F)\wedge(E\triangle1_\triangle)=(E\triangle F)\wedge E$. Áp T8 với $G:=1_\bigtriangledown$, dùng T13: $E\bigtriangledown(F\vee1_\bigtriangledown)=(E\bigtriangledown F)\vee(E\bigtriangledown1_\bigtriangledown)=(E\bigtriangledown F)\vee E$. $\blacksquare$

**Remark.** Hoàn toàn trong tầng API (T7,T8,T12,T13), không cần gì thêm.

---

## T15 (= N1) — Điều kiện dấu cho Fibor (đối xứng)

**Phát biểu.** Với $E,F\in\mathbb X$: $\ F\subseteq1_\triangle\Rightarrow E\triangle F\subseteq E$; $\ 1_\triangle\subseteq F\Rightarrow E\subseteq E\triangle F$.

**Chứng minh.** $F\subseteq1_\triangle$ nghĩa là $g\ge0$ khắp $X$ (hàm của $F$). Với mỗi $x$: $e(x)+g(x)\ge e(x)$ (kiểm trên $\overline{\mathbb R}$, quy ước Rockafellar). Vậy $e+g\ge e$ pointwise $\Rightarrow\mathrm{epi}(e+g)\subseteq\mathrm{epi}(e)$, tức $E\triangle F\subseteq E$ (dùng L.I để biết $E+_{\rm fib}F$ đã closed, bằng chính $\mathrm{epi}(e+g)$). Đối xứng cho chiều kia. $\blacksquare$

**Remark (tầng dưới).** Toàn bộ chứng minh làm việc trực tiếp trên biểu diễn hàm $e,g$ và trên $\overline{\mathbb R}$ — không phải hệ quả trừu tượng của $\wedge,\vee,\triangle$; đây là một mệnh đề "lai" giữa tầng đại số (phát biểu bằng $\subseteq,\triangle,1_\triangle$) và tầng hàm số (chứng minh cần giá trị $e(x),g(x)$ cụ thể).

---

## T16 (= N2) — Điều kiện dấu cho Spator (bất đối xứng)

**Phát biểu.** Với $E,F\in\mathbb X$: $\ g(0)\le0\Rightarrow E\subseteq E\bigtriangledown F$; $\ F\subseteq1_\bigtriangledown\Rightarrow E\bigtriangledown F\subseteq E$.

**Chứng minh.** $(e\,\square\,g)(x)=\inf_y[e(y)+g(x-y)]\le e(x)+g(0)\le e(x)$ (lấy $y=x$). Toán tử $\mathrm{cl}(\cdot)$ đơn điệu và $\mathrm{cl}(h)\le h$, nên $\mathrm{cl}(e\,\square\,g)\le e$, tức $E\subseteq E\bigtriangledown F$. Chiều kia: $g\ge\delta_{\{0\}}\Rightarrow e\,\square\,g\ge e\,\square\,\delta_{\{0\}}=e$ (đơn điệu của inf-convolution + luật đơn vị $\delta_{\{0\}}$), áp $\mathrm{cl}$ đơn điệu: $\mathrm{cl}(e\,\square\,g)\ge e$, tức $E\bigtriangledown F\subseteq E$. $\blacksquare$

**Remark (tầng dưới).** Cùng loại T15 — chứng minh hoàn toàn ở tầng hàm số ($\inf$-convolution cụ thể trên $\overline{\mathbb R}^X$), không thuần túy $\wedge,\vee,\triangle,\bigtriangledown$ trừu tượng.

---

## Bảng tổng hợp

| Theorem | Phát biểu (rút gọn) | Trạng thái | Primitive dùng (nếu có) |
|---|---|---|---|
| T0 | đơn điệu $\triangle,\bigtriangledown$ | ⚠️ cần tầng dưới | $+_{\rm fib},+_{\rm sp}$ nguyên thủy; P4 |
| T1 | idempotent $\wedge,\vee$ | ⚠️ cần tầng dưới | idempotent nguyên thủy của $\cap$ |
| T2 | giao hoán $\wedge,\vee,\triangle,\bigtriangledown$ | ⚠️ một phần (chỉ $\wedge$) | giao hoán nguyên thủy của $\cap$; $\triangle,\bigtriangledown$ sạch (L.G) |
| T3 | kết hợp $\wedge,\vee$ | ⚠️ cần tầng dưới | kết hợp nguyên thủy của $\cap$ |
| T4 | hấp thụ | ⚠️ cần tầng dưới | P1 (mở rộng của polar) |
| T5 | tương thích thứ tự $\wedge,\vee$ | ⚠️ một phần | P1 (cho phần $\vee$); phần $\wedge$ sạch |
| T6 | polar là đối hợp phản biến trên $\mathbb X$ | ⚠️ cần tầng dưới | P2 (phản biến) |
| T7 (D1) | $\triangle$ qua $\wedge$ | ✅ API-tier (kế thừa L.I) | dịch qua hàm số ở bước đầu; L.I có điều kiện "proper" |
| T8 (D2) | $\bigtriangledown$ qua $\vee$ | ✅ Hoàn toàn API-tier | không, chỉ kế thừa gián tiếp từ T7 |
| T9 (D3) | $\triangle$ qua $\vee$ thất bại | ⚠️ một phần (phản ví dụ) | hàm số cụ thể $e,f,g$ (PL) |
| T10 (D4) | $\bigtriangledown$ qua $\wedge$ thất bại | ⚠️ một phần (phản ví dụ) | hàm số cụ thể $e,f,g$ (PL) |
| T11 (M1) | kết hợp $\triangle$ | ✅ API-tier | truy cập định nghĩa $\triangle$ qua $+_{\rm fib}$; L.I có điều kiện "proper" |
| T12 (M2) | đơn vị $\triangle$ | ⚠️ cần tầng dưới | tính toán trực tiếp trên $+_{\rm fib}$ |
| T13 (M3) | kết hợp $+$ đơn vị $\bigtriangledown$ | ✅ Hoàn toàn API-tier | không, chỉ kế thừa gián tiếp từ T11/T12 |
| T14 | hệ quả phân phối-đơn vị | ✅ Hoàn toàn API-tier | không |
| T15 (N1) | dấu cho $\triangle$ | ⚠️ cần tầng dưới | hàm số $e,g$ trên $\overline{\mathbb R}$ |
| T16 (N2) | dấu cho $\bigtriangledown$ | ⚠️ cần tầng dưới | inf-convolution trên hàm số |

**Quan sát tổng thể.** Bốn định lý cốt lõi cho MALL — **T7 (D1), T8 (D2), T11 (M1), T13 (M3)** — đạt trạng thái tốt nhất có thể trong khuôn khổ hiện tại: T8, T13, T14 **hoàn toàn API-tier** (không cần đi xuống); T7, T11 cần một bước dịch qua hàm số/nguyên thủy nhưng chỉ **một lần**, sau đó mọi hệ quả (T8, T13, T14) suy ra thuần túy bằng đối ngẫu polar mà **không cần lặp lại** bước đó — đúng đặc tính "kiến trúc Grothendieck" đã nêu: chi phí tầng dưới trả đúng một lần ở nguồn (T7, T11, và ẩn trong đó là điều kiện "proper" của L.I), còn lại lan tỏa miễn phí qua các định lý đối ngẫu. Các định lý còn "⚠️" khác (T0–T6, T12, T15, T16) là các sự kiện nền/phụ trợ, cũng chỉ cần tầng dưới đúng một lần mỗi định lý, không có định lý nào cần lặp lại nhiều bước nguyên thủy.
