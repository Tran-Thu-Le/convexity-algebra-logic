# Residual tự sinh, nhưng tương thích với $\perp$ là chuyện khác

## Đặt lại câu hỏi cho chính xác

Ở cuối file 2, có một câu hỏi bị gộp làm một cách vô tình: "$(M,+,\perp)$ có sinh ra residuation kiểu Girard algebra hay không". Câu hỏi này thực ra che giấu hai câu hỏi khác nhau, và nhầm lẫn giữa chúng là chỗ dễ trượt nhất.

Câu hỏi thứ nhất: phép tensor $\otimes$ trên $S=\mathcal P(M)$ có residual hay không. Câu trả lời là có, luôn luôn, không cần biết gì về $\perp$ cả. Đây là một sự kiện thuần túy về $(M,+)$.

Câu hỏi thứ hai: residual đó có "khớp" với polarity $*$ sinh từ $\perp$ hay không, theo nghĩa cái đóng vai trò phủ định trong cả hai câu chuyện là một. Câu trả lời nói chung là không, và khi nó có khớp thì đó là một sự kiện đặc biệt, không phải quy luật chung.

Fenchel là ví dụ cho thấy rõ nhất: residual của $\otimes$ tồn tại (như mọi $(M,+)$ khác), nhưng nó không khớp với polarity Fenchel theo nghĩa trên. Vậy nucleus của Fenchel, khi nó đúng, đúng vì một lý do khác, tinh vi hơn, chứ không phải vì "có residual nên tự động ổn". File này dành để tách bạch hai chuyện đó ra, và định vị chính xác Theorem A của file 2 nằm ở đâu trong bức tranh.

## Residual nội tại của $\otimes$: luôn có, không điều kiện

Chỉ cần $(M,+)$ là monoid giao hoán, semiring $S=\mathcal P(M)$ đã có một tính chất mạnh hơn phân phối hữu hạn: tensor phân phối trên hợp tùy ý, kể cả hợp vô hạn,

$$
A\otimes\Bigl(\bigcup_{i\in I}B_i\Bigr)=\bigcup_{i\in I}(A\otimes B_i),
$$

vì $a+(\text{phần tử của }B_i\text{ nào đó})$ đơn giản duyệt qua tất cả các $i$. Một cấu trúc như vậy, dàn đầy đủ với phép nhân phân phối trên join tùy ý, gọi là một quantale. Và mọi quantale đều có một hệ quả đại số miễn phí: định lý hàm tử liên hợp (adjoint functor theorem, hoặc trực tiếp hơn là định lý điểm cố định Knaster-Tarski) cho phép định nghĩa

$$
A\to B:=\bigcup\{\,C\subseteq M:\ A\otimes C\subseteq B\,\}.
$$

Đây là tập lớn nhất theo quan hệ bao hàm sao cho $A\otimes(A\to B)\subseteq B$, và nó thỏa Galois connection

$$
A\otimes C\subseteq B\iff C\subseteq A\to B.
$$

Không có gì phải chứng minh thêm ở đây ngoài việc kiểm tra $A\to B$ như định nghĩa trên thực sự đạt supremum, điều luôn đúng nhờ phân phối trên hợp tùy ý. Nói cách khác: residual $\to$ tồn tại với mọi $(M,+)$ là monoid giao hoán, không cần bất kỳ giả thiết nào về $\perp$. Đây chính xác là phép $x\to C$ đã dùng ở file 2, chỉ khác là ở đây tổng quát hóa từ $x$ đơn lẻ lên $A$ bất kỳ.

Vậy nếu câu hỏi dừng ở "có residuation hay không", câu trả lời là có, và nó chẳng liên quan gì đến việc bạn chọn $\perp$ như thế nào. Đây là điều khiến câu hỏi ban đầu dễ gây hiểu lầm: sự tồn tại của residual là một sự kiện tầm thường, trong khi điều thực sự cần bàn nằm ở chỗ khác.

## Hai phép phủ định khác nhau đang sống trên cùng một $S$

Bây giờ mới đến chỗ mấu chốt. Trên $S$, có hai cách hoàn toàn độc lập để tạo ra một phép toán một ngôi đóng vai trò "phủ định".

Cách thứ nhất, nội tại, đến từ chính $\otimes$: cố định một phần tử $D\in S$ bất kỳ, đặt $A^{\bot_D}:=A\to D$. Đây là phủ định theo nghĩa quantale, hoàn toàn xây từ residual, không cần $\perp$.

Cách thứ hai, ngoại lai, đến từ $\perp$: $A^*=\{y:\forall x\in A,\ x\perp y\}$. Đây được cho như dữ liệu độc lập, không xây từ $\otimes$ chút nào; nó chỉ dùng quan hệ $\perp$ trên $M$, một dữ liệu hoàn toàn tách rời khỏi cấu trúc cộng.

Hai phép toán này a priori không có liên hệ gì với nhau. Chúng chỉ tình cờ cùng sống trên $S$. Câu hỏi thật sự đáng hỏi, và đây mới là câu hỏi đúng chỗ nhầm lẫn ban đầu, là: khi nào $*$ trùng với $\bot_D$ của một $D$ nào đó?

## Trường hợp trùng khớp: pole và Girard quantale miễn phí

Giả sử tồn tại một tập $D\subseteq M$ cố định sao cho

$$
x\perp y\iff x+y\in D.
$$

Khi đó với mọi $A\subseteq M$,

$$
A^*=\{y:\forall x\in A,\ x+y\in D\}=\{y:A\otimes\{y\}\subseteq D\}=A\to D=A^{\bot_D}.
$$

Vậy $*$ và $\bot_D$ là một, và ta rơi đúng vào trường hợp phase semantics đã nói ở file 2. Ở đây có một định lý chuẩn của lý thuyết quantale, đáng phát biểu tường minh vì nó giải thích tại sao trường hợp này "miễn phí":

Định lý. Trong bất kỳ quantale giao hoán nào, với bất kỳ $D$ cố định nào, đặt $j(A):=(A\to D)\to D$. Khi đó $j$ luôn là một nucleus đối với $\otimes$.

Ý tưởng chứng minh chỉ dùng tính chất phổ dụng của residual, không dùng gì đặc thù về $D$: từ $A\otimes(A\to D)\subseteq D$ (định nghĩa residual) và tính phản xạ $B\subseteq (B\to D)\to D$ áp dụng hai lần, cộng với tính nghịch biến của $(-)\to D$, suy ra $j(A)\otimes j(B)\subseteq j(A\otimes B)$ bằng một dây chuyền bất đẳng thức thuần túy hình thức, không cần biết thêm gì về $A,B,D$.

Điều quan trọng cần rút ra: khi $\perp$ có dạng cực cộng tính như trên, nucleus không phải điều cần chứng minh, nó là một định lý miễn phí của lý thuyết quantale tổng quát, áp dụng cho bất kỳ $D$ nào, không riêng gì $\perp$ bạn chọn. Đây là lý do phase semantics của logic tuyến tính không bao giờ cần một "Theorem A" riêng: nó tự động đúng ngay khi viết ra định nghĩa.

## Fenchel không rơi vào trường hợp miễn phí

Câu hỏi bây giờ là: liệu có tồn tại một $D\subseteq \mathbb R^n\times\mathbb R$ cố định sao cho quan hệ Fenchel $(p,w)\perp(q,s)\iff\langle p,q\rangle\le w+s$ viết được dưới dạng $(p,w)+(q,s)\in D$?

Nếu có, thì điều kiện $\langle p,q\rangle\le w+s$ phải chỉ phụ thuộc vào tổng $(p+q,\ w+s)$, không phụ thuộc vào cách tổng đó được tách thành $(p,w)$ và $(q,s)$. Đây là điều sai, và sai một cách rõ ràng khi $n\ge 1$.

Lấy $n=1$. Xét hai cách tách cùng một tổng: $(p,w)=(2,0)$, $(q,s)=(0,0)$, cho $\langle p,q\rangle=0\le 0=w+s$, đúng. Và $(p,w)=(1,0)$, $(q,s)=(1,0)$, cùng tổng $(p+q,w+s)=(2,0)$ như trước, nhưng $\langle p,q\rangle=1>0=w+s$, sai. Vậy cùng một giá trị tổng $(2,0)$ cho hai kết luận trái ngược nhau tùy cách tách, nên không thể có $D$ nào để $\langle p,q\rangle\le w+s\iff(p+q,w+s)\in D$.

Kết luận: quan hệ Fenchel không phải quan hệ cực theo nghĩa $x\perp y\iff x+y\in D$. Định lý miễn phí ở mục trước không áp dụng được. Nếu nucleus vẫn đúng cho Fenchel, như định lý gốc đã chứng minh, thì nó đúng vì một cơ chế khác, không đến từ việc có một $D$ cố định làm cực toàn cục.

## Vậy Theorem A thực sự đang chứng minh điều gì

Bây giờ có thể phát biểu chính xác vị trí của Theorem A trong bức tranh residual-nội-tại đối lập polarity-ngoại-lai. Viết lại điều kiện (ii) của Theorem A bằng đúng ngôn ngữ residual vừa dựng ở đầu file này: với mọi $x\in M$ và mọi $C$ đóng,

$$
x\to C\ \text{đóng}.
$$

Đây chính xác là điều kiện chuẩn cho một closure operator là nucleus trên một quantale, phát biểu bằng residual nội tại của chính $\otimes$: nucleus đúng khi và chỉ khi residual nội tại $x\to(-)$ đưa tập đóng vào tập đóng. Điều Theorem A làm là chỉ ra: dù $*$ (polarity từ $\perp$) và $\to$ (residual từ $\otimes$) là hai phép toán độc lập, không có lý do tiên nghiệm để tương thích, nhưng chúng tương thích đúng khi lát cắt $D_{x,y}=\{m:(x+m)\perp y\}=x\to\{y\}^*$ là một tập polar.

Nói cách khác, Theorem A không chứng minh $*=\to(-,D)$ toàn cục như trường hợp pole. Nó chứng minh một điều yếu hơn nhưng đủ dùng: residual nội tại $x\to(-)$, áp dụng riêng lên các tập polar đơn $\{y\}^*$, luôn cho lại một tập polar khác. Đây là một điều kiện cục bộ, kiểm tra được từng cặp $x,y$, chứ không đòi một cực toàn cục duy nhất chi phối toàn bộ $M$.

Residuation dựng ở file 2 qua công thức $(x+m)\perp y\iff m\perp(x\backslash y)$ chính là cách hiện thực hóa cụ thể điều kiện cục bộ này: nó nói rằng với $D_{x,y}=\{y'\}^*$ trong đó $y':=x\backslash y$, tức là bản thân lát cắt $D_{x,y}$ được biểu diễn như polar của đúng một điểm, chứ không phải polar của một tập $D$ cố định không đổi khi $x$ thay đổi. Sự khác biệt tinh tế nằm ở đây: pole cố định cho một $D$ duy nhất cho mọi $x$; residuation kiểu Fenchel cho một điểm $x\backslash y$ phụ thuộc vào cả $x$ lẫn $y$, thay đổi theo từng cặp.

## Sơ đồ phân loại ba mức

Có thể tổng kết toàn bộ thảo luận thành ba mức độ, từ yếu nhất đến mạnh nhất, và định vị các ví dụ đã gặp vào đúng chỗ.

Mức một, luôn đúng. Residual nội tại $A\to B$ của $\otimes$ tồn tại với mọi $(M,+)$ monoid giao hoán, không cần $\perp$. Đây là sự kiện tầm thường của lý thuyết quantale, không phải một tính chất đặc trưng cho $\perp$ nào cả.

Mức hai, trường hợp đặc biệt miễn phí. Nếu $\perp$ có dạng cực cộng tính $x\perp y\iff x+y\in D$ với $D$ cố định, thì $*=\bot_D$ toàn cục, và nucleus là hệ quả tự động của định lý phủ định kép trong quantale. Đây là phase semantics của logic tuyến tính. Girard quantale, theo đúng nghĩa gốc, chính là trường hợp này.

Mức ba, trường hợp cần chứng minh riêng. Nếu $\perp$ không có dạng cực (như Fenchel, đã chỉ ra ở trên), residual nội tại và polarity không trùng khớp toàn cục. Nucleus khi đó không tự động, và đúng khi và chỉ khi điều kiện cục bộ của Theorem A được thỏa: mỗi lát cắt $D_{x,y}$ riêng lẻ là polar, dù không có một $D$ chung nào làm việc cho mọi $x$. Fenchel và kernel toàn phương đều thuộc mức này, được cứu bởi residuation phần tử $x\backslash y$ phụ thuộc cặp, chứ không bởi một pole toàn cục.

## Vì sao sự phân biệt này quan trọng hơn là một điểm kỹ thuật

Nếu gộp mức một và mức ba lại, dễ rơi vào ngộ nhận rằng "vì $\otimes$ luôn có residual nên nucleus của bất kỳ $\perp$ nào cũng miễn phí". Phản ví dụ additivity ở file 2 (quan hệ $x\le y^2\wedge y\le x^2$ trên $\mathbb N$) chính là lời cảnh báo cho ngộ nhận này: residual của $\otimes$ trên $\mathcal P(\mathbb N)$ vẫn tồn tại như thường ở đó, nhưng nó không khớp với polarity sinh từ quan hệ ấy, và nucleus thất bại thật sự.

Ngược lại, nếu gộp mức hai và mức ba, dễ đi tìm một pole $D$ cho Fenchel một cách vô ích, vì đã chỉ ra rõ ràng không tồn tại. Điều cần tìm không phải một hằng số toàn cục, mà một hàm hai biến $x\backslash y$, và chính sự phụ thuộc vào cả hai biến, chứ không chỉ vào tổng $x+y$, là dấu hiệu của mức ba.

## Câu hỏi còn mở: một khái niệm cực xoắn tổng quát

Có một hướng tự nhiên nối lại mức hai và mức ba: liệu residuation kiểu $x\backslash y$ phụ thuộc cặp có luôn viết được như một cực bị xoắn bởi một tác động nào đó của $M$ lên chính nó, theo kiểu

$$
x\perp y\iff \sigma_x(y)\in D
$$

với $\sigma_x$ là một họ song ánh của $M$ tham số hóa bởi $x$ (với Fenchel, $\sigma_x(q,s)=(q,\ s-\langle p,q\rangle)$ nếu $x=(p,w)$), sao cho định lý phủ định kép miễn phí ở mức hai áp dụng được sau khi "tháo xoắn" bằng $\sigma_x$? Nếu đúng, toàn bộ Theorem A sẽ quy về đúng một câu: nucleus tự động một khi $\perp$ là cực xoắn bởi một tác động thích hợp, và việc kiểm tra một $\perp$ cụ thể chỉ còn là việc tìm ra $\sigma_x$ đúng, một bài toán mang tính xây dựng hơn là chứng minh lại toàn bộ Theorem A mỗi lần. Đây vẫn là một phỏng đoán, chưa phải kết quả đã kiểm chứng, nhưng nó cho một chương trình làm việc rõ ràng cho bước tiếp theo.
