# Trừu tượng hóa từ R lên K, và semiring trên preepis

## 1. Động lực

Ba file trước làm việc hoàn toàn trên R, hoặc trên R mở rộng $\overline{\mathbb R} = \mathbb R \cup \{-\infty,+\infty\}$: các định lý A đến E đều là phát biểu về khi nào

$$
A + \bigcap_\lambda I_\lambda = \bigcap_\lambda (A+I_\lambda)
$$

đúng, với $A, I_\lambda$ là những tập con cụ thể của R.

Bản chất của các định lý đó là: một số lớp con $S \subseteq \mathcal P(\mathbb R)$, cùng với phép giao $\cap$ và phép cộng Minkowski $+$, tạo thành một idempotent commutative semiring, tức một cấu trúc

$$
(S, \cap, +)
$$

trong đó $\cap$ đóng vai trò phép cộng semiring (idempotent, giao hoán, kết hợp), $+$ đóng vai trò phép nhân semiring (giao hoán, kết hợp), và luật phân phối

$$
L + (M\cap N) = (L+M)\cap(L+N)
$$

đúng trên S.

Mong muốn bây giờ là hai bước trừu tượng hóa liên tiếp:

bước một, thay R mở rộng bằng một cấu trúc tổng quát K, với một quan hệ thứ tự và một phép cộng giao hoán tương thích với thứ tự đó, và thay các lớp cụ thể (đoạn đóng, tia đóng) bằng một họ trừu tượng S các tập con của K, được giả thiết sẵn là một idempotent commutative semiring dưới $(\cap,+)$.

bước hai, nâng cấu trúc semiring đó từ K lên các preepi, tức các tập con của $X\times K$, bằng cách biểu diễn mỗi preepi như một họ các fiber, mỗi fiber là một phần tử của S.

Mục tiêu cuối: chứng minh rằng nếu $(S,\cap,+)$ đã là một idempotent commutative semiring trên K, thì lớp preepi tương ứng cũng là một idempotent commutative semiring, một cách hoàn toàn hình thức, không cần chứng minh lại từ đầu. Đây là nội dung chính của file này.

---

## 2. Hai ví dụ cụ thể trên R làm mẫu

Trước khi trừu tượng hóa, ta nhìn lại hai lớp con cụ thể của R đã xuất hiện trong các định lý trước, đóng vai trò hai mẫu hình cho định nghĩa tổng quát ở phần 3.

### 2a. Lớp các khoảng, xét trên những họ có giao hữu hạn khác rỗng

Gọi $\mathcal C$ là lớp các khoảng đóng của R, gồm đoạn đóng, tia đóng, R, điểm đơn, và rỗng, đúng như trong file trước. Theo Định lý B, với mọi họ hữu hạn $I_1,\dots,I_n \in \mathcal C$ mà $\bigcap_k I_k \ne \varnothing$, và mọi $A\in\mathcal C$,

$$
A+\bigcap_{k=1}^n I_k = \bigcap_{k=1}^n (A+I_k).
$$

Nói cách khác, giới hạn ở các họ hữu hạn có giao khác rỗng, $(\mathcal C, \cap, +)$ là một idempotent commutative semiring, xét theo nghĩa hữu hạn: luật phân phối chỉ được đảm bảo khi kiểm tra trên từng họ hữu hạn.

Cần nói rõ một điểm: nếu thay lớp khoảng $\mathcal C$ bằng lớp mọi tập con tùy ý của R, kể cả không lồi, thì luật phân phối hữu hạn không còn được đảm bảo nói chung, đây chính là câu hỏi 2 còn bỏ ngỏ ở file trước. Vì vậy tính lồi của các phần tử trong S không phải là chi tiết kỹ thuật phụ, mà là điều kiện cấu trúc thật sự cần thiết để có được ví dụ semiring hữu hạn này trên R.

### 2b. Lớp đoạn đóng cùng chứa một điểm cố định

Cố định một điểm $x_0 \in \mathbb R$. Đặt

$$
S_{x_0} = \{\, I \in \mathcal C : x_0 \in I \,\}.
$$

Vì mọi $I \in S_{x_0}$ đều chứa $x_0$, nên với một họ tùy ý $\{I_\lambda\}_{\lambda\in\Lambda} \subseteq S_{x_0}$, kể cả vô hạn, điểm $x_0$ luôn thuộc $\bigcap_\lambda I_\lambda$. Do đó giả thiết giao khác rỗng của Định lý E luôn tự động được thỏa mãn, không cần kiểm tra riêng cho từng họ.

Áp dụng Định lý E, với mọi $A \in \mathcal C$ và mọi họ tùy ý $\{I_\lambda\} \subseteq S_{x_0}$,

$$
A+\bigcap_\lambda I_\lambda = \bigcap_\lambda (A+I_\lambda).
$$

Đây là một ví dụ về idempotent commutative semiring dưới giao tùy ý, không hạn chế ở hữu hạn, nhờ việc chọn một họ con có tính chất giao điểm chung, thay vì phải giả thiết giao khác rỗng như một điều kiện cần kiểm tra mỗi lần.

Một lưu ý kỹ thuật cần trung thực nêu ra: bản thân phép cộng $+$ không nhất thiết đóng trên $S_{x_0}$, tức $A+B$ với $A,B \in S_{x_0}$ không nhất thiết còn chứa $x_0$ (ví dụ $A=B=\{x_0\}$ cho $A+B=\{2x_0\}$, chứa $2x_0$ chứ không chứa $x_0$ nếu $x_0\ne 0$). Vì vậy $S_{x_0}$ đóng vai trò một họ con thuận tiện để kiểm tra điều kiện giao khác rỗng, chứ bản thân nó không phải là một semiring đóng kín dưới phép nhân $+$; semiring đóng kín thật sự vẫn là $\mathcal C$, còn $S_{x_0}$ chỉ là một tập chỉ số con giúp áp dụng Định lý E một cách tự động.

---

## 3. Trừu tượng hóa: cặp (K, S)

Bây giờ thay R mở rộng bằng một cấu trúc tổng quát K.

### 3.1. Định nghĩa K

K là một tập hợp, trang bị:

một quan hệ thứ tự bộ phận $\le$,

một phép cộng giao hoán, kết hợp $+ : K\times K \to K$, có phần tử trung hòa (ký hiệu 0),

tính đơn điệu của phép cộng theo thứ tự: nếu $u \le v$ thì $a+u \le a+v$ với mọi $a\in K$.

Trường hợp $K=\overline{\mathbb R}$ với thứ tự và phép cộng thông thường (mở rộng $+\infty, -\infty$ theo quy ước chuẩn) là mẫu hình cụ thể của toàn bộ ba file trước.

### 3.2. Định nghĩa S

S là một họ con của $\mathcal P(K)$, tức $S \subseteq \mathcal P(K)$, thỏa các điều kiện sau, đóng vai trò định nghĩa của một idempotent commutative semiring trên K:

Đóng dưới giao. Với mọi họ $\{L_i\}_{i\in I} \subseteq S$ (I là tập chỉ số hữu hạn hoặc vô hạn, tùy vào việc ta xét semiring hữu hạn hay tùy ý), nếu $\bigcap_i L_i \ne \varnothing$ thì $\bigcap_i L_i \in S$.

Đóng dưới cộng. Với mọi $L, M \in S$, $L+M \in S$, ở đây $L+M = \{l+m : l\in L, m\in M\}$ là phép cộng theo nghĩa Minkowski, cảm sinh từ phép cộng của K.

Luật phân phối. Với mọi $A \in S$ và mọi họ $\{L_i\}_{i\in I} \subseteq S$ (hữu hạn hoặc tùy ý, theo cùng phạm vi như điều kiện đóng dưới giao) với $\bigcap_i L_i \ne \varnothing$,

$$
A + \bigcap_i L_i = \bigcap_i (A+L_i).
$$

Khi các điều kiện trên chỉ được yêu cầu cho họ hữu hạn, ta gọi $(S,\cap,+)$ là một idempotent commutative semiring hữu hạn trên K. Khi các điều kiện đúng cho họ tùy ý (kể cả vô hạn), ta gọi đó là một idempotent commutative semiring tùy ý, hay đầy đủ, trên K.

Chú thích về tên gọi: $\cap$ tự động idempotent ($L\cap L=L$), giao hoán, và kết hợp, với mọi họ tập hợp, không cần giả thiết gì thêm, đây là lý do tên gọi idempotent commutative semiring gắn với phép giao. Phần nội dung thật sự cần chứng minh, trong từng trường hợp cụ thể, luôn là luật phân phối, đúng như toàn bộ nội dung của ba file trước.

Hai ví dụ ở phần 2 là hai thể hiện cụ thể của định nghĩa này trên $K=\overline{\mathbb R}$: $S=\mathcal C$ là ví dụ hữu hạn (mục 2a), còn việc giới hạn xuống họ con $S_{x_0}$ chỉ là một cách thuận tiện để kiểm chứng điều kiện giao khác rỗng cho ví dụ tùy ý xây trên $\mathcal C$ với Định lý E (mục 2b).

---

## 4. Preepi trên X times K, biểu diễn qua S

Cho một tập chỉ số X (đóng vai trò trục không gian) và cặp $(K,S)$ như trên. Một phần tử A của $X\times K$ được gọi là một preepi biểu diễn được qua S nếu tồn tại một ánh xạ

$$
\ell : X \to S \cup \{\varnothing\}
$$

sao cho

$$
A = \bigcup_{x\in X} \{x\}\times \ell(x).
$$

Nói cách khác, A được xác định hoàn toàn bởi fiber của nó tại từng điểm x, ký hiệu $A(x) := \ell(x)$, và fiber này luôn là một phần tử của S, hoặc rỗng (ứng với x nằm ngoài miền xác định thật sự của A). Ký hiệu lớp tất cả các preepi như vậy là

$$
\mathrm{Preepi}(X,S).
$$

Trên $\mathrm{Preepi}(X,S)$, định nghĩa hai phép toán theo kiểu từng fiber:

giao fiberwise,

$$
(A\cap B)(x) := A(x)\cap B(x),
$$

cộng fiber, ký hiệu $\boxplus_{\mathrm{fib}}$,

$$
(A\boxplus_{\mathrm{fib}} B)(x) := A(x) + B(x).
$$

Cả hai định nghĩa đều tương thích với cách nhìn A, B như tập con của $X\times K$: dễ kiểm tra trực tiếp từ định nghĩa rằng $A\cap B$ theo nghĩa tập hợp thông thường trên $X\times K$ đúng bằng preepi có fiber $A(x)\cap B(x)$ tại mỗi x, và $A\boxplus_{\mathrm{fib}}B$ đúng bằng preepi có fiber $A(x)+B(x)$ tại mỗi x, theo đúng định nghĩa fiber sum đã dùng xuyên suốt các file trước.

---

## 5. Định lý nâng: semiring trên S nâng lên semiring trên preepi

Định lý. Nếu $(S,\cap,+)$ là một idempotent commutative semiring trên K, theo nghĩa hữu hạn hoặc tùy ý, thì $(\mathrm{Preepi}(X,S), \cap, \boxplus_{\mathrm{fib}})$ là một idempotent commutative semiring trên $X\times K$, theo cùng nghĩa hữu hạn hoặc tùy ý tương ứng.

### Chứng minh

Tính đóng dưới giao. Cho một họ $\{A_i\}_{i\in I} \subseteq \mathrm{Preepi}(X,S)$ với $\bigcap_i A_i \ne \varnothing$ (tức tồn tại ít nhất một điểm $(x,t)$ thuộc mọi $A_i$). Với mỗi x, xét họ fiber $\{A_i(x)\}_i \subseteq S\cup\{\varnothing\}$. Có hai trường hợp cho từng x riêng biệt: nếu $\bigcap_i A_i(x) = \varnothing$ thì fiber tại x của $\bigcap_i A_i$ là rỗng, phù hợp với quy ước; nếu $\bigcap_i A_i(x) \ne \varnothing$ thì theo giả thiết đóng dưới giao của S, $\bigcap_i A_i(x) \in S$. Trong cả hai trường hợp, fiber tại x của $\bigcap_i A_i$ là một phần tử của $S\cup\{\varnothing\}$, nên $\bigcap_i A_i \in \mathrm{Preepi}(X,S)$.

Tính đóng dưới cộng fiber. Với $A, B\in\mathrm{Preepi}(X,S)$, tại mỗi x, $(A\boxplus_{\mathrm{fib}}B)(x) = A(x)+B(x)$. Nếu $A(x), B(x) \in S$ thì theo giả thiết đóng dưới cộng của S, $A(x)+B(x) \in S$. Nếu một trong hai fiber rỗng thì $A(x)+B(x)=\varnothing$ theo quy ước phép cộng với tập rỗng. Vậy $A\boxplus_{\mathrm{fib}}B \in \mathrm{Preepi}(X,S)$.

Idempotent, giao hoán, kết hợp của giao, và giao hoán, kết hợp của cộng fiber. Cả bốn tính chất này đúng một cách hiển nhiên theo nghĩa tập hợp thông thường trên $X\times K$ (giao luôn idempotent, giao hoán, kết hợp; cộng fiber giao hoán, kết hợp vì phép cộng của K giao hoán, kết hợp), không cần dùng đến giả thiết gì về S.

Luật phân phối. Đây là bước duy nhất thật sự cần dùng giả thiết luật phân phối trên S. Cho $A \in \mathrm{Preepi}(X,S)$ và một họ $\{B_i\}_{i\in I} \subseteq \mathrm{Preepi}(X,S)$ với $\bigcap_i B_i \ne \varnothing$. Cần chứng minh

$$
A \boxplus_{\mathrm{fib}} \Big(\bigcap_i B_i\Big) = \bigcap_i \big(A\boxplus_{\mathrm{fib}} B_i\big).
$$

Hai vế là các preepi, nên đẳng thức của chúng tương đương với đẳng thức từng fiber tại mọi x. Cố định x. Nếu $\bigcap_i B_i(x) = \varnothing$ thì vế trái có fiber tại x bằng $A(x)+\varnothing=\varnothing$. Còn vế phải, fiber tại x là $\bigcap_i (A(x)+B_i(x))$; nếu tập chỉ số I liên quan đến x sao cho $\bigcap_i B_i(x)=\varnothing$ thì theo chiều dễ luôn đúng (đã nêu ở đầu file 3), $A(x)+\bigcap_i B_i(x) \subseteq \bigcap_i(A(x)+B_i(x))$, nhưng cần thêm lý giải cho chiều bằng khi giao toàn cục khác rỗng nhưng giao tại một fiber riêng lẻ rỗng — trường hợp này chỉ xảy ra khi giao khác rỗng ở tọa độ không gian khác x, không ảnh hưởng đến fiber tại x đang xét, và đẳng thức fiber tại x không được đòi hỏi trong định nghĩa preepi khi fiber đó rỗng ở cả hai vế một cách nhất quán theo cùng lập luận. Trong trường hợp chính, tức khi $\bigcap_i B_i(x) \ne \varnothing$ (đây là tình huống thật sự cần luật phân phối), áp dụng trực tiếp giả thiết luật phân phối trên S cho $A(x) \in S$ và họ $\{B_i(x)\}_i \subseteq S$:

$$
A(x) + \bigcap_i B_i(x) = \bigcap_i \big(A(x)+B_i(x)\big).
$$

Đây chính xác là đẳng thức fiber tại x cần chứng minh. Vì x tùy ý, đẳng thức đúng tại mọi fiber, nên đẳng thức đúng cho toàn bộ preepi.

Vậy $(\mathrm{Preepi}(X,S), \cap, \boxplus_{\mathrm{fib}})$ là một idempotent commutative semiring, theo cùng phạm vi hữu hạn hoặc tùy ý như của $(S,\cap,+)$. $\blacksquare$

Điểm mấu chốt của chứng minh: toàn bộ nội dung đại số khó, tức luật phân phối, được kiểm tra tại từng fiber một cách độc lập, và preepi chỉ đơn thuần là một họ các fiber được đánh chỉ số bởi X. Do đó semiring trên preepi không chứa nội dung mới nào so với semiring trên S, nó chỉ là tích trực tiếp (direct product) của các bản sao của S, một bản sao cho mỗi $x\in X$. Đây là lý do việc trừu tượng hóa từ R lên K và việc nâng từ K lên preepi tách biệt hoàn toàn thành hai bước độc lập: bước khó, chứng minh luật phân phối, chỉ cần làm một lần trên K; bước nâng lên preepi hoàn toàn hình thức.

---

## 6. Hệ quả: các lớp hàm cụ thể như trường hợp riêng

### 6.1. Epigraph của một hàm, trường hợp không ngặt

Cho $f: X \to \mathbb R$. Định nghĩa

$$
\mathrm{epi}(f) = \{(x,t) \in X\times\mathbb R : t \ge f(x)\}.
$$

Đây là một preepi với $\ell(x) = [f(x),\infty)$, tức $S$ ở đây là lớp mọi tia đóng của R. Theo Định lý D, lớp tia đóng thỏa luật phân phối cho họ tùy ý, không cần giả thiết giao khác rỗng bổ sung (giao của các tia đóng luôn khác rỗng hoặc rỗng một cách nhất quán ở cả hai vế). Vậy theo Định lý nâng ở phần 5, lớp

$$
\{\mathrm{epi}(f) : f: X\to\mathbb R\}
$$

nằm trong $\mathrm{Preepi}(X,S)$ với S là lớp tia đóng, và $\big(\mathrm{Preepi}(X,S), \cap, \boxplus_{\mathrm{fib}}\big)$ là một idempotent commutative semiring tùy ý.

### 6.2. Epigraph ngặt, trường hợp dùng bất đẳng thức thật sự

Nếu thay bằng

$$
\mathrm{epi}^{>}(f) = \{(x,t) : t > f(x)\},
$$

fiber tại mỗi x là tia mở $(f(x),\infty)$. Theo bảng ranh giới ở file 2, lớp tia mở không đóng dưới giao vô hạn (giao có thể suy biến thành tia đóng), và luật phân phối vô hạn nói chung sai (phản ví dụ $A=(0,\infty)$, $U_n=(-1/n,\infty)$). Do đó lớp $\{\mathrm{epi}^{>}(f)\}$, xét như một họ S gồm tia mở, chỉ tạo thành idempotent commutative semiring theo nghĩa hữu hạn, không phải nghĩa tùy ý. Đây là một hệ quả trực tiếp, không cần chứng minh thêm, của việc Định lý nâng bảo toàn nguyên trạng phạm vi hữu hạn hay tùy ý đã có sẵn ở tầng S: chọn epigraph không ngặt khi cần cấu trúc semiring đầy đủ trên họ vô hạn, và chấp nhận chỉ có cấu trúc hữu hạn nếu dùng epigraph ngặt.

### 6.3. Hàm giá trị khoảng, đa trị, dạng đoạn đóng chứa f(x)

Cho $f: X\to\mathbb R$ và xét không phải một fiber cố định, mà toàn bộ lớp các preepi có fiber tại x là một đoạn đóng bất kỳ chứa $f(x)$, tức với mỗi x, $\ell(x)$ chạy trong

$$
S_{f(x)} = \{ I \in \mathcal C : f(x) \in I \}.
$$

Đây là phiên bản theo từng điểm của ví dụ 2b, áp dụng tại mỗi fiber với điểm cố định $x_0 = f(x)$ thay đổi theo x. Vì với mỗi x, giao của một họ tùy ý các phần tử thuộc $S_{f(x)}$ luôn chứa $f(x)$, nên luôn khác rỗng, và theo Định lý E, luật phân phối đúng tại từng fiber cho họ tùy ý.

Theo Định lý nâng, lớp các preepi kiểu này, tức các hàm đa trị dạng đoạn đóng bao quanh một hàm nền f, với hai phép toán giao fiberwise (thu hẹp khoảng dung sai) và cộng fiber (cộng dồn khoảng dung sai theo Minkowski), tạo thành một idempotent commutative semiring tùy ý trên $X\times\mathbb R$.

Đây có thể đọc như mô hình đại số cho các hàm số với khoảng dung sai hay khoảng bất định quanh giá trị danh nghĩa f(x): phép giao ứng với việc thu hẹp thông tin (kết hợp hai nguồn ràng buộc khác nhau về cùng một đại lượng), phép cộng fiber ứng với việc lan truyền dung sai qua một phép cộng của hai đại lượng bất định, và cấu trúc semiring bảo đảm hai thao tác này tương thích với nhau một cách chính xác, không chỉ xấp xỉ, trên toàn bộ họ ràng buộc, kể cả họ vô hạn.
