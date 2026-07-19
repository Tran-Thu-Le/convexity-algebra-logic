# Định lý: Tính đóng của Polar sinh bởi Kernel

## Thiết lập

$$\overline X:=\mathbb R^n\times(-\infty,+\infty],\qquad c:X\times X\to\overline{\mathbb R}.$$

$$
E^{*_c}:=\{(y,s)\in\overline X:\ c(x,y)\le r+s\ \ \forall(x,r)\in E\}=\bigcap_{(x,r)\in E}H_{(x,r)},\qquad H_{(x,r)}:=\{(y,s):c(x,y)\le r+s\}.
$$

## Định lý

$$
\boxed{
E^{*_c}\ \text{đóng, với mọi } E\subseteq\overline X \iff \forall a\in X,\ \ b\mapsto c(a,b)\ \text{nửa liên tục dưới (lsc)}.
}
$$

*(Không cần đối xứng của $c$. Không cần lồi. Không cần liên tục toàn phần.)*

## Chứng minh

**($\Leftarrow$).** Với $(x,r)\in E$ cố định, $H_{(x,r)}=\{(y,s):\psi(y,s)\le r\}$ với $\psi(y,s):=c(x,y)-s$. Vì $s\mapsto-s$ liên tục và $y\mapsto c(x,y)$ lsc, $\psi$ lsc jointly $\Rightarrow H_{(x,r)}$ đóng (sublevel set của hàm lsc). Giao tùy ý các tập đóng là đóng $\Rightarrow E^{*_c}=\bigcap_{(x,r)\in E}H_{(x,r)}$ đóng.

**($\Rightarrow$).** Giả sử $b\mapsto c(a_0,b)$ không lsc tại $b_0$: tồn tại $b_k\to b_0$ với $\liminf_k c(a_0,b_k)=L<c(a_0,b_0)$. Chọn $M\in[L,c(a_0,b_0))$ và dãy con $b_{k_j}$ với $c(a_0,b_{k_j})\le M\ \forall j$. Đặt $E:=\{(a_0,0)\}$. Khi đó $(b_{k_j},M)\in E^{*_c}\ \forall j$ (vì $c(a_0,b_{k_j})\le M=0+M$), nhưng $(b_0,M)\notin E^{*_c}$ (vì $c(a_0,b_0)>M$). Dãy hội tụ $(b_{k_j},M)\to(b_0,M)$ nằm trong $E^{*_c}$ mà điểm giới hạn không thuộc $\Rightarrow E^{*_c}$ không đóng. $\blacksquare$

## Hệ quả trên hai kernel mẫu

| Kernel | Điều kiện lsc | Kết luận |
|---|---|---|
| $c(x,y)=\langle x,y\rangle$ | $b\mapsto\langle a,b\rangle$ liên tục, mọi $a$ | Luôn đóng |
| $c_h(x,y)=h(x+y)$ | $b\mapsto h(a+b)$ lsc $\iff h$ lsc | Đóng $\iff h$ lsc |

## Ghi chú

Điều kiện đóng của polar **không liên quan đến đối xứng của $c$** (đối xứng chỉ cần cho tính extensive $A\subseteq A^{**}$, một sự kiện độc lập). Kết quả trên áp dụng như nhau cho polar một lần ($E^{*_c}$) và mọi tầng lặp tiếp theo ($E^{**_c}$, v.v.), vì mỗi tầng chỉ dùng lại đúng một quy ước slot của $c$.
