# Sáu khối tiên đề cho MALL trên preepi: Bảng đối chiếu và Bổ đề

## Section 1 — Bảng sáu khối: tiên đề và bổ đề tương ứng

Ký hiệu bổ đề dùng chữ viết tắt **(L.x)** cho lemma thuần túy, và **D1–D4, M1–M3** cho các mệnh đề trung gian (đã được chứng minh từ các L.x, giữ lại để tham chiếu nhanh khi một tiên đề dùng lại nguyên một khối chứng minh đã có).

| Khối | Tiên đề | Bổ đề / Mệnh đề dùng để chứng minh |
|---|---|---|
| **1. Join & Meet** $(\wedge,\vee)$ | (1a) $\wedge,\vee$ idempotent, giao hoán, kết hợp | **(L.J)** — trực tiếp từ $\cap,\cup$ ở Level 1 cho $\wedge$; cho $\vee$ cần **(L.D)** để đóng dưới $(\cdot)^{**}$ |
| | (1b) hấp thụ: $E\wedge(E\vee F)=E$, $E\vee(E\wedge F)=E$ | **(L.D)** + tính mở rộng $E\subseteq E^{**}$ (trong **(L.A)**) |
| | (1c) tương thích thứ tự: $E\subseteq F\iff E\wedge F=E\iff E\vee F=F$ | định nghĩa trực tiếp cho $\wedge$; **(L.C)** cho $\vee$ |
| **2. Fibor & Spator** $(\triangle,\bigtriangledown)$ | (2a) $\triangle$ kết hợp | **(L.H)** + **(L.I)** $\Rightarrow$ **M1** |
| | (2b) $\triangle$ có đơn vị $1_\triangle$ | tính trực tiếp $E+_{\rm fib}1_\triangle=E$ $\Rightarrow$ **M2** |
| | (2c) $\bigtriangledown$ kết hợp | **(L.F)** + **(L.A)** $\Rightarrow$ **P.U**, rồi **M1** (qua polar) $\Rightarrow$ **M3** |
| | (2d) $\bigtriangledown$ có đơn vị $1_{\bigtriangledown}$ | **(L.UD)** + **P.U** + **M2** $\Rightarrow$ **M3** |
| | (2e) $\triangle,\bigtriangledown$ giao hoán | **(L.G)** |
| **3. Polar** $(\cdot)^*$ | (3a) $E^{**}=E$ với $E\in\mathbb X$ ("fact"/bipolar theorem) | **(L.A)** + định nghĩa $\mathbb X=$ điểm bất động của $(\cdot)^{**}$ |
| | (3b) $(\cdot)^*$ phản biến (order-reversing) | **(L.A)**, bước đầu của chứng minh |
| | (3c) $E^*\in\mathbb X$ với mọi preepi $E$ | hệ quả trực tiếp **(L.A)** |
| **4. Polar ↔ Join/Meet** (De Morgan lattice) | (4a) $(E\cup F)^*=E^*\cap F^*$ | **(L.B)** |
| | (4b) $E\vee F=(E^*\wedge F^*)^*$ | **(L.C)** $=$ (L.B) $+$ (L.A) |
| | (4c) đơn vị đối ngẫu $1_\wedge^*=1_\vee$ | **(L.UD)**, phần 1 |
| **5. Polar ↔ Fibor/Spator** (De Morgan monoid, tensor–par duality) | (5a) $(E+_{\rm sp}F)^*=E^*+_{\rm fib}F^*$ | **(L.F)** |
| | (5b) $E\bigtriangledown F=(E^*\triangle F^*)^*$ | **P.U** $=$ (L.F) $+$ (L.A) |
| | (5c) đơn vị đối ngẫu $1_\triangle^*=1_{\bigtriangledown}$ | **(L.UD)**, phần 2 |
| **6. Fibor/Spator ↔ Join/Meet** (bốn luật phân phối MALL) | (6a) $\triangle$ phân phối qua $\wedge$ | **(L.MP)** + **(L.I)** + **(L.D)** $\Rightarrow$ **D1** |
| | (6b) $\bigtriangledown$ phân phối qua $\vee$ | **(L.C)** + **P.U** + **D1** $\Rightarrow$ **D2** |
| | (6c) $\triangle$ **không** phân phối qua $\vee$ (chỉ $\subseteq$) | đơn điệu (từ định nghĩa) + phản ví dụ tường minh $\Rightarrow$ **D3** |
| | (6d) $\bigtriangledown$ **không** phân phối qua $\wedge$ (chỉ $\subseteq$) | đối ngẫu của D3 qua **(L.C)** + **P.U** $\Rightarrow$ **D4** |

**Quy ước tham chiếu:** L.A–L.MP là các bổ đề nguyên thủy (Section 2). P.U là "Mệnh đề hợp nhất" (Spator = đối ngẫu bipolar của Fibor), đứng giữa lemma và theorem — dùng lại nhiều lần nên được đặt tên riêng. M1–M3, D1–D4 là các định lý cấp cao hơn, đã có chứng minh đầy đủ trong file trước (`dai_so_fibor_spator_full.md`); ở đây chỉ liệt kê như điểm tham chiếu, không lặp lại chứng minh.

---

## Section 2 — Phát biểu các bổ đề

### (L.A) — Tam polar bất động

Với mọi preepi $E$: $\ E^{***}=E^*$.

Hệ quả: $E^*\in\mathbb X$ luôn đúng, với mọi preepi $E$, không cần $E\in\mathbb X$; và $(\cdot)^*$ phản biến ($A\subseteq B\Rightarrow B^*\subseteq A^*$).

### (L.B) — Polar của hợp

Với mọi preepi $E,F$: $\ (E\cup F)^* = E^*\cap F^*$.

### (L.C) — Join là đối ngẫu bipolar của meet

Với mọi preepi $E,F$: $\ E\vee F = (E^*\wedge F^*)^*$.

*(Hệ quả trực tiếp của (L.A) $+$ (L.B), không cần giả thiết thêm.)*

### (L.D) — Đóng dưới giao của điểm bất động

Nếu $A^{**}=A$ và $B^{**}=B$ thì $(A\cap B)^{**}=A\cap B$.

### (L.E) — Đơn ánh của polar trên $\mathbb X$

Nếu $A,B\in\mathbb X$ và $A^*=B^*$ thì $A=B$.

### (L.F) — Polar của spatial sum

Với mọi preepi $E,F$: $\ (E+_{\rm sp}F)^* = E^*+_{\rm fib}F^*$.

### (L.G) — Giao hoán

Với mọi preepi $E,F$: $\ E+_{\rm fib}F=F+_{\rm fib}E$ và $E+_{\rm sp}F=F+_{\rm sp}E$; suy ra $E\triangle F=F\triangle E$ và $E\bigtriangledown F=F\bigtriangledown E$.

### (L.H) — Kết hợp của phép cộng mở rộng

Với quy ước Rockafellar $(+\infty)+(-\infty):=+\infty$: với mọi $r,s,t\in\overline{\mathbb R}$,
$$(r+s)+t = r+(s+t).$$

### (L.I) — Fiber sum của hai regepi tự động là regepi

Nếu $A,B\in\mathbb X$ thì $A+_{\rm fib}B\in\mathbb X$, tức $(A+_{\rm fib}B)^{**}=A+_{\rm fib}B$ không cần đóng thêm.

### (L.MP) — Bổ đề max-plus

Với mọi $t,a,b\in\overline{\mathbb R}$ (quy ước Rockafellar): $\ t+\max(a,b)=\max(t+a,\,t+b)$.

### (L.UD) — Đơn vị đối ngẫu

Phần 1: $\ 1_\wedge^* = 1_\vee$, với $1_\wedge:=X\times\overline{\mathbb R}$, $1_\vee:=X\times\{+\infty\}$.

Phần 2: $\ 1_\triangle^* = 1_{\bigtriangledown}$, với $1_\triangle:=X\times[0,+\infty]$, $1_{\bigtriangledown}:=(\{0\}\times[0,+\infty])\cup((X\setminus\{0\})\times\{+\infty\})$.

*(Cả hai đều kiểm bằng tính trực tiếp từ định nghĩa polar; phần 2 kéo theo $1_{\bigtriangledown}^*=1_\triangle$ nhờ (L.A) áp cho $1_\triangle\in\mathbb X$.)*

---

## Mệnh đề trung gian (không phải lemma nguyên thủy, nhưng dùng lặp lại)

### (P.U) — Mệnh đề hợp nhất

Với mọi preepi $E,F$: $\ E\bigtriangledown F = (E^*\triangle F^*)^*$.

*Chứng minh.* Từ (L.F): $(E+_{\rm sp}F)^*=E^*+_{\rm fib}F^*$. Vậy
$$E\bigtriangledown F=(E+_{\rm sp}F)^{**}=\bigl((E+_{\rm sp}F)^*\bigr)^*=(E^*+_{\rm fib}F^*)^*\overset{\text{(L.A)}}{=}\bigl((E^*+_{\rm fib}F^*)^{**}\bigr)^*=(E^*\triangle F^*)^*.\qquad\blacksquare$$

Hệ quả: $\{\wedge,\vee,\triangle,\bigtriangledown\}$ chỉ có hai bậc tự do ở Level 1 ($\cap$ hay $\cup$; $+_{\rm fib}$ hay $+_{\rm sp}$) — $\vee$ và $\bigtriangledown$ đều là đối ngẫu bipolar tự động của $\wedge,\triangle$ tương ứng, không phải định nghĩa độc lập.
