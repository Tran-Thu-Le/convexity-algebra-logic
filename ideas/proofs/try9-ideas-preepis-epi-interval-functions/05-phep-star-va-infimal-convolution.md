# Phép star cảm sinh bởi spatial sum, tổng quát hóa infimal convolution

## 1. Câu hỏi xuất phát

Với hàm lồi, phép infimal convolution

$$
(f\square g)(x) = \inf_{u+v=x} \{f(u)+g(v)\}
$$

là phép toán chính xác thỏa

$$
\operatorname{epi}(f\square g) = \operatorname{epi}(f) \boxplus_{\mathrm{sp}} \operatorname{epi}(g),
$$

một định lý nền tảng của giải tích lồi.

Câu hỏi: với hàm giá trị-khoảng $F(x)=[l_F(x),u_F(x)]$, có tồn tại một phép $F\square G$ tương tự, thỏa

$$
\operatorname{Preepi}(F\square G) = \operatorname{Preepi}(F) \boxplus_{\mathrm{sp}} \operatorname{Preepi}(G)?
$$

Theo hiểu biết thông thường, không có một phép toán chuẩn được chấp nhận rộng rãi cho vai trò này đối với hàm giá trị-khoảng; người ta thường làm việc trực tiếp với tập giá trị. Với ánh xạ đa trị (set-valued map) thì có các phép Minkowski sum, inf-projection, inf-translation, inf-extension, nhưng đây là các xây dựng trong lý thuyết tối ưu, không đóng vai trò như $f\square g$.

Tuy nhiên, nhìn từ góc độ preepi và spatial sum, một phép toán như vậy xuất hiện một cách hoàn toàn tự nhiên, không cần giả thiết gì đặc biệt về lớp giá trị. Đây là nội dung của file này.

## 2. Thiết lập

Cho X và K là hai nửa nhóm giao hoán cộng được (ví dụ $X=K=\mathbb R$). Cho $F, G: X \to \mathcal P(K)$ là hai hàm giá trị-tập hợp bất kỳ, chưa cần giả thiết gì về lớp giá trị của chúng. Định nghĩa preepi tương ứng

$$
A_F = \bigcup_{u\in X} \{u\}\times F(u) \;\subseteq\; X\times K,
$$

và tương tự $A_G$ với G.

Spatial sum, theo đúng định nghĩa gốc, cộng cả tọa độ không gian lẫn tọa độ giá trị:

$$
A_F \boxplus_{\mathrm{sp}} A_G = \big\{(x,k) : \exists\, (u,k_1)\in A_F,\ (v,k_2)\in A_G,\ x=u+v,\ k=k_1+k_2 \big\}.
$$

Định nghĩa phép star

$$
(F\star G)(x) := \bigcup_{u+v=x} \big(F(u)+G(v)\big),
$$

nơi $F(u)+G(v) = \{k_1+k_2 : k_1\in F(u),\ k_2\in G(v)\}$ là tổng Minkowski thông thường.

## 3. Định lý

$$
\operatorname{Preepi}(F\star G) = A_F \boxplus_{\mathrm{sp}} A_G.
$$

## 4. Chứng minh

Chứng minh trực tiếp bằng một chuỗi tương đương logic, không cần giả thiết lồi, đóng, hay giao khác rỗng nào về F, G:

$$
(x,k) \in A_F \boxplus_{\mathrm{sp}} A_G
$$

$$
\iff \exists\, u,v,k_1,k_2 \text{ với } u+v=x,\ k_1\in F(u),\ k_2\in G(v),\ k=k_1+k_2
$$

$$
\iff \exists\, u,v \text{ với } u+v=x \text{ sao cho } k \in F(u)+G(v)
$$

$$
\iff k \in \bigcup_{u+v=x} \big(F(u)+G(v)\big)
$$

$$
\iff k \in (F\star G)(x)
$$

$$
\iff (x,k) \in \operatorname{Preepi}(F\star G).
$$

Mỗi bước là một khai triển định nghĩa thuần túy. Không có bước nào cần đến tính lồi, tính đóng, hay điều kiện giao khác rỗng của các tập giá trị. $\blacksquare$

Nói cách khác: đây không phải một định lý sâu về lớp giá trị $\mathcal S$, mà là hệ quả tất yếu của cách spatial sum được định nghĩa. Spatial sum cộng cả tọa độ không gian, và cộng tọa độ không gian theo mọi cách phân tích $x=u+v$ có thể chính xác là phép convolution. Phần khó của lý thuyết, tức luật phân phối trên $\mathcal S$ (các định lý A đến E của file phân tầng và chứng minh), không cần dùng cho chính đẳng thức này; nó chỉ cần khi ta muốn nói thêm điều gì đó về cấu trúc của $F\star G$.

## 5. Điều kiện kèm theo: tính đóng của lớp giá trị

Đẳng thức tập hợp ở trên đúng vô điều kiện, nhưng để $F\star G$ vẫn là một hàm giá trị trong cùng lớp $\mathcal S$ đang xét, tức để $(F\star G)(x) \in \mathcal S$ với mọi x, cần $\mathcal S$ đóng dưới hợp của các họ dạng

$$
\{F(u)+G(v)\}_{u+v=x}.
$$

Nếu không có điều kiện này, $F\star G$ vẫn tồn tại như một hàm giá trị-tập hợp bình thường, và đẳng thức Preepi ở phần 3 vẫn đúng, chỉ là kết quả không còn nằm gọn trong cùng lớp $\mathcal S$ đang làm việc, tương tự cách spatial sum phân phối lên hợp tùy ý mà không cần điều kiện gì (file động lực), trong khi việc ở lại trong một lớp cụ thể lại là chuyện khác.

## 6. Trường hợp riêng: epigraph, và khớp với lý thuyết cổ điển

Lấy $F(x)=[f(x),\infty)$, $G(x)=[g(x),\infty)$. Khi đó với mỗi cặp $(u,v)$,

$$
F(u)+G(v) = [f(u)+g(v),\ \infty),
$$

và

$$
(F\star G)(x) = \bigcup_{u+v=x} [f(u)+g(v), \infty).
$$

Đặt

$$
m(x) = \inf_{u+v=x} \big(f(u)+g(v)\big).
$$

Hợp của một họ tia đóng $[c,\infty)$ khi c chạy trên một tập C có công thức:

nếu infimum của C đạt được bởi một phần tử của C, hợp bằng $[\inf C,\infty)$,

nếu infimum của C không đạt được bởi phần tử nào của C, hợp bằng $(\inf C,\infty)$, một tia mở.

Trong khi đó, theo định nghĩa cổ điển,

$$
\operatorname{epi}(f\square g)(x) = [m(x),\infty)
$$

luôn là một tia đóng, bất kể $m(x)$ có được đạt tới bởi một cặp $(u,v)$ cụ thể hay không, vì đây chỉ là giá trị số thực của hàm $f\square g$ tại x.

Do đó:

$$
(F\star G)(x) \subseteq \operatorname{epi}(f\square g)(x) \text{ luôn đúng},
$$

và

$$
(F\star G)(x) = \operatorname{epi}(f\square g)(x) \iff \inf_{u+v=x}\big(f(u)+g(v)\big) \text{ đạt được tại một cặp } (u,v).
$$

Đây chính xác là điều kiện exact infimal convolution quen thuộc trong giải tích lồi: đẳng thức

$$
\operatorname{epi}(f\square g) = \operatorname{epi}(f) + \operatorname{epi}(g)
$$

chỉ đúng khi infimum trong định nghĩa của $f\square g$ được đạt tới tại mỗi x; nếu không, chỉ có bao hàm thức, và cần lấy bao đóng để sửa lại.

Việc định lý tổng quát ở phần 3 tái tạo đúng chính xác trường hợp ngoại lệ tinh tế này, không phải một phiên bản gần đúng hay bị lệch đi, là một kiểm chứng mạnh cho thấy phép star không phải một tương tự lỏng lẻo, mà là sự tổng quát hóa đúng đắn của infimal convolution, kể cả ở chi tiết biên khó chịu nhất của lý thuyết cổ điển.

## 7. Kết luận và hướng tiếp theo

Định lý ở phần 3 là một đẳng thức hình thức, đúng vô điều kiện ở mức preepi, không cần dùng đến các định lý A đến E về luật phân phối. Nội dung "khó" của lý thuyết fiber semiring cần thiết cho bước tiếp theo, không phải cho chính định lý này: ví dụ, chứng minh tính kết hợp của phép star, sự tồn tại phần tử trung hòa, hay điều kiện để lớp các hàm giá trị trong $\mathcal S$ cùng với phép star tạo thành một monoid, đều sẽ cần quay lại dùng cấu trúc semiring của $\mathcal S$ đã dựng ở các file trước.

Tóm tắt vị trí của kết quả này trong toàn bộ chương trình:

phép $\boxplus_{\mathrm{sp}}$ trên preepi, cảm sinh từ spatial sum, luôn tương ứng với phép star trên hàm giá trị-tập hợp, không điều kiện gì.

infimal convolution cổ điển là trường hợp riêng khi lớp giá trị là các tia đóng.

interval convolution, hay set-valued convolution tổng quát cho lớp $\mathcal S$ bất kỳ, đều được sinh ra theo cùng công thức, và câu hỏi còn mở là các tính chất đại số sâu hơn của phép star này trên từng lớp $\mathcal S$ cụ thể.
