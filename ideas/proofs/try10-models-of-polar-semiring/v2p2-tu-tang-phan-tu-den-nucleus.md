# Từ tầng phần tử đến nucleus (v2)

## Giới thiệu

File này là phiên bản viết lại của phần trung tâm nhất trong dự án: định lý đặc trưng cần-và-đủ cho điều kiện nucleus, cây cầu nối dữ liệu ở mức phần tử với đại số ở mức tập hợp. Nội dung toán học giữ nguyên; điều thay đổi là hệ ký hiệu, nay được chuẩn hóa cho toàn bộ dự án. Cấu trúc nguyên thủy $(M,\cdot,\perp)$ từ đây được gọi là một polaroid: một monoid giao hoán mang một quan hệ polar. Phép toán monoid viết theo lối nhân, polarity viết bằng mũ $\perp$, residual viết theo lối thương. Cách viết này tách bạch rõ ba tầng của lý thuyết: tầng phần tử với $\cdot$ và $\perp$; tầng tập hợp với các phép nâng thô $A\cdot B$, $A^\perp$, $A\cup B$; và tầng regular với các phép đã đóng hóa $A\otimes B$, $A\vee B$, $A\oslash B$. Đặc biệt, ký hiệu $\otimes$ từ nay được dành riêng cho tensor regular, tức tích đã lấy bipolar, khác với các phiên bản trước nơi $\otimes$ chỉ tích thô.

## Bảng ký hiệu

| Cấp | Ký hiệu | Tên gọi | Định nghĩa | Vai trò |
| --- | --- | --- | --- | --- |
| Primitive | $(M,\cdot,\perp)$ | Polaroid | Monoid giao hoán mang một quan hệ polar | Cấu trúc nguyên thủy |
| Element | $x\cdot y$ | Tích monoid | Phép nhân trên $M$ | Phép hợp thành đại số |
| Element | $x\perp y$ | Quan hệ polar | Quan hệ nguyên thủy trên $M$ | Tương tác hình học / logic |
| Element | $x/y$ | Residual | Residual của $\cdot$ (nếu tồn tại) | Phép kéo theo ở mức phần tử |
| Power set | $A\cdot B$ | Tích nâng | $\{x\cdot y:x\in A,\ y\in B\}$ | Tensor trước regular hóa |
| Power set | $A^\perp$ | Polarity | $\{y:\forall x\in A,\ x\perp y\}$ | Đối tượng đối ngẫu |
| Power set | $A\cup B$ | Hợp | Hợp thông thường | Join nguyên thủy |
| Power set | $A/B$ | Residual nâng | Residual cảm sinh từ residual phần tử | Kéo theo mức tập trước regular hóa |
| Regular | $A^{\perp\perp}$ | Bipolar closure | $(A^\perp)^\perp$ | Toán tử regular hóa |
| Regular | $A\otimes B$ | Tensor regular | $(A\cdot B)^{\perp\perp}$ | Tensor trong polar semiring |
| Regular | $A\vee B$ | Join regular | $(A\cup B)^{\perp\perp}$ | Join trong polar semiring |
| Regular | $A\oslash B$ | Residual regular | $(A/B)^{\perp\perp}$ | Residual trong polar semiring |

## Dữ liệu nguyên thủy: polaroid

Xuất phát điểm là một polaroid $(M,\cdot,\perp)$: một tập $M$ mang một phép nhân $\cdot:M\times M\to M$ làm cho $(M,\cdot,e)$ thành monoid giao hoán với đơn vị $e$, và một quan hệ polar $\perp\subseteq M\times M$ đối xứng, $x\perp y\iff y\perp x$.

Không có gì khác được giả sử. Không thứ tự, không topology, không tuyến tính. Mọi cấu trúc bổ sung, nếu cần, sẽ được thêm vào như giả thiết tường minh chứ không ngầm định.

Trước khi đi tiếp, hãy giữ trong đầu một ví dụ mẫu làm điểm tựa trực giác xuyên suốt. Lưu ý về quy ước: lý thuyết trừu tượng viết phép monoid theo lối nhân $x\cdot y$, nhưng trong các ví dụ cụ thể phép monoid thường là phép cộng của một nhóm quen thuộc; khi đó ta viết cộng như bình thường và ngầm hiểu đó chính là $\cdot$ của polaroid.

Ví dụ Fenchel. Lấy $M=\mathbb R^n\times\mathbb R$, tích monoid là phép cộng theo tọa độ $(p,w)\cdot(r,v)=(p+r,\ w+v)$, và quan hệ polar

$$
(p,w)\perp(q,s)\iff\langle p,q\rangle\le w+s.
$$

Phần tử thứ hai của mỗi cặp đóng vai trò một ngân sách: quan hệ polar nói rằng tích vô hướng giữa hai phần thứ nhất không vượt quá tổng hai ngân sách.

## Polarity và bipolar

Với mỗi $A\subseteq M$, polarity cho

$$
A^\perp:=\{y\in M:x\perp y\ \text{với mọi }x\in A\}.
$$

Vì quan hệ polar đối xứng, phép lấy polar hai lần, bipolar closure

$$
A^{\perp\perp}:=(A^\perp)^\perp,
$$

là một closure operator theo nghĩa quen thuộc: $A\subseteq A^{\perp\perp}$, đơn điệu, và lũy đẳng $(A^{\perp\perp})^{\perp\perp}=A^{\perp\perp}$. Điều này đúng với mọi quan hệ đối xứng, không cần thêm giả thiết. Ta gọi $A$ là regular nếu $A=A^{\perp\perp}$.

Trong ví dụ Fenchel, bipolar closure chính là bao đóng theo nghĩa hàm liên hợp: $A^{\perp\perp}$ tương ứng với epigraph của hàm lồi đóng nhỏ nhất chứa dữ liệu của $A$.

## Tích nâng và câu hỏi trung tâm

Tích monoid nâng lên thành tích nâng trên các tập con:

$$
A\cdot B:=\{a\cdot b:a\in A,\ b\in B\},
$$

trong ví dụ Fenchel đây là tổng Minkowski. Câu hỏi trung tâm của toàn bộ dự án: khi nào bipolar closure tương thích với tích nâng, theo nghĩa

$$
A^{\perp\perp}\cdot B^{\perp\perp}\subseteq(A\cdot B)^{\perp\perp} \tag{N}
$$

với mọi $A,B\subseteq M$? Đây là điều kiện nucleus.

Bộ ký hiệu mới cho phép phát biểu lại (N) dưới một dạng đặc biệt gợi hình. Tensor regular được định nghĩa là $A\otimes B:=(A\cdot B)^{\perp\perp}$; khi đó (N) tương đương với

$$
A^{\perp\perp}\otimes B^{\perp\perp}=A\otimes B, \tag{N'}
$$

tức tensor regular chỉ phụ thuộc vào bipolar của hai đối số, không phụ thuộc cách chọn đại diện. Chiều suy từ (N) sang (N') lấy bipolar hai vế của (N) rồi kẹp với bao hàm hiển nhiên $A\cdot B\subseteq A^{\perp\perp}\cdot B^{\perp\perp}$; chiều ngược đọc ngay từ $A^{\perp\perp}\cdot B^{\perp\perp}\subseteq A^{\perp\perp}\otimes B^{\perp\perp}$. Vậy nucleus chính xác là điều kiện để $\otimes$ được định nghĩa tốt trên các lớp regular, tức để phép nhân đi xuống được tầng thứ ba của bảng ký hiệu.

Điều kiện này không tầm thường chút nào. Bipolar của $A$ có thể lớn hơn $A$ rất nhiều, và khi nhân hai tập đã phồng lên như vậy, không có lý do tiên nghiệm nào để tích vẫn nằm trong bipolar của tích ban đầu. Chính xác đây là chỗ chứng minh định lý Fenchel truyền thống cần một thao tác kỹ thuật: tách một ngân sách $s$ thành $s=s_A+s_B$ sao cho mỗi phần dùng cho đúng một tập. Mục tiêu phần tiếp theo là làm rõ thao tác tách ấy thực chất là gì, ở mức trừu tượng nhất có thể.

## Từ tích nâng xuống một phép tịnh tiến duy nhất

Quan sát mấu chốt: kiểm tra (N) cho mọi cặp tập nghe có vẻ là một lượng tử phổ dụng khó kiểm soát, nhưng có thể quy về việc kiểm tra một họ tập rất đặc biệt: các tập một phần tử.

Với $x\in M$ cố định và $C\subseteq M$ bất kỳ, định nghĩa phép tịnh tiến ngược

$$
x\multimap C:=\{m\in M:x\cdot m\in C\}.
$$

Đây là tập mọi thứ có thể nhân thêm vào $x$ để vẫn rơi vào $C$. Phép toán này là internal hom của tích nâng trên $\mathcal P(M)$:

$$
\{x\}\cdot D\subseteq C\iff D\subseteq x\multimap C.
$$

Nó cũng là mảnh ghép đơn giản nhất của residual mức tập; liên hệ với residual nâng $A/B$ của bảng ký hiệu sẽ hiện ra ở cuối mục residuation. Ý tưởng bây giờ: nucleus đúng khi và chỉ khi phép tịnh tiến ngược bảo toàn tính regular.

## Định lý đặc trưng

Định lý. Cho polaroid $(M,\cdot,\perp)$. Ba điều sau tương đương.

(i) Nucleus: $A^{\perp\perp}\cdot B^{\perp\perp}\subseteq(A\cdot B)^{\perp\perp}$ với mọi $A,B\subseteq M$.

(ii) Điều kiện phản xạ: với mọi $x\in M$ và mọi tập regular $C$, tập $x\multimap C$ cũng regular.

(iii) Điều kiện mức phần tử: với mọi $x,y\in M$, lát cắt tịnh tiến

$$
D_{x,y}:=\{m\in M:(x\cdot m)\perp y\}
$$

là tập regular, tương đương là một tập polar: $D_{x,y}=Y^\perp$ với $Y$ nào đó.

Trước khi chứng minh, đáng dừng lại cảm nhận vì sao (iii) là điều đáng giá nhất. Nó không lượng hóa trên tập con nào, chỉ trên hai phần tử $x,y$. Nó hỏi: cố định $y$, tập những $m$ mà khi nhân vào $x$ thì polar-liên hệ được với $y$, tập đó có phải một tập polar hay không. Câu hỏi này kiểm tra trực tiếp trên công thức định nghĩa của quan hệ polar, không cần đụng đến closure operator một cách trừu tượng.

Chứng minh (i) suy ra (ii). Lấy $C$ regular, đặt $D=x\multimap C$. Theo định nghĩa, $\{x\}\cdot D\subseteq C$. Áp (i) cho cặp $\{x\}$ và $D$:

$$
\{x\}^{\perp\perp}\cdot D^{\perp\perp}\subseteq(\{x\}\cdot D)^{\perp\perp}\subseteq C^{\perp\perp}=C.
$$

Vì $x\in\{x\}^{\perp\perp}$ luôn đúng, suy ra $\{x\}\cdot D^{\perp\perp}\subseteq C$, tức $D^{\perp\perp}\subseteq x\multimap C=D$. Kết hợp với $D\subseteq D^{\perp\perp}$, ta có $D=D^{\perp\perp}$: regular.

Chứng minh (ii) suy ra (i). Đặt $C:=(A\cdot B)^{\perp\perp}$, một tập regular chứa $A\cdot B$. Với mỗi $a\in A$ cố định, từ $\{a\}\cdot B\subseteq C$ suy ra $B\subseteq a\multimap C$. Vì $a\multimap C$ regular theo (ii), và bipolar là closure nhỏ nhất chứa $B$ trong lớp regular, ta có $B^{\perp\perp}\subseteq a\multimap C$, tức $A\cdot B^{\perp\perp}\subseteq C$. Lặp lại theo biến còn lại: với mỗi $b\in B^{\perp\perp}$ cố định, từ $A\cdot\{b\}\subseteq C$ suy ra $A\subseteq b\multimap C$, regular theo (ii), nên $A^{\perp\perp}\subseteq b\multimap C$. Điều này đúng với mọi $b\in B^{\perp\perp}$, nên $A^{\perp\perp}\cdot B^{\perp\perp}\subseteq C=(A\cdot B)^{\perp\perp}$.

Chứng minh (ii) tương đương (iii). Mọi tập regular $C$ viết được thành giao các polar đơn phần tử: $C=Y^\perp$ với $Y=C^\perp$, và $Y^\perp=\bigcap_{y\in Y}\{y\}^\perp$. Phép tịnh tiến ngược giao hoán với phép giao, $x\multimap\bigcap_iC_i=\bigcap_i(x\multimap C_i)$, và với $C=\{y\}^\perp$ tính trực tiếp

$$
x\multimap\{y\}^\perp=\{m:x\cdot m\in\{y\}^\perp\}=\{m:(x\cdot m)\perp y\}=D_{x,y}.
$$

Lớp regular ổn định dưới giao tùy ý, nên (iii) áp cho từng $y\in Y$ kéo theo (ii) cho $C=Y^\perp$ bất kỳ, và mọi tập regular đều có dạng ấy. Chiều ngược lấy $C=\{y\}^\perp$ trong (ii) chính là (iii). $\blacksquare$

Đây là dạng $\mathcal P(M)$ của định lý phản xạ Day, kết quả kinh điển của lý thuyết phạm trù đóng: closure đi qua được tensor khi và chỉ khi lớp đối tượng đóng ổn định dưới internal hom. Điều thú vị: trên $\mathcal P(M)$ cụ thể, internal hom quy được hoàn toàn về mức phần tử, và đó là nội dung của (iii).

## Điều kiện đủ dễ kiểm tra: residuation

Điều kiện (iii) là cần và đủ, nhưng để kiểm một ví dụ cụ thể, tiện hơn nếu có tiêu chuẩn mang tính xây dựng. Đây là nơi residual $x/y$ của bảng ký hiệu bước vào.

Giả sử với mọi $x,y\in M$ tồn tại phần tử $x/y\in M$ với tính chất định nghĩa

$$
(x\cdot m)\perp y\iff m\perp(x/y)\qquad\text{với mọi }m.
$$

Khi đó lập tức $D_{x,y}=\{m:m\perp(x/y)\}=\{x/y\}^\perp$, một tập polar theo đúng định nghĩa. Điều kiện (iii) tự động thỏa, nucleus đúng. Một polaroid có residual như vậy gọi là polaroid residuated.

Vì sao gọi là residual: công thức trên đúng là công thức phần dư trong một quantale, $x/y$ là dữ liệu cho phép hấp thụ phép nhân với $x$ vào chính quan hệ polar. Đọc theo tinh thần logic, $x/y$ là phép kéo theo ở mức phần tử: kiểm tra "$x\cdot m$ chống lại $y$" tương đương kiểm tra "$m$ chống lại $x/y$".

Đây cũng là chỗ residual nâng $A/B$ của bảng ký hiệu nhận nghĩa: khi residual phần tử tồn tại, đặt $A/B:=\{a/b:a\in A,\ b\in B\}$, thì với các lát đơn, $D_{x,y}=\{x/y\}^\perp$ nói rằng internal hom của các polar đơn được đại diện bởi residual nâng của các điểm; và residual regular $A\oslash B=(A/B)^{\perp\perp}$ là phiên bản đã đóng hóa của nó, sống ở tầng ba cùng $\otimes$ và $\vee$. Khảo sát đầy đủ tầng này thuộc về file dựng polar semiring; ở đây chỉ cần mảnh đơn giản nhất.

## Ba ví dụ qua lăng kính residuation

Ví dụ Fenchel. Với $x=(p,w)$, $y=(q,s)$, khai triển trực tiếp:

$$
\langle p+r,q\rangle\le w+v+s\iff\langle r,q\rangle\le v+(w+s-\langle p,q\rangle).
$$

Vậy $x/y=(q,\ w+s-\langle p,q\rangle)$. Residual tồn tại nhờ tính song tuyến tính của tích vô hướng, cho phép tách $\langle p+r,q\rangle$ thành $\langle p,q\rangle+\langle r,q\rangle$. Đây chính là thao tác tách ngân sách trong chứng minh cổ điển, nay lộ rõ là trường hợp riêng của một cơ chế tổng quát hơn nhiều.

Ví dụ phase semantics. Nếu quan hệ polar có dạng $x\perp y\iff x\cdot y\in D$ với một pole $D\subseteq M$ cố định, residual gần như tầm thường: $x/y=x\cdot y$, vì $(x\cdot m)\cdot y\in D\iff m\cdot(x\cdot y)\in D$ nhờ giao hoán và kết hợp. Đây là lý do quantale các facts trong ngữ nghĩa pha của logic tuyến tính luôn được định nghĩa tốt mà không cần giả thiết nào ngoài tính monoid giao hoán.

Ví dụ kernel toàn phương. Lấy $M=\mathbb R^n\times\mathbb R$ như trước, thay quan hệ Fenchel bằng

$$
(p,w)\perp(q,s)\iff\tfrac12\|p-q\|^2\le w+s.
$$

Mấu chốt không phải tính lồi hay tuyến tính, mà là tính bất biến tịnh tiến của kernel: $\tfrac12\|(p+r)-q\|^2=\tfrac12\|r-(q-p)\|^2$. Từ đó

$$
(p+r,\ w+v)\perp(q,s)\iff(r,v)\perp(q-p,\ w+s),
$$

nên $x/y=(q-p,\ w+s)$. Nucleus đúng cho kernel toàn phương, và bipolar sinh ra chính là proximal hull, bao đóng gần kề của giải tích biến phân. Đáng chú ý: toàn bộ lập luận không dùng đến việc $\tfrac12\|\cdot\|^2$ là hàm lồi.

Nhìn ba ví dụ cùng lúc, một quy luật chung xuất hiện.

Mệnh đề. Cho $X$ nhóm giao hoán, $\varphi:X\times X\to\mathbb R$, polaroid $M=X\times\mathbb R$ với tích theo tọa độ và $(p,w)\perp(q,s)\iff\varphi(p,q)\le w+s$. Nếu tồn tại $\tau(p,q)\in X$ và $\delta(p,q)\in\mathbb R$ sao cho

$$
\varphi(p+r,\ q)=\varphi(r,\ \tau(p,q))+\delta(p,q)\qquad\text{với mọi }r,
$$

thì $x/y=(\tau(p,q),\ w+s-\delta(p,q))$, và nucleus đúng.

Trường hợp riêng đáng nhớ nhất: mọi kernel bất biến tịnh tiến $\varphi(p,q)=\psi(q-p)$ trên một nhóm, với $\psi$ hoàn toàn tùy ý, đều sinh nucleus. Phát biểu này mạnh hơn nhiều so với trực giác "phải lồi mới đúng".

## Khi trực giác sai: additivity không đủ và không cần

Có một ứng viên rất tự nhiên cho điều kiện đủ, thoạt nhìn có vẻ đúng hướng: nếu $x_1\perp y_1$ và $x_2\perp y_2$ thì $(x_1\cdot x_2)\perp(y_1\cdot y_2)$. Gọi đây là tính additivity của quan hệ polar (giữ tên cũ dù phép toán nay viết theo lối nhân, vì trong mọi ví dụ số nó là phép cộng). Đáng kiểm tra kỹ, vì đây là thứ đầu tiên ai cũng nghĩ đến.

Additivity không đủ. Lấy polaroid $M=(\mathbb N,+)$, tích monoid là phép cộng số tự nhiên, và

$$
x\perp y\iff x\le y^2\ \text{và}\ y\le x^2.
$$

Quan hệ đối xứng theo định nghĩa, và additive: nếu $x_1\le y_1^2$, $x_2\le y_2^2$ thì $x_1+x_2\le y_1^2+y_2^2\le(y_1+y_2)^2$, tương tự chiều kia. Nhưng tính trực tiếp: $\{2\}^\perp=\{y:2\le y^2,\ y\le 4\}=\{2,3,4\}$, nên $\{2\}^{\perp\perp}=\{x\le 4:x^2\ge 4\}=\{2,3,4\}$. Trong khi đó $\{2\}\cdot\{2\}=\{4\}$, và $\{4\}^\perp=\{2,\dots,16\}$, nên $\{4\}^{\perp\perp}=\{x\le 4:x^2\ge 16\}=\{4\}$. Vậy $\{2\}^{\perp\perp}\cdot\{2\}^{\perp\perp}=\{4,\dots,8\}\not\subseteq\{4\}$: nucleus sai dù additivity đúng.

Đọc lại qua định lý đặc trưng: $D_{2,2}=\{m:(2+m)\perp 2\}=\{0,1,2\}$, và $\{0,1,2\}^\perp=\varnothing$ nên $\{0,1,2\}^{\perp\perp}=M\ne\{0,1,2\}$: điều kiện (iii) vỡ ngay tại $x=y=2$. Additivity quá yếu để kiểm soát hành vi của lát cắt tịnh tiến.

Additivity không cần. Quan hệ Fenchel không additive: với $n=1$, $(t,0)\perp(0,0)$ đúng và $(0,0)\perp(t,0)$ đúng, nhưng tích đòi $(t,0)\perp(t,0)$, tức $t^2\le 0$, sai với $t>0$. Fenchel có nucleus mà không additive.

Lý do sâu xa: additivity là phát biểu về polar bậc nhất, $A^\perp\cdot B^\perp\subseteq(A\cdot B)^\perp$, còn nucleus là phát biểu về bipolar. Polarity đảo chiều bao hàm thức, nên một bất đẳng thức đúng ở mức polar không tự động chuyển thành bất đẳng thức đúng ở mức bipolar. Phản ví dụ minh họa đúng cơ chế: closure phồng $\{2\}$ lên hẳn $\{2,3,4\}$ nhưng không phồng $\{4\}$ tương ứng đủ để chứa tích.

## Nhìn lại: điều gì đã học được

Điều kiện nucleus, dù phát biểu ở tầng tập hợp, hoàn toàn được quyết định bởi hành vi của quan hệ polar trên từng cặp phần tử, cụ thể bởi việc các lát cắt tịnh tiến $D_{x,y}$ có là tập polar hay không; và trong ký hiệu mới, nó chính là điều kiện để tensor regular $\otimes$ được định nghĩa tốt qua các lớp bipolar, mở đường cho toàn bộ tầng regular của bảng ký hiệu. Residual $x/y$ là cách xây dựng tường minh và hiệu quả nhất để đảm bảo điều đó, bao trùm mọi ví dụ cổ điển: song tuyến tính trong Fenchel, tính nhóm trong phase semantics, bất biến tịnh tiến trong kernel toàn phương. Trong khi đó additivity, ứng viên trực giác nhất, là một điều kiện ở tầng sai.

Với định lý đặc trưng và bộ ví dụ này trong tay, ta đủ nền tảng để lên tầng tập hợp và dựng đại số hoàn chỉnh với bộ ba phép toán regular $\vee$, $\otimes$, $\oslash$, nội dung của file tiếp theo.
