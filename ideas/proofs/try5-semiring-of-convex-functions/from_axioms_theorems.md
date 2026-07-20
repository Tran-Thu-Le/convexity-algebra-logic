# Polar Idempotent Commutative Semiring

## 1. Các toán tử nguyên thủy và hệ tiên đề

Cho $X$ là một tập, được trang bị ba toán tử nguyên thủy

$$
\wedge:X\times X\to X,\qquad
+:X\times X\to X,\qquad
(-)^*:X\to X,
$$

cùng hai phần tử phân biệt về vai trò

$$
e_{\wedge},\qquad e_{+}.
$$

Ta giả sử các tiên đề sau đúng với mọi $a,b,c\in X$.

### 1.1. Các tiên đề của meet

$$
\tag{M0} a\wedge a=a,
$$

$$
\tag{M1} a\wedge(b\wedge c)=(a\wedge b)\wedge c,
$$

$$
\tag{M2} a\wedge b=b\wedge a,
$$

$$
\tag{M3} a\wedge e_{\wedge}=a.
$$

### 1.2. Các tiên đề của sum

$$
\tag{S1} a+(b+c)=(a+b)+c,
$$

$$
\tag{S2} a+b=b+a,
$$

$$
\tag{S3} a+e_{+}=a.
$$

### 1.3. Các tiên đề liên hệ giữa sum và meet

$$
\tag{SM1}
a+(b\wedge c)=(a+b)\wedge(a+c),
$$

$$
\tag{SM2}
a+e_{\wedge}=e_{\wedge}.
$$

### 1.4. Các tiên đề của polar

$$
\tag{P}
a^{**}=a,
$$

$$
\tag{PM}
a\wedge b=a
\quad\Longleftrightarrow\quad
b^*\wedge a^*=b^*.
$$

Như vậy, hệ gồm đúng mười một tiên đề

$$
\mathrm{M0\!-\!M3},\quad
\mathrm{S1\!-\!S3},\quad
\mathrm{SM1\!-\!SM2},\quad
\mathrm{P},\quad
\mathrm{PM}.
$$

---

## 2. Các toán tử và phần tử dẫn xuất

### 2.1. Thứ tự dẫn xuất

Định nghĩa

$$
a\le b
\quad:\Longleftrightarrow\quad
a\wedge b=a.
$$

Theo M0–M2, quan hệ $\le$ là một thứ tự bộ phận.

### 2.2. Join

Định nghĩa toán tử join bởi

$$
a\vee b
:=
(a^*\wedge b^*)^*.
$$

Phần tử đơn vị của join là

$$
e_{\vee}:=e_{\wedge}^*.
$$

### 2.3. Times

Định nghĩa toán tử times bởi

$$
a\times b
:=
(a^*+b^*)^*.
$$

Phần tử đơn vị của times là

$$
e_{\times}:=e_{+}^*.
$$

### 2.4. Các công thức De Morgan

Từ tiên đề P suy ra

$$
(a\vee b)^*=a^*\wedge b^*,
$$

$$
(a\times b)^*=a^*+b^*,
$$

và ngược lại,

$$
(a\wedge b)^*=a^*\vee b^*,
$$

$$
(a+b)^*=a^*\times b^*.
$$

Ngoài ra,

$$
e_{\vee}^*=e_{\wedge},
\qquad
e_{\times}^*=e_{+}.
$$

---

## 3. Các định lý cơ bản

### Định lý 1. Polar là một song ánh đối hợp

Ánh xạ

$$
(-)^*:X\to X
$$

là song ánh và nghịch đảo của nó chính là nó:

$$
(*\,)^{-1}=*.
$$

#### Chứng minh

Nếu $a^*=b^*$, thì theo P,

$$
a=a^{**}=b^{**}=b,
$$

nên $*$ đơn ánh. Với mọi $b\in X$,

$$
b=(b^*)^*,
$$

nên $b$ có tiền ảnh $b^*$, và do đó $*$ toàn ánh. $\square$

---

### Định lý 2. Meet sinh một thứ tự bộ phận

Quan hệ

$$
a\le b
\iff
a\wedge b=a
$$

là một thứ tự bộ phận trên $X$.

#### Chứng minh

- Phản xạ suy ra từ M0.
- Phản đối xứng suy ra từ M2.
- Bắc cầu suy ra từ M1. $\square$

---

### Định lý 3. $e_{\wedge}$ là phần tử lớn nhất

Với mọi $a\in X$,

$$
a\le e_{\wedge}.
$$

#### Chứng minh

Theo M3,

$$
a\wedge e_{\wedge}=a,
$$

nên $a\le e_{\wedge}$. $\square$

---

### Định lý 4. Meet đơn điệu

Nếu $a\le b$, thì với mọi $c\in X$,

$$
a\wedge c\le b\wedge c.
$$

#### Chứng minh

Từ $a\wedge b=a$, dùng M0–M2,

$$
(a\wedge c)\wedge(b\wedge c)
=
(a\wedge b)\wedge(c\wedge c)
=
a\wedge c.
$$

Do đó $a\wedge c\le b\wedge c$. $\square$

---

### Định lý 5. Sum đơn điệu

Nếu $a\le b$, thì với mọi $c\in X$,

$$
a+c\le b+c.
$$

#### Chứng minh

Từ $a\wedge b=a$, dùng SM1 và S2,

$$
(c+a)\wedge(c+b)
=
c+(a\wedge b)
=
c+a.
$$

Vì vậy $a+c\le b+c$. $\square$

---

### Định lý 6. Polar đảo thứ tự

Với mọi $a,b\in X$,

$$
a\le b
\quad\Longleftrightarrow\quad
b^*\le a^*.
$$

#### Chứng minh

Đây chính là tiên đề PM khi viết bằng quan hệ thứ tự dẫn xuất:

$$
a\le b
\iff
a\wedge b=a
\iff
b^*\wedge a^*=b^*
\iff
b^*\le a^*.
$$

$\square$

---

### Định lý 7. Join là supremum của hai phần tử

Với mọi $a,b,c\in X$,

$$
a\le a\vee b,
\qquad
b\le a\vee b,
$$

và nếu

$$
a\le c,\qquad b\le c,
$$

thì

$$
a\vee b\le c.
$$

Do đó $a\vee b$ là cận trên nhỏ nhất của $a$ và $b$.

#### Chứng minh

Do $a^*\wedge b^*\le a^*$, Định lý 6 cho

$$
a\le(a^*\wedge b^*)^*=a\vee b.
$$

Tương tự $b\le a\vee b$.

Nếu $a\le c$ và $b\le c$, thì

$$
c^*\le a^*,
\qquad
c^*\le b^*,
$$

suy ra

$$
c^*\le a^*\wedge b^*.
$$

Áp Định lý 6 một lần nữa,

$$
(a^*\wedge b^*)^*\le c,
$$

tức $a\vee b\le c$. $\square$

---

### Định lý 8. $e_{\vee}$ là phần tử nhỏ nhất

Với mọi $a\in X$,

$$
e_{\vee}\le a.
$$

#### Chứng minh

Từ Định lý 3,

$$
a^*\le e_{\wedge}.
$$

Áp tính đảo thứ tự,

$$
e_{\wedge}^*\le a^{**}=a.
$$

Vì $e_{\vee}=e_{\wedge}^*$, suy ra $e_{\vee}\le a$. $\square$

---

### Định lý 9. Cấu trúc dẫn xuất qua polar

Các phép toán dẫn xuất thỏa:

1. $(X,\vee,e_{\vee})$ là một nửa giàn giao hoán lũy đẳng;
2. $(X,\times,e_{\times})$ là một monoid giao hoán;
3. times phân phối trên join:

$$
a\times(b\vee c)
=
(a\times b)\vee(a\times c);
$$

4. $e_{\vee}$ hấp thụ đối với times:

$$
a\times e_{\vee}=e_{\vee}.
$$

#### Chứng minh

Các tính chất được vận chuyển từ các tiên đề tương ứng của
$(\wedge,+,e_{\wedge},e_+)$ qua đối hợp $*$. Chẳng hạn,

$$
a\times(b\vee c)
=
\bigl(a^*+(b^*\wedge c^*)\bigr)^*
$$

$$
=
\bigl((a^*+b^*)\wedge(a^*+c^*)\bigr)^*
=
(a\times b)\vee(a\times c).
$$

Các tính chất còn lại được chứng minh tương tự. $\square$

---

### Định lý 10. $e_{\vee}$ là phần tử nhỏ nhất

Với mọi $a\in X$,

$$
e_{\vee}\le a.
$$

#### Chứng minh

Từ Định lý 3,

$$
a^*\le e_{\wedge}.
$$

Áp Định lý 6,

$$
e_{\wedge}^*\le a^{**}=a.
$$

Vì $e_{\vee}=e_{\wedge}^*$, suy ra

$$
e_{\vee}\le a.
$$

$\square$

**Không giả sử thêm bất kỳ tính chất thứ tự nào đối với** $e_{+}$ **hoặc** $e_{\times}$. Chúng chỉ được xem là các phần tử đơn vị của hai phép toán $+$ và $\times$.

---

## Ghi chú về tính độc lập của hệ tiên đề

Mace4 đã tìm được một mô hình hữu hạn của toàn bộ hệ và một phản mô hình
hữu hạn cho từng phép thử bỏ riêng một trong mười một tiên đề. Vì vậy,
mười một tiên đề trên là độc lập theo từng tiên đề: không tiên đề nào suy
ra từ mười tiên đề còn lại.
