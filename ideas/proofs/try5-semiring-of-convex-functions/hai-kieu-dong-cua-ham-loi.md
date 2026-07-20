# Hai kiểu "đóng" của hàm lồi: khi trực giác hình học đánh lừa bạn

Có một niềm tin âm thầm mà hầu hết những ai học giải tích lồi đều mang theo, kể cả sau khi đã làm quen với Fenchel conjugate, subgradient, đối ngẫu Lagrange: rằng "hàm lồi đóng" là một khái niệm *duy nhất*, và ba cách mô tả nó — hình học (epigraph không có "lỗ hổng"), tô-pô (nửa liên tục dưới), và đại số (bất biến qua phép lấy đối ngẫu hai lần) — chỉ là ba cách nói khác nhau của cùng một sự thật.

Bài viết này chỉ ra rằng niềm tin đó **sai**, và sai theo một cách khá thú vị: một trong ba mô tả kia *mạnh hơn hẳn* hai cái còn lại, và khoảng cách giữa chúng không phải là lỗi kỹ thuật vặt vãnh — nó là lý do vì sao giáo trình giải tích lồi phải nhét thêm từ "proper" vào gần như mọi định lý quan trọng.

---

## 1. Bốn tính chất, và hai cách gộp chúng lại

Cho $f:\mathbb R^n\to\overline{\mathbb R}=[-\infty,+\infty]$ là một hàm bất kỳ (chưa giả sử gì). Xét bốn tính chất sau, tất cả đều nhìn qua lăng kính epigraph $\operatorname{epi}(f):=\{(x,r): r\ge f(x)\}$:

- **(U) — Upward theo thớ.** Nếu $r\in\operatorname{epi}(f)$ tại $x$ và $r'\ge r$ thì $(x,r')$ cũng thuộc epigraph.
- **(C) — Lồi.** $\operatorname{epi}(f)$ là tập lồi trong $\mathbb R^n\times\mathbb R$.
- **(T) — Đóng tô-pô.** $\operatorname{epi}(f)$ là tập đóng — tương đương $f$ nửa liên tục dưới (lsc).
- **(B) — Đóng-bipolar.** $f=f^{**}$, tức $f$ bằng chính đối ngẫu Fenchel của đối ngẫu Fenchel của nó:
$$f^*(y):=\sup_{x}\big(\langle x,y\rangle-f(x)\big),\qquad f^{**}(x):=\sup_y\big(\langle x,y\rangle-f^*(y)\big).$$

Lưu ý (U) thật ra tự động đúng với **mọi** hàm — đó chỉ là định nghĩa của epigraph, không phải một ràng buộc thật sự. Vậy hai định nghĩa "đóng" tự nhiên nhất mà người ta có thể viết ra là:

$$\textbf{UCT-đóng} :\iff (U)\wedge(C)\wedge(T)\qquad\text{và}\qquad\textbf{Bipolar-đóng} :\iff (B).$$

UCT-đóng là định nghĩa "hình học/tô-pô": lồi, và epigraph không hở. Bipolar-đóng là định nghĩa "đại số": bất động dưới phép lấy đối ngẫu hai lần — phiên bản hàm học của một sự kiện quen thuộc trong lý thuyết Galois connection (đóng = ảnh của chính phép đóng).

Câu hỏi tự nhiên: hai định nghĩa này có tương đương không?

## 2. Một chiều thì đúng — miễn phí, không cần lồi có sẵn

**Định lý.** Nếu $f=f^{**}$ (bipolar-đóng) thì $f$ tự động thỏa (U), (C), (T).

Chứng minh gần như không cần làm gì: (U) tự động đúng như đã nói. Còn $f^{**}(x)=\sup_y\big(\langle x,y\rangle-f^*(y)\big)$ là **supremum của một họ hàm affine theo $x$** — với mỗi $y$ cố định, $x\mapsto\langle x,y\rangle-f^*(y)$ là affine (hệ số $-f^*(y)$ có thể là $\pm\infty$, không sao, hàm affine suy biến vẫn lồi và lsc). Sup của một họ hàm lồi-lsc luôn lồi-lsc, vì epigraph của sup chính là **giao** các epigraph thành phần — mà mỗi epigraph thành phần ở đây là một nửa-không-gian affine (đóng, lồi), và giao của các tập lồi đóng vẫn lồi đóng. Vì $f=f^{**}$, hàm $f$ thừa hưởng cả (C) lẫn (T).

Nói cách khác: bất cứ hàm nào là bipolar của một hàm khác đều tự động có hình dạng "giao của các nửa-không-gian tựa nó" — và hình dạng ấy tự động lồi, tự động không hở. Chiều này miễn phí, không viện dẫn bất cứ giả thiết bổ sung nào.

## 3. Chiều ngược lại — và một phản ví dụ khá bất ngờ

Vấn đề nằm ở chiều còn lại: UCT-đóng có suy ra bipolar-đóng không? Trực giác nói có — "lồi + không hở" nghe như đã đủ để đảm bảo hàm "khớp hoàn hảo" với đối ngẫu kép của nó. Nhưng xét ví dụ sau, với $n=1$:

$$f(x):=\begin{cases}-\infty & \text{nếu } x\in[0,1]\\ +\infty & \text{nếu } x\notin[0,1]\end{cases}$$

Kiểm ba tính chất:

- **(U)**: tự động, như luôn.
- **(C)**: $\operatorname{epi}(f)=[0,1]\times\mathbb R$ — tích của hai tập lồi, nên lồi. ✓
- **(T)**: $[0,1]\times\mathbb R$ là tích của hai tập đóng trong $\mathbb R$, nên đóng trong $\mathbb R\times\mathbb R$. ✓

Vậy $f$ **UCT-đóng hoàn toàn hợp lệ**: lồi, epigraph đóng, không có gì đáng ngờ về mặt hình học hay tô-pô.

Nhưng thử tính đối ngẫu: với bất kỳ $y$, chọn $x_0\in[0,1]$ bất kỳ, ta có $f^*(y)\ge\langle x_0,y\rangle-f(x_0)=\langle x_0,y\rangle-(-\infty)=+\infty$. Vậy $f^*\equiv+\infty$ **với mọi $y$**. Từ đó $f^{**}(x)=\sup_y(\langle x,y\rangle-\infty)=-\infty$ — với **mọi** $x$, không riêng gì $x\in[0,1]$.

Kết quả: $f^{**}\equiv-\infty$, trong khi $f$ lại bằng $+\infty$ ở khắp nơi ngoài $[0,1]$. Rõ ràng $f^{**}\ne f$. **(B) thất bại**, dù (U), (C), (T) đều thỏa mãn không sót gì.

### Vì sao trực giác hình học "lừa" ta ở đây

Nhìn epigraph của $f$: nó là một dải đứng $[0,1]\times\mathbb R$ — một tập lồi đóng hoàn toàn bình thường theo con mắt hình học thuần túy. Nhưng phép lấy đối ngẫu hai lần chỉ "nhìn thấy" hàm qua **các nửa-không-gian tựa nó từ bên dưới** (affine minorant). Vấn đề là: một dải đứng vô hạn theo chiều $r$ không có nửa-không-gian tựa nào khác ngoài hàm hằng $-\infty$ — bởi vì bất kỳ affine minorant thật sự nào (độ dốc hữu hạn) đều sẽ tiến ra $-\infty$ khi $x$ chạy dọc theo dải, nhưng lại phải $\ge f(x)=+\infty$ ngay khi $x$ ra khỏi $[0,1]$ — điều không hàm affine nào làm được trừ khi bản thân nó đã là $-\infty$ (một dạng suy biến).

Nói cách khác, tập bipolar chỉ "thấy" hình dạng $-\infty$ ở phần trong, và vì không có affine minorant nào phân biệt được phần trong với phần ngoài $[0,1]$, bipolar-closure san phẳng toàn bộ thành hằng $-\infty$ — mất sạch thông tin về việc $f=+\infty$ bên ngoài đoạn $[0,1]$.

## 4. Kết luận Phần 1: bao hàm thật sự, không phải tương đương

$$\{\text{Bipolar-đóng}\}\ \subsetneq\ \{\text{UCT-đóng}\}.$$

Bao hàm là *thật sự*, không phải bằng nhau — ví dụ ở mục 3 là chứng cứ. Nói theo ngôn ngữ dàn ý ban đầu: đóng-bipolar là một điều kiện **mạnh hơn hẳn**, không phải một cách phát biểu khác của cùng một khái niệm.

---

## 5. Rockafellar đã "né" khoảng cách này như thế nào

Nếu bipolar-đóng mạnh hơn UCT-đóng, thì phát biểu "$f$ lồi, $f$ đóng $\Rightarrow f^{**}=f$" — thứ mà bất kỳ ai học giải tích lồi cũng từng nghe qua dưới tên "định lý Fenchel–Moreau" — hẳn phải có một điều kiện ẩn nào đó chưa nói ra. Và đúng là có.

Trước tiên, một định lý khác, đơn giản hơn nhiều, giải thích chính xác *tại sao* ví dụ ở mục 3 thất bại ở (B):

**Định lý (suy biến toàn cục).** Nếu $f=f^{**}$ và tồn tại một điểm $x_0$ với $f(x_0)=-\infty$, thì $f\equiv-\infty$ trên toàn bộ $\mathbb R^n$.

*Chứng minh.* $f(x_0)=-\infty$ kéo theo, với mọi $y$: $f^*(y)\ge\langle x_0,y\rangle-(-\infty)=+\infty$, nên $f^*\equiv+\infty$. Từ đó $f^{**}(x)=\sup_y(\langle x,y\rangle-\infty)=-\infty$ với **mọi** $x$ (không chỉ $x_0$). Vì $f=f^{**}$, suy ra $f\equiv-\infty$ khắp nơi. $\blacksquare$

Chứng minh này không dùng gì đến lồi, tô-pô, hay các định lý tách tập lồi — thuần túy là đại số của phép $\sup$. Nó cho biết: **nếu** một hàm là bipolar-đóng và có dù chỉ một điểm $-\infty$, hàm đó buộc phải là hằng số $-\infty$ toàn cục — không có kiểu "vừa $-\infty$ ở chỗ này vừa $+\infty$ ở chỗ khác" như ví dụ mục 3. Đảo lại: chính vì ví dụ mục 3 vi phạm kết luận này (nó có điểm $-\infty$ mà không hằng số), nó **buộc phải** không bipolar-đóng — khớp đúng những gì ta đã tính tay ở trên, nhưng giờ có lý do cấu trúc rõ ràng thay vì chỉ là một phép tính.

### "Proper" — hàng rào định nghĩa, không phải hệ quả logic

Đây là chỗ Rockafellar thực hiện một bước đi khéo léo. Ông định nghĩa:

$$f \text{ proper} :\iff f(x)>-\infty\ \ \forall x\ \ \wedge\ \ f\not\equiv+\infty.$$

Và khi phát biểu "hàm lồi đóng", ông không nói "lồi + epigraph đóng" một cách trần trụi — ông định nghĩa nó là: **proper + lsc**, hoặc là hằng số $\equiv+\infty$, hoặc là hằng số $\equiv-\infty$ (đúng ba trường hợp, không hơn). Hàm ở ví dụ mục 3 — có điểm $-\infty$ nhưng không phải hằng số toàn cục, và cũng không proper — **không thuộc bất kỳ trường hợp nào trong ba trường hợp đó**. Nó bị loại khỏi phạm vi nghiên cứu bằng chính định nghĩa, trước khi câu hỏi "nó có $f^{**}=f$ không" kịp được đặt ra.

Điều quan trọng cần nhấn mạnh: đây **không phải** một định lý kiểu "mọi hàm lồi đóng tô-pô đều tự động rơi vào một trong ba trường hợp trên" — mệnh đề đó **sai**, và ví dụ mục 3 chính là phản chứng. Đây là một **quyết định định nghĩa**: Rockafellar chọn nghiên cứu đúng phạm vi mà (B) và (UCT) trùng nhau, và đặt tên cho phạm vi ấy là "đóng". Cái giá phải trả (một cách âm thầm, hiếm khi được nói thành lời trong giáo trình) là: tồn tại những hàm lồi có epigraph đóng hoàn toàn hợp lệ về mặt hình học, nhưng bị loại khỏi lý thuyết chỉ vì chúng "vừa $-\infty$ vừa không hằng số".

## 6. Định lý chính, phát biểu đúng phạm vi của nó

Gộp lại, ta có phát biểu chính xác của cái mà mọi người quen gọi tắt là "Fenchel–Moreau":

**Định lý.** Với $f$ **proper**: $f$ lồi và nửa liên tục dưới $\iff$ $f=f^{**}$.

Hai chiều của định lý này có "trọng lượng" rất khác nhau:

- **Chiều $(\Leftarrow)$**, từ bipolar-đóng suy ra lồi + lsc, là chiều **miễn phí** — đã chứng minh nguyên vẹn ở mục 2, không cần proper, không cần gì thêm. Proper ở đây chỉ đơn giản là thu hẹp phạm vi áp dụng, không đóng góp gì vào chứng minh.

- **Chiều $(\Rightarrow)$**, từ lồi + lsc suy ra bipolar-đóng, mới là nội dung *sâu* thật sự của Fenchel–Moreau — nó cần định lý tách tập lồi (một dạng Hahn–Banach hữu hạn chiều): nếu $f^{**}(x_0)<f(x_0)$ tại một điểm nào đó, ta tách điểm $(x_0,\beta)$ (với $\beta$ nằm giữa hai giá trị đó) ra khỏi epigraph đóng lồi của $f$ bằng một siêu phẳng, siêu phẳng ấy cho ra chính xác một affine minorant "vượt quá" giá trị $f^{**}(x_0)$ đang giả sử — mâu thuẫn.

  Và đây chính là chỗ giả thiết **proper thật sự cần thiết**: nếu $f$ không proper — tức nếu $f$ có một điểm $-\infty$ mà không phải hằng số toàn cục — thì lập luận tách bị hỏng ngay từ bước đầu, vì không có gì đảm bảo tồn tại một siêu phẳng tách "sạch sẽ" khi epigraph chứa cả điểm $-\infty$ lẫn vùng $+\infty$ đan xen kiểu ví dụ mục 3. Chính ví dụ đó — vốn dĩ là phản chứng cho chiều $(\Rightarrow)$ khi bỏ giả thiết proper — cho thấy proper không phải điều kiện thừa thãi được thêm vào cho gọn, mà là điều kiện *thật sự cần* để định lý tách hoạt động.

## 7. Vậy rút ra được gì?

Ba điều đáng nhớ:

1. **"Đóng" trong giải tích lồi không phải một khái niệm — nó là hai khái niệm, một hình học/tô-pô (UCT) và một đại số (bipolar), trong đó đại số mạnh hơn hẳn.** Chiều mạnh-hơn này (bipolar ⟹ UCT) hoàn toàn miễn phí, không cần một định lý sâu nào — chỉ là sự kiện "sup của các hàm affine luôn lồi và nửa liên tục dưới".

2. **Khoảng cách giữa hai khái niệm ấy được lấp bằng một quyết định định nghĩa** — từ "proper" — chứ không phải bằng một định lý chứng minh chúng tự động trùng nhau. Nhiều giáo trình lướt qua điều này quá nhanh, khiến người học có cảm giác proper chỉ là một tính từ kỹ thuật vô hại, trong khi thực ra nó đang âm thầm cắt bỏ hẳn một lớp hàm — những hàm "vừa $-\infty$ cục bộ vừa không hằng số" — ra khỏi lý thuyết.

3. **Cái giá thật sự của định lý Fenchel–Moreau nằm đúng ở chiều khó** (lồi+lsc ⟹ bipolar), và chính giả thiết proper là thứ khiến định lý tách tập lồi áp dụng được sạch sẽ. Chiều dễ thì miễn phí đến mức gần như không đáng gọi là một phần của "định lý" — nó chỉ là quan sát rằng bipolar luôn có dạng giao của các nửa-không-gian.

Lần tới khi thấy dòng "vì $f$ lồi, đóng, proper, nên $f^{**}=f$", có lẽ đáng dừng lại một giây để nhớ rằng ba tính từ "lồi", "đóng", "proper" không đứng cạnh nhau một cách ngẫu nhiên — "proper" đang âm thầm gánh phần việc nặng nhất.
