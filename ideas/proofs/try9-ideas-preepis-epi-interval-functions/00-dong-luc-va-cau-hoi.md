# Động lực và câu hỏi hình học

## 1. Xuất phát điểm: một đẳng thức sơ cấp về hàm số

Với ba hàm số thực f, g, h trên cùng một miền, ta luôn có đẳng thức sau, đúng vô điều kiện:

$$
f + \max(g,h) = \max(f+g,\ f+h).
$$

Đây là sự kiện sơ cấp: cộng một hàm cố định vào hai vế của một phép lấy max không làm thay đổi hàm nào lớn hơn tại từng điểm, nên thứ tự được bảo toàn theo từng điểm một.

Câu hỏi tự nhiên: có đẳng thức tương tự cho min hay không?

$$
f + \min(g,h) \;\overset{?}{=}\; \min(f+g,\ f+h).
$$

Chiều $\le$ luôn đúng, cùng lý do như trên. Nhưng chiều ngược lại nói chung sai: nếu g đạt min tại một điểm còn h đạt min tại điểm khác, phép cộng f có thể làm đảo thứ tự giữa hai giá trị min cục bộ đó.

Kết luận sơ cấp: phép cộng phân phối vô điều kiện lên max, nhưng chỉ phân phối có điều kiện lên min. Đây là hạt giống của toàn bộ bài toán tập hợp trình bày dưới đây.

## 2. Chuyển sang ngôn ngữ tập hợp: epigraph

Với một hàm g, xét epigraph của nó, tập các điểm nằm trên hoặc trên đồ thị:

$$
\mathrm{epi}(g) = \{(x,t) : t \ge g(x)\}.
$$

Hai sự kiện hình học cơ bản:

$$
\mathrm{epi}(\max(g,h)) = \mathrm{epi}(g) \cap \mathrm{epi}(h),
$$

$$
\mathrm{epi}(\min(g,h)) = \mathrm{epi}(g) \cup \mathrm{epi}(h).
$$

Lý do: một điểm nằm trên đồ thị của max(g,h) khi và chỉ khi nó nằm trên cả hai đồ thị, tức thuộc cả hai epigraph, tức thuộc giao. Một điểm nằm trên đồ thị của min(g,h) khi và chỉ khi nó nằm trên ít nhất một trong hai đồ thị, tức thuộc hợp.

Cộng một hàm f vào g tương ứng với việc dịch chuyển từng fiber của epigraph theo tọa độ t, tại mỗi x cố định lấy tổng Minkowski của fiber đó với fiber của f. Đây chính là fiber sum.

Đẳng thức sơ cấp ban đầu, qua phép dịch này, trở thành hai câu hỏi hình học song song.

Câu hỏi dễ, tương ứng với min và hợp:

$$
A \boxplus (\mathrm{epi}(g) \cup \mathrm{epi}(h)) \;\overset{?}{=}\; (A \boxplus \mathrm{epi}(g)) \cup (A \boxplus \mathrm{epi}(h)).
$$

Câu hỏi khó, tương ứng với max và giao:

$$
A \boxplus (\mathrm{epi}(g) \cap \mathrm{epi}(h)) \;\overset{?}{=}\; (A \boxplus \mathrm{epi}(g)) \cap (A \boxplus \mathrm{epi}(h)).
$$

Đẳng thức $f + \max(g,h) = \max(f+g,f+h)$ nói rằng, trên các fiber là tia đóng dạng $[g(x),\infty)$, câu hỏi khó luôn đúng. Câu hỏi trung tâm: điều này còn đúng đến đâu khi thay tia đóng bằng các lớp tập con tổng quát hơn của R.

## 3. Hai phép cộng của tập hợp

Với E, F là tập con của $X \times K$, có hai phép cộng tự nhiên:

spatial sum, ký hiệu $\boxplus_{\mathrm{sp}}$, cộng cả tọa độ không gian x lẫn tọa độ giá trị.

fiber sum, ký hiệu $\boxplus_{\mathrm{fib}}$, chỉ cộng tọa độ giá trị, giữ nguyên tọa độ không gian, tức cộng riêng trong từng fiber.

## 4. Phần dễ: spatial sum phân phối lên hợp tùy ý

Đây là sự kiện hoàn toàn tổng quát, không cần điều kiện gì:

$$
A \boxplus_{\mathrm{sp}} \Big(\bigcup_{i\in I} B_i\Big) = \bigcup_{i\in I} \big(A \boxplus_{\mathrm{sp}} B_i\big).
$$

Lý do thuần túy logic: một điểm thuộc vế trái khi và chỉ khi nó có một biểu diễn dùng một phần tử thuộc ít nhất một $B_i$ nào đó, đây chính xác là định nghĩa của hợp. Không cần lồi, không cần đóng, không cần topology, không cần giao khác rỗng, đúng cho hợp hữu hạn lẫn vô hạn.

## 5. Phần khó: fiber sum và câu hỏi giao

Câu hỏi còn lại, khó hơn nhiều, là bản Minkowski sum trên từng fiber, một tập con của R:

$$
A + \bigcap_{i} I_i \;\overset{?}{=}\; \bigcap_{i} (A+I_i).
$$

Chiều $\subseteq$ luôn đúng một cách hiển nhiên, giống chiều dễ của bất đẳng thức min ở phần 1:

$$
A + \bigcap_{i} I_i \;\subseteq\; \bigcap_{i} (A+I_i).
$$

Chiều ngược lại nói chung sai, y hệt hiện tượng min ở phần 1.

Điều này dẫn tới bài toán con trung tâm của toàn bộ khảo sát:

phân tầng các lớp tập con của R, theo mức độ tổng quát của điều kiện đủ, để đẳng thức trên đúng, trước hết cho giao hữu hạn, sau đó cho giao tùy ý.

Bài toán con này được giải quyết trong file thứ hai, phân tầng điều kiện đủ trên R, và các định lý được chứng minh chi tiết trong file thứ ba.
