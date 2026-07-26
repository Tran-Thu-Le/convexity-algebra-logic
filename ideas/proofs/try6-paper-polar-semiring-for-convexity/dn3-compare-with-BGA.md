# d2-compare-with-BGA.md

# Polar Semiring vs Bounded Girard Algebra: Quan Hệ Đầy Đủ

*(Nối tiếp dn2 "Bounded Girard Algebra", dn3 "Bảng ký hiệu PS-BGA", d1 "Kiến trúc PICS và Hai Định Lý Bất Khả Thi".)*

---

## Sec 1. Hai bộ ký hiệu — quy ước thống nhất

Ta dùng **ký hiệu của Polar Semiring (PS)** làm chuẩn xuyên suốt tài liệu (kể cả khi phát biểu lại các đối tượng của BGA), vì PS có ít ký hiệu nguyên thủy hơn.

| # | Polar Semiring (PS) | Bounded Girard Algebra (BGA) | Trạng thái | Ký hiệu thống nhất (dùng từ đây) |
|---|---|---|---|---|
| 1 | `^` — plus, **P** (M0-M3, idempotent) | `∨` — join, **P** | trùng khớp trực tiếp | `^` |
| 2 | `+` — tensor, **P** (S1-S3, SM1, SM2) | `·` — fusion/tensor, **P** | trùng khớp trực tiếp | `+` |
| 3 | `star` — polarity, **P** (P, PM) | `¬x := res(x,zero)` , **D** | *khác trạng thái*: PS nguyên thủy, BGA dẫn xuất | `star` |
| 4 | `em` (unit của `^`) = đáy, **P** | `⊥ := star(top)`, **D** | *khác trạng thái* | `em` |
| 5 | `ez` (unit của `+`), **P** | `1`, **P** | trùng khớp trực tiếp | `ez` |
| 6 | `with(x,y) := star(star(x)^star(y))`, **D** | `∧` — meet, **P** | *khác trạng thái* | `with` |
| 7 | `parr(x,y) := star(star(x)+star(y))`, **D** | `⅋(a,b) := star(star(a)+star(b))`, **D** | trùng khớp công thức 1-1 | `parr` |
| 8 | **— (trống)** | `res` — residual, **P** | **KHOẢNG TRỐNG DUY NHẤT** | `res` (chỉ dùng khi nói về BGA) |
| 9 | `zero := star(ez)`, **D** (ứng viên) | `0`, **P** | *khác trạng thái* | `zero` |
| 10 | `top := star(em)`, **D** | `⊤`, **P** | *khác trạng thái* | `top` |

**Kết luận Sec 1:** hai bộ ký hiệu **khớp 1-1 ở 9/10 vị trí** (chỉ khác nhau ở việc bên nào xem là nguyên thủy, bên nào là dẫn xuất). Vị trí **duy nhất thực sự trống bên PS** là `res` (residual) — PS không có, và **không có tiên đề nào trong 11 tiên đề PS đóng vai trò định nghĩa hay ràng buộc một residual**. Đây là khoảng trống cấu trúc trung tâm của toàn bộ tài liệu.

---

## Sec 2. BGA là một Polar Semiring — chứng minh đầy đủ

### 2.1. Tiên đề BGA (14 dòng, ký hiệu thống nhất)

**(A) Lattice** `(A, ^, with)`:
```
L1.  x^x = x                    L5.  with(x,y) = with(y,x)
L2.  x^y = y^x                  L6.  with(x,with(y,z)) = with(with(x,y),z)
L3.  x^(y^z) = (x^y)^z          L7.  x ^ with(x,y) = x        (hấp thụ 1)
L4.  with(x,x) = x              L8.  with(x, x^y) = x         (hấp thụ 2)
```

**(B) Vị nhóm giao hoán** `(A, +, ez)`:
```
M1.  x+(y+z) = (x+y)+z
M2.  x+y = y+x
M3'. x+ez = x        (đánh dấu M3' để không trùng tên với tiên đề M3 của PS)
```

**(C) Residuation** — điều kiện duy nhất liên kết `+` với thứ tự (`x≤y :⟺ with(x,y)=x`):
```
R1.  with(x+y, z) = x+y   <->   with(y, res(x,z)) = y
     (đọc: a·b ≤ c ⟺ b ≤ a→c)
```

**(D) 0 involutive + bounded:**
```
I1.  res(res(x,zero), zero) = x
B1.  with(ez, res(x,top)) = ez        (tương đương x ≤ top, tức top thật sự là max)
```

Định nghĩa dẫn xuất: `star(x):=res(x,zero)`, `em:=star(top)`, `parr(x,y):=star(star(x)+star(y))`.

### 2.2. Bổ đề trung gian (chỉ từ L1-L8, M1-M3', R1)

**Bổ đề A** (`a≤b ⟺ 1≤a→b`): từ R1 với `y:=ez`: `(a+ez)≤b ⟺ ez≤(res(a,b))`; vì `a+ez=a` (M3'), suy ra `a≤b ⟺ ez≤res(a,b)`.

**Bổ đề C** ("eval", `b·(b→c)≤c` luôn đúng): áp R1 với `x:=b,y:=res(b,c),z:=c`: `b+res(b,c) ≤ c ⟺ res(b,c)≤res(b,c)` — vế phải phản xạ luôn đúng, nên vế trái luôn đúng.

**Bổ đề D** (đơn điệu của `+`: `a≤b ⟹ a+c≤b+c`): từ giao hoán, `c+b=b+c≤b+c` tầm thường ⟹ (R1) `b≤res(c,b+c)` đúng vô điều kiện. Kết hợp `a≤b` (bắc cầu): `a≤res(c,b+c)` ⟹ (R1 ngược) `a+c≤b+c`. ∎

**Bổ đề E** (antitonic của `res`, do đó của `star`: `a≤b ⟹ res(b,z)≤res(a,z)`): từ Bổ đề D: `a+res(b,z) ≤ b+res(b,z)`; từ Bổ đề C: `b+res(b,z)≤z`. Bắc cầu: `a+res(b,z)≤z` ⟹ (R1) `res(b,z)≤res(a,z)`. ∎
→ Đặt `z:=zero`: **`star` antitonic**: `a≤b ⟹ star(b)≤star(a)`.

### 2.3. Chứng minh 11 tiên đề PS

**7 tiên đề trivial** (trùng thẳng với tiên đề BGA tương ứng, không cần chứng minh gì thêm):

| PS | ⟸ trùng trực tiếp với |
|---|---|
| M0: `x^x=x` | L1 |
| M1: `x^(y^z)=(x^y)^z` | L3 |
| M2: `x^y=y^x` | L2 |
| S1: `x+(y+z)=(x+y)+z` | M1 |
| S2: `x+y=y+x` | M2 |
| S3: `x+ez=x` | M3' |
| P: `star(star(x))=x` | I1 (vì `star(star(x))=res(res(x,zero),zero)=x`) |

**4 tiên đề cần chứng minh thật:**

**M3** (`x^em=x`, với `em:=star(top)`):

*Bước 1 — `x≤top` mọi `x`:* từ B1 (`ez≤res(x,top)`) và Bổ đề A ngược: `ez≤res(x,top) ⟹ x+ez≤top ⟹ x≤top` (vì `x+ez=x`).

*Bước 2 — antitonic áp cho `x≤top`:* `star(top)≤star(x)`, tức `em≤star(x)`, mọi `x`.

*Bước 3 — `star` toàn ánh (từ I1):* vì `star(star(y))=y` mọi `y`, nên `y=star(x)` với `x:=star(y)`. Vậy "`em≤star(x)` mọi `x`" ⟺ "`em≤y` mọi `y`" — `em` là **đáy** của lattice.

*Bước 4:* đáy `em` thỏa `x^em=x` mọi `x` theo định nghĩa lattice chuẩn (`a≤b ⟹ a^b=b`, áp với `a=em`). ∎

**SM1** (`x+(y^z)=(x+y)^(x+z)`):

Chiều `≥`: `y≤y^z ⟹ x+y≤x+(y^z)` (Bổ đề D); tương tự `x+z`; hợp lại `(x+y)^(x+z)≤x+(y^z)`.

Chiều `≤`: đặt `X:=(x+y)^(x+z)`. Từ `x+y≤X, x+z≤X`, Bổ đề A/R1 cho `y≤res(x,X)`, `z≤res(x,X)` → `y^z≤res(x,X)` (định nghĩa cận trên nhỏ nhất) → R1 ngược: `x+(y^z)≤X`. ∎

**SM2** (`x+em=em`, dùng `em` đã xác định là đáy ở M3):

`em≤x+em` luôn đúng (đáy nhỏ hơn mọi phần tử). Chiều ngược: R1 với `z:=em`: `x+em≤em ⟺ em≤res(x,em)` — đúng tự động vì `em` là đáy (nhỏ hơn mọi phần tử, kể cả `res(x,em)`). Hai chiều + phản đối xứng ⟹ `x+em=em`. ∎

**PM** (`(x^y=x) ⟺ (star(y)^star(x)=star(y))`):

Diễn dịch: `x^y=x ⟺ y≤x`; `star(y)^star(x)=star(y) ⟺ star(x)≤star(y)`. Vậy PM ⟺ `y≤x ⟺ star(x)≤star(y)`.

Chiều `⟹`: chính là Bổ đề E áp trực tiếp.
Chiều `⟸`: giả sử `star(x)≤star(y)`. Áp Bổ đề E lần nữa: `star(star(y))≤star(star(x))`. Dùng I1: `y≤x`. ∎

### 2.4. Kết luận Sec 2

    BGA  ==>  Polar Semiring

đã được chứng minh **đầy đủ, sơ cấp** (không cần category theory, không cần completeness/infinite joins) — chỉ dùng 14 tiên đề BGA liệt kê ở 2.1, qua 4 bổ đề trung gian (2.2) và 11 dòng chứng minh trực tiếp (2.3, trong đó 7 dòng trivial và 4 dòng cần lập luận thật).

---

## Sec 3. Incompatibility Theorem — Fenchel Polar không sinh bởi residual của `+`

### 3.1. Phát biểu

    Γ(R^n) := { f: R^n -> R-bar | f = f** }        (bipolar-đóng)
    f*(y)  := sup_x ( <x,y> - f(x) )                (Fenchel conjugate)

với cấu trúc PS: `^ := max` (điểm-theo-điểm), `+ :=` cộng max-plus, `em := -infinity`, `ez := 0`, `star :=` Fenchel conjugate `(-)*`.

**Định lý (Incompatibility).** Không tồn tại `q ∈ Γ(R^n)` — **kể cả hai phần tử đơn vị** `q=em=-∞` hay `q=ez=0` — sao cho

    a+b ⪯ q   <=>   b ⪯ star(a)      với mọi a,b ∈ Γ(R^n),

tức không tồn tại *dualizing element* làm cho residual sinh bởi `+` trùng đúng `star` (Fenchel polar). (Ở đây `u⪯v :⟺ u^v=u`, tức thứ tự PS trên `Γ`, tương ứng `u≥v` theo thứ tự thực thông thường vì `^=max`.)

### 3.2. Chứng minh

**Bước 0 — loại 2 đơn vị bằng một phản ví dụ chung `a=b:=0`:**

- `q=em=-∞`: vế trái `a+b⪯em` luôn đúng vô điều kiện (`em` hấp thụ mọi phần tử qua `^=max`). Tại `a=b=0`: vế phải cần `0⪯star(0)`. Tính `star(0)(y)=sup_x<x,y>`: bằng `0` nếu `y=0`, bằng `+∞` nếu `y≠0` — tức `star(0)=indicator({0})`. Điều kiện `0⪯star(0)` nghĩa `0(x)≥star(0)(x)` mọi `x` — **sai** tại `x≠0`. Vế trái đúng, vế phải sai ⟹ mâu thuẫn. `q≠em`.
- `q=ez=0`: tại `a=b=0`: vế trái `0+0=0⪯0` đúng (phản xạ). Vế phải giống hệt trên: `0⪯star(0)` — sai. Mâu thuẫn. `q≠ez`.

**Bước 1 — nếu `q` tồn tại (khác 2 đơn vị), nó bị ép duy nhất về `‖·‖²`:**

Cố định `y0`. Lấy `a := indicator({y0})`, nên `star(a)(x)=<x,y0>`. Điều kiện thu về `b(y0)≥q(y0) <=> b(x)≥<x,y0> ∀x`.
- `b1(x):=<x,y0>` (vế phải đúng, đẳng thức) ⟹ `q(y0)≤‖y0‖²`.
- `b2(x):=<x,y0>-ε` (vế phải sai) ⟹ `q(y0)>‖y0‖²-ε`, mọi `ε>0`.

Cho `ε→0`: `q(y0)=‖y0‖²`, đúng mọi `y0` (kể cả `y0=0`, khớp lại Bước 0). Vậy `q=‖·‖²` là ứng viên duy nhất còn lại.

**Bước 2 — loại nốt `q=‖·‖²`:**

Lấy `a:=‖·‖², b:=0`. Vế trái: `‖x‖²+0≥‖x‖²` — đúng (đẳng thức). Vế phải cần `0⪯star(a)`, tức `0≥star(a)(y)` mọi `y`. Tính `star(a)(y)=‖y‖²/4` (đạo hàm chuẩn). Cần `0≥‖y‖²/4` mọi `y` — sai với `y≠0`. Mâu thuẫn. **∎**

### 3.3. Kết luận Sec 3

    PICS (Polar Semiring)   =/=>   Bounded Girard Algebra

và mô hình phản ví dụ **không phải bảng cộng hữu hạn nhân tạo** mà là `Γ(R^n)` — mô hình trung tâm của giải tích lồi. Kết hợp với Sec 2 (`BGA ⟹ PS` đã chứng minh đầy đủ), quan hệ giữa hai lớp cấu trúc được xác lập **trọn vẹn cả hai chiều**:

    BGA  (⊊)  Polar Semiring

> **Remark.** Sự bất khả thi ở Sec 3 phản ánh đúng khoảng trống đã chỉ ra ở Sec 1: hệ 11 tiên đề của Polar Semiring **không có bất kỳ tiên đề nào ràng buộc trực tiếp giữa `+` (sum/tensor) và `^` (max/join) thông qua `star`** — ràng buộc duy nhất giữa `+` và `^` trong PS là SM1/SM2 (tensor phân phối qua join, và hấp thụ tại đáy), hoàn toàn không nhắc đến `star`; còn ràng buộc của `star` (P, PM) chỉ nói về chính `^` và chính nó, không hề đá động đến `+`. Do đó, việc một `star` cụ thể (như Fenchel polar) có "tương thích residuation" với một phép `+` cụ thể (như cộng max-plus) hay không là hoàn toàn không được quyết định bởi 11 tiên đề — và `Γ(R^n)` chứng minh rằng khoảng trống này không rỗng trên thực tế, chứ không chỉ là thiếu sót hình thức.
