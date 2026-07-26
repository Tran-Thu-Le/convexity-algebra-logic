# try5-semiring-of-convex-functions

## Tóm tắt mục tiêu của folder

Thư mục này tiếp nối chương trình try4 (regepi là ICS+polar) nhưng bỏ qua tầng hình học trung gian: xây dựng trực tiếp trên **lớp hàm lồi đóng** $\Gamma(\mathbb R^n)=\{f:f=f^{**}\}$ (bipolar-đóng, không phải "lồi + epigraph đóng tô-pô" — hai khái niệm này **không** tương đương, xem [[two-kinds-of-closed-convex-functions]]), rằng $\Gamma(\mathbb R^n)$ với meet $=\max$, sum $=$ cộng điểm-theo-điểm, polar $=$ Fenchel conjugate là một **PICS** (Polar Idempotent Commutative Semiring) đầy đủ — cùng cấu trúc 11-tiên-đề đã tiên đề hóa trừu tượng ở [[from-axioms-to-theorems-v2]].

Mục tiêu xa hơn là kiểm tra xem cấu trúc PICS này có "nâng cấp" được thành mô hình **Girard quantale** (tức negation Fenchel có sinh được bởi một residual $a^*:=a\multimap q$ theo đúng nghĩa chuẩn) hay không — câu trả lời, chứng minh ở [[d1-paper-pics-kien-truc-mo-hinh-bat-kha-thi]], là **không**, với cả hai phép nhân tự nhiên duy nhất tương thích với polar. Đây là kết quả bất khả thi (impossibility) đầu tiên của toàn bộ chương trình, đặt giới hạn rõ ràng cho tham vọng "PICS ⟹ mô hình MALL đầy đủ".

---

## Sec 1. Mục tiêu chính mỗi file

- **[[two-kinds-of-closed-convex-functions]]** (bản Việt: **[[hai-kieu-dong-cua-ham-loi]]**) — Vạch rõ có **hai** khái niệm "đóng" khác nhau cho hàm lồi: UCT-đóng (lồi + epigraph đóng tô-pô) và bipolar-đóng ($f=f^{**}$). Chứng minh bao hàm **thật sự** $\{\text{bipolar-đóng}\}\subsetneq\{\text{UCT-đóng}\}$ bằng phản ví dụ tường minh ($f\equiv-\infty$ trên $[0,1]$, $+\infty$ ngoài), và chỉ ra "proper" trong định lý Fenchel–Moreau là một **quyết định định nghĩa** (thu hẹp phạm vi để hai khái niệm trùng nhau) chứ không phải hệ quả logic tự động. Đây là nền tảng để định nghĩa đúng $\Gamma(\mathbb R^n)$ dùng xuyên suốt các file sau.

- **[[from_axioms_theorems]]** — Bản nháp tiếng Việt đầu tiên của lý thuyết tiên đề PICS trừu tượng $(X,\wedge,+,{}^*,e_\wedge,e_+)$: phát biểu 11 tiên đề và chứng minh 10 định lý cơ bản (polar là song ánh đối hợp, $\wedge$ sinh thứ tự bộ phận, $e_\wedge$ lớn nhất, tính đơn điệu của $\wedge,+$, polar đảo thứ tự, join là supremum, cấu trúc dẫn xuất $(\vee,\times)$ qua polar). Đã bị thay thế bởi **[[from-axioms-to-theorems-v2]]**, giữ lại tham khảo lịch sử.

- **[[from-axioms-to-theorems-v2]]** — Bản đầy đủ (tiếng Anh), mở rộng file trên từ 10 lên **20 định lý**: thêm trọn nhóm De Morgan (4 đẳng thức đối ngẫu $\vee/\wedge$ và $\times/+$), định lý bán vành đối ngẫu $(\vee,e_\vee)$/$(\times,e_\times)$, phân phối, phần tử hấp thụ, và cả nhóm lý thuyết thứ tự (Thm 11–20: $\le$ và $\le_\vee$ đều là thứ tự bộ phận, $e_\wedge$/$e_\vee$ là max/min, tính đơn điệu, đảo thứ tự, hai thứ tự cảm sinh **trùng nhau** ($\le=\le_\vee$), luật hấp thụ). Đây chính là nguồn sinh ra bộ input/output kiểm chứng bằng Prover9/Mace4 ở `code/pics/`.

- **[[d3-from-convex-functions-to-semiring]]** — Hiện thực hóa 11 tiên đề **trực tiếp trên hàm** $f:\mathbb R^n\to\overline{\mathbb R}$ (không qua epigraph/regepi như try4): $(f\wedge g):=\max(f,g)$, $(f\oplus g):=f+g$ (bán vành giá trị max-plus), $f^*:=$ Fenchel conjugate, $e_\wedge:=\mathbf{-\infty}$, $e_\oplus:=\mathbf 0$. Chứng minh **9/11 tiên đề chỉ cần đại số sơ cấp** trên $(\overline{\mathbb R},\max,+)$ (không cần lồi/tách tập lồi); riêng **P** ($f^{**}=f$) cần đúng định lý Fenchel–Moreau (tách tập lồi), và **PM** rơi ra miễn phí chỉ từ P + một bổ đề đơn điệu-đảo sơ cấp.

- **[[d1-paper-pics-kien-truc-mo-hinh-bat-kha-thi]]** — Tài liệu tổng hợp, khép chương trình lại bằng ba phần: (1) định nghĩa lại PICS 11-tiên-đề và chỉ ra Boolean algebra, Girard quantale (Yetter/Rosenthal), involutive residuated lattice (Galatos) đều là các mô hình PICS *giàu hơn* (có residuation) — PICS là lớp **rộng nhất**, không đòi residuation; (2) tóm tắt lại kết quả $\Gamma(\mathbb R^n)$ là PICS đầy đủ (từ [[d3-from-convex-functions-to-semiring]]); (3) **hai định lý bất khả thi** (Định lý A, B): không tồn tại $q\in\Gamma(\mathbb R^n)$ nào khiến Fenchel polar là negation sinh bởi residual, với cả phép nhân $\oplus$ (tổng điểm-theo-điểm) lẫn $\square$ (inf-convolution) — hai phép nhân **duy nhất** tương thích tự nhiên với polar.

---

## Sec 2. Các kết quả chính đạt được

**Từ [[two-kinds-of-closed-convex-functions]] / [[hai-kieu-dong-cua-ham-loi]]:**
- Bipolar-đóng ⟹ UCT-đóng là chiều **miễn phí** (sup của họ affine luôn lồi-lsc); chiều ngược **sai** — phản ví dụ tường minh, không phải trường hợp biên hiếm gặp.
- Định lý suy biến toàn cục: nếu $f=f^{**}$ và có một điểm $f(x_0)=-\infty$ thì $f\equiv-\infty$ khắp nơi — giải thích *tại sao* phản ví dụ thất bại, thuần đại số của $\sup$, không cần lồi/tô-pô.
- "Proper" trong định lý Fenchel–Moreau là *quyết định định nghĩa* thu hẹp phạm vi để hai khái niệm "đóng" trùng nhau, không phải định lý; chiều khó thật sự ($\Rightarrow$, cần tách tập lồi) mới là nơi proper thật sự cần thiết.

**Từ [[from-axioms-to-theorems-v2]]** (thay thế [[from_axioms_theorems]]):
- 20 định lý đầy đủ suy từ đúng 11 tiên đề PICS, độc lập với mọi mô hình cụ thể: 4 đẳng thức De Morgan, $(\vee,e_\vee)$ là nửa-giàn giao hoán lũy đẳng, $(\times,e_\times)$ là monoid giao hoán, phân phối $\times$ trên $\vee$, $e_\vee$ hấp thụ, hai thứ tự cảm sinh bởi $\wedge$ và bởi $\vee$ **trùng nhau**.
- Kiểm chứng độc lập bằng Mace4 (`code/pics/`): hệ 11 tiên đề **consistent** (model domain size 2) và **cả 11 tiên đề đều độc lập** với nhau (không tiên đề nào suy ra từ 10 tiên đề còn lại).

**Từ [[d3-from-convex-functions-to-semiring]]:**
- $\big(\Gamma(\mathbb R^n),\wedge,\oplus,{}^*\big)$ với $e_\wedge=\mathbf{-\infty}$, $e_\oplus=\mathbf 0$ là một **PICS đầy đủ** (11/11 tiên đề).
- Điểm cấu trúc quan trọng: **9/11 tiên đề (M0–M3, S1–S3, SM1–SM2) chỉ là đại số sơ cấp** trên bán vành giá trị max-plus $(\overline{\mathbb R},\max,+)$ — không cần lồi hay tách tập lồi ở đâu cả.
- Chỉ **P** cần Fenchel–Moreau thật sự (định lý tách); **PM** thừa hưởng **miễn phí** từ P + một bổ đề đơn điệu-đảo sơ cấp (khác với tầng trừu tượng ở [[from-axioms-to-theorems-v2]], nơi PM/luật hấp thụ **không** tự động và cần giả thiết độc lập).

**Từ [[d1-paper-pics-kien-truc-mo-hinh-bat-kha-thi]]** *(kết quả trung tâm của folder)*:
- Sơ đồ phân tầng: involutive po-semigroup ⊃ involutive semiring ⊃ involutive residuated lattice ⊃ Girard quantale (complete) — tất cả ⊂ **PICS**. PICS chỉ đòi PM (điều kiện thứ tự thuần túy giữa $\le$ và $*$), không đòi residuation tồn tại.
- **Định lý A**: không tồn tại $q\in\Gamma(\mathbb R^n)$ sao cho $a\oplus b\preceq q\iff b\preceq a^*$ đúng với mọi $a,b$ — chứng minh bằng cách ép $q$ phải bằng $\|\cdot\|^2$ (bước 1) rồi loại chính $q=\|\cdot\|^2$ bằng phản ví dụ cụ thể (bước 2).
- **Định lý B**: tương tự, không tồn tại $q$ nào khiến $f\multimap q=f^*$ với $\multimap$ là residual (dạng kernel dịch chuyển) của inf-convolution $\square$ — chứng minh ép $q(x+y)=\langle x,y\rangle$ rồi chỉ ra vô lý (không thể là hằng số theo hướng tịnh tiến).
- **Hệ quả trung tâm:** ghép A+B — với **cả hai** phép nhân duy nhất tương thích tự nhiên với polar trên $\Gamma(\mathbb R^n)$, Fenchel conjugate **không thể** là negation sinh bởi residuation chuẩn. Vậy $\textbf{PICS}\not\Rightarrow\textbf{Girard quantale}$ (cùng phép nhân) — kết quả độc lập tiên đề nâng lên một tầng so với Định lý T3 của try4/d1 (ở đó chỉ PM không tự động; ở đây, cả tính chất "residuation-compatible" cũng không tự động), và phản ví dụ không phải bảng cộng nhân tạo hữu hạn mà là **mô hình quan trọng bậc nhất của giải tích lồi**.

---

## Sec 3. Ý nghĩa đối với chương trình MALL

Kết quả bất khả thi (Định lý A, B) không phủ nhận việc $\Gamma(\mathbb R^n)$ là mô hình MALL hợp lệ theo nghĩa PICS/polarized-semiring (điều đó vẫn đúng, xem README gốc của repo và [[../try4-semiring/remark_properness_and_residual_for_full_MALL]]) — nó chỉ ra rằng **negation không đến từ residuation kiểu Girard-quantale truyền thống** trên mô hình này. Điều này củng cố hướng đi đã mở ra ở cuối try4 (residual của inf-convolution và Fenchel polar sống trên hai *kernel* khác nhau — bilinear vs. dịch chuyển): việc thiếu residuation chuẩn không phải là lỗ hổng cần vá, mà là bằng chứng thêm rằng PICS đúng là khung tiên đề *tổng quát hơn thật sự* — rộng hơn cả những gì lý thuyết quantale/residuated-lattice truyền thống đòi hỏi.
