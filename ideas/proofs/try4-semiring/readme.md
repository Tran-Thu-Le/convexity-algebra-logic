# try4-semiring

## Tóm tắt mục tiêu của folder

Thư mục này chứng minh rằng họ **regepi** (regularized preepi, tập con của $\overline X=\mathbb R^n\times(-\infty,+\infty]$ đóng dưới bipolar Fenchel $E=E^{**}$) tạo thành một **idempotent commutative semiring (ICS) trang bị polar đối hợp tương thích (PM)**, theo hai hướng bổ sung nhau:

1. **Hướng trừu tượng** — tiên đề hóa cấu trúc đại số $(X,\wedge,+,{}^*)$ ở mức tối thiểu, tách bạch kết quả nào *tự động* có từ tiên đề thuần túy và kết quả nào cần *giả thiết thêm* (đặc biệt là tính tương thích PM/luật hấp thụ).
2. **Hướng hình học cụ thể** — xuất phát từ quan hệ Fenchel $(x,r)\sim(y,s):\iff \langle x,y\rangle\le r+s$ trên $\overline X$, xây dựng regepi và chỉ ra cấu trúc ICS ấy **rơi ra tự động** từ một Galois connection, dùng đúng lượng "nguyên liệu" hình học/topo cần thiết cho mỗi tiên đề — rồi bắc cầu ngược lại ngôn ngữ convex analysis cổ điển (epigraph, liên hợp Fenchel, inf-convolution).

Mục tiêu xa hơn (chưa đóng) là dùng cấu trúc này làm mô hình ngữ nghĩa cho **MALL** (multiplicative-additive linear logic), việc mà [[remark_properness_and_residual_for_full_MALL]] đang khảo sát các lỗ hổng còn lại.

---

## Sec 1. Mục tiêu chính mỗi file

- **[[d1-from-algebra-to-logic]]** — Tiên đề hóa trừu tượng, độc lập với mọi mô hình hình học cụ thể: định nghĩa $(X,\wedge,+,{}^*)$ ở mức tối thiểu và xác định chính xác tiên đề nào là *miễn phí* (hệ quả tự động) và tiên đề nào là *độc lập thật sự* (đặc biệt là điều kiện tương thích PM giữa polar và thứ tự sinh bởi $\wedge$).

- **[[d2-from-geometry-to-algebra-main-v2]]** — Xây dựng ICS cụ thể từ hình học: định nghĩa preepi/regepi trên $\overline X$ qua quan hệ Fenchel, cô lập sáu tiên đề hình học/topo nguyên tử Pa1–Pa3 (đại số/order của polar) và Pb1–Pb3 (topo/giải tích), rồi chứng minh toàn bộ 11 tiên đề ICS (M0–M3, S1–S3, SM1–SM2, P, PM) chỉ dùng Pa1–Pa3 và Pb1–Pb2 — không cần tính lồi (Pb3).

- **[[d2b-research-program-fiber-sum-closure]]** — Research program riêng đào sâu đúng điểm nghẽn của Key Lemma trong [[d2-from-geometry-to-algebra-main-v2]] (fiber sum của hai regepi tự động là regepi): phát hiện chứng minh dãy-điểm gốc có lỗ hổng logic (ngầm giả định $A^{**}=\overline A^{\,top}$ — chính điều cần chứng minh), rồi dựng lại toàn bộ bằng con đường thay thế qua tính phân phối riêng lẻ của từng closure nguyên tử $U,C,T$ trên fiber sum.

- **[[d3-from-function-to-geometry]]** — Nối ngược cấu trúc regepi với convex analysis cổ điển: song ánh giữa regepi và hàm lồi-đóng-chính thường qua epigraph, và nhận diện các phép toán đại số dẫn xuất (meet, join, fibor, spator) tương ứng với $\max$, bao lồi đóng của $\min$, tổng hàm, và closure của inf-convolution.

- **[[remark_properness_and_residual_for_full_MALL]]** — Ghi chú về hai nhóm vấn đề còn mở trước khi cấu trúc trên có thể tuyên bố là mô hình đầy đủ của MALL: (1) tính *proper* của regepi có đóng dưới các phép toán và polar hay không; (2) phép kéo theo tuyến tính $\multimap$ có thỏa tính chất phổ dụng (adjunction) của closed monoidal category hay không.

- **old/** — các bản nháp trước của [[d2-from-geometry-to-algebra-main-v2]] (`from-geometry-to-algebra.md`, `from-geometry-to-algebra-add3.md`, `d2-from-geometry-to-algebra-main.md`, và bản PDF tương ứng), đã bị thay thế, giữ lại để tham khảo lịch sử lập luận.

---

## Sec 2. Các kết quả chính đạt được

**Từ [[d1-from-algebra-to-logic]]:**
- Polar tự động là song ánh đối hợp; $\wedge$ sinh thứ tự bộ phận mà $\wedge,+$ đơn điệu theo đó — độc lập hoàn toàn với polar.
- Polar tự động sinh semiring dẫn xuất thứ hai $(\vee,\times)$ và một phản-đẳng-cấu thứ tự *miễn phí* (Định lý T2, cross-antitone) giữa hai thứ tự do $\wedge$ và $\vee$ sinh ra.
- **Kết quả trung tâm:** bốn phát biểu (C1) $a\wedge b=a\iff a\vee b=b$, (C2) $\le\,=\,\le^*$, (Abs) luật hấp thụ, (PM) polar phản biến trên một thứ tự duy nhất — tương đương nhau (Định lý T3), nhưng **không** suy ra tự động từ các tiên đề còn lại; một phản ví dụ hữu hạn (4 phần tử) xác nhận điều này.

**Từ [[d2-from-geometry-to-algebra-main-v2]]:**
- Involution ($a^{**}=a$) không phải tiên đề mà là *định lý* suy từ hai tiên đề Galois connection Pa1 (antitone) + Pa2 (extensive) — định lý Ore 1944.
- Định lý biểu diễn (Sec 3): trên regepi $\mathbb X$, hai phép toán thô $\cap$ và fiber-sum đã tự động đóng bipolar — phép đóng $(-)^{**}$ trong định nghĩa $\wedge,\oplus$ là dư thừa.
- Bảng quy về nguyên tử (Sec 4.6): M0–M3/P/PM chỉ cần Pa1+Pa2; S1/SM1 là hai tiên đề duy nhất cần đến Pb1 (đầy đủ Dedekind) + Pb2 (đóng topo); **tính lồi (Pb3) không được dùng ở bất kỳ tiên đề ICS nào**.
- Định lý tổng hợp: $(\mathbb X,\wedge,\oplus,{}^*)$ là ICS đầy đủ, tương thích PM, chỉ từ Pa1–Pa3 + Pb1–Pb2.

**Từ [[d2b-research-program-fiber-sum-closure]]:**
- Xác định chính xác từng closure $U,C,T$ đứng ở bậc nào trên thang "tương thích với fiber sum" (Sec 6): $U$ phân phối vô điều kiện qua $+_{fib}$ ($U(E+_{fib}F)=U(E)+_{fib}U(F)$, bậc mạnh nhất); $\mathrm{conv}$ **không** phân phối như toán tử (phản ví dụ tường minh) nhưng đóng trên họ đã lồi sẵn (nếu $E,F$ lồi thì $E+_{fib}F$ tự động lồi, không cần điều kiện gì thêm); $T$ **không** phân phối và **không** đóng trên họ đã đóng sẵn (hai phản ví dụ "đường chéo", một-thớ và đa-thớ), chỉ đóng được với điều kiện bổ sung $H$ = "$U$-đóng + đáy đạt được".
- Dựng lại Key Lemma bằng một chuỗi thay-giá-trị-cụ-thể (không phải luật phân phối tổng quát): $A^{**}=T(C(U(A)))=T(C(A))=T(A)=A$ với $A:=E+_{fib}F$, mỗi bước dùng đúng kết quả tương ứng ở trên — cô lập tường minh "chi phí Hahn–Banach" vào đúng một chỗ (công thức phân rã $B^{**}=T(C(U(B)))$, trích dẫn Tran/Rockafellar, chưa tự kiểm chứng độc lập) thay vì để nó ẩn trong lập luận liminf gốc.
- Xác nhận lại: **tính lồi không cần thiết ở bước khó nhất** (bước $T$) — khớp với phát hiện "cột Pb3 trống" của [[d2-from-geometry-to-algebra-main-v2]], nhìn từ một góc độc lập.
- Để lại 5 việc còn mở (Sec 5), quan trọng nhất là kiểm chứng độc lập công thức phân rã $B^{**}=T(C(U(B)))$ (thay vì trích dẫn) và rà soát điều kiện properness một cách hệ thống — cùng mạch với các câu hỏi mở trong [[remark_properness_and_residual_for_full_MALL]].

**Từ [[d3-from-function-to-geometry]]:**
- Song ánh $\mathrm{Conv}(X)\leftrightarrow\mathbb X\setminus\{\emptyset,\overline X\}$ giữa hàm lồi-đóng-chính thường và regepi khác tầm thường, qua $\Phi(e)=\mathrm{epi}(e)$ (Định lý 12.1.1), dựa trên bổ đề cầu nối $\mathrm{epi}(g)^*=\mathrm{epi}(g^*)$.
- Join $E\vee F=(E\cup F)^{**}$ tương ứng $\mathrm{cl\,conv}(\min(e,f))$ — cần bao lồi đóng vì $\min$ phá vỡ tính lồi (Định lý 12.2.2).
- Spator $E\,\mathrm{spator}\,F=(E+_{sp}F)^{**}$ tương ứng $\mathrm{cl}(e\,\square\,f)$ (closure của inf-convolution) — chỉ cần đóng, không cần bao lồi, vì inf-convolution của hai hàm lồi vẫn lồi (Định lý 12.3.5).
- Điểm bất đối xứng nổi bật (Sec 12.4): $\wedge,+$ (fibor) giữ nguyên regularity miễn phí; các đối ngẫu $\vee,+_{sp}$ (spator) cần đóng bipolar để phục hồi tính đóng/lồi.

**Từ [[remark_properness_and_residual_for_full_MALL]]** *(vấn đề mở, chưa có kết quả đóng)*:
- Xác định chính xác hai nhóm câu hỏi còn chặn việc tuyên bố $\mathbb X$ là mô hình MALL: **Properness** (regepi improper, đặc biệt đơn vị $1_\wedge$, có phá vỡ tính đóng của fibor hay tính bảo toàn qua polar không) và **Residual** ($\multimap:=(E\bigtriangledown F^*)^*$ có thỏa universal property của adjoint hay chỉ là ứng viên công thức).
- Khuyến nghị thứ tự giải: Nhóm 1 (Properness, đặc biệt Mệnh đề 1.2 dễ nhất) trước Nhóm 2 (Residual), vì miền áp dụng của Nhóm 2 phụ thuộc kết luận của Nhóm 1.
