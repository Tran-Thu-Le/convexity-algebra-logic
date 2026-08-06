# Điều kiện cộng tính của liên hợp tổng quát: một khung thuần tối ưu (v3, bản chứng minh chi tiết)

## 1. Giới thiệu

File này viết lại nội dung trung tâm của dự án — điều kiện cần-và-đủ để phép liên hợp kép (bipolar closure) tương thích với phép cộng tập hợp (tổng Minkowski nâng) — bằng ngôn ngữ thuần giải tích lồi/tối ưu hóa, kèm chứng minh đầy đủ từng khẳng định của định lý trung tâm. Không dùng thuật ngữ đại số trừu tượng (monoid, quantale), không dùng ngôn ngữ logic hay lý thuyết phạm trù.

**Ghi chú phạm vi.** Phát biểu tổng quát nhất của kết quả này, ở mức trừu tượng, là một trường hợp riêng của định lý phản xạ Day (Day, 1972) trong lý thuyết phạm trù đóng đối xứng. File này không dùng và không cần ngôn ngữ đó — mọi định nghĩa và chứng minh dưới đây độc lập, dựa hoàn toàn trên bất đẳng thức/đẳng thức hàm số thực và đại số tập hợp cơ bản.

---

## 2. Định nghĩa polaroid tối ưu và sáu toán tử

### 2.1 Dữ liệu nguyên thủy

**Định nghĩa.** Một **hệ ghép cặp cộng tính** là bộ ba $(M,\oplus,\kappa)$ gồm:

- $M$ là một tập, mang phép cộng $\oplus:M\times M\to M$ giao hoán, kết hợp, có phần tử trung hòa $0$;
- $\kappa: M\times M\to\mathbb R\cup\{+\infty\}$ là một hàm ghép cặp đối xứng: $\kappa(x,y)=\kappa(y,x)$ với mọi $x,y\in M$.

Không giả thiết gì khác. Mọi tính chất thêm (như tồn tại residual) là giả thiết tường minh ở mục sau.

**Ví dụ chuẩn (Fenchel).** $M=\mathbb R^n\times\mathbb R$, $(p,w)\oplus(r,v)=(p+r,w+v)$, $\kappa\big((p,w),(q,s)\big)=\langle p,q\rangle-w-s$.

### 2.2 Sáu toán tử

**Mức phần tử (2 toán tử):**

1. **Phép cộng** $x\oplus y$.
2. **Liên hợp dịch chuyển** $x_2\ominus x_1$: nếu tồn tại, là phần tử thỏa

$$\kappa(x_1\oplus x_0,\ x_2) = \kappa(x_0,\ x_2\ominus x_1)\qquad\forall x_0\in M.$$

**Mức tập hợp (3 toán tử):** với $A,B\subseteq M$,

3. **Tổng Minkowski nâng**: $A\oplus B := \{a\oplus b: a\in A,\ b\in B\}$.
4. **Hợp**: $A\cup B$.
5. **Tập liên hợp**: $A^\star := \{y\in M:\kappa(x,y)\le 0\ \ \forall x\in A\}$.

**Mức lồi hóa (1 toán tử):**

6. **Tổng Minkowski đã đóng hóa**: $A\circledast B := (A\oplus B)^{\star\star}$, với $A^{\star\star}:=(A^\star)^\star$.

---

## 3. Điều kiện cộng tính: định lý và chứng minh chi tiết

### 3.0 Bổ đề nền (dùng xuyên suốt)

Bốn bổ đề sau chỉ dùng định nghĩa của $\star$, đúng với **mọi** hệ ghép cặp, không cần giả thiết gì thêm. Ta chứng minh chi tiết vì toàn bộ định lý chính dựa vào chúng.

**Bổ đề 0.1 (Mở rộng và đảo chiều bao hàm).** Với mọi $A\subseteq M$: $A\subseteq A^{\star\star}$. Với mọi $A\subseteq B\subseteq M$: $B^\star\subseteq A^\star$.

*Chứng minh.* Lấy $x\in A$. Với mọi $y\in A^\star$, theo định nghĩa $\kappa(x,y)\le0$ với mọi $x\in A$, nên riêng $x$ này thỏa $\kappa(x,y)\le0$; đúng với mọi $y\in A^\star$ nên $x\in(A^\star)^\star=A^{\star\star}$. Vậy $A\subseteq A^{\star\star}$.

Với $A\subseteq B$: lấy $y\in B^\star$, tức $\kappa(x,y)\le0$ với mọi $x\in B$. Vì $A\subseteq B$, riêng điều này đúng với mọi $x\in A$, nên $y\in A^\star$. Vậy $B^\star\subseteq A^\star$. $\blacksquare$

**Bổ đề 0.2 (Đơn điệu của liên hợp kép, và lũy đẳng).** Với mọi $A\subseteq B$: $A^{\star\star}\subseteq B^{\star\star}$. Với mọi $A$: $A^{\star\star\star}=A^\star$, và do đó $(A^{\star\star})^{\star\star}=A^{\star\star}$ — tức $A^{\star\star}$ luôn regular; nói riêng, $A^\star$ luôn regular với mọi $A$.

*Chứng minh.* Áp Bổ đề 0.1 (đảo chiều) hai lần cho $A\subseteq B$: $B^\star\subseteq A^\star$, rồi áp lại: $A^{\star\star}\subseteq B^{\star\star}$ (đảo chiều lần hai đưa về đúng chiều).

Cho $A^{\star\star\star}=A^\star$: áp Bổ đề 0.1 (mở rộng) cho $A$: $A\subseteq A^{\star\star}$, áp đảo chiều: $(A^{\star\star})^\star\subseteq A^\star$, tức $A^{\star\star\star}\subseteq A^\star$. Ngược lại, áp Bổ đề 0.1 (mở rộng) cho $B:=A^\star$: $A^\star\subseteq (A^\star)^{\star\star}=A^{\star\star\star}$. Hai chiều cho $A^{\star\star\star}=A^\star$.

Từ đó $(A^{\star\star})^{\star\star} = A^{\star\star\star\star} = (A^{\star\star\star})^\star = (A^\star)^\star = A^{\star\star}$ (dùng đẳng thức vừa chứng minh áp cho $A^\star$ thay vì $A$: $(A^\star)^{\star\star\star}=(A^\star)^\star$, tức $A^{\star\star\star\star}=A^{\star\star}$, và vế trái bằng $(A^{\star\star})^{\star\star}$). Vậy $A^{\star\star}$ regular.

Riêng $A^\star$: đặt $B:=A^\star$; $B^{\star\star}=A^{\star\star\star}=A^\star=B$, nên $B=A^\star$ regular. $\blacksquare$

**Bổ đề 0.3 (Giao của các tập regular là regular).** Nếu $C_i=C_i^{\star\star}$ với mọi $i$ trong một họ chỉ số bất kỳ, thì $\bigcap_i C_i$ regular.

*Chứng minh.* Luôn có $\bigcap_i C_i \subseteq (\bigcap_i C_i)^{\star\star}$ (Bổ đề 0.1). Ngược lại: với mỗi $j$, $\bigcap_i C_i\subseteq C_j$, áp Bổ đề 0.2 (đơn điệu): $(\bigcap_i C_i)^{\star\star}\subseteq C_j^{\star\star}=C_j$. Đúng với mọi $j$, nên $(\bigcap_i C_i)^{\star\star}\subseteq\bigcap_j C_j$. Hai chiều cho đẳng thức. $\blacksquare$

**Bổ đề 0.4 (Đặc trưng qua $T_A$).** Định nghĩa $T_A(C):=\{m\in M: A\oplus\{m\}\subseteq C\}$. Khi đó với mọi $A,D,C\subseteq M$:

$$A\oplus D\subseteq C \iff D\subseteq T_A(C).$$

Ngoài ra $T_A(C)=\bigcap_{a\in A}T_a(C)$ (viết $T_a:=T_{\{a\}}$), và với mọi họ $(C_i)$: $T_a\big(\bigcap_i C_i\big)=\bigcap_i T_a(C_i)$, và $T_a(\{y\}^\star)=D_{a,y}:=\{m:\kappa(a\oplus m,y)\le0\}$.

*Chứng minh.* $A\oplus D\subseteq C \iff \forall a\in A,\forall d\in D,\ a\oplus d\in C \iff \forall d\in D,\ \forall a\in A,\ a\oplus d\in C \iff \forall d\in D,\ A\oplus\{d\}\subseteq C \iff \forall d\in D,\ d\in T_A(C) \iff D\subseteq T_A(C)$ — chỉ là đổi thứ tự lượng từ, không cần giả thiết gì.

$T_A(C)=\{m: A\oplus\{m\}\subseteq C\}=\{m:\forall a\in A, a\oplus m\in C\}=\{m:\forall a\in A, m\in T_a(C)\}=\bigcap_{a\in A}T_a(C)$.

$T_a(\bigcap_i C_i)=\{m: a\oplus m\in\bigcap_i C_i\}=\{m:\forall i, a\oplus m\in C_i\}=\{m:\forall i, m\in T_a(C_i)\}=\bigcap_i T_a(C_i)$.

$T_a(\{y\}^\star)=\{m: a\oplus m\in\{y\}^\star\}=\{m:\kappa(a\oplus m,y)\le0\}=D_{a,y}$, đúng theo định nghĩa $D_{a,y}$. $\blacksquare$

**Bổ đề 0.5 (Phân rã một tập regular thành giao các tập liên hợp đơn).** Nếu $C$ regular, đặt $Y:=C^\star$, thì $C=\bigcap_{y\in Y}\{y\}^\star$.

*Chứng minh.* $C=C^{\star\star}=(C^\star)^\star=Y^\star$. Và $Y^\star=\{z:\forall y\in Y,\kappa(z,y)\le0\}=\{z:\forall y\in Y,\ z\in\{y\}^\star\}=\bigcap_{y\in Y}\{y\}^\star$. $\blacksquare$

---

### 3.1 Điều kiện cộng tính

$$A^{\star\star}\oplus B^{\star\star} \subseteq (A\oplus B)^{\star\star}\qquad\text{với mọi } A,B\subseteq M. \qquad\text{(i)}$$

### 3.2 Định lý năm mệnh đề tương đương

**(i) Điều kiện cộng tính:** như trên.

**(ii) Điều kiện phản xạ (mức sinh):** với mọi $x\in M$, mọi $C$ regular, $T_x(C)$ regular.

**(iii) Điều kiện mức phần tử:** với mọi $x_1,x_2\in M$, $D_{x_1,x_2}$ regular.

**(iv) Tương thích tensor:** $A^{\star\star}\circledast B^{\star\star}=A\circledast B$ với mọi $A,B\subseteq M$.

**(v) Điều kiện phản xạ đầy đủ:** với mọi $A\subseteq M$, mọi $C$ regular, $T_A(C)$ regular.

---

#### Chứng minh (i) $\Rightarrow$ (ii)

Cho $C$ regular. Đặt $D:=T_x(C)$. Cần chứng minh $D$ regular.

**Bước 1.** Theo định nghĩa $T_x$ (Bổ đề 0.4 với $A=\{x\}$): $\{x\}\oplus D\subseteq C$.

**Bước 2.** Áp (i) cho cặp tập $\{x\}$ và $D$:
$$\{x\}^{\star\star}\oplus D^{\star\star} \subseteq (\{x\}\oplus D)^{\star\star}.$$

**Bước 3.** Vì $\{x\}\oplus D\subseteq C$ (Bước 1) và $C$ regular, Bổ đề 0.2 (đơn điệu) cho $(\{x\}\oplus D)^{\star\star}\subseteq C^{\star\star}=C$. Kết hợp Bước 2:
$$\{x\}^{\star\star}\oplus D^{\star\star}\subseteq C.$$

**Bước 4.** Theo Bổ đề 0.1, $x\in\{x\}^{\star\star}$. Vậy
$$\{x\}\oplus D^{\star\star} \subseteq \{x\}^{\star\star}\oplus D^{\star\star} \subseteq C.$$

**Bước 5.** Theo Bổ đề 0.4 (chiều $\Rightarrow$), $\{x\}\oplus D^{\star\star}\subseteq C$ kéo theo $D^{\star\star}\subseteq T_x(C)=D$.

**Bước 6.** Theo Bổ đề 0.1, $D\subseteq D^{\star\star}$. Kết hợp Bước 5: $D=D^{\star\star}$, tức $D$ regular. $\blacksquare$

---

#### Chứng minh (ii) $\Rightarrow$ (i)

Cho $A,B\subseteq M$ bất kỳ. Đặt $C:=(A\oplus B)^{\star\star}$ — regular theo Bổ đề 0.2, và $A\oplus B\subseteq C$ theo Bổ đề 0.1.

**Lượt 1 (mở rộng $B$ thành $B^{\star\star}$).** Cố định $a\in A$. Vì $A\oplus B\subseteq C$, thu hẹp về $a$: $\{a\}\oplus B\subseteq C$. Theo Bổ đề 0.4: $B\subseteq T_a(C)$. Theo (ii), $T_a(C)$ regular, và vì $B\subseteq T_a(C)$ (tập đã regular), áp Bổ đề 0.2 (đơn điệu, cộng với tính $T_a(C)$ là điểm bất động): $B^{\star\star}\subseteq T_a(C)^{\star\star}=T_a(C)$. Theo Bổ đề 0.4 (chiều ngược): $\{a\}\oplus B^{\star\star}\subseteq C$.

Đúng với mọi $a\in A$, nên:
$$A\oplus B^{\star\star}\subseteq C. \tag{$*$}$$

**Lượt 2 (mở rộng $A$ thành $A^{\star\star}$).** Cố định $b\in B^{\star\star}$. Từ ($*$), thu hẹp về $b$: $A\oplus\{b\}\subseteq C$. Theo Bổ đề 0.4 (đổi vai trò $A,D$: ở đây lấy tập $\{b\}$ đóng vai "$D$" và $A$ đóng vai "$A$" trong bổ đề, dùng dạng đối xứng của phép cộng): $A\subseteq T_b(C)$. Theo (ii), $T_b(C)$ regular, nên $A^{\star\star}\subseteq T_b(C)$. Theo Bổ đề 0.4: $A^{\star\star}\oplus\{b\}\subseteq C$.

Đúng với mọi $b\in B^{\star\star}$, nên:
$$A^{\star\star}\oplus B^{\star\star}\subseteq C = (A\oplus B)^{\star\star}.$$

Đây chính là (i). $\blacksquare$

---

#### Chứng minh (ii) $\Leftrightarrow$ (v)

**(v) $\Rightarrow$ (ii):** lấy $A=\{x\}$ trong (v); vì $T_{\{x\}}=T_x$ theo định nghĩa, đây chính là (ii). Tầm thường.

**(ii) $\Rightarrow$ (v):** cho $A\subseteq M$ bất kỳ, $C$ regular. Theo Bổ đề 0.4: $T_A(C)=\bigcap_{a\in A}T_a(C)$. Theo (ii), mỗi $T_a(C)$ regular. Theo Bổ đề 0.3, giao của các tập regular là regular, nên $T_A(C)$ regular. $\blacksquare$

---

#### Chứng minh (ii) $\Leftrightarrow$ (iii)

**(ii) $\Rightarrow$ (iii):** lấy $C:=\{x_2\}^\star$ trong (ii). Theo Bổ đề 0.2, $\{x_2\}^\star$ luôn regular (là ảnh của $\star$). Áp (ii): $T_{x_1}(C)$ regular. Theo Bổ đề 0.4, $T_{x_1}(\{x_2\}^\star)=D_{x_1,x_2}$. Vậy $D_{x_1,x_2}$ regular. Đúng với mọi $x_1,x_2$, tức là (iii).

**(iii) $\Rightarrow$ (ii):** cho $C$ regular bất kỳ. Theo Bổ đề 0.5, $C=\bigcap_{y\in Y}\{y\}^\star$ với $Y=C^\star$. Theo Bổ đề 0.4 (tính chất giao hoán với giao):
$$T_x(C) = T_x\Big(\bigcap_{y\in Y}\{y\}^\star\Big) = \bigcap_{y\in Y} T_x(\{y\}^\star) = \bigcap_{y\in Y} D_{x,y}.$$
Theo (iii), mỗi $D_{x,y}$ regular. Theo Bổ đề 0.3, giao của chúng regular. Vậy $T_x(C)$ regular. Đúng với mọi $x$, tức (ii). $\blacksquare$

---

#### Chứng minh (i) $\Leftrightarrow$ (iv)

**(i) $\Rightarrow$ (iv):** cần chứng minh $A^{\star\star}\circledast B^{\star\star}=A\circledast B$, tức $(A^{\star\star}\oplus B^{\star\star})^{\star\star}=(A\oplus B)^{\star\star}$.

*Chiều $\subseteq$ (không cần (i)):* theo Bổ đề 0.1, $A\subseteq A^{\star\star}$, $B\subseteq B^{\star\star}$, nên $A\oplus B\subseteq A^{\star\star}\oplus B^{\star\star}$. Áp Bổ đề 0.2 (đơn điệu): $(A\oplus B)^{\star\star}\subseteq(A^{\star\star}\oplus B^{\star\star})^{\star\star}$, tức $A\circledast B\subseteq A^{\star\star}\circledast B^{\star\star}$.

*Chiều $\supseteq$ (dùng (i)):* áp (i) trực tiếp cho $A,B$: $A^{\star\star}\oplus B^{\star\star}\subseteq(A\oplus B)^{\star\star}$. Áp Bổ đề 0.2 (đơn điệu) hai vế:
$$(A^{\star\star}\oplus B^{\star\star})^{\star\star} \subseteq \big((A\oplus B)^{\star\star}\big)^{\star\star}.$$
Vế trái là $A^{\star\star}\circledast B^{\star\star}$. Vế phải: theo Bổ đề 0.2, $(A\oplus B)^{\star\star}$ đã regular, nên lấy $\star\star$ thêm lần nữa không đổi: $\big((A\oplus B)^{\star\star}\big)^{\star\star}=(A\oplus B)^{\star\star}=A\circledast B$. Vậy $A^{\star\star}\circledast B^{\star\star}\subseteq A\circledast B$.

Hai chiều cho đẳng thức (iv). $\blacksquare$

**(iv) $\Rightarrow$ (i):** theo Bổ đề 0.1, $A^{\star\star}\oplus B^{\star\star}\subseteq (A^{\star\star}\oplus B^{\star\star})^{\star\star}=A^{\star\star}\circledast B^{\star\star}$. Theo (iv), vế phải bằng $A\circledast B=(A\oplus B)^{\star\star}$. Vậy $A^{\star\star}\oplus B^{\star\star}\subseteq(A\oplus B)^{\star\star}$, đúng là (i). $\blacksquare$

---

### 3.3 Điều kiện đủ dễ kiểm tra: tồn tại liên hợp dịch chuyển

**Định lý.** Nếu với mọi $x_1,x_2\in M$, $x_2\ominus x_1$ tồn tại theo định nghĩa mục 2.2, thì (iii) đúng, do đó (i) đúng.

*Chứng minh.* Với mọi $x_1,x_2\in M$:
$$D_{x_1,x_2} = \{m:\kappa(x_1\oplus m,x_2)\le0\} = \{m:\kappa(m,x_2\ominus x_1)\le0\} = \{x_2\ominus x_1\}^\star,$$
trong đó bước giữa dùng đúng đẳng thức định nghĩa của $x_2\ominus x_1$ (áp cho ngưỡng $\le0$, hệ quả trực tiếp của việc hai vế bằng nhau như hàm số). Theo Bổ đề 0.2, $\{x_2\ominus x_1\}^\star$ luôn regular. Vậy $D_{x_1,x_2}$ regular, đúng với mọi $x_1,x_2$ — đây là (iii). Theo định lý 5 mệnh đề tương đương, (iii)$\Rightarrow$(ii)$\Rightarrow$(i). $\blacksquare$

---

## 4. Ứng dụng: bảng năm loại kernel

Mọi ví dụ dùng $M=\mathbb R^n\times\mathbb R$ (trừ ví dụ 5, $M$ tổng quát), tọa độ thứ hai là ngân sách, $\oplus$ là cộng tọa độ.

| # | Tên | $\kappa\big((p_1,w_1),(p_2,w_2)\big)$ | $x_2\ominus x_1$ | Cơ chế tách |
|---|---|---|---|---|
| 1 | Fenchel (bilinear chuẩn) | $\langle p_1,p_2\rangle - w_1-w_2$ | $\big(p_2,\ w_1+w_2-\langle p_1,p_2\rangle\big)$ | song tuyến tính |
| 2 | Fenchel có trọng số | $\langle Tp_1,p_2\rangle-w_1-w_2$, $T$ tuyến tính | $\big(p_2,\ w_1+w_2-\langle Tp_1,p_2\rangle\big)$ | song tuyến tính |
| 3 | Kernel toàn phương | $\tfrac12\|p_1-p_2\|^2-w_1-w_2$ | $\big(p_2-p_1,\ w_1+w_2\big)$ | bất biến tịnh tiến |
| 4 | Bất biến tịnh tiến tổng quát | $\psi(p_1-p_2)-w_1-w_2$, $\psi$ chẵn, tùy ý | $\big(p_2-p_1,\ w_1+w_2\big)$ | bất biến tịnh tiến |
| 5 | Ràng buộc cứng | $\iota_D(x_1\oplus x_2)$, $D\subseteq M$ bất kỳ | $x_1\oplus x_2$ | kết hợp + giao hoán của $\oplus$ |

### Kiểm chứng cụ thể (đại diện #1, #3, #5 — mẫu tính toán đầy đủ)

**#1 Fenchel.** $\kappa(x_1\oplus x_0,x_2)=\langle p_1+p_0,p_2\rangle-w_1-w_0-w_2 = \langle p_0,p_2\rangle - w_0 - \big(w_1+w_2-\langle p_1,p_2\rangle\big) = \kappa\big(x_0,(p_2,w_1+w_2-\langle p_1,p_2\rangle)\big)$. Đẳng thức đúng với mọi $x_0$.

**#3 Kernel toàn phương.** $\kappa(x_1\oplus x_0,x_2)=\tfrac12\|p_1+p_0-p_2\|^2-w_1-w_0-w_2$. Đặt $r=p_2-p_1$: $\|p_1+p_0-p_2\|^2=\|p_0-r\|^2$, nên biểu thức $=\tfrac12\|p_0-r\|^2-w_0-(w_1+w_2)=\kappa\big(x_0,(r,w_1+w_2)\big)$. Đẳng thức đúng với mọi $x_0$, không dùng tính lồi của $\tfrac12\|\cdot\|^2$.

**#5 Ràng buộc cứng.** $\kappa(x_1\oplus x_0,x_2)=\iota_D\big((x_1\oplus x_0)\oplus x_2\big)$. Dùng kết hợp+giao hoán của $\oplus$: $(x_1\oplus x_0)\oplus x_2 = x_0\oplus(x_1\oplus x_2)$, nên biểu thức $=\iota_D\big(x_0\oplus(x_1\oplus x_2)\big)=\kappa(x_0,x_1\oplus x_2)$. Đẳng thức đúng với mọi $x_0$, không dùng cấu trúc số thực nào của $\iota_D$ ngoài định nghĩa nhị phân.

### Ranh giới của cơ chế: khi nào thất bại

Lấy $M=\mathbb R^n$ trần (không tọa độ ngân sách), $\kappa(x,y)=\langle x,y\rangle$ (cone polar). Thử tách:
$$\kappa(x_1\oplus x_0,x_2)=\langle x_1,x_2\rangle+\langle x_0,x_2\rangle.$$
Muốn viết dưới dạng $\kappa(x_0,z)=\langle x_0,z\rangle$ với mọi $x_0$, so hệ số buộc $z=x_2$, nhưng còn dư số hạng hằng $\langle x_1,x_2\rangle$ không có chỗ hấp thụ (không có tọa độ ngân sách). Vậy $x_2\ominus x_1$ **không tồn tại** tổng quát.

Kiểm chứng trực tiếp (i) thất bại: $A_0=\{e_1\},B_0=\{e_2\}\subset\mathbb R^2$. $A_0^{\star\star}$ là tia qua $e_1$, $B_0^{\star\star}$ tia qua $e_2$ (định lý bao lồi nón cổ điển), nên $A_0^{\star\star}\oplus B_0^{\star\star}$ là cả góc phần tư thứ nhất. Nhưng $A_0\oplus B_0=\{(1,1)\}$, và $(A_0\oplus B_0)^{\star\star}$ chỉ là tia qua $(1,1)$. Góc phần tư không nằm trong một tia — (i) vỡ, minh chứng cụ thể cho việc thiếu tọa độ ngân sách phá vỡ điều kiện cộng tính dù $\kappa$ song tuyến tính, cùng dạng với #1.
