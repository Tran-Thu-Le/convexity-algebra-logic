# Positioning v4

**Phạm vi**: chỉ hàm lồi (closed convex proper functions, và phần mở rộng $\Gamma(\mathbb R^n)$) + polar semiring. Không đề cập regepi, preepi, linear logic, MALL — kể cả như hướng bị loại bỏ. Chỉ bàn đúng ba cơ chế chính quy hóa: convexify, closedness, properness. Không tuyên bố về "regularization nói chung".

## Sec 0. Framing chính xác hóa: pain point đã được giải quyết bằng thực hành — bài này chứng minh phần thực hành đó là tối thiểu

**Pain point có thật, và đã được giải quyết — nhưng bằng thực hành, không phải bằng chứng minh.**
Cộng đồng convex analysis (Ekeland–Temam/Lieb) đã ngầm thêm hai hằng số suy biến $f\equiv-\infty,\ f\equiv+\infty$ vào $\Gamma(X)$, để việc compose $\max,+,{}^*$ không còn vỡ ra ngoài lớp closed convex proper. Đây là fact quan sát được, không phải claim của bài — không ai có thể nói pain point không tồn tại, vì chính cộng đồng đã phải thêm hai hằng số này để dùng được.

**Nhưng "thêm hai hằng số và nó work" khác hẳn về loại với "chứng minh hai là con số tối thiểu và đủ."**
Thực hành chỉ xác nhận: thêm $\pm\infty$ là *đủ dùng* cho mục đích cụ thể. Nó không xác nhận: (i) hai là con số *tối thiểu* — không có completion nào nhỏ hơn đóng được dưới cả ba phép; (ii) không có phần tử suy biến thứ ba nào phát sinh khi cho $\oplus,\otimes,*$ tác động lặp lại lên hai phần tử vừa thêm — tức lớp thu được thật sự *đóng hoàn toàn*, không phải "đóng đủ dùng".

**Bài này chứng minh chính xác việc thêm 2 phần tử đó là đóng theo nghĩa của cấu trúc polar semiring:** Thêm 2 phần tử suy biến này lập tức có cấu trúc đóng polar semiring. Hệ quả là convex min và closed inf convolution cũng nằm trong cấu trúc đó.

**Vì sao framing này quan trọng:** nó tránh đúng bẫy "chỉ là góc nhìn khác" — bài không tuyên bố phát hiện ra việc cần thêm $\pm\infty$ (đã có người làm), mà tuyên bố loại kết quả khác hẳn: rigor hóa và chứng minh tính tối thiểu tường minh cho một thực hành đã tồn tại nhưng chưa từng được đại số hóa hay chứng minh chặt.

## Sec 0b. Contribution (đã xác lập)

**Hành động.** Thêm đúng hai hàm suy biến $f\equiv-\infty$ ($e_\oplus$) và $f\equiv+\infty$ ($e_\&$) vào lớp closed convex proper.

**Hệ quả trực tiếp.** Lớp thu được, $\Gamma(\mathbb R^n)=\{f:f=f^{**}\}$, đóng hoàn toàn dưới cả ba phép toán $\max\,(\oplus),\ +\,(\otimes),\ {}^*$ — không chỉ "đủ dùng" như thực hành trước đó (Ekeland–Temam/Lieb) đã ngầm cho thấy, mà đóng theo nghĩa chặt: mọi phép áp lặp lại, kể cả trên chính hai phần tử suy biến, đều cho kết quả nằm lại trong lớp.

**Công cụ chính xác hóa.** Tính đóng này được phát biểu và chứng minh chặt chẽ thông qua cấu trúc **polar semiring**: $\big(\Gamma(\mathbb R^n),\oplus,\otimes,{}^*,e_\oplus,e_\otimes\big)$ thỏa đầy đủ 11 tiên đề. Chính việc tiên đề hóa này — không phải quan sát "thêm 2 hằng số là được" — mới là điều biến một thực hành có sẵn thành một định lý.

**Hệ quả kéo theo (không cần chứng minh riêng).** Một khi cấu trúc đã đóng, hai phép đại số phái sinh — With ($f\&g:=(f^*\oplus g^*)^*$) và Parr ($f\operatorname{parr}g:=(f^*\otimes g^*)^*$) — tự động well-defined trên toàn miền, và cụ thể hóa đúng ra $\operatorname{conv}\min(f,g)$ và $\operatorname{cl}(f\square g)$: hai construction quen thuộc nhất của giải tích lồi rơi ra như hệ quả của cấu trúc đóng, không phải hai thao tác rời rạc cần chứng minh riêng bằng công cụ giải tích.

---

## Sec 1 — Nguyên tắc định vị đã chốt

### 1.1 Hai vai trò tách biệt: pain point vs. structural question

- **Pain point** chỉ đóng vai trò mồi mở bài, không mang sức nặng chứng minh, không cần mọi người đồng thuận. Nó không phải nền móng của bài — nếu ai đó không thấy "đau", bài vẫn đứng vững.
- **Structural question** là câu hỏi có/không, kiểm chứng bằng toán, độc lập với cảm nhận người đọc. Đây là nền móng thật của bài. Bài chỉ chịu trách nhiệm về câu hỏi này, không chịu trách nhiệm thuyết phục ai đó rằng họ "nên thấy đau".

Hệ quả: mở bài không dựa vào việc thuyết phục pain-point là phổ quát; mở bài dựa vào việc đặt đúng một câu hỏi well-posed rồi trả lời nó.

### 1.2 Xuất phát điểm: bốn phép toán đối ngẫu, không phải slogan triết học

Thay vì mở bằng phát biểu trừu tượng ("regularization is a repair mechanism"), positioning xuất phát từ một sự kiện toán học kiểm chứng trực tiếp: bốn phép toán đối ngẫu quen thuộc $\max,+,\min,\square$ và bốn đẳng thức dual liên hệ chúng qua Fenchel conjugate. Đây là fact, không phải diễn giải — không ai cãi được.

### 1.3 Ba cơ chế chính quy hóa — hai nguồn gốc khác nhau, không gộp làm một

- **Convexify** ($\operatorname{conv}\min$) và **closedness** ($\operatorname{cl}(f\square g)$): cùng một nguồn gốc — representation artifact của một involution $*$ áp hai lần. Biconjugate luôn tự động cho ra hàm vừa lồi vừa đóng, bất kể defect ban đầu (convexity hay closedness) nằm ở đâu.
- **Properness**: nguồn gốc khác hẳn — không phải output của một phép toán, mà là side-condition sinh ra từ việc loại trừ hai phần tử suy biến ($f\equiv\pm\infty$) khỏi lớp cổ điển. Được giải quyết không phải bằng $*$, mà bằng việc mở rộng poset để hai phần tử đó gia nhập như thành viên bình thường.

Không được nói cả ba cơ chế "sinh từ $*$ theo cùng một cách" — đó là overclaim đã bị loại bỏ ở các bản trước.

### 1.4 Thông điệp một câu (headline)

> Convex analysis dùng bốn phép toán đối ngẫu $\max,+,\min,\square$ nhưng lớp closed convex proper không đóng dưới chúng theo hai kiểu khác nhau — vỡ properness ở $\max,+$, vỡ convexity/closedness ở $\min,\square$; bài này chỉ ra rằng một completion tối thiểu (thêm đúng hai hằng số suy biến) giải quyết cả hai, và trên completion đó, convexify và closure không còn là hai toán tử sửa riêng biệt mà là ảnh của một phép đại số duy nhất áp $*$ hai lần — nên mọi identity ghép giữa chúng được chứng minh một lần ở tầng đại số, không cần chứng minh lại bằng giải tích mỗi lần.

Impossibility result (negation không sinh từ residuation, Sec 3.4) là phát hiện phụ trong lúc xây hệ tiên đề — không phải headline, vì nó không trả lời trực tiếp hai câu hỏi cấu trúc dưới đây.

### 1.5 Những gì bị loại khỏi positioning

- Không dùng khung "regularization nói chung là representation artifact" — chỉ đúng cho 2/3 cơ chế.
- Không dựng tháp Convex → Regepi → Polar Semiring → Linear Logic.
- Không mở bài bằng tuyên bố cảm tính về mức độ "đau" của người dùng.
- Không để impossibility result cạnh tranh vị trí headline với completion + double-conjugate mechanism.

---

## Sec 2 — Dàn ý chi tiết: Quan sát → Câu hỏi → Cách tiếp cận → Kết quả

### 2.0 Bốn đẳng thức dual mở đầu

$$
(f+g)^* = \operatorname{cl}(f^*\square g^*), \qquad (f\square g)^* = f^*+g^*
$$
$$
\big(\max(f,g)\big)^* = \operatorname{conv}\min(f^*,g^*), \qquad \big(\operatorname{conv}\min(f,g)\big)^* = \max(f^*,g^*)
$$

Bốn đẳng thức chuẩn (Rockafellar) gợi ý $\max,+,\min,\square$ tạo thành cấu trúc đối xứng qua $*$ — nhưng tính đóng của chúng trên lớp closed convex proper vỡ theo hai cách khác nhau, dẫn tới hai quan sát dưới đây.

---

### 2.1 Quan sát 1 — $\max,+$ không đóng trên lớp proper

Với $f,g$ closed convex proper: $\max(f,g)$ và $f+g$ luôn lồi (và $\max$ luôn đóng), nhưng có thể suy biến ra khỏi tính **proper** — ví dụ $f+g\equiv+\infty$ khi $\operatorname{dom}f\cap\operatorname{dom}g=\emptyset$. Defect thuần túy là properness, không phải convexity hay closedness.

**Câu hỏi 1.** Có tồn tại completion tối thiểu của closed convex proper, đóng hoàn toàn dưới cả $\max$ và $+$ (và do đó dưới $*$), hay không?

**Cách tiếp cận — domino argument (Sec 1 paper) → completion (Sec 2 paper).**
Chuỗi vá hai bước: thêm $e_\oplus=-\infty$ để chứa $\max,+$ suy biến; nhưng $(-\infty)^*=+\infty$ lại improper, buộc thêm tiếp $e_\&=+\infty$. Định lý suy biến toàn cục (nếu $f=f^{**}$ và $f(x_0)=-\infty$ tại một điểm thì $f\equiv-\infty$ khắp nơi) đảm bảo không phát sinh case biên nào khác — đúng 2 hằng số là đủ và cần thiết.

**Kết quả.** $\Gamma(\mathbb R^n)=\{f:f=f^{**}\}$ — gồm đúng ba loại phần tử: closed convex proper, hằng $-\infty$, hằng $+\infty$ — là completion tối thiểu, đóng dưới $\oplus(=\max),\otimes(=+),*$. Chứng minh chia hai phần: phần generic dẫn thẳng Rockafellar (Fenchel–Moreau, công thức conjugate của sum/max); phần biên ($f\equiv\pm\infty$) xử lý riêng bằng tính toán trực tiếp — chỗ Rockafellar không phủ tới.

---

### 2.2 Quan sát 2 — $\min,\square$ vỡ theo hai cách khác nhau

Vế đối ngẫu của $\max,+$ qua bốn đẳng thức ở 2.0 là $\min,\square$ — nhưng chúng vỡ khác loại:
- $\min(f,g)$ của hai hàm lồi **nói chung không lồi** → cần `conv` (convex hull) để sửa.
- $f\square g$ **luôn lồi** (nếu $f,g$ lồi) nhưng **không chắc đóng** → cần `cl` (lower-semicontinuous closure) để sửa.

Một cái vỡ convexity, một cái vỡ closedness — hai defect khác loại, cách viết cổ điển dùng hai toán tử sửa khác loại.

**Câu hỏi 2.** Tại sao khi định nghĩa qua double-conjugate,
$$f\&g:=(f^*\oplus g^*)^*,\qquad f\operatorname{parr}g:=(f^*\otimes g^*)^*,$$
cả hai defect khác loại đó lại được sửa bởi **cùng một cơ chế duy nhất** (áp $*$ hai lần), thay vì cần `conv` và `cl` tách biệt?

**Cách tiếp cận — tiên đề hóa (Sec 3.1 paper) → cụ thể hóa ngược (Sec 4 paper).**
Trừu tượng hóa $\Gamma(\mathbb R^n)$ thành 11 tiên đề trên $(\oplus,\otimes,*,e_\oplus,e_\otimes)$: M0–M3 ($\oplus$ idempotent commutative monoid), S1–S3 ($\otimes$ commutative monoid), SM1 (phân phối), SM2 (hấp thụ), P ($a^{**}=a$), PM (tương thích thứ tự-polar). Từ đó định nghĩa dẫn xuất $\&,\operatorname{parr},e_\&,e_{\operatorname{parr}}$ — độc lập hoàn toàn với giải tích lồi. Sau đó cụ thể hóa ngược With/Parr trên $\Gamma(\mathbb R^n)$.

**Kết quả.**
$$f\&g=(f^*\oplus g^*)^*=(\max(f^*,g^*))^*=\operatorname{conv}\min(f,g)$$
$$f\operatorname{parr}g=(f^*\otimes g^*)^*=(f^*+g^*)^*=\operatorname{cl}(f\square g)$$
Cơ chế lý giải: biconjugate luôn tự động cho ra hàm vừa lồi vừa đóng, bất kể defect input nằm ở đâu — khi input $\min$ vỡ convexity, hai lần $*$ tự động phục hồi convexity; khi input $\square$ chỉ vỡ closedness, hai lần $*$ tự động phục hồi closedness. Cùng một cơ chế đại số, tác động đúng loại sửa cần thiết tùy defect. Điều kiện để cơ chế này well-defined chính là domain đã đóng dưới $*$ — tức đúng completion đã trả lời ở Câu hỏi 1. **Câu hỏi 1 là tiền đề kỹ thuật bắt buộc để Câu hỏi 2 có nghĩa.**

Hệ quả phụ trợ được thừa hưởng miễn phí từ SM1 + De Morgan, không cần chứng minh giải tích riêng:
$$\operatorname{cl}\big(f\square\operatorname{conv}\min(g,h)\big)=\operatorname{conv}\min\big(\operatorname{cl}(f\square g),\operatorname{cl}(f\square h)\big)$$

---

### 2.3 Hạ tầng đại số phụ trợ (không phải câu hỏi trung tâm, nhưng cần thiết để 2.2 có nghĩa)

**Nội dung.** ~20 định lý thuần đại số trên hệ tiên đề (De Morgan, $(\&,e_\&)$ và $(\operatorname{parr},e_{\operatorname{parr}})$ là monoid, thứ tự bộ phận $\le$, đơn điệu của $\oplus,\otimes$). Đi kèm kết quả bất khả thi: không tồn tại residual $q$ sao cho $a\otimes b\preceq q\iff b\preceq a^*$, cho cả hai phép nhân tự nhiên ($\otimes$ và $\operatorname{parr}$) — tức negation (Fenchel conjugate) không sinh từ residuation kiểu Girard quantale.

**Vai trò trong narrative.** Đây là phát hiện phụ, xuất hiện trong lúc xây hệ tiên đề đủ giàu để phát biểu Câu hỏi 2 một cách chặt chẽ — không phải trục chính, vì nó không trả lời trực tiếp Câu hỏi 1 hay Câu hỏi 2. Đặt đúng vị trí: sau khi đã trả lời hai câu hỏi cấu trúc, kết quả này cho biết cấu trúc vừa xây rộng hơn thật sự so với các mô hình đại số có residuation chuẩn.

---

### 2.4 Tổng kết mối quan hệ giữa hai câu hỏi

```
Quan sát 1 (max,+ vỡ properness)     Quan sát 2 (min,□ vỡ convexity/closedness)
        ↓                                       ↓
   Câu hỏi 1: completion tối thiểu?      Câu hỏi 2: một cơ chế cho cả hai defect?
        ↓                                       ↑ (cần domain đã đóng dưới *)
   Trả lời: Γ(R^n), +2 hằng số (Sec 2)  ────────┘
        ↓
   Tiên đề hóa (Sec 3.1) — hạ tầng để phát biểu Câu hỏi 2 chặt chẽ
        ↓
   Trả lời Câu hỏi 2: With/Parr = double-conjugate, tự động conv/cl (Sec 4)
        ↓
   Phát hiện phụ: impossibility result (Sec 3.4) — không sinh từ residuation
```

Không có tầng hình học hay logic trung gian nào chen vào giữa hai câu hỏi này và lời giải của chúng.

---

## Ghi chú — cần chuẩn hóa môi trường làm việc: $\Gamma(X)$ chuẩn là gì?

**Vấn đề.** Có hai ký hiệu khác nhau đang tồn tại song song trong literature convex analysis, và cả hai đều liên quan trực tiếp tới ký hiệu $\Gamma(\mathbb R^n)$ đang dùng trong bài:

1. **$\Gamma_0(X)$** — ký hiệu chuẩn phổ biến nhất (Moreau, dùng rộng rãi trong proximal methods/optimization): tập các hàm **proper**, convex, lower semicontinuous trên $X$. Lớp này **không chứa** $f\equiv\pm\infty$ — properness là điều kiện định nghĩa, không phải phần tử được thêm vào bằng completion.
2. **$\Gamma(X)$** (không subscript) — đã xuất hiện trong ít nhất một nguồn (gắn với truyền thống Ekeland–Temam / phụ lục convex analysis kiểu Lieb, dùng trong bối cảnh density-functional theory) với định nghĩa: gồm mọi hàm là sup của hàm affine — tức chính xác các hàm weak-* lsc proper convex, **cộng thêm cả hai hàm suy biến $f\equiv-\infty,\ f\equiv+\infty$**, với phần proper được tách riêng ký hiệu $\Gamma_0$. Đây gần như là định nghĩa **y hệt** $\Gamma(\mathbb R^n)$ của bài này.

**Hệ quả cần xử lý trước khi chốt notation và trước khi định vị Câu hỏi 1 là mới:**

- Cần đọc kỹ nguồn gốc $\Gamma(X)$-bao-gồm-$\pm\infty$ để xác định: nguồn đó có phát biểu completion là *tối thiểu* không, có *chứng minh* đóng dưới cả $\max,+,*$ không, hay chỉ dùng như định nghĩa tiện lợi không kèm định lý — đây là ranh giới giữa "đã có" và "còn thiếu, bài này lấp".
- Nếu chỉ là định nghĩa tiện lợi không kèm completion theorem, đóng góp mới của Sec 2 vẫn đứng vững (minimality + closedness dưới cả 3 phép + suy biến toàn cục là nội dung chưa thấy ở nguồn đó) — nhưng **phải cite và định vị tường minh**, không được để reviewer tự tìm ra.
- Cần quyết định ký hiệu trước khi nộp: (a) đổi hẳn ký hiệu bài (ví dụ $\widehat\Gamma$, $\Gamma^\pm(\mathbb R^n)$) để tránh nhầm với cả $\Gamma_0$ lẫn $\Gamma(X)$ đã dùng, hoặc (b) giữ $\Gamma(\mathbb R^n)$ nhưng thêm câu định vị ngay đầu Sec 2 nói rõ quan hệ với cả hai ký hiệu đã có.

**Trạng thái**: chưa xử lý — cần truy nguồn gốc chính xác (rất có thể Ekeland–Temam, *Convex Analysis and Variational Problems*, hoặc phụ lục convex analysis trong tài liệu DFT kiểu Lieb–Loss) trước khi hoàn tất Sec 2 của paper và trước khi tuyên bố completion là đóng góp mới trong positioning.
