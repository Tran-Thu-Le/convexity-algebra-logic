# Phụ lục: Trừu tượng hóa $K$ và Properness của Regepi

*(Tiếp nối "Regepi là một Idempotent Commutative Semiring có Polar")*

---

## Chốt kiến trúc: $K=\mathbb R\cup\{\top\}$

Kiến trúc cuối cùng cố định $K:=\mathbb R\cup\{\top\}$ (đúng hai dữ kiện gốc N1+N2, Sec 0.2 — không đáy). Hai kết quả chốt:

**1) $\mathbb X_K$ vẫn là idempotent commutative semiring có polar, và tính hấp thụ đúng vô điều kiện.**
$$E\oplus e_\wedge = e_\wedge \quad \forall E\in\mathbb X_K, \qquad e_\wedge:=\overline X=X\times K.$$
Đây là Định lý 4.4.2 (bản sửa, Sec 3) — đúng **không ngoại lệ** vì $\emptyset\notin\mathbb X_K$ (Hệ quả 2.3). Toàn bộ M0–M3, S1–S3, SM1, SM2, P, PM (Sec 4 gốc) đứng vững, vì K1–K8,K10 đều tự động đúng theo Định lý 0.2.1 (hệ quả của N1+N2).

**2) Properness chỉ định nghĩa trên $\mathbb X_K$** (không trên tập con thô $A\subseteq\overline X$ bất kỳ):
$$E\in\mathbb X_K \text{ proper} \;:\!\iff\; E\ne e_\wedge \ \wedge\ E\ne e_\wedge^*,$$
$$\text{tương đương} \iff \underbrace{(\forall x\in X: E_x\ne K)}_{\text{loại } e_\wedge=\overline X} \ \wedge\ \underbrace{(\exists x\in X: E_x\ne\{\top\})}_{\text{loại } e_\wedge^*=X\times\{\top\}},$$
với $e_\wedge^*=X\times\{\top\}$ (Định lý 2.2) là đáy của $(\mathbb X_K,\subseteq)$, còn $e_\wedge$ là đỉnh (Sec 2.5). Hai điều kiện **không rút gọn được về một** (Sec 2.4/4.1) — cần cả hai.

---

## Sec 0. Trừu tượng hóa $K$ — "ngưỡng-đại số" (threshold algebra)

Trước khi viết lại định nghĩa regepi, ta cô lập **chính xác** những gì $K=(-\infty,+\infty]$ đã dùng ở Sec 1–4 của tài liệu gốc, không hơn không kém.

**Định nghĩa 0.1 (Ngưỡng-đại số).** Bộ $(K,\le,+,0,\top,\tau)$ gọi là một *ngưỡng-đại số* nếu $\tau$ là **tô-pô thứ tự** trên $K$ (sinh bởi các tia mở $\{r<a\}$, $\{r>a\}$, $a\in K$ — với $K_2=(-\infty,+\infty]$ đây là tô-pô thường mở rộng bằng compact-hóa một điểm tại $+\infty$; $\tau$ chỉ thực sự được dùng ở K8) và:

- **(K1 — Order có đỉnh).** $(K,\le)$ là chain, $\mathbb R\hookrightarrow K$ bảo toàn thứ tự, và $\top:=\sup K\in K$.
- **(K2 — Giao hoán).** $+:K\times K\to K$ giao hoán (toàn phần hoặc từng phần trên miền $D\subseteq K\times K$).
- **(K3 — Kết hợp).** $+$ kết hợp trên $D$.
- **(K4 — Đơn điệu).** $r\le r'\Rightarrow r+s\le r'+s$ (bất cứ khi nào cả hai vế xác định).
- **(K5 — Đơn vị).** $\exists\,0\in K$: $r+0=r$.
- **(K6 — $\top$ hấp thụ).** $r+\top=\top$ với **mọi** $r\in K$ (kể cả $r=\top$, kể cả $r=\bot$ nếu $\bot\in K$) — đây là một **quy ước bắt buộc**, không phải hệ quả.
- **(K7 — Đầy đủ Dedekind trên phần hữu hạn).** Mọi tập con bị chặn dưới của $K\cap\mathbb R$ có infimum trong $K$.
- **(K8 — Liên tục).** $+$ liên tục trên $D$ trừ (có thể) tại góc $\{\bot\}\times\{\top\}$ nếu $\bot:=\inf K\in K$.

  *Ghi chú (không được xóa tiên đề này, dù nó có vẻ dư với $K_2$).* Khi $\bot\notin K$ (trường hợp $K_2=(-\infty,+\infty]$), điều khoản ngoại lệ rỗng, và K8 **suy biến thành một định lý** — hệ quả tự động của K1 (tô-pô thứ tự) + K6 (quy ước hấp thụ tại $\top$, khớp một-điểm-compact-hóa) + liên tục chuẩn của phép cộng thực. Nhưng trong định nghĩa *trừu tượng* của ngưỡng-đại số, K8 vẫn phải được liệt kê độc lập, vì (i) $K_3=[-\infty,+\infty]$ là phản ví dụ sống cho thấy nó **thất bại thật** khi $\bot\in K$ (xem Sec 5), và (ii) K7 (thứ tự Dedekind-đầy đủ) không tự động kéo theo K8 (tô-pô) — có thể có $K$ thỏa K1–K7 với tô-pô "lạ" khiến $+$ gián đoạn dù không có $\bot$. Bỏ K8 sẽ khiến định nghĩa âm thầm chấp nhận các $K$ bệnh lý mà Pb2/S1/SM1 thực ra không đứng vững.
- **(K10 — Vô hạn dưới ngặt).** Với mọi $s\ne\top$ và mọi $c\in\mathbb R$, tồn tại $r\in K$ với $r+s<c$.

**Bảng đối chiếu — tiên đề nào của $K$ nuôi tiên đề nào của Pa/Pb:**

| Pa/Pb | Cần từ $K$ | Không cần |
|---|---|---|
| Pa1 (Antitone) | *(miễn phí — đúng với mọi quan hệ)* | mọi thứ |
| Pa2 (Extensive) | K2 (giao hoán) | K4, K6, K7, K8 |
| Pa3 (Upward-closed) | K1 + K4 (order + đơn điệu) | K7, K8 |
| Pb1 (Fiber-closed) | K7 (Dedekind) + K3 (cộng dãy hội tụ) | K8 |
| Pb2 (Topo-closed) | K8 (liên tục) | K7 riêng lẻ |
| Pb3 (Convexity, không dùng) | cần $K$ **affine** trên $\mathbb R$ (mạnh hơn K1–K10) | — |
| **Pc1 (mới — Properness, xem Sec 2)** | K6 + K10 | K7, K8 |

Điểm đáng chú ý: **Pa1, Pa2, Pa3 không bao giờ cần K7/K8** — nhóm đại số hoàn toàn tách khỏi nhóm giải tích, đúng như document gốc ngầm chỉ ra. Điểm mới là dòng **Pc1**: định lý về suy biến toàn thớ chỉ cần K6+K10, không cần đầy đủ/liên tục — nó là một tiên đề "rẻ" ngang hàng S2/Pa3, không phải một điều kiện giải tích nặng.

### 0.2. Nén lại: K1–K10 rút về hai dữ kiện gốc (trường hợp không đáy)

$\tau$ sinh trực tiếp từ $\le$ (K1) — không phải dữ liệu độc lập. Và K8 (liên tục) hoá ra bị ép bởi K4+K6 cộng với việc phần hữu hạn của $K$ là $\mathbb R$ chuẩn. Toàn bộ danh sách K1–K10 (trường hợp không đáy, $\bot\notin K$) rút về:

**(N1) Nền chuẩn.** $K\setminus\{\top\}=\mathbb R$, với $+,\le$ là phép cộng/thứ tự thông thường trên $\mathbb R$.

**(N2) Đỉnh hấp thụ.** $\top=\sup K\in K$, và $r+\top:=\top$ với mọi $r\in K$.

**Định lý 0.2.1 (K2–K8,K10 là hệ quả của N1+N2).** Từ N1+N2 suy ra K2 (giao hoán), K3 (kết hợp), K4 (đơn điệu), K5 (đơn vị $0$), K7 (Dedekind-đầy đủ), K10 (không chặn dưới) — tất cả thừa hưởng nguyên xi từ $(\mathbb R,+,\le)$ chuẩn — và **K8 (liên tục)**.

*Chứng minh phần khó nhất — K8 tại biên $(r_0,\top)$, $r_0$ hữu hạn.* Lấy $r_k\to r_0$, $s_k\to\top$ (nghĩa là $\forall a\in\mathbb R,\ \exists N,\ \forall k\ge N: s_k>a$). Với mọi $M\in\mathbb R$, chọn $a:=M-r_0-1$: kể từ một lúc, $s_k>a$ và $r_k>r_0-1$ (vì $r_k\to r_0$), nên theo K4: $r_k+s_k>(r_0-1)+a=M-2$. Vậy $r_k+s_k\to\top$. Không dùng gì ngoài đơn điệu và số học $\mathbb R$ chuẩn — không cần một giả thiết liên tục độc lập. $\blacksquare$

**Hệ quả.** $K_2=\mathbb R\cup\{\top\}$ chỉ cần đúng hai dữ kiện N1+N2; toàn bộ 8 tiên đề K1–K8,K10 còn lại là định lý.

**(N3, tùy chọn — thêm đáy).** $\bot=\inf K\in K$, cùng một quy ước bắt buộc cho $\bot+\top$ (xem Sec 5). N3 là dữ kiện **duy nhất** trong toàn bộ khung không thể chọn mà giữ được K8 — đây chính xác là cái giá của việc thêm đáy, không hơn không kém, và giải thích gọn tại sao $K_2$ "rẻ" (N1+N2, mọi thứ khác miễn phí) còn $K_3$ "vỡ" (N1+N2+N3, và N3 luôn phá K8 tại góc $(\bot,\top)$).

---

## Sec 1. Regepi cho $K$ tổng quát

**Định nghĩa 1.1.** $\overline X_K := X\times K$, $X=\mathbb R^n$. Quan hệ Fenchel:
$$(x,r)\sim_K(y,s):\iff \langle x,y\rangle\le r+s.$$
$$\mathbb X_K:=\{E\subseteq\overline X_K : E=E^{**}\}.$$

Toàn bộ Sec 1–4 của tài liệu gốc đi qua nguyên vẹn với $K$ thay cho $(-\infty,+\infty]$, **miễn là** $K$ thỏa K1–K8 (Pb3 vẫn bị loại khỏi yêu cầu). Không cần viết lại từng chứng minh — bảng trên đã chỉ rõ chúng chỉ dùng K-tiên đề nào.

---

## Sec 2. Định lý suy biến toàn thớ — lõi của "properness"

**Bổ đề 2.1 (Suy biến toàn thớ).** Giả sử $K$ thỏa K6, K10. Nếu $A\subseteq\overline X_K$ và $\exists x_0: A_{x_0}=K$ (thớ toàn phần tại $x_0$), thì
$$A^*\subseteq X\times\{\top\}.$$

*Chứng minh.* Giả sử $p=(y,s)\in A^*$, $s\ne\top$. Vì $A_{x_0}=K$, mọi $r\in K$ đều cho $(x_0,r)\in A$, nên cần $\langle x_0,y\rangle\le r+s$ **đúng với mọi** $r\in K$. Theo K10 (với $c=\langle x_0,y\rangle$), tồn tại $r$ sao cho $r+s<c$ — mâu thuẫn. Vậy $s=\top$. $\blacksquare$

**Remark 2.1.1 (Từ suy biến cục bộ đến suy biến toàn cục: $E=e_\wedge$, không chỉ $E_{x_0}=K$).** Bổ đề 2.1 chỉ mới cho $A^*\subseteq X\times\{\top\}$ — một phát biểu về *polar*, chưa nói gì về việc $A$ (hay bao đóng của nó) trông ra sao. Điều đáng chú ý thật sự là hệ quả mạnh hơn nhiều:

> Nếu $E\in\mathbb X_K$ (đã bipolar-closed) và $\exists x_0: E_{x_0}=K$, thì $E=e_\wedge$ — tức **mọi thớ** của $E$, không chỉ thớ tại $x_0$, đều bằng $K$.

*Chứng minh.* Áp Bổ đề 2.1 cho $A=E$: $E^*\subseteq X\times\{\top\}$. Áp Pa1 (antitone) cho bao hàm thức này: $(X\times\{\top\})^*\subseteq E^{**}$. Trực tiếp: với $p=(y,\top)$ bất kỳ và mọi $(x,r)\in\overline X_K$, $\langle x,y\rangle\le r+\top=\top$ (K6) — luôn đúng, nên $(X\times\{\top\})^*=\overline X_K$. Vậy $\overline X_K\subseteq E^{**}$; kết hợp $E^{**}\subseteq\overline X_K$ (hiển nhiên) cho $E^{**}=\overline X_K=e_\wedge$. Vì $E\in\mathbb X_K$ nên $E=E^{**}=e_\wedge$. $\blacksquare$

Vậy: một thớ toàn phần **cục bộ** tại một điểm $x_0$ duy nhất, kết hợp với tính bipolar-closed, buộc **toàn bộ tập hợp** sụp về $e_\wedge=\overline X$ — closure không cho phép suy biến "một phần". Đây là bản đầy đủ, sớm hơn, của phát biểu vốn chỉ xuất hiện gián tiếp qua Bổ đề 2.1′ ở Sec 2.4.

**Định lý 2.2 (Hai phần tử suy biến chính tắc, tự-đối ngẫu).**
$$\overline X_K^{\,*} = X\times\{\top\}, \qquad (X\times\{\top\})^*=\overline X_K.$$
Do đó $e_\wedge:=\overline X_K$ và $e_\wedge^*=X\times\{\top\}$ là một **cặp đối ngẫu qua $*$**, cả hai đều thuộc $\mathbb X_K$.

*Chứng minh.* Chiều 1: áp Bổ đề 2.1 cho $A=\overline X_K$ (thớ toàn phần tại mọi $x$) $\Rightarrow \overline X_K^*\subseteq X\times\{\top\}$. Chiều ngược: với $p=(y,\top)$, mọi $(x,r)\in\overline X_K$: $\langle x,y\rangle\le r+\top=\top$ (K6) — luôn đúng. Vậy $\overline X_K^*=X\times\{\top\}$.

Chiều 2: với $p=(y,s)\in(X\times\{\top\})^*$, cần $\forall x: \langle x,y\rangle\le\top+s=\top$ (K6) — luôn đúng với mọi $y,s$. Vậy $(X\times\{\top\})^*=\overline X_K$. $\blacksquare$

**Hệ quả 2.3 (Sự vắng mặt bắt buộc của $\emptyset$).** Với mọi $K$ thỏa K6, K10 (và $X\ne\emptyset$): $\emptyset\notin\mathbb X_K$.

*Chứng minh.* $\emptyset^*=\overline X_K$ (đúng vô điều kiện, mệnh đề rỗng). Áp Định lý 2.2: $\emptyset^{**}=\overline X_K^*=X\times\{\top\}\ne\emptyset$ (vì $X\ne\emptyset$). Vậy $\emptyset\ne\emptyset^{**}$. $\blacksquare$

### 2.4. Kiểm tra chiều đảo của Bổ đề 2.1

Chiều đảo *ngây thơ* — "$A^*\subseteq X\times\{\top\} \Rightarrow A$ có thớ toàn phần" — **sai**.

*Phản ví dụ.* $K=(-\infty,+\infty]$, $A:=X\times\mathbb R$ (bỏ mức $\top$). Ta có $A_x=\mathbb R\ne K$ với mọi $x$ (không thớ nào toàn phần), nhưng tính trực tiếp: với $y\ne0$, $\sup_x\langle x,y\rangle=+\infty$ buộc $s=\top$; với $y=0$, cần $0\le r+s$ với mọi $r\in\mathbb R$ (kể cả $r\to-\infty$), cũng chỉ $s=\top$ thỏa (K6). Vậy $A^*=X\times\{\top\}\subseteq X\times\{\top\}$ — giả thiết đúng, kết luận sai.

**Bổ đề 2.1′ (chiều đảo đúng, tổng quát, không cần $A\in\mathbb X$).**
$$A^*\subseteq X\times\{\top\} \ \Longrightarrow\ A^{**}=\overline X.$$

*Chứng minh.* Áp Pa1 (antitone): $A^*\subseteq X\times\{\top\}\Rightarrow (X\times\{\top\})^*\subseteq A^{**}$. Theo Định lý 2.2, $(X\times\{\top\})^*=\overline X$. Vậy $\overline X\subseteq A^{**}\subseteq\overline X$, suy ra $A^{**}=\overline X$. $\blacksquare$

Kiểm lại phản ví dụ: $A^{**}=(X\times\{\top\})^*=\overline X$ — khớp với bổ đề, dù $A$ (chưa đóng bipolar) không có thớ toàn phần. Vậy chiều đảo chỉ đúng ở mức **bao đóng bipolar**, không ở mức tập thô.

**Hệ quả (hạn chế trên $\mathbb X$).** Nếu $E\in\mathbb X$ và $E^*\subseteq X\times\{\top\}$ thì $E=e_\wedge$ — chỉ cần Pa1 + Định lý 2.2, không cần K7/K8.

### 2.5. $e_\wedge,e_\wedge^*$ là đỉnh/đáy của $(\mathbb X,\subseteq)$ — properness không phải closure

Áp Pa1 cho bao hàm thức tầm thường $E\subseteq\overline X=e_\wedge$ (đúng với mọi $E\in\mathbb X$): $e_\wedge^*\subseteq E^*$. Vì $*$ là song ánh tự nghịch đảo trên $\mathbb X$ (Định lý 2.1.1), khi $E$ chạy khắp $\mathbb X$ thì $E^*$ cũng chạy khắp $\mathbb X$, nên câu trên tương đương $e_\wedge^*\subseteq F$ với **mọi** $F\in\mathbb X$. Vậy:

$$e_\wedge = \overline X \ \text{là đỉnh}, \qquad e_\wedge^*=X\times\{\top\}\ \text{là đáy}, \qquad \text{của }(\mathbb X,\subseteq).$$

Hơn nữa $e_\wedge^*=\emptyset^{**}$ và $e_\wedge=\overline X^{**}$ — hai phần tử suy biến chính là ảnh của hai hạt giống tầm thường nhất của $\mathcal P(\overline X)$ ($\emptyset$ và $\overline X$) qua closure $(-)^{**}$.

**Properness không phải một closure operator** (không extensive, không có phép "properization" mở rộng $E$; và $\wedge,\oplus$ không bảo toàn tính proper — ví dụ giao hai tập lồi có miền xác định rời nhau cho ra $e_\wedge$). Nó đúng hơn là khái niệm *phần tử thực sự* chuẩn của lý thuyết dàn (giống "ideal thực sự", "tập mở thực sự"): **$\mathbb X$ bỏ đi đỉnh và đáy của chính nó**, hai đỉnh/đáy ấy chính là hạt nhân bị loại trừ của closure $(-)^{**}$ khi áp lên hai đầu mút của $\mathcal P(\overline X)$.

---

## Sec 3. Sửa lỗi cụ thể trong Định lý 4.4.2 của tài liệu gốc

Đây là bằng chứng cụ thể rằng khung trừu tượng ở trên không phải trò chơi hình thức — nó phát hiện một khe hở thật.

Trong chứng minh Định lý 4.4.2, đoạn tính $\big(\pi(E)\times(-\infty,+\infty]\big)^*$, lập luận chỉ xét *"cho $r\to-\infty$ phá vỡ bất đẳng thức với mọi $y,s$ hữu hạn"* — bỏ sót nhánh $s=+\infty$. Nhưng chính xác theo Định lý 2.2: với $s=\top=+\infty$, điều kiện $\langle x,y\rangle\le r+\infty=\infty$ luôn đúng, nên
$$\big(\pi(E)\times(-\infty,+\infty]\big)^* = X\times\{+\infty\} \ne \emptyset,$$
**không phải $\emptyset$** như đã viết. Kết luận cuối ($E\oplus e_\wedge = e_\wedge$) vẫn đúng may mắn (vì $(X\times\{\infty\})^*=\overline X$ trùng với $\emptyset^*=\overline X$ một cách tình cờ), nhưng đoạn *"Trường hợp $E=\emptyset$: $\emptyset\oplus e_\wedge=\emptyset$"* là sai: theo đúng Định nghĩa 3.2, phải đóng bipolar, $\emptyset\oplus e_\wedge = \emptyset^{**} = X\times\{\infty\} \ne \emptyset$.

**Kết luận thực chất:** $\emptyset$ chưa từng là phần tử hợp lệ của $\mathbb X$ (Hệ quả 2.3). Cái gọi là "trường hợp con rời rạc" của SM2 **không tồn tại** — nó là ảo giác sinh từ một polar tính thiếu một nhánh. Khi tính đúng:

> **Định lý 4.4.2 (bản sửa, vô điều kiện).** $E\oplus e_\wedge=e_\wedge$ với **mọi** $E\in\mathbb X$, không ngoại lệ.

---

## Sec 4. Định nghĩa Properness chính thức

**Định nghĩa 4.1.** $E\in\mathbb X_K$ là **proper** $:\iff E\notin\{e_\wedge,\,e_\wedge^*\}$, tương đương (Định lý 2.2 + tính đối hợp) $E\ne\overline X_K \wedge E^*\ne\overline X_K$, tương đương
$$E \text{ proper} \iff \underbrace{\big(\forall x\in X: E_x\ne K\big)}_{\text{loại }e_\wedge} \ \wedge\ \underbrace{\big(\exists x\in X: E_x\ne\{\top\}\big)}_{\text{loại }e_\wedge^*}.$$

**Lưu ý quan trọng (đã kiểm bằng Sec 2.4).** Hai điều kiện trên **không đối xứng về cấu trúc** dù $e_\wedge,e_\wedge^*$ đối xứng qua $*$: vế đầu là "$\forall x$", vế sau là "$\exists x$" (phủ định của $\forall x: E_x=\{\top\}$). Điều kiện $\forall x: E_x\ne K$ **một mình** chỉ loại $e_\wedge$, **không** loại được $e_\wedge^*$ — phản chứng: $E=e_\wedge^*=X\times\{\top\}$ có $E_x=\{\top\}\ne K$ với mọi $x$ (giả sử $|K|>1$), tức thỏa điều kiện thớ-toàn-phần một cách vô hại trong khi chính nó là phần tử suy biến còn lại. Do đó **cả hai vế đều cần thiết**, không thể rút gọn về một điều kiện thớ duy nhất như bản trước đây từng tuyên bố sai. Đây chính là hệ quả của việc chiều đảo của Bổ đề 2.1 chỉ đúng ở mức bao đóng bipolar ($A^{**}=\overline X$), không đúng ở mức tập thô.

Với cách phát biểu đúng này, properness vẫn là tiên đề **rẻ** — không cần Pb1/Pb2/Pb3, chỉ cần K6+K10 (qua Bổ đề 2.1 và 2.1′) — nhưng là **hội của hai điều kiện độc lập**, không phải một điều kiện thớ đơn lẻ như tuyên bố (sai) trước đó.

Lý do nó rẻ ở đây mà đắt ở giải tích lồi cổ điển: trong giải tích lồi cổ điển, hàm chưa nhất thiết đóng, nên hai loại suy biến ($\equiv+\infty$ và $\exists x: f(x)=-\infty$) là hai hiện tượng độc lập. Trên $\mathbb X_K$ (đã đóng bipolar sẵn), Định lý 2.2 chứng minh chúng **sụp thành đúng một cặp đối ngẫu duy nhất** $\{e_\wedge,e_\wedge^*\}$ — một định lý kiểu Ore thứ hai, song song với Định lý 2.1.1 (involutive): đóng bipolar "nuốt" mọi suy biến cục bộ thành suy biến toàn cục.

---

## Sec 5. Ba lựa chọn $K$ dưới lăng kính properness

| | $K_1=\mathbb R$ | $K_2=(-\infty,+\infty]$ | $K_3=[-\infty,+\infty]$ |
|---|---|---|---|
| K1 (có $\top$) | ✗ — không có $\sup K\in K$ | ✓ | ✓ |
| K6 (top hấp thụ) | vô nghĩa | ✓, tường minh | ✓, cần quy ước tại góc $\bot+\top$ |
| K8 (liên tục) | ✓ (tầm thường) | ✓ | **✗ tại góc $(\bot,\top)$** |
| $\emptyset\in\mathbb X_K$? | không áp dụng | **không** (Hệ quả 2.3) | không (cùng chứng minh) |
| Cặp suy biến $\{e_\wedge,e_\wedge^*\}$ | không định nghĩa được | $\{\overline X,\,X\times\{\infty\}\}$ | trùng cộng thêm: bất kỳ thớ nào chứa $\bot$ đều tự động $=K$ (Pa3+K4), nên collapse xảy ra ngay khi $-\infty$ xuất hiện ở **một điểm** |

$K_3$ "vỡ nhiều" chính xác vì hai lý do liên kết:

1. K8 thất bại tại góc $(-\infty,+\infty)$: lấy $a_k\to-\infty,\ b_k=c-a_k\to+\infty$, thì $a_k+b_k\equiv c$ (hữu hạn) với mọi $k$, nhưng quy ước K6 buộc giới hạn góc phải là $\top$ — gián đoạn thật sự. Điều này làm sập chính Định lý 3.1.2 (Key Lemma), vì chứng minh của nó dùng Pb1+Pb2 (dãy hội tụ + tính đóng) tại đúng chỗ này.

   *Đây là hỏng cấu trúc, không phải do chọn sai quy ước:* với $\bot+\top$, không có giá trị nào "tự nhiên" — dãy tiến tới góc theo các cách khác nhau (như trên) cho giới hạn tổng khác nhau tùy ý $c\in\mathbb R$. Dù quy ước $\bot+\top:=\top$ (K6 chọn) hay ngược lại $\bot+\top:=\bot$, tính liên tục tại góc $(\bot,\top)$ đều **bất khả thi** một khi cả $\bot,\top\in K$ và $+$ đòi toàn phần. $K_2$ tránh vấn đề không phải vì có quy ước đẹp, mà vì không đưa $\bot$ vào $K$ nên câu hỏi "$\bot+\top=?$" không bao giờ được đặt ra.
2. Bất kỳ giá trị $-\infty$ cục bộ nào (một thớ chứa $\bot$) đều buộc **toàn bộ thớ ấy** $=K$ (do Pa3), rồi Bổ đề 2.1 buộc **toàn bộ $E$** $=\overline X$ — collapse toàn cục, mạnh hơn nhiều so với hiện tượng cổ điển "hàm lồi nhận giá trị $-\infty$ ở một điểm thì $\equiv-\infty$ trên phần trong tương đối của domain" (Rockafellar). Ở đây không có "phần trong tương đối" nữa — chỉ có tất-cả hoặc không-gì, vì $\mathbb X_K$ đã đóng bipolar sẵn.

$K_1=\mathbb R$ thất bại ngay ở tầng định nghĩa: không có $\top$ nghĩa là không định nghĩa nổi $e_\oplus=X\times[0,\top]$, và không biểu diễn nổi hàm chỉ thị ($\iota_C(x)=+\infty$ ngoài $C$) — khối xây dựng cơ bản nhất của giải tích lồi.

**Kết luận.** $K_2=(-\infty,+\infty]$ là lựa chọn *duy nhất* trong ba lựa chọn thỏa **đồng thời** K1–K10, và — như Sec 3–4 chứng minh — nó làm điều đó **mà không cần một tiên đề properness tách biệt nào cả**: properness tự động là một định lý (Định lý 2.2), không phải một giả thiết phải thêm vào.

---

## Sec 6. Trả lời câu hỏi kiến trúc — hấp thụ bởi 0

> *"Tính hấp thụ bởi 0 có thể giữ hoặc bỏ do MALL không cần tính chất đó"*

Câu trả lời không còn là lựa chọn gu (taste) mà là **bị ép bởi toán học**: Hệ quả 2.3 chứng minh $\emptyset\notin\mathbb X_K$ với mọi $K$ hợp lệ. Do đó **không có phần tử nào trong $\mathbb X_K$ có thể đóng vai trò "0 hấp thụ cả hai phép toán"** theo nghĩa cổ điển của idempotent semiring có zero (như bán vành tropical $(\mathbb R\cup\{\pm\infty\},\min,+)$ có $+\infty$ là 0 thật). Thay vào đó, cấu trúc thật của $\mathbb X_K$ là:

- $e_\wedge=\overline X$: đơn vị của $\wedge$, đồng thời hấp thụ với $\oplus$ (Định lý 4.4.2 sửa, vô điều kiện).
- $e_\wedge^*=X\times\{\top\}$: đối ngẫu của $e_\wedge$ qua $*$, cũng hấp thụ với $\oplus$ theo cách đối xứng (chứng minh song song bằng cách áp $*$ lên toàn bộ Định lý 4.4.2, dùng PM).
- Không có "0" chung cho cả $\wedge$ lẫn $\oplus$ theo đúng nghĩa bán vành cổ điển.

Đây chính là dáng dấp MALL: hai đơn vị $\top$ (của $\&$) và $\bot$ (của $\parr$) không trùng nhau và không cần một "zero" phổ quát duy nhất — mô hình $(\mathbb X_K,\wedge,\oplus,{}^*)$ khớp tự nhiên với cặp đơn vị nhân-cộng của linear logic hơn là với bán vành tropical cổ điển.

**Khuyến nghị kiến trúc:** bỏ hẳn tiên đề "hấp thụ bởi 0" khỏi danh sách 11 tiên đề ICS — nó không chỉ "không cần" mà còn **không thỏa mãn được** trên $\mathbb X_K$ với $K_2$, nên yêu cầu nó sẽ làm cấu trúc trống rỗng (vacuous).

---

## Sec 7. Bảng: 11 tiên đề ICS và properness

| Tiên đề | Nội dung | Cần properness? |
|---|---|---|
| M0 | $E\wedge E=E$ | Không |
| M1 | $\wedge$ kết hợp | Không |
| M2 | $\wedge$ giao hoán | Không |
| M3 | $E\wedge e_\wedge=E$ | Không |
| S1 | $\oplus$ kết hợp | Không |
| S2 | $\oplus$ giao hoán | Không |
| S3 | $E\oplus e_\oplus=E$ | Không |
| SM1 | $E\oplus(F\wedge G)=(E\oplus F)\wedge(E\oplus G)$ | Không |
| SM2 | $E\oplus e_\wedge=e_\wedge$ | **Không** — bản gốc viết "trên $E\ne\emptyset$" như thể cần loại trừ phần tử suy biến, nhưng $\emptyset\notin\mathbb X$ vô điều kiện (Hệ quả 2.3), nên đúng trên **toàn bộ** $\mathbb X$, không cần lọc |
| P | $E^{**}=E$ | Không |
| PM | $E\subseteq F\iff F^*\subseteq E^*$ | Không |

**Kết luận.** Properness không được dùng bởi bất kỳ tiên đề ICS nào — toàn bộ $(\mathbb X,\wedge,\oplus,{}^*)$ đúng đồng đều trên $E\in\mathbb X$ dù proper hay không (kể cả $e_\wedge,e_\wedge^*$ — chính hai phần tử không proper — vẫn tuân thủ đầy đủ 11 tiên đề, chỉ là chúng nằm ở đỉnh/đáy của dàn). Properness là một khái niệm **độc lập, không phải điều kiện cho ICS**; nó chỉ có ý nghĩa khi bắc cầu sang ngôn ngữ hàm lồi cổ điển ($f\not\equiv\pm\infty$), giống hệt vai trò của Pb3 (convexity) đã bị loại khỏi Sec 4 gốc.

**Ghi chú mạnh hơn.** Properness cũng không được dùng để chứng minh Pa1–Pa3, Pb1–Pb3 (Sec 2) — mọi chứng minh ở đó chạy trên $A\subseteq\overline X$ hoặc $E,F\in\mathbb X$ tùy ý, không giả sử proper. Bổ đề 2.1/Định lý 2.2 (nơi định nghĩa properness) đi theo chiều **ngược lại**: dùng Pa1+Pa2+K6+K10 để suy ra cấu trúc $\{e_\wedge,e_\wedge^*\}$, chứ không dùng properness làm giả thiết. Vậy properness chỉ được dùng để chứng minh **về chính nó** (Định lý 2.2, Hệ quả 2.3, Sec 2.4–2.5) — nó là sản phẩm phân loại của khung, không phải giả thiết đầu vào cho bất kỳ định lý nền tảng nào trong Sec 1–4.

### 7.1. Ngộ nhận cổ điển: properness KHÔNG cần cho $E^{**}=E$ (hay $f^{**}=f$)

Trực giác thường gặp: *"$f$ lồi, đóng, proper $\Rightarrow f^{**}=f$"* — nghe như proper là điều kiện cần cho biconjugate. Đây là gộp-chung lỏng lẻo. Phát biểu chính xác (Rockafellar, *Convex Analysis*, §7 — định nghĩa "hàm lồi đóng"): một hàm lồi là **đóng** nếu **hoặc** proper+lsc, **hoặc** $\equiv+\infty$, **hoặc** $\equiv-\infty$ — đúng ba trường hợp — và với **cả ba**, $f^{**}=f$ đúng, không ngoại lệ. Kiểm trực tiếp $f\equiv+\infty$: $f^*\equiv-\infty$ (hằng), $f^{**}\equiv+\infty=f$ — đúng dù $f$ không proper.

Trong ngôn ngữ regepi, đây chính xác là nội dung bảng Sec 7 ở tầng tổng quát hơn: $E^{**}=E$ đúng với **mọi** $E\in\mathbb X$ — kể cả $e_\wedge,e_\wedge^*$ (hai phần tử không proper). Properness không rò rỉ vào phương trình $E^{**}=E$ vì đó là **định nghĩa** của $\mathbb X$ (Định nghĩa 3.1), không phải một định lý cần điều kiện thêm.

Properness thật sự cần cho các định lý **ở tầng sau**, nơi thao tác **với $f^*$** chứ không chỉ tồn tại nó: $f^*$ chính nó proper (để lặp lại lý luận), $\partial f(x)\ne\emptyset$, công thức tổng $(f+g)^*=f^*\,\square\,g^*$ không có duality gap — tất cả nằm ngoài phạm vi Sec 1–4 (đúng như ghi chú "biểu diễn hàm là một tầng hoàn toàn khác" ở đầu Sec 4 gốc).
