# Ghi chú sửa lỗi: lớp đúng là tập lồi đóng chứa 0

## 1. Nhắc lại lỗi cũ

Trong mục 2b và mục 6.3 của file trừu tượng hóa, tôi đã định nghĩa, với một điểm cố định $x_0$ tùy ý,

$$
S_{x_0} = \{ I \in \mathcal C : x_0 \in I \},
$$

và gọi đây là một idempotent commutative semiring dưới giao tùy ý. Điều này sai: $S_{x_0}$ chỉ đóng dưới $\cap$, không đóng dưới $+$, nên không phải một semiring, chỉ là một $\cap$-semilattice nằm trong $\mathcal C$. Phản ví dụ đã nêu: $A=I=\{x_0\}\in S_{x_0}$, nhưng

$$
A+I = \{2x_0\},
$$

và $2x_0 \ne x_0$ khi $x_0\ne 0$, nên $A+I \notin S_{x_0}$.

## 2. Vì sao lỗi xảy ra, và vì sao chọn đúng $x_0=0$ thì sửa được

Nguyên nhân của lỗi nằm ở chỗ: tính chất "chứa $x_0$" không được bảo toàn qua phép cộng, trừ khi $x_0$ chính là phần tử trung hòa của phép cộng. Nếu $x_0=0$, thì $0+0=0$, tức phần tử trung hòa cộng với chính nó vẫn là phần tử trung hòa. Đây là lý do lớp đúng, không phải lớp gần đúng hay lớp minh họa, phải là

$$
S_0 = \{ I \in \mathcal C : 0 \in I \}.
$$

## 3. Định lý đúng: $(S_0, \cap, +)$ là một idempotent commutative semiring dưới giao tùy ý

### Đóng dưới $\cap$

Nếu $\{I_\lambda\}_{\lambda\in\Lambda} \subseteq S_0$ thì $0\in I_\lambda$ với mọi $\lambda$, nên $0 \in \bigcap_\lambda I_\lambda$, do đó $\bigcap_\lambda I_\lambda \ne \varnothing$ và, theo tính đóng dưới giao tùy ý của $\mathcal C$ (đã có sẵn), $\bigcap_\lambda I_\lambda \in \mathcal C$. Vì giao này chứa 0, nó thuộc $S_0$.

### Đóng dưới $+$

Đây là chỗ khác biệt thật sự so với $S_{x_0}$ với $x_0$ tùy ý. Cho $A, B \in S_0$, tức $A, B \in \mathcal C$ và $0\in A$, $0\in B$. Vì $\mathcal C$ đã đóng dưới $+$ (tổng Minkowski của hai tập lồi đóng trên R vẫn là một tập lồi đóng), $A+B \in \mathcal C$. Hơn nữa,

$$
0 = 0+0 \in A+B,
$$

vì $0\in A$ và $0\in B$. Vậy $A+B \in S_0$. Đây chính là chỗ lập luận cũ với $x_0$ tùy ý bị vỡ: với $x_0\ne 0$, $x_0+x_0=2x_0 \ne x_0$ nói chung, còn với $x_0=0$, đẳng thức $0+0=0$ luôn đúng, đơn giản vì đó là định nghĩa của phần tử trung hòa.

### Luật phân phối

Với $A\in S_0$ và họ tùy ý $\{I_\lambda\}\subseteq S_0$, ta có $A, I_\lambda \in \mathcal C$ và $\bigcap_\lambda I_\lambda \ne \varnothing$ (vì chứa 0, theo phần đóng dưới $\cap$ ở trên). Áp dụng thẳng Định lý E cho $\mathcal C$:

$$
A + \bigcap_\lambda I_\lambda = \bigcap_\lambda (A+I_\lambda).
$$

Cả hai vế đều thuộc $S_0$ theo phần đóng dưới $+$ và đóng dưới $\cap$ đã chứng minh, nên đẳng thức này diễn ra trọn vẹn bên trong $S_0$, không cần thoát ra ngoài rồi quay lại.

### Kết luận

$(S_0, \cap, +)$ là một idempotent commutative semiring thật sự, đóng kín dưới cả hai phép toán, dưới giao tùy ý, không phải chỉ có tính phân phối vay mượn từ $\mathcal C$ như $S_{x_0}$ trước đây.

## 4. Vì sao $x_0=0$ là lựa chọn đặc biệt, không phải một trường hợp riêng tùy ý

Bản chất của việc này: 0 không phải một điểm bất kỳ của R, mà là phần tử trung hòa của phép cộng đang xét. Một tính chất dạng "chứa một phần tử cố định $p$" được bảo toàn qua phép cộng Minkowski khi và chỉ khi $p+p=p$ trong nhóm cộng đó, và trong một nhóm, điều này chỉ đúng với $p=0$ (phần tử trung hòa là nghiệm duy nhất của phương trình $p+p=p$ trong một nhóm, vì có thể trừ p ở hai vế). Vì vậy không có một họ $S_p$ nào khác, với $p\ne 0$, có thể đóng dưới $+$ theo cùng cách; $S_0$ là trường hợp duy nhất trong họ này thật sự là một semiring con.

## 5. Tổng quát hóa lên K trừu tượng

Cho $(K,S)$ như trong file trừu tượng hóa, với $0_K$ là phần tử trung hòa của phép cộng trên K, và giả sử $(S,\cap,+)$ đã là một idempotent commutative semiring trên K (theo định nghĩa ở đó). Đặt

$$
S_0 = \{ L \in S : 0_K \in L \}.
$$

Cùng lập luận như trên áp dụng nguyên vẹn: $S_0$ đóng dưới $\cap$ (vì $0_K$ thuộc mọi thành phần nên thuộc giao), và đóng dưới $+$ (vì $S$ đã đóng dưới $+$, và $0_K+0_K=0_K \in A+B$ với mọi $A,B\in S_0$). Vậy $(S_0,\cap,+)$ luôn là một semiring con thật sự của $(S,\cap,+)$, với cùng phạm vi hữu hạn hay tùy ý như $S$. Đây là phát biểu đúng, thay cho phát biểu sai trước đây về $S_{x_0}$ với $x_0$ tùy ý.

## 6. Sửa lại hệ quả liên quan đến hàm nền f

Trong mục 6.3 của file trừu tượng hóa, tôi có dùng $S_{f(x)} = \{I\in\mathcal C : f(x)\in I\}$ tại mỗi fiber, với $f(x)$ đóng vai trò một điểm neo di động. Theo đúng phân tích ở trên, $S_{f(x)}$ không phải semiring trừ khi $f(x)=0$; nói chung nó chỉ là một họ con dùng để kiểm tra điều kiện giao khác rỗng của Định lý E, không phải một cấu trúc đóng kín.

Nếu muốn có một semiring con thật sự gắn với một hàm nền f di động, cách đúng là dùng phép tịnh tiến: đặt

$$
S_0^{(x)} = \{ I - f(x) : I \in \mathcal C,\ f(x) \in I \} = \{ J \in \mathcal C : 0 \in J \} = S_0,
$$

tức xét các tập đã dịch chuyển về gốc. Khi đó $S_0^{(x)}$ không phụ thuộc x, luôn bằng đúng $S_0$ ở phần 3, và là một semiring con thật sự. Việc gắn lại với f, tức xét $I = J+f(x)$ với $J\in S_0$, là một phép tịnh tiến bên ngoài cấu trúc semiring, không phải bản thân phép toán $\cap$ hay $+$ của semiring, nên không cần và không nên đưa "chứa f(x)" vào định nghĩa của lớp giá trị đang xét.

## 7. Tóm tắt sửa lỗi

| Nội dung | Phát biểu cũ, sai | Phát biểu đúng |
|---|---|---|
| Lớp con của $\mathcal C$ | $S_{x_0}=\{I : x_0\in I\}$, $x_0$ tùy ý, là semiring | $S_{x_0}$ chỉ đóng dưới $\cap$, không phải semiring, trừ khi $x_0=0$ |
| Semiring con thật sự | không có | $S_0=\{I\in\mathcal C : 0\in I\}$, đóng dưới cả $\cap$ và $+$ |
| Lý do | không nêu | 0 là phần tử trung hòa, nên $0+0=0$; đây là nghiệm duy nhất của $p+p=p$ trong một nhóm |
| Ứng dụng với hàm nền f | dùng trực tiếp $S_{f(x)}$ | dùng $S_0$ cố định, rồi tịnh tiến bằng $f(x)$ ở bên ngoài semiring |

Bài học chung: khi muốn một họ con "đi qua một điểm" trở thành một semiring con thật sự, điểm đó bắt buộc phải là phần tử trung hòa của phép cộng, không thể là một điểm tùy ý; nếu cần một điểm neo di động khác 0, phải tách nó ra thành một phép tịnh tiến áp dụng sau, bên ngoài cấu trúc đại số, chứ không được gộp vào định nghĩa của lớp giá trị.
