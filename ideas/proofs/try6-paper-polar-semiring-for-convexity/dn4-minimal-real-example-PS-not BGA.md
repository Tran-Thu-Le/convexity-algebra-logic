# dn4-minimal-real-example.md

# Ví Dụ Tối Giản Trên $[0,1]\subset\mathbb R$: Polar Semiring Không Phải BGA

*(Nối tiếp d2-compare-with-BGA. Mục đích: cung cấp một ví dụ "toy" hoàn toàn trên số thực,
không cần bộ máy $\Gamma(\mathbb R^n)$/hàm lồi, để mở đầu phần motivation trước khi vào
ví dụ chính. Không dùng ký hiệu mở rộng $\pm\infty$ — mọi phần tử là số thực thật.)*

---

## 1. Định nghĩa cấu trúc

$$A:=[0,1]\subset\mathbb R.$$

| Ký hiệu PS | Định nghĩa cụ thể |
|---|---|
| `^` (plus) | $x\wedge y:=\max(x,y)$ |
| `+` (tensor) | $x+y:=x\times y$ (phép nhân thường) |
| `em` | $0$ |
| `ez` | $1$ |
| `star` | $\text{star}(x):=(1-\sqrt x)^2$ |

**Nguồn gốc của `star`:** lấy song ánh tăng $\tau(x):=x^2$ trên $[0,1]$ (với nghịch đảo $\tau^{-1}(y)=\sqrt y$), và đặt
$$\text{star}(x):=\tau\big(1-\tau^{-1}(x)\big)=\big(1-\sqrt x\big)^2.$$
Đây là "liên hợp" của phép đối chuẩn $x\mapsto1-x$ qua $\tau$ — một song ánh nghịch đảo thứ tự **phi tuyến**, khác hẳn $1-x$.

**Định nghĩa dẫn xuất:**
$$\text{with}(x,y):=\text{star}\big(\text{star}(x)\wedge\text{star}(y)\big),\qquad \text{parr}(x,y):=\text{star}\big(\text{star}(x)+\text{star}(y)\big).$$

---

## 2. 11 tiên đề — phát biểu đầy đủ và kiểm từng cái

### M0 (idempotence của `^`)
$$x\wedge x=x.$$
*Kiểm:* $\max(x,x)=x$ — hiển nhiên đúng với mọi $x\in[0,1]$.

### M1 (kết hợp của `^`)
$$x\wedge(y\wedge z)=(x\wedge y)\wedge z.$$
*Kiểm:* $\max$ kết hợp trên mọi tập sắp toàn phần — đúng.

### M2 (giao hoán của `^`)
$$x\wedge y=y\wedge x.$$
*Kiểm:* $\max(x,y)=\max(y,x)$ — đúng.

### M3 (đơn vị của `^`)
$$x\wedge em=x.$$
*Kiểm:* $\max(x,0)=x$ với mọi $x\in[0,1]$ — đúng, vì $0$ là **phần tử nhỏ nhất thật sự** của $[0,1]$ (không cần mở rộng $-\infty$).

### S1 (kết hợp của `+`)
$$x+(y+z)=(x+y)+z.$$
*Kiểm:* $x(yz)=(xy)z$ — kết hợp của phép nhân thực, đúng.

### S2 (giao hoán của `+`)
$$x+y=y+x.$$
*Kiểm:* $xy=yx$ — đúng.

### S3 (đơn vị của `+`)
$$x+ez=x.$$
*Kiểm:* $x\times1=x$ — đúng.

### SM1 (`+` phân phối qua `^`)
$$x+(y\wedge z)=(x+y)\wedge(x+z).$$
*Kiểm:* cần $x\cdot\max(y,z)=\max(xy,xz)$. Vì $x\ge0$: nếu $y\ge z$ thì $xy\ge xz$ (nhân hai vế với số không âm bảo toàn thứ tự), nên $\max(xy,xz)=xy=x\max(y,z)$; đối xứng cho $z\ge y$. Đúng với mọi $x,y,z\in[0,1]$.

### SM2 (`em` hấp thụ với `+`)
$$x+em=em.$$
*Kiểm:* $x\times0=0=em$ với mọi $x\in[0,1]$ — đúng ($0$ là phần tử hấp thụ chuẩn của phép nhân).

### P (involution của `star`)
$$\text{star}(\text{star}(x))=x.$$
*Kiểm:* đặt $u:=\sqrt x\in[0,1]$, có $\text{star}(x)=(1-u)^2$. Vì $1-u\in[0,1]$ (do $u\in[0,1]$) nên $1-u\ge0$, và
$$\text{star}(\text{star}(x))=\Big(1-\sqrt{(1-u)^2}\Big)^2=\big(1-(1-u)\big)^2=u^2=x.$$
Đúng với mọi $x\in[0,1]$. $\blacksquare$

### PM (polarity đảo thứ tự cảm sinh bởi `^`)
$$(x\wedge y=x)\iff\big(\text{star}(y)\wedge\text{star}(x)=\text{star}(y)\big).$$
*Kiểm:* đặt $g(x):=(1-\sqrt x)^2$. Với $x\in(0,1)$:
$$g'(x)=2(1-\sqrt x)\cdot\Big(-\frac{1}{2\sqrt x}\Big)=-\frac{1-\sqrt x}{\sqrt x}<0$$
(vì $\sqrt x\in(0,1)\Rightarrow1-\sqrt x>0$). Vậy $g$ **giảm chặt liên tục** trên $(0,1)$, với $g(0)=1,\ g(1)=0$ — song ánh giảm chặt toàn cục trên $[0,1]$. Với một song ánh giảm chặt trên tập sắp toàn phần, đẳng thức chuẩn
$$x\ge y\iff\text{star}(x)\le\text{star}(y)$$
tự động đúng — dịch qua $\max(x,y)=x\iff x\ge y$ chính là nội dung PM. $\blacksquare$

**Kết luận Sec 2:** $(A,\wedge,+,\text{star},em,ez)=([0,1],\max,\times,(1-\sqrt{\cdot})^2,0,1)$ thỏa **đầy đủ 11/11 tiên đề** — là một polar semiring hợp lệ.

---

## 3. Kiểm chứng số (brute-force/sampling)

```python
import random

def P(x,y): return max(x,y)       # ^
def T(x,y): return x*y            # +
em, ez = 0.0, 1.0

def star(x):
    return (1 - x**0.5)**2

random.seed(0)
xs = [random.uniform(0,1) for _ in range(5000)]

print("P:",   all(abs(star(star(x))-x) < 1e-9 for x in xs))
print("M3:",  all(abs(P(x,em)-x)<1e-9 for x in xs))
print("S3:",  all(abs(T(x,ez)-x)<1e-9 for x in xs))
print("SM2:", all(abs(T(x,em)-em)<1e-9 for x in xs))
print("SM1:", all(abs(T(x,P(y,z)) - P(T(x,y),T(x,z)))<1e-9
                   for x,y,z in zip(xs, xs[::-1], sorted(xs))))

xs_sorted = sorted(xs[:2000])
print("PM (antitone):", all(star(xs_sorted[i]) > star(xs_sorted[i+1]) - 1e-9
                             for i in range(len(xs_sorted)-1)))
```

Kết quả chạy thực tế: **tất cả `True`** — khớp với chứng minh tay ở Sec 2.

---

## 4. Định lý bất tương thích: `star` không sinh từ residual của `+`

### 4.1. Residual luôn tồn tại trên $[0,1]$ — nhưng có dạng cụ thể

**Bổ đề.** $[0,1]$ là lattice **đầy đủ** (mọi tập con có sup/inf trong $[0,1]$), và tensor $\times$ bảo toàn $\max$ hữu hạn (SM1 vừa chứng minh). Theo định lý adjoint chuẩn cho lattice đầy đủ, residual **luôn tồn tại** và cho bởi:
$$\text{res}(x,c):=\sup\{b\in[0,1]:x\cdot b\le c\}=\begin{cases}\min(1,\,c/x) & x>0\\ 1 & x=0\end{cases}$$

*Kiểm bằng số:* điều kiện $x b\le c\iff b\le\text{res}(x,c)$ đúng $100\%$ trên $3000$ bộ $(x,c,b)$ ngẫu nhiên.

### 4.2. Định lý (Bất tương thích)

> **Không tồn tại** $\text{zero}\in[0,1]$ sao cho $\text{star}(x)=\text{res}(x,\text{zero})$ với **mọi** $x\in[0,1]$.

*Chứng minh.* Giả sử phản chứng tồn tại $c_0:=\text{zero}$ thỏa mãn với mọi $x$.

**Bước 1 — xác định $c_0$ từ điều kiện tại $x=1$:**
$$\text{star}(1)=(1-\sqrt1)^2=0.$$
Cần $\text{res}(1,c_0)=\min(1,c_0)=c_0$ (vì $c_0\in[0,1]$). Vậy $c_0=0$.

**Bước 2 — kiểm $c_0=0$ tại một điểm khác, ví dụ $x=0.25$:**
$$\text{res}(0.25,\,0)=\min\Big(1,\ \frac{0}{0.25}\Big)=0.$$
Nhưng
$$\text{star}(0.25)=\big(1-\sqrt{0.25}\big)^2=(1-0.5)^2=0.25.$$

**Mâu thuẫn:** $0.25=\text{star}(0.25)\ne\text{res}(0.25,0)=0$.

Vậy không tồn tại $c_0$ nào thỏa mãn đồng thời cả hai điểm — nói riêng không tồn tại với **mọi** $x$. $\blacksquare$

### 4.3. Xác nhận số bổ sung — quét toàn bộ lưới `zero`

```python
def res(x,c):
    if x==0: return 1.0
    return min(1.0, c/x)

best = None
for zero in [i/200 for i in range(201)]:
    diffs = [abs(star(x) - res(x,zero)) for x in xs]
    m = max(diffs)
    if best is None or m < best[1]:
        best = (zero, m)
print("Zero khop nhat + sai so max:", best)
# Ket qua: (zero=0.02, sai_so_max≈0.268) — khong tien ve 0 tai bat ky zero nao
```

Sai số tối thiểu trên toàn lưới $201$ giá trị `zero` là $\approx0.268$ — xác nhận **không có `zero` nào** làm `star` khớp `res(·,zero)`, khớp hoàn toàn với chứng minh tay ở 4.2.

---

## 5. Kết luận & vai trò trong bài

$$\big([0,1],\ \max,\ \times,\ (1-\sqrt{\cdot})^{2},\ 0,\ 1\big)\ \text{là Polar Semiring, nhưng KHÔNG phải Bounded Girard Algebra.}$$

Điểm mấu chốt của ví dụ này (so với ví dụ đầy đủ $\Gamma(\mathbb R^n)$ trong `d2-compare-with-BGA.md`):

1. **Không cần bộ máy hàm lồi/extended-real** — mọi phần tử là số thực thật trong $[0,1]$, mọi phép toán là max/nhân thông thường.
2. **Residual không phải "không tồn tại"** — nó tồn tại (do $[0,1]$ đầy đủ + SM1), nhưng có **dạng cụ thể** $\min(1,c/x)$, và `star` phi tuyến ta chọn đơn giản **không thuộc họ đó với bất kỳ tham số nào**.
3. **Vai trò trong bài:** dùng làm ví dụ mở đầu ("ngay cả trên $[0,1]$, hiện tượng này đã xảy ra") trước khi trình bày $\Gamma(\mathbb R^n)$ như trường hợp *tự nhiên, không hề dàn dựng* — nơi `star` (Fenchel conjugate) không phải do ta chọn để phá residuation, mà là phép đối quan trọng bậc nhất của giải tích lồi, và nó **vẫn** thất bại residuation.
