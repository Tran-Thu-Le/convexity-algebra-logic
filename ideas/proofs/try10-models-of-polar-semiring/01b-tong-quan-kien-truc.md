# Polar Semiring: Tổng quan kiến trúc (bản cập nhật)

## Dự án này nói về điều gì

Có một hiện tượng lặp lại ở ba vùng toán học tưởng như xa nhau. Trong giải tích lồi, liên hợp Fenchel và bao lồi đóng tương thích với phép cộng Minkowski theo một cách rất đặc biệt. Trong logic tuyến tính, ngữ nghĩa pha xây các "facts" từ một quan hệ trực giao, và tensor luôn đi xuống được lớp facts. Trong hình học khoảng cách và giải tích biến phân, bao gần kề sinh từ kernel toàn phương cũng hành xử y hệt. Ba câu chuyện, ba ngôn ngữ, một khung xương chung.

Dự án chỉ ra khung xương đó: mọi thứ được sinh ra từ một bộ ba dữ liệu tối thiểu ở mức phần tử,

$$
(M,\ +,\ \perp),
$$

gồm một monoid giao hoán và một quan hệ đối xứng, mà ta gọi là một orthogonality monoid. Từ bộ ba này, một cách máy móc, sinh ra cả một đại số bốn phép toán với đối ngẫu hoàn hảo trên lớp các tập regular. Chốt chặn duy nhất trên đường đi là điều kiện nucleus, và điều kiện này có một đặc trưng cần-và-đủ ngay ở mức phần tử. Sâu hơn nữa, khi quan hệ $\perp$ đến từ một kernel số, toàn bộ các ví dụ mốc được phân loại trọn vẹn bởi một bất biến duy nhất: hạng của residual action, một khái niệm mới xuất hiện trong chính dự án này.

Điểm xuất phát của toàn bộ câu chuyện không phải semiring, không phải lattice, không phải negation. Tất cả những thứ đó là sản phẩm. Primitive tuyệt đối chỉ có hai: phép cộng và quan hệ.

## Tầng một: nâng từ phần tử lên tập hợp

Đặt $S=\mathcal P(M)$. Ba cấu trúc tự động xuất hiện: join $A\vee B=A\cup B$ từ phép hợp; tensor $A\otimes B=A+B$ (tổng Minkowski) nâng từ phép cộng; polarity $A^*=\{y:\forall x\in A,\ x\perp y\}$ nâng từ quan hệ. Không cấu trúc nào trong ba là primitive độc lập ở tầng tập: chúng đều là bóng của dữ liệu tầng dưới.

Vì tensor phân phối trên hợp tùy ý, $S$ không chỉ là một idempotent commutative semiring mà là một commutative unital quantale. Và đây là quan sát then chốt đầu tiên, dễ bị bỏ qua nhất: quantale luôn tự có residual,

$$
A\multimap C=\{m:A+m\subseteq C\},
$$

thỏa $A+B\subseteq C\iff B\subseteq A\multimap C$. Trong hình học Minkowski, đây chính là hiệu Minkowski $C\ominus A=\bigcap_{a\in A}(C-a)$, phép erosion của hình thái học toán học. Residual không phải thứ polarity tạo ra; nó có sẵn từ trước, chỉ nhờ $(M,+)$. Điều polarity mang đến là một câu hỏi: closure sinh từ nó có tương thích với đại số có sẵn hay không.

## Tầng hai: closure, nucleus, và định lý trung tâm

Vì $\perp$ đối xứng, $c(A)=A^{**}$ là closure operator; fixed points $S_c$ là lớp các tập regular. Với join, mọi closure đều tương thích tự động. Toàn bộ độ khó dồn vào tensor: điều kiện nucleus

$$
c(A)\otimes c(B)\subseteq c(A\otimes B)
$$

không tự động, và nó chính xác tương đương với việc quan hệ "cùng bipolar" là một congruence đối với tensor, tức tương đương với việc đại số đi xuống được lớp thương. Định lý trung tâm của dự án (file 2) đặc trưng nó trọn vẹn ở mức phần tử:

$$
c\text{ là nucleus}\iff x\multimap C\text{ đóng với mọi }x,\ C\text{ đóng}\iff D_{x,y}:=\{m:(x+m)\perp y\}\text{ là tập regular với mọi }x,y.
$$

Đọc bằng lời: bipolar closure là nucleus khi và chỉ khi mọi lát cắt residual của quan hệ trực giao đều regular. Đây là lời giải cần-và-đủ cho bài toán element-to-set lifting, và là chiếc cầu chính xác nối quan hệ ở tầng phần tử với congruence ở tầng tập.

Điều kiện đủ mạnh hơn, dễ kiểm tra hơn, là residuation ở mức phần tử: tồn tại $x\backslash y\in M$ sao cho $(x+m)\perp y\iff m\perp(x\backslash y)$; khi đó $D_{x,y}=\{x\backslash y\}^*$ là polar theo định nghĩa. Cấu trúc $(M,+,\perp)$ mang thêm điều kiện này xứng đáng một cái tên riêng: residuated orthogonality monoid.

Một kết quả âm quan trọng ngang định lý dương: ứng viên trực giác nhất, tính additivity của $\perp$ ($x_1\perp y_1,\ x_2\perp y_2\Rightarrow x_1+x_2\perp y_1+y_2$), không đủ và cũng không cần. Nó kiểm soát polar bậc nhất, trong khi nucleus là phát biểu về bipolar; phản ví dụ cụ thể trên $(\mathbb N,+)$ nằm ở file 2. Điều kiện đúng nằm ở lát cắt $D_{x,y}$, không nằm ở bản thân quan hệ.

## Tầng ba: thương, regular hóa, và bốn phép toán

Dưới nucleus, lớp thương $S/{\sim_c}$ là một semiring, đẳng cấu với $S_c$ mang các phép toán regularized $U\vee_c V=(U\cup V)^{**}$ và $U\otimes_c V=(U+V)^{**}$; ánh xạ $c:S\twoheadrightarrow S_c$ là toàn cấu semiring. Trên $S_c$, polarity từ một ánh xạ không khả nghịch trên $S$ kết tinh thành một involution nghịch biến, $*:S_c\overset{\cong}{\to}S_c^{\mathrm{op}}$, và transport of structure qua involution sinh miễn phí hai phép toán đối ngẫu

$$
U\wedge V=(U^*\vee_c V^*)^*,\qquad U\oplus V=(U^*\otimes_c V^*)^*,
$$

với các luật De Morgan đúng theo định nghĩa. Kết quả là polar semiring $(S_c,\vee_c,\wedge,\otimes_c,\oplus,{}^*)$: bốn phép toán, nhưng chỉ hai primitive. Toàn bộ quá trình dựng chi tiết nằm ở file 3.

Một câu tóm cả ba tầng: closure tạo lớp thương, nucleus biến lớp thương thành đại số thương, involution nhân đôi số phép toán.

## Phân biệt then chốt: residual có sẵn và tính tương thích với $\perp$

File 4 tách bạch một nhầm lẫn dễ mắc. Residual $\multimap$ của tensor luôn tồn tại, miễn phí, với mọi $(M,+)$; nhưng nó là một phép phủ định nội tại, còn polarity $*$ là phép phủ định ngoại lai đến từ $\perp$, và hai thứ này a priori không liên quan. Chúng trùng nhau toàn cục đúng khi $\perp$ có dạng cực: tồn tại pole $D\subseteq M$ với

$$
x\perp y\iff x+y\in D,
$$

lúc đó $A^*=A\multimap D$, nucleus là định lý miễn phí của lý thuyết quantale (phủ định kép qua một phần tử cố định luôn là nucleus), và trên $S_c$ ta khôi phục trọn residual kiểu Girard: $A\multimap B=(A\otimes B^*)^*$. Đây chính xác là phase semantics, và là lý do Girard quantale không bao giờ cần một định lý riêng.

Fenchel chứng minh được là không có dạng cực (cùng một tổng, hai cách tách cho hai kết luận trái ngược), nên nucleus của nó đúng vì cơ chế cục bộ của định lý trung tâm, không vì cơ chế miễn phí. Ba mức phân loại: residual luôn có (tầm thường); pole toàn cục (Girard, miễn phí); lát cắt regular từng cặp (Fenchel và họ hàng, cần định lý thật). Framework của dự án rộng hơn Girard đúng ở chỗ này: không đòi $\perp$ được đại diện bởi một pole, chỉ đòi các residual slices regular.

## Tầng bốn: lý thuyết kernel và phương trình cocycle

Khi quan hệ đến từ một kernel số, $M=X\times\mathbb R$ và $(p,w)\perp_\phi(q,s)\iff\phi(p,q)\le w+s$, điều kiện đủ residuation trở thành một phương trình hàm cụ thể, phương trình cocycle:

$$
\phi(p+r,\ q)=\phi\bigl(r,\ \tau(p,q)\bigr)+\delta(p,q)\qquad\forall r. \tag{Coc}
$$

Khi nó có nghiệm, residual phần tử là $(p,w)\backslash(q,s)=(\tau(p,q),\ w+s-\delta(p,q))$ và nucleus theo sau. File 5 khảo sát phương trình này trên các họ kernel của giải tích lồi, với một kết quả cứng đáng chú ý: với kernel không thuộc dạng sai phân, điều kiện (Coc) đòi các số gia $F(p+r)-F(r)$ affine theo $r$, và dưới giả thiết $C^2$ điều này ép Hessian hằng. Hệ quả: Fenchel-Young coupling $F(x)+F^*(y)-\langle x,y\rangle$ và Bregman divergence $D_F$ sinh nucleus khi $F$ toàn phương, và không tự động với $F$ lồi tổng quát. Hình học Bregman tổng quát, nếu muốn tương thích, có lẽ cần một tensor biến dạng theo hình học của $F$ thay vì spatial sum thường; đây là một hướng mở được đánh dấu rõ.

Ngược lại, kernel toàn phương $\tfrac12\|p-q\|^2$ nằm gọn trong lớp sai phân $\phi=\psi(q-p)$, nơi (Coc) đúng với $\tau=q-p$, $\delta=0$, không cần lồi, không cần trơn. Bài học: cơ chế thật của kernel toàn phương là bất biến tịnh tiến, không phải song tuyến tính hay gauge transform.

## Tầng năm: residual rank và định lý phân loại

File 6 là tầng sâu nhất hiện có, chứng minh đầy đủ chuỗi khẳng định sau. Thứ nhất, dưới một điều kiện không suy biến nhẹ, $\tau$ trong (Coc) buộc phải là một tác động phải của $(X,+)$ lên $X$, và $\delta$ buộc là cocycle của tác động đó. Thứ hai, các tác động đẳng biến tịnh tiến có đúng dạng $\tau_\varphi(p,q)=q+\varphi(p)$ với $\varphi\in\mathrm{End}(X)$, tính cộng tính của $\varphi$ được suy ra chứ không giả sử. Thứ ba, phương trình (Coc) trong mỗi sector được giải trọn: mọi nghiệm có dạng

$$
\phi(x,y)=\psi\bigl(y+\varphi(x)\bigr)+\widetilde A_{[y]}(x)+\eta(y),
$$

và số hạng hiệu chỉnh $\delta$ chính là thành phần cocycle của kernel. Hệ quả đẹp nhất của phân tách này: cặp $(\tau_\varphi,\delta)$ có kernel thỏa (Coc) khi và chỉ khi $\delta$ tự nó là cocycle, và khi đó tập nghiệm là không gian affine mô hình trên các hàm một biến $\psi$. Vậy primitive của lớp kernel residuated chính là cặp $(\varphi,\delta)$; kernel chỉ là cặp ấy cộng một bậc tự do trơ. Lưu ý ranh giới: $(\varphi,\delta)$ là primitive của lớp kernel residuated, không phải primitive tuyệt đối của toàn framework; primitive tuyệt đối vẫn là $(M,+,\perp)$.

Thứ tư, và là định lý phân loại: đổi biến tuyến tính độc lập hai phía biến sector theo $\varphi\mapsto B^{-1}\varphi A$, mà quan hệ tương đương hai phía trên $\mathrm{End}(\mathbb R^n)$ được phân loại bởi đúng một bất biến, hạng. Ta gọi nó là residual rank. Kết quả: đúng $n+1$ sector sai khác đổi biến,

$$
\begin{array}{c|c|c}
\text{residual rank} & \text{đại diện} & \text{ý nghĩa}\\
\hline
0 & \varphi=0 & \text{sector Fenchel: coupling affine }L_y(x)+\gamma(y)\\
n & \varphi=-I & \text{sector sai phân }\psi(y-x)+\eta(y)\text{; phase semantics qua }y\mapsto-y\\
0<r<n & \varphi=-P_r & \text{sector lai: sai phân trên }r\text{ phương, Fenchel trên }n-r\text{ phương}
\end{array}
$$

Ba hệ quả khái niệm. Một, phase semantics ($\varphi=I$) và kernel sai phân ($\varphi=-I$) cùng hạng $n$, nên là một lý thuyết sai khác quy ước dấu ở biến đối ngẫu; logic tuyến tính và hình học khoảng cách hợp nhất ở tầng này. Hai, Fenchel (hạng $0$) tách tuyệt đối khỏi hạng $n$: không phép đổi biến tuyến tính nào nối chúng, và đây là lý do cấu trúc khiến tổng một kernel Fenchel với một kernel sai phân trên cùng biến rơi ra ngoài mọi sector, giải thích tận gốc các phản ví dụ cộng kernel ở file trước. Ba, các sector trung gian là lai ghép thật sự, với ví dụ mới cụ thể $\tfrac12\|y_1-x_1\|^2+\langle x_2,y_2\rangle$, nửa toàn phương nửa Fenchel, đối xứng, sinh nucleus; và mệnh đề tổng trực tiếp cho thấy thang $n+1$ bậc chính là thang nội suy rời rạc

$$
(\text{sai phân})^{\oplus r}\oplus(\text{Fenchel})^{\oplus(n-r)}
$$

giữa đúng hai lý thuyết nguyên thủy. Về calculus của các kernel: mỗi $\mathcal K_\tau$ là một không gian vector (cộng, nhân vô hướng bảo toàn sector, với $\delta$ biến đổi tuyến tính theo); các ràng buộc bổ sung như không âm, đối xứng, triệt tiêu trên đường chéo cắt nó xuống một nón; không trộn được hai sector trên cùng biến, trộn tự do trên các khối biến độc lập. Cần nhớ giới hạn: rank phân loại các residual action, chưa phân loại hết các kernel; trong một sector vẫn có vô số kernel, và kernel suy biến có thể thuộc nhiều sector.

## Ba đóng góp của dự án, phát biểu gọn

Một nguyên lý kiến tạo: từ $(M,+,\perp)$ dựng chuỗi semiring, polarity, closure, quotient, polar semiring; không phải một mô hình của polar semiring mà là một cơ chế sinh polar semiring.

Một định lý cầu nối: nucleus khi và chỉ khi mọi lát residual $D_{x,y}$ regular; lời giải cần-và-đủ của element-to-set lifting.

Một sự thống nhất có phân loại: Fenchel polarity, kernel sai phân và toàn phương, $c$-polarity, hiệu Minkowski và erosion, residual của quantale, phase semantics và phủ định kiểu Girard, tất cả cùng được sinh qua một chuỗi duy nhất, và phần residuated của bức tranh được phân tầng trọn vẹn bởi residual rank, với hai thái cực Fenchel và phase/difference cùng các bậc lai ở giữa.

## Sơ đồ tổng thể

$$
(M,+,\perp)\ \xrightarrow{\ \mathcal P\ }\ \bigl(S,\vee,\otimes,{}^*,\multimap\bigr)\ \xrightarrow{\ c={}^{**},\ \text{nucleus}\ }\ S/{\sim_c}\ \cong\ S_c\ \xrightarrow{\ \text{De Morgan}\ }\ (S_c,\vee_c,\wedge,\otimes_c,\oplus,{}^*)
$$

và, riêng cho nhánh kernel:

$$
\phi\ \xrightarrow{\ \text{(Coc)}\ }\ (\varphi,\delta)\ \xrightarrow{\ B^{-1}\varphi A\ }\ \text{residual rank }r\in\{0,\dots,n\}.
$$

## Bản đồ các file

File 2 chứng minh định lý trung tâm ba điều kiện tương đương, residuation phần tử, và phản ví dụ additivity. File 3 dựng toàn bộ tầng tập hợp đến polar semiring. File 4 tách residual nội tại khỏi tính tương thích với $\perp$, định vị phase semantics là trường hợp pole miễn phí và Fenchel là trường hợp cần định lý. File 5 khảo sát các họ kernel của giải tích lồi qua phương trình cocycle, với kết quả cứng về tính toàn phương. File 6 chứng minh đầy đủ luật tác động, giải trọn phương trình cocycle, và định lý phân loại theo residual rank.

## Các hướng còn mở

Các tác động không đẳng biến tịnh tiến chưa được phân loại. Khoảng cách giữa điều kiện đủ (Coc) và tiêu chuẩn cần-đủ của định lý trung tâm chưa được đo: có thể tồn tại kernel sinh nucleus ngoài mọi sector residuated. Bài toán phân loại trong lớp đối xứng, với nhóm đổi biến chéo và bất biến liên hợp mịn hơn hạng, mới được nhận diện. Và câu hỏi lớn nhất từ phía giải tích: với $F$ lồi không toàn phương, liệu có một tensor biến dạng theo hình học của $F$ (qua đổi tọa độ gradient, theo tinh thần hình học thông tin) làm cho Bregman coupling trở nên residuated, tức đưa cả giải tích lồi phi toàn phương vào bức tranh bằng cách xoắn phép cộng thay vì xoắn quan hệ.

## Một câu để mang theo

Tương tác ở mức phần tử sinh ra đối ngẫu và đại số ở mức tập regular; và trong thế giới kernel, toàn bộ phổ các tương tác residuated trải từ Fenchel đến phase semantics trên một chiếc thang $n+1$ bậc, đo bởi đúng một con số, residual rank.
