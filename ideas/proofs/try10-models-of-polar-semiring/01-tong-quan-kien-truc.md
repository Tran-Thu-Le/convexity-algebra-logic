# Polar Semiring: Tổng quan kiến trúc

## Câu hỏi xuất phát

Có một hiện tượng lặp đi lặp lại trong toán học mà thoạt nhìn tưởng là trùng hợp. Trong giải tích lồi, phép liên hợp Fenchel biến hàm lồi thành hàm lồi, và phép cộng infimal convolution tương thích với phép cộng thường qua liên hợp. Trong logic tuyến tính, ngữ nghĩa pha (phase semantics) có một quan hệ trực giao sinh ra đúng cấu trúc cần thiết để tensor đi xuống được lớp các "facts". Trong giải tích idempotent (max-plus), một cơ chế tương tự lại xuất hiện. Ba câu chuyện này được kể bằng ba ngôn ngữ khác nhau, nhưng có một khung xương chung bên dưới.

Dự án này đặt câu hỏi: khung xương chung đó là gì, và điều kiện tối thiểu nào trên dữ liệu nguyên thủy khiến hiện tượng ấy xảy ra?

Câu trả lời hóa ra rất gọn. Chỉ cần hai thứ trên một tập $M$: một phép cộng $+$, và một quan hệ đối xứng $\perp$. Từ hai thứ ấy, một cách hoàn toàn máy móc, ta xây được một đại số bốn phép toán với đối ngẫu hoàn hảo. Điều kiện duy nhất cần kiểm tra, gọi là điều kiện nucleus, hóa ra lại có một đặc trưng cần và đủ ở ngay mức phần tử của $M$, không cần nhắc gì đến tập hợp.

## Ba tầng của bức tranh

Toàn bộ câu chuyện đi qua ba tầng, và mỗi tầng là chủ đề của một file riêng trong dự án này.

Tầng phần tử. Dữ liệu chỉ là $(M, +, \perp)$. Đây là nơi mọi trực giác thực sự nằm ở đó: khi nào một quan hệ "tương thích" với một phép cộng theo nghĩa đủ mạnh để cỗ máy phía sau chạy được. File thứ hai của dự án dành trọn cho tầng này, và đó là phần có nội dung toán học sâu nhất: một định lý đặc trưng ba điều kiện tương đương, một loạt ví dụ mẫu (Fenchel, kernel toàn phương, phase semantics), và một phản ví dụ cho thấy trực giác "hiển nhiên" nhất lại sai.

Tầng tập hợp. Từ $(M, +, \perp)$, lấy $S = \mathcal P(M)$, ta được một cấu trúc đại số trên các tập con: một phép hợp đóng vai trò join, một phép cộng Minkowski đóng vai trò tensor, và một phép lấy polar sinh ra từ $\perp$. Đây là nơi ngôn ngữ giải tích lồi (tập lồi đóng, hàm liên hợp) và ngôn ngữ đại số (semiring, closure operator) gặp nhau.

Tầng thương và tầng regular. Dưới điều kiện nucleus đã kiểm tra ở tầng phần tử, quan hệ "có cùng bipolar" trở thành một quan hệ tương đương tương thích với toàn bộ cấu trúc đại số, tức một congruence. Lớp thương theo quan hệ này lại đẳng cấu với lớp các tập "đóng" (regular), và trên lớp đóng, phép lấy polar trở thành một involution nghịch biến, từ đó nhân đôi số phép toán qua công thức De Morgan. Kết quả cuối cùng là một polar semiring hoàn chỉnh. File thứ ba của dự án dựng toàn bộ quá trình này từng bước.

## Sơ đồ tổng thể

$$
(M,+,\perp)
\ \xrightarrow{\ \mathcal P(-)\ }\
\bigl(S,\ \vee,\ \otimes,\ {}^*\bigr)
\ \xrightarrow{\ c=(-)^{**}\ }\
S_c
\ \xrightarrow{\ \text{De Morgan}\ }\
\mathbb S_c=(S_c,\ \vee_c,\ \wedge_c,\ \otimes_c,\ \oplus_c,\ {}^*)
$$

Mũi tên đầu tiên là hoàn toàn miễn phí: bất kỳ $(M,+,\perp)$ nào cũng cho ra một semiring có polarity trên $S$. Mũi tên thứ hai đòi hỏi một điều kiện, gọi là điều kiện nucleus, và đây là chốt chặn duy nhất của toàn bộ câu chuyện. Mũi tên thứ ba lại một lần nữa miễn phí, thuần túy là hệ quả hình thức của việc polarity là một involution.

Nói cách khác, toàn bộ độ khó của bài toán dồn vào đúng một câu hỏi: khi nào phép cộng ở tầng phần tử "đi xuống" được qua closure sinh bởi $\perp$? Đây chính là nội dung của file thứ hai.

## Vì sao đáng làm ở mức trừu tượng này

Có một cám dỗ tự nhiên là làm việc trực tiếp trên $\mathbb R^n \times \mathbb R$ với tích vô hướng, vì đó là nơi ta có trực giác giải tích lồi vững nhất. Nhưng làm vậy che khuất mất điều thật sự đang vận hành. Chứng minh gốc cho định lý Fenchel dùng đến tính song tuyến tính của tích vô hướng để "tách ngân sách" $s = s_A + s_B$. Khi viết lại ở mức trừu tượng, thao tác tách ngân sách ấy lộ ra bản chất của nó: nó chỉ là một phép residuation, tức tồn tại phần tử $x \backslash y$ sao cho $(x+m) \perp y \iff m \perp (x \backslash y)$. Một khi đã thấy điều này, kernel toàn phương $\varphi(p,q) = \tfrac12\|p-q\|^2$ cũng thỏa mãn đúng cơ chế ấy, dù không hề tuyến tính, không hề lồi theo nghĩa cần thiết cho song tuyến tính. Phase semantics của logic tuyến tính cũng vậy, dù ở đó không có gì giống tích vô hướng cả.

Tóm lại, làm việc ở mức trừu tượng không phải là một trò chơi hình thức, mà là cách duy nhất để thấy ba câu chuyện tưởng như khác nhau thực ra là một câu chuyện, và để nhận ra phạm vi áp dụng thật sự của kết quả.

## Kết quả chính, phát biểu ngắn gọn

Với $(M,+)$ là monoid giao hoán và $\perp$ là quan hệ đối xứng trên $M$, ba điều sau tương đương:

Điều kiện nucleus ở tầng tập hợp: $c(A) \otimes c(B) \subseteq c(A \otimes B)$ với mọi $A, B \subseteq M$, trong đó $c(A) = A^{**}$.

Điều kiện phản xạ kiểu Day ở tầng tập hợp: với mọi $x \in M$ và mọi tập đóng $C$, tập tịnh tiến ngược $x \to C = \{m : x + m \in C\}$ cũng đóng.

Điều kiện ở tầng phần tử: với mọi $x, y \in M$, tập $D_{x,y} = \{m : (x+m) \perp y\}$ là một tập polar.

Sự tương đương giữa ba điều này là nội dung của định lý trung tâm, trình bày chi tiết trong file thứ hai. Điều kiện thứ ba, tuy phát biểu ở mức tập hợp, chỉ nói về hành vi của $\perp$ khi ta tịnh tiến một biến, nên có thể kiểm tra trực tiếp trên từng cặp phần tử $x, y$ mà không cần lượng hóa trên mọi tập con. Đây là ý nghĩa của cụm từ element-to-set lifting: mọi thông tin cần thiết ở tầng tập hợp đã nằm sẵn ở tầng phần tử, chỉ cần biết đọc đúng chỗ.

## Cách đọc ba file

File thứ hai nên đọc trước, vì nó chứa nội dung toán học nặng nhất và là nơi trực giác được xây dựng. File thứ ba giả sử định lý ở file thứ hai đã có sẵn, và tập trung vào việc dựng cấu trúc đại số tầng tập hợp cho đến polar semiring hoàn chỉnh, với trọng tâm là cơ chế De Morgan sinh ra bốn phép toán từ hai phép toán nguyên thủy. File này, file thứ nhất, chỉ đóng vai trò bản đồ, để người đọc không lạc giữa các tầng.

Một câu duy nhất để mang theo khi đọc hai file còn lại: closure tạo ra lớp thương, nucleus đưa đại số xuống được lớp thương, và involution nhân đôi số phép toán trên lớp thương ấy.
