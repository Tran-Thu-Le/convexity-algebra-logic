# Dàn ý paper — v1

## Ký hiệu chuẩn hóa (dùng xuyên suốt)

| Ký hiệu | Tên gọi | Trên convex functions | Loại |
|---|---|---|---|
| $\oplus$ | Plus | $\max(f,g)$ | nguyên thủy |
| $\otimes$ | Tensor | $f+g$ | nguyên thủy |
| $a^*$ | Negation | $f^*$ (Fenchel conjugate) | nguyên thủy |
| $\&$ | With | $\operatorname{conv}\min(f,g)$ | dẫn xuất: $a\&b:=(a^*\oplus b^*)^*$ |
| $\operatorname{parr}$ | Parr | $\operatorname{cl}(f\square g)$ | dẫn xuất: $a\operatorname{parr}b:=(a^*\otimes b^*)^*$ |
| $e_\oplus$ | Unit of Plus | $f\equiv-\infty$ | |
| $e_\otimes$ | Unit of Tensor | $f\equiv0$ | |
| $e_\&$ | Unit of With | $f\equiv+\infty$ | $e_\&=e_\oplus^*$ |
| $e_{\operatorname{parr}}$ | Unit of Parr | $\delta_{\{0\}}$ | $e_{\operatorname{parr}}=e_\otimes^*$ |

Tên gọi: **Polar Semiring** ≡ **PICS** (Polar Idempotent Commutative Semiring), dùng thay nhau; PICS ưu tiên khi trích công thức/định lý.

Lớp nền: $\Gamma(\mathbb R^n)=\{f:f=f^{**}\}$ (bipolar-đóng).

---

## Sec 1 — Introduction

**Thông điệp chính**: Ba phép toán quen thuộc của giải tích lồi ($\max$, $+$, Fenchel conjugate) gần như tạo thành một idempotent semiring với negation, nhưng lớp hàm lồi chuẩn (closed convex proper) không đóng dưới cấu trúc này — đây là động lực cho toàn bộ chương trình.

**Ý con:**

1. Quan sát khởi điểm: các công thức dual đẹp đã biết giữa $\max$, $+$ và $*$ trên lớp closed convex proper — bằng chứng có cấu trúc đại số ẩn.

2. Vấn đề chính, kể như một chuỗi domino (chỉ nêu hiện tượng, không chứng minh ở đây):
   - Trên lớp closed convex **proper**: $\otimes=+$ và $\oplus=\max$ có công thức dual đẹp qua $*$, nhưng **không đóng** — vì tính proper.
   - Vá bằng cách thêm $f\equiv-\infty$ (đơn vị $e_\oplus$) vào lớp.
   - Nhưng ngay khi thêm $f\equiv-\infty$, polar của nó ($(-\infty)^*=+\infty$) lại **không proper** → phải thêm tiếp $f\equiv+\infty$ ($e_\&$).
   - Thêm cả hai phần tử suy biến này vào thì lớp mới **đóng hoàn toàn** dưới cả 3 phép — dẫn thẳng vào định nghĩa $\Gamma(\mathbb R^n)$ ở Sec 2.

3. Không đi theo hướng try4 (regepi/hình học trung gian) — một câu định vị ngắn.

4. Contributions:
   - Một completion tự nhiên, tối thiểu của lớp hàm lồi đóng thành $\Gamma(\mathbb R^n)$, dùng trực tiếp kết quả Rockafellar (không dựng vật hình học trung gian).
   - Tiên đề hóa polar semiring (11 tiên đề, ký hiệu $\oplus,\otimes,*$), độc lập với mọi mô hình cụ thể.
   - Một họ ~20 định lý (De Morgan, semiring đối ngẫu, thứ tự) chứng minh hoàn toàn ở tầng đại số, áp dụng ngược lại convex analysis cho With/Parr.
   - Kết quả bất khả thi: negation (Fenchel conjugate) không sinh từ residuation kiểu Girard quantale, với cả hai phép nhân tự nhiên — polar semiring là khung rộng hơn thật sự so với Girard quantale/residuated lattice.

---

## Sec 2 — Completion

**Thông điệp chính**: $\Gamma(\mathbb R^n)=\{f:f=f^{**}\}$ là lớp tối thiểu chứa lớp closed convex proper mà đóng dưới cả 3 phép $\oplus,\otimes,*$; điểm kết thúc tự nhiên của chuỗi domino ở Sec 1.

**Ý con:**

1. Định nghĩa $\Gamma(\mathbb R^n)$ — gồm đúng 3 loại phần tử: (i) closed convex proper functions, (ii) hằng $-\infty$, (iii) hằng $+\infty$. Khẳng định bằng định lý suy biến toàn cục: nếu $f=f^{**}$ và $f(x_0)=-\infty$ tại một điểm thì $f\equiv-\infty$ khắp nơi — lý do chỉ cần thêm đúng 2 hằng số, không phát sinh case lạ nào khác.

2. Theorem (Completion): $\big(\Gamma(\mathbb R^n),\oplus,\otimes,{}^*,e_\oplus,e_\otimes\big)$ với $e_\oplus=-\infty$, $e_\otimes=0$ là một polar semiring đầy đủ (11/11 tiên đề).

3. Chứng minh — chỉ dẫn kết quả, không tự chứng minh lại:
   - Phần "generic" (closed convex proper): dẫn thẳng kết quả chuẩn của **Rockafellar** (Fenchel–Moreau + công thức conjugate của sum/max) cho phần lõi tiên đề.
   - Phần còn lại: xử lý riêng **2 trường hợp biên** ($f\equiv-\infty$, $f\equiv+\infty$ tham gia vào $\oplus,\otimes,*$) bằng tính toán trực tiếp, ngắn gọn — chỗ giả thiết proper của Rockafellar không phủ tới.

4. Không lặp lại cấu trúc nội bộ tiên đề (kiểu "9/11 tiên đề là đại số sơ cấp") ở đây — thuộc Sec 3.

---

## Sec 3 — Polar Semiring

**Thông điệp chính**: Từ $\Gamma(\mathbb R^n)$ trừu tượng hóa thành hệ tiên đề polar semiring độc lập với convex analysis; chứng minh ~20 định lý thuần đại số; định vị trong bản đồ các cấu trúc đại số liên quan (bao gồm việc $\Gamma(\mathbb R^n)$ là mô hình MALL theo nghĩa PICS); và chỉ ra giới hạn cốt lõi — negation không sinh từ residuation.

**Ý con:**

1. **3.1 Axioms** — 11 tiên đề bằng $(\oplus,\otimes,*,e_\oplus,e_\otimes)$:
   - M0–M3: $\oplus$ là idempotent commutative monoid.
   - S1–S3: $\otimes$ là commutative monoid.
   - SM1: $\otimes$ phân phối trên $\oplus$.
   - SM2: hấp thụ, $a\otimes e_\oplus=e_\oplus$.
   - P: $a^{**}=a$.
   - PM: tương thích thứ tự-polar.
   - Định nghĩa dẫn xuất: $\le$ (từ $\oplus$), $\&$ (With), $\operatorname{parr}$ (Parr), $e_\&=e_\oplus^*$, $e_{\operatorname{parr}}=e_\otimes^*$.

2. **3.2 Theorems** — chia 3 nhóm:
   - *Duality*: 4 đẳng thức De Morgan ($(a\&b)^*=a^*\oplus b^*$, v.v.) + đơn vị đối ngẫu.
   - *Algebra*: $(\&,e_\&)$ idempotent comm. monoid; $(\operatorname{parr},e_{\operatorname{parr}})$ comm. monoid; $\operatorname{parr}$ phân phối trên $\&$ (đối ngẫu của SM1); $e_\&$ hấp thụ với $\operatorname{parr}$.
   - *Order*: $\le$ là thứ tự bộ phận; $e_\oplus/e_\&$ là max/min; đơn điệu của $\oplus,\otimes$; đảo thứ tự qua $*$; thứ tự cảm sinh từ $\&$ trùng $\le$; luật hấp thụ $\oplus/\&$.

3. **3.3 Related algebra**:
   - Sơ đồ phân tầng: Boolean algebra ⊂ Girard quantale ⊂ involutive residuated lattice ⊂ ... ⊂ **polar semiring**; polar semiring chỉ đòi PM (điều kiện thứ tự thuần túy), không đòi residuation tồn tại — lớp rộng nhất trong sơ đồ.
   - **MALL thỏa PICS**: $\Gamma(\mathbb R^n)$ với đủ 4 connective ($\oplus,\otimes,\&,\operatorname{parr}$) + 4 đơn vị + De Morgan đầy đủ là một mô hình hợp lệ của MALL theo nghĩa polar semiring — nhưng (dẫn sang 3.4) negation không đến từ residuation kiểu Girard-quantale chuẩn, nên đây là mô hình MALL theo nghĩa polar semiring, khác/rộng hơn mô hình MALL kiểu quantale truyền thống.

4. **3.4 Impossibility (không tồn tại residual)**:
   - Thm A: không tồn tại $q$ để $a\otimes b\preceq q\iff b\preceq a^*$ (residual ứng với $\otimes$, tức pointwise sum).
   - Thm B: tương tự cho $\operatorname{parr}$ (residual dạng kernel dịch chuyển, dùng $q(x+y)=\langle x,y\rangle$ để phản chứng).
   - Hệ quả: polar semiring $\not\Rightarrow$ Girard quantale, với **cả hai** phép nhân tự nhiên tương thích với polar.

---

## Sec 4 — Application back to convex functions

**Thông điệp chính**: With và Parr — định nghĩa thuần đại số ở Sec 3 — khi cụ thể hóa trên $\Gamma(\mathbb R^n)$ chính xác là hai phép giải tích lồi kinh điển ($\operatorname{conv}\min$ và $\operatorname{cl}$ inf-convolution); luật phân phối đại số (SM1 + đối ngẫu) hạ xuống thành một đẳng thức giải tích lồi được thừa hưởng miễn phí, không cần chứng minh riêng.

**Ý con:**

1. **4.1 With trên hàm lồi — định lý + chứng minh**:
$$f\& g:=(f^*\oplus g^*)^*=(\max(f^*,g^*))^*=\operatorname{conv}\min(f,g)$$
Chứng minh: dùng công thức biconjugate của $\min$ (convex hull of pointwise min qua conjugate của max).

2. **4.2 Parr trên hàm lồi — định lý + chứng minh**:
$$f\operatorname{parr}g:=(f^*\otimes g^*)^*=(f^*+g^*)^*=\operatorname{cl}(f\square g)$$
Chứng minh: dùng công thức chuẩn $(f\square g)^*=f^*+g^*$, lấy $*$ hai vế.

3. **4.3 Phân phối, cụ thể hóa bằng toán tử hàm lồi**: từ SM1 nguyên thủy
$$f\otimes(g\oplus h)=(f\otimes g)\oplus(f\otimes h)\quad\text{tức}\quad f+\max(g,h)=\max(f+g,f+h)$$
(đẳng thức sơ cấp trên $\overline{\mathbb R}$) — dualize qua $*$ ra luật $\operatorname{parr}$ phân phối trên $\&$, cụ thể hóa thành:
$$\operatorname{cl}\big(f\square\operatorname{conv}\min(g,h)\big)=\operatorname{conv}\min\big(\operatorname{cl}(f\square g),\,\operatorname{cl}(f\square h)\big)$$
Nhấn mạnh: đẳng thức này **không cần chứng minh giải tích riêng**, chỉ là ảnh của Theorem đại số (SM1 + De Morgan) qua phép cụ thể hóa.

(Mục "MALL thỏa PICS" đã chuyển lên Sec 3.3 — Sec 4 không lặp lại.)
