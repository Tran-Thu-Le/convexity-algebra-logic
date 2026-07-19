# Regepi là một Idempotent Commutative Semiring có Polar
### Bản v4 — Kiến trúc chốt: Kernel Đối xứng + Nửa liên tục dưới (KHÔNG cần Lồi)

---

## Phần 0 — Lăng kính nền: mọi thứ là phép chiếu của một cấu trúc hai biến

**Quan sát nền tảng** (thay cho lời mở đầu): đối tượng nguyên thủy không phải $f:X\to\overline{\mathbb R}$, mà là một **bifunction** $H:X\times X\to\overline{\mathbb R}$, và $f$ chỉ là **marginal** (partial infimum) của $H$:
$$
f(x)=\inf_y H(x,y).
$$

**Định lý (partial minimization).** $H$ jointly convex $\Rightarrow$ $f$ lồi. Áp cho $H(x,y)=f_0(y)+g(x-y)$ (tổng hai hàm lồi trên $X\times X$, luôn jointly convex) cho lại đúng định lý "inf-convolution lồi" — **không phải sự kiện riêng của $\square$**, mà hệ quả của một sự kiện tổng quát hơn.

**Viết lại bằng epigraph — cấu trúc chiếu lộ rõ:**
$$
\operatorname{epi}(f)=\Phi\bigl(\operatorname{epi}(H)\bigr),\qquad \Phi:\ (x,y,t)\mapsto(x,t)\ \text{(quên biến }y\text{)}.
$$

**Hệ quả quan trọng nhất của lăng kính này:** tính đóng topo (Pb2) không phải một giả thiết "phụ", mà là điều kiện bắt buộc để tránh hiện tượng phổ quát **"ảnh của tập đóng qua phép chiếu không tự đóng"** (ví dụ chuẩn: $\{(x,y):xy\ge1,x>0\}$ đóng nhưng chiếu lên trục $x$ cho $(0,\infty)$ — mở). Đây là lý do cấu trúc, không phải kỹ thuật, khiến Pb2 **không thể bỏ** dù đã bỏ hoàn toàn tính lồi (Pb3). Toàn bộ Phần I–IV dưới đây được dựng với tinh thần: **giữ đúng-và-chỉ-đúng những gì phép chiếu đòi hỏi, bỏ mọi thứ khác.**

---

## Phần I — Kernel, Quan hệ, Polar: tiên đề hóa từ gốc (không giả thiết lồi ở bất kỳ đâu)

### I.1. Định nghĩa

$$\overline X:=\mathbb R^n\times(-\infty,+\infty],\qquad c:X\times X\to\overline{\mathbb R}\ \text{(kernel, hoàn toàn tự do)}.$$
$$(x,r)\sim_c(y,s):\iff c(x,y)\le r+s.$$
$$E^{*_c}:=\{p\in\overline X:\ e\sim_c p\ \ \forall e\in E\}.$$

Đây là **định nghĩa duy nhất** cần công thức tường minh của $c$; mọi thứ sau đó là hệ quả của sáu tiên đề dưới, dùng như hộp đen.

### I.2. Bảng tiên đề — điều kiện tối giản, KHÔNG có dòng nào cần tính lồi

| Tiên đề | Nội dung | Điều kiện tối giản trên $c$ |
|---|---|---|
| Pa1 Antitone | $A\subseteq B\Rightarrow B^{*_c}\subseteq A^{*_c}$ | **Không cần gì** |
| Pa2 Extensive | $A\subseteq A^{**}$ | **$c$ đối xứng**: $c(x,y)=c(y,x)$ |
| Thm Involution | $A^{***}=A^*$ | hệ quả Pa1+Pa2 |
| Pa3 Upward-closed | thớ là tia hướng lên | **Không cần gì** (chỉ dùng đơn điệu $+$ trên $r$) |
| Pb1 Fiber-closed | Dedekind trong một thớ cố định | **Không cần gì** (thuần số thực, không đụng $X$) |
| Pb2 Topo-closed | $A^{**}$ đóng trong $\overline X$ | **$c(\cdot,y)$ nửa liên tục dưới, $\forall y$** (⟺ cả hai chiều nhờ đối xứng) |
| ~~Pb3 Convexity~~ | ~~$A^{**}$ lồi~~ | **BỎ HOÀN TOÀN khỏi kiến trúc lõi** — xem Phần V.1 để biết khi nào nó quay lại như hệ quả, không phải tiên đề |

$$
\boxed{
\text{ICS đầy đủ}\ (\mathbb X_c,\wedge,\oplus,{}^{*_c})\iff c\ \text{đối xứng} + c(\cdot,y)\ \text{lsc},\ \forall y.\quad\textbf{Chỉ hai điều kiện. Không có lồi.}
}
$$

### I.3. Vì sao Pb1 không thể thay Pb2 (đã kiểm bằng phản ví dụ, nay giải thích bằng Phần 0)

Pb1 kiểm soát **trong một thớ cố định** ($x,y$ đứng yên, chỉ $r$ chạy) — đây là hiện tượng thuần túy order/Dedekind, không đụng đến cấu trúc $X$. Pb2 kiểm soát **sự khớp nối giữa các thớ khi $x$ biến thiên** — đây chính là bước "chiếu" của Phần 0, và như đã chỉ ra, phép chiếu tập đóng có thể mất tính đóng bất kể order-completeness bên trong mỗi thớ tốt đến đâu. **Hai loại "đóng" này không quy về nhau được** — đây là ranh giới đúng của lý thuyết, không phải "đại số vs. giải tích" như từng nghĩ, mà là **"trong-thớ vs. giữa-các-thớ"**.

---

## Phần II — Từ Polar đến ICS (Regepi, Meet, Fiber Sum) — không đổi từ v3, chỉ dùng Pa1–Pa3+Pb1–Pb2

Toàn bộ Định lý biểu diễn, Key Lemma, và bảng tổng hợp M0–M3/S1–S3/SM1/SM2/P/PM đứng vững nguyên vẹn với **bất kỳ** $c$ đối xứng + lsc riêng biến — không một dòng nào trong 11 tiên đề ICS viện dẫn Pb3.

**Điều kiện tồn tại của hai unit** (không tự động, cần kiểm riêng theo $c$ cụ thể):
$$
e_\wedge=\overline X:\ \text{luôn sống, mọi } c.
\qquad
e_\oplus=X\times[0,+\infty]:\ \text{sống} \iff \sup_X c(\cdot,y)<\infty\ \text{đều theo }y\ \text{(hoặc điều kiện tương ứng, xem III).}
$$

---

## Phần III — Hai họ kernel mẫu và cấu trúc $c=h\circ T$

**Nhận thức chốt (thay cho toàn bộ so sánh rời rạc ở các bản trước):** mọi kernel "có ý nghĩa" trong note này có dạng
$$
c(x,y)=h\bigl(T(x,y)\bigr),
$$
với $T:X\times X\to Z$ là một **ánh xạ tương tác đối xứng cố định** (không có tự do chọn), và $h:Z\to\overline{\mathbb R}$ là **profile một-biến tự do**.

| Họ | $T$ | $Z$ | $h$ | Đối xứng của $T$ | "Giá" cấu trúc |
|---|---|---|---|---|---|
| **Shift** (residual, inf-convolution) | $T=+$ | $Z=X$ | tự do, chỉ cần lsc | Tự động (nhóm abel) | Miễn phí |
| **Bilinear** (Fenchel) | $T=\langle\cdot,\cdot\rangle$ | $Z=\mathbb R$ | cố định $=\mathrm{id}$ | Cần chọn inner product (Riesz self-dual) | Phải trả bằng cách trang bị thêm cấu trúc Hilbert |
| **$\varphi$-twisted Fenchel** (mới, Phần V.2) | $T=\langle\cdot,\cdot\rangle$ | $Z=\mathbb R$ | $\varphi$ đơn điệu lsc, tự do | như trên | Trung gian |
| **Quadratic/OT cost** (cầu nối) | $T=\|x-y\|^2$ | $Z=\mathbb R_{\ge0}$ | affine | Tự động ($\|x-y\|=\|y-x\|$) | Miễn phí, nhưng chứa cả hai họ trên qua khai triển $\|x-y\|^2=\|x\|^2+\|y\|^2-2\langle x,y\rangle$ |

---

## Phần IV — Residual của Infimal Convolution: instance kernel shift

$$
(f\multimap h)(z)=\sup_{y\in\operatorname{dom}f}\bigl(h(z+y)-f(y)\bigr)=f^{c_h}(z),\qquad c_h(y,z):=h(y+z).
$$

Tính lồi/đóng của $f\multimap h$ (định lý gốc của note đầu tiên): đóng $\Leftarrow$ Pb2 áp cho $c_h$ (cần $h$ lsc — đúng như đã dùng); lồi $\Leftarrow$ Pb3 — **không thuộc kiến trúc lõi**, chỉ là hệ quả phụ khi $h$ lồi, không phải điều kiện cần cho đại số.

Định lý residuation $f\square g\ge h\iff g\ge f\multimap h$ = adjunction Pa1+Pa2 áp cho $c_h$.

---

## Phần V — Thảo luận mở rộng

### V.1. Tính lồi quay lại khi nào, và quay lại như gì

Trong kiến trúc mới, Pb3 **không phải tiên đề** — nhưng nó **có thể xuất hiện trở lại như một hệ quả**, đúng một lần, ở đúng một chỗ:

> **Mệnh đề.** Nếu $T$ là **bilinear** (không chỉ đối xứng mà còn tuyến tính riêng theo từng biến) và $h$ là **affine**, thì mỗi lát cắt $\varphi_e(z):=c(x,y)-r-s$ (dùng trong chứng minh Pb2, xem I.2) tự động **affine** theo biến còn lại — cho ngay Pb3 "miễn phí", không cần thêm giả thiết.

Đây chính xác là trường hợp kernel Fenchel: $T=\langle\cdot,\cdot\rangle$ bilinear, $h=\mathrm{id}$ affine $\Rightarrow$ mọi $H_p$ là nửa-không-gian affine $\Rightarrow$ regepi lồi "tự động". Với kernel shift $c_h(x,y)=h(x+y)$: $T=+$ **là affine** (tịnh tiến), nhưng $h$ **tự do** — nên Pb3 chỉ quay lại **nếu ta CHỌN thêm** $h$ lồi (một ràng buộc thật sự trên profile, không tự động như bên Fenchel).

$$
\boxed{
\text{Lồi (Pb3) là hệ quả TỰ ĐỘNG chỉ khi CẢ } T \text{ lẫn } h \text{ đều tuyến tính/affine — đây là đặc trưng riêng của họ Fenchel, không phải quy luật chung của } c\text{-conjugate.}
}
$$

Nói cách khác: dot product không "được" tính lồi nhờ may mắn — nó **là** điểm duy nhất trong không gian $c=h\circ T$ nơi cả hai tầng ($T$ và $h$) đều affine cùng lúc, nên Pb3 sụp ra hoàn toàn miễn phí, đúng như cách $\langle x,y\rangle$ trông "đặc biệt" từ những lượt thảo luận đầu tiên.

### V.2. Residual của linear logic $\Rightarrow$ dạng $c$-transform, và liên hệ Kantorovich duality

Từ lượt trước: chọn dualizing element $\bot=h$ trong quantale $(\overline{\mathbb R}^X,\square,\multimap)$ cho $f^\bot=f\multimap h=f^{c_h}$ — **negation kiểu Girard chính là $c$-conjugate với kernel shift**. Tổng quát hóa: với **bất kỳ** kernel $c$ hợp lệ (đối xứng + lsc riêng biến), định nghĩa negation-tổng-quát $f^\bot_c:=f^c$ vẫn cho nucleus (Pa1+Pa2 luôn đúng).

**Remark (Kantorovich duality).** Trong lý thuyết vận chuyển tối ưu (optimal transport), với cost function $c:X\times Y\to\overline{\mathbb R}$ bất kỳ, **$c$-transform** được định nghĩa **đúng cùng công thức**:
$$
\varphi^c(y):=\sup_x\bigl(c(x,y)-\varphi(x)\bigr)
$$
và bài toán Kantorovich đối ngẫu tìm cặp $(\varphi,\psi)$ với $\varphi\oplus\psi\le c$ tối đa hoá $\int\varphi\,d\mu+\int\psi\,d\nu$, đạt tối ưu tại $\psi=\varphi^c,\ \varphi=\psi^c$ — **đúng cấu trúc bipolar/nucleus** đã dựng ở Phần I–II, chỉ thay $\preceq$ (thứ tự hàm) bằng ràng buộc tích phân. Trường hợp $c(x,y)=-\langle x,y\rangle$ (cost tuyến tính) khôi phục **chính xác** đối ngẫu Fenchel–Legendre cổ điển; trường hợp $c(x,y)=\|x-y\|^2/2$ (cost bậc hai) cho định lý Brenier, và chính là "kernel cầu nối" ở Phần III. Vậy: **residual/negation của linear logic, $c$-conjugate của giải tích lồi tổng quát, và $c$-transform của optimal transport là cùng một cơ chế nucleus, khác nhau ở việc thứ tự nền là $\preceq$ trên hàm hay ràng buộc trên độ đo.**

### V.3. Giả thuyết "$f(x,y)$ mới là đối tượng đúng" — ví dụ, và ghi chú về tính bác bỏ

**Ví dụ cụ thể (partial inf minh hoạ, không phải chứng minh):** $f_1(x):=\inf_y \bigl(|x-y|+\mathbb 1_{[0,1]}(y)\bigr)$ (khoảng cách từ $x$ tới $[0,1]$) là marginal của $H_1(x,y)=|x-y|+\mathbb 1_{[0,1]}(y)$ — jointly convex, cho $f_1$ lồi tự động qua đúng định lý ở Phần 0. So sánh: $f_2(x):=x^2$ **cũng** có thể viết thành marginal, ví dụ $H_2(x,y):=x^2+0\cdot y$ (thêm biến $y$ giả, không tương tác) — nhưng đây là **lifting tầm thường**, không mang thông tin gì mới.

**Ghi chú về tính bác bỏ (falsifiability) — cần trung thực:** giả thuyết "$f(x,y)$ là đối tượng đúng, $f(x)$ chỉ là chiếu" **không dễ bác bỏ theo nghĩa Popper**, vì lý do cấu trúc: với **mọi** $f:X\to\overline{\mathbb R}$, luôn có thể viết $f(x)=\inf_y H(x,y)$ một cách tầm thường bằng $H(x,y):=f(x)$ (không phụ thuộc $y$) hoặc $H(x,y):=f(y)+\delta_{\{0\}}(x-y)$ (lifting qua đường chéo). Vậy **lifting luôn tồn tại, không bao giờ có phản ví dụ** — điều này khiến giả thuyết, phát biểu trần trụi, **không phải một tuyên bố thực nghiệm có nội dung**, mà là một **lựa chọn mô hình hoá** (modeling choice). Nội dung thực sự nằm ở việc **lifting nào là "chính tắc"/tối giản** (ví dụ: $H$ jointly convex khi $f=f_1\square f_2$, nhưng không phải mọi $f$ lồi đều cần một $H$ *jointly convex không tầm thường* để giải thích nó — hàm affine $f(x)=ax+b$ đã lồi sẵn, không "cần" cấu trúc hai biến gì để giải thích tính lồi của nó). Vậy phát biểu đúng đắn hơn, có nội dung và bác bỏ được, là:

$$
\boxed{
\text{"Tính lồi (hay: tính đóng-dưới-polar) của MỘT SỐ hàm/tập cụ thể } f=g\square k\ \text{có NGUỒN GỐC là partial-minimization của bifunction jointly convex } H=g\oplus k\text{"}
}
$$

— đây **là** một tuyên bố có nội dung thật (đã chứng minh ở Phần 0), khác với tuyên bố tổng quát "mọi hàm một biến thực chất là hàm hai biến" (không có nội dung, vì luôn đúng bằng lifting tầm thường).

### V.4. Câu hỏi mở: cấu trúc chung phía sau hai kernel là gì

Câu trả lời hiện có (Phần III): **$c=h\circ T$**, với $T$ đối xứng cố định (đóng vai trò "hình học nền": nhóm cộng $X$, hoặc dạng song tuyến tính trên $X\times X^*$ tự-đối-ngẫu) và $h$ profile tự do. Nhưng câu hỏi thật sự sâu hơn vẫn mở:

1. **Có đúng chỉ hai lớp $T$ "cơ bản" (cộng nhóm và dạng song tuyến tính), hay còn lớp thứ ba độc lập** (không suy được từ hai lớp trên qua composition/limit)? Kernel $\|x-y\|^2$ ở Phần III cho thấy ít nhất một cách **pha trộn** hai lớp, nhưng chưa rõ có lớp $T$ nào **không thể phân rã** thành tổ hợp shift+bilinear.
2. Trong ngôn ngữ nhóm Lie / hình học vi phân: $T=+$ tương ứng phép tác động của chính $X$ lên bản thân nó (translation, nhóm abel); $T=\langle,\rangle$ tương ứng cấu trúc symplectic/metric. Câu hỏi mở: **mọi $T$ đối xứng hợp lệ (cho Pa2) có nhất thiết sinh từ một tác động nhóm (Lie group action) lên $X$ hay không**, và nếu có, phân loại các tác động đó có tương ứng 1-1 với phân loại các "họ đối ngẫu" (Fenchel, residual, Kantorovich-với-cost-đối-xứng, …)?
3. Vai trò của $Z$ (không gian đích của $T$): $Z=X$ (shift) vs $Z=\mathbb R$ (bilinear) — liệu $Z=$ một nhóm/vành trung gian khác (vd. $Z=X\times\mathbb R$, hoặc $Z$ là một đại số Lie) có sinh ra họ kernel thứ tư với tính chất mới, chưa xuất hiện ở đâu trong note này?

*(Không có câu trả lời chốt ở đây — đây là biên giới thật sự của lý thuyết tại thời điểm này.)*

---

## Phụ lục — Bảng tổng kết kiến trúc v4

| | v2 (chỉ Fenchel) | v3 (kernel tổng quát) | **v4 (kiến trúc chốt)** |
|---|---|---|---|
| Đối tượng nền | $\langle x,y\rangle$ | $c$ tổng quát | $c=h\circ T$, $T$ đối xứng cố định + $h$ tự do |
| Vai trò của lồi | Giả thiết chính (Pb3) | Ghi nhận là "không cần" | **Loại khỏi kiến trúc lõi**, chỉ quay lại như hệ quả khi $T,h$ đều affine (V.1) |
| Vai trò của đóng topo | Ngầm định (liên tục toàn phần) | Điều kiện tối giản: lsc riêng biến | **Trụ cột duy nhất còn lại** ngoài đối xứng — giải thích bằng "phép chiếu" (Phần 0) |
| Vị trí residual | Không liên hệ | Instance kernel shift | Instance $c=h\circ T$ với $T=+$, đồng thời là negation-Girard, đồng thời là $c$-transform Kantorovich khi $\mu,\nu$ tham gia (V.2) |
| Đối tượng nguyên thủy | Hàm một biến | Hàm một biến | **Bifunction hai biến**, hàm một biến là marginal (Phần 0, V.3) |
