# Regepi là một Idempotent Commutative Semiring có Polar
### Bản cải tổ v3 — Tiên đề hóa qua Kernel Tổng quát, với Dot Product và Kernel Dịch chuyển như Hai Instance

---

## Lời nói đầu — vì sao cần viết lại bố cục

Bản v2 dựng toàn bộ lý thuyết trực tiếp trên kernel Fenchel $\langle x,y\rangle$: quan hệ $\sim$, sáu tiên đề Pa1–Pa3/Pb1–Pb3, rồi đại số $(\mathbb X,\wedge,\oplus,{}^*)$. Cách làm đó đúng nhưng **che giấu** một sự thật quan trọng: **không một dòng chứng minh nào trong Sec 2–4 thực sự cần đến dạng cụ thể $\langle x,y\rangle$** — chúng chỉ cần một số **tính chất trừu tượng** của kernel. Khi thảo luận mở rộng sang kernel tổng quát $c(x,y)$ và đặc biệt sang kernel dịch chuyển $c_h(x,y)=h(x+y)$ (sinh ra đúng residual của infimal convolution), sự thật này lộ ra rõ ràng, và hai lý thuyết tưởng độc lập (residual/inf-convolution và Fenchel polar) hoá ra là **hai instance của cùng một định lý tiên đề**.

Bố cục mới đảo ngược thứ tự trình bày: **kernel tổng quát trước, các trường hợp riêng sau**. Tiên đề hóa polar không còn là "làm cho gọn Fenchel" mà là **đối tượng nghiên cứu chính**; Fenchel và residual chỉ là hai điểm trong không gian kernel thỏa tiên đề.

---

## PHẦN I — Kernel-based Relation và Polar: tiên đề hóa từ gốc

### I.1. Không gian nền và kernel tổng quát

$$\overline X := \mathbb R^n\times(-\infty,+\infty],\qquad c: X\times X\to\overline{\mathbb R}\ \text{(kernel, chưa giả thiết gì)}.$$

**Định nghĩa I.1.1 (Quan hệ sinh bởi kernel).**
$$(x,r)\sim_c(y,s)\ :\iff\ c(x,y)\le r+s.$$

**Định nghĩa I.1.2 (Polar).** Với $E\subseteq\overline X$:
$$E^{*_c}:=\{p\in\overline X:\ e\sim_c p\ \ \forall e\in E\}.$$

Đây là **định nghĩa duy nhất** trong toàn bộ lý thuyết cần công thức tường minh của $c$. Từ đây trở đi, mọi thứ được xây trên $\sim_c$ như hộp đen, đúng tinh thần "sáu khối tiên đề" của bản v2, nhưng giờ **tham số hoá tường minh theo $c$**.

### I.2. Sáu tiên đề, và điều kiện tối thiểu thật sự cần trên $c$

Đây là nội dung cốt lõi cần nhấn mạnh của bản cải tổ — bảng dưới đây thay thế hoàn toàn Sec 2.3 của v2:

| Tiên đề | Phát biểu | Điều kiện tối thiểu trên $c$ | Có cần dạng cụ thể $\langle\cdot,\cdot\rangle$ không? |
|---|---|---|---|
| **Pa1** Antitone | $A\subseteq B\Rightarrow B^{*_c}\subseteq A^{*_c}$ | **Không cần gì** | Không — đúng cho mọi $c$ |
| **Pa2** Extensive ($A\subseteq A^{**}$) | | **$c$ đối xứng**: $c(x,y)=c(y,x)$ | Không — chỉ cần đối xứng |
| **Thm (Involution)** $A^{***}=A^{*}$ | hệ quả thuần túy của Pa1+Pa2 | như Pa2 | Không |
| **Pa3** Upward-closed theo thớ | | **Không cần gì** (chỉ dùng đơn điệu của $+$ trên $r$) | Không |
| **Pb1** Fiber-closed | | **Không cần gì** ($c(x,y)$ là hằng số cố định trong phép lấy giới hạn) | Không |
| **Pb2** Topo-closed ($A^{**}$ đóng) | | **$c(\cdot,y)$ nửa liên tục dưới (lsc), $\forall y$** (⟺ cả hai chiều, nhờ đối xứng ở Pa2) | Không — liên tục là dư thừa, lsc là đủ |
| **Pb3** Convexity | | $c(\cdot,y)$ lồi, $\forall y$ | **Không bao giờ được dùng ở Sec 4** — hoàn toàn phụ tùy |

**Hệ quả trung tâm (thay cho toàn bộ Sec 2 của v2):**

$$
\boxed{
\text{Đại số }(\mathbb X_c,\wedge,\oplus,{}^{*_c})\text{ là ICS đầy đủ} \iff c\text{ đối xứng và nửa liên tục dưới riêng theo từng biến.}
}
$$

Không cần song tuyến tính. Không cần lồi (chung hay riêng). Không cần liên tục toàn phần. **Dot product là một điểm rất đặc biệt** (đối xứng bởi song tuyến tính, liên tục toàn phần, affine cả hai chiều — "miễn phí" thừa mứa) trong một họ kernel rộng hơn nhiều mà lý thuyết vẫn đứng vững.

*(Chứng minh chi tiết từng dòng: giữ nguyên logic Sec 2.1–2.2 của v2, chỉ thay $\langle x,y\rangle$ bằng $c(x,y)$ tổng quát ở mọi bước; phần duy nhất cần sửa là bước "lật đối xứng" trong Pa2 — nay trở thành **điều kiện**, không còn là "tính chất tự động của $\langle,\rangle$".)*

### I.3. Vì sao Pa2 là nút thắt thật sự

Phân tích sâu (không có trong v2): định nghĩa $E^{**}$ trong khung "tự-đối-ngẫu một-không-gian" ($X=Y=\overline X$, tái dùng cùng công thức hai lần) ngầm giả định có thể "lật" $e\sim_c p \Rightarrow p\sim_c e$. Điều này **chỉ** đúng khi $c$ đối xứng. Nếu muốn dùng kernel không đối xứng (hoặc $X\ne Y$), phải chuyển sang khung **Galois connection hai phía** $\bar X\overset{\triangleright}{\to}\bar Y\overset{\triangleleft}{\to}\bar X$ với hai toán tử chuyển vị riêng biệt — khi đó extensivity $A\subseteq A^{\triangleright\triangleleft}$ lại đúng **vô điều kiện** (định lý Ore), nhưng đối tượng thu được là một cấu trúc hai-không-gian khác hẳn ICS tự-đối-ngẫu của tài liệu này. Đây chính là khung của $c$-conjugate tổng quát (Phần III).

---

## PHẦN II — Từ Polar đến ICS: Regepi, Meet, Fiber Sum (tổng quát hóa Sec 3–4 của v2)

Toàn bộ nội dung Sec 3–4 của v2 **giữ nguyên không đổi một chữ**, chỉ thay ký hiệu $*$ bằng $*_c$ ở khắp nơi, **miễn $c$ thỏa điều kiện ở bảng I.2** (đối xứng + lsc riêng biến). Đây là điểm mạnh nhất của việc viết lại: toàn bộ Định lý biểu diễn (3.1.1–3.1.3), Key Lemma, và Định lý tổng hợp Sec 4 (M0–M3, S1–S3, SM1, SM2, P, PM) **không cần viết lại chứng minh** — chúng là hệ quả của Pa1–Pa3+Pb1–Pb2 như hộp đen, và hộp đen đó nay đã được chứng minh đúng cho toàn bộ họ kernel (đối xứng + lsc riêng biến), không riêng gì dot product.

### II.1. Điểm mới: điều kiện tồn tại của các unit

Đây là nội dung **không có** trong v2 (v2 chỉ tính cho dot product, nơi mọi thứ "tự động ổn"):

**$e_\wedge=\overline X$:** luôn sống, mọi kernel $c$ (kể cả không đối xứng):
$$\overline X^{*_c}=\varnothing,\qquad \varnothing^{*_c}=\overline X.$$

**$e_\oplus=X\times[0,+\infty]$:** với kernel dịch chuyển $c_h(x,y)=h(x+y)$, cần thêm điều kiện **định lượng**:
$$
\boxed{e_\oplus\in\mathbb X_{c_h}\iff M:=\sup_X h<+\infty.}
$$
Nếu $M=+\infty$: $e_\oplus^{*_{c_h}}\to X\times\{+\infty\}\to \overline X=e_\wedge$ — hai unit sụp làm một, đại số suy biến (dù Pa1–Pa3, Pb1–Pb2 vẫn đúng nguyên vẹn!). Với kernel bilinear $\langle x,y\rangle$, unit luôn sống nhờ "điểm neo" $y=0$ mà kernel dịch chuyển không có (xem III.3).

$\Rightarrow$ **Tách bạch quan trọng**: "ICS có cấu trúc đúng" (Phần I) và "hai unit không suy biến" (Phần II.1) là **hai điều kiện độc lập** — kernel có thể thỏa cái đầu mà hỏng cái sau.

---

## PHẦN III — Hai họ kernel mẫu: Bilinear vs Dịch chuyển

### III.1. Kernel bilinear (Fenchel): $c(x,y)=\langle x,y\rangle$

- Đối xứng: đúng, nhờ tính đối xứng của dạng song tuyến tính — **phải kiểm, không tự động** trong họ kernel tổng quát, nhưng đúng cho trường hợp này.
- Pb2: $c(\cdot,y)$ liên tục (hữu hạn chiều) — dư thừa so với yêu cầu lsc.
- Pb3: $c(\cdot,y)$ affine — dư thừa, và **không dùng ở Sec 4**.
- Unit $e_\oplus$: luôn sống (điểm neo $y=0$, xem III.3).
- Bất biến dịch chuyển đường chéo $c(x+t,y-t)=c(x,y)$: **KHÔNG** — kernel bilinear thực sự phụ thuộc cả hai biến độc lập.

### III.2. Kernel dịch chuyển: $c_h(x,y)=h(x+y)$, $h$ proper lsc

- Đối xứng: **tự động**, mọi $h$ (hệ quả của $x+y=y+x$ — cấu trúc, không phải giả thiết).
- Pb2: cần đúng $h$ lsc (tịnh tiến bảo toàn lsc, không thêm gì).
- Pb3: cần $h$ lồi, nhưng **không dùng ở Sec 4** — có thể lấy $h$ lõm (vd. $h=c_0-\|x\|^2$) mà ICS vẫn đứng vững.
- Unit $e_\oplus$: sống $\iff \sup_X h<\infty$ — **không tự động**.
- Bất biến dịch chuyển đường chéo: **CÓ**, $c_h(x+t,y-t)=h(x+y)=c_h(x,y)$ — đây là đặc trưng cấu trúc của cả họ kernel này.

### III.3. Chứng minh chặt: hai họ rời nhau

Giả sử $c_h(x,y)=\langle x,y\rangle$ với $h$ nào đó, tức $h(x+y)=\langle x,y\rangle\ \forall x,y$. Cố định $x_0$, cho $y$ chạy: $h(w)=\langle x_0,w-x_0\rangle$ với $w=x_0+y$ — **phải đúng với mọi $x_0$**, nhưng vế phải phụ thuộc $x_0$ còn vế trái thì không $\Rightarrow$ mâu thuẫn trừ $\dim X=0$ (đây chính là chứng minh chặt "không có $\bot$ nào cho ra Fenchel" ở Phần V, viết lại dưới dạng cấu trúc thuần túy: bất biến-dịch-chuyển vs. song-tuyến-tính-thật-sự là hai tính chất loại trừ nhau).

$$
\boxed{
\{c\text{ bilinear đối xứng thật sự}\}\ \cap\ \{c_h: h\text{ proper}\} = \varnothing\ \text{(trừ trường hợp suy biến)}.
}
$$

---

## PHẦN IV — Residual của Infimal Convolution như một Instance của Kernel Dịch chuyển

### IV.1. Nhận diện

$$
(f\multimap h)(z):=\sup_{y\in\operatorname{dom}f}\bigl(h(z+y)-f(y)\bigr)\ =\ f^{c_h}(z),\qquad c_h(y,z):=h(y+z).
$$

Đây là **cùng một đối tượng**, không phải tương tự: đặt $c(x,y):=h(y+x)$ vào định nghĩa $c$-conjugate tổng quát $f^c(y)=\sup_x(c(x,y)-f(x))$ cho đúng công thức residual, từng ký tự.

### IV.2. Định lý về tính lồi/đóng — nay là hệ quả tầm thường của Phần I

$h$ lsc $\Rightarrow f\multimap h$ đóng: đây chính là **Pb2** áp cho $c_h$, không cần chứng minh lại bằng epigraph riêng như v2 làm — nó tự động từ bảng I.2.

$h$ lồi $\Rightarrow f\multimap h$ lồi: đây là **Pb3**, và bảng I.2 đã chỉ ra **không tiên đề ICS nào cần Pb3**. Vậy điều kiện "$h$ lồi" trong định lý gốc của tài liệu residual chỉ cần thiết nếu ta muốn **thêm** kết luận lồi — bản thân cấu trúc đại số/Galois không đòi hỏi nó.

### IV.3. Định lý residuation = định lý adjunction tổng quát của $c$-conjugate

$$
f\square g\ge h\iff g\ge f\multimap h
$$
là trường hợp riêng (viết dưới dạng hàm thay vì tập) của Pa1+Pa2 áp cho $c_h$ — tức chính là adjunction Galois phản biến $f^c\le g\iff g^c\le f$ đã thiết lập ở Phần III của thảo luận trước, thu hẹp về kernel dịch chuyển.

### IV.4. Sup-convolution — hiệu đính lại claim ban đầu

Định nghĩa đối xứng gương của inf-convolution:
$$(p\boxplus q)(z):=\sup_y(p(y)+q(z-y))=-\bigl((-p)\square(-q)\bigr)(z).$$

**Kiểm lại (quan trọng, sửa sai lầm ban đầu):** sup-convolution **không** bảo toàn tính lồi nói chung — thử $p=q=x^2$ cho $p\boxplus q\equiv+\infty$. Định lý đúng là đối xứng gương:
$$p,q\ \text{lõm}\ \Rightarrow\ p\boxplus q\ \text{lõm}.$$

Công thức cầu nối: $f\multimap h=h\boxplus N(f)$ với $N(f)(t):=-f(-t)$. Ở đây $h$ lồi nhưng $N(f)$ (nếu $f$ lồi) lại **lõm** — nên $f\multimap h$ lồi là **ngoại lệ cấu trúc** (đến từ cơ chế "sup của họ tịnh tiến của $h$", tức chính Pb2/I.2, không phải một định lý tổng quát về $\boxplus$).

---

## PHẦN V — Negation kiểu Linear Logic: Dualizing Element

### V.1. Cơ chế Girard (tổng quát, không cần $\bot$ là unit của $\otimes,\&,\oplus,\parr$)

Trong một quantale/Girard quantale $(Q,\preceq,\otimes,\multimap)$, với **bất kỳ** $\bot\in Q$:
$$a^\bot:=a\multimap\bot,\qquad j(a):=a^{\bot\bot}\ \text{luôn là nucleus}.$$
Trong linear logic cổ điển, quy ước $\bot=$ unit của $\parr$ chỉ là **một lựa chọn**, không phải yêu cầu cấu trúc.

### V.2. Áp dụng: $\bot=h$

Chọn $\bot=h$ (proper, lsc, không hằng $\pm\infty$) trong quantale $(\overline{\mathbb R}^X,\square,\multimap)$:
$$f^\bot=f\multimap h=f^{c_h}\quad(\text{IV.1}),\qquad \operatorname{epi}(f^\bot)=(\operatorname{epi}f)^{*_{c_h}}\quad(\text{Phần I}).$$

**Ba tầng hội tụ về một điểm:** negation-linear-logic ($\bot=h$) = $h$-conjugate = $*_{c_h}$-polar hình học.

### V.3. So sánh các lựa chọn $\bot$ (bảng tổng hợp, thay Mục 4.3 của thảo luận trước)

| $\bot$ | $f^\bot$ | Suy biến? | Vì sao |
|---|---|---|---|
| $\top$ | $\equiv\top$ | Có, toàn phần | $\top$ là phần tử hấp thụ của $\square$ |
| $e=\delta_{\{0\}}$ | $\equiv+\infty$ trừ domain 1 điểm | Gần như hoàn toàn | domain của residual quá hẹp |
| $-\delta_{\{0\}}$ | $N(f)=-f(-\cdot)$ | Không suy biến, nhưng **nông** | involutive toàn phần, chỉ phản xạ-đổi dấu, lồi$\leftrightarrow$lõm |
| $h$ proper lsc, $\ne$ hằng | $f\multimap h=f^{c_h}$ | Không suy biến, **có nội dung hình học thật** | sinh lớp $h$-lồi, số Pa2 miễn phí (đối xứng của $c_h$) |
| bất kỳ $\bot\in\overline{\mathbb R}^X$ | — | Fenchel **không bao giờ** đạt được | chứng minh chặt III.3/Phần V.4 |

### V.4. Vì sao Fenchel không phải instance của $(\cdot)\multimap\bot$

Giả sử $f\multimap\bot=f^*$ với $\bot\in\overline{\mathbb R}^X$ nào đó. Lấy $f=\delta_{\{y_0\}}$: $\bot(z+y_0)=\langle z,y_0\rangle\ \forall z$, tức $\bot(w)=\langle w,y_0\rangle-\|y_0\|^2$ phải đúng với **mọi** $y_0$ — mâu thuẫn (ví dụ $X=\mathbb R$: $y_0=1,z=0\Rightarrow\bot(1)=0$; $y_0=2,z=-1\Rightarrow\bot(1)=-2$).

$$\boxed{\nexists\,\bot\in\overline{\mathbb R}^X:\ (\cdot)\multimap\bot=(\cdot)^*.}$$

Đây là **cùng một mâu thuẫn cấu trúc** đã chỉ ra ở III.3 (bất biến-dịch-chuyển của $c_h$ vs. song-tuyến-tính-thật-sự của $\langle,\rangle$), chỉ viết lại dưới ngôn ngữ negation.

### V.5. Nơi Fenchel thật sự sống

Fenchel là $c$-conjugate với kernel **bilinear hai-không-gian** $c(x,y)=\langle x,y\rangle:X\times X^*\to\mathbb R$ — một Galois connection **giữa hai poset khác nhau** $\overline{\mathbb R}^X,\overline{\mathbb R}^{X^*}$, không phải nucleus tự-đối-ngẫu một-không-gian của quantale $\square$. Định lý Fenchel–Moreau ($f^{**}=f\iff f$ lồi đóng proper) là đúng đối tác của Định lý 2.1.1 (involution) **ở tầng đó**, không phải tầng $\multimap$.

---

## PHẦN VI — Bản đồ toàn cảnh

| | Kernel dịch chuyển $c_h(x,y)=h(x+y)$ | Kernel bilinear $\langle x,y\rangle$ |
|---|---|---|
| Sống ở | quantale nội tại $(\overline{\mathbb R}^X,\square,\multimap)$, $\bot=h$ | Galois 2-poset $\overline{\mathbb R}^X\leftrightarrow\overline{\mathbb R}^{X^*}$ |
| Đối xứng | Tự động, mọi $h$ | Phải kiểm (đúng, nhờ song tuyến tính) |
| Pb2 (lsc) | Cần $h$ lsc | Tự động (liên tục hữu hạn chiều) |
| Pb3 (lồi) | Cần, nhưng **không dùng ở Sec 4** | Tự động (affine), cũng không dùng |
| Unit $e_\oplus$ sống khi | $\sup_X h<\infty$ | Luôn (điểm neo $y=0$) |
| Bất biến dịch chuyển | Có (đặc trưng cấu trúc) | Không |
| Phần tử đóng ($f^{\bot\bot}=f$) | Lớp hàm $h$-lồi | Lớp hàm lồi đóng cổ điển (Fenchel–Moreau) |
| Liên hệ giải tích | Residual của inf-convolution | Fenchel conjugate cổ điển |

**Kết luận tổng thể của bản cải tổ:** tính tiên đề của polar sinh từ kernel không nằm ở dạng cụ thể của $c$ mà ở **hai điều kiện tối giản** — đối xứng (cho Pa2/involution) và nửa liên tục dưới riêng biến (cho Pb2/đóng) — trong khi tính lồi (Pb3) và dạng bilinear cụ thể của $\langle\cdot,\cdot\rangle$ chỉ là **thuộc tính phụ tùy** của một điểm đặc biệt (dot product) trong không gian kernel rộng hơn nhiều, nơi residual của infimal convolution (kernel dịch chuyển) chiếm một góc khác, tách biệt về cấu trúc nhưng cùng tuân một định lý tiên đề duy nhất.

---

## Phụ lục — Câu hỏi mở cho các bản sau

1. Điều kiện chính xác (không chỉ đủ mà cần-và-đủ) để $\mathbb X_c$ khác $\{\varnothing,\overline X\}$ (không suy biến hoàn toàn) với kernel dịch chuyển — mối liên hệ với $\inf_X h$ song song với $\sup_X h$ đã xét ở Phần II.1?
2. Có họ kernel thứ ba (ngoài bilinear và dịch chuyển) thỏa đối xứng + lsc riêng biến, mà không thuộc cả hai họ đã biết? (vd. $c(x,y)=-\|x-y\|_p^p$ với $p\ne2$ — kiểm lại đối xứng, lsc, và tính "bất biến dịch chuyển" có giữ được không.)
3. Vai trò của Pb3 (bị bỏ hoàn toàn ở Sec 4) trong việc bắc cầu ngược sang ngôn ngữ hàm lồi cổ điển — cần chính xác hóa ranh giới giữa "ICS đại số" và "giải tích lồi cổ điển".
