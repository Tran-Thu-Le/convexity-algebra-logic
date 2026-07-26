# Bảng đối chiếu ký hiệu: Polar Semiring (PS) <-> Bounded Girard Algebra (BGA)

Muc dich: chuan hoa 1 bo ky hieu Mace4 duy nhat de dung xuyen suot cac file
.in sau nay, phuc vu chung minh:

    BGA  =>  PS      (moi bounded Girard algebra deu la polar semiring)
    PS   =/=>  BGA    (khong phai polar semiring nao cung la bounded Girard algebra)

Quy uoc trang thai:
- **P**  = nguyen thuy (primitive) trong he do
- **D**  = dan xuat (derived) - co cong thuc dinh nghia tuong minh
- **—**  = KHONG co tuong ung (trong that su, day chinh la "khoang trong cau truc")

---

## Bang doi chieu day du

| # | Polar Semiring (PS) | Bounded Girard Algebra (BGA) | Ky hieu Mace4 thong nhat | Ghi chu |
|---|---|---|---|---|
| 1 | `^` — plus, **P** (idempotent, M0-M3) | `∨` (join), **P** | `^` | Trung khop truc tiep: ca hai deu la join cua lattice, cung dinh nghia thu tu `x^y=x` |
| 2 | `+` — tensor, **P** (S1-S3, SM1, SM2) | `·` (fusion/tensor), **P** | `+` | Trung khop truc tiep |
| 3 | `star` — polarity, **P** (P, PM) | `¬` — negation, **D**: `¬x := x → 0` | `star` | **Khac biet cau truc cot loi**: PS lay `star` la nguyen thuy; BGA phai *dan xuat* no tu `→` va `0` |
| 4 | `em` (unit cua `^`) = bottom, **P** | `⊥`, **D**: `⊥ := ¬⊤` | `em` | PS lay bottom la nguyen thuy; BGA dan xuat bottom tu top qua negation |
| 5 | `ez` (unit cua `+`), **P** | `1` (unit cua `·`), **P** | `ez` | Trung khop truc tiep |
| 6 | `with(x,y) := star(star(x)^star(y))`, **D** | `∧` (meet), **P** | `with` | PS dan xuat meet tu star+join; BGA lay meet la nguyen thuy (mot phan cua dinh nghia lattice) — **can kiem tra `with` co thoa cac luat hap thu (absorption) cua meet that su hay khong**, xem muc "Van de mo" ben duoi |
| 7 | `parr(x,y) := star(star(x)+star(y))`, **D** | `⅋(a,b) := ¬(¬a·¬b)`, **D** | `parr` | Trung khop cong thuc dan xuat 1-1 |
| 8 | — (khong co) | `→` — residual/linear implication, **P** | `res` (de xuat, infix `-o` neu can doc de) | **Khoang trong lon nhat cua PS**: khong co toan tu nao trong 11 tien de dong vai tro residuation `a·x ≤ b ⟺ x ≤ a→b` |
| 9 | `star(ez)`, **D** (neu dinh nghia duoc, xem ghi chu) | `0` — hang so dinh nghia negation, **P** | `zero` | Theo bai bao (Aglianò): `0 := ¬1`. Ap dung nguoc lai cho PS: neu dat `zero := star(ez)`, day la ung cu vien tu nhien cho `0` cua BGA — **nhung can chung minh (khong mac dinh) rang `star(x) = res(x, zero)` voi moi x, tuc la star phai KHOP voi residual-negation** |
| 10 | `star(em)`, **D** | `⊤` — top, **P** | `top` | PS dan xuat top tu bottom qua star (da thay xuat hien trong proof Prover9 truoc: `x ^ star(em) = star(em)`, tuc star(em) hap thu — dung tinh chat cua top) |
| 11 | thu tu: ma hoa qua `x^y=x`, khong co ky hieu rieng | thu tu: `≤` chuan cua lattice tu `∧,∨` | (khong can them ky hieu — dung quy uoc `x^y=x` cho ca hai he) | |

---

## Tom tat khoang trong

**Trong PS khong co (that su blank):**
- `→` (residual) — day la khoang trong DUY NHAT khong the lap day chi bang 11 tien de hien tai. Day chinh la thu can bo sung/chung minh de co gang di theo chieu PS ⟹ BGA (va rat co the se KHONG lap day duoc noi chung — do la ly do PS ⇏ BGA).

**Trong BGA khong co gi la "blank" so voi PS** — moi khai niem cua PS (`^,+,star,em,ez,with,parr`) deu co tuong ung truc tiep hoac dan xuat duoc trong BGA (cot 2 khong co dong nao la "—"). Day la dau hieu dinh tinh dau tien cho thay **BGA co cau truc giau hon PS mot cach nghiem ngat** (co them `→` nguyen thuy) — phu hop voi muc tieu chung minh BGA ⟹ PS.

---

## Chien luoc chung minh de xuat (dung bo ky hieu tren)

**Chieu BGA ⟹ PS** (du kien CHUNG MINH DUOC bang Prover9):
1. Dinh nghia trong Mace4/Prover9: `em:=bot`, `ez:=1`, `^:=join`, `+:=fusion`, `star(x):=neg(x)` (voi `neg(x):=res(x,zero)`), `with:=meet`, `parr(x,y):=neg(fusion(neg(x),neg(y)))`.
2. Tu tien de cua BGA (residuated lattice + 0 involutive + bounded), suy ra tung tien de M0-M3, S1-S3, SM1, SM2, P, PM bang Prover9 (giong cach da lam voi "chain forces D6" truoc day).
3. SM1 (`+` phan phoi qua `^`) se la he qua CHUAN cua residuation (adjoint bao toan join) — gan nhu chac chan chung minh duoc de dang.
4. P va PM se la he qua cua tinh chat involutive+antitonic cua negation da duoc chung minh trong bai bao (khong can chung minh lai tu dau, chi can dich sang Mace4 syntax).

**Chieu PS ⇏ BGA** (du kien BAC BO bang Mace4 — tim mo hinh phan vi du):
1. Dung dung mo hinh polar semiring da co san (vi du: Klein four-group phase semantics, hoac chinh cac mo hinh D2..D6 da tim duoc truoc day).
2. Thu dinh nghia `res(x,y) := with(star(x), y)` (cong thuc residual-tu-meet-va-negation tu nhien nhat co the nghi ra tu cac toan tu san co) roi kiem tra bang Mace4 xem no co thoa dieu kien residuation `x+a ^ b = b <-> a ^ res(x,b) = res(x,b)` (dang ma hoa cua `a·x≤b ⟺ x≤a→b`) hay khong.
3. Neu Mace4 tim duoc, voi MOI cach dinh nghia `res` hop ly, mot mo hinh PS ma dieu kien residuation bi vo — day chinh la chung minh hinh thuc (it nhat la phan vi du cu the) cho chieu PS ⇏ BGA.
4. Diem mau chot can kiem tra rieng: `with` (dinh nghia qua star) co luon thoa luat hap thu cua meet that su (`x with (x^y) = x` va `x ^ (x with y) = x`) hay khong — day la dieu kien can DE `<A,^,with>` la mot lattice thuc su (yeu cau bat buoc trong dinh nghia BGA). Neu Mace4 tim duoc mo hinh PS ma luat hap thu nay VO, thi PS thua nhan nhung cau truc khong phai la lattice — mot ly do doc lap va manh me hon de khang dinh PS ⇏ BGA.

---

## Van de mo can giai quyet o buoc tiep theo

1. `with` co luon thoa 2 luat hap thu cua lattice trong moi mo hinh PS hay khong? (chua kiem chung — de xuat chay Mace4 tim phan vi du truoc khi viet Prover9)
2. `res(x,y) := with(star(x),y)` co phai la cong thuc residual "dung" khong, hay can mot cong thuc khac? (Trong ly thuyet quantale, cong thuc chuan la `a→b := sup{x : a·x≤b}`, ma tren mien huu han se can duoc bieu dien qua mot phep join lon — Mace4 khong lam viec voi sup truc tiep nen se can ma hoa lai bang dang universally-quantified formula.)
3. Xac dinh xem SM1+SM2 (chi phan phoi qua join HUU HAN) co du manh de dam bao tinh chat residuation DAY DU (bao toan MOI join, ke ca join vo han neu mo hinh vo han) hay khong — voi mo hinh HUU HAN thi cau hoi nay thu gon thanh: SM1+SM2 co tuong duong voi "residual ton tai" hay khong (day la cau hoi dai so thuan tuy, co the giai bang ly thuyet gach noi adjoint functor cho lattice huu han, nhung can xac nhan lai bang Mace4/Prover9 truoc khi dua vao bai chung minh chinh).
