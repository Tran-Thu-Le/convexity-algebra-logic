# try4-semiring

## Tóm tắt mục tiêu của folder

Thư mục này chứng minh rằng họ **regepi** (regularized preepi, tập con của $\overline X=\mathbb R^n\times(-\infty,+\infty]$ đóng dưới bipolar Fenchel $E=E^{**}$) tạo thành một **idempotent commutative semiring (ICS) trang bị polar đối hợp tương thích (PM)**, theo hai hướng bổ sung nhau:

1. **Hướng trừu tượng** — tiên đề hóa cấu trúc đại số $(X,\wedge,+,{}^*)$ ở mức tối thiểu, tách bạch kết quả nào *tự động* có từ tiên đề thuần túy và kết quả nào cần *giả thiết thêm* (đặc biệt là tính tương thích PM/luật hấp thụ).
2. **Hướng hình học cụ thể** — xuất phát từ quan hệ Fenchel $(x,r)\sim(y,s):\iff \langle x,y\rangle\le r+s$ trên $\overline X$, xây dựng regepi và chỉ ra cấu trúc ICS ấy **rơi ra tự động** từ một Galois connection, dùng đúng lượng "nguyên liệu" hình học/topo cần thiết cho mỗi tiên đề — rồi bắc cầu ngược lại ngôn ngữ convex analysis cổ điển (epigraph, liên hợp Fenchel, inf-convolution).

Mục tiêu xa hơn (chưa đóng) là dùng cấu trúc này làm mô hình ngữ nghĩa cho **MALL** (multiplicative-additive linear logic), việc mà [[remark_properness_and_residual_for_full_MALL]] đang khảo sát các lỗ hổng còn lại.

---

## Sec 1. Mục tiêu chính mỗi file

- **[[d1-from-algebra-to-logic]]** — Tiên đề hóa trừu tượng, độc lập với mọi mô hình hình học cụ thể: định nghĩa $(X,\wedge,+,{}^*)$ ở mức tối thiểu và xác định chính xác tiên đề nào là *miễn phí* (hệ quả tự động) và tiên đề nào là *độc lập thật sự* (đặc biệt là điều kiện tương thích PM giữa polar và thứ tự sinh bởi $\wedge$).

- **[[d2a-from-geometry-to-algebra-main-v2]]** — Xây dựng ICS cụ thể từ hình học: định nghĩa preepi/regepi trên $\overline X$ qua quan hệ Fenchel, cô lập sáu tiên đề hình học/topo nguyên tử Pa1–Pa3 (đại số/order của polar) và Pb1–Pb3 (topo/giải tích), rồi chứng minh toàn bộ 11 tiên đề ICS (M0–M3, S1–S3, SM1–SM2, P, PM) chỉ dùng Pa1–Pa3 và Pb1–Pb2 — không cần tính lồi (Pb3). *(Bản đầu, chỉ làm việc trên kernel Fenchel cụ thể $\langle x,y\rangle$; xem v3–v4 để biết bước tổng quát hóa tiếp theo.)*

- **[[d2a-from-geometry-to-algebra-main-v3]]** — Viết lại toàn bộ v2 trên **kernel trừu tượng** $c(x,y)$ thay vì $\langle x,y\rangle$ cụ thể: chứng minh cả 11 tiên đề ICS của v2 đứng vững nguyên vẹn cho bất kỳ $c$ nào thỏa đúng hai điều kiện — **đối xứng** (nuôi Pa2/involution) và **nửa liên tục dưới riêng biến** (nuôi Pb2/đóng) — không cần song tuyến tính, không cần lồi ở bất kỳ đâu. Nhận diện residual của inf-convolution ($f\multimap h$) là **cùng một định lý tiên đề**, chỉ khác kernel (kernel dịch chuyển $c_h(x,y):=h(x+y)$ thay cho kernel bilinear); chứng minh chặt hai họ kernel (bilinear/dịch chuyển) rời nhau, và không tồn tại $\bot$ nào biến $(\cdot)\multimap\bot$ thành đúng Fenchel polar.

- **[[d2a-from-geometry-to-algebra-main-v4]]** — Bản kiến trúc chốt: đặt toàn bộ lý thuyết dưới lăng kính **bifunction/marginal** (Phần 0) — mọi hàm một biến là phép chiếu (partial infimum) của một bifunction hai biến $H(x,y)$, giải thích vì sao đóng tô pô (Pb2) là bắt buộc về **cấu trúc** (ảnh của tập đóng qua phép chiếu có thể không đóng) trong khi lồi (Pb3) thì không hề. Xác định chính xác điều kiện lồi "quay lại" như hệ quả: chỉ khi kernel phân rã $c=h\circ T$ với **cả** $T$ (tương tác hai biến) **lẫn** $h$ (profile một biến) đều affine đồng thời — đặc trưng riêng của dot product, không phải quy luật chung. Liên hệ negation kiểu Girard (dualizing element $\bot$ trong quantale) với $c$-transform Kantorovich của optimal transport, thống nhất ba lý thuyết (residual logic, Fenchel duality, optimal transport) dưới một cơ chế nucleus/Galois connection duy nhất.

- **[[d2c-regepi-properness-K-abstract]]** — Trừu tượng hóa không gian đích $K$ (thay $(-\infty,+\infty]$ cụ thể) thành một "ngưỡng-đại số" (threshold algebra) $(K,\le,+,0,\top,\tau)$; chứng minh $K=\mathbb R\cup\{\top\}$ (không đáy) là lựa chọn *duy nhất* trong các ứng viên tự nhiên thỏa **đồng thời** mọi tiên đề, và định nghĩa lại properness chính xác là $E\ne e_\wedge\wedge E\ne e_\wedge^*$ (hội của hai điều kiện độc lập, không phải một điều kiện thớ đơn lẻ như từng nghĩ). Với $K$ đúng, properness trở thành một **định lý tự động** (Định lý suy biến toàn thớ), không phải tiên đề phải thêm — trả lời phần lớn Nhóm 1 (Mệnh đề 1.1–1.3) của [[remark_properness_and_residual_for_full_MALL]].

- **[[d2b-research-program-fiber-sum-closure]]** — Research program riêng đào sâu đúng điểm nghẽn của Key Lemma trong [[d2a-from-geometry-to-algebra-main-v2]] (fiber sum của hai regepi tự động là regepi): phát hiện chứng minh dãy-điểm gốc có lỗ hổng logic (ngầm giả định $A^{**}=\overline A^{\,top}$ — chính điều cần chứng minh), rồi dựng lại toàn bộ bằng con đường thay thế qua tính phân phối riêng lẻ của từng closure nguyên tử $U,C,T$ trên fiber sum.

- **[[d3-from-function-to-geometry]]** — Nối ngược cấu trúc regepi với convex analysis cổ điển: song ánh giữa regepi và hàm lồi-đóng-chính thường qua epigraph, và nhận diện các phép toán đại số dẫn xuất (meet, join, fibor, spator) tương ứng với $\max$, bao lồi đóng của $\min$, tổng hàm, và closure của inf-convolution.

- **[[remark_properness_and_residual_for_full_MALL]]** — Ghi chú về hai nhóm vấn đề còn mở trước khi cấu trúc trên có thể tuyên bố là mô hình đầy đủ của MALL: (1) tính *proper* của regepi có đóng dưới các phép toán và polar hay không; (2) phép kéo theo tuyến tính $\multimap$ có thỏa tính chất phổ dụng (adjunction) của closed monoidal category hay không.

- **old/** — các bản nháp trước của [[d2a-from-geometry-to-algebra-main-v2]] (`from-geometry-to-algebra.md`, `from-geometry-to-algebra-add3.md`, `d2-from-geometry-to-algebra-main.md`, và bản PDF tương ứng), đã bị thay thế, giữ lại để tham khảo lịch sử lập luận.

---

## Sec 2. Các kết quả chính đạt được

**Từ [[d1-from-algebra-to-logic]]:**
- Polar tự động là song ánh đối hợp; $\wedge$ sinh thứ tự bộ phận mà $\wedge,+$ đơn điệu theo đó — độc lập hoàn toàn với polar.
- Polar tự động sinh semiring dẫn xuất thứ hai $(\vee,\times)$ và một phản-đẳng-cấu thứ tự *miễn phí* (Định lý T2, cross-antitone) giữa hai thứ tự do $\wedge$ và $\vee$ sinh ra.
- **Kết quả trung tâm:** bốn phát biểu (C1) $a\wedge b=a\iff a\vee b=b$, (C2) $\le\,=\,\le^*$, (Abs) luật hấp thụ, (PM) polar phản biến trên một thứ tự duy nhất — tương đương nhau (Định lý T3), nhưng **không** suy ra tự động từ các tiên đề còn lại; một phản ví dụ hữu hạn (4 phần tử) xác nhận điều này.

**Từ [[d2a-from-geometry-to-algebra-main-v2]]:**
- Involution ($a^{**}=a$) không phải tiên đề mà là *định lý* suy từ hai tiên đề Galois connection Pa1 (antitone) + Pa2 (extensive) — định lý Ore 1944.
- Định lý biểu diễn (Sec 3): trên regepi $\mathbb X$, hai phép toán thô $\cap$ và fiber-sum đã tự động đóng bipolar — phép đóng $(-)^{**}$ trong định nghĩa $\wedge,\oplus$ là dư thừa.
- Bảng quy về nguyên tử (Sec 4.6): M0–M3/P/PM chỉ cần Pa1+Pa2; S1/SM1 là hai tiên đề duy nhất cần đến Pb1 (đầy đủ Dedekind) + Pb2 (đóng topo); **tính lồi (Pb3) không được dùng ở bất kỳ tiên đề ICS nào**.
- Định lý tổng hợp: $(\mathbb X,\wedge,\oplus,{}^*)$ là ICS đầy đủ, tương thích PM, chỉ từ Pa1–Pa3 + Pb1–Pb2.

**Từ [[d2a-from-geometry-to-algebra-main-v3]]:**
- Định lý trung tâm mới: $(\mathbb X_c,\wedge,\oplus,{}^{*_c})$ là ICS đầy đủ $\iff$ $c$ đối xứng và nửa liên tục dưới riêng biến — **chỉ hai điều kiện**, không có lồi, không có song tuyến tính.
- Residual của inf-convolution $f\multimap h = f^{c_h}$ (kernel dịch chuyển $c_h(x,y)=h(x+y)$) và Fenchel conjugate $f^*$ (kernel bilinear $\langle x,y\rangle$) là **hai điểm trong cùng một không gian kernel**, cùng tuân một định lý tiên đề — không còn là hai lý thuyết song song tình cờ giống nhau.
- Đối xứng của $c$ (không phải song tuyến tính) mới là điều kiện thật sự nuôi Pa2/involution; hai unit $e_\wedge,e_\oplus$ có thể suy biến (sụp làm một) tùy kernel — một hiện tượng không xuất hiện trong trường hợp Fenchel thuần túy của v2.

**Từ [[d2a-from-geometry-to-algebra-main-v4]]:**
- Phần 0 (lăng kính bifunction/marginal): $f(x)=\inf_y H(x,y)$; $\mathrm{epi}(f)$ là ảnh chiếu của $\mathrm{epi}(H)$ qua $\Phi:(x,y,t)\mapsto(x,t)$ — Pb2 (đóng tô pô) bắt buộc vì ảnh chiếu của tập đóng nói chung không đóng (phản ví dụ chuẩn $\{xy\ge1,x>0\}$).
- Mọi kernel "có ý nghĩa" có dạng $c=h\circ T$ ($T$ đối xứng cố định, $h$ profile tự do); lồi (Pb3) chỉ là hệ quả tự động khi **cả** $T$ **lẫn** $h$ đều affine cùng lúc — đúng đặc trưng riêng của $\langle x,y\rangle$ (kernel bilinear + $h=\mathrm{id}$), không phải quy luật chung của $c$-conjugate.
- Cầu nối then chốt (V.2): negation kiểu Girard ($\bot=h$ trong quantale $(\overline{\mathbb R}^X,\square,\multimap)$) $=$ $c$-conjugate kernel dịch chuyển $=$ $c$-transform $\varphi^c(y)=\sup_x(c(x,y)-\varphi(x))$ của Kantorovich duality trong optimal transport; cost tuyến tính khôi phục đúng đối ngẫu Fenchel–Legendre, cost bậc hai $\|x-y\|^2/2$ cho định lý Brenier — residual logic, giải tích lồi tổng quát, và optimal transport là **cùng một cơ chế nucleus/Galois**, chỉ khác nhau ở thứ tự nền ($\preceq$ trên hàm hay ràng buộc trên độ đo).

**Từ [[d2c-regepi-properness-K-abstract]]:**
- $K=\mathbb R\cup\{\top\}$ rút gọn về đúng hai dữ kiện gốc N1 (nền chuẩn $=\mathbb R$) + N2 (đỉnh hấp thụ $\top$); tám tiên đề K còn lại (K2–K8, K10) đều là *định lý*, không phải giả thiết độc lập — kể cả K8 (liên tục), vốn suy ra thuần túy từ K1+K4+K6.
- Properness không "rò rỉ" vào phương trình $E^{**}=E$ (đúng với mọi $E\in\mathbb X$, kể cả hai phần tử không proper $e_\wedge,e_\wedge^*$) — nó chỉ cần thiết ở tầng sau, nơi thao tác trực tiếp với $f^*$ (như $\partial f\ne\emptyset$ hay công thức tổng không có duality gap).
- Thêm đáy $\bot=\inf K$ vào $K$ (ví dụ $K_3=[-\infty,+\infty]$) luôn phá vỡ K8 tại góc $(\bot,\top)$ — xác định chính xác "cái giá" phải trả nếu muốn mở rộng $K$, giải thích vì sao quy ước Rockafellar ($K_2$, không đáy) là lựa chọn đúng, không phải tùy tiện.

**Từ [[d2b-research-program-fiber-sum-closure]]:**
- Xác định chính xác từng closure $U,C,T$ đứng ở bậc nào trên thang "tương thích với fiber sum" (Sec 6): $U$ phân phối vô điều kiện qua $+_{fib}$ ($U(E+_{fib}F)=U(E)+_{fib}U(F)$, bậc mạnh nhất); $\mathrm{conv}$ **không** phân phối như toán tử (phản ví dụ tường minh) nhưng đóng trên họ đã lồi sẵn (nếu $E,F$ lồi thì $E+_{fib}F$ tự động lồi, không cần điều kiện gì thêm); $T$ **không** phân phối và **không** đóng trên họ đã đóng sẵn (hai phản ví dụ "đường chéo", một-thớ và đa-thớ), chỉ đóng được với điều kiện bổ sung $H$ = "$U$-đóng + đáy đạt được".
- Dựng lại Key Lemma bằng một chuỗi thay-giá-trị-cụ-thể (không phải luật phân phối tổng quát): $A^{**}=T(C(U(A)))=T(C(A))=T(A)=A$ với $A:=E+_{fib}F$, mỗi bước dùng đúng kết quả tương ứng ở trên — cô lập tường minh "chi phí Hahn–Banach" vào đúng một chỗ (công thức phân rã $B^{**}=T(C(U(B)))$, trích dẫn Tran/Rockafellar, chưa tự kiểm chứng độc lập) thay vì để nó ẩn trong lập luận liminf gốc.
- Xác nhận lại: **tính lồi không cần thiết ở bước khó nhất** (bước $T$) — khớp với phát hiện "cột Pb3 trống" của [[d2a-from-geometry-to-algebra-main-v2]], nhìn từ một góc độc lập.
- Để lại 5 việc còn mở (Sec 5), quan trọng nhất là kiểm chứng độc lập công thức phân rã $B^{**}=T(C(U(B)))$ (thay vì trích dẫn) và rà soát điều kiện properness một cách hệ thống — cùng mạch với các câu hỏi mở trong [[remark_properness_and_residual_for_full_MALL]].

**Từ [[d3-from-function-to-geometry]]:**
- Song ánh $\mathrm{Conv}(X)\leftrightarrow\mathbb X\setminus\{\emptyset,\overline X\}$ giữa hàm lồi-đóng-chính thường và regepi khác tầm thường, qua $\Phi(e)=\mathrm{epi}(e)$ (Định lý 12.1.1), dựa trên bổ đề cầu nối $\mathrm{epi}(g)^*=\mathrm{epi}(g^*)$.
- Join $E\vee F=(E\cup F)^{**}$ tương ứng $\mathrm{cl\,conv}(\min(e,f))$ — cần bao lồi đóng vì $\min$ phá vỡ tính lồi (Định lý 12.2.2).
- Spator $E\,\mathrm{spator}\,F=(E+_{sp}F)^{**}$ tương ứng $\mathrm{cl}(e\,\square\,f)$ (closure của inf-convolution) — chỉ cần đóng, không cần bao lồi, vì inf-convolution của hai hàm lồi vẫn lồi (Định lý 12.3.5).
- Điểm bất đối xứng nổi bật (Sec 12.4): $\wedge,+$ (fibor) giữ nguyên regularity miễn phí; các đối ngẫu $\vee,+_{sp}$ (spator) cần đóng bipolar để phục hồi tính đóng/lồi.

**Từ [[remark_properness_and_residual_for_full_MALL]]** *(vấn đề mở, chưa có kết quả đóng)*:
- Xác định chính xác hai nhóm câu hỏi còn chặn việc tuyên bố $\mathbb X$ là mô hình MALL: **Properness** (regepi improper, đặc biệt đơn vị $1_\wedge$, có phá vỡ tính đóng của fibor hay tính bảo toàn qua polar không) và **Residual** ($\multimap:=(E\bigtriangledown F^*)^*$ có thỏa universal property của adjoint hay chỉ là ứng viên công thức).
- Khuyến nghị thứ tự giải: Nhóm 1 (Properness, đặc biệt Mệnh đề 1.2 dễ nhất) trước Nhóm 2 (Residual), vì miền áp dụng của Nhóm 2 phụ thuộc kết luận của Nhóm 1.

---

## Sec 3. Sự chuyển biến nhận thức: Convexity như thuộc tính phụ tùy của Kernel, và cầu nối Residual–$c$-transform

Đọc lại toàn bộ folder theo trình tự thời gian (d1 → d2a-v2 → remark/d2b → d2a-v3 → d2a-v4 → d2c) cho thấy một đường tiến hóa nhận thức rõ rệt, không chỉ là các kết quả rời rạc.

### 3.1. Xuất phát điểm: convexity được xem là điều kiện gần như hiển nhiên của mô hình

Ở [[d2a-from-geometry-to-algebra-main-v2]], convexity (Pb3: $A^{**}$ lồi) được chứng minh cẩn thận cùng lúc với Pb1, Pb2 — như một tính chất "đương nhiên phải có" của polar Fenchel, vì $H_p=\{(x,r):\langle x,y\rangle\le r+s\}$ là nửa-không-gian affine, quá tự nhiên để nghi ngờ. Nhưng bảng quy-về-nguyên-tử ở Sec 4.6 của chính tài liệu này đã âm thầm gài một quả bom: **cột Pb3 trống tuyệt đối trên cả 11 hàng tiên đề ICS**. Không một định lý nào trong M0–M3, S1–S3, SM1–SM2, P, PM viện dẫn đến nó. [[d2b-research-program-fiber-sum-closure]] xác nhận lại phát hiện này từ một góc độc lập: ngay ở bước khó nhất của Key Lemma (đóng $T$ của fiber sum), lồi cũng không cần thiết.

Đây là hạt giống của toàn bộ chuyển biến sau này: **lồi được chứng minh là đúng, nhưng không bao giờ được dùng.** Một tính chất thật của $*$ mà đại số không đòi hỏi là dấu hiệu cho thấy đại số đang mô tả một cấu trúc rộng hơn ranh giới "hình học lồi" mà ta ngỡ nó thuộc về.

### 3.2. Vết nứt thứ hai: residual của logic không khớp khuôn Fenchel

Song song, [[remark_properness_and_residual_for_full_MALL]] để lại một câu hỏi mở về phép kéo theo tuyến tính $\multimap:=(E\bigtriangledown F^*)^*$ trong MALL — liệu nó có thỏa universal property của adjoint. Khi đối chiếu công thức này với residual cổ điển của inf-convolution $f\multimap h(z)=\sup_y(h(z+y)-f(y))$, nhận ra công thức residual **không phải Fenchel polar được viết lại** — nó dùng một quan hệ $\sim$ khác, sinh bởi $h(x+y)$ (một kernel *dịch chuyển*) thay vì $\langle x,y\rangle$ (kernel *bilinear*). Hai công thức trông giống hệt nhau ở dạng $\sup(\cdot-\cdot)$ nhưng sống trên hai kernel khác nhau về bản chất.

### 3.3. Bước ngoặt: kernel trở thành đối tượng nghiên cứu chính

[[d2a-from-geometry-to-algebra-main-v3]] là nơi hai vết nứt trên hợp lại thành một phát hiện duy nhất. Thay vì hỏi "polar Fenchel có tính chất gì", tài liệu lật ngược câu hỏi: **kernel $c(x,y)$ cần thỏa điều kiện tối thiểu nào để toàn bộ 11 tiên đề ICS đứng vững?** Câu trả lời (đóng khung lại toàn bộ Sec 2 của v2):

$$\text{ICS đầy đủ} \iff c \text{ đối xứng} \ (\text{nuôi Pa2/involution}) \ + \ c(\cdot,y) \text{ nửa liên tục dưới} \ (\text{nuôi Pb2/đóng}).$$

Không song tuyến tính, không lồi, không liên tục toàn phần. Dot product $\langle x,y\rangle$ chỉ là **một điểm đặc biệt** trong không gian kernel rộng hơn nhiều — đối xứng nhờ song tuyến tính (một trùng hợp cấu trúc, không phải yêu cầu), liên tục toàn phần (dư thừa so với lsc), affine cả hai chiều ("miễn phí" thừa mứa). Kernel dịch chuyển $c_h(x,y)=h(x+y)$ là điểm thứ hai, hoàn toàn hợp lệ, và chính là nơi residual của inf-convolution sống — với $h$ đóng vai trò "profile" tự do, không cần lồi để đại số đứng vững. **Đây là nơi "kernel" ngừng là công cụ trung gian để rút gọn chứng minh Fenchel, và trở thành đối tượng trung tâm mà cả Fenchel lẫn residual chỉ là hai instance.**

### 3.4. Truy đến gốc rễ: khi nào lồi thật sự cần, và tại sao đóng thì không thể thiếu

[[d2a-from-geometry-to-algebra-main-v4]] đào sâu thêm một tầng, trả lời câu hỏi "nếu lồi không cần, vậy cái gì thật sự phân biệt Pb2 (đóng) với Pb3 (lồi)?" bằng lăng kính **bifunction/marginal**: mọi hàm một biến $f(x)=\inf_y H(x,y)$ là phép chiếu của một bifunction hai biến, và $\mathrm{epi}(f)$ là ảnh chiếu tô-pô của $\mathrm{epi}(H)$. Ảnh chiếu của một tập đóng nói chung **không đóng** (phản ví dụ chuẩn $\{(x,y):xy\ge1,x>0\}$ chiếu xuống $(0,\infty)$ — mở) — đây là lý do cấu trúc, không phải ngẫu nhiên kỹ thuật, khiến Pb2 không thể bỏ dù Pb3 đã bị loại hoàn toàn khỏi kiến trúc lõi.

Và khi nào lồi "quay lại"? Chỉ khi kernel phân rã $c=h\circ T$ với **cả** ánh xạ tương tác $T$ **lẫn** profile $h$ đều affine đồng thời — đúng đặc trưng riêng của dot product ($T=\langle\cdot,\cdot\rangle$ bilinear, $h=\mathrm{id}$), không phải quy luật chung. Nói cách khác: **dot product không "được" tính lồi nhờ may mắn hình học — nó là điểm duy nhất trong không gian kernel nơi hai tầng affine trùng nhau, khiến lồi sụp ra hoàn toàn miễn phí.** Convexity, từ chỗ được ngầm coi là điều kiện định nghĩa của mô hình lồi/MALL, hạ xuống thành một hệ quả phụ tùy của một lựa chọn kernel cụ thể.

### 3.5. Cầu nối Residual (logic) ↔ $c$-transform (tối ưu)

Hệ quả trực tiếp và rõ nhất của bước tổng quát hóa kernel là một cầu nối ba chiều (Phần V.2 của v4):

- **Trong linear logic**, negation kiểu Girard chọn một *dualizing element* $\bot$ trong quantale $(\overline{\mathbb R}^X,\square,\multimap)$: $f^\bot:=f\multimap\bot$. Chọn $\bot=h$ cho đúng $f^\bot=f\multimap h=f^{c_h}$ — tức **negation chính là $c$-conjugate với kernel dịch chuyển**.
- **Trong optimal transport**, Kantorovich duality định nghĩa **$c$-transform** cho cost function $c(x,y)$ *bất kỳ*: $\varphi^c(y):=\sup_x(c(x,y)-\varphi(x))$ — đúng cùng công thức, đúng từng ký tự, chỉ thay $\preceq$ trên hàm bằng ràng buộc tích phân $\varphi\oplus\psi\le c$ trên độ đo.
- **Trong giải tích lồi cổ điển**, $c(x,y)=\langle x,y\rangle$ (cost tuyến tính) khôi phục đúng đối ngẫu Fenchel–Legendre; $c(x,y)=\|x-y\|^2/2$ (cost bậc hai) cho định lý Brenier — cả hai đều là trường hợp riêng của cùng kernel "cầu nối" $\|x-y\|^2$ đã xuất hiện ở Phần III của v4 ($\|x-y\|^2=\|x\|^2+\|y\|^2-2\langle x,y\rangle$ trộn cả hai họ bilinear và dịch chuyển).

Ba lý thuyết — residual/negation của MALL, $c$-conjugate của giải tích lồi tổng quát, $c$-transform của optimal transport — hóa ra là **cùng một cơ chế nucleus/Galois connection** ($A\subseteq A^{**}$, phản biến, đối hợp), khác nhau duy nhất ở loại thứ tự nền mà chúng tác động lên (thứ tự điểm-theo-điểm trên hàm, hay ràng buộc tích phân trên độ đo). Câu hỏi $\multimap$ có phải adjoint thật sự (Nhóm 2 của [[remark_properness_and_residual_for_full_MALL]]) nay có một câu trả lời về *hình dạng*: nó là instance kernel-dịch-chuyển của đúng định lý adjunction Pa1+Pa2 đã chứng minh tổng quát ở v3/v4 — dù việc kiểm chứng đầy đủ universal property trên $\mathbb X$ cụ thể (không chỉ trên hàm) vẫn còn mở.

### 3.6. Tác động ngược lên câu hỏi properness

Cùng lúc, [[d2c-regepi-properness-K-abstract]] áp dụng đúng tinh thần "trừu tượng hóa để lộ điều kiện tối thiểu" — lần này không phải lên kernel $c$ mà lên **không gian đích** $K$ (thay $(-\infty,+\infty]$ cụ thể). Kết quả: $K=\mathbb R\cup\{\top\}$ không đáy là lựa chọn *duy nhất* thỏa mọi tiên đề, và với lựa chọn đó, **properness không còn là một giả thiết phải kiểm riêng (như Nhóm 1 của remark file lo ngại) mà là một định lý tự động** (suy biến toàn thớ, Sec 2 của d2c) — thu hẹp đáng kể phạm vi những gì Nhóm 1 còn phải làm trước khi giải Nhóm 2 (Residual).

### 3.7. Tóm một câu

Nhận thức đã đi từ **"convexity là điều kiện định nghĩa của mô hình lồi/MALL, residual là một công thức phụ cần kiểm riêng"** sang **"convexity là thuộc tính phụ tùy của đúng một điểm (dot product) trong không gian kernel đối xứng+lsc rộng hơn nhiều, và residual — cùng với $c$-transform của optimal transport — chỉ là những điểm khác trong CHÍNH không gian kernel đó, cùng tuân một cơ chế nucleus/Galois duy nhất."**
