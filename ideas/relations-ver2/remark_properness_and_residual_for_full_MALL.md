# Hai nhóm vấn đề còn mở: Properness và Residual

## Bối cảnh

Sau khi xác nhận bốn luật phân phối MALL (T7–T10) đúng-sai chính xác theo dự đoán và gán tensor$\leftrightarrow\bigtriangledown$, par$\leftrightarrow\triangle$ được ép buộc bởi đại số, hai mảng câu hỏi còn lại trước khi $(\mathbb X,\subseteq,\wedge,\vee,\triangle,\bigtriangledown,{}^*)$ có thể tuyên bố là một model của MALL: **(1) properness** — liệu $\mathbb X$ như hiện định nghĩa (qua $U,\mathcal F,C,T$) có phải đối tượng đúng, hay cần thu hẹp/mở rộng; **(2) residual** — liệu phép kéo theo tuyến tính $\multimap$ có thỏa tính chất phổ dụng của một adjoint, điều kiện định nghĩa "closed monoidal" mà bốn luật phân phối không tự động cho.

---

## Nhóm 1 — Properness: $\mathbb X$ có phải đối tượng đúng?

### Nguồn gốc vấn đề

Chính tài liệu gốc đã để ngỏ điều này ở Claim 3: *"An additional intrinsic condition will likely be needed to characterize proper functions, and is left open."* Toàn bộ chuỗi chứng minh vừa qua đã chạm đúng chỗ đó — không phải một chi tiết kỹ thuật phụ, mà là câu hỏi Claim 3 đã cảnh báo trước.

**Định nghĩa (proper).** $E\in\mathbb X$ là **proper** nếu hàm đại diện $e:X\to\overline{\mathbb R}$ không nhận giá trị $-\infty$ ở bất kỳ đâu. Viết $\mathbb X_{\mathrm{proper}}\subsetneq\mathbb X$.

Phần tử **improper** cực đoan nhất là chính đơn vị $1_\wedge=X\times\overline{\mathbb R}$ ($e\equiv-\infty$) — nó *bắt buộc phải tồn tại* để $\wedge,\vee$ là lattice có đơn vị (T1–T5 cần $1_\wedge$), nhưng nó lại chính xác là loại phần tử làm Prop 10 (đóng $\mathcal F,C,T$ dưới $+_{\mathrm{fib}}$) có nguy cơ gãy.

### Mệnh đề 1.1 — Mở rộng của Prop 10 ra toàn $\mathbb X$

**Cần kiểm tra:** Với **mọi** $A,B\in\mathbb X$ (không giả thiết proper), có đúng $A+_{\mathrm{fib}}B\in\mathbb X$ hay không?

Hai khả năng, cả hai đều đáng giá trị:
- Nếu **đúng**: cần một chứng minh khác Prop 10 (không dựa vào $\liminf$-superadditivity cần proper), có thể qua đặc trưng khác của $\mathbb X$ hoặc case-split tường minh trên tập $\{x:e(x)=-\infty\}$.
- Nếu **sai**: cần một phản ví dụ cụ thể — hai regepi improper $A,B$ sao cho $A+_{\mathrm{fib}}B$ không đóng theo $\mathcal F$ hoặc $C$ hoặc $T$.

### Mệnh đề 1.2 — Tính hấp thụ của $1_\wedge$ dưới Fibor

**Cần kiểm tra:** $1_\wedge\triangle F = 1_\wedge$ với mọi $F\in\mathbb X$?

*Động lực.* Nếu đúng, trường hợp cực đoan nhất ($1_\wedge$ tham gia) tách ra thành một quy tắc hấp thụ đơn giản, không cần Prop 10 tổng quát — thu hẹp câu hỏi 1.1 xuống còn đúng các trường hợp "improper cục bộ" (hàm nhận $-\infty$ trên một phần miền xác định, hữu hạn ở phần còn lại), vốn là lớp bệnh lý hẹp hơn nhiều theo lý thuyết hàm lồi cổ điển (một hàm lồi nhận $-\infty$ ở đâu đó mà không đồng nhất $-\infty$ buộc phải nhận $-\infty$ trên toàn bộ phần trong tương đối của miền xác định — một ràng buộc mạnh, gần như loại trừ các trường hợp "vá lỗi" tùy tiện).

### Mệnh đề 1.3 — Polar có bảo toàn tính proper?

**Cần kiểm tra:** $E\in\mathbb X_{\mathrm{proper}}\implies E^*\in\mathbb X_{\mathrm{proper}}$?

*Vì sao mệnh đề này quan trọng độc lập với 1.1.* Ngay cả khi 1.1 được thu hẹp thành công về $\mathbb X_{\mathrm{proper}}$, các chứng minh dùng đối ngẫu polar (T8=D2, T13=M3, và toàn bộ P.U) đều thao tác trên $E^*,F^*,G^*$ chứ không phải $E,F,G$ trực tiếp. Nếu polar **không** bảo toàn properness, thu hẹp $\mathbb X\to\mathbb X_{\mathrm{proper}}$ sẽ không đóng dưới các phép đối ngẫu này, và toàn bộ chiến lược "chứng minh một bên rồi suy ra bên kia qua P.U" (đã dùng liên tục từ T8 trở đi) sẽ mất hiệu lực trên $\mathbb X_{\mathrm{proper}}$.

**Ba tình huống có thể xảy ra**, cần xác định tình huống nào đúng:
- (a) Polar bảo toàn properness hoàn toàn $\Rightarrow \mathbb X_{\mathrm{proper}}$ đóng dưới $(\cdot)^*$, chiến lược cũ cứu được nguyên vẹn.
- (b) Polar biến mọi $E$ improper thành $E^*$ có dạng đặc biệt (ví dụ hằng $+\infty$ hoặc hằng $-\infty$) — đây là hiện tượng được biết đến trong giải tích lồi cổ điển cho hàm lồi improper, cần dịch lại chính xác sang ngôn ngữ preepi và kiểm chứng trong khuôn khổ Rockafellar convention đang dùng, không suy diễn từ trí nhớ.
- (c) Không có quy luật đơn giản — cần một điều kiện thứ năm (đúng như Claim 3 dự đoán) để đặc trưng đúng lớp "tốt", có thể không trùng với $\mathbb X_{\mathrm{proper}}$ như định nghĩa sơ bộ ở trên.

### Kết luận nhóm 1

**Nếu (1.1) sai và (1.2) đúng nhưng không đủ dọn sạch mọi trường hợp improper, và (1.3) rơi vào tình huống (c)** — thì $\mathbb X=\mathrm{Fix}(U,\mathcal F,C,T)$, đúng như Claim 3 đã tự cảnh báo, **không phải đối tượng đúng nhất** cho chương trình. Đối tượng đúng có thể là một tập con $\mathbb X^\sharp\subsetneq\mathbb X$ cắt ra bởi một điều kiện thứ năm chưa được đặt tên — và việc tìm điều kiện đó (khả năng cao liên quan đến tính "properness" theo nghĩa cổ điển, nhưng có thể tinh vi hơn định nghĩa sơ bộ ở trên) trở thành mục tiêu trung tâm mới của Milestone I, thay vì một chi tiết kỹ thuật phụ.

---

## Nhóm 2 — Residual: $\multimap$ có phải adjoint thật sự?

### Định nghĩa cần kiểm

Theo mẫu Claim 10 gốc, dịch sang ký hiệu mới:
$$E\multimap F := (E\bigtriangledown F^*)^*, \qquad E,F\in\mathbb X.$$

### Mệnh đề 2.1 — Tính chất phổ dụng (universal property / adjunction)

**Cần kiểm tra:** với mọi $E,F,G\in\mathbb X$:
$$G\bigtriangledown E\subseteq F \iff G\subseteq E\multimap F.$$

Đây **chính là điều kiện định nghĩa** để $(\mathbb X,\bigtriangledown)$ là *closed monoidal* — không phải hệ quả tự động của bốn luật phân phối T7–T10 đã chứng minh. Cần kiểm hai chiều riêng biệt:

- **($\Leftarrow$, dễ hơn, "counit"):** $G\subseteq E\multimap F\implies G\bigtriangledown E\subseteq F$. Dự đoán chứng minh được từ đơn điệu (T0) áp cho $\bigtriangledown E$ hai vế, cộng một bước "evaluation" $\ (E\multimap F)\bigtriangledown E\subseteq F$ cần kiểm riêng trước (xem Mệnh đề 2.2).
- **($\Rightarrow$, khó hơn):** $G\bigtriangledown E\subseteq F\implies G\subseteq E\multimap F$. Đây là chiều thường cần đến tính đầy đủ của thứ tự (complete lattice, xem Mệnh đề 2.3) hoặc một lập luận polar trực tiếp — chưa có chứng minh.

### Mệnh đề 2.2 — Evaluation map (counit)

**Cần kiểm tra:** $(E\multimap F)\bigtriangledown E\subseteq F$, với mọi $E,F\in\mathbb X$.

*Đây là điều kiện yếu hơn 2.1*, đáng kiểm trước như một "sanity check" — nếu ngay cả evaluation map cũng thất bại, toàn bộ định nghĩa $\multimap$ theo công thức Claim 10 có vấn đề nghiêm trọng hơn chỉ là thiếu adjunction đầy đủ.

### Mệnh đề 2.3 — Residual trừu tượng khớp với công thức tường minh

**Cần kiểm tra:** nếu $(\mathbb X,\subseteq)$ là complete lattice (đóng dưới giao/hợp **tùy ý**, không chỉ nhị nguyên — bản thân điều này cũng chưa kiểm, xem Nhận xét bên dưới) và $\bigtriangledown$ phân phối qua hợp tùy ý (mở rộng T8/D2 từ nhị nguyên lên tùy ý), thì residual trừu tượng
$$\bigvee\{G\in\mathbb X: G\bigtriangledown E\subseteq F\}$$
luôn tồn tại. **Cần kiểm tra riêng:** công thức tường minh $(E\bigtriangledown F^*)^*$ có bằng đúng residual trừu tượng này hay không — đây chính xác là câu hỏi Milestone II gốc đã nêu (*"Whether E ⊸ F = (E +M F)^{**} on 𝕏"*, nay viết lại đúng ngữ cảnh Fibor/Spator).

### Mệnh đề 2.4 — Residual kế thừa điều kiện properness

**Quan sát cần xác nhận bằng chứng minh, không phải giả định:** vì định nghĩa $\multimap$ dùng $\bigtriangledown$ và $(\cdot)^*$, và cả hai đều mang theo (trực tiếp hoặc gián tiếp qua T13) điều kiện properness từ Nhóm 1, nhiều khả năng Mệnh đề 2.1–2.3 **cũng chỉ chứng minh được trên $\mathbb X_{\mathrm{proper}}$** (hoặc trên $\mathbb X^\sharp$ đúng đối tượng cuối cùng nếu Nhóm 1 kết luận (c)) — chứ không phải trên toàn $\mathbb X$. Đây là lý do hai nhóm vấn đề **không độc lập**: kết quả của Nhóm 1 quyết định miền áp dụng của Nhóm 2.

---

## Quan hệ giữa hai nhóm và thứ tự khuyến nghị

```
Nhóm 1 (Properness)                    Nhóm 2 (Residual)
─────────────────────                  ──────────────────
1.1 Prop 10 trên toàn 𝕏?  ──────┐
1.2 1_∧ hấp thụ dưới △?          │
1.3 Polar bảo toàn proper?  ─────┼───►  xác định miền 𝕏_proper
                                 │      hay 𝕏^♯ đúng cho...
                                 │
                                 └───►  2.1 Adjunction G▽E⊆F ⟺ G⊆E⊸F
                                        2.2 Evaluation map (counit)
                                        2.3 Residual trừu tượng = công thức
                                        2.4 (kế thừa miền từ Nhóm 1)
```

**Khuyến nghị:** giải Nhóm 1 trước (1.1, 1.2, 1.3, theo thứ tự đó — 1.2 dễ nhất, có thể giải nhanh và thu hẹp phạm vi 1.1 ngay lập tức), vì kết quả của nó xác định chính xác miền $\mathbb X_{\mathrm{proper}}$ hay $\mathbb X^\sharp$ mà Nhóm 2 sẽ phải làm việc trên đó — tránh việc chứng minh 2.1–2.3 trên một miền rồi phải làm lại khi Nhóm 1 thay đổi kết luận.
