# Từ nucleus đến polar semiring

## Điểm xuất phát của file này

File trước đã thiết lập xong nội dung khó nhất: một định lý đặc trưng cho biết khi nào phép cộng và quan hệ $\perp$ trên $M$ sinh ra nucleus, cùng một loạt ví dụ và một phản ví dụ để hiểu rõ ranh giới của điều kiện đó. Từ đây trở đi, mọi thứ là xây dựng hình thức thuần túy: cho $(M,+,\perp)$ đã biết thỏa nucleus, ta dựng từng bước một đại số hoàn chỉnh trên $\mathcal P(M)$, rồi thu hẹp về lớp các tập đóng để được một cấu trúc có đối ngẫu hoàn hảo. Phần thưởng của việc kiểm tra nucleus ở file trước sẽ được thu hoạch trọn vẹn ở đây.

## Bước một: dựng semiring trên $\mathcal P(M)$

Đặt $S := \mathcal P(M)$. Trên $S$ định nghĩa hai phép toán.

Phép join, đến từ cấu trúc tập hợp thuần túy, không liên quan gì đến $+$ hay $\perp$:

$$
A \vee B := A \cup B.
$$

Phép tensor, đến từ phép cộng trên $M$:

$$
A \otimes B := A + B = \{a+b : a \in A,\ b \in B\}.
$$

Hai đơn vị tương ứng là $0_S := \varnothing$ và $1_S := \{0\}$, với $0$ là phần tử trung hòa của $+$ trên $M$.

Bộ ba $(S, \vee, \otimes, 0_S, 1_S)$ là một idempotent commutative semiring. Idempotent vì $A \vee A = A$, commutative vì cả $\cup$ lẫn $+$ đều giao hoán, và luật phân phối $A \otimes (B \vee C) = (A \otimes B) \vee (A \otimes C)$ đúng ngay từ định nghĩa tập hợp, không cần chứng minh gì thêm: $a + (b \text{ hoặc } c)$ đơn giản là $(a+b)$ hoặc $(a+c)$.

Điều đáng nhấn mạnh ở bước này: chưa cần bất kỳ giả thiết nào về $\perp$ hay nucleus. Cấu trúc semiring trên $S$ là hoàn toàn miễn phí, chỉ cần $(M,+)$ là monoid giao hoán.

## Bước hai: đưa polarity vào

Quan hệ $\perp$ sinh phép lấy polar $A^* = \{y : \forall x \in A,\ x \perp y\}$, và vì $\perp$ đối xứng, $c(A) = A^{**}$ là closure operator, như đã thấy ở file trước. Gọi

$$
S_c := \{A \in S : A = A^{**}\}
$$

là lớp các tập đóng, hay tập regular.

Đến đây có một điểm cần dừng lại suy ngẫm. Ta đã có hai cấu trúc trên $S$: cấu trúc đại số $(\vee, \otimes)$ và cấu trúc topo-hóa $c$. Câu hỏi tự nhiên là chúng có tương thích với nhau hay không, tức closure operator có "tôn trọng" các phép toán đại số hay không. Với $\vee$, câu trả lời luôn là có, một cách hoàn toàn tự động.

Mệnh đề. Với mọi closure operator $c$ trên một join-semilattice bất kỳ, luôn có $c(c(A) \vee c(B)) = c(A \vee B)$.

Chứng minh chỉ dùng các tiên đề của closure operator. Vì $A \subseteq c(A)$ và $B \subseteq c(B)$, suy ra $A \vee B \subseteq c(A) \vee c(B)$, lấy closure hai vế: $c(A \vee B) \subseteq c(c(A) \vee c(B))$. Chiều ngược lại, vì $A \subseteq A \vee B$ nên $c(A) \subseteq c(A \vee B)$, tương tự $c(B) \subseteq c(A \vee B)$, nên $c(A) \vee c(B) \subseteq c(A \vee B)$, và vì vế phải đã đóng, lấy closure vế trái không vượt quá nó: $c(c(A) \vee c(B)) \subseteq c(A \vee B)$. $\blacksquare$

Vậy với join, không có gì phải lo. Toàn bộ nguy cơ mất tương thích dồn vào $\otimes$, và đó chính xác là lý do điều kiện nucleus

$$
c(A) \otimes c(B) \subseteq c(A \otimes B)
$$

trở thành chốt chặn duy nhất của cả câu chuyện. File trước đã chứng minh: điều kiện này tương đương với một điều kiện thuần túy ở mức phần tử của $M$. Từ đây, ta coi nucleus đã được thiết lập, và khai thác nó.

## Bước ba: nucleus là congruence

Định nghĩa quan hệ tương đương trên $S$:

$$
A \sim_c B \iff c(A) = c(B).
$$

Đây luôn là quan hệ tương đương, với bất kỳ closure operator nào, không cần nucleus. Điều nucleus mang lại là một tính chất mạnh hơn nhiều: tính tương thích với phép toán đại số, gọi là congruence.

Một quan hệ tương đương $\sim$ trên một đại số là congruence đối với một phép toán hai ngôi $\star$ nếu $A \sim A'$ và $B \sim B'$ kéo theo $A \star B \sim A' \star B'$. Đây là điều kiện đúng đắn để phép toán $\star$ "đi xuống được" lớp thương $S/{\sim}$, tức để định nghĩa $[A] \star [B] := [A \star B]$ không phụ thuộc vào đại diện được chọn.

Với join, congruence tự động đúng nhờ mệnh đề ở bước hai: nếu $c(A)=c(A')$ và $c(B)=c(B')$ thì $c(A \vee B) = c(c(A) \vee c(B)) = c(c(A') \vee c(B')) = c(A' \vee B')$.

Với tensor, ta cần chính xác nucleus.

Mệnh đề. Nucleus (điều kiện N) tương đương với việc $\sim_c$ là congruence đối với $\otimes$.

Chứng minh. Giả sử nucleus đúng và $A \sim_c A'$, $B \sim_c B'$, tức $c(A)=c(A')=:U$, $c(B)=c(B')=:V$. Từ $A \subseteq U$, $B \subseteq V$ suy ra $A \otimes B \subseteq U \otimes V$, lấy closure: $c(A \otimes B) \subseteq c(U \otimes V)$. Áp dụng nucleus cho $U, V$: $c(U) \otimes c(V) \subseteq c(U \otimes V)$, mà $c(U)=U$, $c(V)=V$ (vì $U,V$ đã đóng), nên $U \otimes V \subseteq c(U \otimes V)$, tức $c(U \otimes V) \supseteq U \otimes V$, luôn đúng, không cho thêm thông tin theo chiều này; nhưng mặt khác từ $U \otimes V \subseteq c(A \otimes B)$ (suy ra tương tự bằng cách đổi vai trò, dùng $A \subseteq U \subseteq c(A)$ nên $c(A) = c(U)$ và làm lại lập luận với $A \otimes B \subseteq U \otimes B \subseteq U \otimes V$), ta có hai bao hàm thức ngược nhau giữa $c(A \otimes B)$ và $c(U \otimes V)$, suy ra bằng nhau. Cùng lý luận cho $A', B'$ với cùng $U, V$ cho $c(A' \otimes B') = c(U \otimes V)$. Vậy $c(A \otimes B) = c(A' \otimes B')$, tức $A \otimes B \sim_c A' \otimes B'$.

Chiều ngược lại: nếu $\sim_c$ là congruence, áp dụng cho $A \sim_c c(A)$ (luôn đúng vì $c(c(A))=c(A)$) và $B \sim_c c(B)$, được $A \otimes B \sim_c c(A) \otimes c(B)$, tức $c(A \otimes B) = c(c(A) \otimes c(B)) \supseteq c(A) \otimes c(B)$, chính là nucleus. $\blacksquare$

Điểm mấu chốt cần mang theo: nucleus không phải một điều kiện kỹ thuật phụ, nó chính xác là điều kiện để phép nhân trên $S$ đi xuống được lớp thương theo bipolar. Không có nucleus, lớp thương $S/{\sim_c}$ chỉ là một tập hợp trần trụi; có nucleus, nó là một semiring.

## Bước bốn: semiring thương

Dưới nucleus, định nghĩa trên $S/{\sim_c}$:

$$
[A] \vee_q [B] := [A \vee B], \qquad [A] \otimes_q [B] := [A \otimes B].
$$

Theo mệnh đề vừa chứng minh, hai định nghĩa này không phụ thuộc đại diện, tức được xác định tốt. Đơn vị là $[0_S]$ và $[1_S]$. Cấu trúc $(S/{\sim_c}, \vee_q, \otimes_q)$ là một idempotent commutative semiring, thừa hưởng mọi tiên đề từ $S$ vì các phép toán trên thương được định nghĩa bằng cách nâng lên $S$ rồi chiếu xuống, và ánh xạ chiếu

$$
q : S \twoheadrightarrow S/{\sim_c}, \qquad q(A) = [A]
$$

là một toàn cấu semiring theo đúng định nghĩa: nó bảo toàn cả hai phép toán và cả hai đơn vị.

## Bước năm: đồng nhất lớp thương với lớp đóng

Đến đây có hai mô tả cho "cùng một thứ", và cần một cầu nối tường minh giữa chúng: một bên là lớp thương trừu tượng $S/{\sim_c}$, bên kia là lớp cụ thể $S_c$ gồm các tập đã đóng, sống ngay bên trong $S$.

Định nghĩa $\bar c : S/{\sim_c} \to S_c$ bởi $\bar c([A]) := c(A) = A^{**}$.

Ánh xạ này được xác định tốt: nếu $[A] = [A']$ tức $c(A)=c(A')$, thì rõ ràng $\bar c([A]) = \bar c([A'])$. Nó là đơn ánh: nếu $\bar c([A]) = \bar c([B])$ tức $c(A) = c(B)$, thì theo định nghĩa $A \sim_c B$, tức $[A]=[B]$. Nó là toàn ánh lên $S_c$: với $U \in S_c$ bất kỳ, $U = c(U)$, nên $U = \bar c([U])$.

Vậy $\bar c$ là song ánh. Để nó là đẳng cấu semiring, cần trang bị cho $S_c$ hai phép toán tương thích. Định nghĩa các phép toán regularized trên $S_c$:

$$
U \vee_c V := c(U \vee V) = (U \cup V)^{**}, \qquad U \otimes_c V := c(U \otimes V) = (U+V)^{**}.
$$

Sở dĩ cần "đóng lại" sau mỗi phép toán là vì $U \cup V$ hay $U + V$ của hai tập đã đóng chưa chắc đã đóng: hợp của hai tập lồi đóng chưa chắc lồi, tổng Minkowski của hai tập đóng chưa chắc đóng theo nghĩa bipolar. Đây là lý do phép quy nạp lại đóng là bước bắt buộc.

Với các định nghĩa này, kiểm tra trực tiếp từ định nghĩa của $\bar c$ và của $\vee_q, \otimes_q$: $\bar c([A] \vee_q [B]) = c(A \vee B) = c(c(A) \vee c(B)) = \bar c([A]) \vee_c \bar c([B])$, trong đó đẳng thức giữa vì đã chứng minh ở bước hai. Tương tự cho $\otimes$, dùng chính xác nucleus (bước ba). Vậy $\bar c$ là đẳng cấu semiring:

$$
S/{\sim_c} \ \overset{\cong}{\longrightarrow}\ S_c.
$$

Và vì $c = \bar c \circ q$, ta có thể nói gọn: $c$ tự nó là một toàn cấu semiring từ $S$ lên $S_c$, khi $S_c$ được trang bị các phép toán regularized.

## Bước sáu: polarity trở thành involution trên $S_c$

Trên toàn bộ $S$, phép lấy polar $* : S \to S$ nói chung không phải song ánh, vì có thể nhiều tập khác nhau cùng có một polar. Nhưng thu hẹp về $S_c$, tình huống hoàn toàn khác.

Với $U \in S_c$ bất kỳ, ta có $(U^*)^{**} = U^{***}$. Mà với mọi tập $A$, luôn có $A^{***} = A^*$ (đây là một đồng nhất thức thuần túy hình thức của mọi closure operator sinh từ polarity: áp dụng $A \subseteq A^{**}$ cho $A := A^*$ được $A^* \subseteq A^{***}$; áp dụng tính nghịch biến của $*$ cho $A \subseteq A^{**}$ được $A^{***} \subseteq A^*$; hai chiều cho đẳng thức). Vậy $(U^*)^{**} = U^*$, tức $U^* \in S_c$: polar của một tập đóng luôn đóng.

Hơn nữa với $U \in S_c$, tức $U = U^{**}$, ta có $(U^*)^* = U^{**} = U$. Vậy thu hẹp

$$
* : S_c \to S_c
$$

thỏa $U^{**} = U$ với mọi $U \in S_c$: đây chính xác là định nghĩa của một involution. Nó cũng nghịch biến: $U \subseteq V \Rightarrow V^* \subseteq U^*$, trực tiếp từ định nghĩa polar. Một song ánh nghịch biến bằng chính nghịch đảo của nó, đây là dạng đối ngẫu mạnh nhất có thể có.

## Bước bảy: De Morgan sinh hai phép toán mới

Đây là phần thưởng cuối cùng của toàn bộ cấu trúc. Có một involution nghịch biến trên $S_c$ nghĩa là ta có thể "chuyển ngữ" bất kỳ phép toán nào qua polarity để được một phép toán đối ngẫu. Cụ thể, định nghĩa

$$
U \wedge_c V := (U^* \vee_c V^*)^*, \qquad U \oplus_c V := (U^* \otimes_c V^*)^*.
$$

Ý tưởng đằng sau công thức này rất trực quan nếu nhìn theo ba bước: lấy polar để "bước sang phía bên kia", thực hiện phép toán quen thuộc ở phía bên kia, rồi lấy polar lần nữa để "quay lại". Vì $*$ là involution, bước quay lại luôn thực hiện được và không mất thông tin.

Các luật De Morgan bây giờ đúng theo đúng định nghĩa, không cần chứng minh gì thêm ngoài việc thay công thức và dùng $U^{**}=U$:

$$
(U \vee_c V)^* = U^* \wedge_c V^*, \qquad (U \wedge_c V)^* = U^* \vee_c V^*,
$$

$$
(U \otimes_c V)^* = U^* \oplus_c V^*, \qquad (U \oplus_c V)^* = U^* \otimes_c V^*.
$$

Ví dụ kiểm chứng luật đầu: $(U \vee_c V)^* = ((U \vee_c V)^*)$, và theo định nghĩa của $\wedge_c$, $U^* \wedge_c V^* = (U^{**} \vee_c V^{**})^* = (U \vee_c V)^*$, đúng ngay lập tức.

Như vậy, chỉ với hai phép toán nguyên thủy $\vee_c, \otimes_c$ và một involution $*$, ta sinh ra thêm hai phép toán $\wedge_c, \oplus_c$ hoàn toàn miễn phí. Đây là cơ chế giống hệt với cách logic tuyến tính sinh ra bốn kết nối $\otimes, \parr, \with, \oplus$ (hay $\wedge, \vee$ cổ điển) từ một cặp nguyên thủy và một phép phủ định tuyến tính.

## Bước tám: polar semiring hoàn chỉnh

Gọi cấu trúc thu được

$$
\mathbb S_c := (S_c,\ \vee_c,\ \wedge_c,\ \otimes_c,\ \oplus_c,\ {}^*,\ 0_c,\ 1_c)
$$

là một polar semiring, với $0_c := c(\varnothing)$, $1_c := c(\{0\})$. Các tiên đề đã được kiểm chứng qua các bước trên có thể liệt kê lại thành một danh sách gọn:

$(S_c, \vee_c, 0_c)$ là monoid giao hoán idempotent, thừa hưởng trực tiếp từ tính chất của $\cup$ và closure operator.

$(S_c, \otimes_c, 1_c)$ là monoid giao hoán, với tính kết hợp và trung hòa được kiểm tra qua phép quy nạp đóng, dùng nucleus khi cần đẩy closure qua nhiều lớp cộng liên tiếp.

Tensor phân phối trên join: $U \otimes_c (V \vee_c W) = (U \otimes_c V) \vee_c (U \otimes_c W)$, hệ quả của phân phối trên $S$ cộng với việc $q$, hay tương đương $c$, là toàn cấu.

Polarity là song ánh nghịch biến và involutive: $U \le V \Rightarrow V^* \le U^*$, và $U^{**}=U$.

Hai phép $\wedge_c, \oplus_c$ được định nghĩa qua De Morgan và tự động thỏa các luật đối ngẫu.

## Nhìn lại toàn bộ hành trình

Ba bước đầu của file này (dựng $S$, đưa polarity vào, chứng minh nucleus là congruence) thuần túy là hệ quả hình thức một khi định lý ở file trước đã được thiết lập. Ba bước tiếp theo (semiring thương, đồng nhất với $S_c$, involution) là nơi cấu trúc thực sự "kết tinh": một tập hợp trừu tượng các lớp tương đương hóa ra đẳng cấu với một tập hợp cụ thể sống ngay trong $S$, và trên tập cụ thể ấy, polarity không còn là một phép toán một chiều nữa mà trở thành một đối xứng thực sự. Hai bước cuối chỉ là thu hoạch: một khi có đối xứng, De Morgan cho không thêm hai phép toán.

Câu chuyện khép lại đúng như đã hứa ở file tổng quan: closure tạo ra lớp thương, nucleus đưa đại số xuống lớp thương, và involution nhân đôi số phép toán trên lớp thương ấy. Toàn bộ công sức thực sự nằm ở việc kiểm tra đúng một điều kiện, ở đúng một mức, mức phần tử của $M$; mọi thứ còn lại được suy ra bằng những lập luận hoàn toàn máy móc.
