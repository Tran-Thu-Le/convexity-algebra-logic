# Idempotent Commutative Semiring với Polar

**Tóm tắt.** Chúng tôi nghiên cứu cấu trúc $(X,\wedge,+,{}^*)$ gồm một *meet* $\wedge$ idempotent-commutative, một *sum* $+$ commutative, liên kết bởi phân phối, cùng một *polar* $(-)^*$ chỉ thỏa tính đối hợp. Chúng tôi chỉ ra: (i) polar tự động là song ánh; (ii) $\wedge$ sinh một thứ tự bộ phận mà cả $\wedge,+$ đều đơn điệu theo đó — độc lập với polar; (iii) polar tự động biến $(\wedge,+)$ thành một semiring dẫn xuất thứ hai $(\vee,\times)$ và cho một phản-đẳng-cấu thứ tự *miễn phí* giữa hai thứ tự sinh bởi $\wedge$ và $\vee$; (iv) để polar phản biến trên **một** thứ tự duy nhất — điều kiện (PM) — cần một giả thiết **độc lập, không tự động**, tương đương với luật hấp thụ cổ điển của lattice. Một phản ví dụ hữu hạn xác nhận (PM) không suy ra từ các tiên đề còn lại.

---

## 1. Giới thiệu

Cấu trúc polar (Fenchel conjugate, phủ định tuyến tính) xuất hiện xuyên suốt trong convex analysis và linear logic như một đối hợp nghịch đảo thứ tự trên các đối tượng lồi/công thức. Bài này tách bạch, ở mức trừu tượng tối thiểu, **kết quả nào tự động có** từ tiên đề đại số thuần túy, và **kết quả nào cần thêm giả thiết**. Kết quả chính là: tính "phản biến" của polar trên một thứ tự duy nhất — thường được ngầm giả định — **không phải hệ quả tự động** của (meet lũy đẳng) + (sum) + (phân phối) + (polar đối hợp), mà tương đương với luật hấp thụ, một điều kiện độc lập.

---

## 2. Định nghĩa

**Định nghĩa 1 (Meet).** $(X,\wedge,e_\wedge)$ thỏa:

$$\textbf{M0}:\ a\wedge a=a \qquad \textbf{M1}:\ a\wedge(b\wedge c)=(a\wedge b)\wedge c \qquad \textbf{M2}:\ a\wedge b=b\wedge a \qquad \textbf{M3}:\ a\wedge e_\wedge=a$$

**Định nghĩa 2 (Sum).** $(X,+,e_+)$ thỏa:

$$\textbf{S1}:\ a+(b+c)=(a+b)+c \qquad \textbf{S2}:\ a+b=b+a \qquad \textbf{S3}:\ a+e_+=a$$

**Định nghĩa 3 (Liên hệ Sum–Meet).**

$$\textbf{SM1}\ (\text{phân phối}):\ a+(b\wedge c)=(a+b)\wedge(a+c) \qquad \textbf{SM2}\ (\text{hấp thụ}):\ a+e_\wedge=e_\wedge$$

**Định nghĩa 4 (Polar).** $(-)^*:X\to X$ thỏa:

$$\textbf{P}:\ a^{**}=a\qquad\forall a\in X.$$

**Định nghĩa 5 (Toán tử dẫn xuất, thứ tự).**
$$a\vee b:=(a^*\wedge b^*)^*,\quad e_\vee:=e_\wedge^*, \qquad a\times b:=(a^*+b^*)^*,\quad e_\times:=e_+^*,$$
$$a\le b:\iff a\wedge b=a, \qquad a\le^* b:\iff a\vee b=b.$$

**Định nghĩa 6 (Tương thích).**
$$\textbf{PM}:\qquad a\le b\iff b^*\le a^*\qquad\forall a,b\in X.$$

*(Toàn bài dùng M0–M3, S1–S3, SM1, P làm nền; SM2 chỉ để hoàn chỉnh định nghĩa semiring cổ điển, không dùng trong chứng minh nào dưới đây.)*

---

## 3. Kết quả nguyên thủy — độc lập với polar

**Bổ đề 1 (L1 — Polar là song ánh).** Từ **P**: $(-)^*$ là song ánh, $\ast\circ\ast=\mathrm{id}_X$.

*Chứng minh.* Đơn ánh: $a^*=b^*\Rightarrow a=(a^*)^*=(b^*)^*=b$. Toàn ánh: $b=(b^*)^*$, tiền ảnh của $b$ là $b^*$. $\blacksquare$

**Bổ đề 2 (L2 — Thứ tự từ lũy đẳng).** Từ **M0–M2**: $\le$ là thứ tự bộ phận, $e_\wedge$ là phần tử lớn nhất (dùng thêm M3).

*Chứng minh.* Phản xạ: M0. Phản đối xứng: $a\wedge b=a,\,b\wedge a=b\overset{\text{M2}}{\Rightarrow}a=b$. Bắc cầu: $a\wedge b=a,\,b\wedge c=b\Rightarrow a\wedge c=(a\wedge b)\wedge c\overset{\text{M1}}{=}a\wedge(b\wedge c)=a\wedge b=a$. $\blacksquare$

**Định lý 1 (TA, TB — Đơn điệu).**
$$a\le b\ \Rightarrow\ a\wedge c\le b\wedge c\quad(\text{cần M0-M2}), \qquad a\le b\ \Rightarrow\ a+c\le b+c\quad(\text{cần M0-M2, SM1}).$$

*Chứng minh (TA).* $(a\wedge c)\wedge(b\wedge c)\overset{\text{M1,M2}}{=}(a\wedge b)\wedge(c\wedge c)\overset{a\wedge b=a,\ \text{M0}}{=}a\wedge c$.

*Chứng minh (TB).* Áp SM1 với $(c,a,b)$: $c+(a\wedge b)=(c+a)\wedge(c+b)$. Vì $a\wedge b=a$: $c+a=(c+a)\wedge(c+b)$, tức $a+c\le b+c$ (dùng S2). $\blacksquare$

*Nhận xét.* TA không cần SM1; hai nhánh {L1} và {L2, TA, TB} độc lập hoàn toàn với nhau và với polar.

---

## 4. Semiring dẫn xuất qua polar

**Bổ đề 3 (De Morgan trừu tượng).** Từ **P**: $(a\vee b)^*=a^*\wedge b^*$, $(a\times b)^*=a^*+b^*$.

*Chứng minh.* $(a\vee b)^*=((a^*\wedge b^*)^*)^*\overset{\text{P}}{=}a^*\wedge b^*$. Tương tự. $\blacksquare$

**Định lý 2 (T1 — Semiring thứ hai).** Từ **P, M0-M3, S1-S3, SM1**: $(X,\vee,\times,e_\vee,e_\times)$ thỏa M0-M3, S1-S3, SM1 (với vai trò $\wedge\to\vee,\ +\to\times$), và $(-)^*$ là đẳng cấu đại số giữa hai semiring.

*Chứng minh (phác).* Mỗi tiên đề được suy ra bằng cách áp $*$, dùng Bổ đề 3 và **P** để "vận chuyển" tiên đề tương ứng của $(\wedge,+)$. Ví dụ, kết hợp của $\vee$:
$$(a\vee b)\vee c\overset{\text{đ/n, BĐ3}}{=}\big((a^*\wedge b^*)\wedge c^*\big)^*\overset{\text{M1}}{=}\big(a^*\wedge(b^*\wedge c^*)\big)^*=a\vee(b\vee c).$$
Phân phối: $a\times(b\vee c)=(a^*+(b\vee c)^*)^*=(a^*+(b^*\wedge c^*))^*\overset{\text{SM1}}{=}((a^*+b^*)\wedge(a^*+c^*))^*=(a\times b)\vee(a\times c)$. Các tiên đề còn lại tương tự. $\blacksquare$

**Định lý 3 (T2 — Cross-antitone, miễn phí).** Từ **P, M0-M2**:
$$a\le b\iff b^*\le^*a^*\qquad\forall a,b\in X.$$

*Chứng minh.* ($\Rightarrow$) $a\wedge b=a$. Áp $*$: $a^*=(a\wedge b)^*\overset{\text{BĐ3 ngược}}{=}$ ta tính $(a^*\vee b^*)^*\overset{\text{BĐ3}}{=}a^{**}\wedge b^{**}\overset{\text{P}}{=}a\wedge b=a$, nên $a^*\vee b^*=a^*\Rightarrow b^*\vee a^*=a^*\Rightarrow b^*\le^*a^*$. ($\Leftarrow$) đối xứng. $\blacksquare$

*Nhận xét.* T2 không cần S1-S3, SM1 — chỉ cần đủ để $\vee$ lũy đẳng-giao hoán (từ T1, vốn cần đầy đủ tiên đề để phát biểu, nhưng bản thân T2 dùng lại kết quả ấy chứ không cần lại toàn bộ chứng minh).

---

## 5. Điều kiện tương thích

**Bổ đề 4 (A, B — miễn phí).** Từ M0-M2 (và T1 cho phần $\vee$):
$$(a\wedge b)\wedge a=a\wedge b, \qquad a\vee(a\vee b)=a\vee b.$$

*Chứng minh.* $(a\wedge b)\wedge a\overset{\text{M1,M2}}{=}a\wedge a\wedge b\overset{\text{M0}}{=}a\wedge b$. $a\vee(a\vee b)\overset{\text{kết hợp}}{=}(a\vee a)\vee b\overset{\text{T1}}{=}a\vee b$. $\blacksquare$

**Định lý 4 (T3 — Bốn mệnh đề tương đương).** Các phát biểu sau tương đương:

$$\textbf{(C1)}\ a\wedge b=a\iff a\vee b=b \qquad \textbf{(C2)}\ \le\,=\,\le^* \qquad \textbf{(Abs)}\ a\wedge(a\vee b)=a,\ a\vee(a\wedge b)=a \qquad \textbf{(PM)}$$

*Chứng minh.*

**(C1)$\iff$(C2):** tầm thường — hai quan hệ $\le,\le^*$ bằng nhau khi và chỉ khi điều kiện xác định chúng tương đương với mọi cặp, đó là (C1).

**(Abs)$\Rightarrow$(C1):** $a\wedge b=a\Rightarrow$ áp Abs2 $(x{:=}b,y{:=}a)$: $b\vee(b\wedge a)=b\Rightarrow b\vee a=b\Rightarrow a\vee b=b$. Ngược lại $a\vee b=b\Rightarrow$ Abs1: $a\wedge(a\vee b)=a\Rightarrow a\wedge b=a$.

**(C1)$\Rightarrow$(Abs):** Abs1: áp (C1) với $(a,a\vee b)$, vế phải $a\vee(a\vee b)=a\vee b$ đúng theo Bổ đề 4 $\Rightarrow$ vế trái $a\wedge(a\vee b)=a$ đúng. Abs2: áp (C1) với $(a\wedge b,a)$, vế trái $(a\wedge b)\wedge a=a\wedge b$ đúng theo Bổ đề 4 $\Rightarrow$ vế phải $(a\wedge b)\vee a=a$ đúng.

**(C2)$\iff$(PM):** theo T2, $a\le b\iff b^*\le^*a^*$; kết hợp (C2) ($\le^*=\le$): $b^*\le^*a^*\iff b^*\le a^*$. Vậy $a\le b\iff b^*\le a^*$, tức (PM). Ngược lại, nếu (PM) đúng, kết hợp T2 cho $b^*\le a^*\iff b^*\le^*a^*$ với mọi $a,b$; do $*$ toàn ánh (Bổ đề 1), điều này quét hết mọi cặp, cho $\le=\le^*$, tức (C2). $\blacksquare$

**Hệ quả.** Khi (PM) đúng, $(-)^*$ là một *order-anti-automorphism* đầy đủ của $(X,\le)$: song ánh (L1), tự nghịch đảo (L1), đảo chiều cả hai hướng (PM).

**Ví dụ 1 (Phản ví dụ — (PM) không tự động đúng).** Cho $X=\{z,p,q,e_\wedge\}$, $\wedge$: $e_\wedge$ đơn vị, $z$ hút ($z\wedge x=z$), $p\wedge q=z$, $p,q$ lũy đẳng. Polar: $z^*=z,\,q^*=q,\,e_\wedge^*=p,\,p^*=e_\wedge$ (đối hợp, kiểm trực tiếp). Tính $e_\wedge\vee q=(p\wedge q)^*=z^*=z$, nên
$$e_\wedge\wedge(e_\wedge\vee q)=e_\wedge\wedge z=z\neq e_\wedge,$$
vi phạm Abs1. Mô hình thỏa M0-M3, P đầy đủ nhưng (PM) sai. $\blacksquare$

---

## 6. Thảo luận

Trong mô hình cụ thể (regepi/Fenchel polar trên convex geometry), $\le$ chỉ được định nghĩa **một lần** (bao hàm tập hợp $\subseteq$), nên (C2) đúng theo nghĩa tầm thường ngay từ định nghĩa — thứ mà Định lý 4 chỉ ra là **không miễn phí ở tầng đại số trừu tượng** lại trở thành hệ quả của một sự kiện hình học cụ thể (bipolar containment $E\subseteq E^{**}$ trên toàn bộ preepi, không chỉ trên lớp đã chính quy hóa). Điều này cho thấy: luật hấp thụ (Abs), khi nhìn từ đại số trừu tượng, mã hóa chính xác lượng thông tin hình học bổ sung mà mô hình cụ thể cung cấp "miễn phí".

---

## 7. Kết luận

Bốn tầng kết quả — nguyên thủy (L1, L2, TA, TB), dẫn xuất (Bổ đề 3, T1, T2), tương thích (Bổ đề 4, T3) — tách bạch rõ ràng phần nào của trực giác hình học là **tất định đại số** và phần nào là **giả thiết bổ sung thật sự**. Hướng mở: (a) tìm điều kiện đại số thuần túy (không viện dẫn hình học) đảm bảo (PM); (b) mở rộng khung sang trường hợp $\wedge$ không lũy đẳng (bỏ M0) — khi đó $\le$ không còn là thứ tự bộ phận theo cách dựng ở Bổ đề 2, cần cơ chế khác.

---

## Phụ lục — Bảng tiên đề

| Tên | Phát biểu |
|---|---|
| M0 | $a\wedge a=a$ |
| M1 | $a\wedge(b\wedge c)=(a\wedge b)\wedge c$ |
| M2 | $a\wedge b=b\wedge a$ |
| M3 | $a\wedge e_\wedge=a$ |
| S1 | $a+(b+c)=(a+b)+c$ |
| S2 | $a+b=b+a$ |
| S3 | $a+e_+=a$ |
| SM1 | $a+(b\wedge c)=(a+b)\wedge(a+c)$ |
| SM2 | $a+e_\wedge=e_\wedge$ |
| P | $a^{**}=a$ |
| PM | $a\le b\iff b^*\le a^*$ |
