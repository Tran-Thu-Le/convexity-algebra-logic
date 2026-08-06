# Điều kiện cộng tính của liên hợp tổng quát: một khung thuần tối ưu (v3, phần 2)

## 1. Giới thiệu

File này viết lại toàn bộ nội dung trung tâm của dự án — điều kiện cần-và-đủ để phép lấy bao đóng (bipolar closure/liên hợp kép) tương thích với phép cộng tập hợp (tổng Minkowski nâng) — bằng ngôn ngữ thuần giải tích lồi/tối ưu hóa. Không dùng thuật ngữ đại số trừu tượng (monoid, quantale), không dùng ngôn ngữ logic (quan hệ $\perp$, phép kéo theo), không dùng ngôn ngữ lý thuyết phạm trù (internal hom, adjunction).

Toàn bộ cấu trúc được sinh từ một dữ liệu nguyên thủy duy nhất: một **hàm ghép cặp** (coupling function) $\kappa$, đóng vai trò tổng quát hóa của hàm liên hợp song tuyến tính $\langle p,q\rangle$ trong đối ngẫu Fenchel cổ điển. Câu hỏi trung tâm: khi nào phép lấy liên hợp kép (bao lồi hóa tổng quát) tương thích với phép cộng Minkowski? Điều kiện này gọi là **điều kiện cộng tính** (trong ngôn ngữ trước đây gọi là "nucleus").

**Ghi chú phạm vi.** Về mặt cấu trúc trừu tượng, phát biểu tổng quát nhất của kết quả này là một trường hợp riêng của định lý phản xạ Day (Day, 1972) trong lý thuyết phạm trù đóng đối xứng. File này **không dùng và không cần** ngôn ngữ đó — mọi định nghĩa và chứng minh dưới đây độc lập, thuần túy dựa trên bất đẳng thức/đẳng thức hàm số thực và đại số tập hợp cơ bản. Độc giả quan tâm liên hệ phạm trù học có thể tham khảo tài liệu riêng; nó không cần thiết để hiểu hay dùng kết quả ở đây.

---

## 2. Định nghĩa polaroid tối ưu và sáu toán tử

### 2.1 Dữ liệu nguyên thủy

**Định nghĩa.** Một **hệ ghép cặp cộng tính** (additive coupling system) là bộ ba $(M,\oplus,\kappa)$ gồm:

- $M$ là một tập, mang phép cộng $\oplus:M\times M\to M$ giao hoán, kết hợp, có phần tử trung hòa $0$ (mọi ví dụ cụ thể: $M=X\times\mathbb R$, $\oplus$ là cộng tọa độ);
- $\kappa: M\times M\to\mathbb R\cup\{+\infty\}$ là một **hàm ghép cặp đối xứng**: $\kappa(x,y)=\kappa(y,x)$ với mọi $x,y\in M$.

Không giả thiết gì khác: không lồi, không trơn, không hữu hạn. Mọi tính chất thêm (như tồn tại residual) sẽ là giả thiết tường minh ở mục sau.

**Ví dụ chuẩn (Fenchel).** $M=\mathbb R^n\times\mathbb R$, $(p,w)\oplus(r,v)=(p+r,w+v)$, $\kappa\big((p,w),(q,s)\big)=\langle p,q\rangle-w-s$. Cặp $(p,w)$ đọc là (hướng, ngân sách).

### 2.2 Sáu toán tử

**Mức phần tử (2 toán tử):**

1. **Phép cộng** $x\oplus y$ — dữ liệu nguyên thủy.
2. **Liên hợp dịch chuyển** (residual/shifted conjugate) $x_2\ominus x_1$: nếu tồn tại, là phần tử $x_2\ominus x_1\in M$ thỏa

$$\kappa(x_1\oplus x_0,\ x_2) = \kappa(x_0,\ x_2\ominus x_1)\qquad\text{với mọi } x_0\in M.$$

(Không phải mọi hệ ghép cặp đều có toán tử này định nghĩa được — xem Định lý 2.)

**Mức tập hợp (3 toán tử):** với $A,B\subseteq M$,

3. **Tổng Minkowski nâng**: $A\oplus B := \{a\oplus b: a\in A,\ b\in B\}$.
4. **Hợp**: $A\cup B$ — hợp tập hợp thông thường.
5. **Tập liên hợp** (conjugate set / polar set tổng quát): $A^\star := \{y\in M:\kappa(x,y)\le 0\ \ \forall x\in A\}$.

**Mức lồi hóa (1 toán tử):**

6. **Tổng Minkowski đã đóng hóa (tensor)**: $A\circledast B := (A\oplus B)^{\star\star}$, trong đó $A^{\star\star}:=(A^\star)^\star$ là **liên hợp kép** (bao đóng tổng quát).

### 2.3 Tính chất nền của liên hợp kép

Vì $\kappa$ đối xứng, phép liên hợp kép luôn là một toán tử bao đóng (closure operator), đúng với **mọi** hệ ghép cặp, không cần thêm giả thiết:

- Mở rộng: $A\subseteq A^{\star\star}$;
- Đơn điệu: $A\subseteq B \Rightarrow A^\star\supseteq B^\star \Rightarrow A^{\star\star}\subseteq B^{\star\star}$;
- Lũy đẳng: $(A^{\star\star})^{\star\star}=A^{\star\star}$.

Gọi $A$ là **regular** (đã bao lồi hóa đầy đủ) nếu $A=A^{\star\star}$. Trong ví dụ Fenchel, $A^{\star\star}$ là epigraph của bao lồi đóng nhỏ nhất chứa dữ liệu của $A$; đây chính là định lý bao lồi Fenchel–Moreau viết lại.

---

## 3. Điều kiện cộng tính và định lý năm mệnh đề tương đương

### 3.1 Phát biểu điều kiện cộng tính

**Câu hỏi trung tâm.** Khi nào, với mọi $A,B\subseteq M$,

$$A^{\star\star}\oplus B^{\star\star} \subseteq (A\oplus B)^{\star\star}\qquad\text{(N)}$$

**Định nghĩa tương đương qua tensor.** (N) đúng với mọi $A,B$ khi và chỉ khi

$$A^{\star\star}\circledast B^{\star\star} = A\circledast B\qquad\text{với mọi } A,B\subseteq M. \qquad\text{(N')}$$

*(Chứng minh nhanh: chiều $\subseteq$ luôn đúng từ $A\subseteq A^{\star\star}$ và tính đơn điệu; chiều $\supseteq$ dùng (N) cộng tính lũy đẳng của $A\oplus B$ đã đóng hóa.)*

(N') nói: giá trị của phép cộng đã đóng hóa $\circledast$ chỉ phụ thuộc vào bao lồi của mỗi tập, không phụ thuộc đại diện cụ thể — đây là điều kiện để $\circledast$ trở thành một phép cộng thực sự trên các tập regular.

### 3.2 Định lý năm mệnh đề tương đương

Để phát biểu ba điều kiện trung gian, cần một khái niệm phụ trợ (không nằm trong sáu toán tử chính, chỉ là công cụ chứng minh):

$$T_A(C) := \{m\in M : A\oplus\{m\}\subseteq C\}\qquad (A\subseteq M,\ C\subseteq M),$$

viết gọn $T_x(C):=T_{\{x\}}(C)$ khi $A=\{x\}$ đơn điểm, và

$$D_{x_1,x_2} := \{m\in M : \kappa(x_1\oplus m,\ x_2)\le 0\} = T_{x_1}(\{x_2\}^\star).$$

**Định lý.** Cho hệ ghép cặp $(M,\oplus,\kappa)$. Năm điều sau tương đương.

**(i) Điều kiện cộng tính:** $A^{\star\star}\oplus B^{\star\star}\subseteq(A\oplus B)^{\star\star}$ với mọi $A,B\subseteq M$.

**(ii) Điều kiện phản xạ (mức sinh):** với mọi $x\in M$, mọi $C$ regular, $T_x(C)$ regular.

**(iii) Điều kiện mức phần tử:** với mọi $x_1,x_2\in M$, $D_{x_1,x_2}$ là regular (tương đương: $D_{x_1,x_2}=Y^\star$ với $Y$ nào đó).

**(iv) Tương thích tensor:** $A^{\star\star}\circledast B^{\star\star}=A\circledast B$ với mọi $A,B\subseteq M$.

**(v) Điều kiện phản xạ đầy đủ:** với mọi $A\subseteq M$, mọi $C$ regular, $T_A(C)$ regular.

**Sơ đồ chứng minh** (chi tiết từng bước xem phụ lục tính toán riêng — ở đây chỉ nêu cấu trúc để dùng khi soạn bài giảng):

- **(i)$\Leftrightarrow$(iv):** kẹp hai chiều bao hàm bằng tính đơn điệu và lũy đẳng của liên hợp kép.
- **(i)$\Rightarrow$(ii):** áp (i) cho cặp $\{x\},D:=T_x(C)$, dùng $x\in\{x\}^{\star\star}$.
- **(ii)$\Rightarrow$(i):** hai lượt — cố định lần lượt từng biến $A$ rồi $B$, mỗi lượt dùng (ii) cộng tính nhỏ nhất của liên hợp kép trong lớp regular.
- **(ii)$\Leftrightarrow$(v):** $T_A(C)=\bigcap_{a\in A}T_a(C)$; lớp regular ổn định dưới giao tùy ý; (v) là (ii) mở rộng lên mọi tập sinh, còn (ii) chỉ là (v) thu hẹp về tập một phần tử — hai chiều đều tầm thường một khi có bổ đề giao.
- **(ii)$\Leftrightarrow$(iii):** mọi $C$ regular viết được $C=Y^\star=\bigcap_{y\in Y}\{y\}^\star$ với $Y=C^\star$; $T_x$ giao hoán với giao; $T_x(\{y\}^\star)=D_{x,y}$.

### 3.3 Điều kiện đủ dễ kiểm tra: tồn tại liên hợp dịch chuyển

**Định lý (điều kiện đủ).** Nếu với mọi $x_1,x_2\in M$, liên hợp dịch chuyển $x_2\ominus x_1$ tồn tại (theo định nghĩa mục 2.2), thì (iii) tự động đúng — do đó điều kiện cộng tính (i) đúng.

*Chứng minh.* $D_{x_1,x_2}=\{m:\kappa(x_1\oplus m,x_2)\le0\}=\{m:\kappa(m,x_2\ominus x_1)\le0\}=\{x_2\ominus x_1\}^\star$ — polar của một điểm, tự động regular. $\blacksquare$

**Lưu ý về độ mạnh của điều kiện định nghĩa.** Định nghĩa ở mục 2.2 đòi **đẳng thức hàm số** $\kappa(x_1\oplus x_0,x_2)=\kappa(x_0,x_2\ominus x_1)$ với mọi $x_0$ — mạnh hơn yêu cầu tối thiểu (chỉ cần tương đương ở ngưỡng $\le 0$). Trong mọi ví dụ cụ thể ở Mục 4, đẳng thức đúng ở mức hàm số, không chỉ mức ngưỡng, nên đây không phải là làm yếu đi điều kiện mà là mô tả đúng cơ chế xảy ra trong thực hành.

---

## 4. Ứng dụng: bảng năm loại kernel

Mọi ví dụ dưới đây dùng $M=\mathbb R^n\times\mathbb R$ (trừ ví dụ 5, dùng $M$ tổng quát), tọa độ thứ hai là ngân sách, $\oplus$ là cộng tọa độ.

| # | Tên | $\kappa\big((p_1,w_1),(p_2,w_2)\big)$ | $x_2\ominus x_1$ | Cơ chế tách |
|---|---|---|---|---|
| 1 | Fenchel (bilinear chuẩn) | $\langle p_1,p_2\rangle - w_1-w_2$ | $\big(p_2,\ w_1+w_2-\langle p_1,p_2\rangle\big)$ | song tuyến tính |
| 2 | Fenchel có trọng số (anisotropic) | $\langle Tp_1,p_2\rangle-w_1-w_2$, $T$ tuyến tính bất kỳ | $\big(p_2,\ w_1+w_2-\langle Tp_1,p_2\rangle\big)$ | song tuyến tính (tổng quát hóa #1) |
| 3 | Kernel toàn phương (proximal) | $\tfrac12\|p_1-p_2\|^2-w_1-w_2$ | $\big(p_2-p_1,\ w_1+w_2\big)$ | bất biến tịnh tiến |
| 4 | Bất biến tịnh tiến tổng quát | $\psi(p_1-p_2)-w_1-w_2$, $\psi$ **chẵn**, tùy ý (không cần lồi/liên tục) | $\big(p_2-p_1,\ w_1+w_2\big)$ | bất biến tịnh tiến thuần túy |
| 5 | Ràng buộc cứng (hard constraint) | $\iota_D(x_1\oplus x_2)$, $D\subseteq M$ bất kỳ, $M$ tổng quát | $x_1\oplus x_2$ | kết hợp + giao hoán của $\oplus$ |

**Ghi chú #2:** tổng quát hóa trực tiếp #1 bằng cách thay tích vô hướng chuẩn bằng dạng song tuyến tính bất kỳ $\langle Tp_1,p_2\rangle$; tính toán y hệt #1, chỉ thay $\langle p_1,p_2\rangle\to\langle Tp_1,p_2\rangle$ xuyên suốt.

**Ghi chú #4:** #3 là trường hợp riêng của #4 với $\psi=\tfrac12\|\cdot\|^2$. Điểm mạnh nhất của #4: kết quả **không dùng đến tính lồi của $\psi$** — chỉ cần đẳng thức đại số $\|(p_1+p_0)-p_2\|^2=\|p_0-(p_2-p_1)\|^2$ kiểu tổng quát $\psi\big((p_1+p_0)-p_2\big)=\psi\big(p_0-(p_2-p_1)\big)$, đúng với mọi $\psi$ nhờ đơn thuần đổi biến, cộng thêm **tính chẵn** $\psi(t)=\psi(-t)$ — đây là điều kiện *tiên quyết* để $\kappa$ đối xứng (mục 2.1), không phải điều kiện riêng cho residual.

**Ghi chú #5:** $\iota_D(z)=0$ nếu $z\in D$, $=+\infty$ nếu không. Đây là ví dụ cho thấy điều kiện cộng tính **không phải hiện tượng của giải tích lồi** — nó là hệ quả thuần đại số của tính kết hợp-giao hoán của $\oplus$, đúng với $\kappa$ chỉ nhận hai giá trị $\{0,+\infty\}$, không epigraph, không độ đo mức vi phạm, không khái niệm lồi nào áp dụng được. Bốn ví dụ 1–4 nằm trong phạm vi giải tích lồi cổ điển; ví dụ 5 nằm ngoài hoàn toàn — cùng cơ chế đại số vận hành trong cả hai thế giới.

### 4.1 Ranh giới của cơ chế: khi nào thất bại

Để định vị đúng phạm vi bảng trên, đáng nêu một phản ví dụ: lấy $M=\mathbb R^n$ **trần** (không có tọa độ ngân sách), $\kappa(x,y)=\langle x,y\rangle$ (cone polar) hoặc $\kappa(x,y)=\langle x,y\rangle-1$ (polar thường). Cả hai đều **không** có liên hợp dịch chuyển tồn tại, và điều kiện cộng tính (i) **thất bại** — kiểm chứng cụ thể: với $A_0=\{e_1\}, B_0=\{e_2\}\subset\mathbb R^2$, $A_0^{\star\star}\oplus B_0^{\star\star}$ là cả góc phần tư thứ nhất, trong khi $(A_0\oplus B_0)^{\star\star}$ chỉ là tia qua $(1,1)$ — sai lệch hẳn một bậc chiều.

Kết luận: dạng $\kappa$ song tuyến tính/thuần nhất **không** đủ; điều quyết định là $M$ có đủ "bậc tự do ngân sách" ($M\cong X\times\mathbb R$, tọa độ $\mathbb R$ hấp thụ số hạng dư sinh ra khi tách $\kappa(x_1\oplus x_0,x_2)$) hay không. Cone polar/polar thường chỉ khôi phục được điều kiện cộng tính khi nhúng lại vào dạng #1/#2 (khôi phục tọa độ ngân sách) — đúng cách support function làm trong thực hành giải tích lồi cổ điển.
