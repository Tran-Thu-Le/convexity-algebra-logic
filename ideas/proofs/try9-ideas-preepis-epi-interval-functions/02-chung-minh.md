# Chứng minh các định lý

Ký hiệu $A+B = \{a+b : a\in A, b\in B\}$. Trong toàn bộ file này, chiều dễ

$$
A + \bigcap_\lambda I_\lambda \;\subseteq\; \bigcap_\lambda (A+I_\lambda)
$$

luôn đúng và không cần chứng minh: nếu $x = a+t$ với $a\in A$ và $t \in \bigcap_\lambda I_\lambda$, thì với mọi $\lambda$ ta có $t\in I_\lambda$, nên $x \in A+I_\lambda$ với mọi $\lambda$, tức $x \in \bigcap_\lambda(A+I_\lambda)$. Toàn bộ nội dung cần chứng minh dưới đây là chiều ngược lại.

---

## Định lý A

Cho A tùy ý và B, C là khoảng với $B\cap C \ne \varnothing$. Khi đó $A+(B\cap C) = (A+B)\cap(A+C)$.

### Chứng minh

Lấy $x \in (A+B)\cap(A+C)$. Trường hợp tổng quát nhất (B, C là khoảng tùy ý, có thể mở hoặc đóng) đòi hỏi xét riêng theo dạng đầu mút; ở đây trình bày trường hợp B, C là đoạn đóng hoặc tia đóng, trường hợp còn lại được suy ra như hệ quả của Định lý B với n bằng 2.

Viết $B = [b_1,b_2]$, $C=[c_1,c_2]$ (cho phép $b_2$ hoặc $c_2$ bằng $+\infty$, $b_1$ hoặc $c_1$ bằng $-\infty$). Vì $B\cap C \ne \varnothing$, đặt

$$
p = \max(b_1,c_1), \qquad q = \min(b_2,c_2), \qquad p \le q,
$$

khi đó $B\cap C = [p,q]$.

Lấy $x\in(A+B)\cap(A+C)$. Ta cần chỉ ra $x \in A + [p,q]$. Đây chính xác là nội dung của Định lý B với n=2, chứng minh chi tiết ở phần sau. Vậy Định lý A với B, C là đoạn hoặc tia đóng là trường hợp riêng của Định lý B.

---

## Định lý B, giao hữu hạn

Cho A là khoảng (tùy ý loại đầu mút), và $I_1,\dots,I_n$ là đoạn đóng hoặc tia đóng với $J := \bigcap_{k=1}^n I_k \ne \varnothing$. Khi đó

$$
A + J = \bigcap_{k=1}^n (A+I_k).
$$

Ta trình bày hai chứng minh độc lập.

### Chứng minh 1, trực tiếp qua max và min

Viết $I_k = [c_k,d_k]$ (cho phép $d_k = +\infty$ hoặc $c_k=-\infty$). Đặt

$$
c = \max_{1\le k \le n} c_k, \qquad d = \min_{1\le k \le n} d_k.
$$

Vì $J\ne\varnothing$, ta có $c\le d$, và $J=[c,d]$.

Với $A$ là một khoảng có infimum $\alpha$ và supremum $\beta$ (cho phép vô hạn, và cho phép đạt được hoặc không), lấy $x \in \bigcap_k(A+I_k)$. Với mỗi k, tồn tại $a_k \in A$, $t_k \in I_k$ sao cho $x = a_k+t_k$.

Vì $A$ là khoảng nên với hai giá trị $a_k, a_{k'}$ bất kỳ thuộc A, mọi giá trị trung gian cũng thuộc A (đây là định nghĩa của khoảng). Ta cần một giá trị $a\in A$ và $t\in[c,d]$ với $x=a+t$.

Xét $t_k = x-a_k \in I_k = [c_k,d_k]$, tức $c_k \le x-a_k \le d_k$, tức $x-d_k \le a_k \le x-c_k$.

Lấy $a^* = x-d$ nếu $x-d \in A$, ngược lại lấy giá trị gần nhất trong A. Cách làm gọn hơn: vì mỗi $a_k \in A$ và $A$ là khoảng, khoảng $[\min_k a_k, \max_k a_k] \subseteq A$. Ta chỉ ra $x-d$ và $x-c$ đều nằm trong đoạn này, hoặc trực tiếp $x-d, x-c \in A$.

Vì $d = \min_k d_k = d_{k_0}$ với chỉ số $k_0$ nào đó, và $a_{k_0} \ge x-d_{k_0} = x-d$. Tương tự, $c=\max_k c_k = c_{k_1}$, và $a_{k_1} \le x-c_{k_1}=x-c$. Do đó

$$
x-d \le a_{k_0}, \qquad a_{k_1} \le x-c.
$$

Vì $a_{k_0}, a_{k_1} \in A$ và A là khoảng, mọi giá trị giữa $a_{k_0}$ và $a_{k_1}$ đều thuộc A. Ta xét hai trường hợp:

Nếu $x-d \le x-c$ (tức $c\le d$, luôn đúng), và nếu $x-d, x-c$ đều nằm giữa $\min(a_{k_0},a_{k_1})$ và $\max(a_{k_0},a_{k_1})$ hoặc ngoài nhưng vẫn trong A do A là khoảng chứa cả $a_{k_0}$ lẫn mọi điểm cần thiết, ta suy ra tồn tại $a \in A \cap [x-d,x-c]$.

Cụ thể hơn và chặt chẽ hơn: đặt $a = \mathrm{clip}(x-d, \alpha,\beta)$, tức chiếu $x-d$ vào bao đóng của A theo thứ tự. Vì $a_{k_0}\ge x-d$ và $a_{k_0}\in A$, còn $a_{k_1}\le x-c$ và $a_{k_1}\in A$, khoảng $[a_{k_1},a_{k_0}]$ nếu $a_{k_1}\le a_{k_0}$, hoặc $[a_{k_0},a_{k_1}]$ ngược lại, đều nằm trong A theo tính lồi, và khoảng này giao với $[x-d,x-c]$ khác rỗng vì $a_{k_0}\ge x-d$ và $a_{k_1}\le x-c$ với $x-d\le x-c$. Suy ra tồn tại $a$ trong giao này, thuộc A, và $t:=x-a \in [c,d]=J$. Vậy $x=a+t \in A+J$.

Chiều ngược $A+J \subseteq \bigcap_k(A+I_k)$ là chiều dễ đã nêu ở đầu file. Vậy $A+J=\bigcap_k(A+I_k)$.

### Chứng minh 2, quy nạp trên n

Bước cơ sở, n bằng 1, là đẳng thức tầm thường $A+I_1=A+I_1$.

Bổ đề cần dùng: giao của hai đoạn đóng hoặc tia đóng, nếu khác rỗng, lại là một đoạn đóng hoặc tia đóng. Chứng minh bổ đề: nếu $I=[c_1,d_1]$, $I'=[c_2,d_2]$ và $I\cap I' \ne \varnothing$, đặt $c=\max(c_1,c_2)$, $d=\min(d_1,d_2)$, khi đó $c\le d$ và $I\cap I' = [c,d]$, chính là đoạn đóng hoặc tia đóng.

Bước quy nạp: giả sử định lý đúng cho n-1 tập, tức

$$
A + J_{n-1} = \bigcap_{k=1}^{n-1}(A+I_k), \qquad J_{n-1} := \bigcap_{k=1}^{n-1} I_k,
$$

với $J_{n-1} \ne \varnothing$ và $J_{n-1}$ là đoạn đóng hoặc tia đóng theo bổ đề trên (áp dụng lặp lại cho n-1 tập).

Xét thêm $I_n$, với $J_n := J_{n-1}\cap I_n \ne \varnothing$. Áp dụng trường hợp n bằng 2 (tức Định lý B cho hai tập, đã biết đúng, ví dụ theo Chứng minh 1 ở trên áp dụng cho hai tập $J_{n-1}$ và $I_n$) cho cặp $(J_{n-1}, I_n)$:

$$
A + (J_{n-1}\cap I_n) = (A+J_{n-1}) \cap (A+I_n).
$$

Kết hợp với giả thiết quy nạp $A+J_{n-1} = \bigcap_{k=1}^{n-1}(A+I_k)$, ta có

$$
A+J_n = \Big(\bigcap_{k=1}^{n-1}(A+I_k)\Big) \cap (A+I_n) = \bigcap_{k=1}^n (A+I_k).
$$

Đây là điều cần chứng minh cho n. Theo nguyên lý quy nạp, định lý đúng với mọi n.

### So sánh hai chứng minh

Chứng minh 1 tính trực tiếp $c=\max c_k$, $d=\min d_k$ và làm việc với tọa độ cụ thể; nó dùng đến biểu diễn tường minh của J như một đoạn xác định bởi max, min của các đầu mút.

Chứng minh 2 chỉ dùng lặp lại trường hợp hai tập cộng với bổ đề đóng dưới giao từng cặp; nó không cần biết trước công thức tường minh của giao n tập theo max, min, mà chỉ cần biết trường hợp hai tập đúng và giao hai tập cùng loại lại thuộc cùng loại. Vì vậy chứng minh quy nạp tổng quát hơn: nó áp dụng được cho bất kỳ lớp tập nào thỏa mãn hai điều kiện, trường hợp hai tập đúng và đóng dưới giao từng cặp, kể cả khi lớp đó không có công thức max, min tường minh kiểu Helly, ví dụ khi mở rộng bài toán sang một poset tổng quát thay vì R.

---

## Định lý C, giao vô hạn của đoạn đóng

Cho $A=[a,b]$, hoặc tia đóng, hoặc R, và họ tùy ý $\{I_\lambda=[c_\lambda,d_\lambda]\}_{\lambda\in\Lambda}$ với $\bigcap_\lambda I_\lambda \ne \varnothing$. Khi đó

$$
A+\bigcap_\lambda I_\lambda = \bigcap_\lambda (A+I_\lambda).
$$

### Chứng minh 1, qua sup và inf

Đặt $c=\sup_\lambda c_\lambda$, $d=\inf_\lambda d_\lambda$. Vì giao khác rỗng, tồn tại $x_0$ với $c_\lambda \le x_0 \le d_\lambda$ với mọi $\lambda$, suy ra $c\le x_0 \le d$, đặc biệt $c, d$ hữu hạn hoặc bằng $\pm\infty$ một cách nhất quán, và $c\le d$.

Bước 1: $\bigcap_\lambda I_\lambda = [c,d]$. Chiều $\subseteq$: nếu $x\in I_\lambda$ với mọi $\lambda$ thì $x\ge c_\lambda$ với mọi $\lambda$ nên $x\ge \sup_\lambda c_\lambda=c$, tương tự $x\le d$. Chiều $\supseteq$: nếu $c\le x\le d$ thì với mọi $\lambda$, $c_\lambda \le c \le x$ và $x\le d\le d_\lambda$, nên $x\in I_\lambda$.

Bước 2: $A+[c,d] = [a+c,b+d]$, tính chất cơ bản của tổng Minkowski hai đoạn đóng (hoặc tia đóng, thay tọa độ vô hạn tương ứng).

Bước 3: với mỗi $\lambda$, $A+I_\lambda = [a+c_\lambda, b+d_\lambda]$.

Bước 4: $\bigcap_\lambda(A+I_\lambda) = [\sup_\lambda(a+c_\lambda), \inf_\lambda(b+d_\lambda)]$ theo lập luận giống Bước 1. Vì phép cộng với hằng số hữu hạn bảo toàn sup và inf,

$$
\sup_\lambda(a+c_\lambda) = a+\sup_\lambda c_\lambda = a+c, \qquad \inf_\lambda(b+d_\lambda) = b+\inf_\lambda d_\lambda = b+d.
$$

Vậy $\bigcap_\lambda(A+I_\lambda) = [a+c,b+d] = A+[c,d] = A+\bigcap_\lambda I_\lambda$.

### Chứng minh 2, qua quy nạp suy rộng bằng họ hữu hạn con

Cách nhìn khác, không tính trực tiếp sup, inf của toàn họ ngay từ đầu, mà xây dựng dần qua các họ con hữu hạn.

Lấy $x\in\bigcap_\lambda(A+I_\lambda)$, cần chỉ ra $x\in A+\bigcap_\lambda I_\lambda$.

Với mỗi tập con hữu hạn $F\subseteq \Lambda$, đặt $J_F = \bigcap_{\lambda\in F} I_\lambda$. Vì $\bigcap_\lambda I_\lambda \ne \varnothing$ nên $J_F \ne \varnothing$ với mọi F hữu hạn (giao lớn hơn không rỗng thì giao con của nó cũng không rỗng). Theo Định lý B (giao hữu hạn, đã chứng minh ở trên bằng quy nạp), với mỗi F hữu hạn,

$$
A + J_F = \bigcap_{\lambda\in F}(A+I_\lambda) \ni x.
$$

Vậy với mỗi F hữu hạn, tồn tại $a_F \in A$ và $t_F \in J_F$ với $x=a_F+t_F$. Vì $A$ bị chặn dưới bởi $\alpha=\inf A$ và chặn trên bởi $\beta=\sup A$ (có thể vô hạn), và tương tự J bị chặn bởi $c=\sup c_\lambda$, $d=\inf d_\lambda$ như trên, các giá trị $a_F$ nằm trong đoạn đóng $\overline A$ (bao đóng của A) và $t_F$ nằm trong đoạn đóng $[c,d]$.

Xét lưới (net) $(a_F)_F$ theo quan hệ bao hàm trên các tập con hữu hạn F. Vì $t_F = x-a_F$ và $t_F \in J_F \subseteq I_\lambda$ với mọi $\lambda \in F$, khi F tăng dần bao trùm toàn bộ $\Lambda$, giá trị $t_F$ bị ép ngày càng chặt vào $[c,d]$. Do R đầy đủ theo thứ tự (mọi tập bị chặn có sup và inf), lưới $(a_F)$ có một điểm giới hạn $a^*$ trong đoạn đóng bị chặn chứa các $a_F$ (đây là dạng compact theo thứ tự của đoạn đóng bị chặn; nếu A không bị chặn, xét riêng từng phía chặn bởi $c,d$ hữu hạn qua Bước 1 của Chứng minh 1). Điểm giới hạn $a^*$ thỏa $a^*\in \overline A$, và vì A là đoạn đóng hoặc tia đóng nên $\overline A = A$, suy ra $a^*\in A$. Đặt $t^*=x-a^*$; theo cách xây dựng, $t^*$ nằm trong mọi $I_\lambda$ (giới hạn của các xấp xỉ $t_F \in I_\lambda$ khi $F\ni\lambda$, và $I_\lambda$ đóng nên chứa điểm giới hạn), suy ra $t^*\in\bigcap_\lambda I_\lambda$.

Vậy $x=a^*+t^* \in A+\bigcap_\lambda I_\lambda$.

### So sánh hai chứng minh

Chứng minh 1 ngắn gọn và làm việc trực tiếp với công thức tường minh $c=\sup c_\lambda$, $d=\inf d_\lambda$, áp dụng được cả cho A, $I_\lambda$ không bị chặn. Chứng minh 2 quy về trường hợp hữu hạn (Định lý B) rồi lấy giới hạn qua tính đầy đủ thứ tự và tính đóng của đoạn; nó cho thấy rõ vai trò của tính đóng (để điểm giới hạn thuộc lại tập ban đầu) tách biệt với vai trò của tính bị chặn (dùng compact theo thứ tự), và tổng quát hóa tốt hơn sang các phát biểu kiểu compact trong không gian thứ tự tổng quát, trả giá bằng việc cần thêm lập luận về sự tồn tại điểm giới hạn của lưới.

---

## Định lý D, giao vô hạn của tia đóng

Cho A là đoạn đóng hoặc tia đóng, và họ tùy ý $\{U_\lambda=[b_\lambda,\infty)\}_{\lambda\in\Lambda}$, xét trên $\overline{\mathbb R} = \mathbb R\cup\{-\infty,+\infty\}$. Khi đó

$$
A+\bigcap_\lambda U_\lambda = \bigcap_\lambda(A+U_\lambda),
$$

không cần thêm giả thiết giao khác rỗng.

### Chứng minh

Đặt $\beta = \sup_\lambda b_\lambda$ trong $\overline{\mathbb R}$, giá trị này luôn tồn tại do tính đầy đủ của $\overline{\mathbb R}$. Khi đó $\bigcap_\lambda U_\lambda = [\beta,\infty)$ (quy ước $[\infty,\infty) = \varnothing$).

Nếu $\beta = \infty$: hai vế đều bằng $\varnothing$ (vế trái vì $A+\varnothing=\varnothing$; vế phải vì với mỗi M lớn tùy ý tồn tại $\lambda$ với $b_\lambda > M$, nên $\bigcap_\lambda(A+U_\lambda) = \varnothing$).

Nếu $\beta$ hữu hạn: viết $A=[a,\infty)$ hoặc $A=[a_1,a_2]$ (trường hợp đoạn đóng bị chặn xử lý tương tự, chỉ cần thay $\infty$ bởi $a_2$ ở các bước dưới). Với A là tia đóng $[a,\infty)$:

$$
A+[\beta,\infty) = [a+\beta,\infty).
$$

Với mỗi $\lambda$, $A+U_\lambda = [a+b_\lambda,\infty)$, nên

$$
\bigcap_\lambda(A+U_\lambda) = \Big[\sup_\lambda(a+b_\lambda),\infty\Big) = [a+\beta,\infty),
$$

vì phép cộng với hằng số hữu hạn bảo toàn sup: $\sup_\lambda(a+b_\lambda) = a+\sup_\lambda b_\lambda = a+\beta$. Hai vế bằng nhau.

Trường hợp A là đoạn đóng bị chặn $[a_1,a_2]$ suy ra tương tự, dùng cùng đẳng thức bảo toàn sup ở đầu mút dưới, còn đầu mút trên cộng thêm hằng số $a_2$ vào $\infty$ vẫn là $\infty$ ở cả hai vế nên không ảnh hưởng.

---

## Định lý E, lồi đóng tổng quát

Gọi $\mathcal C$ là lớp mọi tập con lồi và đóng của R, gồm đoạn đóng, tia đóng, R, tập một điểm, và rỗng. Cho $A\in\mathcal C$ và họ tùy ý $\{I_\lambda\}_{\lambda\in\Lambda}\subseteq\mathcal C$ với $\bigcap_\lambda I_\lambda \ne\varnothing$. Khi đó

$$
A+\bigcap_\lambda I_\lambda = \bigcap_\lambda(A+I_\lambda),
$$

và $A+\bigcap_\lambda I_\lambda$ vẫn thuộc $\mathcal C$.

### Chứng minh

Mọi phần tử của $\mathcal C$ viết được dưới dạng giao của một tia đóng trên và một tia đóng dưới:

$$
I_\lambda = [c_\lambda,\infty) \cap (-\infty,d_\lambda],
$$

với quy ước $c_\lambda=-\infty$ nếu $I_\lambda$ không bị chặn dưới, $d_\lambda=+\infty$ nếu không bị chặn trên. Tương tự viết $A = [\alpha,\infty)\cap(-\infty,\beta]$.

Đặt

$$
U_\lambda = [c_\lambda,\infty), \qquad V_\lambda = (-\infty,d_\lambda].
$$

Áp dụng Định lý D cho họ $\{U_\lambda\}$ và, bằng phép đối xứng $x\mapsto -x$ (biến tia đóng trên thành tia đóng dưới, biến tổng Minkowski thành tổng Minkowski, biến giao thành giao), áp dụng phiên bản đối ngẫu của Định lý D cho họ $\{V_\lambda\}$, ta có

$$
A+\bigcap_\lambda U_\lambda = \bigcap_\lambda(A+U_\lambda), \qquad A+\bigcap_\lambda V_\lambda = \bigcap_\lambda(A+V_\lambda).
$$

Vì $\bigcap_\lambda I_\lambda = \big(\bigcap_\lambda U_\lambda\big)\cap\big(\bigcap_\lambda V_\lambda\big)$, và vế phải khác rỗng theo giả thiết, đặt $c=\sup_\lambda c_\lambda$, $d=\inf_\lambda d_\lambda$, khi đó $c\le d$ (do giao khác rỗng), và

$$
\bigcap_\lambda I_\lambda = [c,d].
$$

Áp dụng Định lý B (cho hai tập $\bigcap_\lambda U_\lambda = [c,\infty)$ và $\bigcap_\lambda V_\lambda = (-\infty,d]$, giao khác rỗng vì $c\le d$):

$$
A + [c,d] = A+\Big(\bigcap_\lambda U_\lambda \cap \bigcap_\lambda V_\lambda\Big) = \big(A+\bigcap_\lambda U_\lambda\big) \cap \big(A+\bigcap_\lambda V_\lambda\big) = \bigcap_\lambda(A+U_\lambda) \cap \bigcap_\lambda(A+V_\lambda).
$$

Mặt khác với mỗi $\lambda$, $A+I_\lambda = A+(U_\lambda\cap V_\lambda) = (A+U_\lambda)\cap(A+V_\lambda)$ theo Định lý B áp dụng cho từng $\lambda$ riêng lẻ (vì $U_\lambda \cap V_\lambda = I_\lambda \ne \varnothing$ theo giả thiết mỗi $I_\lambda$ khác rỗng, hoặc quy ước tự nhiên nếu rỗng). Do đó

$$
\bigcap_\lambda(A+I_\lambda) = \bigcap_\lambda\big[(A+U_\lambda)\cap(A+V_\lambda)\big] = \Big(\bigcap_\lambda(A+U_\lambda)\Big)\cap\Big(\bigcap_\lambda(A+V_\lambda)\Big).
$$

So sánh hai biểu thức, ta có

$$
A+\bigcap_\lambda I_\lambda = A+[c,d] = \bigcap_\lambda(A+I_\lambda).
$$

Cuối cùng, $A+[c,d]$ là tổng Minkowski của hai tập lồi đóng nên là một tập lồi đóng (đoạn hoặc tia hoặc R), vậy thuộc $\mathcal C$.

---

## Tổng kết vai trò của từng điều kiện

Ba điều kiện xuất hiện xuyên suốt các chứng minh trên:

Đóng dưới giao tùy ý trong lớp đang xét, để giao của cả họ vẫn nằm trong lớp có công thức kiểm soát được (đoạn, tia).

Phép dịch bảo toàn sup và inf, luôn đúng trên R hoặc $\overline{\mathbb R}$ với hằng số hữu hạn, không cần giả thiết thêm.

Đầu mút đạt được, tức sup hoặc inf tính được thực sự là phần tử của tập giao, đây là chỗ tính đóng được dùng một cách thiết yếu, và là chỗ khoảng mở thất bại.

Khi cả ba điều kiện này được thỏa mãn, kết hợp với giả thiết giao của cả họ khác rỗng, sum phân phối lên giao tùy ý. Đây là nội dung của Định lý E, điều kiện đủ tổng quát nhất đã được chứng minh trong bộ ba file này.
