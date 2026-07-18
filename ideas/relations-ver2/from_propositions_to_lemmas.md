# Propositions trên Primitives: nền tảng cho các API Lemma

## Quy ước phạm vi

Các Proposition trong Section 2 chỉ được phép dùng: $\subseteq,\ (\cdot)^*,\ (\cdot)^{**}$, bốn closure nguyên thủy $U,\mathcal F,C,T$, và bốn toán tử nguyên thủy $\cap,\cup,+_{\rm fib},+_{\rm sp}$ — cộng thêm các sự kiện thuần túy **Level 0** (số học trên $\overline{\mathbb R}$ dưới quy ước Rockafellar, và tính song tuyến của cặp ghép $\langle\cdot,\cdot\rangle$ trên $X$), vốn là input có trước mọi cấu trúc preepi, không phải hệ quả của nó.

**Cảnh báo được flag rõ ở cuối:** một trong các API Lemma — (L.I) — **không** thu gọn hoàn toàn về các primitive này; phần liên quan tới $\mathcal F,C,T$ (khác với $U$) của nó thực chất cần nhập nội dung giải tích lồi (đặc trưng regepi ↔ hàm lồi lsc), một sự kiện mà chính tài liệu gốc đã ghi nhận là "left open" (Claim 3, phần motivation), không phải hệ quả thuần túy của bốn closure nguyên thủy. Điều này được nêu tường minh thay vì che giấu.

---

## Section 1 — Bảng: API Lemma và các Proposition trên primitives

| API Lemma | Proposition(s) trên primitives cần dùng |
|---|---|
| **(L.A)** Tam polar bất động | **P1** (mở rộng của polar) $+$ **P2** (phản biến của polar) |
| **(L.B)** Polar của hợp | tự thân — trực tiếp từ định nghĩa $(\cdot)^*$ và $\cup$, không cần proposition trung gian nào |
| **(L.C)** Join = đối ngẫu bipolar của meet | (L.A) $+$ (L.B) — không có proposition mới ngoài hai lemma trên |
| **(L.D)** Đóng dưới giao của điểm bất động | **P1** $+$ **P4** (đơn điệu của $(\cdot)^{**}$, hệ quả của P2 áp hai lần) |
| **(L.E)** Đơn ánh của polar trên $\mathbb X$ | tự thân — trực tiếp từ định nghĩa $\mathbb X:=\mathrm{Fix}((\cdot)^{**})$, thay thế đại số |
| **(L.F)** Polar của spatial sum | **P7** (song tuyến của $\langle\cdot,\cdot\rangle$, Level 0) $+$ **P8** (sup cộng tính trên biến độc lập, số học $\overline{\mathbb R}$) |
| **(L.G)** Giao hoán của $\triangle,\bigtriangledown$ | **P9** (giao hoán của $+$ trên $X$ và trên $\overline{\mathbb R}$, Level 0) |
| **(L.H)** Kết hợp của phép cộng mở rộng | **P10** (số học Rockafellar, thuần Level 0 — **không** dùng bất kỳ toán tử preepi nào) |
| **(L.MP)** Bổ đề max-plus | **P11** (số học Rockafellar cho $\max$, thuần Level 0) |
| **(L.I)** Fiber sum của hai regepi tự động là regepi | **P12** (đóng dưới $U$, thuần primitive) — chỉ giải quyết được thành phần $U$; thành phần $\mathcal F,C,T$ cần **P13**, **flagged là KHÔNG thuần primitive** |
| **(L.UD)** Đơn vị đối ngẫu | tự thân — tính toán trực tiếp từ định nghĩa $(\cdot)^*$ lên $1_\wedge,1_\triangle$ |
| **(P.U)** Mệnh đề hợp nhất | (L.A) $+$ (L.F) — không có proposition mới |

---

## Tổng kết trạng thái

| API Lemma | Trạng thái sau khi hạ xuống primitives |
|---|---|
| L.A, L.B, L.C, L.D, L.E, L.UD | ✅ Hoàn toàn thuần primitive (chỉ P1, P2, P4, hoặc trực tiếp định nghĩa) |
| L.F, L.G | ✅ Thuần primitive $+$ Level 0 (P7, P8, P9) — không có gì bất ngờ, Level 0 luôn được phép dùng như input |
| L.H, L.MP | ✅ Thuần Level 0 (P10, P11) — không liên quan cấu trúc preepi, là tiên đề số học nền |
| **L.I** | ⚠️ **Chỉ một nửa** (thành phần $U$, qua P12) là thuần primitive. Thành phần $\mathcal F,C,T$ (qua P13) hiện phải mượn nội dung Milestone II (đặc trưng hàm lồi lsc), chưa được chứng minh lại từ $U,\mathcal F,C,T$ một cách nội tại — đây là câu hỏi mở thật sự, không phải chi tiết kỹ thuật có thể bỏ qua, vì nó là nền của toàn bộ M1/M3 (khối monoid).
