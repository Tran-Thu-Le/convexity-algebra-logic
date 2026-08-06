# Bảng ký hiệu và định lý 5 mệnh đề tương đương (v2, phần 2d)

## Bảng ký hiệu

| Cấp | Ký hiệu | Tên gọi | Định nghĩa | Vai trò |
| --- | --- | --- | --- | --- |
| Primitive | $(M,\cdot,\perp)$ | Polaroid | Monoid giao hoán mang một quan hệ polar | Cấu trúc nguyên thủy |
| Element | $x\cdot y$ | Tích monoid | Phép nhân trên $M$ | Phép hợp thành đại số |
| Element | $x\perp y$ | Quan hệ polar | Quan hệ nguyên thủy trên $M$ | Tương tác hình học / logic |
| Element | $y\div x$ | Residual điểm | $x\cdot m\perp y \iff m\perp(y\div x)$, $\forall m$ (nếu tồn tại) | Phép kéo theo ở mức phần tử |
| Power set | $A\cdot B$ | Tích nâng | $\{x\cdot y:x\in A,\ y\in B\}$ | Tensor trước regular hóa |
| Power set | $A^\perp$ | Polarity | $\{y:\forall x\in A,\ x\perp y\}$ | Đối tượng đối ngẫu |
| Power set | $A\cup B$ | Hợp | Hợp thông thường | Join nguyên thủy |
| Power set | $C/x$ | Preimage điểm | $\{m\in M : x\cdot m\in C\}$ | Nghịch ảnh qua phép nhân với $x$ |
| Power set | $C/B$ | Preimage tập | $\{m\in M : B\cdot\{m\}\subseteq C\} = \bigcap_{b\in B}(C/b)$ | Nghịch ảnh qua phép nhân với mọi phần tử của $B$ |
| Regular | $A^{\perp\perp}$ | Bipolar closure | $(A^\perp)^\perp$ | Toán tử regular hóa |
| Regular | $A\otimes B$ | Tensor regular | $(A\cdot B)^{\perp\perp}$ | Tensor trong polar semiring |
| Regular | $A\vee B$ | Join regular | $(A\cup B)^{\perp\perp}$ | Join trong polar semiring |
| Regular | $C\oslash x$ | Residual regular điểm | $(C/x)^{\perp\perp}$ | Preimage đã đóng hóa |
| Regular | $C\oslash B$ | Residual regular tập | $(C/B)^{\perp\perp}$ | Preimage đã đóng hóa |

**Chú thích phân tầng.** $y\div x$ (element, partial — có thể không tồn tại) khác hẳn về loại với $C/x$, $C/B$ (power set, total — luôn định nghĩa được, là preimage thuần túy qua phép nhân). $\oslash$ chỉ dùng sau khi đã lấy bipolar closure ($(\ )^{\perp\perp}$), sống ở tầng Regular, không dùng để chỉ preimage thô.

---

## Định nghĩa chi tiết

### Residual điểm $y\div x$

Phần tử $y\div x\in M$ (nếu tồn tại) là phần tử duy nhất thỏa:

$$x\cdot m\perp y \iff m\perp(y\div x) \qquad \text{với mọi } m\in M.$$

$y$ đóng vai trò mục tiêu (target), $x$ đóng vai trò số nhân (multiplier). Đây là toán tử **bộ phận** (partial) — không phải mọi polaroid đều có $y\div x$ tồn tại cho mọi cặp $x,y$.

### Preimage điểm $C/x$

$$C/x := \{m\in M : x\cdot m\in C\} \qquad (x\in M,\ C\subseteq M).$$

Đây là nghịch ảnh của $C$ qua ánh xạ $m\mapsto x\cdot m$ — luôn định nghĩa được (toán tử **toàn phần**, total), không cần điều kiện gì.

### Preimage tập $C/B$

$$C/B := \{m\in M : B\cdot\{m\}\subseteq C\} \qquad (B,C\subseteq M).$$

**Mệnh đề (công thức qua giao).** $C/B = \bigcap_{b\in B}(C/b)$.

*Chứng minh.* $m\in C/B \iff B\cdot\{m\}\subseteq C \iff \forall b\in B,\ b\cdot m\in C \iff \forall b\in B,\ m\in C/b \iff m\in\bigcap_{b\in B}(C/b)$. $\blacksquare$

Khi $B=\{x\}$: $C/\{x\}=C/x$, khớp định nghĩa mức tập-phần tử — mở rộng tự nhiên, cũng total.

### Liên hệ giữa hai tầng: khi $\div$ chui được vào $/$

$$\boxed{\{y\}^\perp/x = \{y\div x\}^\perp \qquad \text{(chỉ khi } y\div x \text{ tồn tại).}}$$

*Chứng minh.* $\{y\}^\perp/x = \{m: x\cdot m\in\{y\}^\perp\} = \{m:(x\cdot m)\perp y\}$. Khi $y\div x$ tồn tại, theo định nghĩa, $(x\cdot m)\perp y\iff m\perp(y\div x)$, nên tập trên bằng $\{m:m\perp(y\div x)\}=\{y\div x\}^\perp$. $\blacksquare$

Vế trái ($\{y\}^\perp/x$) luôn tồn tại (là một preimage); vế phải chỉ viết được khi $y\div x$ tồn tại — đẳng thức này nói chính xác: preimage đó **có đại diện tường minh bằng đúng một điểm**.

### Lát cắt tịnh tiến

$$D_{x,y} := \{y\}^\perp/x = \{m\in M : (x\cdot m)\perp y\}.$$

---

## Định lý 5 mệnh đề tương đương

Cho polaroid $(M,\cdot,\perp)$. Năm điều sau tương đương.

**(i) Nucleus:** $A^{\perp\perp}\cdot B^{\perp\perp}\subseteq(A\cdot B)^{\perp\perp}$ với mọi $A,B\subseteq M$.

**(ii) Điều kiện phản xạ (mức sinh):** với mọi $x\in M$, mọi $C$ regular, $C/x$ regular.

**(iii) Điều kiện mức phần tử:** với mọi $x,y\in M$, $D_{x,y}=\{y\}^\perp/x$ regular.

**(iv) Tương thích tensor:** $A^{\perp\perp}\otimes B^{\perp\perp}=A\otimes B$ với mọi $A,B\subseteq M$.

**(v) Điều kiện phản xạ đầy đủ:** với mọi $B\subseteq M$, mọi $C$ regular, $C/B$ regular.

---

### Sơ đồ chứng minh (dùng đúng ký hiệu bảng)

- **(i)$\Rightarrow$(ii):** đặt $D:=C/x$; từ định nghĩa, $\{x\}\cdot D\subseteq C$; áp (i) cho $\{x\},D$: $\{x\}^{\perp\perp}\cdot D^{\perp\perp}\subseteq(\{x\}\cdot D)^{\perp\perp}\subseteq C^{\perp\perp}=C$; dùng $x\in\{x\}^{\perp\perp}$: $\{x\}\cdot D^{\perp\perp}\subseteq C$, tức $D^{\perp\perp}\subseteq C/x=D$; kết hợp $D\subseteq D^{\perp\perp}$: $D=D^{\perp\perp}$.

- **(ii)$\Rightarrow$(i):** đặt $C:=(A\cdot B)^{\perp\perp}$. Với mỗi $a\in A$: $\{a\}\cdot B\subseteq C \Rightarrow B\subseteq C/a$; $C/a$ regular theo (ii) $\Rightarrow B^{\perp\perp}\subseteq C/a \Rightarrow \{a\}\cdot B^{\perp\perp}\subseteq C$; đúng mọi $a$: $A\cdot B^{\perp\perp}\subseteq C$. Lặp lại theo $b\in B^{\perp\perp}$: $A\subseteq C/b$ (vai trò $A,\{b\}$ đối xứng qua tính giao hoán của $\cdot$); $C/b$ regular theo (ii) $\Rightarrow A^{\perp\perp}\subseteq C/b \Rightarrow A^{\perp\perp}\cdot\{b\}\subseteq C$; đúng mọi $b\in B^{\perp\perp}$: $A^{\perp\perp}\cdot B^{\perp\perp}\subseteq C=(A\cdot B)^{\perp\perp}$.

- **(ii)$\Leftrightarrow$(v):** $C/B=\bigcap_{b\in B}(C/b)$; giao các tập regular là regular; lấy $B=\{x\}$ cho chiều ngược.

- **(ii)$\Leftrightarrow$(iii):** mọi $C$ regular viết $C=\bigcap_{y\in C^\perp}\{y\}^\perp$; $\big(\bigcap_i C_i\big)/x=\bigcap_i(C_i/x)$ (trực tiếp từ định nghĩa preimage); và $\{y\}^\perp/x=D_{x,y}$ theo định nghĩa.

- **(i)$\Leftrightarrow$(iv):** chiều $\subseteq$ luôn đúng từ $A\subseteq A^{\perp\perp}$, $B\subseteq B^{\perp\perp}$ và tính đơn điệu của $(\ )^{\perp\perp}$; chiều $\supseteq$ áp (i) rồi lấy $(\ )^{\perp\perp}$ hai vế, dùng $(A\cdot B)^{\perp\perp}$ đã regular (lũy đẳng).

---

## Điều kiện đủ: tồn tại residual điểm toàn phần

**Định lý.** Nếu $y\div x$ tồn tại với mọi $x,y\in M$, thì
$$D_{x,y}=\{y\}^\perp/x=\{y\div x\}^\perp$$
tự động regular (polar của một điểm luôn regular) $\Rightarrow$ (iii) $\Rightarrow$ (i).

---

## Liên hệ tầng regular ($\oslash$)

$C\oslash x:=(C/x)^{\perp\perp}$ và $C\oslash B:=(C/B)^{\perp\perp}$ chỉ được dùng **sau khi** định lý trên đã xác lập nucleus — chúng thuộc tầng thứ ba (Regular), dùng khi dựng polar semiring hoàn chỉnh $(\vee,\otimes,\oslash)$, không phải điều kiện của định lý 5 mệnh đề. Cả $C/x$, $C/B$ (preimage thô) luôn tồn tại vô điều kiện; $C\oslash x$, $C\oslash B$ cũng luôn tồn tại (vì $(\ )^{\perp\perp}$ luôn áp được), chỉ khác $C/x$, $C/B$ ở việc đã regular hóa hay chưa.

## Bốn mệnh đề về adjunction

### Mệnh đề 1 (Adjunction thô)

Với mọi $A,B,C\subseteq M$:

$$A\cdot B\subseteq C \iff A\subseteq C/B.$$

**Chứng minh.** $A\cdot B\subseteq C \iff \forall a\in A,\forall b\in B,\ a\cdot b\in C$. Đổi thứ tự lượng từ và dùng tính giao hoán $a\cdot b=b\cdot a$:
$$\iff \forall a\in A,\ B\cdot\{a\}\subseteq C \iff \forall a\in A,\ a\in C/B \iff A\subseteq C/B. \qquad\blacksquare$$

Đúng vô điều kiện, không cần $C$ regular.

---

### Mệnh đề 2 (Adjunction tensor — chỉ một chiều nếu $C$ không regular)

Với mọi $A,B,C\subseteq M$:

$$A\otimes B\subseteq C \implies A\subseteq C/B,$$

nhưng chiều ngược **không** đúng nói chung khi $C$ không regular.

**Chứng minh chiều thuận.** $A\cdot B\subseteq A\otimes B$ (tính mở rộng). Nếu $A\otimes B\subseteq C$ thì $A\cdot B\subseteq C$, áp Mệnh đề 1: $A\subseteq C/B$. $\blacksquare$

**Phản ví dụ chiều ngược.** Giả sử $A\subseteq C/B$, tức (Mệnh đề 1) $A\cdot B\subseteq C$. Lấy bipolar hai vế: $A\otimes B=(A\cdot B)^{\perp\perp}\subseteq C^{\perp\perp}$. Nếu $C$ không regular thì $C^{\perp\perp}\supsetneq C$, nên không suy ra được $A\otimes B\subseteq C$ — chỉ suy ra $A\otimes B\subseteq C^{\perp\perp}$, một bao hàm thức yếu hơn.

Cụ thể: lấy $C$ bất kỳ không regular (tồn tại vì $C\subsetneq C^{\perp\perp}$), $B=\{e\}$ ($e$ phần tử đơn vị), $A:=C/B=C/\{e\}=\{m:e\cdot m\in C\}=C$ (vì $e\cdot m=m$). Vậy $A=C\subseteq C/B$ đúng theo giả thiết, nhưng $A\otimes B=C\otimes\{e\}=(C\cdot\{e\})^{\perp\perp}=C^{\perp\perp}\ne C$ nói chung, nên $A\otimes B\not\subseteq C$. $\blacksquare$

---

### Mệnh đề 3 (Adjunction tensor với $C$ regular)

Nếu $C$ regular, thì với mọi $A,B\subseteq M$:

$$A\otimes B\subseteq C \iff A\subseteq C/B.$$

**Chứng minh.** Chiều $\Rightarrow$: Mệnh đề 2.

Chiều $\Leftarrow$: giả sử $A\subseteq C/B$. Theo Mệnh đề 1: $A\cdot B\subseteq C$. Lấy bipolar hai vế (đơn điệu): $(A\cdot B)^{\perp\perp}\subseteq C^{\perp\perp}$. Vì $C$ regular, $C^{\perp\perp}=C$, nên $A\otimes B=(A\cdot B)^{\perp\perp}\subseteq C$. $\blacksquare$

---

### Mệnh đề 4 (Trên họ các tập regular: $/ = \oslash$)

Giả sử nucleus (i) đúng trên $(M,\cdot,\perp)$ (điều kiện cộng tính). Khi đó với mọi $C$ regular và mọi $B\subseteq M$:

1. $C/B$ **regular**;
2. do đó định nghĩa $C\oslash B := C/B$ (giới hạn trên $C$ regular) là **nhất quán**: đầu ra tự động nằm trong đúng lớp regular, và theo Mệnh đề 3, nó là adjoint đúng nghĩa (hai chiều) của $\otimes$ — không cần thao tác $(\ )^{\perp\perp}$ nào thêm ở định nghĩa.

**Chứng minh (1).** Đây chính là mệnh đề (v) của định lý 5 mệnh đề tương đương, hệ quả trực tiếp của nucleus (i): với $C$ regular, $C/B=\bigcap_{b\in B}(C/b)$, mỗi $C/b$ regular theo (ii) (tương đương (i)), và giao các tập regular là regular (Bổ đề 0.3). $\blacksquare$

**Hệ quả của (2).** Vì $C/B$ đã regular (theo (1)), ép thêm $(\ )^{\perp\perp}$ không đổi gì: $(C/B)^{\perp\perp}=C/B$. Vậy định nghĩa cũ $C\oslash B:=(C/B)^{\perp\perp}$ và định nghĩa chốt $C\oslash B:=C/B$ **trùng nhau tuyệt đối** trên miền $C$ regular — không mâu thuẫn, chỉ là định nghĩa chốt bỏ đi một bước dư thừa. $\blacksquare$
