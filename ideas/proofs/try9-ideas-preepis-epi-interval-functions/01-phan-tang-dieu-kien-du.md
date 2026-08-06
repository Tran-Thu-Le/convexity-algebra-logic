# Phân tầng sum phân phối lên giao trên R

Ký hiệu $A+B = \{a+b : a\in A, b\in B\}$ là tổng Minkowski trên $\mathbb R$. Mỗi khối dưới đây là một câu hỏi, kèm câu trả lời, suy luận, và điều kiện được thêm vào để dẫn tới câu hỏi kế tiếp.

---

## Câu hỏi 1

| Mục | Nội dung |
|---|---|
| Câu hỏi | Trên họ các tập con tùy ý của R: $A+(B\cap C) = (A+B)\cap(A+C)$ với mọi A, B, C? |
| Chứng minh/Phản ví dụ | Sai. $A=\{0,1\}$, $B=\{0\}$, $C=\{1\}$: $B\cap C = \varnothing$ nên $A+(B\cap C)=\varnothing$, nhưng $(A+B)\cap(A+C) = \{1\}$. |
| Suy luận | Nguyên nhân là $B\cap C=\varnothing$, nhưng mỗi tổng riêng lẻ vẫn có thể giao nhau nhờ dùng các phần tử khác nhau của A. |
| Điều kiện thêm | Thêm giả thiết $B\cap C \ne \varnothing$, chuyển sang câu hỏi 2. |

---

## Câu hỏi 2

| Mục | Nội dung |
|---|---|
| Câu hỏi | Trên họ tập con tùy ý của R, với $B\cap C \ne \varnothing$: $A+(B\cap C)=(A+B)\cap(A+C)$? |
| Chứng minh/Phản ví dụ | Không rõ nói chung, có thể sai với tập không lồi (ví dụ tập rời rạc hoặc tập kiểu Cantor), do thiếu cấu trúc thứ tự để kiểm soát phần tử biên. |
| Suy luận | Nếu sai, nguyên nhân nghi ngờ là thiếu tính lồi: các phần tử của $A+B$ và $A+C$ có thể trùng nhau một cách tình cờ, không đến từ một phần tử chung của $B\cap C$. |
| Điều kiện thêm | Giới hạn về lớp các khoảng, chuyển sang câu hỏi 3. |

---

## Câu hỏi 3

| Mục | Nội dung |
|---|---|
| Câu hỏi | A tùy ý, I, J là khoảng, $I\cap J \ne \varnothing$: $A+(I\cap J)=(A+I)\cap(A+J)$? |
| Chứng minh/Phản ví dụ | Đúng khi I, J là đoạn đóng hoặc tia đóng. Cần xét riêng khoảng mở và nửa mở. |
| Suy luận | Nghi vấn nằm ở loại đầu mút: đóng thì kiểm soát được qua max, min hữu hạn; mở thì cần kiểm tra riêng, đặc biệt ở giao vô hạn. |
| Điều kiện thêm | Tách hai nhánh: đoạn đóng, câu hỏi 4a; khoảng mở, câu hỏi 4b. |

---

## Câu hỏi 4a

| Mục | Nội dung |
|---|---|
| Câu hỏi | A là khoảng, I, J là đoạn đóng hoặc tia đóng, $I\cap J\ne\varnothing$: $A+(I\cap J)=(A+I)\cap(A+J)$? |
| Chứng minh/Phản ví dụ | Đúng, đây là trường hợp hai tập của Định lý B bên dưới. |
| Suy luận | Đầu mút đóng cho phép dùng max, min hữu hạn, được phép cộng bảo toàn. |
| Điều kiện thêm | Mở rộng lên họ hữu hạn tùy ý, rồi họ vô hạn, câu hỏi 5a. |

---

## Câu hỏi 4b

| Mục | Nội dung |
|---|---|
| Câu hỏi | A là khoảng, I, J là khoảng mở, $I\cap J \ne \varnothing$: $A+(I\cap J)=(A+I)\cap(A+J)$, cho họ hữu hạn? |
| Chứng minh/Phản ví dụ | Đúng cho họ hữu hạn. |
| Suy luận | Với số lượng hữu hạn, sup và inf liên quan chỉ là max, min hữu hạn, hiện tượng giới hạn chưa xuất hiện, nên tính mở của đầu mút chưa gây vấn đề. |
| Điều kiện thêm | Mở rộng lên họ vô hạn, câu hỏi 5b. |

---

## Câu hỏi 5a

| Mục | Nội dung |
|---|---|
| Câu hỏi | A là đoạn đóng hoặc tia đóng hoặc R, họ tùy ý $\{I_\lambda\}$ các đoạn đóng, $\bigcap_\lambda I_\lambda \ne \varnothing$: $A+\bigcap_\lambda I_\lambda = \bigcap_\lambda(A+I_\lambda)$? |
| Chứng minh/Phản ví dụ | Đúng, đây là Định lý C bên dưới. |
| Suy luận | Lớp đoạn đóng đóng dưới giao vô hạn khác rỗng, phép dịch bảo toàn sup và inf, đầu mút luôn đạt được. |
| Điều kiện thêm | Thay đoạn đóng bằng tia đóng, câu hỏi 6; hoặc gộp cả hai thành lớp lồi đóng tổng quát, câu hỏi 7. |

---

## Câu hỏi 5b

| Mục | Nội dung |
|---|---|
| Câu hỏi | A là khoảng mở, họ vô hạn $\{I_\lambda\}$ khoảng mở, $\bigcap_\lambda I_\lambda \ne \varnothing$: $A+\bigcap_\lambda I_\lambda = \bigcap_\lambda(A+I_\lambda)$? |
| Chứng minh/Phản ví dụ | Sai. Phản ví dụ: $A=(0,1)$, $I_n = (-1/n, 1/n)$. Khi đó $\bigcap_n I_n = \{0\}$, một tập đóng, không còn mở. $A+\{0\}=(0,1)$, nhưng $A+I_n = (-1/n, 1+1/n)$, và $\bigcap_n(A+I_n) = [0,1]$. |
| Suy luận | Hai nguyên nhân đồng thời: lớp khoảng mở không đóng dưới giao vô hạn, giao có thể suy biến; và đầu mút xuất hiện ở giới hạn mà không thuộc bất kỳ tổng thành phần nào theo một phân tích chung. |
| Điều kiện thêm | Câu hỏi rẽ nhánh: liệu điều kiện lớp tập đóng dưới giao vô hạn có phải là điều kiện quyết định, câu hỏi 6''. |

---

## Câu hỏi 6

| Mục | Nội dung |
|---|---|
| Câu hỏi | A là đoạn đóng hoặc tia đóng, họ tùy ý $\{U_\lambda = [b_\lambda,\infty)\}$ các tia đóng: $A+\bigcap_\lambda U_\lambda = \bigcap_\lambda(A+U_\lambda)$? |
| Chứng minh/Phản ví dụ | Đúng, không cần thêm giả thiết giao khác rỗng, vì trên $\overline{\mathbb R}$ giao của tia đóng luôn khác rỗng hoặc bằng rỗng một cách nhất quán ở cả hai vế. |
| Suy luận | Tia đóng đóng dưới giao vô hạn một cách tự động, sup được bảo toàn qua phép dịch với hằng số hữu hạn. |
| Điều kiện thêm | Gộp với câu hỏi 5a thành lớp lồi đóng tổng quát, câu hỏi 7. |

---

## Câu hỏi 6''

| Mục | Nội dung |
|---|---|
| Câu hỏi | Nếu lớp $\mathcal F$ đóng dưới giao tùy ý và phép dịch bảo toàn sup, inf của các đầu mút thuộc lớp đó, thì $\mathcal F$ có luôn cho phân phối vô hạn không? |
| Chứng minh/Phản ví dụ | Chưa có phản ví dụ nào phá vỡ giả thuyết này trong các lớp đã xét; khoảng mở thất bại chính ở điều kiện đầu tiên, tính đóng dưới giao vô hạn. |
| Suy luận | Gợi ý rằng ba điều kiện, đóng dưới giao, bảo toàn sup/inf, và đầu mút đạt được, là bộ điều kiện đủ mấu chốt. |
| Điều kiện thêm | Kiểm chứng bằng lớp cụ thể lớn nhất: lồi và đóng, câu hỏi 7. |

---

## Câu hỏi 7, câu hỏi thống nhất

| Mục | Nội dung |
|---|---|
| Câu hỏi | Gọi $\mathcal C$ là lớp mọi tập con lồi và đóng của R, gồm đoạn đóng, tia đóng, R, tập một điểm, và rỗng. Với A thuộc $\mathcal C$ và họ tùy ý $\{I_\lambda\}\subseteq \mathcal C$, $\bigcap_\lambda I_\lambda \ne \varnothing$, có phải $A+\bigcap_\lambda I_\lambda = \bigcap_\lambda(A+I_\lambda)$? |
| Chứng minh/Phản ví dụ | Đúng, đây là Định lý E bên dưới, hợp nhất từ Định lý C và Định lý D. |
| Suy luận | Mọi tập lồi đóng viết được thành giao của một tia đóng trên và một tia đóng dưới, áp dụng Định lý D cho từng phía rồi giao lại. |
| Điều kiện thêm | Câu hỏi mở còn lại: khoảng nửa mở có đạt tính chất này dưới điều kiện yếu hơn hay không, chưa được giải quyết ở đây. |

---

## Bảng tổng hợp các định lý điều kiện đủ

| Định lý | Lớp tập | Giao | Điều kiện | Kết luận |
|---|---|---|---|---|
| A | Tùy ý | Hữu hạn, hai tập | $B\cap C \ne \varnothing$, cộng thêm điều kiện lồi | Đúng |
| B | Đoạn đóng, tia đóng | Hữu hạn | $\bigcap \ne \varnothing$ | Đúng |
| C | Đoạn đóng | Vô hạn | $\bigcap \ne \varnothing$ | Đúng |
| D | Tia đóng | Vô hạn | tự động trên $\overline{\mathbb R}$ | Đúng |
| E | Lồi đóng, mọi dạng | Vô hạn tùy ý | $\bigcap \ne \varnothing$ | Đúng, tổng quát nhất |

---

## Phát biểu các định lý

Định lý A. Cho A tùy ý và B, C là khoảng với $B\cap C \ne \varnothing$. Khi đó $A+(B\cap C) = (A+B)\cap(A+C)$.

Định lý B. Cho A là khoảng, tùy ý loại đầu mút, và $I_1,\dots,I_n$ là đoạn đóng hoặc tia đóng với $\bigcap_{k=1}^n I_k \ne \varnothing$. Khi đó

$$
A+\bigcap_{k=1}^n I_k = \bigcap_{k=1}^n (A+I_k).
$$

Định lý C. Cho $A=[a,b]$, hoặc tia đóng, hoặc R, và họ tùy ý $\{I_\lambda = [c_\lambda,d_\lambda]\}_{\lambda\in\Lambda}$ các đoạn đóng với $\bigcap_\lambda I_\lambda \ne \varnothing$. Khi đó

$$
A + \bigcap_\lambda I_\lambda = \bigcap_\lambda (A+I_\lambda).
$$

Định lý D. Cho A là đoạn đóng hoặc tia đóng, và họ tùy ý $\{U_\lambda = [b_\lambda,\infty)\}_{\lambda\in\Lambda}$ các tia đóng, xét trên $\overline{\mathbb R}$. Khi đó

$$
A+\bigcap_\lambda U_\lambda = \bigcap_\lambda (A+U_\lambda),
$$

không cần thêm giả thiết giao khác rỗng.

Định lý E. Gọi $\mathcal C$ là lớp mọi tập con lồi và đóng của R, gồm đoạn đóng, tia đóng, R, tập một điểm, và rỗng. Cho $A \in \mathcal C$ và họ tùy ý $\{I_\lambda\}_{\lambda\in\Lambda} \subseteq \mathcal C$ với $\bigcap_\lambda I_\lambda \ne \varnothing$. Khi đó

$$
A+\bigcap_\lambda I_\lambda = \bigcap_\lambda (A+I_\lambda),
$$

và hơn nữa $A+\bigcap_\lambda I_\lambda$ vẫn thuộc $\mathcal C$.

## Ranh giới đã xác định bằng phản ví dụ

| Vi phạm điều kiện nào | Phản ví dụ | Kết luận |
|---|---|---|
| Bỏ giao khác rỗng | $A=\{0,1\}$, $B=\{0\}$, $C=\{1\}$ | Sai |
| Bỏ tính đóng, giao vô hạn của khoảng mở | $A=(0,1)$, $I_n = (-1/n,1/n)$ | Sai |
| Bỏ tính đóng, giao vô hạn của tia mở | $A=(0,\infty)$, $U_n = (-1/n,\infty)$ | Sai |

Điều kiện đủ tổng quát nhất đã xác lập là Định lý E: lồi, đóng, và giao của cả họ, hữu hạn hay vô hạn, khác rỗng. Đây là điều kiện đủ, câu hỏi về tính cần thiết đối với khoảng nửa mở vẫn còn bỏ ngỏ.
