# important-notes

## Tóm tắt mục tiêu của folder

Ba file trong thư mục này là bản "publish" (đã chọn lọc, dùng để công bố) của cùng một chương trình nghiên cứu: chứng minh họ **regepi** trên $\overline X=\mathbb R^n\times(-\infty,+\infty]$ (đóng dưới bipolar Fenchel) tạo thành một **idempotent commutative semiring có polar tương thích**, rồi dùng cấu trúc đó làm mô hình ngữ nghĩa cho **MALL** (multiplicative-additive linear logic). Hai file `.md` là hai mảnh độc lập của lập luận (đại số trừu tượng, và hình học cụ thể); file `.tex` là bản tổng hợp đầy đủ nối cả hai mảnh tới tận Level 3 (logic).

---

## Sec 1. Mục tiêu chính mỗi file

- **[[from-algebra-to-logic]]** — Tiên đề hóa trừu tượng của $(X,\wedge,+,{}^*)$, độc lập với mọi mô hình hình học cụ thể: xác định tiên đề nào tự động có và tiên đề nào (đặc biệt điều kiện tương thích PM giữa polar và thứ tự) là giả thiết độc lập thật sự.

- **[[publish/important-notes/from-geometry-to-algebra]]** — Xây dựng cụ thể: từ quan hệ Fenchel $(x,r)\sim(y,s):\iff\langle x,y\rangle\le r+s$ trên $\overline X$, cô lập sáu tiên đề nguyên tử Pa1–Pa3 (đại số/order) và Pb1–Pb3 (hình học/topo), rồi chứng minh cả 11 tiên đề ICS chỉ cần Pa1–Pa3 + Pb1–Pb2 — không cần tính lồi (Pb3).

- **[[from-convexity-to-logic]]** *(phiên bản cũ hơn)* — File này chứa ý tưởng gốc ban đầu nối trực tiếp từ convexity sang logic. Do tính phức tạp, sau này được tách thành 02 file md. File này gồm các chứng minh nối toàn bộ chuỗi lập luận qua bốn tầng (vector space → hình học nguyên thủy → đại số chính → MALL), hệ thống hóa dưới dạng Propositions/Lemmas/Theorems, và đi xa hơn hai file `.md`: chứng minh bốn luật phân phối MALL (tensor/par/with/plus) và suy ra phép gán logic **bắt buộc**
$$ tensor \leftrightarrow Spator, par \leftrightarrow Fibor. $$

---

## Sec 2. Các kết quả chính đạt được

**Từ [[from-algebra-to-logic]]:**
- Polar tự động là song ánh đối hợp; $\wedge$ sinh thứ tự bộ phận mà $\wedge,+$ đơn điệu theo đó — độc lập hoàn toàn với polar.
- Polar tự động sinh semiring dẫn xuất thứ hai $(\vee,\times)$ và một phản-đẳng-cấu thứ tự *miễn phí* (cross-antitone) giữa hai thứ tự do $\wedge,\vee$ sinh ra.
- **Kết quả trung tâm:** (C1) $a\wedge b=a\iff a\vee b=b$, (C2) $\le=\le^*$, (Abs) luật hấp thụ, (PM) polar phản biến trên một thứ tự duy nhất — bốn phát biểu tương đương, nhưng **không** suy ra tự động từ các tiên đề còn lại; một phản ví dụ 4 phần tử xác nhận điều này.

**Từ [[publish/important-notes/from-geometry-to-algebra]]:**
- Involution ($a^{**}=a$) không phải tiên đề mà là *định lý* suy từ hai tiên đề Galois connection Pa1 (antitone) + Pa2 (extensive) — định lý Ore 1944.
- Định lý biểu diễn: trên regepi $\mathbb X$, hai phép toán thô $\cap$ và fiber-sum đã tự động đóng bipolar — phép đóng $(-)^{**}$ trong định nghĩa $\wedge,\oplus$ là dư thừa.
- Bảng quy về nguyên tử: nhóm M0–M3/P/PM chỉ cần Pa1+Pa2; S1/SM1 là hai tiên đề duy nhất cần Pb1 (đầy đủ Dedekind) + Pb2 (đóng topo); **tính lồi (Pb3) không được dùng ở bất kỳ tiên đề ICS nào**.

**Từ [[from-convexity-to-logic]]:**
- Kiến trúc bốn tầng tự chứa: mỗi tầng chỉ phụ thuộc tầng dưới qua đúng một phép $(-)^{**}$; Level 3 (logic) chỉ là một cách đọc ở cuối, không chi phối định nghĩa các tầng dưới.
- **Sự hợp nhất (P.U):** bốn toán tử tưởng độc lập $\{\wedge,\vee,\triangle,\bigtriangledown\}$ (meet, join, Fibor, Spator) thực chất chỉ có hai bậc tự do nguyên thủy ($\cap$/$\cup$, $+_{fib}$/$+_{sp}$) — join và Spator là đối ngẫu bipolar tự động của meet và Fibor.
- Bốn luật phân phối MALL (T7–T10) chỉ đúng **một nửa**: Fibor phân phối qua Meet (T7) và Spator phân phối qua Join (T8) đúng; hai chiều chéo (T9, T10) **thất bại**, được xác nhận bằng phản ví dụ hàm số cụ thể (piecewise-linear).
- Nửa đúng đó ép buộc phép gán logic duy nhất: **tensor$\leftrightarrow$Spator, par$\leftrightarrow$Fibor** — ngược với trực giác ban đầu của tài liệu gốc.
- Lỗ hổng đã biết, khoanh vùng rõ (Prop 10 → L.I → T11/T7 → T13/T8): kết hợp tính và đơn vị của Fibor/Spator (T11=M1, T13=M3) mới chỉ chứng minh được trên lớp con **proper** của $\mathbb X$ (hàm đại diện không nhận $-\infty$); trường hợp improper (như đơn vị $1_\wedge$) còn bỏ ngỏ — đúng câu hỏi mà [[remark_properness_and_residual_for_full_MALL]] (thư mục `ideas/proofs/try4-semiring`) đang khảo sát tiếp.
