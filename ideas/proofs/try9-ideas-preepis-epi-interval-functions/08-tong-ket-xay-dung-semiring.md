# Tổng kết: xây dựng S là idempotent commutative semiring trên K

## 1. Nhắc lại tiên đề

Cho K là một monoid giao hoán (thường có thêm thứ tự tương thích). Một họ $S\subseteq\mathcal P(K)$ là một idempotent commutative semiring dưới $(\cap,+)$, theo nghĩa hữu hạn hoặc tùy ý, nếu:

đóng dưới giao (hữu hạn hoặc tùy ý, tùy phạm vi đang xét) khi giao khác rỗng,

đóng dưới cộng Minkowski,

luật phân phối $A+\bigcap_i L_i = \bigcap_i(A+L_i)$ đúng khi giao khác rỗng.

Toàn bộ phần dưới đây tổng hợp lại mọi cách đã tìm được để xây một S như vậy, chia theo hai trục: khi các phần tử của S là khoảng của R (hoặc $\overline{\mathbb R}$), và khi mở rộng ra K tổng quát hoặc ra ngoài dạng khoảng.

---

## 2. Trục thứ nhất: S gồm các khoảng của R, đặc trưng hóa qua cặp (A,B)

### 2.1. Nguyên lý tách biến

Mỗi khoảng đóng $[a,b]\in\mathcal C$ tương ứng một cặp $(a,b)$, và

$$
[a_1,b_1]\cap[a_2,b_2] = [\max(a_1,a_2),\min(b_1,b_2)], \qquad [a_1,b_1]+[a_2,b_2]=[a_1+a_2,b_1+b_2].
$$

Đầu trái chỉ tương tác với $\max$ và $+$; đầu phải chỉ tương tác với $\min$ và $+$, hoàn toàn tách biệt. Vì vậy với

$$
S = \{[a,b] : a\in A,\ b\in B,\ a\le b\},
$$

tính hợp lệ của S quy đúng về hai câu hỏi độc lập một chiều: A có đóng dưới $\sup$ tùy ý và dưới $+$ không, B có đóng dưới $\inf$ tùy ý và dưới $+$ không.

### 2.2. Định lý đặc trưng hóa cho A (đối xứng cho B qua đổi dấu, đổi sup thành inf)

A hợp lệ khi và chỉ khi A là một tập con topologically đóng của $\overline{\mathbb R}$ (tức đóng dưới $\sup$ tùy ý), đồng thời là một nửa nhóm con cộng của $(\overline{\mathbb R},+)$ (đóng dưới $+$).

Chiều đủ đã kiểm chứng cho mọi ví dụ dưới đây. Chiều cần đã kiểm chứng chặt cho các cấu trúc dạng tia (lập luận $2s\le s\Rightarrow s\le0$), nhưng chưa có một chứng minh tổng quát bao trùm mọi tập con đóng bất kỳ; đây vẫn là một giả thuyết mạnh, không phải định lý đã đóng.

### 2.3. Danh mục các A cụ thể đã kiểm chứng

Tia xuống $(-\infty,c]$ với $c\le0$: kiểm tra trực tiếp $a,a'\le c \Rightarrow a+a'\le 2c\le c$.

Tia lên $[c,\infty)$ với $c\ge0$: $a,a'\ge c \Rightarrow a+a' \ge 2c\ge c$.

Lưới đều một phía $\{0,-\delta,-2\delta,\dots\}$ với $\delta>0$: tổng hai bội số vẫn là bội số, đóng theo tôpô vì rời rạc và giảm dần về $-\infty$.

Lưới đều hai phía $\delta\mathbb Z$ (mọi bội số của $\delta$, cả âm lẫn dương): tổng hai bội số của $\delta$ vẫn là bội số của $\delta$; đóng theo tôpô vì rời rạc, không có điểm tụ. Đây là một ví dụ chưa nêu trước đó, tổng quát hơn lưới một phía.

Hỗn hợp rời rạc dán vào tia, ví dụ

$$
A=(-\infty,-k\delta]\cup\{0,-\delta,\dots,-(k-1)\delta\}:
$$

phần rời rạc cộng với nhau hoặc rơi lại vào chính nó, hoặc rơi thẳng vào tia khi vượt ngưỡng $-k\delta$, không có khe hở; phần tia cộng với bất kỳ phần tử nào cũng rơi vào tia.

Trường hợp suy biến: $A=\{0\}$, $A=\varnothing$, $A=\overline{\mathbb R}$ (hoặc $(-\infty,0]$, $[0,\infty)$ toàn phần) đều là trường hợp riêng của các mục trên.

### 2.4. Vì sao "chứa 0" hay "chứa $\infty$" không phải điều kiện cần

Ví dụ tia lên $[5,\infty)$ ($c=5\ge0$) không chứa 0. Ví dụ lưới một phía $\{-1,-2,-3,\dots\}$ không chứa 0. Điều kiện thật sự là dấu của ngưỡng (hay dấu của bước nhảy sinh ra nửa nhóm), tương đối so với 0, chứ không phải bản thân 0 có mặt trong tập hay không. "Chứa 0" chỉ là trường hợp riêng khi ngưỡng bằng đúng 0; "chứa $\infty$" chỉ là trường hợp riêng khi A không bị chặn.

---

## 3. Trục thứ hai: mở rộng ra ngoài R, ba nguyên lý độc lập

### 3.1. Kéo lùi qua đồng cấu monoid tách được thành tích

Nếu $K\cong K_0\times\overline{\mathbb R}$ và $\varphi$ là phép chiếu lên thành phần $\overline{\mathbb R}$, thì $S_\varphi=\{\varphi^{-1}(I):I\in\mathcal C\}$ là semiring, kéo lùi nguyên vẹn từ trường hợp R. Áp dụng lặp lại cho $K=\overline{\mathbb R}^n$ cho ra lớp hộp trục tọa độ, một ví dụ mới, không quy về trường hợp một chiều.

Ranh giới: nếu bỏ cấu trúc tích, dùng lớp lồi đóng tổng quát của $\mathbb R^2$, luật phân phối sai (phản ví dụ đĩa đơn vị và hai nửa mặt phẳng vuông góc, đã kiểm tra bằng tọa độ cụ thể tại điểm $(-1,-1)$).

### 3.2. Thay R bằng một nhóm sắp thứ tự toàn phần đầy đủ Dedekind

Chứng minh của các định lý về khoảng chỉ dùng thứ tự toàn phần, phép cộng đơn điệu bảo toàn sup/inf, và tính đầy đủ Dedekind, không dùng gì riêng của R. Vậy $K=\mathbb Z$ với lớp đoạn đóng của Z hoạt động nguyên vẹn.

Ranh giới: $K=\mathbb Q$ thất bại ở giao vô hạn, vì Q không đầy đủ Dedekind (ví dụ hội tụ về $\sqrt2$, giao của một dãy đoạn đóng hữu tỷ giảm dần không còn là đoạn đóng của Q).

### 3.3. Giới hạn xuống semiring con qua phần tử trung hòa

Với $(K,S)$ bất kỳ đã có sẵn cấu trúc, $S_0=\{L\in S: 0_K\in L\}$ luôn là một semiring con thật sự (đóng dưới cả hai phép, vì $0_K+0_K=0_K$), độc lập với hai nguyên lý trên, áp dụng được cho bất kỳ K nào có phần tử trung hòa.

---

## 4. Ví dụ hoàn toàn khác loại, không thuộc dạng khoảng: lớp ghép nhóm con

Cố định một nhóm con $H\le(\mathbb R,+)$, ví dụ $H=\mathbb Z$, đặt $S_H=\{H+t : t\in\mathbb R\}\cup\{\varnothing\}$. Vì các lớp ghép khác nhau luôn rời nhau, giao khác rỗng ép mọi lớp ghép trong họ phải trùng nhau, khiến luật phân phối đúng gần như tự động; cộng hai lớp ghép cho ra một lớp ghép khác vì $H+H=H$. Đây là một idempotent commutative semiring hợp lệ, nhưng mỗi phần tử của nó là một tập rời rạc, không lồi, không liên thông, hoàn toàn không thuộc dạng $[a,b]$ nào cả, và không quy về khung (A,B) ở mục 2.

Điểm cần lưu ý trung thực: ví dụ này thỏa tiên đề semiring theo kiểu suy biến (luật phân phối đúng chỉ vì giả thiết giao khác rỗng ép các tập bằng nhau), khác về bản chất với các khoảng ở mục 2, nơi hai tập có thể giao nhau một phần mà không trùng nhau và luật phân phối vẫn phải được kiểm chứng thật sự.

---

## 5. Bảng tổng hợp toàn bộ

| Loại cấu trúc | K | S | Giao | Trạng thái |
|---|---|---|---|---|
| Tia đúng dấu | $\overline{\mathbb R}$ | $(A,B)$ với A, B là tia | Tùy ý | Đúng |
| Lưới đều một hoặc hai phía | $\overline{\mathbb R}$ | $(A,B)$ dạng $\delta\mathbb Z$ hoặc nửa lưới | Tùy ý | Đúng |
| Hỗn hợp rời rạc dán tia | $\overline{\mathbb R}$ | $(A,B)$ dạng hybrid | Tùy ý | Đúng |
| Hộp trục tọa độ | $\overline{\mathbb R}^n$ | tích các khoảng theo tọa độ | Tùy ý | Đúng, kéo lùi qua phép chiếu |
| Đoạn đóng của Z | $\mathbb Z$ | $\mathcal C(\mathbb Z)$ | Tùy ý | Đúng, đầy đủ rời rạc |
| Semiring con qua $0_K$ | K bất kỳ | $S_0\subseteq S$ | theo phạm vi của S | Đúng, tự động |
| Lớp ghép nhóm con | $\mathbb R$ | $\{H+t\}$ | Tùy ý | Đúng, nhưng suy biến, không lồi |
| Lồi đóng tổng quát nhiều chiều | $\mathbb R^2$ | mọi tập lồi đóng | Hữu hạn | Sai, phản ví dụ đĩa |
| Đoạn đóng của Q | $\mathbb Q$ | $\mathcal C(\mathbb Q)$ | Vô hạn | Sai, thiếu đầy đủ Dedekind |

---

## 6. Câu hỏi còn mở, chưa đóng lại

Chứng minh đầy đủ chiều cần của Định lý 2.2 (mọi A hợp lệ nhất thiết là tập đóng và nửa nhóm con cộng, không có cách nào khác để thỏa luật phân phối).

Phân loại đầy đủ các A hợp lệ có cấu trúc rời rạc tích lũy vô hạn về một điểm giới hạn trước khi thành tia (chưa kiểm tra trường hợp này, chỉ mới kiểm tra rời rạc hữu hạn dán vào tia).

Tính cụ thể pushout của hai semiring cụ thể (ví dụ $S_0$ và semiring qua tia $[c,\infty)$) trong phạm trù semiring, và kiểm tra pushout đó có nhúng lại thành một họ khoảng nhận dạng được trong $\mathcal P(\overline{\mathbb R})$ hay không; hiện chỉ biết pushout tồn tại một cách trừu tượng (vì lớp semiring là một variety đại số), chưa tính cụ thể.

Đặc trưng hóa đầy đủ (không chỉ ví dụ) cho các S không thuộc dạng khoảng, tương tự lớp ghép nhóm con ở mục 4, tức phân loại mọi idempotent commutative semiring trên $(\mathbb R,+)$ không cần giả thiết các phần tử là tập lồi hay liên thông.
