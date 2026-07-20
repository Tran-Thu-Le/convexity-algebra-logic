# PICS: Kiến Trúc, Mô Hình Hàm Lồi Đóng, và Hai Định Lý Bất Khả Thi Residuation

*(Tổng hợp — nối tiếp d1 "From Algebra to Logic", d2a/d2c "Regepi is ICS with Polar", d3 "Hàm Lồi Đóng là ICS+Polar".)*

---

## Sec 1. Kiến trúc PICS — 11 tiên đề và các ví dụ

### 1.1. Định nghĩa

**PICS** (Polar Idempotent Commutative Semiring) là cấu trúc $(X,\wedge,\oplus,{}^*,e_\wedge,e_\oplus)$ thỏa 11 tiên đề:

| Nhóm    | Tên | Phát biểu                                                                                              |
| ------- | --- | ------------------------------------------------------------------------------------------------------ |
| Meet    | M0  | $a\wedge a=a$                                                                                          |
|         | M1  | $a\wedge(b\wedge c)=(a\wedge b)\wedge c$                                                               |
|         | M2  | $a\wedge b=b\wedge a$                                                                                  |
|         | M3  | $a\wedge e_\wedge=a$                                                                                   |
| Sum     | S1  | $a\oplus(b\oplus c)=(a\oplus b)\oplus c$                                                               |
|         | S2  | $a\oplus b=b\oplus a$                                                                                  |
|         | S3  | $a\oplus e_\oplus=a$                                                                                   |
| Liên hệ | SM1 | $a\oplus(b\wedge c)=(a\oplus b)\wedge(a\oplus c)$                                                      |
|         | SM2 | $a\oplus e_\wedge=e_\wedge$                                                                            |
| Polar   | P   | $a^{**}=a$                                                                                             |
|         | PM  | $a\wedge b=a\iff b^*\wedge a^*=b^*$ (viết gọn: $a\le b\iff b^*\le a^*$, với $a\le b:\iff a\wedge b=a$) |

Thứ tự cảm sinh $\le$ đặt $e_\wedge$ làm phần tử **lớn nhất**. Toán tử dẫn xuất $a\vee b:=(a^*\wedge b^*)^*$, $e_\vee:=e_\wedge^*$; theo Định lý T3 (d1), PM $\iff$ luật hấp thụ $a\wedge(a\vee b)=a,\ a\vee(a\wedge b)=a$, nên khi PM đúng, $(X,\wedge,\vee)$ là một **lattice bị chặn** ($e_\wedge$ = đỉnh, $e_\vee=e_\wedge^*$ = đáy).

### 1.2. Ví dụ 1 — Boolean algebra

$(B,\wedge,\vee,\neg,0,1)$ Boolean algebra bất kỳ: đặt $\oplus:=\vee$, $e_\oplus:=0$, $e_\wedge:=1$, $(-)^*:=\neg$.

- M0–M3, S1–S3: tiên đề lattice/monoid chuẩn của Boolean algebra.
- SM1: luật phân phối $\vee$ trên $\wedge$ — tiên đề Boolean chuẩn: $a\vee(b\wedge c)=(a\vee b)\wedge(a\vee c)$.
- SM2: $a\vee 1=1$ — hiển nhiên ($1$ là đỉnh).
- P: $\neg\neg a=a$ — tiên đề Boolean chuẩn.
- PM: $a\wedge b=a\Rightarrow \neg b\wedge\neg a=\neg b$ — chính là luật De Morgan/phản đảo, hệ quả trực tiếp của Boolean algebra.

Boolean algebra là mô hình **hữu hạn, rời rạc**, kiểm toàn bộ 11 tiên đề trong vài dòng — mỏ neo cụ thể nhất của PICS.

### 1.3. Ví dụ 2 — Girard quantale $\Rightarrow$ PICS

**Định nghĩa (Girard quantale, chuẩn — Yetter 1990, Rosenthal 1990/92; đối chiếu Galatos, *Residuated Lattices*, slide bài giảng).** Một *commutative Girard quantale* là $(Q,\le,\cdot,1,0)$ với:

- $(Q,\le)$ complete lattice;
- $(Q,\cdot,1)$ commutative monoid, $\cdot$ phân phối trên **mọi** sup: $a\cdot\bigvee_iб_i=\bigvee_i(a\cdot b_i)$;
- $0\in Q$ là **dualizing element**: đặt $\sim a:=a\backslash 0$ (residual, tồn tại tự động theo định lý hàm phụ trợ nhờ completeness+phân phối-sup), khi đó $\sim\sim a=a$ với mọi $a$.

**Mệnh đề.** Mọi commutative Girard quantale là một PICS, với $\wedge:=\vee_Q$ (join của lattice — *lưu ý đảo vai trò*, xem Nhận xét), $\oplus:=\cdot$, $e_\wedge:=$ đáy của $Q$ (đơn vị của $\vee_Q$), $e_\oplus:=1$, $(-)^*:=\sim(-)$.

*Chứng minh (phác).* M0–M3: $\vee_Q$ idempotent-commutative-associative với đơn vị là tiên đề complete lattice chuẩn. S1–S3: tiên đề monoid. SM1: trường hợp nhị phân của "phân phối trên mọi sup". SM2: hệ quả tự động khi đáy tồn tại — Jipsen–Tsinakis, *A Survey of Residuated Lattices*: "*If a residuated po-groupoid $P$ has a bottom element $0$... $x0=0=0x$*" — một **định lý**, không phải tiên đề, trong quantale. P: định nghĩa dualizing element. PM: hệ quả chuẩn của residuation + involution (đối ngẫu của Prop 2.1, Jipsen–Tsinakis). $\blacksquare$

**Nhận xét (đảo vai trò $\wedge/\vee$).** Quy ước PICS gọi $\wedge$ là phép **idempotent** mà $\oplus$ phân phối lên trên — khớp với $\vee$ (join) trong quy ước dioid/quantale chuẩn (nơi thứ tự $x\le y\iff x\vee y=y$, đáy $=$ đơn vị của $\vee$), không phải $\wedge$ nghĩa "giao" thông thường. Đây thuần túy là khác biệt đặt tên/quy ước dấu, không ảnh hưởng nội dung.

### 1.4. Ví dụ 3 — Involutive residuated lattice $\Rightarrow$ PICS

**Định nghĩa (Involutive residuated lattice — Galatos).** $L=(L,\wedge,\vee,\cdot,\backslash,/,1)$ residuated lattice ($ (L,\wedge,\vee)$ lattice, $(L,\cdot,1)$ monoid, $ab\le c\iff b\le a\backslash c\iff a\le c/b$ với mọi $a,b,c$), thêm hằng số $0$, đặt $\sim x:=x\backslash 0,\ -x:=0/x$, thỏa $\sim{-}x=x={-}\sim x$.

**Mệnh đề.** Mọi *commutative* involutive residuated lattice là một PICS (cùng cách dịch như 1.3, không cần completeness — chỉ cần lattice nhị phân + residuation nhị phân đủ cho SM1/SM2/PM ở mức hữu hạn).

*(Chứng minh song song 1.3, dùng Prop 2.1–2.2 của Jipsen–Tsinakis cho trường hợp không cần sup vô hạn.)*

### 1.5. Sơ đồ phân tầng

$$\text{involutive po-semigroup} \supset \underbrace{\text{involutive semiring}}_{\substack{\text{residuation}\\ \text{tồn tại, nhị phân}}} \supset \text{involutive residuated lattice} \supset \text{Girard quantale (complete)}$$

$$\text{Tất cả} \subset \textbf{PICS}$$

PICS là lớp **rộng nhất**: chỉ đòi hỏi PM (một điều kiện thứ tự thuần túy giữa $\le$ và $*$), không đòi residuation tồn tại. Ba ví dụ trên đều là mô hình PICS *giàu hơn* — chúng có residuation, PICS thì không bắt buộc.

---

## Sec 2. Họ hàm lồi đóng $\Gamma(\mathbb R^n)$ là một PICS

### 2.1. Không gian nền

$$\Gamma(\mathbb R^n):=\{f:\mathbb R^n\to\overline{\mathbb R}\mid f=f^{**}\}\quad(\text{bipolar-đóng}),$$

$$f^*(y):=\sup_x\big(\langle x,y\rangle-f(x)\big).$$

Theo Định lý Fenchel–Moreau (chứng minh: chiều $f^{**}\le f$ tự do từ Fenchel–Young; chiều ngược cần tách tập lồi, chỉ đúng khi $f$ **proper**), $\Gamma(\mathbb R^n)$ tách thành:
$$\Gamma(\mathbb R^n)=\underbrace{\Gamma_{\text{proper}}}_{\text{lồi, lsc, không }\equiv\pm\infty}\ \sqcup\ \{\mathbf{+\infty}\}\ \sqcup\ \{\mathbf{-\infty}\}.$$

*(Lưu ý: bipolar-đóng mạnh hơn hẳn "lồi + epigraph đóng tô-pô" — xem thảo luận riêng về phản ví dụ $f=\iota_{[0,1]\times\mathbb R}$-kiểu suy biến; ở đây $\Gamma(\mathbb R^n)$ được định nghĩa thẳng bằng bipolar để tránh mập mờ.)*

### 2.2. Ba phép toán, hai đơn vị

$$(f\wedge g)(x):=\max\{f(x),g(x)\},\qquad (f\oplus g)(x):=f(x)+g(x)\ \text{(cộng max-plus, }-\infty\text{ hút)},$$

$$e_\wedge:=\mathbf{-\infty},\qquad e_\oplus:=\mathbf 0.$$

Cộng max-plus: $a+b:=-\infty$ nếu $a=-\infty$ hoặc $b=-\infty$; ngược lại cộng thường trên $(-\infty,+\infty]$. Đây là bán vành giá trị $(\overline{\mathbb R},\max,+,-\infty,0)$ — dioid chuẩn (Bổ đề 1, d3).

**Bổ đề đóng.** $\Gamma(\mathbb R^n)$ ổn định dưới cả ba phép toán: max của hai hàm lồi-lsc là lồi-lsc; tổng hai hàm lồi-lsc là lồi-lsc (dùng quy ước hút cho $-\infty$); conjugate của một hàm bất kỳ luôn lồi-lsc (sup của họ affine).

### 2.3. Chứng minh 11 tiên đề — bảng compact

| Tiên đề | Nội dung mấu chốt | Cần gì |
|---|---|---|
| M0–M3 | $\max$ trên $\overline{\mathbb R}$ là chuỗi toàn phần, $-\infty$ đáy | Sơ cấp |
| S1–S3 | Bổ đề 1 (dioid max-plus): kết hợp, giao hoán, đơn vị $0$ | Sơ cấp |
| SM1 | $a+\max(b,c)=\max(a+b,a+c)$ | Bổ đề 1 |
| SM2 | $a+(-\infty)=-\infty$ mọi $a$, kể cả $a=+\infty$ | Bổ đề 1 (hút) |
| **P** | $f^{**}=f$ | **Fenchel–Moreau** — chỗ duy nhất cần tách tập lồi |
| **PM** | $f\ge g\iff f^*\le g^*$ | Bổ đề đơn điệu-đảo (sơ cấp) $+$ P |

*(Chứng minh đầy đủ, từng dòng: xem d3.)* Điểm cấu trúc quan trọng: **9/11 tiên đề thuần đại số sơ cấp** trên bán vành giá trị, không cần lồi/tách tập lồi gì cả; chỉ **P** cần Fenchel–Moreau thật sự, và **PM** thừa hưởng miễn phí từ P.

### 2.4. Kết luận Sec 2

$$\big(\Gamma(\mathbb R^n),\wedge,\oplus,{}^*\big)\ \text{là một PICS đầy đủ, với } e_\wedge=\mathbf{-\infty},\ e_\oplus=\mathbf 0.$$

---

## Sec 3. Hai định lý bất khả thi — Fenchel polar không sinh bởi residual

### 3.1. Định nghĩa chuẩn — negation sinh bởi residual

Theo lý thuyết residuated lattice/quantale (Sec 1.3–1.4), negation "đúng chuẩn" luôn có dạng $a^*:=a\multimap q$ cho một **hằng số đối ngẫu hóa** $q$ cố định, với residual $\multimap$ thỏa:
$$a\oplus b\preceq q\iff b\preceq a^*.$$

Câu hỏi: trên $\Gamma(\mathbb R^n)$, có tồn tại $q$ nào khiến Fenchel polar khớp đúng dạng này, với **một trong hai** phép nhân tự nhiên duy nhất tương thích với polar (Bổ đề 3, d1: $(f\oplus g)^*=f^*\square g^*$ và ngược lại) — $\oplus$ (tổng điểm-theo-điểm) hoặc $\square$ (inf-convolution)?

### 3.2. Định lý A — bất khả thi với $\oplus$

**Định lý A.** Không tồn tại $q\in\Gamma(\mathbb R^n)$ sao cho $a\oplus b\preceq q\iff b\preceq a^*$ đúng với mọi $a,b\in\Gamma(\mathbb R^n)$.

*Chứng minh.*

**Bước 1 (ép $q$ duy nhất).** Cố định $y_0\ne0$. Lấy $a:=\iota_{\{y_0\}}$ (nên $a^*(x)=\langle x,y_0\rangle$). Điều kiện thu về: $b(y_0)\ge q(y_0)\iff b(x)\ge\langle x,y_0\rangle\ \forall x$. Thử $b_1(x):=\langle x,y_0\rangle$ (vế phải đúng) $\Rightarrow q(y_0)\le\|y_0\|^2$. Thử $b_2(x):=\langle x,y_0\rangle-\varepsilon$ (vế phải sai, $\forall\varepsilon>0$) $\Rightarrow q(y_0)>\|y_0\|^2-\varepsilon$. Cho $\varepsilon\to0$: $q(y_0)=\|y_0\|^2$. Đúng $\forall y_0$ (kể cả $y_0=0$), nên $q=\|\cdot\|^2$ là ứng viên **duy nhất**.

**Bước 2 (loại chính $q=\|\cdot\|^2$).** Lấy $a:=\|\cdot\|^2,\ b:=\mathbf0$. Vế trái: $a(x)+0=\|x\|^2\ge q(x)=\|x\|^2$ — đúng. Vế phải cần $b\ge a^*$; nhưng $a^*(y)=\|y\|^2/4\ne0$ khi $y\ne0$, nên $b(y)=0\not\ge\|y\|^2/4$ — sai. Mâu thuẫn. $\blacksquare$

### 3.3. Định lý B — bất khả thi với $\square$ (inf-convolution)

Residual của $\square$ chỉ có một dạng khả dĩ (kernel dịch chuyển, hệ quả trực tiếp cấu trúc tịnh tiến của $\square$): $(f\multimap q)(x):=\sup_y[q(x+y)-f(y)]$.

**Định lý B.** Không tồn tại $q$ sao cho $f\multimap q=f^*$ với mọi $f\in\Gamma(\mathbb R^n)$.

*Chứng minh.*

**Bước 1.** Với $y_0$ tùy ý, lấy $f:=\iota_{\{y_0\}}$: $(f\multimap q)(x)=q(x+y_0)$, còn $f^*(x)=\langle x,y_0\rangle$. Đẳng thức đòi $q(x+y_0)=\langle x,y_0\rangle\ \forall x$. Đúng $\forall y_0$, nên $q(x+y)=\langle x,y\rangle\ \forall x,y$.

**Bước 2 (vô lý).** Cố định $z=x+y$: $q(z)=\langle x,z-x\rangle=\langle x,z\rangle-\|x\|^2$ phải là **hằng số theo $x$**. Lấy $x=tv,\ t\to\infty,\ v\ne0$: vế phải $\to-\infty$, trong khi $x=0$ cho vế phải $=0$. Mâu thuẫn. $\blacksquare$

> **Remark.** If the class of proper closed convex functions is enlarged by adjoining the improper function $+\infty$, then arbitrary joins are expected to exist. In this setting, the natural candidate for the residual associated with pointwise addition is the right adjoint
> $$f \multimap h
:=
\bigvee \{\, g : f+g \le h \,\}.
$$
> Moreover, Fenchel conjugation exchanges pointwise addition and infimal convolution,
> $$(f+g)^* = f^* \square g^*,
\qquad
(f \square g)^* = f^* + g^*,
$$
> while reversing the order. Consequently, the existence (or nonexistence) of a residual for one tensor is equivalent to that for the other. Therefore, it is sufficient to establish the impossibility of residuation for pointwise addition.
### 3.4. Hệ quả — PICS không tự động là Girard quantale, kể cả trên mô hình tự nhiên nhất

Ghép 3.2–3.3: với **cả hai** phép nhân duy nhất tương thích tự nhiên với polar trên $\Gamma(\mathbb R^n)$, Fenchel conjugate **không thể** là negation sinh bởi residuation theo đúng nghĩa chuẩn (Sec 1.3–1.4). Vậy:

$$\textbf{PICS}\ \not\Rightarrow\ \textbf{Girard quantale (cùng phép nhân)}.$$

Đây là một **kết quả độc lập tiên đề** (independence result), cùng tinh thần Định lý T3/(PM) của d1 (PM không tự động từ M+S+P), nhưng nâng lên một tầng: tính chất "residuation-compatible" không tự động từ 11 tiên đề PICS — và phản ví dụ không phải một bảng cộng hữu hạn nhân tạo (như Ví dụ 1, d1) mà là **mô hình quan trọng bậc nhất của giải tích lồi**.

### 3.5. Giới hạn phạm vi — cần ghi rõ khi trích dẫn

Hai định lý phủ đúng $\oplus$ và $\square$ — hai phép nhân **duy nhất** tương thích tự nhiên với cấu trúc polar đã cho (qua đẳng thức De Morgan trừu tượng, Bổ đề 3 d1: $(f\oplus g)^*=f^*\square g^*$ và ngược lại — không còn "phép nhân thứ ba" nào khớp polar theo cách tương tự). Kết quả **không** loại trừ mọi monoid giao hoán nhân tạo khác trên $\Gamma(\mathbb R^n)$ không liên hệ gì đến $*$ — nhưng đó cũng chính xác là phạm vi mọi phản biện nghiêm túc sẽ hỏi tới, nên giới hạn này không làm yếu kết quả trong thực tế.

---

## Kết luận chung

Ba tầng nội dung của tài liệu này khép lại một mạch lập luận đầy đủ:

1. **PICS** (Sec 1) là khung tiên đề rộng, chứa Boolean algebra, Girard quantale, involutive residuated lattice như các trường hợp riêng *giàu hơn* (có residuation).
2. **$\Gamma(\mathbb R^n)$** (Sec 2) là một mô hình PICS hợp lệ, xây dựng trực tiếp từ Fenchel conjugate — 9/11 tiên đề sơ cấp, chỉ P cần Fenchel–Moreau.
3. **Hai định lý bất khả thi** (Sec 3) chứng tỏ mô hình này **không** nâng cấp được thành Girard quantale bằng bất kỳ phép nhân tự nhiên nào tương thích với polar — PICS là khung *thực sự tổng quát hơn*, không chỉ về mặt hình thức tiên đề mà còn được minh chứng bằng một mô hình cụ thể, quan trọng, nơi khoảng cách ấy *có thật*.
