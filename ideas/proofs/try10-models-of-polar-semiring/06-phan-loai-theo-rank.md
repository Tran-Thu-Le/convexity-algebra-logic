# Phân loại kernel theo hạng

## Mục tiêu và những gì cần chứng minh

Các file trước đã tích lũy một loạt quan sát chưa được chứng minh trọn vẹn: rằng $\tau$ trong điều kiện residual phải là một tác động; rằng họ $\tau_\varphi(p,q)=q+\varphi(p)$ thống nhất Fenchel ($\varphi=0$), kernel sai phân ($\varphi=-\mathrm{id}$) và phase semantics ($\varphi=\mathrm{id}$); rằng phép đổi biến hai phía chuyển sector theo $\varphi\mapsto B^{-1}\varphi A$; và rằng bất biến phân loại đúng là hạng của $\varphi$. File này chứng minh đầy đủ tất cả các khẳng định đó, đồng thời giải trọn vẹn phương trình residual trong từng sector, một kết quả mạnh hơn mọi thứ đã phát biểu trước đây: không chỉ biết sector nào chứa ví dụ nào, mà biết chính xác mọi phần tử của mỗi sector.

Cố định ký hiệu cho toàn file. $X$ là một nhóm giao hoán, viết theo lối cộng. Một kernel là một hàm $c:X\times X\to\mathbb R$. Với một ánh xạ $\tau:X\times X\to X$ cho trước, ta nói $c$ thuộc lớp $\mathcal K_\tau$ nếu tồn tại $\delta_c:X\times X\to\mathbb R$ sao cho

$$
c(p+r,\ q)=c\bigl(r,\ \tau(p,q)\bigr)+\delta_c(p,q)\qquad\forall\, p,q,r\in X. \tag{R}
$$

Như file 2 và file 5 đã thiết lập, mọi $c\in\mathcal K_\tau$ đều sinh nucleus trên $M=X\times\mathbb R$ với spatial sum thường. File này không lặp lại điều đó, mà phân loại chính các lớp $\mathcal K_\tau$.

## Bước một: tính không suy biến và luật tác động

Trước hết cần một khái niệm kỹ thuật, vì phương trình (R) tự nó không xác định $\tau$ duy nhất nếu kernel quá nghèo (chẳng hạn $c$ hằng số thuộc mọi $\mathcal K_\tau$).

Định nghĩa (không suy biến). Kernel $c$ gọi là không suy biến theo biến thứ hai nếu: hễ hàm $r\mapsto c(r,u)-c(r,u')$ là hằng số trên $X$ thì $u=u'$.

Kiểm tra nhanh cho các ví dụ mốc: với Fenchel $c(x,y)=\langle x,y\rangle$ trên $\mathbb R^n$, hiệu $c(r,u)-c(r,u')=\langle r,u-u'\rangle$ là hằng khi và chỉ khi $u=u'$, nên không suy biến. Với kernel sai phân $c=\psi(y-x)$, tính không suy biến tương đương với việc không có hai tịnh tiến khác nhau của $\psi$ sai khác một hằng số; điều này đúng cho $\psi$ toàn phương và cho $\psi$ "đại trà", nhưng sai cho $\psi$ affine. Với kernel indicator của phase semantics, nó tương đương việc pole $D$ phân biệt được các tịnh tiến của chính nó. Vậy không suy biến là giả thiết nhẹ nhưng không tự động; các kết quả duy nhất dưới đây cần nó, còn các kết quả cấu trúc thì không.

Bổ đề 1. Giả sử $c\in\mathcal K_\tau$ và $c$ không suy biến. Khi đó $\tau(0,q)=q$ và $\delta_c(0,q)=0$ với mọi $q$.

Chứng minh. Đặt $p=0$ trong (R): $c(r,q)=c(r,\tau(0,q))+\delta_c(0,q)$ với mọi $r$, tức $c(r,q)-c(r,\tau(0,q))$ là hằng số $\delta_c(0,q)$. Không suy biến cho $\tau(0,q)=q$, và thay lại được $\delta_c(0,q)=0$. $\blacksquare$

Định lý 1 (luật tác động). Giả sử $c\in\mathcal K_\tau$ và $c$ không suy biến. Khi đó với mọi $p_1,p_2,q$,

$$
\tau(p_1+p_2,\ q)=\tau\bigl(p_2,\ \tau(p_1,q)\bigr), \tag{A}
$$

$$
\delta_c(p_1+p_2,\ q)=\delta_c(p_1,q)+\delta_c\bigl(p_2,\ \tau(p_1,q)\bigr). \tag{C}
$$

Chứng minh. Tính $c(p_1+p_2+r,\ q)$ theo hai cách. Cách một, coi $p_1+p_2$ là một cú tịnh tiến duy nhất:

$$
c(p_1+p_2+r,\ q)=c\bigl(r,\ \tau(p_1+p_2,q)\bigr)+\delta_c(p_1+p_2,q).
$$

Cách hai, tịnh tiến bởi $p_1$ trước rồi $p_2$ sau, dùng (R) hai lần:

$$
c\bigl(p_1+(p_2+r),\ q\bigr)=c\bigl(p_2+r,\ \tau(p_1,q)\bigr)+\delta_c(p_1,q)=c\bigl(r,\ \tau(p_2,\tau(p_1,q))\bigr)+\delta_c\bigl(p_2,\tau(p_1,q)\bigr)+\delta_c(p_1,q).
$$

Hai vế phải bằng nhau với mọi $r$, nên hiệu $c\bigl(r,\tau(p_1+p_2,q)\bigr)-c\bigl(r,\tau(p_2,\tau(p_1,q))\bigr)$ là hằng theo $r$. Không suy biến cho (A), và khi hai đối số thứ hai đã trùng nhau, so sánh phần hằng cho (C). $\blacksquare$

Viết $q\cdot p:=\tau(p,q)$, thì (A) cùng Bổ đề 1 nói $q\cdot 0=q$ và $q\cdot(p_1+p_2)=(q\cdot p_1)\cdot p_2$: $\tau$ là một tác động phải của monoid $(X,+)$ lên tập $X$. Còn (C) là đồng nhất thức cocycle chuẩn của $\delta_c$ đối với tác động đó. Đây là điều đã phác thảo ở lượt thảo luận trước, giờ có chứng minh trọn vẹn. Điều rút ra: $\tau$ không phải tham số tự do; nó buộc phải mang cấu trúc tác động, và $\delta_c$ buộc phải là cocycle của tác động ấy.

Bổ đề 2 (đặc trưng dạng tịnh tiến). Giả sử $\tau$ là tác động phải thỏa Bổ đề 1 và Định lý 1, và giả sử thêm $\tau$ đẳng biến tịnh tiến theo biến thứ hai, nghĩa là $\tau(p,\ q+u)=\tau(p,q)+u$ với mọi $p,q,u$. Khi đó tồn tại $\varphi:X\to X$ cộng tính, tức $\varphi\in\mathrm{End}(X)$, sao cho

$$
\tau(p,q)=q+\varphi(p).
$$

Chứng minh. Đặt $\varphi(p):=\tau(p,0)$. Đẳng biến với $q=0$: $\tau(p,u)=\tau(p,0)+u=u+\varphi(p)$, cho đúng dạng cần. Luật tác động (A) áp lên dạng này: $q+\varphi(p_1+p_2)=\tau(p_1+p_2,q)=\tau(p_2,\tau(p_1,q))=q+\varphi(p_1)+\varphi(p_2)$, nên $\varphi$ cộng tính. $\blacksquare$

Ý nghĩa của giả thiết đẳng biến: phép cộng trên $M=X\times\mathbb R$ vốn có sẵn đối xứng tịnh tiến theo biến thứ hai (thay $q$ bởi $q+u$ chỉ tịnh tiến toàn cảnh); các sector tương thích với đối xứng có sẵn đó chính là các sector dạng $\tau_\varphi$. Từ đây trở đi ta cố định

$$
\tau_\varphi(p,q):=q+\varphi(p),\qquad \varphi\in\mathrm{End}(X),
$$

và viết gọn $\mathcal K_\varphi:=\mathcal K_{\tau_\varphi}$. Các tác động không đẳng biến nằm ngoài phạm vi phân loại của file này; điểm này sẽ nhắc lại ở phần giới hạn.

## Bước hai: giải trọn phương trình residual trong một sector

Kết quả sau đây mạnh và gọn một cách bất ngờ: nó tách mọi kernel trong $\mathcal K_\varphi$ thành hai phần độc lập, và đồng thời nhận diện $\delta_c$ là gì.

Định lý 2 (phân tách). Cho $\varphi\in\mathrm{End}(X)$. Một hàm $c:X\times X\to\mathbb R$ thuộc $\mathcal K_\varphi$ khi và chỉ khi nó có dạng

$$
c(x,y)=\psi\bigl(y+\varphi(x)\bigr)+h(x,y),
$$

trong đó $\psi:X\to\mathbb R$ tùy ý và $h:X\times X\to\mathbb R$ thỏa đồng nhất thức cocycle

$$
h(p+r,\ q)=h(p,q)+h\bigl(r,\ q+\varphi(p)\bigr)\qquad\forall\,p,q,r. \tag{Coc}
$$

Hơn nữa, khi đó $\delta_c=h$: số hạng hiệu chỉnh trong (R) chính là thành phần cocycle của kernel.

Chứng minh. Chiều thuận. Giả sử $c\in\mathcal K_\varphi$ với hiệu chỉnh $\delta_c$. Đặt $r=0$ trong (R):

$$
c(p,q)=c\bigl(0,\ q+\varphi(p)\bigr)+\delta_c(p,q).
$$

Đặt $\psi(u):=c(0,u)$ và $h(x,y):=c(x,y)-\psi\bigl(y+\varphi(x)\bigr)$; đẳng thức trên cho ngay $h=\delta_c$. Còn phải kiểm tra $h$ thỏa (Coc). Thay $c=\psi(y+\varphi(x))+h(x,y)$ vào (R):

$$
\psi\bigl(q+\varphi(p)+\varphi(r)\bigr)+h(p+r,q)=\psi\bigl(q+\varphi(p)+\varphi(r)\bigr)+h\bigl(r,q+\varphi(p)\bigr)+\delta_c(p,q),
$$

trong đó vế trái dùng $\varphi(p+r)=\varphi(p)+\varphi(r)$. Giản ước $\psi$ và thay $\delta_c=h$ được đúng (Coc).

Chiều ngược. Cho $\psi$ tùy ý, $h$ thỏa (Coc), đặt $c=\psi(y+\varphi(x))+h(x,y)$. Tính trực tiếp:

$$
c(p+r,q)=\psi\bigl(q+\varphi(p)+\varphi(r)\bigr)+h(p,q)+h\bigl(r,q+\varphi(p)\bigr)=c\bigl(r,\ q+\varphi(p)\bigr)+h(p,q),
$$

tức (R) đúng với $\delta_c=h$. $\blacksquare$

Chú ý nhỏ: (Coc) tự động kéo theo $h(0,q)=0$, vì đặt $p=r=0$ cho $h(0,q)=2h(0,q)$.

Định lý 2 trả lời trọn vẹn câu hỏi đã nêu ở tài liệu về phase semantics: những cặp $(\tau,\delta)$ nào cho phép tồn tại một kernel thỏa phương trình residual. Câu trả lời, trong phạm vi các sector đẳng biến:

Hệ quả (phân loại cặp chấp nhận được). Cặp $(\tau_\varphi,\delta)$ có ít nhất một kernel $c$ thỏa (R) khi và chỉ khi $\delta$ tự nó thỏa đồng nhất thức cocycle (Coc). Khi đó, tập tất cả các nghiệm là

$$
\bigl\{\,\psi\bigl(y+\varphi(x)\bigr)+\delta(x,y)\ :\ \psi:X\to\mathbb R\text{ tùy ý}\,\bigr\},
$$

một không gian affine mô hình trên không gian các hàm một biến $\psi$.

Vậy đúng như phỏng đoán ở tài liệu đó: primitive thật sự là cặp $(\varphi,\delta)$, gồm một tự đồng cấu chọn sector và một cocycle chọn "độ xoắn trọng số"; kernel chỉ là cặp ấy cộng thêm một bậc tự do $\psi$ hoàn toàn trơ, không ảnh hưởng gì đến cơ chế residual. Đối chiếu ba mốc: phase semantics chọn $(\mathrm{id},0)$ với $\psi=\chi$; kernel sai phân chọn $(-\mathrm{id},0)$ với $\psi$ là hàm khoảng cách; Fenchel chọn $(0,\ \langle p,q\rangle)$ với $\psi=0$, và kiểm tra được $\langle p,q\rangle$ đúng là cocycle của tác động tầm thường: $\langle p_1+p_2,q\rangle=\langle p_1,q\rangle+\langle p_2,q\rangle$, khớp (C) khi $\tau(p_1,q)=q$.

## Bước ba: cấu trúc của mọi cocycle

Định lý 2 quy toàn bộ việc mô tả $\mathcal K_\varphi$ về việc giải (Coc). Phần này giải trọn nó, bằng tay, không cần ngôn ngữ đối đồng điều, dù người đọc quen đại số đồng điều sẽ nhận ra ngay đây là tính toán $H^1$ của $(X,+)$ với hệ số trong module hàm trên $X$, và kết quả khớp với bổ đề Shapiro.

Cần vài ký hiệu. Ảnh $\mathrm{Im}\,\varphi$ là nhóm con của $X$; các quỹ đạo của tác động $q\mapsto q+\varphi(p)$ chính là các lớp kề $q+\mathrm{Im}\,\varphi$; ký hiệu $[q]\in X/\mathrm{Im}\,\varphi$ là nhãn quỹ đạo của $q$. Hạt nhân $\ker\varphi$ là nhóm ổn định của mọi điểm.

Định lý 3 (cấu trúc cocycle). Hàm $h:X\times X\to\mathbb R$ thỏa (Coc) khi và chỉ khi nó có dạng

$$
h(p,q)=\widetilde A_{[q]}(p)+\eta(q)-\eta\bigl(q+\varphi(p)\bigr),
$$

trong đó, với mỗi nhãn quỹ đạo $t\in X/\mathrm{Im}\,\varphi$, $\widetilde A_t:X\to\mathbb R$ là một đồng cấu cộng tính, và $\eta:X\to\mathbb R$ là một hàm tùy ý.

Chứng minh. Chiều ngược là kiểm tra trực tiếp: với $h$ có dạng trên,

$$
h(p+r,q)=\widetilde A_{[q]}(p+r)+\eta(q)-\eta\bigl(q+\varphi(p)+\varphi(r)\bigr),
$$

còn

$$
h(p,q)+h\bigl(r,q+\varphi(p)\bigr)=\widetilde A_{[q]}(p)+\eta(q)-\eta\bigl(q+\varphi(p)\bigr)+\widetilde A_{[q+\varphi(p)]}(r)+\eta\bigl(q+\varphi(p)\bigr)-\eta\bigl(q+\varphi(p)+\varphi(r)\bigr).
$$

Vì $[q+\varphi(p)]=[q]$ và $\widetilde A_t$ cộng tính, hai vế bằng nhau.

Chiều thuận, chia ba bước.

Bước a: phần hạt nhân của $h$ cộng tính và chỉ phụ thuộc quỹ đạo. Lấy $k\in\ker\varphi$ và $p\in X$ bất kỳ. Áp (Coc) cho cặp $(k,p)$ theo hai thứ tự:

$$
h(k+p,q)=h(k,q)+h\bigl(p,\ q+\varphi(k)\bigr)=h(k,q)+h(p,q),
$$

$$
h(p+k,q)=h(p,q)+h\bigl(k,\ q+\varphi(p)\bigr).
$$

So sánh (dùng $k+p=p+k$): $h(k,q)=h\bigl(k,q+\varphi(p)\bigr)$ với mọi $p$, tức $h(k,\cdot)$ hằng trên từng quỹ đạo. Ngoài ra, áp (Coc) cho $k_1,k_2\in\ker\varphi$: $h(k_1+k_2,q)=h(k_1,q)+h(k_2,q+\varphi(k_1))=h(k_1,q)+h(k_2,q)$. Vậy với mỗi quỹ đạo $t$, hàm

$$
A_t:=h(\cdot,\,q)\big|_{\ker\varphi}\quad(\text{với }q\text{ bất kỳ trong quỹ đạo }t)
$$

là một đồng cấu cộng tính $\ker\varphi\to\mathbb R$, xác định tốt.

Bước b: khử phần hạt nhân. Với mỗi $t$, chọn một mở rộng cộng tính $\widetilde A_t:X\to\mathbb R$ của $A_t$ từ $\ker\varphi$ lên toàn $X$. Mở rộng như vậy tồn tại: khi $X$ là không gian vector thực và $A_t$ tuyến tính, chỉ cần chọn một phần bù của $\ker\varphi$ và cho $\widetilde A_t$ triệt tiêu trên đó; với nhóm giao hoán tổng quát, $\mathbb R$ là nhóm chia được, do đó là $\mathbb Z$-module nội xạ theo tiêu chuẩn Baer, nên mọi đồng cấu từ nhóm con đều mở rộng được. Như đã kiểm ở chiều ngược, $(p,q)\mapsto\widetilde A_{[q]}(p)$ tự nó là một cocycle, nên

$$
h'(p,q):=h(p,q)-\widetilde A_{[q]}(p)
$$

vẫn thỏa (Coc), và theo bước a, $h'(k,q)=A_{[q]}(k)-A_{[q]}(k)=0$ với mọi $k\in\ker\varphi$: cocycle $h'$ triệt tiêu trên $\ker\varphi\times X$.

Bước c: cocycle triệt tiêu trên hạt nhân là một coboundary. Trên mỗi quỹ đạo $t$, chọn một điểm gốc $b_t$. Với $q$ thuộc quỹ đạo $t$, tồn tại $m$ với $q=b_t+\varphi(m)$; định nghĩa

$$
\eta(q):=-h'(m,\,b_t).
$$

Định nghĩa này không phụ thuộc cách chọn $m$: nếu $\varphi(m)=\varphi(m')$ thì $m'=m+k$ với $k\in\ker\varphi$, và

$$
h'(m+k,b_t)=h'(m,b_t)+h'\bigl(k,\ b_t+\varphi(m)\bigr)=h'(m,b_t)+0.
$$

Bây giờ kiểm tra $h'(p,q)=\eta(q)-\eta\bigl(q+\varphi(p)\bigr)$ với mọi $p,q$. Viết $q=b_t+\varphi(m)$; khi đó $q+\varphi(p)=b_t+\varphi(m+p)$, nên

$$
\eta\bigl(q+\varphi(p)\bigr)=-h'(m+p,\,b_t)=-h'(m,b_t)-h'\bigl(p,\ b_t+\varphi(m)\bigr)=\eta(q)-h'(p,q),
$$

trong đó bước giữa dùng (Coc) cho cặp $(m,p)$ tại gốc $b_t$. Chuyển vế được đúng đẳng thức cần. Gộp bước b và c: $h(p,q)=\widetilde A_{[q]}(p)+\eta(q)-\eta(q+\varphi(p))$. $\blacksquare$

Nhận xét về tính không duy nhất: phân tách trong Định lý 3 không duy nhất. Có thể cộng vào $\widetilde A_t$ bất kỳ đồng cấu nào triệt tiêu trên $\ker\varphi$, tức có dạng $B_t\circ\varphi$, rồi bù trừ vào $\eta$ (đây chính là nội dung ẩn của bước b: phần của $\widetilde A_t$ ngoài hạt nhân là coboundary); và $\eta$ tự do sai khác một hằng số trên mỗi quỹ đạo. Bất biến thật sự của $h$ là họ các hạn chế $A_t=\widetilde A_t|_{\ker\varphi}$, đúng như bổ đề Shapiro dự đoán: lớp đối đồng điều của cocycle được tham số hóa bởi $\mathrm{Hom}(\ker\varphi,\mathbb R)$ trên từng quỹ đạo.

## Bước bốn: định lý cấu trúc sector

Ghép Định lý 2 và Định lý 3:

Định lý 4 (mô tả trọn vẹn $\mathcal K_\varphi$). Cho $\varphi\in\mathrm{End}(X)$. Khi đó

$$
\mathcal K_\varphi=\Bigl\{\,c(x,y)=\psi\bigl(y+\varphi(x)\bigr)+\widetilde A_{[y]}(x)+\eta(y)\ :\ \psi,\eta:X\to\mathbb R\text{ tùy ý},\ \widetilde A_t\in\mathrm{Hom}(X,\mathbb R)\ \forall t\in X/\mathrm{Im}\,\varphi\,\Bigr\},
$$

trong đó số hạng $\eta(y)-\eta(y+\varphi(x))$ của Định lý 3 đã được hấp thụ: phần $-\eta(y+\varphi(x))$ gộp vào $\psi$, phần $\eta(y)$ giữ nguyên.

Đối chiếu với ba sector mốc, mỗi trường hợp thu lại đúng mô tả từng biết, cộng thêm phần tổng quát trước đây bị bỏ sót.

Sector $\varphi=0$. Ảnh bằng $\{0\}$, quỹ đạo là các điểm đơn lẻ, $[y]=y$, hạt nhân là toàn bộ $X$. Công thức cho

$$
c(x,y)=L_y(x)+\gamma(y),
$$

với $L_y:=\widetilde A_y$ cộng tính tùy ý theo $x$ và $\gamma:=\psi+\eta$ tùy ý theo $y$: chính xác lớp coupling affine theo biến thứ nhất, chứa Fenchel. Đây là sector duy nhất mà phần cocycle chiếm toàn bộ nội dung còn phần $\psi$ suy biến thành hàm một biến.

Sector $\varphi=-\mathrm{id}$. Hạt nhân bằng $0$ nên mọi $\widetilde A$ hấp thụ được (bước b của Định lý 3 với $\ker\varphi=0$ cho thấy toàn bộ cocycle là coboundary); một quỹ đạo duy nhất. Công thức cho

$$
c(x,y)=\psi(y-x)+\eta(y).
$$

Điểm đáng lưu ý: mô tả đầy đủ là kernel sai phân cộng một hàm chỉ phụ thuộc biến thứ hai, rộng hơn phát biểu "chỉ gồm $\psi(y-x)$" từng nêu ở lượt thảo luận trước; số hạng $\eta(y)$ đã bị bỏ sót ở đó và nay được phục hồi nhờ giải trọn phương trình.

Sector $\varphi=\mathrm{id}$. Tương tự, hạt nhân bằng $0$, một quỹ đạo, và

$$
c(x,y)=\chi(x+y)+\eta(y).
$$

Nếu đòi hỏi thêm quan hệ $\perp_c$ đối xứng, tức $c(x,y)=c(y,x)$, thì $\chi(x+y)+\eta(y)=\chi(x+y)+\eta(x)$ ép $\eta$ hằng, hấp thụ vào $\chi$: các nghiệm đối xứng đúng là $\chi(x+y)$, khớp khẳng định ở lượt trước, nhưng nay thấy rõ khẳng định ấy chỉ đúng trong lớp đối xứng, không đúng cho phương trình residual nói chung.

Mệnh đề (tính duy nhất của sector). Nếu $c$ không suy biến thì $c$ thuộc nhiều nhất một lớp $\mathcal K_\varphi$; nói cách khác, $\varphi$ được $c$ xác định duy nhất.

Chứng minh. Giả sử $c\in\mathcal K_\varphi\cap\mathcal K_{\varphi'}$. Trừ hai phiên bản của (R) cho cùng $p,q$: $c\bigl(r,q+\varphi(p)\bigr)-c\bigl(r,q+\varphi'(p)\bigr)=\delta'(p,q)-\delta(p,q)$, hằng theo $r$. Không suy biến cho $q+\varphi(p)=q+\varphi'(p)$ với mọi $p,q$, tức $\varphi=\varphi'$. $\blacksquare$

Với kernel suy biến, các sector giao nhau (mọi hàm chỉ phụ thuộc $y$ thuộc mọi $\mathcal K_\varphi$, như thấy ngay từ Định lý 4). Vì vậy phân loại dưới đây là phân loại các sector, không phải một phân hoạch của không gian tất cả các kernel; hai điều này chỉ trùng nhau trên phần không suy biến.

## Bước năm: đổi biến hai phía và định lý hạng

Từ đây lấy $X=\mathbb R^n$ và giới hạn ở các $\varphi$ tuyến tính (lưu ý: đồng cấu cộng tính $\mathbb R^n\to\mathbb R^n$ đo được thì tự động tuyến tính, nên hạn chế này chỉ loại các nghiệm phi đo được của phương trình Cauchy, không mất gì trong mọi ứng dụng giải tích).

Định lý 5 (đổi biến hai phía). Cho $A,B\in GL_n(\mathbb R)$ và $c\in\mathcal K_\varphi$. Đặt $c'(x,y):=c(Ax,\,By)$. Khi đó $c'\in\mathcal K_{\varphi'}$ với

$$
\varphi'=B^{-1}\varphi A,
$$

và ánh xạ $c\mapsto c'$ là một đẳng cấu tuyến tính $\mathcal K_\varphi\to\mathcal K_{B^{-1}\varphi A}$.

Chứng minh. Tính trực tiếp, dùng tính tuyến tính của $A$:

$$
c'(p+r,\,q)=c\bigl(Ap+Ar,\ Bq\bigr)=c\bigl(Ar,\ Bq+\varphi(Ap)\bigr)+\delta_c(Ap,Bq)=c\Bigl(Ar,\ B\bigl(q+B^{-1}\varphi A\,p\bigr)\Bigr)+\delta_c(Ap,Bq),
$$

vế phải bằng $c'\bigl(r,\ q+\varphi'(p)\bigr)+\delta_c(Ap,Bq)$, đúng dạng (R) với $\delta_{c'}(p,q)=\delta_c(Ap,Bq)$. Ánh xạ hiển nhiên tuyến tính, và nghịch đảo là đổi biến bởi $(A^{-1},B^{-1})$, đưa $\varphi'$ về $B\varphi'A^{-1}=\varphi$. $\blacksquare$

Định lý 6 (phân loại theo hạng). Trên $\mathbb R^n$, hai sector $\mathcal K_\varphi$ và $\mathcal K_{\varphi'}$ liên hệ với nhau bởi một phép đổi biến hai phía khi và chỉ khi $\mathrm{rank}\,\varphi=\mathrm{rank}\,\varphi'$. Do đó, sai khác đổi biến tuyến tính hai phía, có đúng $n+1$ sector, đánh số bởi $r\in\{0,1,\dots,n\}$, với đại diện

$$
\varphi_r:=-P_r,\qquad P_r=\mathrm{diag}(\underbrace{1,\dots,1}_{r},\,0,\dots,0).
$$

Chứng minh. Chiều cần: $A,B$ khả nghịch nên $\mathrm{rank}(B^{-1}\varphi A)=\mathrm{rank}\,\varphi$. Chiều đủ là dạng chuẩn hạng quen thuộc: cho $\varphi$ hạng $r$, chọn cơ sở $w_1,\dots,w_r$ của một phần bù của $\ker\varphi$ và $w_{r+1},\dots,w_n$ cơ sở của $\ker\varphi$; các ảnh $\varphi(w_1),\dots,\varphi(w_r)$ độc lập tuyến tính, bổ sung thành cơ sở $u_1,\dots,u_n$ của không gian đích. Gọi $A$ là ma trận đổi từ cơ sở chuẩn sang $(w_i)$ và $B$ đổi từ cơ sở chuẩn sang $(-u_i)$; khi đó $B^{-1}\varphi A=-P_r$. Hai tự đồng cấu cùng hạng thì cùng tương đương với $-P_r$, nên tương đương với nhau. $\blacksquare$

Việc chọn dấu trừ trong đại diện chỉ là quy ước để sector hạng đầy đủ mang bộ mặt kernel sai phân quen thuộc; như đã thấy, $P_r$ và $-P_r$ tương đương hai phía qua $B=\mathrm{diag}(-I_r,I_{n-r})$.

Hệ quả tức thời, giải quyết dứt điểm hai câu hỏi treo từ các lượt trước. Thứ nhất, $\varphi=\mathrm{id}$ và $\varphi=-\mathrm{id}$ cùng hạng $n$ nên cùng sector sai khác đổi biến: phép đổi biến tường minh là $(A,B)=(\mathrm{id},-\mathrm{id})$, tức $c'(x,y)=c(x,-y)$, biến $\chi(x+y)$ thành $\chi(x-y)$; phase semantics và kernel sai phân là một, sai khác quy ước dấu ở biến đối ngẫu. Thứ hai, $\varphi=0$ có hạng $0$, tách tuyệt đối khỏi hạng $n$ dưới mọi đổi biến hai phía: không tồn tại phép đổi biến tuyến tính nào đưa sector Fenchel về sector sai phân, và đây là lý do cấu trúc khiến tổng của một kernel Fenchel với một kernel sai phân trên cùng các biến rơi ra ngoài cả hai sector, như phản ví dụ $\langle p,q\rangle+\tfrac12\|p-q\|^2$ đã minh họa bằng tính toán.

Riêng về ràng buộc đối xứng: nếu đòi mọi phép đổi biến bảo toàn thêm tính đối xứng $c(x,y)=c(y,x)$, lớp đổi biến được phép thu hẹp về dạng chéo $A=B$, quan hệ tương đương trở thành liên hợp $\varphi\mapsto A^{-1}\varphi A$, và bất biến mịn hơn hạng, gồm cả dữ liệu phổ. Trong khung đó, $\mathrm{id}$ và $-\mathrm{id}$ lại tách nhau, phản ánh đúng ghi chú ở lượt trước rằng phép $y\mapsto-y$ chỉ khớp phần $\chi$ chẵn của phía phase với phía sai phân. Vậy có hai bài toán phân loại song song, ứng với hai nhóm đối xứng: nhóm hai phía cho bài toán residual thuần túy, bất biến là hạng; nhóm chéo cho bài toán residual cộng đối xứng, bất biến mịn hơn và chưa được giải trọn ở đây.

## Bước sáu: các sector lai và phép tổng trực tiếp

Định lý 6 nói rằng ngoài hai thái cực $r=0$ và $r=n$, còn $n-1$ sector trung gian chưa từng xuất hiện trong bất kỳ ví dụ nào trước đây của dự án. Định lý 4 cho phép viết chúng ra tường minh. Lấy đại diện $\varphi=-P_r$, tách tọa độ $x=(x_1,x_2)\in\mathbb R^r\oplus\mathbb R^{n-r}$, tương tự cho $y$. Khi đó $y+\varphi(x)=(y_1-x_1,\ y_2)$, hạt nhân là khối $x_2$, ảnh là khối thứ nhất, nhãn quỹ đạo là $y_2$. Định lý 4, với quy tắc $\widetilde A$ chỉ mang nội dung trên hạt nhân và giả thiết đo được để các đồng cấu thành tuyến tính, cho

$$
c(x,y)=\psi\bigl(y_1-x_1,\ y_2\bigr)+\bigl\langle a(y_2),\,x_2\bigr\rangle+\eta(y),
$$

với $\psi:\mathbb R^r\times\mathbb R^{n-r}\to\mathbb R$, $a:\mathbb R^{n-r}\to\mathbb R^{n-r}$, $\eta:\mathbb R^n\to\mathbb R$ đều tùy ý. Đọc cấu trúc này: một kernel kiểu khoảng cách trên $r$ tọa độ đầu, có tham số trượt theo $y_2$; một coupling kiểu Fenchel trên $n-r$ tọa độ cuối, với "gradient suy rộng" phi tuyến $a$; và phần trơ $\eta$. Sector lai là đúng nghĩa lai ghép của hai lý thuyết mốc, mỗi lý thuyết chiếm một khối tọa độ.

Ví dụ cụ thể gọn nhất, lấy $\psi(u_1,y_2)=\tfrac12\|u_1\|^2$, $a(y_2)=y_2$, $\eta=0$:

$$
c(x,y)=\tfrac12\|y_1-x_1\|^2+\langle x_2,\,y_2\rangle.
$$

Kernel này đối xứng, không suy biến, sinh nucleus vì thuộc $\mathcal K_{-P_r}$, và không thuộc sector thuần nào khi $0<r<n$: một ví dụ mới thật sự, nửa toàn phương nửa Fenchel, mà các file trước chưa có công cụ để nhận ra là hợp lệ.

Hiện tượng lai ghép này là trường hợp riêng của một quy tắc calculus tổng quát, bổ sung vào danh sách các phép toán bảo toàn tính sinh nucleus:

Mệnh đề (tổng trực tiếp theo khối biến độc lập). Nếu $c_1\in\mathcal K_{\varphi_1}$ trên $X_1$ và $c_2\in\mathcal K_{\varphi_2}$ trên $X_2$, thì

$$
c\bigl((x_1,x_2),(y_1,y_2)\bigr):=c_1(x_1,y_1)+c_2(x_2,y_2)
$$

thuộc $\mathcal K_{\varphi_1\oplus\varphi_2}$ trên $X_1\oplus X_2$, với $\delta_c=\delta_{c_1}+\delta_{c_2}$.

Chứng minh. Cộng hai phương trình (R) thành phần, các biến không giao thoa. $\blacksquare$

Đặt cạnh kết quả âm ở tài liệu trước, bức tranh calculus trở nên cân đối: không thể trộn hai sector khác nhau trên cùng một bộ biến (vì hạng là bất biến tách biệt), nhưng trộn tự do trên các khối biến độc lập; và tham số $r$ của phân loại đếm chính xác số phương "kiểu sai phân" so với số phương "kiểu Fenchel". Nói cách khác, sai khác đổi biến hai phía, mọi sector đều là sector của một tổng trực tiếp

$$
(\text{lý thuyết sai phân})^{\oplus r}\oplus(\text{lý thuyết Fenchel})^{\oplus(n-r)},
$$

và thang $n+1$ bậc của Định lý 6 chính là thang nội suy rời rạc giữa hai lý thuyết mốc.

## Giới hạn trung thực của phân loại

Bốn điều chưa được giải quyết trong file này, ghi rõ để không tạo ảo giác trọn vẹn.

Thứ nhất, toàn bộ phân loại nằm trong phạm vi các tác động đẳng biến tịnh tiến, tức dạng $\tau_\varphi$; Bổ đề 2 biện minh vì sao lớp này tự nhiên, nhưng các tác động phải không đẳng biến của $(X,+)$ lên $X$ chưa được xét, và có thể chứa các sector mới.

Thứ hai, phân loại là của các sector, không phải của các kernel: phần suy biến (chẳng hạn các hàm chỉ phụ thuộc $y$) thuộc nhiều sector cùng lúc, và Mệnh đề duy nhất chỉ áp dụng cho kernel không suy biến.

Thứ ba, điều kiện (R) là điều kiện đủ cho nucleus, không phải cần; tiêu chuẩn cần và đủ vẫn là điều kiện đóng của các lát cắt trong Theorem A của file 2. Hoàn toàn có thể tồn tại kernel sinh nucleus mà không thuộc bất kỳ $\mathcal K_\varphi$ nào; phân loại ở đây phủ phần "có cơ chế residual", chưa phủ phần "nucleus vì lý do khác".

Thứ tư, bài toán phân loại trong lớp đối xứng, với nhóm đổi biến chéo và bất biến liên hợp mịn hơn hạng, mới chỉ được nhận diện chứ chưa giải; đây là ứng viên tự nhiên cho một file tiếp theo.

## Bảng kết luận

$$
\begin{array}{c|c|c|c}
\text{Hạng }r\text{ của }\varphi & \text{Đại diện} & \text{Thành viên tổng quát của sector} & \text{Lý thuyết mốc}\\
\hline
0 & \varphi=0 & L_y(x)+\gamma(y) & \text{Fenchel, coupling affine}\\
n & \varphi=-\mathrm{id} & \psi(y-x)+\eta(y) & \text{kernel sai phân; phase semantics qua }y\mapsto-y\\
0<r<n & \varphi=-P_r & \psi(y_1-x_1,y_2)+\langle a(y_2),x_2\rangle+\eta(y) & \text{lai: sai phân}^{\oplus r}\oplus\text{Fenchel}^{\oplus(n-r)}
\end{array}
$$

Và chuỗi kết quả chống đỡ bảng này: luật tác động và cocycle của $\delta$ (Định lý 1) buộc $\tau$ có cấu trúc; phân tách $c=\psi+h$ với $\delta_c=h$ (Định lý 2) tách phần trơ khỏi phần mang nội dung, đồng thời phân loại các cặp $(\tau,\delta)$ chấp nhận được; cấu trúc cocycle (Định lý 3) giải trọn phần mang nội dung; đổi biến hai phía và dạng chuẩn hạng (Định lý 5, 6) rút gọn vô hạn sector về $n+1$ lớp; và phép tổng trực tiếp cho thấy $n+1$ lớp ấy là thang nội suy giữa đúng hai lý thuyết nguyên thủy, giải tích lồi kiểu Fenchel ở một đầu và hình học sai phân, cũng là phase semantics, ở đầu kia.
