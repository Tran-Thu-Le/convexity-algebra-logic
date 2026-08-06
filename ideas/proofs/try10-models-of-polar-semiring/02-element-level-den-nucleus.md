# Từ tầng phần tử đến nucleus

## Dữ liệu nguyên thủy

Xuất phát điểm là một tập $M$ mang hai cấu trúc:

Một phép cộng $+ : M \times M \to M$, lý tưởng nhất là làm cho $(M, +, 0)$ thành một monoid giao hoán.

Một quan hệ $\perp \subseteq M \times M$, đối xứng: $x \perp y \iff y \perp x$.

Không có gì khác được giả sử. Không có thứ tự, không có topology, không có tuyến tính. Mọi cấu trúc bổ sung, nếu cần, sẽ được thêm vào như một giả thiết tường minh chứ không phải ngầm định.

Trước khi đi tiếp, hãy giữ trong đầu một ví dụ mẫu để làm điểm tựa trực giác xuyên suốt file này.

Ví dụ Fenchel. Lấy $M = \mathbb R^n \times \mathbb R$, phép cộng theo tọa độ $(p,w) + (r,v) = (p+r, w+v)$, và

$$
(p,w) \perp (q,s) \iff \langle p,q \rangle \le w + s.
$$

Phần tử thứ hai của mỗi cặp đóng vai trò một "ngân sách": quan hệ $\perp$ nói rằng tích vô hướng giữa hai phần thứ nhất không vượt quá tổng hai ngân sách.

## Polarity và bipolar

Với mỗi $A \subseteq M$, đặt

$$
A^* := \{ y \in M : x \perp y \ \text{với mọi } x \in A \}.
$$

Vì $\perp$ đối xứng, phép lấy polar hai lần

$$
c(A) := A^{**}
$$

là một closure operator theo nghĩa quen thuộc: $A \subseteq c(A)$, $A \subseteq B \Rightarrow c(A) \subseteq c(B)$, và $c(c(A)) = c(A)$. Điều này đúng với mọi quan hệ đối xứng, không cần thêm giả thiết gì. Ta gọi $A$ là đóng nếu $A = A^{**}$.

Trong ví dụ Fenchel, đây chính là bao đóng theo nghĩa hàm liên hợp: $c(A)$ tương ứng với epigraph của hàm lồi đóng nhỏ nhất chứa dữ liệu của $A$.

## Tensor và câu hỏi trung tâm

Phép cộng trên $M$ nâng lên thành phép cộng Minkowski trên các tập con:

$$
A \otimes B := A + B = \{ a + b : a \in A,\ b \in B \}.
$$

Câu hỏi trung tâm của toàn bộ dự án là: khi nào phép closure $c$ tương thích với phép tensor này, theo nghĩa

$$
c(A) \otimes c(B) \subseteq c(A \otimes B) \tag{N}
$$

với mọi $A, B \subseteq M$? Đây gọi là điều kiện nucleus.

Điều kiện này không tầm thường chút nào. Bao đóng của $A$ có thể lớn hơn $A$ rất nhiều, và khi ta cộng hai tập đã phồng lên như vậy, không có lý do tiên nghiệm nào để tổng đó vẫn nằm trong bao đóng của tổng ban đầu. Chính xác đây là chỗ mà chứng minh định lý Fenchel truyền thống cần đến một thao tác kỹ thuật: tách một "ngân sách" $s$ thành $s = s_A + s_B$ sao cho mỗi phần dùng cho đúng một tập. Mục tiêu của phần tiếp theo là làm rõ thao tác tách ấy thực chất là gì, ở mức trừu tượng nhất có thể.

## Từ tensor xuống một phép tịnh tiến duy nhất

Quan sát mấu chốt: kiểm tra điều kiện (N) cho mọi cặp tập $A, B$ nghe có vẻ là một lượng tử phổ dụng khó kiểm soát. Nhưng ta có thể quy nó về việc kiểm tra một họ tập rất đặc biệt: các tập chỉ gồm một phần tử.

Với $x \in M$ cố định và $C \subseteq M$ bất kỳ, định nghĩa phép tịnh tiến ngược

$$
x \to C := \{ m \in M : x + m \in C \}.
$$

Đây là tập hợp tất cả những gì có thể cộng thêm vào $x$ để vẫn rơi vào $C$. Phép toán này chính là internal hom của tensor trên $\mathcal P(M)$, theo nghĩa

$$
\{x\} + D \subseteq C \iff D \subseteq x \to C.
$$

Ý tưởng bây giờ là: nucleus đúng khi và chỉ khi phép tịnh tiến ngược này bảo toàn tính đóng.

## Định lý đặc trưng

Định lý. Cho $(M,+)$ monoid giao hoán, $\perp$ quan hệ đối xứng, $c(A) = A^{**}$. Ba điều sau tương đương.

(i) Nucleus: $c(A) + c(B) \subseteq c(A+B)$ với mọi $A, B \subseteq M$.

(ii) Điều kiện phản xạ: với mọi $x \in M$ và mọi tập đóng $C$, tập $x \to C$ cũng đóng.

(iii) Điều kiện ở mức phần tử: với mọi $x, y \in M$, tập

$$
D_{x,y} := \{ m \in M : (x+m) \perp y \}
$$

là một tập đóng, tương đương là một tập polar: $D_{x,y} = Y^*$ với $Y$ nào đó.

Trước khi chứng minh, đáng dừng lại để cảm nhận vì sao (iii) là điều đáng giá nhất trong ba điều. Nó không lượng hóa trên tập con nào cả, chỉ trên hai phần tử $x, y$ của $M$. Nó nói: cố định $y$, và hỏi tập hợp những $m$ mà khi cộng vào $x$ thì $\perp$-liên hệ được với $y$, tập đó có phải một tập polar hay không. Đây là một câu hỏi có thể kiểm tra trực tiếp trên công thức định nghĩa $\perp$, không cần đụng đến closure operator một cách trừu tượng.

Chứng minh (i) suy ra (ii). Lấy $C$ đóng, đặt $D = x \to C$. Theo định nghĩa, $\{x\} + D \subseteq C$. Áp dụng (i) cho cặp tập $\{x\}$ và $D$:

$$
c(\{x\}) + c(D) \subseteq c(\{x\} + D) \subseteq c(C) = C.
$$

Vì $x \in c(\{x\})$ luôn đúng (do $A \subseteq A^{**}$), suy ra $x + c(D) \subseteq C$, tức $c(D) \subseteq x \to C = D$. Kết hợp với $D \subseteq c(D)$ luôn đúng, ta có $D = c(D)$, tức $D$ đóng.

Chứng minh (ii) suy ra (i). Đặt $C := c(A+B)$, là một tập đóng chứa $A + B$. Với mỗi $a \in A$ cố định, từ $\{a\} + B \subseteq C$ suy ra $B \subseteq a \to C$. Vì $a \to C$ đóng theo (ii), và $c$ là closure operator nhỏ nhất chứa $B$, ta có $c(B) \subseteq a \to C$, tức $A + c(B) \subseteq C$. Bây giờ lặp lại lý luận theo biến còn lại: với mỗi $b \in c(B)$ cố định, từ $A + \{b\} \subseteq C$ suy ra $A \subseteq b \to C$, đóng theo (ii), nên $c(A) \subseteq b \to C$. Điều này đúng với mọi $b \in c(B)$, nên $c(A) + c(B) \subseteq C = c(A+B)$.

Chứng minh (ii) tương đương (iii). Mọi tập đóng $C$ đều viết được dưới dạng giao của các polar đơn phần tử: $C = Y^{**}$ với $Y = C$, và $Y^* = \bigcap_{y \in Y} \{y\}^*$. Phép tịnh tiến ngược giao hoán với phép giao: $x \to \bigcap_i C_i = \bigcap_i (x \to C_i)$, và với $C = \{y\}^*$ ta tính trực tiếp

$$
x \to \{y\}^* = \{ m : x + m \in \{y\}^* \} = \{ m : (x+m) \perp y \} = D_{x,y}.
$$

Vì họ các tập đóng ổn định dưới phép giao tùy ý, (iii) áp dụng cho từng $y \in Y$ kéo theo (ii) áp dụng cho $C = Y^*$ bất kỳ, và mọi tập đóng đều có dạng này. Chiều ngược lại, lấy $C = \{y\}^*$ trong (ii) chính là (iii). $\blacksquare$

Đây chính là dạng $\mathcal P(M)$ của định lý phản xạ Day, kết quả kinh điển trong lý thuyết phạm trù đóng nói rằng closure đi qua được tensor khi và chỉ khi lớp các đối tượng đóng ổn định dưới internal hom. Điều thú vị ở đây là: trên $\mathcal P(M)$ cụ thể, internal hom lại quy được hoàn toàn về mức phần tử của $M$, và đó là nội dung của (iii).

## Một điều kiện đủ dễ kiểm tra: residuation

Điều kiện (iii) là cần và đủ, nhưng để kiểm tra một ví dụ cụ thể, thường tiện hơn nếu có một tiêu chuẩn mang tính xây dựng. Đây là nơi khái niệm residuation xuất hiện tự nhiên.

Giả sử với mọi $x, y \in M$ tồn tại một phần tử $x \backslash y \in M$, đóng vai trò "phần còn lại sau khi trừ $x$", sao cho

$$
(x+m) \perp y \iff m \perp (x \backslash y) \qquad \text{với mọi } m.
$$

Khi đó ngay lập tức $D_{x,y} = \{m : m \perp (x \backslash y)\} = \{x \backslash y\}^*$, một tập polar theo đúng định nghĩa. Vậy điều kiện (iii) tự động thỏa mãn, và nucleus đúng.

Tại sao gọi đây là residuation? Vì công thức trên chính xác là công thức định nghĩa phần dư trong một quantale: $x \backslash y$ là phần tử lớn nhất theo nghĩa quan hệ sao cho "cộng $x$ vào rồi kiểm tra $\perp y$" tương đương với "kiểm tra $\perp (x \backslash y)$" trực tiếp. Nói cách khác, tồn tại residuation chính là nói $\perp$ "biết cách hấp thụ phép tịnh tiến $+x$ vào chính nó".

## Ba ví dụ qua lăng kính residuation

Ví dụ Fenchel. Với $x = (p,w)$, $y = (q,s)$, khai triển trực tiếp:

$$
\langle p+r, q \rangle \le w+v+s \iff \langle r,q \rangle \le v + (w+s-\langle p,q\rangle).
$$

Vậy $x \backslash y = (q,\ w+s-\langle p,q\rangle)$. Residuation tồn tại nhờ tính song tuyến tính của tích vô hướng, cho phép tách $\langle p+r,q\rangle$ thành $\langle p,q\rangle + \langle r,q\rangle$. Đây chính là thao tác "tách ngân sách" trong chứng minh cổ điển, chỉ khác là bây giờ nó lộ rõ là một trường hợp riêng của một cơ chế tổng quát hơn nhiều.

Ví dụ phase semantics. Nếu $\perp$ có dạng $x \perp y \iff x + y \in D$ với một "pole" $D \subseteq M$ cố định, residuation gần như tầm thường: $x \backslash y = x + y$, vì $(x+m) + y \in D \iff m + (x+y) \in D$ nhờ tính giao hoán và kết hợp của $+$. Đây là lý do tại sao quantale các "facts" trong ngữ nghĩa pha của logic tuyến tính luôn được định nghĩa tốt, mà không cần bất kỳ giả thiết bổ sung nào ngoài $+$ là monoid giao hoán.

Ví dụ kernel toàn phương. Lấy $M = \mathbb R^n \times \mathbb R$ như trước, nhưng thay quan hệ Fenchel bằng

$$
(p,w) \perp (q,s) \iff \tfrac12 \|p-q\|^2 \le w+s.
$$

Mấu chốt ở đây không phải tính lồi hay tuyến tính, mà là tính bất biến tịnh tiến của kernel: $\tfrac12\|(p+r)-q\|^2 = \tfrac12\|r-(q-p)\|^2$. Từ đó

$$
(p+r,w+v) \perp (q,s) \iff (r,v) \perp (q-p,\ w+s),
$$

nên $x \backslash y = (q-p,\ w+s)$. Vậy nucleus đúng cho kernel toàn phương, và bipolar sinh ra ở đây chính là bao đóng gần kề, proximal hull, một khái niệm quan trọng trong giải tích biến phân. Điều đáng chú ý: toàn bộ lập luận không hề dùng đến việc $\tfrac12\|\cdot\|^2$ là hàm lồi.

Nhìn ba ví dụ cùng lúc, một quy luật chung xuất hiện.

Mệnh đề. Cho $X$ nhóm giao hoán, $\varphi : X \times X \to \mathbb R$, $M = X \times \mathbb R$, và $(p,w) \perp (q,s) \iff \varphi(p,q) \le w+s$. Nếu tồn tại $\tau(p,q) \in X$ và $\delta(p,q) \in \mathbb R$ sao cho

$$
\varphi(p+r,q) = \varphi(r,\tau(p,q)) + \delta(p,q) \qquad \text{với mọi } r,
$$

thì $x \backslash y = (\tau(p,q),\ w+s-\delta(p,q))$, và nucleus đúng.

Trường hợp riêng đáng nhớ nhất: mọi kernel bất biến tịnh tiến $\varphi(p,q) = \psi(q-p)$ trên một nhóm, với $\psi$ hoàn toàn tùy ý, đều sinh nucleus. Đây là một phát biểu mạnh hơn nhiều so với những gì trực giác "phải lồi mới đúng" gợi ý.

## Khi trực giác sai: additivity không đủ và không cần

Có một ứng viên rất tự nhiên cho điều kiện đủ, thoạt nhìn có vẻ đúng hướng: nếu $x_1 \perp y_1$ và $x_2 \perp y_2$ thì $x_1+x_2 \perp y_1+y_2$. Gọi đây là additivity của $\perp$. Đáng để kiểm tra kỹ điều này, vì nó là thứ đầu tiên ai cũng nghĩ đến.

Additivity không đủ. Lấy $M = (\mathbb N, +)$ và

$$
x \perp y \iff x \le y^2 \ \text{và}\ y \le x^2.
$$

Quan hệ này đối xứng theo định nghĩa, và additive: nếu $x_1 \le y_1^2$, $x_2 \le y_2^2$ thì $x_1+x_2 \le y_1^2+y_2^2 \le (y_1+y_2)^2$, tương tự chiều kia. Nhưng tính trực tiếp: $\{2\}^* = \{y : 2 \le y^2,\ y \le 4\} = \{2,3,4\}$, nên $\{2\}^{**} = \{x \le 4 : x^2 \ge 4\} = \{2,3,4\}$. Trong khi đó $\{2\}+\{2\} = \{4\}$, và $\{4\}^* = \{2,\dots,16\}$, nên $\{4\}^{**} = \{x \le 4 : x^2 \ge 16\} = \{4\}$. Vậy $\{2\}^{**} + \{2\}^{**} = \{4,\dots,8\} \not\subseteq \{4\}$: nucleus sai dù additivity đúng.

Đọc lại qua định lý đặc trưng: $D_{2,2} = \{m : (2+m) \perp 2\} = \{0,1,2\}$, và $\{0,1,2\}^* = \varnothing$ nên $\{0,1,2\}^{**} = M \ne \{0,1,2\}$, tức điều kiện (iii) bị vi phạm ngay tại $x=y=2$. Additivity là một điều kiện quá yếu để kiểm soát hành vi của lát cắt tịnh tiến $D_{x,y}$.

Additivity không cần. Quan hệ Fenchel không additive: với $n=1$, $(t,0) \perp (0,0)$ đúng (vì $0 \le 0$) và $(0,0) \perp (t,0)$ đúng, nhưng tổng đòi $(t,0) \perp (t,0)$, tức $t^2 \le 0$, sai với $t > 0$. Vậy Fenchel có nucleus nhưng không additive.

Lý do sâu xa: additivity là một phát biểu về polar bậc nhất, $A^* + B^* \subseteq (A+B)^*$, còn nucleus là phát biểu về bipolar. Phép lấy polar đảo chiều bao hàm thức, nên một bất đẳng thức đúng ở mức polar không tự động chuyển thành bất đẳng thức đúng ở mức bipolar. Phản ví dụ trên minh họa đúng cơ chế này: closure phồng $\{2\}$ lên hẳn $\{2,3,4\}$, nhưng không phồng $\{4\}$ tương ứng đủ để chứa tổng.

## Nhìn lại: điều gì đã học được

Điều kiện nucleus, dù phát biểu ở mức tập hợp, hoàn toàn được quyết định bởi hành vi của $\perp$ trên từng cặp phần tử, cụ thể là bởi việc các lát cắt tịnh tiến $D_{x,y}$ có phải tập polar hay không. Residuation là cách xây dựng tường minh và hiệu quả nhất để đảm bảo điều này, và nó bao trùm mọi ví dụ cổ điển: song tuyến tính trong Fenchel, tính nhóm trong phase semantics, tính bất biến tịnh tiến trong kernel toàn phương. Trong khi đó, additivity, dù là ứng viên trực giác nhất, lại không nắm bắt đúng bản chất của hiện tượng: nó là một điều kiện ở tầng sai.

Với định lý đặc trưng và bộ ví dụ này trong tay, ta có đủ nền tảng để đi lên tầng tập hợp và dựng đại số hoàn chỉnh, nội dung của file tiếp theo.
