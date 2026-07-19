# Research Program: Đóng của Fiber Sum trên Regepi

*(Quy ước: **[ĐÃ CM]** = đã chứng minh chặt trong quá trình thảo luận; **[MỞ]** = giả thuyết/mục tiêu chưa kiểm chứng; **[CẦN KIỂM]** = trích từ tài liệu ngoài (Tran, *Height Sets*), chưa được xác nhận độc lập trong chương trình này; **[SAI]** = đã có phản ví dụ, ghi lại để tránh lặp lại nhầm lẫn.)*

---

## Sec 1. Động cơ — Convexity, Logic, và kiến trúc Regepi

### 1.1. Bối cảnh

Không gian nền $\overline X := \mathbb R^n \times (-\infty,+\infty]$. Với $A \subseteq \overline X$, định nghĩa Fenchel polar
$$A^\ast := \{(y,s) \in \overline X : \langle x,y\rangle \le r+s \ \ \forall (x,r)\in A\}.$$

**Regepi**: $\mathbb X := \{E \subseteq \overline X : E = E^{\ast\ast}\}$. Trên $\mathbb X$ định nghĩa:
$$E \wedge F := E \cap F, \qquad E \oplus F := \big(E +_{fib} F\big)^{\ast\ast}, \qquad E +_{fib} F := \{(x,r+s): (x,r)\in E, (x,s)\in F\}.$$

Mục tiêu ban đầu (tài liệu gốc): chứng minh $(\mathbb X, \wedge, \oplus, \ast)$ là một **idempotent commutative semiring (ICS) với polar đối hợp**, dùng sáu tiên đề hộp đen:

- **Nhóm Pa (đại số/thứ tự):** Pa1 (antitone), Pa2 (extensive), Pa3 (upward-closed theo thớ).
- **Nhóm Pb (hình học/topo):** Pb1 (fiber-closed, đáy đạt được), Pb2 (topo-closed), Pb3 (convexity).

**Quan sát ban đầu gây ngạc nhiên** (Sec 4.6, tài liệu gốc): trong bảng tổng kết 11 tiên đề ICS, **cột Pb3 (convexity) trống hoàn toàn** — không tiên đề ICS nào viện dẫn tính lồi. Điều này mâu thuẫn với trực giác Fenchel–Moreau cổ điển, nơi $f=f^{\ast\ast} \iff f$ proper, **convex**, lsc — tức convexity tưởng chừng là điều kiện trung tâm.

### 1.2. Điểm nghẽn thật sự: Key Lemma

Toàn bộ việc xây ICS quy về đúng **một** bổ đề khó (điểm nghẽn duy nhất cho tiên đề S1 — kết hợp của $\oplus$ — và SM1 — phân phối $\oplus$ qua $\wedge$):

> **Key Lemma.** Với $E, F \in \mathbb X$: $E +_{fib} F \in \mathbb X$ (tức $(E+_{fib}F)^{\ast\ast} = E+_{fib}F$), và do đó $E \oplus F = E +_{fib} F$ (đẳng thức tập hợp thô, không cần đóng thêm).

Chứng minh gốc (Định lý 3.1.2, tài liệu chính) dùng lập luận dãy-điểm 4 bước (liminf, dùng Pb1+Pb2 áp trực tiếp cho $E, F$), nhưng qua nhiều lượt kiểm tra chi tiết đã lộ ra:

1. **Bước "lấy dãy $(x_k,u_k)\in A$ hội tụ tới điểm cho trước $(x_0,u_0)\in A^{\ast\ast}$"** trong chứng minh gốc là **không hợp lệ như đã viết** — nó ngầm giả định $A^{\ast\ast} = \overline{A}^{\,top}$, điều **chính là cái cần chứng minh**, không phải giả thiết có sẵn.
2. Việc "ráp" ba mảnh (đại số, lồi, topo) thành kết luận $A^{\ast\ast}\subseteq A$ **không phải một phép cộng liminf trực tiếp** — nó cần một bước tách điểm khỏi tập lồi đóng (Hahn–Banach hữu hạn chiều), đúng như tài liệu Tran gọi là "the single step that genuinely requires a convex-analytic separation argument".
3. Nếu thừa nhận công thức tổng quát $B^{\ast\ast} = T(C(U(B)))$ (Theorem 2, Tran) như hộp đen — trả chi phí Hahn–Banach **một lần duy nhất** cho toàn lý thuyết — thì Key Lemma thu gọn về kiểm ba mệnh đề sơ cấp: $U(A)=A$, $C(A)=A$, $T(A)=A$, trong đó chỉ mệnh đề cuối ($T(A)=A$, "tổng hai hàm lsc là lsc") thật sự khó, và nó **không cần tính lồi**.

Đây chính là lý do Sec 1 tồn tại: **quan sát "Pb3 trống" ở Sec 4.6 và "bước lồi (Tầng 2) độc lập với bước topo (Tầng 3)" ở Key Lemma là cùng MỘT hiện tượng**, nhìn từ hai phía khác nhau — cấu trúc ICS không cần convexity vì bản thân Key Lemma, khi phân rã đúng, cũng không cần convexity ở bước khó nhất.

### 1.3. Ý tưởng trung tâm cần hiện thực hóa (đề xuất khởi phát chương trình này)

$$
E +_{fib} F \ \overset{(1)}{=}\ E^{\ast\ast} +_{fib} F^{\ast\ast} \ \overset{(2)}{=}\ T(C(U(E))) +_{fib} T(C(U(F))) \ \overset{(3)}{=}\ T\big(C(U(E +_{fib} F))\big) \ \overset{(4)}{=}\ (E+_{fib}F)^{\ast\ast}.
$$

Nếu toàn bộ chuỗi đẳng thức này đúng, ta có ngay $E+_{fib}F$ là regepi — một chứng minh Key Lemma hoàn toàn khác, đi qua **tính phân phối của các toán tử đóng thành phần** thay vì lập luận dãy-điểm trực tiếp.

**Nhưng chuỗi này chứa ít nhất hai chỗ đáng ngờ, cần kiểm tra độc lập trước khi tin:**
- Đẳng thức (1): tầm thường, chỉ là $E,F\in\mathbb X$.
- Đẳng thức (2): áp dụng công thức phân rã $\ast\ast = T\circ C\circ U$ — **bản thân công thức này cần kiểm lại** (nó có điều kiện áp dụng: $E,F \ne \emptyset$, $E^\ast, F^\ast \ne \emptyset$, tức properness).
- Đẳng thức (3): đây là **tính phân phối của $T\circ C\circ U$ (như một khối) qua $+_{fib}$** — hoàn toàn chưa được chứng minh, và có lý do nghi ngờ mạnh: đã biết $T$ (đóng tô pô) **không** phân phối qua $+_{fib}$ một cách vô điều kiện (phản ví dụ dãy chẵn/lẻ, Sec 3 bên dưới), nên (3) — nếu đúng — phải đúng nhờ sự **phối hợp** giữa $U, C, T$ chứ không phải từng cái riêng lẻ.
- Đẳng thức (4): chính là công thức phân rã áp cho $E+_{fib}F$ — cần cùng điều kiện properness như (2), áp cho $A:=E+_{fib}F$.

Chương trình này nhằm kiểm tra chặt từng mắt xích.

---

## Sec 2. Mục tiêu nghiên cứu (chưa biết đúng/sai)

**Mục tiêu 1 — Tính phân rã của $\ast\ast$.**
Xác định chính xác điều kiện để
$$B^{\ast\ast} = T(C(U(B)))$$
đúng, với $B \subseteq \overline X$ tùy ý (không giả sử $B$ đã regular). Làm rõ vai trò của properness ($B\ne\emptyset$, $B^\ast\ne\emptyset$) và trường hợp suy biến.

**Mục tiêu 2 — Tính phân phối của $U, C, T$ trên fiber sum, với $E, F$ tổng quát (không giả sử $\in\mathbb X$).**
Với mỗi $\Phi \in \{U, C, T\}$ và mỗi tổ hợp của chúng, xác định:
$$\Phi(E +_{fib} F) \overset{?}{=} \Phi(E) +_{fib} \Phi(F)$$
đúng vô điều kiện, đúng có điều kiện (và điều kiện gì), hay sai (kèm phản ví dụ).

Hai mục tiêu này, ghép lại, quyết định chuỗi đẳng thức (1)-(4) ở Sec 1.3 có đứng vững hay không, và nếu không, chuỗi cần sửa ở đâu.

---

## Sec 3. Tính phân phối của $U, C, T$ trên Fiber Sum

### 3.1. $U$ phân phối — **[ĐÃ CM]**, vô điều kiện

**Định lý 3.1.** Với mọi $E, F \subseteq \overline X$:
$$U(E +_{fib} F) = U(E) +_{fib} U(F).$$

*Chứng minh.*
($\supseteq$) $(x,r) \in U(E)+_{fib}U(F)$: $r=r_1+r_2$, $\exists r_1'\le r_1, (x,r_1')\in E$; $\exists r_2'\le r_2, (x,r_2')\in F$. Thì $r_1'+r_2' \le r$ và $(x,r_1'+r_2')\in E+_{fib}F$, nên $(x,r)\in U(E+_{fib}F)$.

($\subseteq$) $(x,r)\in U(E+_{fib}F)$: $\exists r'\le r$, $r'=e+f$, $(x,e)\in E, (x,f)\in F$. Đặt $r_1:=e+(r-r')\ge e$, $r_2:=f$. Thì $(x,r_1)\in U(E)$, $(x,r_2)\in F\subseteq U(F)$, $r_1+r_2=r$. $\blacksquare$

**Nhận xét.** Đây là toán tử duy nhất trong ba toán tử phân phối **vô điều kiện, không cần $E,F$ đã có tính chất gì trước**. Lý do cấu trúc: $U$ là toán tử **địa phương theo thớ** (chỉ tác động trong từng $\{x\}\times(-\infty,+\infty]$ riêng biệt, không liên hệ các thớ khác nhau) — cùng họ với Lemma 6, 7 trong Tran (U commute với F, với C).

### 3.2. $C$ phân phối — **[SAI]** như luật tổng quát; **[MỞ]** dạng có điều kiện

**Phản ví dụ 3.2 (tính $C$ không phân phối vô điều kiện).** $X=\mathbb R$, $E=\{(0,0),(1,0)\}$, $F=\{(0,0),(2,0)\}$.
- $E+_{fib}F = \{(0,0)\}$ (chỉ $x=0$ chung miền), nên $C(E+_{fib}F) = \{(0,0)\}$.
- $C(E) = [0,1]\times\{0\}$, $C(F)=[0,2]\times\{0\}$; $\big(C(E)+_{fib}C(F)\big)_x = \{0\}$ với mọi $x\in[0,1]$, nên $C(E)+_{fib}C(F) = [0,1]\times\{0\} \ne \{(0,0)\}$.

Vậy $C(E+_{fib}F) \subsetneq C(E)+_{fib}C(F)$ nói chung — sai theo cả hai chiều so với kỳ vọng đẳng thức. **[MỞ]:** liệu bao hàm thức một chiều $C(E+_{fib}F) \subseteq C(E)+_{fib}C(F)$ có luôn đúng? (Chưa kiểm.)

**Bổ đề 3.2' — [ĐÃ CM] (trường hợp $E,F$ đã lồi sẵn, không phải luật phân phối tổng quát).** Nếu $C(E)=E$ và $C(F)=F$ thì $C(E+_{fib}F) = E+_{fib}F$ (tức $A:=E+_{fib}F$ tự động lồi).

*Chứng minh.* Lấy $(x_1,r_1),(x_2,r_2)\in A$, $r_i=e_i+f_i$, $(x_i,e_i)\in E,(x_i,f_i)\in F$. Với $\lambda\in[0,1]$:
$$\lambda(x_1,r_1)+(1-\lambda)(x_2,r_2) = \big[\lambda(x_1,e_1)+(1-\lambda)(x_2,e_2)\big] + \big[\lambda(x_1,f_1)+(1-\lambda)(x_2,f_2)\big] \in E+_{fib}F$$
vì ngoặc đầu $\in E$ (lồi), ngoặc sau $\in F$ (lồi), cùng $x=\lambda x_1+(1-\lambda)x_2$. $\blacksquare$

**Vai trò trong chương trình:** Bổ đề 3.2' là **tất cả những gì Key Lemma thật sự cần** từ phía convexity — nó không phải một "luật phân phối của $C$" theo nghĩa toán tử, mà là một sự kiện đại số kín (nếu input đã lồi thì output tự động lồi), không đòi hỏi $C$ giao hoán hay phân phối với bất kỳ điều gì khác.

### 3.3. $T$ phân phối — **[SAI]** như luật tổng quát; điều kiện đủ đã biết **[ĐÃ CM]**

**Phản ví dụ 3.3a (một thớ, $X=\{\text{pt}\}$, do người nêu câu hỏi cung cấp).** $A:=\{-2^k:k\ge1\}$, $B:=\{2^k-\tfrac1k:k\ge1\}$, cả hai đóng (rời rạc, không điểm tụ hữu hạn). Với $m=n$: $-2^n + 2^n - \tfrac1n = -\tfrac1n \to 0$, nên $0\in T(A+B)$. Kiểm trực tiếp mọi cặp $(a,b)\in(A\cup\{-\infty\})\times(B\cup\{+\infty\})$ khác: tổng không tiến về $0$. Vậy $0\notin T(A)+T(B) = A+B$, tức
$$T(A)+T(B) \subsetneq T(A+B).$$

**Phản ví dụ 3.3b (đa thớ, dựng riêng cho chương trình này, lộ đúng cơ chế "đường chéo theo $x$").** $X=\mathbb R$. $\mathrm{dom}(E) = \{1/2n : n\ge1\}$ (chỉ số chẵn), $E_{1/2n}=[0,\infty)$; $\mathrm{dom}(F) = \{1/(2n{+}1): n\ge0\}$ (chỉ số lẻ), $F_{1/(2n+1)}=[0,\infty)$. Hai domain rời nhau tuyệt đối. $E+_{fib}F=\emptyset$ (không có $x$ chung), nên $T(E+_{fib}F)=\emptyset$. Nhưng $T(E) \ni (0,0)$ (vì $1/2n\to0$, thớ đóng dọc dãy), tương tự $T(F)\ni(0,0)$, nên $T(E)+_{fib}T(F) \ni (0,0) \ne \emptyset$. Vậy
$$T(E+_{fib}F) = \emptyset \subsetneq T(E)+_{fib}T(F).$$

**Nhận xét cấu trúc quan trọng.** Phản ví dụ 3.3a (một thớ) và 3.3b (đa thớ) là **cùng một cơ chế đường chéo**, chỉ khác trục xảy ra: 3.3a xảy ra trên trục $r$ (giá trị, trong một thớ cố định); 3.3b xảy ra trên trục $x$ (giữa các thớ, khi $x_k\to x_0$). Cả hai đều bị triệt tiêu nếu có thêm điều kiện $U$:

**Định lý 3.3c — [ĐÃ CM] (T phân phối, có điều kiện $U$ + Pb1 dạng đạt-được, đây chính là nội dung thật của "Tầng 3" trong Key Lemma).** Nếu $U(E)=E$, $U(F)=F$, và với mọi $x$ mà $\inf E_x$ (resp. $F_x$) hữu hạn thì đạt được (đáy $\in E_x$) — và $T(E)=E$, $T(F)=F$ — thì:
$$T(E+_{fib}F) = E+_{fib}F \quad (\text{tức } A \text{ tự động đóng, không cần } T \text{ "phân phối" theo nghĩa toán tử}).$$

*Chứng minh (bản rút gọn, chi tiết đầy đủ đã làm ở Sec 4 phía dưới, xem "Tầng 3").* Lấy $(x_k,u_k)\in A$, $(x_k,u_k)\to(x_0,u_0)$; viết $u_k=\theta_E(x_k)+\theta_F(x_k)$ (đáy đạt được, do $U$+Pb1); chứng minh $\liminf_k\theta_E(x_k)\ge\theta_E(x_0)$ bằng phản chứng (dùng đóng của $E$, dãy con); cộng hai liminf; kết luận $u_0\ge\theta_A(x_0)$; dùng $U(A)=A$ (Định lý 3.1) để kết luận $(x_0,u_0)\in A$. $\blacksquare$

**Vì sao 3.3c không mâu thuẫn với phản ví dụ 3.3a/3.3b:** trong cả hai phản ví dụ, $E$ (hoặc $A,B$) **không upward** — chúng là các tập rời rạc, không phải tia. Điều kiện $U(E)=E$ nén toàn bộ thớ về một số $\theta_E(x)$ duy nhất, triệt tiêu "không gian" cần thiết để hiện tượng đường chéo tồn tại (không còn hai chỉ số độc lập để phối hợp).

**[MỞ], quan trọng cho chương trình:** Định lý 3.3c phát biểu $T(A)=A$ **trực tiếp** (không qua ngôn ngữ "$T$ phân phối vào $+_{fib}$ như toán tử"). Câu hỏi mở: có cách phát biểu 3.3c như đúng một **luật phân phối toán tử** $T(U(E))+_{fib}T(U(F)) = T(U(E+_{fib}F))$ hay không, và nó có tương đương với 3.3c hay mạnh/yếu hơn? (Cần kiểm — đây chính là đẳng thức (3) trong Sec 1.3, thu hẹp về trường hợp $C$ vắng mặt.)

### 3.4. Bảng tổng kết Sec 3

| $\Phi$ | Phân phối vô điều kiện? | Điều kiện đủ đã biết | Cơ chế phản ví dụ (nếu sai) |
|---|---|---|---|
| $U$ | **Đúng** (Định lý 3.1) | — | — |
| $C$ | Sai (3.2) | $E,F$ đã lồi $\Rightarrow A$ lồi (3.2') | Miền xác định của $E,F$ "gặp nhau" giả tạo sau khi lồi hóa riêng |
| $T$ | Sai (3.3a, 3.3b) | $E,F$ đã $U$-đóng + đáy đạt được + $T$-đóng $\Rightarrow A$ $T$-đóng (3.3c) | Đường chéo: hai dãy độc lập (rời rạc hoặc theo $x$) phối hợp tạo giới hạn hụt |

---

## Sec 4. Phân rã $\ast\ast$ theo $U, C, T$ và quan hệ với quotient qua $A\sim B \iff A^\ast=B^\ast$

### 4.1. Phát biểu phân rã — **[CẦN KIỂM]**, trích Tran, Theorem 2

$$
B^{\ast\ast} =
\begin{cases}
\emptyset & B=\emptyset,\\
\overline X & B\ne\emptyset, B^\ast=\emptyset,\\
T(C(U(B))) & B\ne\emptyset, B^\ast\ne\emptyset.
\end{cases}
$$

**Trạng thái trong chương trình này:** công thức này được **trích dẫn**, không phải chứng minh lại. Bước chứng minh khó nhất ẩn trong nó (Case C của Tran — điểm biên domain không đạt được, cần Rockafellar Thm 7.4/Cor 7.5.1) **chưa được kiểm tra độc lập** trong hội thoại này. Mục tiêu con của chương trình: hoặc (a) chấp nhận nó như hộp đen ngoài (trích dẫn Rockafellar), hoặc (b) tìm một chứng minh sơ cấp hơn cho trường hợp riêng $B = E+_{fib}F$ với $E,F\in\mathbb X$ — xem 4.3.

### 4.2. Quan hệ tương đương qua $\ast$ — khung diễn giải

Định nghĩa $A \sim B :\iff A^\ast = B^\ast$. Theo Lemma 4 (Tran) — **[CẦN KIỂM]**: $E^\ast = U(E)^\ast = C(E)^\ast = T(E)^\ast$, tức $U, C, T$ đều **cố định lớp tương đương** $[E]_\sim$. Vậy $R(E):=T(C(U(E)))$ chọn ra **đại diện chính quy** (regular representative) duy nhất của mỗi lớp $\sim$-tương đương mà $E^{\ast\ast}$ trùng với đại diện đó.

**Hệ quả diễn giải cho Sec 1.3:** đẳng thức (2) ($E^{\ast\ast} = T(C(U(E)))$) chỉ là phát biểu "$E$ đã là đại diện chính quy của lớp của chính nó" — tầm thường khi $E\in\mathbb X$ (regular sẵn). Đẳng thức (3) (phân phối của khối $TCU$ qua $+_{fib}$) **không** suy ra được từ 4.1 hay 4.2 — đây là nội dung thật sự cần chứng minh, và chính là Mục tiêu 2 (Sec 2), đã giải quyết một phần ở Sec 3: $U$ phân phối (3.1), $C$ không phân phối như toán tử nhưng đủ dùng ở dạng yếu (3.2'), $T$ không phân phối như toán tử nhưng đủ dùng ở dạng yếu có điều kiện (3.3c).

### 4.3. Kết luận tạm thời cho chuỗi đẳng thức Sec 1.3, và con đường thay thế đã xác lập

**Đánh giá chuỗi (1)-(4):** đẳng thức (3) — "$T(C(U(\cdot)))$ phân phối qua $+_{fib}$ như một khối toán tử" — **không được chứng minh** trong chương trình này và **không cần thiết**. Thay vào đó, ta có con đường thay thế **đã hoàn thiện từng bước** (Sec 3, tổng hợp lại):

$$
A^{\ast\ast} \overset{\text{4.1 (hộp đen, cần } A\ne\emptyset, A^\ast\ne\emptyset)}{=} T(C(U(A)))
\overset{\text{Định lý 3.1}}{=} T(C(A))
\overset{\text{Bổ đề 3.2'}}{=} T(A)
\overset{\text{Định lý 3.3c}}{=} A.
$$

Đây **không phải** chứng minh (3) như một luật phân phối tổng quát — nó là một chuỗi **thay giá trị cụ thể** ($U(A)=A$ từ 3.1 áp trực tiếp cho $A=E+_{fib}F$; $C(A)=A$ từ 3.2' vì $E,F$ đã lồi; $T(A)=A$ từ 3.3c vì $E,F$ đã $U,T$-đóng với đáy đạt được), hợp lệ đúng cho trường hợp $A=E+_{fib}F$ với $E,F\in\mathbb X$, không khẳng định gì cho $E,F$ tổng quát.

**Điều kiện còn treo (properness), cần kiểm trước khi áp dụng bước đầu:** phải xác nhận $A\ne\emptyset$ (tương đương $\pi(E)\cap\pi(F)\ne\emptyset$) và $A^\ast\ne\emptyset$ (đủ nếu $E^\ast,F^\ast\ne\emptyset$: lấy $(y,s_E)\in E^\ast,(y,s_F)\in F^\ast$ cùng $y$ thì $(y,s_E+s_F)\in A^\ast$ — kiểm trực tiếp, đại số). **[MỞ]:** liệu $E^\ast, F^\ast \ne\emptyset$ với $E,F\in\mathbb X\setminus\{\emptyset\}$ luôn đúng, hay có trường hợp suy biến ($E^\ast=\emptyset$, như $E=\overline X$ trong ví dụ SM2) cần loại trừ riêng?

### 4.4. So sánh hai chứng minh Key Lemma — vị trí của "chi phí Hahn–Banach"

| | Chứng minh gốc (dãy-điểm trực tiếp, Sec 3 tài liệu chính) | Chứng minh qua phân rã (chương trình này) |
|---|---|---|
| Chi phí Hahn–Banach/separation | Ẩn, không tường minh — nguồn gốc lỗi logic đã phát hiện (giả định ngầm $A^{\ast\ast}=\overline A$) | Tường minh, trả **một lần** trong công thức nền 4.1, không lặp lại cho từng $A$ cụ thể |
| Vai trò convexity | Không xuất hiện tường minh, nhưng thực chất ẩn trong bước "sandwich" | Tường minh: Bổ đề 3.2', độc lập hoàn toàn với bước $T$ |
| Bước khó nhất | Lập luận liminf 4 bước, khó tách bạch với phần lồi | Định lý 3.3c — chính là "tổng hai hàm lsc là lsc", không cần lồi |
| Trạng thái chặt chẽ | Có lỗ hổng đã xác nhận | Chặt, với điều kiện 4.1 được chấp nhận làm hộp đen |

---

## Sec 5. Danh mục việc cần làm (mở)

1. **[MỞ]** Kiểm chứng độc lập công thức 4.1 (Theorem 2, Tran) — đặc biệt "Case C" (Rockafellar 7.4/7.5.1) — hoặc tìm chứng minh sơ cấp thay thế cho trường hợp hẹp $B=E+_{fib}F$, $E,F\in\mathbb X$.
2. **[MỞ]** Xác định bao hàm thức một chiều cho $C$ (câu hỏi cuối 3.2): $C(E+_{fib}F) \subseteq C(E)+_{fib}C(F)$ luôn đúng?
3. **[MỞ]** Làm rõ quan hệ giữa Định lý 3.3c (dạng "$T(A)=A$ trực tiếp") và một phát biểu "luật phân phối toán tử" tương đương cho $T\circ U$ — có tồn tại không, và nếu có, mạnh/yếu hơn 3.3c thế nào.
4. **[MỞ]** Kiểm properness ($A\ne\emptyset$, $A^\ast\ne\emptyset$) một cách hệ thống, kể cả các trường hợp suy biến (như $E=\overline X$, liên quan SM2).
5. **[MỞ]** Đối chiếu lại toàn bộ bảng Sec 4.6 (tài liệu gốc) dưới ánh sáng của chương trình này: xác nhận lại chính xác Pa/Pb nào thật sự cần cho mỗi tiên đề ICS (S3, SM2 đã phát hiện cần điều chỉnh so với bảng gốc ở các lượt thảo luận trước; cần rà soát toàn bộ theo cùng chuẩn).

## Sec 6. Remark quan trọng — Phân cấp ba mức của "closure tương thích với một phép toán"

Cho $C$ là một toán tử đóng (closure operator: idempotent, extensive, monotone) trên $\mathcal P(\overline X)$, và $+$ là một phép toán hai ngôi tùy ý trên $\mathcal P(\overline X)$. Có ba mệnh đề, mạnh dần yếu:

**(1) Phân phối toán tử.**
$$C(E+F) = C(E) + C(F) \qquad \forall E,F \subseteq \overline X.$$

**(2) Đóng trên họ $C$-closed.**
$$C(E)=E,\ C(F)=F \ \Longrightarrow\ C(E+F)=E+F.$$

**(3) Cần điều kiện bổ sung $H$ để đóng trên $C$-closed.**
$$\exists H(E,F) \text{ (phát biểu bằng ngôn ngữ độc lập với kết luận)}:\quad C(E)=E,\ C(F)=F,\ H(E,F) \ \Longrightarrow\ C(E+F)=E+F.$$

**Quan hệ giữa ba mệnh đề: $1\Rightarrow 2\Rightarrow 3$, và cả hai chiều đều KHÔNG đảo được — phân cấp chặt (strict).**

*Chứng minh $1\Rightarrow2$.* Thay trực tiếp: $C(E+F)=C(E)+C(F)=E+F$ khi $E,F$ đã $C$-đóng. $\blacksquare$ (Tầm thường, không cần thêm giả thiết.)

*Nhân chứng $2\not\Rightarrow1$ — $C=\mathrm{conv}$, $+=+_{fib}$.* (1) sai: $E=\{(0,0),(1,0)\}$, $F=\{(0,0),(2,0)\}$ cho $C(E+_{fib}F)=\{(0,0)\} \subsetneq [0,1]\times\{0\}=C(E)+_{fib}C(F)$. (2) đúng: nếu $E,F$ đã lồi, tổ hợp lồi của hai điểm trong $E+_{fib}F$ tách thành tổng của hai tổ hợp lồi cùng tọa độ $x$ — một trong $E$, một trong $F$ — nên $E+_{fib}F$ tự động lồi, vô điều kiện, không cần $H$ nào thêm.

*Nhân chứng $3$ thật sự yếu hơn $2$ — $C=T$ (đóng tô pô), $+=+_{fib}$.* (2) sai: có $E,F$ đã đóng tô pô mà $E+_{fib}F$ không đóng — cơ chế "đường chéo", hai dạng:
- *Một thớ* ($X=\{\mathrm{pt}\}$): $A=\{-2^k:k\ge1\}$, $B=\{2^k-\tfrac1k:k\ge1\}$, cả hai đóng (rời rạc); $-2^n+2^n-\tfrac1n=-\tfrac1n\to0$ nhưng $0\notin A+B$.
- *Đa thớ*: $\mathrm{dom}(E)=\{1/2n\}$ (chẵn), $\mathrm{dom}(F)=\{1/(2n{+}1)\}$ (lẻ), hai domain rời nhau nhưng cùng tụ về $x=0$; $E+_{fib}F=\emptyset$ nhưng $T(E)+_{fib}T(F)\ni(0,0)$.

(3) đúng, với $H(E,F):=$ "$U(E)=E, U(F)=F$, và với mọi $x$, $\inf E_x$ (resp. $F_x$) hữu hạn thì đạt được" — phát biểu hoàn toàn bằng $U$ và tính đạt-được (Pb1), độc lập với kết luận về $T$. Đây là nội dung của Định lý 3.3c: bổ sung đúng $U$ triệt tiêu "không gian" cần thiết cho hiện tượng đường chéo (thớ bị nén về một số $\theta$ duy nhất, không còn hai chỉ số độc lập để phối hợp).

**Vị trí của $U$ trên thang bậc.** $U$ (Định lý 3.1: $U(E+_{fib}F)=U(E)+_{fib}U(F)$, vô điều kiện) nằm ở bậc (1) — mạnh nhất. Đây là lý do $U$ dùng được làm thành phần của điều kiện $H$ cho $T$ ở bậc (3): một toán tử đã ở bậc (1) có thể "cho mượn" tính chất của nó mà không sợ đảo ngược.

**Bảng tổng hợp ba toán tử của chương trình này trên đúng một thang bậc:**

| $C$             | (1)      | (2)                     | $H$ cần cho (3)                             |
| --------------- | -------- | ----------------------- | ------------------------------------------- |
| $U$             | **Đúng** | Đúng (hệ quả (1))       | $H=\emptyset$                               |
| $\mathrm{conv}$ | Sai      | **Đúng**, không cần $H$ | $H=\emptyset$                               |
| $T$             | Sai      | Sai                     | **Đúng** với $H=$ "$U$-đóng + đáy đạt được" |

**Cảnh báo về tính không-tầm-thường của $H$.** Điều kiện $H$ ở (3) chỉ có nội dung thật sự nếu được phát biểu bằng ngôn ngữ **độc lập** với kết luận — nếu cho phép $H(E,F):=\text{"}C(E+F)=E+F\text{"}$ thì (3) đúng một cách rỗng tuếch với mọi $C,+$. Chuẩn tối thiểu để chấp nhận một chứng minh dạng (3): $H$ phải được viết hoàn toàn bằng các toán tử/tính chất đã có sẵn trước đó trong lý thuyết (ở đây: $U$ và Pb1), không được viện dẫn ngược lại chính $C(E+F)=E+F$ hay bất kỳ hệ quả tương đương nào của nó.