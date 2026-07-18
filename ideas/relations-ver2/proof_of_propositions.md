
## Section 2 — Phát biểu chính xác các Proposition

### P1 — Mở rộng của polar (extensivity)

Với mọi preepi $E$: $\ E\subseteq E^{**}$.

*Chứng minh.* Lấy $(x,r)\in E$. Cần chỉ ra $(x,r)\in E^{**}$, tức với mọi $(y,s)\in E^*$: $\langle x,y\rangle\le r+s$. Theo định nghĩa $E^*$, mọi $(y,s)\in E^*$ thỏa $\langle x',y\rangle\le r'+s$ với **mọi** $(x',r')\in E$ — áp riêng cho $(x',r')=(x,r)\in E$, được đúng bất đẳng thức cần. $\square$

### P2 — Phản biến của polar (antitonicity)

Với mọi preepi $A,B$: $\ A\subseteq B\implies B^*\subseteq A^*$.

*Chứng minh.* Nếu $(y,s)\in B^*$: bất đẳng thức định nghĩa đúng với mọi $(x,r)\in B$, do đó đúng với mọi $(x,r)\in A\subseteq B$ — tức $(y,s)\in A^*$. $\square$

### P4 — Đơn điệu của bipolar (hệ quả trực tiếp của P2)

Với mọi preepi $A,B$: $\ A\subseteq B\implies A^{**}\subseteq B^{**}$.

*Chứng minh.* Áp P2 hai lần: $A\subseteq B\overset{\text{P2}}{\implies}B^*\subseteq A^*\overset{\text{P2}}{\implies}A^{**}\subseteq B^{**}$. $\square$

### P7 — Song tuyến của cặp ghép (Level 0)

Với mọi $x_1,x_2,y\in X$: $\ \langle x_1+x_2,y\rangle = \langle x_1,y\rangle+\langle x_2,y\rangle$.

*(Tiên đề của tích trong Euclid trên $X=\mathbb R^n$, không phải hệ quả của cấu trúc preepi — là input có trước mọi định nghĩa polar.)*

### P8 — Sup cộng tính trên biến độc lập (số học $\overline{\mathbb R}$)

Với mọi hàm $f,g$ nhận giá trị trong $\overline{\mathbb R}$, trên các miền độc lập:
$$\sup_{a,b}\bigl(f(a)+g(b)\bigr) = \sup_a f(a) + \sup_b g(b).$$

*(Sự kiện chuẩn của $\sup$ trên tích hai tập, không cần cấu trúc preepi — dùng quy ước Rockafellar khi các sup bằng $\pm\infty$ để vế phải luôn xác định.)*

### P9 — Giao hoán của phép cộng (Level 0)

Với mọi $x_1,x_2\in X$: $x_1+x_2=x_2+x_1$. Với mọi $r,s\in\overline{\mathbb R}$: $r+s=s+r$ (kể cả dưới quy ước Rockafellar, vì $(+\infty)+(-\infty)=(-\infty)+(+\infty):=+\infty$ đối xứng theo định nghĩa).

### P10 — Số học Rockafellar: kết hợp tính (Level 0, thuần)

Với mọi $r,s,t\in\overline{\mathbb R}$, dưới quy ước $(+\infty)+(-\infty):=+\infty$:
$$(r+s)+t=r+(s+t).$$

*Chứng minh (kiểm từng trường hợp, không liên quan preepi).* Viết công thức tường minh ba-biến: tổng bằng $+\infty$ nếu có ít nhất một số hạng $+\infty$; bằng $-\infty$ nếu không có $+\infty$ nhưng có $-\infty$; bằng tổng thường nếu cả ba hữu hạn. Công thức này không phụ thuộc cách nhóm ngoặc, khớp với định nghĩa từng cặp. $\square$

*Đây là input Level 0, không phải hệ quả của $\subseteq,{}^*,{}^{**},U,\mathcal F,C,T,\cap,\cup,+_{\rm fib},+_{\rm sp}$ — nó đến trước, là quy ước số học mà các toán tử preepi dựa vào.*

### P11 — Số học Rockafellar: phân phối max–plus (Level 0, thuần)

Với mọi $t,a,b\in\overline{\mathbb R}$: $\ t+\max(a,b)=\max(t+a,t+b)$.

*Chứng minh.* $t$ hữu hạn: luật cộng thường bảo toàn thứ tự. $t=+\infty$: cả ba đại lượng $=+\infty$ theo quy ước. $t=-\infty$: nếu $\max(a,b)=+\infty$ cả hai vế $=+\infty$; ngược lại cả hai vế $=-\infty$. $\square$ *(Cùng tầng Level 0 với P10.)*

### P12 — Đóng dưới $U$ tương thích với fiber sum (thuần primitive, KHÔNG cần lồi)

Nếu $U(A)=A$ và $U(B)=B$ thì $U(A+_{\rm fib}B)=A+_{\rm fib}B$.

*Chứng minh.* Chiều $\supseteq$ tự động (định nghĩa $U$ luôn mở rộng: $U(E)\supseteq E$). Chiều $\subseteq$: lấy $(x,r')\in U(A+_{\rm fib}B)$, tức tồn tại $r\le r'$ với $(x,r)\in A+_{\rm fib}B$, viết $r=a+b$, $(x,a)\in A,(x,b)\in B$. Đặt $a':=a+(r'-r)$ (dùng P10 để cộng hợp lệ, xử lý riêng các trường hợp $\pm\infty$ theo quy ước Rockafellar), $b':=b$. Vì $r'\ge r$, $a'\ge a$; vì $U(A)=A$, từ $(x,a)\in A$ và $a'\ge a$ suy ra $(x,a')\in A$ (đúng định nghĩa $U$). Vì $a'+b'=r'$ (kiểm bằng P10), $(x,r')\in A+_{\rm fib}B$. $\square$

*Đây là kết quả **thuần túy primitive** — không dùng đến biểu diễn hàm lồi/lsc nào, chỉ dùng định nghĩa $U$ và số học Level 0 (P10).*

### P13 — Đóng dưới $\mathcal F,C,T$ tương thích với fiber sum (⚠️ KHÔNG thuần primitive)

**Phát biểu mong muốn (chưa chứng minh thuần túy từ primitive):** nếu $\mathcal F(A)=A,C(A)=A,T(A)=A$ và tương tự cho $B$, thì $\mathcal F(A+_{\rm fib}B)=C(A+_{\rm fib}B)=T(A+_{\rm fib}B)=A+_{\rm fib}B$.

**Vì sao đây không phải một Proposition thuần primitive.** Không giống P12 (chỉ cần định nghĩa $U$ trực tiếp), việc kiểm $C$ (lồi) và $\mathcal F,T$ (đóng) được bảo toàn qua $+_{\rm fib}$ đòi hỏi **biểu diễn cụ thể** của $A,B$ như epigraph của hàm lồi lsc $a,b:X\to\overline{\mathbb R}$ — tức đã dùng tương ứng $\mathbb X\leftrightarrow\Gamma_0(X)$ mà chính tài liệu gốc (Claim 3, phần motivation) ghi nhận: *"An additional intrinsic condition will likely be needed to characterize proper functions, and is left open."* Nói cách khác, đặc trưng $\mathbb X$ như $\mathrm{Fix}(U,\mathcal F,C,T)$ thuần túy tổ hợp/tô-pô **không tự động** cho ta công cụ hàm số (cộng hàm, lồi, $\liminf$) — đó là một tầng dữ liệu bổ sung (Milestone II), chưa được thiết lập lại từ $U,\mathcal F,C,T$ một cách nội tại trong tài liệu.

**Hệ quả cho (L.I).** Thành phần $U$ của (L.I) đã có chứng minh thuần primitive vững chắc (qua P12). Thành phần $\mathcal F,C,T$ — cần cho toàn bộ **M1** (kết hợp tính của Fibor) và do đó **M3** (kết hợp tính của Spator, đi qua M1) — hiện đang dựa vào lập luận hàm số (lồi $+$ lsc, dùng bất đẳng thức $\liminf$) đã trình bày ở các file trước, **không phải** hệ quả của $U,\mathcal F,C,T$ theo nghĩa nguyên thủy thuần túy. Đây là một lỗ hổng thật cần ghi nhận: **M1, M3 (và do đó toàn bộ khối monoid) hiện đứng trên nền Milestone II (đặc trưng hàm số của regepi), chưa được hạ xuống nền Milestone I (thuần primitive) như bảng Section 1 kỳ vọng.**

*(Ghi chú thêm: khi thử chứng minh trực tiếp $\liminf$-superadditivity tổng quát trên $\overline{\mathbb R}$ — tức cố gắng biến P13 thành một sự kiện Level-0 thuần túy giống P10/P11 — ta gặp phản ví dụ: với $r_n\to+\infty,\ s_n\to-\infty$ tùy ý, $\liminf(r_n+s_n)$ có thể nhỏ hơn hẳn quy ước $(+\infty)+(-\infty):=+\infty$. Sự kiện này KHÔNG mâu thuẫn với chứng minh cũ của "Bổ đề I" trong các file trước, vì ở đó $a(x_n)\to a(x)$ với $a$ đã giả thiết lsc và — quan trọng — **thường ngầm giả thiết $a$ proper** (không nhận giá trị $-\infty$); nếu cho phép $a$ hoặc $b$ nhận $-\infty$ (tức preepi improper, như $1_\wedge$), lập luận $\liminf$ cũ cần thêm điều kiện, chưa được kiểm đầy đủ. Đây là điểm cần làm rõ thêm trong Milestone I/II, không chỉ là vấn đề ký hiệu.)*

---

