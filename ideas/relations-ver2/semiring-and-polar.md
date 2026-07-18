# Idempotent Commutative Semiring với Polar
### Đối hợp, phản-đẳng-cấu thứ tự, và điều kiện tương thích

---

# 1. Giới thiệu

Tài liệu này dựng một khung đại số trừu tượng — **idempotent commutative semiring $(X,\wedge,+)$ trang bị một polar $(-)^*$** (đối hợp kiểu Fenchel, *không phải* sao Kleene) — và chứng minh một chuỗi kết quả độc lập với mô hình cụ thể nào:

1. Polar tự động là một **song ánh**.
2. Tính lũy đẳng của $\wedge$ tự động sinh ra một **thứ tự bộ phận** $\le$.
3. Polar **tự động** biến hai phép toán nguyên thủy $\wedge,+$ thành hai phép toán dẫn xuất $\vee,\times$ cũng tạo thành một idempotent commutative semiring — không cần chứng minh lại từng tiên đề, mà suy ra qua một **đẳng cấu đại số**.
4. Polar **tự động** là một phản-đẳng-cấu giữa hai thứ tự $\le$ và $\le^*$ (sinh bởi $\wedge$ và $\vee$ tương ứng) — kết quả này *miễn phí*, không cần thêm giả thiết.
5. Để polar trở thành phản biến **trên một thứ tự duy nhất** (tức $\le=\le^*$), cần một điều kiện **thêm, không tự động**: **tính tương thích**, tương đương với luật hấp thụ cổ điển của lattice. Ta chứng minh ba cách phát biểu của điều kiện này là tương đương, và đưa phản ví dụ cho thấy nó không tự động đúng.
6. Độc lập hoàn toàn với polar: hai phép toán nguyên thủy $\wedge,+$ luôn **đơn điệu** theo thứ tự $\le$ mà chính chúng sinh ra.

Mục tiêu là tách bạch rõ ràng: kết quả nào **miễn phí** (hệ quả cơ học của tiên đề), kết quả nào **cần trả giá** (đòi hỏi giả thiết bổ sung thật sự).

---

# 2. Định nghĩa và Bảng kết quả chính

## 2.1 Bộ ký hiệu chuẩn

| Ký hiệu | Ý nghĩa |
|---|---|
| $X$ | tập nền |
| $\wedge$ | phép toán nguyên thủy thứ nhất (meet), đơn vị $e_\wedge$ |
| $+$ | phép toán nguyên thủy thứ hai, đơn vị $e_+$ |
| $(-)^*$ | polar, ánh xạ $X\to X$ |
| $\vee := \wedge^*$ | phép **dẫn xuất**: $a\vee b:=(a^*\wedge b^*)^*$, đơn vị $e_\vee:=e_\wedge^*$ |
| $\times := +^*$ | phép **dẫn xuất**: $a\times b:=(a^*+ b^*)^*$, đơn vị $e_\times:=e_+^*$ |
| $\le$ | $a\le b:\iff a\wedge b=a$ |
| $\le^*$ | $a\le^* b:\iff a\vee b=b$ |

## 2.2 Tiên đề gốc

Bộ $(X,\wedge,+,e_\wedge,e_+)$ là **idempotent commutative semiring** nếu:

$$\textbf{(S1)}\ (X,\wedge,e_\wedge)\text{ là CM monoid, lũy đẳng: } a\wedge a=a\ \ \forall a$$
$$\textbf{(S2)}\ (X,+,e_+)\text{ là CM monoid}$$
$$\textbf{(S3)}\ a+(b\wedge c)=(a+b)\wedge(a+c)\ \ \forall a,b,c\ \text{(phân phối)}$$

Một **polar** trên $X$ là ánh xạ $(-)^*:X\to X$ thỏa duy nhất:

$$\textbf{(P1)}\ a^{**}=a\ \ \forall a\in X.$$

## 2.3 Bảng các kết quả chính

| # | Tên | Phát biểu ngắn gọn | Giả thiết cần |
|---|---|---|---|
| L1 | Polar là song ánh | $(-)^*$ đơn ánh + toàn ánh, $\ast\circ\ast=\mathrm{id}_X$ | chỉ (P1) |
| L2 | Lũy đẳng sinh thứ tự | $\le$ (từ $\wedge$) là thứ tự bộ phận | chỉ (S1) |
| T1 | Semiring dẫn xuất | $(X,\vee,\times,e_\vee,e_\times)$ là idem-com-semiring; $(-)^*$ là đẳng cấu đại số | (P1)+(S1)+(S2)+(S3) |
| T2 | Cross-antitone (miễn phí) | $a\le b \iff b^*\le^* a^*$ | (P1)+(S1) |
| T3 | Ba mệnh đề tương thích tương đương | $(a\wedge b{=}a\iff a\vee b{=}b)\iff(\le{=}\le^*)\iff(\text{Abs1},\text{Abs2})$ | T1 + Bổ đề A, B |
| H1 | Phản biến thật (có tương thích) | $a\le b\iff b^*\le a^*$ (cùng một $\le$) | T2 + T3 |
| CE | Phản ví dụ | Tồn tại mô hình thỏa (S1)-(S3)+(P1) nhưng vi phạm T3 | — |
| TA | Đơn điệu của $\wedge$ | $a\le b\Rightarrow a\wedge c\le b\wedge c$ | chỉ (S1) |
| TB | Đơn điệu của $+$ | $a\le b\Rightarrow a+c\le b+c$ | (S1)+(S3) |

**Hai nhánh độc lập:** {TA, TB} không liên quan đến polar; {L1, T1, T2, T3, H1} không cần tính đơn điệu; chúng chỉ dùng chung tiên đề nền (S1)–(S3).

---

# 3. Phát biểu chi tiết và chứng minh

## 3.1 Bổ đề L1 — Polar là song ánh

**Phát biểu.** Nếu $(-)^*$ thỏa (P1) thì $(-)^*:X\to X$ là song ánh và $\ast\circ\ast=\mathrm{id}_X$.

**Chứng minh.**

*Đơn ánh:* $a^*=b^*\ \Rightarrow\ (a^*)^*=(b^*)^*\ \overset{\text{(P1)}}{\Rightarrow}\ a=b$.

*Toàn ánh:* với $b\in X$ tùy ý, đặt $a:=b^*$. Khi đó $a^*=(b^*)^*\overset{\text{(P1)}}{=}b$.

Vậy $*$ vừa đơn ánh vừa toàn ánh $\Rightarrow$ song ánh. $\blacksquare$

---

## 3.2 Bổ đề L2 — Lũy đẳng sinh ra thứ tự bộ phận

**Phát biểu.** $a\le b:\iff a\wedge b=a$ là thứ tự bộ phận trên $X$ (phản xạ, phản đối xứng, bắc cầu), với $e_\wedge$ là phần tử lớn nhất.

**Chứng minh.**

- *Phản xạ:* $a\wedge a=a$ (tiên đề S1) $\Rightarrow a\le a$.
- *Phản đối xứng:* $a\le b,\ b\le a \Rightarrow a\wedge b=a,\ b\wedge a=b$. Vì $\wedge$ giao hoán, $a\wedge b=b\wedge a\Rightarrow a=b$.
- *Bắc cầu:* $a\le b,\ b\le c \Rightarrow a\wedge b=a,\ b\wedge c=b$. Khi đó
$$a\wedge c=(a\wedge b)\wedge c=a\wedge(b\wedge c)=a\wedge b=a\ \Rightarrow\ a\le c.$$
- *$e_\wedge$ lớn nhất:* $a\wedge e_\wedge=a\ \forall a\ \Rightarrow\ a\le e_\wedge\ \forall a$. $\blacksquare$

*(Áp dụng lại bổ đề này cho $(X,\vee)$ sau khi có T1, ta được $\le^*$ cũng là thứ tự bộ phận, với $e_\vee$ lớn nhất.)*

---

## 3.3 Định lý T1 — Polar sinh ra một idempotent commutative semiring thứ hai

**Bổ đề chốt (De Morgan trừu tượng).**
$$(a\vee b)^*=a^*\wedge b^*,\qquad (a\times b)^*=a^*+b^*.$$

*Chứng minh:* $(a\vee b)^*=\big((a^*\wedge b^*)^*\big)^*\overset{\text{(P1)}}{=}a^*\wedge b^*$. Tương tự cho $\times$. $\blacksquare$

**Định lý.** $(X,\vee,\times,e_\vee,e_\times)$ là idempotent commutative semiring, và $(-)^*:(X,\wedge,+,e_\wedge,e_+)\to(X,\vee,\times,e_\vee,e_\times)$ là một đẳng cấu đại số.

**Chứng minh.**

- *Kết hợp của $\vee$:* $(a\vee b)\vee c\overset{\text{đ/n}}{=}\big((a\vee b)^*\wedge c^*\big)^*\overset{\text{(L)}}{=}\big((a^*\wedge b^*)\wedge c^*\big)^*\overset{\wedge\text{ kết hợp}}{=}\big(a^*\wedge(b^*\wedge c^*)\big)^*\overset{\text{(L) ngược}}{=}a\vee(b\vee c)$.
- *Giao hoán của $\vee$:* trực tiếp từ giao hoán của $\wedge$ trong định nghĩa $a\vee b:=(a^*\wedge b^*)^*$.
- *Đơn vị:* $a\vee e_\vee=(a^*\wedge e_\wedge^{**})^*\overset{\text{(P1)}}{=}(a^*\wedge e_\wedge)^*=(a^*)^*=a$.
- *Lũy đẳng:* $a\vee a=(a^*\wedge a^*)^*\overset{\text{S1 áp cho }a^*}{=}(a^*)^*=a$.
- *Kết hợp, giao hoán, đơn vị của $\times$:* hoàn toàn tương tự, dùng kết hợp/giao hoán/đơn vị của $+$.
- *Phân phối:* $a\times(b\vee c)\overset{\text{(L)}}{=}\big(a^*+(b\vee c)^*\big)^*\overset{\text{(L)}}{=}\big(a^*+(b^*\wedge c^*)\big)^*\overset{\text{(S3)}}{=}\big((a^*+b^*)\wedge(a^*+c^*)\big)^*\overset{\text{(L) ngược}}{=}(a\times b)\vee(a\times c)$.

$\blacksquare$

**Ý nghĩa:** mọi tiên đề đẳng thức phổ dụng trên $(X,\wedge,+)$ được "vận chuyển" qua song ánh $*$ mà không cần chứng minh riêng lẻ.

---

## 3.4 Định lý T2 — Polar là phản-đẳng-cấu giữa $(X,\le)$ và $(X,\le^*)$

**Phát biểu.**
$$a\le b \iff b^*\le^* a^*\qquad\forall a,b\in X.$$

**Chứng minh.**

($\Rightarrow$) $a\le b\Rightarrow a\wedge b=a$. Áp $*$ và dùng Bổ đề chốt (L) với $u:=a^*,v:=b^*$, cùng (P1):
$$(a^*\vee b^*)^*\overset{\text{(L)}}{=}a^{**}\wedge b^{**}\overset{\text{(P1)}}{=}a\wedge b=a.$$
Áp $*$ hai vế: $a^*\vee b^*=a^*$, tức (giao hoán) $b^*\vee a^*=a^*$, tức $b^*\le^*a^*$.

($\Leftarrow$) $b^*\le^*a^*\Rightarrow b^*\vee a^*=a^*$. Áp $*$, dùng (L) và (P1):
$$b^{**}\wedge a^{**}=a\ \Rightarrow\ b\wedge a=a\ \Rightarrow\ a\wedge b=a\ \Rightarrow\ a\le b.\qquad\blacksquare$$

*Nhận xét:* kết quả **miễn phí**, chỉ cần (P1)+(S1) (đủ để cả $\le,\le^*$ là thứ tự và (L) đúng).

---

## 3.5 Định lý T3 — Ba mệnh đề tương đương về tính tương thích

Ba phát biểu sau, với mọi $a,b\in X$:

$$\textbf{(1)}\quad a\wedge b=a \iff a\vee b=b$$
$$\textbf{(2)}\quad \le\ =\ \le^*\quad\text{(là cùng một quan hệ trên }X\text{)}$$
$$\textbf{(Abs)}\quad a\wedge(a\vee b)=a\ \ \text{và}\ \ a\vee(a\wedge b)=a$$

**Định lý.** $(1)\iff(2)\iff(\text{Abs})$.

### (1) $\iff$ (2): tầm thường

Theo định nghĩa, $\le=\{(a,b):a\wedge b=a\}$ và $\le^*=\{(a,b):a\vee b=b\}$. Hai tập con này bằng nhau $\iff$ điều kiện xác định chúng tương đương với mọi $(a,b)$ — đó chính xác là (1). $\blacksquare$

### Hai bổ đề miễn phí (không cần tương thích)

**Bổ đề A.** $(a\wedge b)\wedge a=a\wedge b$ (tức $a\wedge b\le a$).

*Chứng minh:* $(a\wedge b)\wedge a\overset{\text{kết hợp,giao hoán}}{=}a\wedge a\wedge b\overset{\text{(S1)}}{=}a\wedge b$. $\blacksquare$

**Bổ đề B.** $a\vee(a\vee b)=a\vee b$ (tức $a\le^*a\vee b$).

*Chứng minh:* $a\vee(a\vee b)\overset{\text{kết hợp}}{=}(a\vee a)\vee b\overset{\text{T1, lũy đẳng của }\vee}{=}a\vee b$. $\blacksquare$

### (Abs) $\Rightarrow$ (1)

Giả sử $a\wedge b=a$. Áp (Abs2) với $x:=b,y:=a$: $b\vee(b\wedge a)=b$. Vì $b\wedge a=a\wedge b=a$: $b\vee a=b\Rightarrow a\vee b=b$.

Ngược lại, giả sử $a\vee b=b$. Áp (Abs1): $a\wedge(a\vee b)=a$. Thay $a\vee b=b$: $a\wedge b=a$. $\blacksquare$

### (1) $\Rightarrow$ (Abs)

**Chứng minh (Abs1):** áp (1) với $x:=a,\ y:=a\vee b$:
$$a\wedge(a\vee b)=a \iff a\vee(a\vee b)=a\vee b.$$
Vế phải đúng theo **Bổ đề B**. Vậy vế trái đúng: $a\wedge(a\vee b)=a$.

**Chứng minh (Abs2):** áp (1) với $x:=a\wedge b,\ y:=a$:
$$(a\wedge b)\wedge a=a\wedge b \iff (a\wedge b)\vee a=a.$$
Vế trái đúng theo **Bổ đề A**. Vậy vế phải đúng: $(a\wedge b)\vee a=a\overset{\text{giao hoán}}{\Rightarrow}a\vee(a\wedge b)=a$. $\blacksquare$

Vậy $(1)\iff(2)\iff(\text{Abs})$, ba mệnh đề tương đương. $\blacksquare\blacksquare$

---

## 3.6 Hệ quả H1 — Phản biến thật khi có tương thích

**Phát biểu.** Nếu tính tương thích (T3) đúng, thì
$$a\le b \iff b^*\le a^*\qquad\text{(cùng một thứ tự }\le\text{)}.$$

**Chứng minh.** Từ T2: $a\le b\iff b^*\le^*a^*$. Từ T3(2): $\le^*=\le$, nên $b^*\le^*a^*\iff b^*\le a^*$. Kết hợp hai điều: $a\le b\iff b^*\le a^*$. $\blacksquare$

Vì $*$ song ánh tự nghịch đảo (L1), đây là một **order-anti-automorphism** đầy đủ của $(X,\le)$.

---

## 3.7 Phản ví dụ CE — Tương thích không tự động đúng

Xét $X=\{z,p,q,e_\wedge\}$ với:
$$\wedge:\quad e_\wedge\wedge x=x\ \ \forall x,\qquad z\wedge x=z\ \ \forall x,\qquad p\wedge p=p,\quad q\wedge q=q,\quad p\wedge q=z.$$

Đây là một meet-semilattice hợp lệ (kết hợp, giao hoán, lũy đẳng — kiểm trực tiếp trên bảng hữu hạn), với $e_\wedge$ là phần tử lớn nhất, $z$ là phần tử nhỏ nhất, $p,q$ không so sánh được.

Định nghĩa polar: $z^*=z,\ q^*=q,\ e_\wedge^*=p,\ p^*=e_\wedge$ — dễ kiểm involutive (P1).

Tính $\vee$ theo định nghĩa $a\vee b=(a^*\wedge b^*)^*$, ta được (tính trực tiếp):
$$e_\wedge\vee q=\big(e_\wedge^*\wedge q^*\big)^*=(p\wedge q)^*=z^*=z.$$

Kiểm (Abs1) với $a:=e_\wedge,\ b:=q$:
$$a\wedge(a\vee b)=e_\wedge\wedge z=z\ \neq\ e_\wedge=a.$$

**(Abs1) thất bại** $\Rightarrow$ theo T3, cả (1) và (2) cũng thất bại: $\le\ \neq\ \le^*$ trong mô hình này, dù mọi tiên đề (S1)+(P1) (và (S3) nếu bổ sung $+$ tương ứng) đều được thỏa mãn.

**Kết luận:** tính tương thích là một giả thiết **thật sự độc lập**, không suy ra từ (S1)+(P1) (hay cả (S1)-(S3)+(P1)).

---

## 3.8 Định lý TA, TB — Đơn điệu của $\wedge,+$ theo $\le$ (không cần polar)

Trong toàn bộ mục này, **không dùng đến polar, không dùng tương thích** — chỉ (S1)-(S3).

### Định lý TA — $\wedge$ đơn điệu (miễn phí, không cần phân phối)

$$a\le b\ \Rightarrow\ a\wedge c\le b\wedge c\qquad\forall c\in X.$$

**Chứng minh.** $a\le b\Rightarrow a\wedge b=a$. Tính:
$$(a\wedge c)\wedge(b\wedge c)\overset{\text{kết hợp,giao hoán}}{=}(a\wedge b)\wedge(c\wedge c)\overset{a\wedge b=a,\ \text{(S1)}}{=}a\wedge c.$$
Đẳng thức này chính là định nghĩa $a\wedge c\le b\wedge c$. $\blacksquare$

### Định lý TB — $+$ đơn điệu (cần phân phối)

$$a\le b\ \Rightarrow\ a+c\le b+c\qquad\forall c\in X.$$

**Chứng minh.** $a\le b\Rightarrow a\wedge b=a$. Áp (S3) với vai trò $x:=c,y:=a,z:=b$:
$$c+(a\wedge b)=(c+a)\wedge(c+b).$$
Vế trái $=c+a$ (vì $a\wedge b=a$). Vậy $c+a=(c+a)\wedge(c+b)\overset{\text{giao hoán}}{\Rightarrow}(a+c)\wedge(b+c)=a+c$, tức $a+c\le b+c$. $\blacksquare$

### Hệ quả — đơn điệu hai biến

$$a\le b,\ c\le d\ \Rightarrow\ a\wedge c\le b\wedge d,\qquad a+c\le b+d.$$

**Chứng minh.** $a\wedge c\overset{\text{TA},a\le b}{\le}b\wedge c\overset{\text{TA},c\le d}{\le}b\wedge d$, bắc cầu (L2) cho $a\wedge c\le b\wedge d$. Tương tự dùng TB cho $+$. $\blacksquare$

---

## Sơ đồ phụ thuộc tổng thể

$$\text{(S1)} \Rightarrow \le\text{ là thứ tự (L2)} \Rightarrow \wedge\text{ đơn điệu (TA)}$$
$$\text{(S1)+(S3)} \Rightarrow +\text{ đơn điệu (TB)}$$
$$\text{(P1)} \Rightarrow *\text{ song ánh (L1)}$$
$$\text{(P1)+(S1)+(S2)+(S3)} \Rightarrow \vee,\times\text{ là semiring thứ hai (T1)} \Rightarrow a\le b\iff b^*\le^*a^*\text{ (T2, miễn phí)}$$
$$\underbrace{(1)\iff\le{=}\le^*\iff\text{Abs}}_{\text{Tương thích (T3), giả thiết thêm}} \Rightarrow a\le b\iff b^*\le a^*\text{ (H1, phản biến thật)}$$

**Hai nhánh độc lập:** {TA, TB} không đụng đến polar; {L1, T1, T2, T3, H1} không cần đơn điệu — chúng chỉ giao nhau tại tiên đề nền chung (S1)–(S3).
