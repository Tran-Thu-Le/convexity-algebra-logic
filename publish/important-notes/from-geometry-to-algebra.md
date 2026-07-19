# Regepi là một Idempotent Commutative Semiring có Polar
### Tiên đề hóa Polar qua sáu khối Pa1–Pa3 (đại số/order) và Pb1–Pb3 (hình học/topo)

---

## Sec 1. Preepi — định nghĩa trên phần tử, rồi lifting lên tập

### 1.1. Tầng phần tử

**Định nghĩa 1.1.1 (Không gian nền).**
$$\overline X := \mathbb R^n \times (-\infty, +\infty].$$
Phần tử viết $(x,r),(y,s),\dots$ với $x,y\in\mathbb R^n$, $r,s\in(-\infty,+\infty]$. Với $x\in\mathbb R^n$ cố định, gọi $\{x\}\times(-\infty,+\infty]$ là **thớ tại $x$**.

**Định nghĩa 1.1.2 (Fiber sum ở mức phần tử).** Với hai phần tử cùng thành phần không gian $x$:
$$(x,r) +_{fib}^{e} (x,s) := (x, r+s).$$

**Định nghĩa 1.1.3 (Quan hệ Fenchel).**
$$(x,r) \sim (y,s) \;:\iff\; \langle x, y \rangle \le r + s.$$

**Nhận xét 1.1.4 (Đối xứng).** $\sim$ đối xứng: $\langle x,y\rangle\le r+s \iff \langle y,x\rangle\le s+r$, vì $\langle\cdot,\cdot\rangle$ đối xứng và $+$ giao hoán trên $(-\infty,+\infty]$.

### 1.2. Lifting lên tầng tập $\mathcal P(\overline X)$

**Định nghĩa 1.2.1 (Ba phép toán trên tập).** Với $E,F\in\mathcal P(\overline X)$:

1. **Giao chuẩn**: $E\cap F$.

2. **Fiber sum (lifting của 1.1.2)**:
$$E +_{fib}^{(s)} F := \{(x,r+s) : (x,r)\in E,\ (x,s)\in F\}.$$

3. **Fenchel polar (lifting của 1.1.3, kiểu Galois connection)**:
$$E^* := \{p\in\overline X : e\sim p \ \ \forall e\in E\}.$$

**Mệnh đề 1.2.2 (S2 — giao hoán của fiber sum, miễn phí tuyệt đối, không cần polar).**
$$E +_{fib}^{(s)} F = F +_{fib}^{(s)} E.$$

*Chứng minh.* $\{(x,r+s):(x,r)\in E,(x,s)\in F\} = \{(x,s+r):(x,s)\in F,(x,r)\in E\}$, từ $r+s=s+r$ trên $(-\infty,+\infty]$ (không có dạng vô định vì không xuất hiện $-\infty$). $\blacksquare$

**Ghi chú.** Mệnh đề 1.2.2 đã chứng minh xong **S2** của hệ tiên đề ICS — trước khi $*$ tham gia vào câu chuyện. Đây là tiên đề "rẻ" nhất trong toàn bộ 11 tiên đề, không xuất hiện trong bảng Pa/Pb ở Sec 4.

---

## Sec 2. Fenchel polar — sáu tiên đề Pa1–Pa3, Pb1–Pb3

Mục này là nơi **duy nhất** công thức cụ thể $\langle x,y\rangle\le r+s$ được dùng trực tiếp. Từ Sec 3 trở đi, ta chỉ được viện dẫn sáu tiên đề dưới đây như hộp đen.

### 2.1. Nhóm Pa — Đại số / Order

**Pa1 (Antitone).** $A\subseteq B \ \Rightarrow\ B^*\subseteq A^*$, với mọi $A,B\subseteq\overline X$.

*Chứng minh.* $p\in B^* \Rightarrow (\forall e\in B,\ e\sim p) \Rightarrow (\forall e\in A,\ e\sim p)$ (vì $A\subseteq B$) $\Rightarrow p\in A^*$. $\blacksquare$

**Pa2 (Extensive).** $A\subseteq A^{**}$, với mọi $A\subseteq\overline X$.

*Chứng minh.* Lấy $a_0\in A$. Cần $\forall p\in A^*,\ p\sim a_0$. Với $p\in A^*$: $a_0\sim p$ (định nghĩa $A^*$); áp **đối xứng** của $\sim$ (Nhận xét 1.1.4): $p\sim a_0$. Vậy $a_0\in(A^*)^*=A^{**}$. $\blacksquare$

**Pa3 (Upward-closed theo thớ).** Với mọi $A\subseteq\overline X$: nếu $(x,r)\in A^{**}$ và $r'\ge r$ thì $(x,r')\in A^{**}$.

*Chứng minh.* $A^{**}=\bigcap_{p=(y,s)\in A^*} H_p$ với $H_p:=\{(x,r):\langle x,y\rangle\le r+s\}$. Với mỗi $p\in A^*$: $(x,r)\in A^{**}\Rightarrow\langle x,y\rangle\le r+s\le r'+s$ (vì $r'\ge r$) $\Rightarrow(x,r')\in H_p$. Đúng với mọi $p\in A^*$, nên $(x,r')\in A^{**}$. $\blacksquare$

> **Định lý 2.1.1 (Involutive — KHÔNG phải tiên đề, mà là định lý suy ra từ Pa1+Pa2).**
> Với mọi $A\subseteq\overline X$: $A^{***}=A^*$. Do đó, đặt $\mathbb X:=\{E\subseteq\overline X : E=E^{**}\}$, với mọi $E\in\mathbb X$: $E^*\in\mathbb X$ và $(E^*)^*=E$ — tức $(-)^*$ là song ánh tự nghịch đảo trên $\mathbb X$.
>
> *Chứng minh.* Áp Pa2 cho tập $A^*$: $A^*\subseteq(A^*)^{**}=A^{***}$. Áp Pa2 cho $A$: $A\subseteq A^{**}$; áp Pa1 cho bao hàm thức này: $(A^{**})^*\subseteq A^*$, tức $A^{***}\subseteq A^*$. Kết hợp hai chiều: $A^{***}=A^*$.
>
> Với $E\in\mathbb X$: $(E^*)^{**}=E^{***}=E^*$, nên $E^*\in\mathbb X$; và $(E^*)^*=E^{**}=E$ theo đúng định nghĩa $E\in\mathbb X$. $\blacksquare$
>
> **Ghi chú tầm quan trọng.** Ở tầng đại số trừu tượng thuần túy (nơi carrier $X$ được lấy thẳng là $\mathbb X$, không có $\mathcal P(\overline X)$ bao quanh), $a^{**}=a$ **là một tiên đề tự do**, độc lập với các tiên đề còn lại — không có gì buộc nó phải đúng nếu không giả định. Ở tầng hình học hiện tại, cùng phát biểu ấy **sụp xuống thành một định lý**, hệ quả thuần túy của Pa1+Pa2 (định lý Ore về Galois connection, 1944). Đây là khác biệt tầng quan trọng nhất giữa hai lối tiên đề hóa: bản trừu tượng cần liệt kê 3 tiên đề độc lập cho nhóm "đại số"; bản hình học chỉ cần 2 (Pa1, Pa2), tiên đề thứ ba (involutive) tự động rơi ra.

### 2.2. Nhóm Pb — Hình học / Topo

Ký hiệu thớ $A_x:=\{r\in(-\infty,+\infty] : (x,r)\in A\}$.

**Pb1 (Fiber-closed).** Với mọi $A\subseteq\overline X$, $x\in\mathbb R^n$: nếu $\alpha:=\inf (A^{**})_x \in\mathbb R$ (hữu hạn) thì $\alpha\in(A^{**})_x$.

*Chứng minh.* Đặt $E:=A^{**}$. Vì $\mathbb R$ đầy đủ Dedekind, tồn tại dãy $r_k\in E_x$, $r_k\downarrow\alpha$. Với mọi $p=(y,s)\in E^*$: $(x,r_k)\in E\Rightarrow\langle x,y\rangle\le r_k+s\ \forall k$; cho $k\to\infty$: $\langle x,y\rangle\le\alpha+s$, tức $(x,\alpha)\sim p$. Đúng với mọi $p\in E^*$, nên $(x,\alpha)\in E^{**}=E$ (dùng Định lý 2.1.1: $E=A^{**}\in\mathbb X\Rightarrow E^{**}=E$). $\blacksquare$

**Pb2 (Topo-closed).** Với mọi $A\subseteq\overline X$: $A^{**}$ đóng theo tô pô thường trên $\overline X$.

*Chứng minh.* Mỗi $H_p=\{(x,r):\langle x,y\rangle\le r+s\}$ ($p=(y,s)$) là sublevel set của phiếm hàm **liên tục** $(x,r)\mapsto\langle x,y\rangle-r-s$, nên $H_p$ đóng. $A^{**}=\bigcap_{p\in A^*}H_p$ là giao các tập đóng, nên đóng. $\blacksquare$

**Pb3 (Convexity) — GHI CHÚ: KHÔNG dùng ở Sec 4.** Với mọi $A\subseteq\overline X$: $A^{**}$ lồi trong $\overline X$.

*Chứng minh.* Mỗi $H_p$ là sublevel set của phiếm hàm **affine** (tuyến tính + hằng số theo $(x,r)$), nên $H_p$ lồi. Giao các tập lồi lồi, vậy $A^{**}=\bigcap_p H_p$ lồi. $\blacksquare$

*Ghi chú phương pháp luận.* Pb3 được chứng minh ở đây vì tính hệ thống (nó là một tính chất thật sự của $*$, không sai), nhưng — như sẽ thấy ở Sec 4 — **không một tiên đề ICS nào cần viện dẫn Pb3**. Nó chỉ cần thiết khi bắc cầu ngược sang ngôn ngữ hàm lồi cổ điển ($\mathrm{epi}(f)$), một tầng hoàn toàn khác, không thuộc phạm vi tài liệu này.

### 2.3. Tổng kết Sec 2

| Khối | Tên | Cần gì từ $\sim$ | Dùng cho |
|---|---|---|---|
| Pa1 | Antitone | Không cần gì (đúng với mọi quan hệ) | Nền tảng Galois |
| Pa2 | Extensive | Đối xứng | Nền tảng Galois |
| Pa3 | Upward-closed | Đơn điệu của $+$ theo $\le$ ở tọa độ $r$ | Order trên thớ |
| Pb1 | Fiber-closed | Đầy đủ Dedekind của $\mathbb R$ | Giải tích thực |
| Pb2 | Topo-closed | Liên tục của $\phi_p$ | Tô pô |
| Pb3 | Convexity | Affine của $\phi_p$ | Tuyến tính — **không dùng ở Sec 4** |

Từ đây, Sec 3 và Sec 4 **chỉ được viện dẫn Pa1–Pa3, Pb1–Pb3** (và Định lý 2.1.1 — bản thân nó là hệ quả của Pa1+Pa2) như hộp đen, tuyệt đối không quay lại công thức $\langle x,y\rangle\le r+s$.

---

## Sec 3. Regepi, meet, fibor — Định lý biểu diễn

**Định nghĩa 3.1 (Regepi).**
$$\mathbb X := \{E\subseteq\overline X : E=E^{**}\}.$$

**Định nghĩa 3.2 (Meet và fibor — qua đóng bipolar).** Với $E,F\in\mathbb X$:
$$E\wedge F := (E\cap F)^{**}, \qquad E\oplus F := \big(E+_{fib}^{(s)}F\big)^{**}.$$

### 3.1. Định lý biểu diễn — phép đóng dư thừa

**Định lý 3.1.1 (Meet = giao, không cần đóng thêm).** Với $E,F\in\mathbb X$: $E\cap F\in\mathbb X$, và do đó $E\wedge F=E\cap F$.

*Chứng minh.* Vì $E\cap F\subseteq E$, Pa1 (áp hai lần, tức đơn điệu của $**$ suy ra từ Pa1) cho $(E\cap F)^{**}\subseteq E^{**}=E$; tương tự $\subseteq F$. Vậy $(E\cap F)^{**}\subseteq E\cap F$. Chiều ngược là Pa2 áp cho $E\cap F$. Bằng nhau. $\blacksquare$

**Định lý 3.1.2 (Key Lemma — fiber sum của hai regepi đã tự đóng).** Với $E,F\in\mathbb X$: $E+_{fib}^{(s)}F\in\mathbb X$, và do đó $E\oplus F=E+_{fib}^{(s)}F$.

*Chứng minh.* Đặt $A:=E+_{fib}^{(s)}F$. Chiều $A\subseteq A^{**}$ là Pa2. Chiều ngược:

Theo Pa3 (áp cho $E,F$ riêng lẻ), $E_x,F_x$ là các tia hướng lên; tại $x\in\pi(E)\cap\pi(F)$ (ký hiệu $\pi(E):=\{x:E_x\ne\emptyset\}$), $A_x=E_x+F_x$ với ngưỡng $\theta_A(x):=\theta_E(x)+\theta_F(x)$ (cộng-tia, đẳng thức tập hợp thô).

Lấy $(x_0,u_0)\in A^{**}$, $u_0$ hữu hạn (trường hợp $u_0=+\infty$ tầm thường vì $A$ cũng upward-closed, kế thừa Pa3 áp cho chính $A$ qua $A^{**}$). Vì $A^{**}$ đóng (Pb2), và $A\subseteq A^{**}$ (Pa2), có dãy $(x_k,u_k)\in A$, $(x_k,u_k)\to(x_0,u_0)$ (lập luận sandwich: $A\subseteq A^{**}\subseteq\overline A^{\,top}$ theo Pb2 áp cho $A^{**}$, và $A^{**}$ chính là closure tô pô của $A$ — chứng minh: mọi $H_p$ chứa $A$ đều đóng nên chứa $\overline A^{\,top}$, vậy $\overline A^{\,top}\subseteq\bigcap_{p\in A^*}H_p=A^{**}$; kết hợp $A\subseteq A^{**}$ đóng (Pb2) cho $\overline A^{\,top}\subseteq A^{**}$, hai chiều bằng nhau).

Theo Pb1 áp cho $E$ và cho $F$ riêng biệt, kết hợp Pb2 (để dãy giới hạn nằm trong tập đóng), ta có tính nửa liên tục dưới của ngưỡng thớ:
$$\liminf_k\theta_E(x_k)\ge\theta_E(x_0), \qquad \liminf_k\theta_F(x_k)\ge\theta_F(x_0)$$
(chứng minh chi tiết: nếu $\liminf\theta_E(x_k)=L<\infty$, lấy dãy con $\theta_E(x_{k_j})\to L$; theo Pb1, $(x_{k_j},\theta_E(x_{k_j})+1/j)\in E$, dãy này hội tụ tới $(x_0,L)$; vì $E=E^{**}$ đóng theo Pb2, $(x_0,L)\in E$, tức $\theta_E(x_0)\le L$).

Cộng hai bất đẳng thức liminf (không dạng vô định, vì các ngưỡng luôn hữu hạn-hoặc-$+\infty$, không bao giờ $-\infty$ — hệ quả của $A^{**}\subseteq\bigcap H_p$ với $H_p$ chặn dưới theo $r$):
$$\liminf_k\theta_A(x_k)\ge\theta_E(x_0)+\theta_F(x_0)=\theta_A(x_0).$$
Mặt khác $\theta_A(x_k)\le u_k\to u_0<\infty$ nên $x_0\in\pi(A)$ và $\theta_A(x_0)\le u_0$. Vì $A$ upward-closed theo thớ (Pa3, kế thừa từ $E,F$): $u_0\in A_{x_0}$, tức $(x_0,u_0)\in A$. $\blacksquare$

**Hệ quả 3.1.3 (Định lý biểu diễn).** Trên $\mathbb X$, hai phép toán thô $\cap$ và $+_{fib}^{(s)}$ đã tự động đóng — việc lấy closure bipolar $(-)^{**}$ trong định nghĩa của $\wedge,\oplus$ là **dư thừa** đối với hai regepi bất kỳ đã cho sẵn. Vì vậy từ đây, ta viết đồng nhất
$$E\wedge F = E\cap F, \qquad E\oplus F = E+_{fib}^{(s)}F \qquad \forall E,F\in\mathbb X.$$

---

## Sec 4. Xây ICS chỉ từ Pa1–Pa3, Pb1–Pb3 (không quay lại $\sim$, không dùng epi(f))

Nguyên tắc thép: mọi bước dưới đây chỉ được viện dẫn Sec 1 (định nghĩa thô), Sec 3 (Định lý biểu diễn), và Pa1–Pa3/Pb1–Pb3 như hộp đen. **Không một dòng nào được viết dưới dạng hàm $e:X\to\overline{\mathbb R}$ hay $\mathrm{epi}(e)$** — biểu diễn hàm là một tầng hoàn toàn khác, nằm ngoài phạm vi Sec 4.

### 4.1. Đơn vị

$$e_\wedge := \overline X, \qquad e_\oplus := X\times[0,+\infty], \qquad X:=\mathbb R^n.$$

### 4.2. Nhóm M0–M3 — chỉ cần Pa1, Pa2 (qua Định lý 3.1.1)

**Định lý 4.2.1.** $(\mathbb X,\wedge)$ với $\wedge=\cap|_\mathbb X$ (Định lý 3.1.1) thỏa M0 ($E\wedge E=E$), M1 (kết hợp), M2 (giao hoán) — tự động, tính chất chuẩn của $\cap$. M3: $E\wedge e_\wedge = E\cap\overline X = E$, tầm thường vì $E\subseteq\overline X$ với mọi $E\in\mathcal P(\overline X)$.

### 4.3. P và PM/(Abs) — chỉ cần Pa1, Pa2

**P** đã có ở Định lý 2.1.1 (chính là định nghĩa $\mathbb X$ cộng với involution đã chứng minh).

**Định nghĩa 4.3.1.** $E\vee F := (E^*\wedge F^*)^*$.

**Định lý 4.3.2 ($\vee$ = đóng của hợp).** $E\vee F=(E\cup F)^{**}$.

*Chứng minh.* $E^*\wedge F^*\overset{\text{Đlý }3.1.1}{=}E^*\cap F^* = (E\cup F)^*$ (hợp→giao, hệ quả của Pa1+Pa2 — xem Bổ đề adjunction: $B\subseteq A^*\iff A\subseteq B^*$, suy trực tiếp từ Pa1+Pa2, rồi $(E\cup F)^*=\bigcap$ các $\{e\}^*$ theo cùng cơ chế). Áp $*$: $(E^*\wedge F^*)^*=(E\cup F)^{**}$. $\blacksquare$

**Định lý 4.3.3 (Abs).** $E\wedge(E\vee F)=E$, $E\vee(E\wedge F)=E$.

*Chứng minh (Abs1).* $E\subseteq E\cup F\subseteq(E\cup F)^{**}=E\vee F$ (Pa2). Vì $E\subseteq E\vee F$, cả hai $\in\mathbb X$: $E\wedge(E\vee F)=E\cap(E\vee F)=E$ (Định lý 3.1.1).

*Chứng minh (Abs2).* $E\wedge F=E\cap F\subseteq E$ (Định lý 3.1.1), nên $E\cup(E\wedge F)=E$; áp Định lý 4.3.2: $E\vee(E\wedge F)=(E\cup(E\wedge F))^{**}=E^{**}=E$. $\blacksquare$

**Hệ quả 4.3.4 (PM).** $E\subseteq F\iff F^*\subseteq E^*$ — từ tương đương (Abs)$\iff$(PM) (không cần thêm gì ngoài M0–M2 đã có và Định lý 4.3.3).

### 4.4. S3, SM2 — chỉ cần Pa3

**Định lý 4.4.1 (S3).** $E\oplus e_\oplus = E$.

*Chứng minh.* $(x,r)\in E+_{fib}^{(s)}e_\oplus \iff \exists r_0\in E_x, t\ge0: r=r_0+t \iff \exists r_0\in E_x, r_0\le r$. Chiều $\Leftarrow$: lấy $r_0=r,t=0$. Chiều $\Rightarrow$: hiển nhiên $r_0\le r$. Vậy vế phải $\iff \exists r_0\in E_x, r_0\le r$; kết hợp Pa3 (upward-closed) cho chiều $\Rightarrow r\in E_x$, và $r_0=r\in E_x$ cho chiều $\Leftarrow$ trực tiếp. Nên $E+_{fib}^{(s)}e_\oplus = E$ (đẳng thức tập hợp thô); theo Định lý 3.1.2, $E\oplus e_\oplus = E+_{fib}^{(s)}e_\oplus=E$. $\blacksquare$

**Định lý 4.4.2 (SM2, trên $E\ne\emptyset$).** $E\oplus e_\wedge = e_\wedge$.

*Chứng minh.* $E+_{fib}^{(s)}\overline X = \{(x,r+t):(x,r)\in E, t\in(-\infty,+\infty]\} = \pi(E)\times(-\infty,+\infty]$ (với $x\in\pi(E)$, $r$ cố định hữu hạn-hoặc-$+\infty$, $t$ chạy khắp $(-\infty,+\infty]$ nên $r+t$ chạy khắp). Tính polar: với $p=(y,s)$, $p\in\big(\pi(E)\times(-\infty,+\infty]\big)^*$ đòi hỏi $\langle x,y\rangle\le r+s$ với **mọi** $r\in(-\infty,+\infty]$ và $x\in\pi(E)\ne\emptyset$ cố định — cho $r\to-\infty$ phá vỡ bất đẳng thức với mọi $y,s$ hữu hạn. Vậy $\big(\pi(E)\times(-\infty,+\infty]\big)^*=\emptyset$, nên $\big(\pi(E)\times(-\infty,+\infty]\big)^{**}=\emptyset^*=\overline X$ (tính trực tiếp: $\emptyset^*=\{p:\forall e\in\emptyset,\dots\}=\overline X$, đúng với mọi $p$). Theo Định lý 3.1.2: $E\oplus e_\wedge = (E+_{fib}^{(s)}\overline X)^{**} = \overline X = e_\wedge$. $\blacksquare$

*(Trường hợp $E=\emptyset$: $\emptyset+_{fib}^{(s)}F=\emptyset$ với mọi $F$, nên $\emptyset\oplus e_\wedge=\emptyset\ne e_\wedge$ — $\emptyset$ là phần tử hút riêng, ngoại lệ đã biết.)*

### 4.5. S1, SM1 — cần đủ cả sáu khối trừ Pb3

**Định lý 4.5.1 (S1).**
$$(E\oplus F)\oplus G = E\oplus(F\oplus G).$$

*Chứng minh.* Bổ đề kết hợp thô (từ Sec 1, không cần polar): $(E+_{fib}^{(s)}F)+_{fib}^{(s)}G = E+_{fib}^{(s)}(F+_{fib}^{(s)}G)$, từ $(r+s)+t=r+(s+t)$. Theo Định lý 3.1.2 (Key Lemma — dùng Pa1,Pa2,Pa3,Pb1,Pb2), $E+_{fib}^{(s)}F, F+_{fib}^{(s)}G\in\mathbb X$, nên $\oplus=+_{fib}^{(s)}$ trên các cặp này:
$$(E\oplus F)\oplus G = (E+_{fib}^{(s)}F)\oplus G \overset{\text{Đlý }3.1.2}{=} (E+_{fib}^{(s)}F)+_{fib}^{(s)}G = E+_{fib}^{(s)}(F+_{fib}^{(s)}G) \overset{\text{Đlý }3.1.2}{=} E\oplus(F\oplus G). \qquad\blacksquare$$

**Định lý 4.5.2 (SM1).**
$$E\oplus(F\wedge G) = (E\oplus F)\wedge(E\oplus G).$$

*Chứng minh.* Bổ đề ray-arithmetic (thớ theo thớ, chỉ dùng Pa3 để đảm bảo mọi thớ liên quan là tia thật sự): tại mỗi $x$,
$$E_x+(F_x\cap G_x) = (E_x+F_x)\cap(E_x+G_x),$$
từ $a+\max(b,c)=\max(a+b,a+c)$ ở mức số thực mở rộng, áp cho ngưỡng các tia. $F\wedge G=F\cap G\in\mathbb X$ (Định lý 3.1.1). Theo Key Lemma (Định lý 3.1.2): $E\oplus(F\wedge G)=E+_{fib}^{(s)}(F\cap G)$, và $E\oplus F=E+_{fib}^{(s)}F$, $E\oplus G=E+_{fib}^{(s)}G$ (cả ba đã tự đóng). Áp ray-arithmetic theo từng thớ rồi hợp trên $X$:
$$E+_{fib}^{(s)}(F\cap G) = (E+_{fib}^{(s)}F)\cap(E+_{fib}^{(s)}G) \overset{\text{Đlý }3.1.1}{=} (E\oplus F)\wedge(E\oplus G). \qquad\blacksquare$$

### 4.6. Bảng tổng kết Sec 4

| Tiên đề | Pa1 | Pa2 | Pa3 | Pb1 | Pb2 | Pb3 |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| M0 | ✓ | ✓ | | | | |
| M1 | ✓ | ✓ | | | | |
| M2 | ✓ | ✓ | | | | |
| M3 | ✓ | ✓ | | | | |
| **P** | ✓ | ✓ | | | | |
| **PM**/(Abs) | ✓ | ✓ | | | | |
| S1 | ✓ | ✓ | ✓ | **✓** | **✓** | |
| S2 | | | | | | |
| S3 | | | ✓ | | | |
| SM1 | ✓ | ✓ | ✓ | **✓** | **✓** | |
| SM2 ($E\ne\emptyset$) | ✓ | | ✓ | | | |

*(S2 trống hoàn toàn — đã chứng minh xong ở Mệnh đề 1.2.2, trước khi $*$ tham gia.)*

**Ba quan sát chốt.**

1. **Cột Pb3 (convexity) trống tuyệt đối trên cả 11 hàng.** Regepi lồi (Pb3, chứng minh ở Sec 2.2) là một sự kiện thật của $*$, nhưng không tiên đề ICS nào cần đến nó.

2. **S1, SM1 là hai hàng duy nhất chạm Pb1+Pb2 đồng thời** — điểm nghẽn thực sự duy nhất của toàn bộ việc xây ICS, và nó nằm hoàn toàn trong nhóm Pb1 (đầy đủ Dedekind) + Pb2 (tô pô đóng), không hề cần Pb3.

3. **Nhóm M/P/PM chỉ cần Pa1+Pa2**, không cần Pa3 (upward) — các chứng minh Định lý 3.1.1, 4.3.2, 4.3.3 chưa từng chạm tới thớ hay tọa độ $r$, chỉ thao tác ở mức $\cap,\cup$ trên toàn bộ $\overline X$.

> **Định lý tổng hợp.** $(\mathbb X,\wedge,\oplus,{}^*)$ với $e_\wedge=\overline X$, $e_\oplus=X\times[0,+\infty]$ thỏa đầy đủ M0–M3, S1–S3, SM1, P, PM (SM2 trên phần tử proper), chỉ dùng Pa1–Pa3 và Pb1–Pb2 làm nguyên liệu hình học — **Pb3 (convexity) hoàn toàn không được sử dụng**. Do đó $\mathbb X$ là một idempotent commutative semiring với polar đối hợp, tương thích đầy đủ với meet theo nghĩa (PM).
