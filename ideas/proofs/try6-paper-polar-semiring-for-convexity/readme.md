# try6-paper-polar-semiring-for-convexity

## Tóm tắt mục tiêu của folder

Đây là folder **viết báo** (không phải research thăm dò như try4/try5): mục tiêu là đóng khung đúng **positioning** cho một bài báo về **Polar Semiring / PICS** xây trực tiếp trên hàm lồi $\Gamma(\mathbb R^n)=\{f:f=f^{**}\}$, bỏ hẳn tầng hình học (regepi) và tầng logic (MALL/linear logic) ra khỏi phần thân bài — chỉ giữ **hàm lồi ↔ polar semiring**. Ba mạch nội dung đang tồn tại song song trong folder, **chưa được nối lại thành một dàn ý thống nhất**:

1. **Mạch chính (positioning + outline)** — [[d0-notations]], [[positioning-v1]] → [[positioning-v2]] → [[positioning-v3]] → **[[d00-positioning]]** (bản chốt, gọi là "v4"), [[d1-hierarchy]], [[d2dan-y-paper-v1]].
2. **Mạch so sánh với Bounded Girard Algebra (BGA)** — [[x1-def-of-bounded-Girard-algebra]], [[x3-PS-vs-BGA-symbol-table]], **[[dn3-compare-with-BGA]]** (chứng minh đầy đủ cả hai chiều).
3. **Mạch distribution profile** — [[dn1-distribution-profile-of-polar-semiring]], [[dn2-distribution-profiles-of-convex-functions]].

**Việc quan trọng nhất cần chốt trước khi viết báo: hợp nhất ba mạch này.** Mạch (2) và (3) chứa những kết quả *mạnh hơn* nội dung hiện có trong outline chính (1) nhưng **chưa được đưa vào** [[d1-hierarchy]]/[[d2dan-y-paper-v1]] hay [[d00-positioning]] — xem Sec 3.

---

## Sec 1. Mục tiêu chính mỗi file

### Mạch positioning (đọc theo thứ tự tiến hóa)

- **[[d0-notations]]** — Bảng ký hiệu chuẩn 4×9: MALL / Convex Functions / Regepis / Polar Semiring, gồm cả 4 connective và 4 đơn vị. Dùng convention Plus$(\oplus)$=Meet=$\max$, With$(\&)$=Join=$\operatorname{conv}\min$ — **lưu ý: convention này đảo ngược so với bảng cũ trong README gốc của repo và try4** (ở đó Meet=With, Join=Plus); đây là quy ước hiện hành cho try6, cần nhất quán khi viết báo.

- **[[positioning-v1]]**, **[[positioning-v2]]** — Hai bản nháp đầu, dùng khung "regularization nói chung là representation artifact" và tháp 4 tầng Convex Functions → Regepis → Polar Semiring → Linear Logic. **Đã bị loại bỏ tường minh** ở [[d00-positioning]] Sec 1.5 (overclaim: chỉ đúng cho 2/3 cơ chế chính quy hóa; tháp 4 tầng kéo lại regepi/MALL vào phạm vi bài). Giữ lại để tham khảo lịch sử.

- **[[positioning-v3]]** — Bản trung gian: tách đúng 2 câu hỏi cấu trúc (completion tối thiểu cho $\max,+$; cơ chế chung cho $\operatorname{conv}\min,\operatorname{cl}\square$) nhưng chưa phân biệt rạch ròi *nguồn gốc khác nhau* của ba cơ chế chính quy hóa (convexify/closedness là representation artifact của $*$; properness thì không). Cải tiến thành v4.

- **[[d00-positioning]]** (chứa cả nội dung "Positioning v4", **bản chốt hiện hành**) — Giới hạn phạm vi chặt: chỉ hàm lồi + polar semiring, không regepi/MALL. Headline: mở rộng miền bằng đúng 2 hằng số suy biến ($e_\oplus=-\infty$, $e_\&=+\infty$) làm biến mất cả 3 side-condition (properness, convexity, closedness) — properness biến mất nhờ *mở poset*, convexity/closedness biến mất nhờ *cùng một cơ chế đại số* ($*$ áp hai lần). Impossibility result (negation không sinh từ residuation) được xếp là **phát hiện phụ**, không phải headline. Kết thúc bằng một **việc chưa xử lý**: cần tra cứu xem ký hiệu $\Gamma(X)$-kèm-$\pm\infty$ đã từng xuất hiện trong Ekeland–Temam / phụ lục kiểu Lieb (DFT) hay chưa, để định vị đúng mức độ mới của Sec 2 (completion theorem) trước khi nộp bài.

- **[[d1-hierarchy]]** — Kiến trúc tổng thể bài báo: **Observe → Axiomatize → Represent**, cụ thể hóa thành Sec 2 (cấu trúc hàm lồi, 11 tính chất) → Sec 3 (Polar Semiring: tiên đề hóa, cấu trúc dẫn xuất, quan hệ với residuated structures, **định lý bất khả thi với residual** ở 3.4) → Sec 4 (hàm lồi là mô hình chuẩn tắc của Polar Semiring). Đây là khung mục lục cấp cao nhất hiện dùng.

- **[[d2dan-y-paper-v1]]** — Dàn ý chi tiết nhất, theo đúng khung của [[d1-hierarchy]], viết sẵn thông điệp chính + ý con cho từng Sec 1–4, kèm bảng ký hiệu chuẩn hóa và 4 contribution. Sec 3.3 ("Related algebra") hiện chỉ nói chung chung "Boolean algebra ⊂ Girard quantale ⊂ ... ⊂ polar semiring" — **chưa nhắc đến BGA cụ thể** dù đó chính là điều mạch (2) đã chứng minh chặt hơn nhiều.

### Mạch so sánh với Bounded Girard Algebra (BGA) — kết quả sắc nhất của folder

- **[[x1-def-of-bounded-Girard-algebra]]** — Định nghĩa BGA theo đúng tài liệu tham khảo **Paolo Aglianò, "An Algebraic Investigation of Linear Logic" (Archive for Mathematical Logic, 2025)**, nguồn khẳng định BGA là **ngữ nghĩa đại số tương đương của MALL**. Đây là mỏ neo trích dẫn quan trọng nhất cho toàn bộ claim "polar semiring liên hệ với MALL" — mạnh hơn hẳn việc chỉ nói "Girard quantale" chung chung như ở [[d2dan-y-paper-v1]].

- **[[x3-PS-vs-BGA-symbol-table]]** — Đối chiếu ký hiệu PS ↔ BGA từng mục (9/10 khớp trực tiếp hoặc dẫn xuất được), xác định **khoảng trống cấu trúc duy nhất**: BGA có `→` (residual) nguyên thủy, PS thì không có tiên đề nào ràng buộc `star` với `+` qua một residual. Đề ra chiến lược chứng minh hai chiều (BGA⟹PS bằng Prover9, PS⇏BGA bằng Mace4 tìm phản mô hình) và để lại 3 câu hỏi mở (luật hấp thụ của `with`, công thức `res` đúng là gì, SM1/SM2 có tương đương residuation hữu hạn hay không).

- **[[dn3-compare-with-BGA]]** — **Giải quyết trọn vẹn các câu hỏi mở của x3, chứng minh đầy đủ cả hai chiều:**
  - **Sec 2**: BGA ⟹ Polar Semiring, chứng minh sơ cấp đầy đủ (14 tiên đề BGA → 4 bổ đề trung gian → 11 tiên đề PS, 7 tiên đề trùng trực tiếp + 4 tiên đề cần lập luận thật).
  - **Sec 3**: **Incompatibility theorem** — không tồn tại $q\in\Gamma(\mathbb R^n)$ (kể cả hai đơn vị) sao cho residual sinh bởi `+` trùng đúng Fenchel polar `star`; phản ví dụ là chính $\Gamma(\mathbb R^n)$, không phải mô hình hữu hạn nhân tạo.
  - **Kết luận**: $\textbf{BGA}\subsetneq\textbf{Polar Semiring}$ — xác lập trọn vẹn, cả hai chiều, với phản ví dụ ở chiều ngược là mô hình trung tâm nhất của giải tích lồi.

### Mạch distribution profile

- **[[dn1-distribution-profile-of-polar-semiring]]** — Định nghĩa **distribution profile** $\operatorname{DP}(S)\in\{0,1\}^6$: vì polarity ghép cặp đối ngẫu $\otimes^*=\operatorname{parr}$, $\oplus^*=\&$, chỉ có **6 luật phân phối độc lập** (nguồn là $\otimes$ hoặc $\oplus$; đích là 1 trong 3 phép còn lại) cần kiểm — 6 luật còn lại suy ra tự động qua polarity. Dùng $\operatorname{DP}(S)$ như một "vân tay đại số" để phân loại/so sánh các mô hình polar semiring khác nhau.

- **[[dn2-distribution-profiles-of-convex-functions]]** — Tính cụ thể $\operatorname{DP}(\Gamma_0(\mathbb R^n))$: chỉ đúng 1/6 luật đúng (tensor phân phối trên plus — chính là SM1); **5 luật còn lại đều sai**, mỗi luật có phản ví dụ tường minh bằng hàm chỉ thị (indicator functions) của các tập lồi cụ thể trong $\mathbb R,\mathbb R^2$. Kết quả: $\operatorname{DP}(\Gamma_0)=(1,0,0;0,0,0)$ — một fingerprint rất "nghèo", có thể dùng làm bằng chứng cấu trúc độc lập (bên cạnh incompatibility theorem của [[dn3-compare-with-BGA]]) cho việc $\Gamma_0$ không phải là một lattice phân phối đầy đủ như BGA đòi hỏi.

### Tài liệu tham khảo

- **x2-algebra-of-MALL.pdf** — PDF tham khảo (không phải nội dung tự viết), nhiều khả năng là tài liệu nền cho định nghĩa BGA/MALL dùng ở [[x1-def-of-bounded-Girard-algebra]].

---

## Sec 2. Các kết quả đã chốt, sẵn sàng đưa vào bài báo

1. **Completion theorem** (headline của [[d00-positioning]]): $\Gamma(\mathbb R^n)=\{f=f^{**}\}$ là completion tối thiểu của closed convex proper, đóng hoàn toàn dưới $\max,+,*$ — thêm đúng 2 hằng số suy biến, không hơn không kém (định lý suy biến toàn cục đảm bảo không phát sinh case biên thứ ba).
2. **Tiên đề hóa 11 tiên đề + ~20 định lý đại số** độc lập với giải tích lồi (De Morgan, $(\&,\operatorname{parr})$ là monoid, thứ tự bộ phận, đơn điệu) — hạ tầng cần thiết để phát biểu chặt các câu hỏi cấu trúc.
3. **With/Parr = $\operatorname{conv}\min$/$\operatorname{cl}(f\square g)$ như hệ quả tự động** của cùng một cơ chế đại số (double-conjugate), không phải hai toán tử sửa lỗi độc lập — luật phân phối ghép giữa chúng (SM1 + De Morgan) được thừa hưởng miễn phí, không cần chứng minh giải tích riêng.
4. **$\textbf{BGA}\subsetneq\textbf{Polar Semiring}$, chứng minh cả hai chiều, neo vào tài liệu chuẩn** (Aglianò 2025) — kết quả sắc và có sức nặng citation hơn hẳn claim "PICS $\not\Rightarrow$ Girard quantale" ở try5.
5. **Distribution profile $\operatorname{DP}(\Gamma_0)=(1,0,0;0,0,0)$** — bằng chứng độc lập, cụ thể bằng phản ví dụ tường minh, củng cố thêm cho kết luận ở mục 4.

---

## Sec 3. Việc cần chốt trước khi viết báo (positioning gaps)

1. **Hợp nhất ba mạch nội dung.** [[d1-hierarchy]] và [[d2dan-y-paper-v1]] (outline chính) chưa hề nhắc tới BGA cụ thể (mục 2) hay distribution profile (mục 3) — trong khi đây là hai kết quả chặt và sắc nhất hiện có. Cần quyết định: đưa **BGA comparison** ([[dn3-compare-with-BGA]]) vào thay thế/làm rõ Sec 3.3 ("Related algebra") của [[d2dan-y-paper-v1]], và đưa **distribution profile** ([[dn1-distribution-profile-of-polar-semiring]]/[[dn2-distribution-profiles-of-convex-functions]]) vào Sec 3.2 hoặc một phụ lục riêng.
2. **Cân nhắc lại vị trí headline.** [[d00-positioning]] xếp impossibility result (không có residual) là "phát hiện phụ" — hợp lý khi kết quả chỉ là "không tồn tại $q$". Nhưng bản nâng cấp ở [[dn3-compare-with-BGA]] (BGA ⊊ PS, cả hai chiều, neo Aglianò 2025) là một **kết quả phân loại đại số hoàn chỉnh**, có thể đủ sức nặng để trở thành **contribution ngang hàng** với completion theorem, không chỉ là "phát hiện phụ" nữa — cần quyết định lại thứ bậc trước khi khóa outline.
3. **Giải quyết ghi chú $\Gamma(X)$ còn treo ở cuối [[d00-positioning]]**: chưa tra được nguồn Ekeland–Temam/Lieb có định nghĩa $\Gamma(X)$-kèm-$\pm\infty$ hay không, và nếu có thì họ đã chứng minh completion tối thiểu + đóng dưới cả 3 phép chưa. Đây là rủi ro về tính mới (novelty) của Sec 2 nếu không xử lý trước khi nộp.
4. **Đồng bộ quy ước ký hiệu Plus/With ↔ Meet/Join.** [[d0-notations]] dùng Plus=Meet=$\max$, With=Join=$\operatorname{conv}\min$ — ngược với bảng ở try4/README gốc của repo (Meet=With, Join=Plus). Cần chọn một quy ước duy nhất và áp dụng nhất quán trong toàn bộ paper (khuyến nghị: theo [[d0-notations]]/try6 vì đây là bản mới nhất và đã dùng xuyên suốt dn1–dn3).
5. **Sửa lỗi tham chiếu chéo nhỏ**: dòng mở đầu của [[dn3-compare-with-BGA]] ghi "Nối tiếp dn2 'Bounded Girard Algebra'" nhưng nội dung định nghĩa BGA thực chất nằm ở [[x1-def-of-bounded-Girard-algebra]] (dn2 hiện tại là distribution-profile-of-convex-functions) — có thể là dấu vết đổi tên file, cần rà lại toàn bộ tham chiếu chéo giữa các file trước khi ghép thành bản thảo.
