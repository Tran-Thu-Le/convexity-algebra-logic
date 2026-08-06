# Những kernel nào sinh nucleus

## Vị trí của file này trong dự án

File 4 dừng lại ở một câu hỏi mở: liệu residuation phần tử $x\backslash y$, khi nó tồn tại, có luôn quy về được một "cực bị xoắn" bởi một tác động $\sigma_x$ nào đó của $M$ lên chính nó hay không. File này chưa trả lời trọn vẹn câu hỏi đó, nhưng làm một việc cụ thể hơn và có lẽ hữu ích hơn ngay lúc này: khảo sát một họ kernel rộng, xuất hiện tự nhiên trong giải tích lồi, và xem với kernel nào thì phép xoắn $\tau(p,q)$ tồn tại tường minh, với kernel nào thì không, và tại sao ranh giới đó lại rơi đúng vào lớp hàm toàn phương một cách gần như tất yếu.

Kết quả cuối cùng khá bất ngờ nếu nhìn từ xa: hầu hết các đối tượng quen thuộc của giải tích lồi hiện đại, liên hợp Fenchel-Young của một hàm lồi tổng quát, phân kỳ Bregman của một hàm lồi tổng quát, đều không tự động sinh nucleus. Điều kiện đủ mà file 2 và file 4 đã dựng, tưởng như tổng quát, thực ra chỉ nắm bắt được một lớp hẹp: các kernel toàn phương và các kernel sai phân. Đây không phải một thất bại của lý thuyết, mà là một thông tin cấu trúc quan trọng, chỉ ra chính xác ranh giới của cơ chế "phủ định kép miễn phí".

## Thiết lập chung

Cho $X$ là một nhóm giao hoán, $M=X\times\mathbb R$ với phép cộng theo tọa độ, và một kernel bất kỳ $c:X\times X\to\mathbb R$, định nghĩa quan hệ

$$
(p,w)\perp_c(q,s)\iff c(p,q)\le w+s.
$$

Đây là dạng tổng quát nhất của mọi ví dụ đã gặp: Fenchel ứng với $c(p,q)=\langle p,q\rangle$, kernel toàn phương ứng với $c(p,q)=\tfrac12\|p-q\|^2$.

## Tiêu chuẩn cần và đủ, viết lại cho kernel

Theorem A ở file 2 nói nucleus đúng khi và chỉ khi mọi lát cắt tịnh tiến là tập polar. Với $\perp_c$, lát cắt đó có dạng cụ thể

$$
D_{p,q}:=\{(r,v):c(p+r,q)\le v\},
$$

sau khi đã hấp thụ các hằng số $w,s$ vào phương trọng số, việc này không thay đổi bản chất vì $w,s$ chỉ tịnh tiến giá trị ngưỡng. Vậy tiêu chuẩn cần và đủ là

$$
c \text{ sinh nucleus}\iff D_{p,q}\text{ bipolar-đóng với mọi }p,q\in X.
$$

Đây là một cách nói khác của cùng điều kiện, nhưng đặt đúng trọng tâm vào kernel: bipolar closure ở đây được lấy đối với chính họ hàm $r\mapsto c(r,y)-\alpha$, tức lớp hàm $c$-lồi sinh bởi $c$. Nói cách khác, điều kiện cần và đủ là: mọi lát tịnh tiến của kernel, $r\mapsto c(p+r,q)$, vẫn phải nằm trong đúng lớp $c$-lồi mà bản thân $c$ sinh ra. Đây là một điều kiện tự-tham-chiếu khá đẹp: kernel phải "đóng" dưới chính phép tịnh tiến của nó.

## Điều kiện đủ: cocycle-residuation

Điều kiện cần và đủ trên khó kiểm tra trực tiếp vì bản thân nó nhắc đến bipolar closure. Điều kiện đủ thực dụng hơn nhiều, và đây là công cụ chính của toàn bộ file này: giả sử tồn tại $\tau(p,q)\in X$ và $\delta(p,q)\in\mathbb R$ sao cho

$$
c(p+r,q)=c(r,\tau(p,q))+\delta(p,q)\qquad\forall r\in X. \tag{R}
$$

Khi điều này đúng, khai triển trực tiếp cho ngay residuation ở mức phần tử:

$$
(p+r,w+v)\perp_c(q,s)\iff c(p+r,q)\le w+v+s\iff c(r,\tau(p,q))\le v+\bigl(w+s-\delta(p,q)\bigr),
$$

tức

$$
(p,w)\backslash(q,s)=\bigl(\tau(p,q),\ w+s-\delta(p,q)\bigr).
$$

Sự tồn tại của residual này, theo đúng lập luận ở file 2, kéo theo nucleus. Công thức (R) đáng gọi là điều kiện cocycle, vì nó có đúng cấu trúc của một cocycle: giá trị kernel sau khi tịnh tiến biến thứ nhất bởi $p$ bằng giá trị kernel gốc tại một điểm bị "xoắn" $\tau(p,q)$, cộng thêm một số hạng hiệu chỉnh $\delta(p,q)$ không phụ thuộc $r$. Toàn bộ phần còn lại của file này là đi tìm $\tau,\delta$ cho từng họ kernel cụ thể, và xem khi nào việc tìm kiếm đó thất bại.

## Kernel sai phân: trường hợp luôn thắng

Nếu $c(p,q)=\psi(q-p)$ với $\psi$ bất kỳ trên nhóm $X$, tính trực tiếp

$$
c(p+r,q)=\psi(q-p-r)=\psi\bigl((q-p)-r\bigr)=c(r,q-p).
$$

Vậy (R) đúng với $\tau(p,q)=q-p$ và $\delta(p,q)=0$, không cần bất kỳ giả thiết trơn hay lồi nào lên $\psi$. Đây là lớp kernel dễ nhất, đã gặp ở file 2, và bây giờ thấy rõ tại sao dễ: cấu trúc sai phân khiến phép tịnh tiến biến thứ nhất tự động chuyển hóa thành phép tịnh tiến trên chính $\psi$, không sinh ra số hạng hiệu chỉnh nào cả. Nếu muốn $\perp_c$ đối xứng, cần thêm $\psi(z)=\psi(-z)$, và kernel toàn phương $c(p,q)=\tfrac12\|p-q\|^2$ nằm gọn trong lớp này vì $\psi(z)=\tfrac12\|z\|^2$ thỏa điều kiện chẵn một cách tự nhiên.

## Fenchel-Young coupling: cái giá của tính bất đối xứng

Bây giờ đến lớp thú vị hơn. Với $F$ lồi trên $X=\mathbb R^n$ và $F^*$ là liên hợp Fenchel của nó, đặt

$$
c_F(x,y):=F(x)+F^*(y)-\langle x,y\rangle.
$$

Đáng chú ý ngay: đây không phải kernel sai phân, vì $c_F$ trộn cả $F$ lẫn $F^*$ theo hai biến khác nhau, không có lý do gì để nó chỉ phụ thuộc vào $y-x$.

Khai triển vế trái của (R):

$$
c_F(p+r,q)=F(p+r)+F^*(q)-\langle p+r,q\rangle.
$$

Muốn viết lại thành $F(r)+F^*(\tau)-\langle r,\tau\rangle+\delta$ với $\tau,\delta$ không phụ thuộc $r$, bước bắt buộc là tách $F(p+r)$ thành một phần phụ thuộc $r$ giống hệt $F(r)$ và một phần còn lại không phụ thuộc $r$. Điều này đòi hỏi chính xác

$$
F(p+r)-F(r)=\langle a_p,r\rangle+b_p\qquad\forall r, \tag{F}
$$

tức hiệu số gia của $F$ khi tịnh tiến bởi $p$ phải là một hàm affine theo $r$. Khi (F) đúng,

$$
c_F(p+r,q)=F(r)+F^*(q)-\langle r,q-a_p\rangle+b_p-\langle p,q\rangle,
$$

và đặt $\tau=q-a_p$, $\delta(p,q)=F^*(q)-F^*(q-a_p)+b_p-\langle p,q\rangle$, ta được đúng dạng cần thiết, miễn là $F^*(q)-\langle r,q-a_p\rangle$ khớp với $F^*(\tau)-\langle r,\tau\rangle$ cộng phần dư không phụ thuộc $r$, điều tự động đúng theo cách đặt $\tau$.

Vậy (F) là điều kiện đủ. Nhưng (F) là một điều kiện rất mạnh, và đây là chỗ đáng dừng lại suy ngẫm: nó nói rằng độ tăng của $F$ khi dịch chuyển theo bất kỳ hướng cố định $p$ nào cũng phải là affine theo điểm xuất phát $r$. Với $F$ khả vi hai lần, lấy Hessian hai vế của (F):

$$
\nabla^2F(p+r)-\nabla^2F(r)=0\qquad\forall p,r,
$$

tức Hessian của $F$ không đổi khi tịnh tiến, với mọi độ tịnh tiến $p$. Điều này chỉ có thể xảy ra nếu Hessian là hằng số trên toàn không gian, tức

$$
F(x)=\tfrac12\langle Qx,x\rangle+\langle b,x\rangle+\gamma,\qquad Q\succeq 0.
$$

Kết luận: Fenchel-Young coupling của một hàm toàn phương sinh nucleus, thông qua đúng cơ chế (R). Với $F$ lồi tổng quát, không toàn phương, điều kiện (F) thất bại, và (R) không thể dùng được; nucleus có thể vẫn đúng nhờ tiêu chuẩn yếu hơn (NC), nhưng không có gì đảm bảo, và không suy ra được chỉ từ tính lồi của $F$.

Điều đáng ghi nhớ ở đây là hình dạng của lập luận: một điều kiện đại số nhìn qua tưởng nhẹ nhàng, "hiệu số gia affine", khi đặt cạnh giả thiết trơn $C^2$, ép ngay ra tính toàn phương. Đây không phải trùng hợp, sẽ thấy lại đúng cơ chế này ở hai mục tiếp theo.

## Kernel đối xứng $F(x)+F(y)-\langle x,y\rangle$: cùng một cái giá

Xét biến thể đối xứng

$$
\widetilde c_F(x,y):=F(x)+F(y)-\langle x,y\rangle.
$$

Lập luận lặp lại y hệt: khai triển $\widetilde c_F(p+r,q)=F(p+r)+F(q)-\langle p+r,q\rangle$, và để tách được thành dạng residuated, lại cần chính xác điều kiện (F): $F(p+r)-F(r)$ affine theo $r$. Dưới giả thiết trơn, lại suy ra $F$ toàn phương cộng affine.

Trường hợp đặc biệt đáng chú ý: nếu $F(x)=\tfrac12\|x\|^2$, thì

$$
F(x)+F(y)-\langle x,y\rangle=\tfrac12\|x-y\|^2,
$$

và kernel trở về đúng dạng sai phân đã biết là luôn thắng. Nhưng nếu $F(x)=\tfrac12\langle Qx,x\rangle$ với $Q$ toàn phương tổng quát, thì $F(x)+F(y)-\langle x,y\rangle$ không nhất thiết chỉ phụ thuộc vào $x-y$ nữa, trừ khi ghép cặp được chọn tương thích với $Q$ ngay từ đầu, ví dụ dùng trực tiếp

$$
c_Q(x,y):=\tfrac12\langle Q(x-y),x-y\rangle,
$$

mà đây lại chính là một kernel sai phân, nên tự động sinh nucleus theo mục trước. Bài học rút ra: không phải mọi cách viết một biểu thức toàn phương dưới dạng $F(x)+F(y)-\langle x,y\rangle$ đều tốt như nhau; chỉ khi biểu thức đó thực chất quy được về một hàm của $x-y$ thì cơ chế đơn giản nhất mới áp dụng trực tiếp.

## Bregman divergence: cùng rào cản, thêm một lớp phức tạp

Cho $F$ khả vi lồi, phân kỳ Bregman là

$$
D_F(x,y):=F(x)-F(y)-\langle\nabla F(y),x-y\rangle.
$$

Viết lại theo biến $x$:

$$
D_F(x,y)=F(x)-\langle\nabla F(y),x\rangle+\bigl(\langle\nabla F(y),y\rangle-F(y)\bigr),
$$

và khai triển tại $x=p+r$:

$$
D_F(p+r,q)=F(p+r)-F(q)-\langle\nabla F(q),p+r-q\rangle.
$$

Muốn có dạng residuated $D_F(p+r,q)=D_F(r,\tau(p,q))+\delta(p,q)$, lại cần $F(p+r)-F(r)$ affine theo $r$, cộng thêm một điều kiện thứ hai: cần tìm được $\tau$ sao cho $\nabla F(\tau)=\nabla F(q)-a_p$, với $a_p$ là hệ số affine xuất hiện trong (F). Nếu $F$ là hàm Legendre, tức $\nabla F$ khả nghịch, có thể đặt hình thức

$$
\tau(p,q)=(\nabla F)^{-1}\bigl(\nabla F(q)-a_p\bigr),
$$

nhưng điều kiện tiên quyết vẫn là $a_p$ tồn tại độc lập với $r$, và dưới giả thiết $F\in C^2$, đây lại chính xác là điều kiện Hessian hằng, tức $F$ toàn phương.

Vậy Bregman divergence của một hàm toàn phương sinh nucleus; với $F$ lồi hoặc Legendre tổng quát, không có gì đảm bảo, và nói riêng phân kỳ Bregman tổng quát không tự động tương thích với spatial sum thông thường trên $X\times\mathbb R$.

## Một bổ đề ẩn đằng sau cả ba ví dụ

Nhìn lại ba mục vừa qua, một quy luật chung hiện rõ: mọi kernel không thuộc dạng sai phân thuần túy, khi ghép với điều kiện trơn $C^2$, đều đưa điều kiện đủ (R) về đúng một mệnh đề duy nhất.

Bổ đề (tính cứng của số gia affine). Cho $F\in C^2(\mathbb R^n)$. Nếu với mọi $p\in\mathbb R^n$, hàm $r\mapsto F(p+r)-F(r)$ là affine theo $r$, thì $F$ là một hàm toàn phương cộng affine.

Chứng minh chỉ cần lấy đạo hàm bậc hai của giả thiết theo $r$: $\nabla^2F(p+r)=\nabla^2F(r)$ với mọi $p,r$, tức $\nabla^2F$ là hàm hằng trên $\mathbb R^n$, và tích phân lại hai lần cho đúng dạng toàn phương cộng affine.

Bổ đề này là lý do thực sự đằng sau mọi kết luận "quadratic" ở các mục trên: nó không đặc thù cho Fenchel-Young hay Bregman, mà là một sự kiện thuần túy giải tích về chính điều kiện (F), và điều kiện (F) lại là thứ mọi kernel không-sai-phân đều cần để cocycle-residuation (R) khả thi.

## Phân biệt quan trọng: giữ nguyên phép cộng hay biến dạng nó

Toàn bộ thất bại ở các mục Fenchel-Young và Bregman tổng quát đều xảy ra trong một bối cảnh cụ thể: phép cộng trên $M$ được cố định là $(p,w)+(r,v)=(p+r,w+v)$, tức spatial sum Euclid thông thường, và ta hỏi kernel nào tương thích với phép cộng cố định đó.

Nhưng nhìn lại câu hỏi mở ở cuối file 4, có một hướng khác: thay vì cố định phép cộng và tìm kernel tương thích, có thể cố định kernel $c$ (đến từ $F$ cụ thể, không nhất thiết toàn phương) và đi tìm một phép composition khác, biến dạng theo hình học của $F$, chẳng hạn qua một phép đổi tọa độ gradient $x\mapsto\nabla F(x)$ hoặc một gauge transform thích hợp, sao cho dưới phép composition mới này, cocycle-residuation (R) lại khả thi.

Đây chính là phiên bản cụ thể của "cực xoắn" $\sigma_x$ được phỏng đoán ở file 4, nhưng bây giờ nhìn từ góc độ ngược lại: thay vì xoắn quan hệ $\perp$ giữ nguyên phép cộng, ta xoắn chính phép cộng để giữ nguyên kernel. Hai cách nhìn này có lẽ tương đương về mặt hình thức, nhưng cách nhìn thứ hai gợi ý một chương trình làm việc rõ ràng hơn: với mỗi $F$ lồi cho trước, hình học Riemann hoặc affine cảm sinh bởi Hessian của $F$ (khi $F$ đủ trơn và lồi chặt) có thể chính là nơi định nghĩa đúng phép cộng biến dạng, và nucleus khi đó không còn là câu hỏi về $F$ có toàn phương hay không, mà là câu hỏi hình học vi phân về cấu trúc affine phẳng cảm sinh bởi $F$. Đây là điểm nối tự nhiên với hình học thông tin, nơi Hessian của một hàm lồi định nghĩa một cấu trúc affine kép, và với $c$-lồi trong vận tải tối ưu, nơi kernel $c$ tổng quát thay thế vai trò của tích vô hướng ngay từ đầu chứ không cố định phép cộng Euclid.

## Bảng tổng kết

$$
\begin{array}{l|l}
\text{Kernel} & \text{Nucleus đối với spatial sum thường}\\
\hline
c(p,q)=\psi(q-p),\ \psi\text{ tùy ý (chẵn nếu cần đối xứng)} & \text{Có, luôn luôn}\\
\tfrac12\|p-q\|^2 & \text{Có (trường hợp riêng của dòng trên)}\\
F(x)+F^*(y)-\langle x,y\rangle & \text{Có nếu }F\text{ toàn phương; không tự động nếu tổng quát}\\
F(x)+F(y)-\langle x,y\rangle & \text{Tương tự; cần }F\text{ toàn phương hoặc quy về dạng sai phân}\\
D_F(x,y)\ \text{(Bregman)} & \text{Có nếu }F\text{ toàn phương; không tự động nếu tổng quát}
\end{array}
$$

Tiêu chuẩn cần và đủ, luôn đúng bất kể kernel: $D_{p,q}=\{(r,v):c(p+r,q)\le v\}$ phải bipolar-đóng với mọi $p,q$. Tiêu chuẩn đủ, dễ kiểm tra và giải thích được mọi dòng trong bảng trên: tồn tại $\tau,\delta$ sao cho $c(p+r,q)=c(r,\tau(p,q))+\delta(p,q)$ với mọi $r$.

## Nhìn lại

Điều rút ra được không chỉ là một danh sách ví dụ, mà là một ranh giới rõ rệt giữa hai chế độ. Khi kernel có cấu trúc sai phân, tương thích tự nhiên với phép cộng đã cho, nucleus đến gần như miễn phí, đúng tinh thần mức hai của file 4. Khi kernel đến từ một hàm lồi tổng quát qua liên hợp Fenchel hoặc phân kỳ Bregman, cơ chế cocycle-residuation chỉ hoạt động đúng lúc hàm đó suy biến về toàn phương, và ranh giới ấy được xác định chính xác bởi một bổ đề giải tích đơn giản về tính cứng của số gia affine. Với phần còn lại, tức đại đa số các hàm lồi thực sự phi tuyến gặp trong tối ưu hóa, câu hỏi nucleus đối với spatial sum thông thường có câu trả lời phủ định trong trường hợp tổng quát, và hướng đi hứa hẹn hơn là không giữ cố định phép cộng, mà để nó biến dạng theo chính hình học của hàm lồi đang xét.
