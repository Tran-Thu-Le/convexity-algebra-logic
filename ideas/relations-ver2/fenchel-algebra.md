# Fenchel Algebra

Tiên đề hóa trừu tượng của tầng đại số (Level 2), tách khỏi mô hình hình học preepi, dùng đúng bộ ký hiệu chuẩn đã xác lập: $\wedge$ (meet), $\triangle$ (fibor), $\vee$ (join), $\bigtriangledown$ (spator), $1_\wedge,1_\vee,1_\triangle,1_\bigtriangledown$ (bốn đơn vị), $(\cdot)^*$ (Fenchel polar).

Theo truyền thống đặt tên của Boolean algebra, Heyting algebra, Girard algebra: tên gọi lưu giữ **nguồn gốc** (Fenchel conjugate), định nghĩa chính xác nằm ở tiên đề, không ở tên gọi.

---

## 1. Pre-Fenchel Algebra

Một **pre-Fenchel algebra** là một bộ $(A,\wedge,\triangle,1_\wedge,1_\triangle)$ thỏa ba tiên đề:

**(pF1) Meet monoid.** $(A,\wedge,1_\wedge)$ là commutative monoid:

$$E\wedge F=F\wedge E,\qquad(E\wedge F)\wedge G=E\wedge(F\wedge G),\qquad E\wedge1_\wedge=E.$$

**(pF2) Fibor monoid.** $(A,\triangle,1_\triangle)$ là commutative monoid:

$$E\triangle F=F\triangle E,\qquad(E\triangle F)\triangle G=E\triangle(F\triangle G),\qquad E\triangle1_\triangle=E.$$

**(pF3) Phân phối.** $\triangle$ phân phối qua $\wedge$:

$$E\triangle(F\wedge G)=(E\triangle F)\wedge(E\triangle G).$$

Đây thuần túy là **hai monoid giao hoán chia sẻ một tính phân phối**, không có thứ tự (vì $\wedge$ chưa idempotent nên chưa sinh semilattice), không có $(\cdot)^*$, không có hình học.

### 1.1 Quan hệ dẫn xuất trước khi có idempotent

Đặt $E\subseteq F:\iff E\wedge F=E$. Với (pF1)-(pF3) không thôi, quan hệ này đã:

- **Bắc cầu**: nếu $E\subseteq F,F\subseteq G$ thì $E\wedge G=(E\wedge F)\wedge G=E\wedge(F\wedge G)=E\wedge F=E$ — chỉ cần kết hợp.
- **Phản đối xứng**: nếu $E\subseteq F$ và $F\subseteq E$ thì $E=E\wedge F=F\wedge E=F$ — chỉ cần giao hoán.
- **Chưa phản xạ**: $E\subseteq E\iff E\wedge E=E$, chưa được đảm bảo.

Vậy $\subseteq$ ở tầng pre-Fenchel đã transitive + antisymmetric, thiếu đúng một mảnh (phản xạ) để thành partial order.

---

## 2. Fenchel Algebra = Pre-Fenchel + Idempotent + Polar

Một **Fenchel algebra** là một pre-Fenchel algebra $(A,\wedge,\triangle,1_\wedge,1_\triangle)$ trang bị thêm hai tiên đề:

**(F4) Idempotent của meet.**

$$E\wedge E=E\qquad\forall E\in A.$$

Đây chính là "$E\subseteq E$ đúng với mọi $E$" — mảnh còn thiếu để $\subseteq$ (đã bắc cầu + phản đối xứng từ pF1) trở thành **partial order thật sự** (không phải preorder — preorder chỉ cần phản xạ+bắc cầu, ở đây có cả ba, mạnh hơn preorder).

**(F5) Fenchel polar.** Một ánh xạ

$$(\cdot)^*:A\to A$$

là **order-reversing involution** đối với $\subseteq$ vừa sinh:

$$E\subseteq F\implies F^*\subseteq E^*,\qquad E^{**}=E.$$

> **Lưu ý.** Hai điều kiện của (F5) độc lập nhau — một ánh xạ phản biến bất kỳ trên một poset không hề tự động extensive/involutive khi áp hai lần (phản ví dụ: chain $a<b<c$, $f(a)=c,f(b)=c,f(c)=a$ là phản biến hoàn hảo nhưng $f(f(b))=a<b$). Vậy (F5) là **hai tiên đề độc lập gộp chung một dòng**, không cái nào suy ra cái kia.

---

## 3. Join và Spator, định nghĩa qua $*$

$$E\vee F:=(E^*\wedge F^*)^*\qquad(\textbf{Join}),$$

$$E\bigtriangledown F:=(E^*\triangle F^*)^*\qquad(\textbf{Spator}),$$

$$1_\vee:=1_\wedge^*,\qquad 1_\bigtriangledown:=1_\triangle^*.$$

Không có định nghĩa nào khác cần thiết — $\vee,\bigtriangledown,1_\vee,1_\bigtriangledown$ hoàn toàn là phái sinh của $\wedge,\triangle,1_\wedge,1_\triangle,(\cdot)^*$. Sơ đồ phụ thuộc:

```
Primitive: ∧, △, *, 1∧, 1△
     ↓
   order ⊆   (⊆ đã có từ pF1, hoàn tất bởi F4)
     ↓
   ∨, ▽, 1∨, 1▽   (dẫn xuất qua De Morgan)
```

### Bổ đề chốt

$$(E\vee F)^*=E^*\wedge F^*,\qquad(E\bigtriangledown F)^*=E^*\triangle F^*.$$

**Chứng minh.** $(E\vee F)^*=\big((E^*\wedge F^*)^*\big)^*=E^*\wedge F^*$, áp $(\cdot)^{**}=\mathrm{id}$ (F5) cho phần tử $E^*\wedge F^*$. Tương tự cho $\bigtriangledown$. $\blacksquare$

Bổ đề này được dùng trong **mọi** chứng minh ở Mục 4.

---

## 4. Join, Spator cũng là monoid; Spator phân phối vào Join

### 4.1 $(A,\vee,1_\vee)$ là commutative **idempotent** monoid

**Giao hoán.**
$$E\vee F=(E^*\wedge F^*)^*=(F^*\wedge E^*)^*=F\vee E\qquad\text{[(pF1) giao hoán]}.$$

**Kết hợp.**
$$(E\vee F)\vee G=\big((E\vee F)^*\wedge G^*\big)^*=\big((E^*\wedge F^*)\wedge G^*\big)^*=\big(E^*\wedge(F^*\wedge G^*)\big)^*=E\vee(F\vee G)$$
$$\text{[bổ đề chốt, rồi (pF1) kết hợp, rồi bổ đề chốt ngược]}.$$

**Idempotent.**
$$E\vee E=(E^*\wedge E^*)^*=(E^*)^*=E\qquad\text{[(F4), đây là chỗ DUY NHẤT trong Mục 4 cần idempotent]}.$$

**Đơn vị.**
$$E\vee1_\vee=(E^*\wedge1_\vee^*)^*=(E^*\wedge1_\wedge^{**})^*=(E^*\wedge1_\wedge)^*=(E^*)^*=E$$
$$\text{[dùng }1_\vee^*=(1_\wedge^*)^*=1_\wedge\text{ theo (F5), rồi đơn vị (pF1)]}.$$

### 4.2 $(A,\bigtriangledown,1_\bigtriangledown)$ là commutative monoid (KHÔNG idempotent)

Lập luận song song hệt trên, thay $\wedge\to\triangle$, dùng (pF2) thay (pF1):

$$E\bigtriangledown F=F\bigtriangledown E,\qquad(E\bigtriangledown F)\bigtriangledown G=E\bigtriangledown(F\bigtriangledown G),\qquad E\bigtriangledown1_\bigtriangledown=E.$$

Không có bước nào dùng (F4) — vì $\triangle$ không được giả sử idempotent (pF2 không có điều kiện đó), nên $\bigtriangledown$ cũng không idempotent, đúng như bản chất hình học (fiber sum của $E$ với chính nó nhân đôi hàm đại diện, không trả về $E$).

### 4.3 Spator phân phối vào Join

$$E\bigtriangledown(F\vee G)=\big(E^*\triangle(F\vee G)^*\big)^*=\big(E^*\triangle(F^*\wedge G^*)\big)^*\overset{\text{(pF3)}}{=}\big((E^*\triangle F^*)\wedge(E^*\triangle G^*)\big)^*=(E\bigtriangledown F)\vee(E\bigtriangledown G).$$

**Duy nhất bước giữa dùng (pF3)** — mọi bước còn lại là bổ đề chốt + định nghĩa. Kết luận: phân phối của Spator vào Join là **ảnh phản chiếu De Morgan trực tiếp** của phân phối Fibor vào Meet — không cần thêm bất kỳ giả thiết nào ngoài (pF1)-(pF3), (F4)-(F5).

---

## 5. Thêm hấp thụ $1_\wedge$ ⟹ Semiring hai phía, tự động đối ngẫu

### 5.1 Tiên đề bổ sung

**(F6) Absorption.**
$$E\triangle1_\wedge=1_\wedge\qquad\forall E\in A.$$

Với (pF1)-(pF3), (F4)-(F6): $(A,\wedge,\triangle,1_\wedge,1_\triangle)$ là **idempotent semiring đầy đủ** theo đúng định nghĩa chuẩn (phân phối + hấp thụ của phần tử không đối với phép nhân).

### 5.2 Định lý: đối ngẫu tự động, miễn phí

Khi có (F6), phía $(A,\vee,\bigtriangledown,1_\vee,1_\bigtriangledown)$ **cũng** là semiring — cụ thể $1_\vee$ hấp thụ $\bigtriangledown$:

$$E\bigtriangledown1_\vee=1_\vee\qquad\forall E\in A.$$

**Chứng minh.**
$$E\bigtriangledown1_\vee=(E^*\triangle1_\vee^*)^*=(E^*\triangle1_\wedge^{**})^*=(E^*\triangle1_\wedge)^*\overset{\text{(F6)}}{=}(1_\wedge)^*=1_\vee.$$

Một dòng — **không cần chứng minh riêng cho phía Join/Spator**, chỉ cần áp $(\cdot)^*$ lên (F6) là ra ngay đối ngẫu. Đây là điểm mấu chốt của kiến trúc: mọi tính chất "phía $\wedge/\triangle$" tự động sinh tính chất "phía $\vee/\bigtriangledown$" tương ứng qua đúng một cơ chế (bổ đề chốt Mục 3), không có công việc kép.

### 5.3 Sơ đồ tổng kết

$$\text{Pre-Fenchel (pF1--pF3)}\ \xrightarrow[\text{+ (F5) polar}]{\text{+ (F4) idempotent}}\ \text{Fenchel algebra}\ \xrightarrow{\text{+ (F6) absorption}}\ \text{Semiring hai phía}.$$

### 5.4 Vị trí của mô hình preepi/regepi

Mô hình hình học ($\mathbb X$, với $\wedge=\cap$, $\triangle=(\cdot+_{\mathrm{fib}}\cdot)^{**}$, $E^*$ = Fenchel conjugate) thỏa **(pF1)-(pF3), (F4)-(F5) đầy đủ** — tức là một Fenchel algebra thật sự.

Nhưng **không** thỏa (F6): phản ví dụ cụ thể

$$1_\wedge\triangle1_\vee=1_\vee\neq1_\wedge$$

(tính trực tiếp trên thớ, dùng quy ước Rockafellar $(+\infty)+(-\infty):=+\infty$; vi phạm xảy ra chính xác tại $E=1_\vee$, và theo Mục 5.2, đối ngẫu của vi phạm này — $E\bigtriangledown1_\vee\neq1_\vee$ tại $E=1_\wedge$ — cũng vi phạm tương ứng).

**Kết luận phân loại:** preepi/regepi là **Fenchel algebra, không phải semiring**. Đây là một phân loại chính xác của mô hình, không phải một lỗ hổng cần vá — khớp với literature đã có (Coniglio–Miraglia: (F1)-(F5) tương ứng **Girard algebra**; thêm điều kiện hấp thụ kiểu (F6) mới lên **bounded Girard algebra** = ngữ nghĩa đại số đầy đủ của MALL chuẩn, không paraconsistent).
