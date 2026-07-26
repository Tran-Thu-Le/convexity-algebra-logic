# Positioning v3

**Phạm vi**: bài viết này chỉ nói về mối quan hệ giữa hai tầng — (i) hàm lồi (closed convex functions, và phần mở rộng $\Gamma(\mathbb R^n)$) và (ii) polar semiring (cấu trúc đại số $\oplus,\otimes,*$). Không đề cập regepi, preepi, linear logic, hay MALL ở bất kỳ đâu trong văn bản này — kể cả như một hướng bị loại bỏ. Nếu cần nhắc "try4" (hướng regepi từng cân nhắc), việc đó thuộc Sec 1 của dàn ý chính, không thuộc positioning.

## Mở đầu — bốn phép toán đối ngẫu, hai quan sát, hai câu hỏi

### Bốn phép toán dual trong giải tích lồi

Giải tích lồi cổ điển có hai cặp phép toán đối ngẫu với nhau qua Fenchel conjugate $(\cdot)^*$:

$$
\max(f,g),\qquad f+g \qquad\Big|\qquad \min(f,g),\qquad f\square g:=\inf_y\{f(y)+g(x-y)\}
$$

với các đẳng thức dual quen thuộc liên hệ chúng qua $*$:

$$
(f+g)^* = \operatorname{cl}(f^*\square g^*), \qquad
(f\square g)^* = f^*+g^*
$$
$$
\big(\max(f,g)\big)^* = \operatorname{conv}\min(f^*,g^*), \qquad
\big(\operatorname{conv}\min(f,g)\big)^* = \max(f^*,g^*)
$$

Bốn đẳng thức này là nền tảng chuẩn của lý thuyết dual (Rockafellar). Chúng gợi ý mạnh mẽ rằng $\max,+,\min,\square$ tạo thành một cấu trúc đóng có tính đối xứng qua $*$ — nhưng khi kiểm tra trực tiếp trên lớp closed convex proper, tính đóng đó vỡ theo hai cách khác nhau.

### Quan sát 1 — $\max$ và $+$ không đóng trên lớp proper

Với $f,g$ closed convex proper, $\max(f,g)$ và $f+g$ luôn lồi và (trong trường hợp $\max$) luôn đóng, nhưng **không đóng trên lớp proper**: kết quả có thể suy biến ra khỏi tính proper — ví dụ $f+g\equiv+\infty$ khi $\operatorname{dom} f\cap\operatorname{dom} g=\emptyset$. Đây thuần túy là vấn đề **properness bị vỡ**, không phải convexity hay closedness.

**Câu hỏi 1.** Có tồn tại một completion tối thiểu của lớp closed convex proper, đóng hoàn toàn dưới cả $\max$ và $+$ (và do đó dưới $*$, theo bốn đẳng thức dual ở trên), hay không?

### Quan sát 2 — $\min$ và $\square$ vỡ theo hai cách khác nhau

Nhìn vào vế đối ngẫu của bốn đẳng thức trên, $\min(f,g)$ và $f\square g$ là hai phép toán "sinh ra" từ $\max,+$ qua $*$ — nhưng chúng vỡ theo hai kiểu khác nhau:

- $\min(f,g)$ của hai hàm lồi **nói chung không lồi** — cần toán tử `conv` (convex hull) để sửa: $\operatorname{conv}\min(f,g)$.
- $f\square g$ **luôn lồi** (nếu $f,g$ lồi) nhưng **không chắc đóng** — cần toán tử `cl` (lower-semicontinuous closure) để sửa: $\operatorname{cl}(f\square g)$.

Một cái vỡ convexity, một cái vỡ closedness. Trong ngôn ngữ giải tích lồi cổ điển, đây là hai defect khác loại, và lẽ tự nhiên cần hai toán tử sửa khác loại.

**Câu hỏi 2.** Tại sao khi định nghĩa qua double-conjugate,
$$
f\&g:=(f^*\oplus g^*)^* ,\qquad f\operatorname{parr}g:=(f^*\otimes g^*)^*,
$$
cả hai defect khác loại đó — convexity của $\min$, closedness của $\square$ — lại được sửa bởi **cùng một cơ chế duy nhất** (áp $*$ hai lần), thay vì cần hai toán tử `conv` và `cl` tách biệt như cách viết cổ điển?

### Bài báo trả lời cả hai câu hỏi

- **Câu hỏi 1** được trả lời bằng một completion tối thiểu: thêm đúng hai hằng số suy biến $e_\oplus=-\infty,\ e_\&=+\infty$ vào lớp closed convex proper, thu được $\Gamma(\mathbb R^n)=\{f=f^{**}\}$, đóng hoàn toàn dưới $\max,+,*$ (Sec 2).
- **Câu hỏi 2** được trả lời bằng cách chỉ ra `conv` và `cl` không phải hai cơ chế độc lập: biconjugate luôn tự động cho ra một hàm vừa lồi vừa đóng, bất kể defect ban đầu của input nằm ở đâu. Khi $\min$ vỡ convexity, hai lần $*$ tự động phục hồi convexity — cho đúng $\operatorname{conv}\min$. Khi $\square$ chỉ vỡ closedness (đã sẵn lồi), hai lần $*$ tự động phục hồi closedness — cho đúng $\operatorname{cl}(f\square g)$ (Sec 4). Điều kiện để double-conjugate well-defined và cho đúng kết quả này chính là miền đã đóng dưới $*$ — tức chính là completion đã trả lời ở Câu hỏi 1. Vậy Câu hỏi 1 là tiền đề kỹ thuật bắt buộc để Câu hỏi 2 có nghĩa.


## Mở đầu — hai vai trò tách biệt

**Đoạn 1 — Pain point (mồi câu chuyện, không cần bảo vệ, không mang sức nặng chứng minh)**

Ai từng viết "let $f$ be proper closed convex" lặp đi lặp lại mỗi khi ghép $\max$, $+$, và Fenchel conjugate hẳn quen với cảm giác phải dừng lại kiểm biên ở từng bước — và quen với việc mỗi identity ghép (như luật phân phối giữa inf-convolution và convexified-min) phải chứng minh lại riêng bằng công cụ giải tích, kiểm case biên riêng, dù về bản chất đại số chúng chỉ là một hệ quả của cùng một cấu trúc.

**Đoạn 2 — Structural question (câu hỏi thật, có/không, trả lời được bằng chứng minh)**

Bài này trả lời một câu hỏi cụ thể: có tồn tại một completion tối thiểu của lớp closed convex proper — đóng hoàn toàn dưới cả ba phép $(\max, +, {}^*)$ — cùng một hệ tiên đề tường minh để mọi identity ghép được suy ra một lần ở tầng đại số, thay vì chứng minh lại bằng giải tích mỗi lần cần dùng, hay chưa? Câu trả lời là có: bằng đúng hai hằng số suy biến ($e_\oplus=-\infty$, $e_\&=+\infty$), lớp $\Gamma(\mathbb R^n)=\{f=f^{**}\}$ đóng dưới cả ba phép, là completion tối thiểu (Sec 2), tiên đề hóa được bằng 11 tiên đề độc lập với giải tích lồi (Sec 3.1), và hai hệ quả cụ thể — convexify, closure — hạ xuống giải tích lồi như hệ quả tự động, không phải chứng minh riêng (Sec 4).

---
# Positioning v4

**Phạm vi**: chỉ hàm lồi + polar semiring. Không đề cập regepi, preepi, linear logic, MALL. Chỉ bàn đúng 3 cơ chế chính quy hóa: convexify, closedness, properness — không tuyên bố về "regularization nói chung".

---

## 0. Thông điệp (một câu, làm headline cho abstract/Sec 1)

> Người làm giải tích lồi phải kiểm properness, closedness, và convexity như side-condition mỗi khi compose max, sum, conjugate; bài này chỉ ra rằng nếu mở rộng miền làm việc bằng đúng hai hằng số suy biến (không hơn), cả ba side-condition đó biến mất — convexify và closure trở thành ảnh tự động của cùng một involution $*$, còn properness trở thành một quan hệ thứ tự bình thường trong poset đã mở rộng — và từ đó mọi identity ghép được chứng minh một lần, ở tầng đại số thuần túy, thay vì chứng minh lại bằng giải tích mỗi lần cần dùng.

Impossibility result (Sec 3.4: negation không sinh từ residuation) là phát hiện thêm trong lúc xây hệ tiên đề — không phải trục chính, vì nó không trả lời trực tiếp câu hỏi "người tối ưu cần gì". Đặt đúng vị trí phụ trợ, không kéo lên làm headline.

---

## 1. Tầng mục tiêu (cách nhìn)

Ba cơ chế chính quy hóa quen thuộc — convexify, closure, kiểm properness — có hai nguồn gốc khác nhau, không phải một:

- **Convexify** ($\operatorname{conv}\min(f,g)$) và **closure** ($\operatorname{cl}(f\square g)$) là *representation artifact* của cùng một involution $*$: chúng là ảnh của hai phép đại số (With, Parr) qua biconjugation. Biconjugate luôn cho ra hàm đóng, nên tính đóng của hai construction này thừa hưởng tự động từ tính đóng của $*$ — không cần chứng minh riêng cho từng cái.
- **Properness** không phải output của một phép toán nào cả. Nó là side-condition sinh ra bởi việc loại trừ đúng hai phần tử suy biến ($f\equiv-\infty$, $f\equiv+\infty$) khỏi lớp closed convex cổ điển. Cơ chế giải quyết nó khác hẳn: **completion đưa 2 phần tử này vào poset**, ngang hàng với mọi hàm lồi đóng khác (chúng trở thành $e_\oplus, e_\&$ — max/min của thứ tự $\le$). Một khi đã ở trong $\Gamma(\mathbb R^n)$, câu hỏi "hàm này có proper không" không còn là side-condition phải kiểm trước khi dùng định lý — nó chỉ là câu hỏi thành viên poset bình thường.

Bài này giải quyết cả hai loại bằng hai cơ chế khác nhau trong cùng một completion: đóng miền dưới $*$ (giải quyết convexify/closure), và mở rộng poset để chứa 2 phần tử suy biến (giải quyết properness).

## 2. Tầng kỹ thuật (cách chứng minh — đúng Sec 1→4)

1. **Domino (Sec 1)** — $\otimes=+,\oplus=\max$ đẹp trên closed convex proper nhưng không đóng vì properness; vá bằng $e_\oplus=-\infty$; $(-\infty)^*=+\infty$ lại improper → vá tiếp bằng $e_\&=+\infty$. Bằng chứng cụ thể cho việc thiếu đúng 2 phần tử.
2. **Completion (Sec 2)** — $\Gamma(\mathbb R^n)=\{f=f^{**}\}$ là lớp tối thiểu đóng dưới $\oplus,\otimes,*$. $*$ tự động cho closed convex nhưng KHÔNG tự động proper — đây là lý do Sec 2 phải tồn tại như bước riêng. Chứng minh: phần generic dẫn Rockafellar, phần biên ($\pm\infty$) tính trực tiếp.
3. **Tiên đề hóa (Sec 3.1)** — 11 tiên đề trên $(\oplus,\otimes,*,e_\oplus,e_\otimes)$, độc lập với giải tích lồi.
4. **Định lý + impossibility (Sec 3.2, 3.4)** — ~20 định lý đại số (hạ tầng cần thiết để phát biểu và dùng Thm A/B); impossibility result là phát hiện phụ, không phải trục chính (xem Sec 0).
5. **Regularization như hệ quả (Sec 4)** — With/Parr cụ thể hóa đúng $\operatorname{conv}\min$, $\operatorname{cl}(f\square g)$; luật phân phối đại số hạ xuống thành identity giải tích lồi miễn phí, không chứng minh riêng.

---

## 3. Vì sao positioning này (v4) hiện là bản tốt nhất

So với v1 (embedded trong dàn ý), v2 (`positioning-v2.md`), v3 (2-tầng nhưng chưa phân biệt nguồn gốc regularization):

- **Không overclaim.** v2 nói "regularization" chung chung, ngụ ý mọi chính quy hóa trong convex analysis đều là representation artifact — không chứng minh được. v4 giới hạn đúng 3 cơ chế cụ thể, và với mỗi cơ chế nói rõ nó *thuộc loại nào trong hai loại* — không có tuyên bố nào vượt quá phần đã chứng minh trong Sec 2–4.
- **Không gộp sai cơ chế.** Bản phân tích trước (trước b) gộp cả 3 cơ chế vào một inversion duy nhất ("$*$ giải quyết hết"). v4 sửa lỗi này: properness không sinh từ $*$, nó biến mất nhờ một thao tác khác (mở poset). Đây là điểm kỹ thuật quan trọng — nếu giữ nguyên gộp sai, một reviewer quen giải tích lồi sẽ bắt bài ngay ở chỗ "tại sao properness cũng là ảnh của conjugate?" vì thực ra không phải.
- **Có đúng một headline, không phải danh sách 4 contribution ngang hàng.** v1/v2/v3 đều liệt kê completion + axioms + theorems + impossibility mà không phân cấp. v4 chọn dứt khoát: headline là "3 side-condition biến mất nhờ completion tối thiểu", impossibility là phát hiện phụ. Việc phân cấp này bắt nguồn từ câu hỏi "người tối ưu cần gì" — không phải sở thích trình bày, mà từ nhu cầu thật của người đọc mục tiêu (ai đó compose max/sum/conjugate và mệt mỏi vì phải kiểm 3 side-condition mỗi bước).
- **Tầng mục tiêu và tầng kỹ thuật khớp 1-1.** Mỗi câu ở Sec 1 (tầng mục tiêu) trỏ thẳng về đúng bước trong Sec 2 (tầng kỹ thuật) sinh ra nó — convexify/closure → bước 5, properness → bước 2. Không có tuyên bố triết học nào ở Sec 1 mà không có bước kỹ thuật tương ứng chứng minh nó.
- **Giới hạn phạm vi tường minh ở đầu file** — loại trừ hẳn regepi/preepi/linear logic/MALL, tránh lặp lỗi tháp 4 tầng của v2.

Đây là lý do v4 đạt điểm cao nhất trong 4 bản: nó là bản duy nhất trả lời được cả hai câu hỏi gốc — (1) pain point có thật và giới hạn đúng phạm vi (3 cơ chế, không hơn), (2) contribution có đúng một headline xuất phát từ nhu cầu người đọc, không phải danh sách kỹ thuật không phân cấp.


## Tầng mục tiêu (cách nhìn)

Regularization trong giải tích lồi — convexification, lower-semicontinuous closure, biconjugation — thường được xem là cơ chế vá lỗi: các phép toán cơ bản như $\max(f,g)$ hay inf-convolution $f\square g$ không tự động cho ra hàm lồi đóng, nên lý thuyết phải chèn thêm $\operatorname{conv}(\cdot)$, $\operatorname{cl}(\cdot)$ để sửa.

Bài này lật ngược cách nhìn đó. Closedness không phải điều kiện phải áp đặt thêm sau khi tính toán — nó là hệ quả tự động của việc đặt đúng cấu trúc đại số nền, trong đó ba phép $\oplus,\otimes,*$ đã đóng kín với nhau ngay từ định nghĩa. Khi tầng đại số này đã đóng, các construction quen thuộc của giải tích lồi ($\operatorname{conv}\min(f,g)$, $\operatorname{cl}(f\square g)$) không còn là hai thao tác riêng biệt cần hai chứng minh riêng — chúng là ảnh, qua một phép cụ thể hóa duy nhất, của hai phép đại số (With và Parr) được *định nghĩa* bằng $*$. Tính đóng của chúng thừa hưởng từ tính đóng của $*$ trong đại số, không phải chứng minh lại từng trường hợp.

Một hệ quả phụ của cách nhìn này: một khi đã tách rõ negation ($*$) ở tầng đại số, câu hỏi negation này có sinh từ residuation (theo nghĩa quen thuộc trong các đại số có phép nhân và phần dư) hay không trở thành một câu hỏi thuần đại số, tách khỏi giải tích lồi — và câu trả lời (không) là một trong những kết quả cho thấy cấu trúc ở đây rộng hơn các mô hình đại số có residuation chuẩn.

## Tầng kỹ thuật (cách chứng minh)

Năm bước, đúng theo trình tự Sec 1 → Sec 4 của dàn ý:

**1. Quan sát — chuỗi domino (Sec 1).**
Trên lớp closed convex **proper**: $\otimes=+$ và $\oplus=\max$ có công thức dual đẹp qua $*$, nhưng lớp này không đóng dưới cả 3 phép — vì tính proper bị phá. Vá bằng cách thêm hằng $f\equiv-\infty$ (đơn vị $e_\oplus$). Nhưng $(-\infty)^*=+\infty$ lại không proper, nên phải thêm tiếp $f\equiv+\infty$ ($e_\&$). Đây là quan sát cụ thể, không phải slogan trừu tượng — chuỗi hai bước vá này là bằng chứng trực tiếp cho thấy thiếu đúng 2 phần tử, không hơn.

**2. Completion (Sec 2).**
$\Gamma(\mathbb R^n)=\{f:f=f^{**}\}$ là lớp tối thiểu chứa closed convex proper mà đóng dưới cả $\oplus,\otimes,*$. Điểm cần nói rõ ở đây: $*$ (Fenchel conjugate) tự động cho ra hàm lồi đóng, nhưng **không** tự động cho ra hàm proper — đó chính là lý do Sec 2 phải tồn tại như một bước riêng, không thể gộp vào tuyên bố chung ở tầng mục tiêu. Chứng minh completion chia hai phần: phần generic dẫn thẳng kết quả Rockafellar; phần biên ($f\equiv\pm\infty$) xử lý riêng bằng tính toán trực tiếp.

**3. Tiên đề hóa (Sec 3.1).**
Từ $\Gamma(\mathbb R^n)$, trừu tượng hóa thành 11 tiên đề trên $(\oplus,\otimes,*,e_\oplus,e_\otimes)$, độc lập hoàn toàn với giải tích lồi — đây là bước chuyển từ "một mô hình cụ thể đóng" sang "một cấu trúc đại số được định nghĩa bằng tiên đề".

**4. Định lý tầng đại số (Sec 3.2, 3.4).**
~20 định lý chứng minh thuần đại số (De Morgan, With/Parr là monoid, thứ tự bộ phận), cộng với kết quả bất khả thi: negation không sinh từ residuation cho cả hai phép nhân tự nhiên ($\otimes$ và $\operatorname{parr}$). Đây là điểm được gợi mở từ tầng mục tiêu ở trên, để không xuất hiện đột ngột.

**5. Regularization như hệ quả (Sec 4).**
Cụ thể hóa With và Parr trên $\Gamma(\mathbb R^n)$ cho đúng $\operatorname{conv}\min(f,g)$ và $\operatorname{cl}(f\square g)$. Luật phân phối đại số (SM1 + De Morgan) hạ xuống thành một đẳng thức giải tích lồi *miễn phí* — không cần chứng minh riêng bằng công cụ giải tích, chỉ là ảnh của một theorem đại số đã có sẵn. Đây là chỗ đóng vòng với tầng mục tiêu: cái ban đầu nhìn như "cơ chế vá" giờ hiện ra là hệ quả của cấu trúc đại số đã đóng từ đầu.

---

## Sơ đồ hai tầng

```
[Tầng mục tiêu]   regularization = hệ quả biểu diễn của một *, không phải cơ chế vá
        ↑ đóng vòng ở bước 5                          ↓ mở ra ở bước 1
[Tầng kỹ thuật]   domino (Sec 1) → completion (Sec 2) → axioms (Sec 3.1)
                  → theorems + impossibility (Sec 3.2, 3.4) → regularization-as-corollary (Sec 4)
```

Không có tầng hình học hay logic nào chen giữa hàm lồi và polar semiring — completion đi thẳng bằng kết quả Rockafellar, và cụ thể hóa ở Sec 4 đi thẳng ngược lại từ đại số về giải tích lồi.
