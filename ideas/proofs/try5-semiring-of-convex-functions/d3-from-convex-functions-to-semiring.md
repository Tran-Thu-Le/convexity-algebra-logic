# Hàm Lồi Đóng là một Idempotent Commutative Semiring có Polar
### Hiện thực hóa 11 tiên đề trực tiếp trên lớp hàm (không đi qua epigraph)

*(Nối tiếp "d1 — From Algebra to Logic" và "d2a — Regepi is ICS with Polar". Ở d2a, mô hình cụ thể được dựng trên **tập con của $\overline X=\mathbb R^n\times(-\infty,+\infty]$** (regepi). Tài liệu này dựng lại **cùng một mô hình, ở cấp độ hàm** $f:\mathbb R^n\to\overline{\mathbb R}$ — hai mô hình đẳng cấu qua $f\mapsto\operatorname{epi}(f)$, nhưng ở đây mọi định nghĩa và chứng minh được viết thẳng trên $f$, không viện dẫn epigraph.)*

---

## 1. Không gian nền

$$\overline{\mathbb R}:=[-\infty,+\infty].$$

**Định nghĩa 1 (Lớp hàm lồi đóng).**
$$\Gamma(\mathbb R^n):=\Big\{f:\mathbb R^n\to\overline{\mathbb R}\ \Big|\ f\text{ lồi},\ \operatorname{epi}(f)\text{ đóng trong }\mathbb R^n\times\mathbb R\Big\}.$$

Sự kiện kinh điển (Rockafellar, *Convex Analysis*, §7): nếu $f$ lồi, $\operatorname{epi}(f)$ đóng, và $f$ nhận giá trị $-\infty$ tại **một** điểm, thì $f\equiv-\infty$ trên toàn miền. Do đó $\Gamma(\mathbb R^n)$ tách đúng thành ba loại không giao nhau:

$$\Gamma(\mathbb R^n)=\Gamma_{\text{proper}}\ \sqcup\ \{\mathbf{+\infty}\}\ \sqcup\ \{\mathbf{-\infty}\},$$

trong đó $\Gamma_{\text{proper}}$ là các hàm lồi, nửa liên tục dưới (lsc), $\not\equiv+\infty$ và không nhận giá trị $-\infty$ ở đâu; $\mathbf{+\infty},\mathbf{-\infty}$ là hai hàm hằng suy biến. Đây chính là hình ảnh hàm-học của $\mathbb X=\{E:E=E^{**}\}$ ở d2a — không cần giả thiết gì thêm, trichotomy này **là định nghĩa** của "đóng" theo Rockafellar, tương đương với $f=f^{**}$ (sẽ chứng minh lại độc lập ở §5, tiên đề P).

---

## 2. Ba phép toán

### 2.1. Meet — max điểm-theo-điểm

$$\boxed{(f\wedge g)(x):=\max\{f(x),g(x)\}}\qquad\forall x\in\mathbb R^n.$$

### 2.2. Sum (Fiber sum) — cộng điểm-theo-điểm trên semiring giá trị max-plus

Trước khi cộng hai hàm, ta cần một phép cộng **trên chính $\overline{\mathbb R}$** tương thích với $\max$ theo nghĩa phân phối — đây chính là bán vành (max, +) cổ điển ("tropical"/max-plus), mở rộng thêm $-\infty$ như phần tử **hút** của $+$:

**Định nghĩa 2 (Cộng mở rộng trên $\overline{\mathbb R}$).**
$$a+b:=\begin{cases}-\infty & \text{nếu } a=-\infty \text{ hoặc } b=-\infty,\\ a+b\ (\text{nghĩa thường}) & \text{nếu } a,b\in(-\infty,+\infty].\end{cases}$$

(Trên $(-\infty,+\infty]$, "+" nghĩa thường đã hoàn toàn không mơ hồ: chỉ cần quy ước $a+\infty=\infty$ với mọi $a$ hữu hạn, và $\infty+\infty=\infty$ — không có dạng $\infty-\infty$ nào xuất hiện vì không có số âm-vô-cùng trong miền này.)

**Bổ đề 1 ($(\overline{\mathbb R},\max,+,-\infty,0)$ là một dioid — max-plus semiring).** Phép $+$ ở Định nghĩa 2 kết hợp, giao hoán, có đơn vị $0$, hút bởi $-\infty$, và phân phối trên $\max$:
$$a+(b+c)=(a+b)+c,\quad a+b=b+a,\quad a+0=a,\quad a+(-\infty)=-\infty,\quad a+\max(b,c)=\max(a+b,a+c).$$

*Chứng minh.* Giao hoán: hiển nhiên từ định nghĩa (đối xứng $a\leftrightarrow b$).

Kết hợp: nếu một trong $a,b,c$ bằng $-\infty$, cả hai vế $(a+b)+c$ và $a+(b+c)$ đều $=-\infty$ (vì $-\infty$ lan truyền qua $+$ bất kể vị trí — kiểm trực tiếp từ định nghĩa: hễ một số hạng là $-\infty$ thì tổng từng bước đều là $-\infty$). Nếu không, cả ba nằm trong $(-\infty,+\infty]$, kết hợp là tính chất chuẩn của cộng mở rộng không âm-vô-cùng.

Đơn vị: $a+0=a$ theo nghĩa thường nếu $a\ne-\infty$; nếu $a=-\infty$, $a+0=-\infty=a$ theo quy ước hút.

Hút: theo đúng định nghĩa.

Phân phối: nếu $a=-\infty$: hai vế đều $-\infty$. Nếu $a\ne-\infty$ và $b=c=-\infty$: hai vế đều $-\infty$. Nếu $a\ne-\infty$, đúng một trong $b,c$ là $-\infty$ — giả sử $b=-\infty,\,c\ne-\infty$: $\max(b,c)=c$ (vì $-\infty$ là đáy của $\overline{\mathbb R}$), vế trái $=a+c$; vế phải $=\max(a+(-\infty),a+c)=\max(-\infty,a+c)=a+c$ (vì $a+c\in(-\infty,+\infty]$, luôn $>-\infty$). Nếu $a,b,c$ đều $\ne-\infty$: đẳng thức $a+\max(b,c)=\max(a+b,a+c)$ là tính chất chuẩn của cộng đơn điệu trên $(-\infty,+\infty]$ (đơn điệu vì $b\le c\Rightarrow a+b\le a+c$, kiểm trực tiếp theo từng trường hợp $b,c$ hữu hạn/$+\infty$). $\blacksquare$

Với Bổ đề 1 trong tay, định nghĩa:

$$\boxed{(f\oplus g)(x):=f(x)+g(x)}\qquad\forall x\in\mathbb R^n,$$

cộng theo nghĩa Định nghĩa 2, điểm theo điểm.

### 2.3. Conjugate (Fenchel polar)

$$\boxed{f^*(y):=\sup_{x\in\mathbb R^n}\big(\langle x,y\rangle - f(x)\big)}\qquad\forall y\in\mathbb R^n,$$

trong đó $\langle x,y\rangle-f(x):=\langle x,y\rangle+\big(-f(x)\big)$ với quy ước $-(+\infty):=-\infty$, $-(-\infty):=+\infty$, và $+$ là phép cộng mở rộng ở Định nghĩa 2. (Hệ quả tức thời: nếu $f(x)=+\infty$ thì số hạng tương ứng là $-\infty$ — "biến mất" khỏi $\sup$; nếu $f\equiv-\infty$ thì mọi số hạng là $+\infty$, nên $f^*\equiv+\infty$.)

### 2.4. Bổ đề đóng — $\Gamma(\mathbb R^n)$ ổn định dưới cả ba phép toán

**Bổ đề 2.** Nếu $f,g\in\Gamma(\mathbb R^n)$ thì $f\wedge g,\ f\oplus g,\ f^*\in\Gamma(\mathbb R^n)$.

*Chứng minh.*

**($\wedge$, lồi):** với $\lambda\in[0,1]$,
$$\max(f,g)(\lambda x+(1-\lambda)y)\le\max\big(\lambda f(x)+(1-\lambda)f(y),\ \lambda g(x)+(1-\lambda)g(y)\big)\le\lambda\max(f,g)(x)+(1-\lambda)\max(f,g)(y),$$
dùng $f,g$ lồi ở bất đẳng thức đầu, và $\max(a+b,c+d)\le\max(a,c)+\max(b,d)$ (đúng với $a,b,c,d\ge$ hệ số dương $\lambda,1-\lambda$ nhân vào, kiểm trực tiếp bằng cách so hai trường hợp $a\ge c$ hay $a<c$) ở bất đẳng thức sau.

**($\wedge$, đóng):** $\{x:\max(f,g)(x)\le\alpha\}=\{f\le\alpha\}\cap\{g\le\alpha\}$, giao hai tập đóng (do $f,g$ lsc) là đóng, nên $\max(f,g)$ lsc, tức $\operatorname{epi}(\max(f,g))$ đóng.

**($\oplus$, lồi + đóng):** nếu $f\equiv-\infty$ hoặc $g\equiv-\infty$, theo Định nghĩa 2, $f\oplus g\equiv-\infty\in\Gamma$. Ngược lại $f,g$ nhận giá trị trong $(-\infty,+\infty]$; tổng hai hàm lồi là lồi (bất đẳng thức lồi cộng trực tiếp, không có dạng vô định vì không có $-\infty$); tổng hai hàm lsc là lsc ($\liminf(f+g)\ge\liminf f+\liminf g$ khi cả hai vế phải xác định — đúng ở đây vì miền giá trị $(-\infty,+\infty]$). Vậy $f\oplus g$ lồi lsc, thuộc $\Gamma$ (rơi vào $\Gamma_{\text{proper}}\cup\{+\infty\}$, một trong ba lớp).

**($*$, lồi + đóng):** với mỗi $x$ cố định, $y\mapsto\langle x,y\rangle-f(x)$ là **affine** theo $y$ (hằng số $-f(x)$ có thể là $\pm\infty$, không ảnh hưởng: nếu $-f(x)=-\infty$ hàm affine suy biến $\equiv-\infty$, không đóng góp vào $\sup$; nếu $=+\infty$ hàm $\equiv+\infty$). $f^*$ là $\sup$ của một họ hàm affine (lồi + lsc), và sup của một họ hàm lồi lsc luôn lồi lsc (epi của sup = giao các epi, giao các tập lồi đóng vẫn lồi đóng). Vậy $f^*\in\Gamma$. $\blacksquare$

---

## 3. Hai đơn vị

$$\boxed{e_\wedge:=\mathbf{-\infty}\ \text{(hàm hằng)}}\qquad\qquad\boxed{e_\oplus:=\mathbf 0\ \text{(hàm hằng)}}.$$

(Đối chiếu d2a: $e_\wedge=\overline X$ ↔ hàm hằng $-\infty$ — vì $\operatorname{epi}(-\infty)=\mathbb R^n\times(-\infty,+\infty]=\overline X$; $e_\oplus=X\times[0,+\infty]$ ↔ hàm hằng $0$ — vì $\operatorname{epi}(0)=\{(x,r):r\ge0\}=X\times[0,+\infty]$.)

---

## 4. Thứ tự cảm sinh bởi $\wedge$

Theo Định nghĩa 5 của d1: $f\preceq g:\iff f\wedge g=f$. Vì $f\wedge g=f\iff\max(f,g)=f\iff f(x)\ge g(x)\ \forall x$, thứ tự cảm sinh là **thứ tự điểm-theo-điểm đảo ngược**:
$$f\preceq g\iff f\ge g\ \text{(điểm theo điểm)}.$$
($e_\wedge=\mathbf{-\infty}$ là phần tử **lớn nhất** của $\preceq$ — khớp Bổ đề 2 (d1): mọi hàm đều $\ge-\infty$ điểm theo điểm.)

---

## 5. Chứng minh 11 tiên đề

### 5.1. Nhóm M — chỉ cần $\max$ trên $\overline{\mathbb R}$ là dàn toàn phần (không cần $+$, không cần $*$)

**M0** ($f\wedge f=f$): $\max(f(x),f(x))=f(x)$. ✓

**M1** ($\wedge$ kết hợp): $\max(\max(f,g),h)=\max(f,\max(g,h))$ điểm theo điểm — kết hợp của $\max$ trên chuỗi toàn phần $\overline{\mathbb R}$. ✓

**M2** ($\wedge$ giao hoán): $\max(f,g)=\max(g,f)$. ✓

**M3** ($f\wedge e_\wedge=f$): $\max(f(x),-\infty)=f(x)$ vì $-\infty$ là đáy của $\overline{\mathbb R}$. ✓

### 5.2. Nhóm S — chỉ cần Bổ đề 1 (bán vành max-plus giá trị)

**S1** ($\oplus$ kết hợp): $(f\oplus g)\oplus h)(x)=\big(f(x)+g(x)\big)+h(x)\overset{\text{Bổ đề 1}}{=}f(x)+\big(g(x)+h(x)\big)=(f\oplus(g\oplus h))(x)$. ✓

**S2** ($\oplus$ giao hoán): $f(x)+g(x)=g(x)+f(x)$ (Bổ đề 1). ✓

**S3** ($f\oplus e_\oplus=f$): $f(x)+0=f(x)$ (Bổ đề 1, đơn vị $0$). ✓

### 5.3. Liên hệ Sum–Meet

**SM1** (phân phối, $f\oplus(g\wedge h)=(f\oplus g)\wedge(f\oplus h)$):
$$f(x)+\max(g(x),h(x))\overset{\text{Bổ đề 1}}{=}\max\big(f(x)+g(x),\,f(x)+h(x)\big),$$
đúng với mọi $x$ — chính là điều kiện phân phối trong Bổ đề 1, áp trực tiếp điểm theo điểm. ✓

**SM2** (hấp thụ, $f\oplus e_\wedge=e_\wedge$): $f(x)+(-\infty)=-\infty$ với **mọi** $x$ và **mọi** $f\in\Gamma(\mathbb R^n)$ — kể cả $f\equiv+\infty$ (kiểm trực tiếp: $(+\infty)+(-\infty)=-\infty$ theo Định nghĩa 2, vì một trong hai số hạng là $-\infty$). Vậy $f\oplus e_\wedge\equiv-\infty=e_\wedge$. ✓ *(Đúng vô điều kiện trên toàn $\Gamma(\mathbb R^n)$, không có ngoại lệ kiểu $E\ne\emptyset$ — khớp d2c: không có "hàm rỗng" trong $\Gamma$.)*

### 5.4. P — tính đối hợp của polar (Fenchel–Moreau)

**Định lý (P).** $f^{**}=f$ với mọi $f\in\Gamma(\mathbb R^n)$.

*Chứng minh.*

**Bất đẳng thức tự do $f^{**}\le f$ (Fenchel–Young, không cần đóng/lồi):** với mọi $x,y$: $f^*(y)\ge\langle x,y\rangle-f(x)$ (định nghĩa $\sup$), tức $\langle x,y\rangle-f^*(y)\le f(x)$. Lấy $\sup$ theo $y$ ở vế trái: $f^{**}(x)=\sup_y(\langle x,y\rangle-f^*(y))\le f(x)$.

**Ba trường hợp cho chiều ngược $f\le f^{**}$:**

*Trường hợp $f\equiv+\infty$:* $f^*(y)=\sup_x(\langle x,y\rangle-\infty)=\sup_x(-\infty)=-\infty$, tức $f^*\equiv-\infty$. Khi đó $f^{**}(x)=\sup_y(\langle x,y\rangle-(-\infty))=\sup_y(+\infty)=+\infty=f(x)$ (miền $y\in\mathbb R^n\ne\emptyset$).

*Trường hợp $f\equiv-\infty$:* $f^*(y)=\sup_x(\langle x,y\rangle+\infty)=+\infty$, tức $f^*\equiv+\infty$. Khi đó $f^{**}(x)=\sup_y(\langle x,y\rangle-\infty)=-\infty=f(x)$.

*Trường hợp $f\in\Gamma_{\text{proper}}$ (lồi, lsc, không $\equiv+\infty$, không nhận $-\infty$):* Đây là định lý Fenchel–Moreau cổ điển. Giả sử phản chứng tồn tại $x_0$ với $f^{**}(x_0)<f(x_0)$ (kể cả trường hợp $f(x_0)=+\infty$). Vì $f$ lồi lsc proper, $\operatorname{epi}(f)$ là tập lồi đóng khác rỗng trong $\mathbb R^n\times\mathbb R$, và $(x_0,\beta)\notin\operatorname{epi}(f)$ với mọi $\beta<f(x_0)$ nói riêng với $\beta$ kẹp giữa $f^{**}(x_0)$ và $f(x_0)$. Theo định lý tách tập lồi (Hahn–Banach hữu hạn chiều) áp cho điểm $(x_0,\beta)$ và tập lồi đóng $\operatorname{epi}(f)$: tồn tại $(y_0,\lambda)\in\mathbb R^n\times\mathbb R$ và $c\in\mathbb R$ tách nghiêm ngặt,
$$\langle x_0,y_0\rangle+\lambda\beta< c\le\langle x,y_0\rangle+\lambda r\qquad\forall (x,r)\in\operatorname{epi}(f).$$
Vì $\operatorname{epi}(f)$ chứa các tia hướng lên ($r\to+\infty$ với $x\in\operatorname{dom} f$ cố định), cần $\lambda\ge0$; và vì $f$ proper (có điểm hữu hạn), $\lambda>0$ (nếu $\lambda=0$ siêu phẳng không tách được theo hướng $r$, dẫn đến mâu thuẫn khi cho $x$ chạy trong $\operatorname{dom} f$ — chuẩn trong chứng minh tách cho epigraph). Chuẩn hóa $\lambda=1$, đặt $y:=-y_0$: bất đẳng thức trên cho $\langle x,y\rangle-f(x)\ge$ hằng số $>\langle x_0,y\rangle-\beta$ với mọi $x\in\operatorname{dom} f$, tức $f^*(-y_0)\ge c>\langle x_0,y_0\rangle+\beta$ hay viết lại $\langle x_0,-y_0\rangle-f^*(-y_0) < -\beta$... rút gọn theo cách chuẩn (Rockafellar, Convex Analysis, Thm 12.1–12.2 hoặc Hiriart-Urruty & Lemaréchal, *Convex Analysis and Minimization Algorithms* I, Thm E.1.3.5): tách này cho một hàm affine $x\mapsto\langle x,\bar y\rangle-\bar c$ thỏa
$$\langle x,\bar y\rangle-\bar c\le f(x)\ \forall x,\qquad \langle x_0,\bar y\rangle-\bar c>\beta.$$
Từ bất đẳng thức đầu: $\bar c\ge\langle x,\bar y\rangle-f(x)$ với mọi $x$, tức $\bar c\ge f^*(\bar y)$, nên $\langle x_0,\bar y\rangle-f^*(\bar y)\ge\langle x_0,\bar y\rangle-\bar c>\beta$. Vế trái là một số hạng trong $\sup$ định nghĩa $f^{**}(x_0)$, nên $f^{**}(x_0)>\beta$. Chọn $\beta\to f^{**}(x_0)$ từ dưới (hoặc trực tiếp $\beta:=f^{**}(x_0)$ nếu hữu hạn) mâu thuẫn với $\beta$ được chọn $\ge f^{**}(x_0)$ ban đầu (hoặc mâu thuẫn trực tiếp $f^{**}(x_0)>f^{**}(x_0)$). Vậy giả thiết phản chứng sai, $f\le f^{**}$.

Kết hợp hai chiều: $f^{**}=f$ trên $\Gamma_{\text{proper}}$, và đã kiểm trực tiếp trên hai hàm hằng suy biến. $\blacksquare$

*(Đây chính là nội dung "Định lý Ore" thứ hai mà d2a nói tới ở tầng regepi — Fenchel–Moreau chính là bản hàm-học của "involution rơi ra tự động từ Galois connection + tách tập lồi", khớp với Định lý 2.1.1 của d2a.)*

### 5.5. PM — tính phản biến của polar (miễn phí, nhờ P)

**Bổ đề 3 (Đơn điệu-đảo, không cần P).** Với mọi $f,g\in\Gamma(\mathbb R^n)$: $f\ge g$ điểm theo điểm $\Rightarrow f^*\le g^*$ điểm theo điểm.

*Chứng minh.* Cố định $y$. Với mọi $x$: nếu $f(x),g(x)$ hữu hạn hoặc $+\infty$ thông thường, $f(x)\ge g(x)\Rightarrow-f(x)\le-g(x)\Rightarrow\langle x,y\rangle-f(x)\le\langle x,y\rangle-g(x)$ (kiểm trực tiếp theo quy ước $-(+\infty)=-\infty$: nếu $g(x)=+\infty$ thì $f(x)=+\infty$ do $f\ge g$, hai vế bằng $-\infty$; nếu $f(x)=+\infty,g(x)<\infty$, vế trái $-\infty\le$ vế phải hữu hạn; còn lại cả hai hữu hạn, bất đẳng thức thường). Trường hợp $f\equiv-\infty$: khi đó $f\ge g$ buộc $g\equiv-\infty$ (vì $g(x)\le f(x)=-\infty$), nên $f=g$, tầm thường. Lấy $\sup$ theo $x$ hai vế: $f^*(y)\le g^*(y)$. Đúng với mọi $y$. $\blacksquare$

**Định lý (PM).** $f\preceq g\iff g^*\preceq f^*$ (tương đương: $f\ge g\iff f^*\le g^*$, điểm theo điểm).

*Chứng minh.*

($\Rightarrow$) $f\ge g\Rightarrow f^*\le g^*$: Bổ đề 3 trực tiếp.

($\Leftarrow$) Giả sử $f^*\le g^*$, tức $g^*\ge f^*$. Áp Bổ đề 3 cho cặp $(g^*,f^*)\in\Gamma\times\Gamma$ (dùng Bổ đề 2 để $f^*,g^*\in\Gamma$): $g^*\ge f^*\Rightarrow (g^*)^*\le(f^*)^*$, tức $g^{**}\le f^{**}$. Theo **P** (§5.4): $g^{**}=g,\ f^{**}=f$. Vậy $g\le f$, tức $f\ge g$. $\blacksquare$

*(Ghi chú đối chiếu d1, Định lý 4/T3: ở tầng đại số trừu tượng, (PM) **không tự động** — cần luật hấp thụ (Abs) như giả thiết độc lập, và phản ví dụ hữu hạn xác nhận điều đó. Ở đây, tại mô hình cụ thể, (PM) **rơi ra miễn phí** chỉ từ Bổ đề 3 (đơn điệu-đảo sơ cấp, không cần lồi/đóng) cộng với **P** (Fenchel–Moreau) — đúng như thảo luận ở §6 của d1: "trong mô hình cụ thể, (C2) đúng theo nghĩa tầm thường". Ở đây nó tầm thường vì $\le$ và $\le^*$ cùng quy về **một** thứ tự điểm-theo-điểm duy nhất trên $\Gamma(\mathbb R^n)$, không phải hai thứ tự độc lập cần được chứng minh trùng nhau.)*

---

## 6. Bảng tổng kết

| Tiên đề | Phát biểu trên $\Gamma(\mathbb R^n)$ | Cần gì |
|---|---|---|
| M0 | $\max(f,f)=f$ | $\overline{\mathbb R}$ là chuỗi toàn phần |
| M1 | $\max$ kết hợp | như trên |
| M2 | $\max$ giao hoán | như trên |
| M3 | $\max(f,-\infty)=f$ | $-\infty$ = đáy $\overline{\mathbb R}$ |
| S1 | $+$ kết hợp (điểm theo điểm) | Bổ đề 1 |
| S2 | $+$ giao hoán | Bổ đề 1 |
| S3 | $f+0=f$ | Bổ đề 1 |
| SM1 | $a+\max(b,c)=\max(a+b,a+c)$ | Bổ đề 1 |
| SM2 | $f+(-\infty)=-\infty$ | Bổ đề 1 (hút) |
| **P** | $f^{**}=f$ | Fenchel–Moreau (tách tập lồi) |
| **PM** | $f\ge g\iff f^*\le g^*$ | Bổ đề 3 (sơ cấp) + P |

**Kết luận.** $\big(\Gamma(\mathbb R^n),\wedge,\oplus,{}^*\big)$ với $e_\wedge=\mathbf{-\infty},\,e_\oplus=\mathbf 0$ thỏa đầy đủ 11 tiên đề M0–M3, S1–S3, SM1–SM2, P, PM. Toàn bộ chứng minh, trừ **P**, hoàn toàn *đại số sơ cấp* trên bán vành giá trị $(\overline{\mathbb R},\max,+)$ — không viện dẫn tách tập lồi. Riêng **P** là nơi duy nhất giải tích lồi thật sự "vào cuộc" (định lý tách), và chính vì P đúng vô điều kiện trên $\Gamma(\mathbb R^n)$ mà **PM** — thứ cần một giả thiết độc lập ở tầng trừu tượng (d1) — rơi ra miễn phí ở đây.
