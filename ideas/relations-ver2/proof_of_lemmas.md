# API Lemmas: Phát biểu và Chứng minh đầy đủ

Tất cả chứng minh dưới đây chỉ dùng: $\subseteq,\ (\cdot)^*,\ (\cdot)^{**}$, bốn closure nguyên thủy $U,\mathcal F,C,T$, bốn toán tử nguyên thủy $\cap,\cup,+_{\rm fib},+_{\rm sp}$, và các Proposition Level 0/primitive **P1–P13** đã thiết lập trước (xem file `propositions_tren_primitives.md`). Khi một chứng minh cần vượt ra ngoài phạm vi này, điều đó được flag tường minh ngay tại chỗ.

**Nền hình học:** $X:=\mathbb R^n$, $\overline{\mathbb R}:=[-\infty,+\infty]$, $X_e:=X\times\overline{\mathbb R}$, quy ước Rockafellar $(+\infty)+(-\infty):=+\infty$. $\mathbb X:=$ lớp regepi $=\mathrm{Fix}(U,\mathcal F,C,T)$. Với $E\in\mathbb X$, viết $E_x=[e(x),+\infty]$, $e:X\to\overline{\mathbb R}$.

---

## (L.A) — Tam polar bất động

**Phát biểu.** Với mọi preepi $E$: $\ E^{***}=E^*$.

**Chứng minh.** Áp P1 (mở rộng) cho $E$: $E\subseteq E^{**}$. Áp P2 (phản biến) lên bao hàm này: $(E^{**})^*\subseteq E^*$, tức $E^{***}\subseteq E^*$. Mặt khác, áp P1 trực tiếp cho $E^*$ (thay $E$ bởi $E^*$ trong P1): $E^*\subseteq(E^*)^{**}=E^{***}$. Kết hợp hai bao hàm: $E^{***}=E^*$. $\blacksquare$

**Hệ quả.** $E^*\in\mathbb X'$ (điểm bất động của $(\cdot)^{**}$) với mọi preepi $E$, không cần $E\in\mathbb X$.

---

## (L.B) — Polar của hợp

**Phát biểu.** Với mọi preepi $E,F$: $\ (E\cup F)^*=E^*\cap F^*$.

**Chứng minh.** $(y,s)\in(E\cup F)^*\iff\langle x,y\rangle\le r+s\ \forall(x,r)\in E\cup F\iff\bigl[\langle x,y\rangle\le r+s\ \forall(x,r)\in E\bigr]\ \text{và}\ \bigl[\langle x,y\rangle\le r+s\ \forall(x,r)\in F\bigr]\iff(y,s)\in E^*\ \text{và}\ (y,s)\in F^*\iff(y,s)\in E^*\cap F^*$. $\blacksquare$

*(Trực tiếp từ định nghĩa, không cần P1–P13.)*

---

## (L.C) — Join là đối ngẫu bipolar của meet

**Phát biểu.** Với mọi preepi $E,F$: $\ E\vee F=(E^*\wedge F^*)^*$.

**Chứng minh.** $E\vee F:=(E\cup F)^{**}=\bigl((E\cup F)^*\bigr)^*\overset{\text{(L.B)}}{=}(E^*\cap F^*)^*=(E^*\wedge F^*)^*$. $\blacksquare$

---

## (L.D) — Đóng dưới giao của điểm bất động

**Phát biểu.** Nếu $A^{**}=A$ và $B^{**}=B$ thì $(A\cap B)^{**}=A\cap B$.

**Chứng minh.** Trước hết dẫn **P4** (đơn điệu của $(\cdot)^{**}$) từ P2 áp hai lần: nếu $S\subseteq S'$ thì $(S')^*\subseteq S^*$ (P2), rồi áp P2 lần nữa lên bao hàm đó: $(S^*)^*\subseteq(S'^*)^*$, tức $S^{**}\subseteq S'^{**}$.

Chiều $\supseteq$: áp P1 cho $A\cap B$: $A\cap B\subseteq(A\cap B)^{**}$.

Chiều $\subseteq$: $A\cap B\subseteq A\overset{\text{P4}}{\Rightarrow}(A\cap B)^{**}\subseteq A^{**}=A$. Tương tự $(A\cap B)^{**}\subseteq B^{**}=B$. Vậy $(A\cap B)^{**}\subseteq A\cap B$.

Kết hợp hai chiều: $(A\cap B)^{**}=A\cap B$. $\blacksquare$

---

## (L.E) — Đơn ánh của polar trên $\mathbb X$

**Phát biểu.** Nếu $A,B\in\mathbb X$ và $A^*=B^*$ thì $A=B$.

**Chứng minh.** Vì $A,B\in\mathbb X$: $A^{**}=A$, $B^{**}=B$. Từ $A^*=B^*$, lấy $(\cdot)^*$ hai vế: $A^{**}=B^{**}$, tức $A=B$. $\blacksquare$

---

## (L.F) — Polar của spatial sum

**Phát biểu.** Với mọi preepi $E,F$: $\ (E+_{\rm sp}F)^*=E^*+_{\rm fib}F^*$.

**Chứng minh.**

*Chiều $\supseteq$.* Nếu $(y,s_1)\in E^*$ và $(y,s_2)\in F^*$: với mọi $(x_1,r_1)\in E,(x_2,r_2)\in F$, có $\langle x_1,y\rangle\le r_1+s_1$ và $\langle x_2,y\rangle\le r_2+s_2$. Cộng hai bất đẳng thức, dùng **P7** (song tuyến): $\langle x_1+x_2,y\rangle=\langle x_1,y\rangle+\langle x_2,y\rangle\le r_1+r_2+(s_1+s_2)$. Vì $(x_1+x_2,r_1+r_2)$ chạy khắp $E+_{\rm sp}F$ khi $(x_1,r_1),(x_2,r_2)$ chạy khắp $E,F$, bất đẳng thức này đúng với mọi phần tử của $E+_{\rm sp}F$, nên $(y,s_1+s_2)\in(E+_{\rm sp}F)^*$.

*Chiều $\subseteq$.* Cố định $y$. Vì $E^*$ đóng-lên theo thớ (định nghĩa polar), viết $E^*_y=[e^*(y),+\infty]$ với $e^*(y):=\sup_{(x,r)\in E}(\langle x,y\rangle-r)$, tương tự $f^*(y)$ cho $F$. Giả sử $(y,s)\in(E+_{\rm sp}F)^*$: với mọi $(x_1,r_1)\in E,(x_2,r_2)\in F$,
$$\langle x_1+x_2,y\rangle\le r_1+r_2+s \overset{\text{P7}}{\iff} (\langle x_1,y\rangle-r_1)+(\langle x_2,y\rangle-r_2)\le s.$$
Lấy $\sup$ độc lập theo $(x_1,r_1)$ và $(x_2,r_2)$, áp **P8** (sup cộng tính trên biến độc lập):
$$e^*(y)+f^*(y) = \sup_{(x_1,r_1)}(\langle x_1,y\rangle-r_1) + \sup_{(x_2,r_2)}(\langle x_2,y\rangle-r_2) \le s.$$
Vậy $s\ge e^*(y)+f^*(y)$, tức $(y,s)\in E^*+_{\rm fib}F^*$. $\blacksquare$

---

## (L.G) — Giao hoán

**Phát biểu.** Với mọi preepi $E,F$: $\ E+_{\rm fib}F=F+_{\rm fib}E$ và $E+_{\rm sp}F=F+_{\rm sp}E$.

**Chứng minh.** Trực tiếp từ **P9** (giao hoán của $+$ trên $X$ và trên $\overline{\mathbb R}$): $E+_{\rm fib}F=\{(x,r+s):(x,r)\in E,(x,s)\in F\}=\{(x,s+r):(x,s)\in F,(x,r)\in E\}=F+_{\rm fib}E$. Tương tự với $+_{\rm sp}$, dùng thêm giao hoán trên $X$. $\blacksquare$

---

## (L.H) — Kết hợp của phép cộng mở rộng

**Phát biểu.** Với mọi $r,s,t\in\overline{\mathbb R}$ (quy ước Rockafellar): $(r+s)+t=r+(s+t)$.

**Chứng minh.** Đây chính là **P10**, thuần Level 0, không liên quan các toán tử preepi. Xem chứng minh chi tiết ở P10. $\blacksquare$

---

## (L.MP) — Bổ đề max-plus

**Phát biểu.** Với mọi $t,a,b\in\overline{\mathbb R}$: $\ t+\max(a,b)=\max(t+a,t+b)$.

**Chứng minh.** Đây chính là **P11**, thuần Level 0. Xem chứng minh chi tiết ở P11. $\blacksquare$

---

## (L.I) — Fiber sum của hai regepi tự động là regepi

**Phát biểu.** Nếu $A,B\in\mathbb X$ thì $A+_{\rm fib}B\in\mathbb X$, tức $(A+_{\rm fib}B)^{**}=A+_{\rm fib}B$ không cần đóng thêm.

**Chứng minh — thành phần $U$ (thuần primitive, đầy đủ).** Đây chính là **P12**: nếu $U(A)=A,U(B)=B$ thì $U(A+_{\rm fib}B)=A+_{\rm fib}B$. Chứng minh trực tiếp bằng định nghĩa $U$ và số học Rockafellar (P10) — xem P12. $\checkmark$

**Chứng minh — thành phần $\mathcal F,C,T$ (⚠️ có điều kiện, không thuần primitive).** Viết $A,B$ qua $a,b:X\to\overline{\mathbb R}$ **giả sử proper** (không nhận giá trị $-\infty$) **lồi, lsc** — đây là biểu diễn hàm số mà tài liệu gốc chưa chứng minh lại thuần túy từ $U,\mathcal F,C,T$ (xem P13). Với giả thiết này:

- **Lồi ($C$):** $h:=a+b$ là tổng hai hàm lồi, nên lồi — chuẩn.
- **Lsc ($\mathcal F,T$):** với $x_n\to x$, vì $a,b$ proper (hữu hạn hoặc $+\infty$, không $-\infty$), không xảy ra dạng $\infty-\infty$ khi lấy $\liminf$, nên bất đẳng thức superadditivity chuẩn của $\liminf$ áp dụng an toàn: $\liminf(a(x_n)+b(x_n))\ge\liminf a(x_n)+\liminf b(x_n)\ge a(x)+b(x)$. Vậy $h$ lsc.

Vậy $A+_{\rm fib}B\in\mathbb X$ **với điều kiện $a,b$ proper**. $\blacksquare$ *(có điều kiện)*

**Trạng thái tổng thể của (L.I):** thành phần $U$ đã chứng minh xong, vô điều kiện, thuần primitive. Thành phần $\mathcal F,C,T$ đã chứng minh **cho lớp con proper** của $\mathbb X$ (đủ dùng cho hầu hết các ứng dụng, ví dụ M1 áp cho các $E,F,G$ hữu hạn hoặc chỉ nhận $+\infty$), nhưng **chưa** chứng minh cho $\mathbb X$ đầy đủ (bao gồm cả các preepi improper như $1_\wedge=X\times\overline{\mathbb R}$, $e\equiv-\infty$) và **chưa** được hạ xuống hoàn toàn từ $U,\mathcal F,C,T$ một cách nội tại (đang mượn biểu diễn hàm lồi lsc). Đây là câu hỏi mở thật sự cho Milestone I.

---

## (L.UD) — Đơn vị đối ngẫu

**Phát biểu, phần 1.** $1_\wedge^*=1_\vee$, với $1_\wedge:=X\times\overline{\mathbb R}$, $1_\vee:=X\times\{+\infty\}$.

**Chứng minh.** $(y,s)\in1_\wedge^*\iff\langle x,y\rangle\le r+s\ \forall x\in X,\forall r\in\overline{\mathbb R}$. Lấy $r=-\infty$: cần $\langle x,y\rangle\le(-\infty)+s$. Nếu $s<+\infty$ (hữu hạn hoặc $-\infty$): $(-\infty)+s=-\infty$ theo quy ước Rockafellar, buộc $\langle x,y\rangle\le-\infty$ với mọi $x$ — vô lý trừ phi... thực ra $\langle x,y\rangle$ hữu hạn luôn, nên bất đẳng thức $\le-\infty$ không thể đúng, buộc $s=+\infty$. Ngược lại nếu $s=+\infty$: $r+s=+\infty$ luôn (mọi $r$, kể cả $r=-\infty$, theo quy ước), bất đẳng thức luôn đúng. Vậy $1_\wedge^*=X\times\{+\infty\}=1_\vee$. $\blacksquare$

**Phát biểu, phần 2.** $1_\triangle^*=1_\bigtriangledown$, với $1_\triangle:=X\times[0,+\infty]$, $1_\bigtriangledown:=(\{0\}\times[0,+\infty])\cup((X\setminus\{0\})\times\{+\infty\})$.

**Chứng minh.** $(y,s)\in1_\triangle^*\iff\langle x,y\rangle\le r+s\ \forall x\in X,\forall r\in[0,+\infty]$. Ràng buộc chặt nhất tại $r=0$: $\langle x,y\rangle\le s\ \forall x\in X$. Nếu $y\neq0$: vế trái không bị chặn trên khi $x$ chạy theo hướng $y$, buộc $s=+\infty$. Nếu $y=0$: cần $0\le s$, tức $s\in[0,+\infty]$. Vậy $1_\triangle^*=(\{0\}\times[0,+\infty])\cup((X\setminus\{0\})\times\{+\infty\})=1_\bigtriangledown$. $\blacksquare$

**Hệ quả (dùng L.A):** vì $1_\triangle\in\mathbb X$ hiển nhiên (hàm hằng $e\equiv0$, lồi, lsc, proper), $1_\triangle^{**}=1_\triangle$, nên $1_\bigtriangledown^*=(1_\triangle^*)^*=1_\triangle^{**}=1_\triangle$.

---

## (P.U) — Mệnh đề hợp nhất: Spator là đối ngẫu bipolar của Fibor

**Phát biểu.** Với mọi preepi $E,F$: $\ E\bigtriangledown F=(E^*\triangle F^*)^*$.

**Chứng minh.** Áp (L.F) lên $E,F$: $(E+_{\rm sp}F)^*=E^*+_{\rm fib}F^*$. Vậy
$$E\bigtriangledown F=(E+_{\rm sp}F)^{**}=\bigl((E+_{\rm sp}F)^*\bigr)^*=(E^*+_{\rm fib}F^*)^*\overset{\text{(L.A)}}{=}\bigl((E^*+_{\rm fib}F^*)^{**}\bigr)^*=(E^*\triangle F^*)^*.\qquad\blacksquare$$

---

## Bảng tổng kết

| API Lemma | Phát biểu (rút gọn) | Proposition dùng | Trạng thái |
|---|---|---|---|
| L.A | $E^{***}=E^*$ | P1, P2 | ✅ Hoàn tất, vô điều kiện |
| L.B | $(E\cup F)^*=E^*\cap F^*$ | trực tiếp định nghĩa | ✅ Hoàn tất, vô điều kiện |
| L.C | $E\vee F=(E^*\wedge F^*)^*$ | L.A, L.B | ✅ Hoàn tất, vô điều kiện |
| L.D | $(A\cap B)^{**}=A\cap B$ khi $A,B$ closed | P1, P2 (→P4) | ✅ Hoàn tất, vô điều kiện |
| L.E | $A^*=B^*\Rightarrow A=B$ trên $\mathbb X$ | định nghĩa $\mathbb X$ | ✅ Hoàn tất, vô điều kiện |
| L.F | $(E+_{\rm sp}F)^*=E^*+_{\rm fib}F^*$ | P7, P8 | ✅ Hoàn tất, vô điều kiện |
| L.G | $+_{\rm fib},+_{\rm sp}$ giao hoán | P9 | ✅ Hoàn tất, vô điều kiện |
| L.H | kết hợp của $+$ trên $\overline{\mathbb R}$ | P10 (Level 0) | ✅ Hoàn tất, vô điều kiện |
| L.MP | $t+\max(a,b)=\max(t+a,t+b)$ | P11 (Level 0) | ✅ Hoàn tất, vô điều kiện |
| **L.I** | $A,B\in\mathbb X\Rightarrow A+_{\rm fib}B\in\mathbb X$ | P12 ($U$) $+$ **hàm lồi/lsc proper** ($\mathcal F,C,T$) | ⚠️ **$U$: xong. $\mathcal F,C,T$: chỉ đúng cho $a,b$ proper, chưa hạ xuống thuần primitive, chưa phủ hết $\mathbb X$** |
| L.UD | $1_\wedge^*=1_\vee$, $1_\triangle^*=1_\bigtriangledown$ | trực tiếp định nghĩa | ✅ Hoàn tất, vô điều kiện |
| P.U | $E\bigtriangledown F=(E^*\triangle F^*)^*$ | L.A, L.F | ✅ Hoàn tất, vô điều kiện |

**Điểm mấu chốt còn treo:** toàn bộ hệ thống lemma đã tự chứa và vô điều kiện, **trừ đúng một chỗ** — thành phần $\mathcal F,C,T$ của (L.I). Vì (L.I) là chốt duy nhất cho **M1** (kết hợp tính Fibor) và gián tiếp **M3** (kết hợp tính Spator, đi qua M1 bằng polar), toàn bộ khối monoid hiện **đúng vô điều kiện cho lớp con proper của $\mathbb X$**, và **cần thêm chứng minh** (hoặc một phản ví dụ) để xác định liệu nó có còn đúng khi cho phép các regepi improper (như $1_\wedge$) tham gia hay không — đây là câu hỏi mở cụ thể, hẹp, và có thể kiểm định độc lập với phần còn lại của chương trình.
