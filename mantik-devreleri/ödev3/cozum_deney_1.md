# BLM2007 Mantık Devreleri — Deney Yaprağı 1 Çözümü
### BCD, Artı-3 ve Aiken Rakam Dönüştürücüsü

**Öğrenci:** Efe Özan (170425062)  
**Tarih:** 10.11.2026  
**Şube / Grup:** Ali Buldu A Grubu  
**İlgili Kodlar:** `rakam_donusturucu.py`, `dogrulama_1.py`

---

### 1. Kodlayıcı ve Çözümleyici Mimarisi

Dönüştürücü üç farklı rakam kodlama sistemini destekler:
1. **8421 BCD (Binary Coded Decimal):** Her onlu rakam doğrudan 4 bitlik ikili ağırlıklarla ($8, 4, 2, 1$) ifade edilir.
2. **Artı-3 (Excess-3):** Rakamın BCD karşılığına $0011_2$ (onlu 3) eklenerek oluşturulur ($d+3$). Ağırlıksız bir koddur.
3. **Standart Aiken 2421:** $2, 4, 2, 1$ ağırlıklarına sahip, kendinden tümleyen (self-complementing) standart sözlüktür.

**Hata Yönetimi ve Giriş Denetimi:**
- Boş girdi (`""`): `ValueError("Girdi boş olamaz.")` fırlatılır.
- Geçersiz karakter (`"48a"`): Rakam dışı karakterler `ValueError` ile gerekçeli reddedilir.
- Yanlış bit uzunluğu (`"01010"` - 5 bit): Bit dizisinin uzunluğu 4'ün katı olmadığında açık hata fırlatılır.
- Geçersiz sözcük (`"1111"` BCD'de): Sözlük dışı bloklar algılanıp onlu karşılığı ve neden reddedildiği raporlanır.

---

### 2. 48 ve 003 Dönüşümleri ile 263 Sayısı Analizi

#### A. 48 ve 003 Dönüşüm Tablosu
| Rakam Dizisi | 8421 BCD | Artı-3 (Excess-3) | Standart Aiken 2421 |
|:---:|:---:|:---:|:---:|
| `48` | `0100 1000` | `0111 1011` | `0100 1110` |
| `003` | `0000 0000 0011` | `0011 0011 0110` | `0000 0000 0011` |

Programda her iki dizi de hatasız kodlanmış ve çözümleyicilerle baştaki sıfırlar kaybedilmeden `48` ve `003` olarak geri çözülmüştür.

#### B. 263'ün Saf İkili vs BCD Gösterimi
- **Saf İkili Gösterim:** $263 = 256 + 4 + 2 + 1 = 100000111_2$ (**9 bit**).
- **BCD Gösterimi:** $2 \to 0010$, $6 \to 0110$, $3 \to 0011 \implies 001001100011_{BCD}$ (**12 bit**).
- **Karşılaştırma:** BCD gösterimi 12 bit harcayarak saf ikiliye göre $\%33.3$ daha fazla bellek kullanır.
- **Yanlış Kodla Okunması:** 12 bitlik BCD dizisi (`001001100011`) saf ikili olarak okunursa:
  $$2^9 + 2^6 + 2^5 + 2^1 + 2^0 = 512 + 64 + 32 + 2 + 1 = \mathbf{611_{10}}$$
  Sayının sayısal değeri 263 yerine 611 olarak tamamen yanlış algılanır.

---

### 3. 16 Dört Bit Deseninin Geçerlilik Taraması ve Aiken 0101 vs 1011

Tüm olası $2^4 = 16$ desen ($0000$ .. $1111$) tarandığında:
- **BCD (8421):**
  - Geçerli (10): `0000, 0001, 0010, 0011, 0100, 0101, 0110, 0111, 1000, 1001` (0--9)
  - Geçersiz (6): `1010, 1011, 1100, 1101, 1110, 1111` (10--15)
- **Artı-3:**
  - Geçerli (10): `0011, 0100, 0101, 0110, 0111, 1000, 1001, 1010, 1011, 1100` (3--12)
  - Geçersiz (6): `0000, 0001, 0010, 1101, 1110, 1111` (0--2 ve 13--15)
- **Standart Aiken (2421):**
  - Geçerli (10): `0000, 0001, 0010, 0011, 0100, 1011, 1100, 1101, 1110, 1111`
  - Geçersiz (6): `0101, 0110, 0111, 1000, 1001, 1010`

#### Aiken 0101 ve 1011 Ağırlıklı Toplam Kıyaslaması
$2421$ ağırlıklarıyla:
- `0101` $\to 0\cdot 2 + 1\cdot 4 + 0\cdot 2 + 1\cdot 1 = \mathbf{5}$
- `1011` $\to 1\cdot 2 + 0\cdot 4 + 1\cdot 2 + 1\cdot 1 = \mathbf{5}$

**Gerekçe:** Her iki desenin de ağırlıklı toplamı 5'tir. Fakat standart Aiken kodunda **kendinden tümleyen** (self-complementing) özelliği aranır. Bu kural gereği, bir rakam $d$ ile onun 9 tümleyeni olan $9-d$'nin kodları birbirinin 1 tümleyeni (tüm bitleri terslenmiş hali) olmak zorundadır. $4$ rakamının kodu `0100` olduğundan, $9-4 = 5$ rakamının kodu mutlaka `0100`'ın tersi olan `1011` olmalıdır. Bu sebeple `0101` sözlük dışı bırakılmıştır ve geçersizdir. Dolayısıyla bir desenin ağırlıklı toplamının 5 vermesi, onun standart Aiken kodunda geçerli olduğunu tek başına kanıtlamaz.

---

### 4. 9 Tümleyeni Doğrulaması ve BCD Karşı Örneği

0--9 arasındaki tüm rakamların bitleri terslendiğinde:
- **Artı-3 (10/10 Doğrulandı):** $d$ rakamı $d+3$ olarak kodlanır. 4 bitlik tersleme $15 - (d+3) = 12 - d = (9-d) + 3$ sonucunu verir. Bu da tanım gereği $9-d$'nin Artı-3 kodudur.
- **Standart Aiken (10/10 Doğrulandı):** Tablo simetrik kurulmuştur ($0 \leftrightarrow 9, 1 \leftrightarrow 8, 2 \leftrightarrow 7, 3 \leftrightarrow 6, 4 \leftrightarrow 5$).
- **BCD Karşı Örneği:** BCD kendinden tümleyen değildir (0/10).
  - Karşı örnek: $d = 2 \implies \text{BCD} = 0010$.
  - Bitleri terslenirse: `1101` ($13_{10}$). Bu sözcük BCD'de geçersizdir.
  - $9 - 2 = 7$'nin gerçek BCD kodu ise `0111`'dir ($1101 \ne 0111$).


### 0–9 dönüşüm tablosu

| Rakam | BCD | Artı-3 | Aiken |
|---|---|---|---|
| 0 | `0000` | `0011` | `0000` |
| 1 | `0001` | `0100` | `0001` |
| 2 | `0010` | `0101` | `0010` |
| 3 | `0011` | `0110` | `0011` |
| 4 | `0100` | `0111` | `0100` |
| 5 | `0101` | `1000` | `1011` |
| 6 | `0110` | `1001` | `1100` |
| 7 | `0111` | `1010` | `1101` |
| 8 | `1000` | `1011` | `1110` |
| 9 | `1001` | `1100` | `1111` |
