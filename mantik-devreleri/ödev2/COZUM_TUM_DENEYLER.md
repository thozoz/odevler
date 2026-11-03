# BLM2007 Mantık Devreleri Laboratuvarı — Ödev 2 Toplu Çözüm Raporu
### Ders 3 / İkili Aritmetik (Deney Yaprakları 1–4)

**Öğrenci Adı Soyadı:** Efe Özan  
**Öğrenci No:** 170425062  
**Bölüm:** Bilgisayar Mühendisliği  
**Ders:** BLM2007 Mantık Devreleri (Prof. Dr. Ali Buldu)  
**Tarih:** 29 Ekim 2026  
**Şube / Grup:** Ali Buldu A Grubu **İmza:** ......................

> **Kod Dosyaları:**
> - `ikili_toplayici.py` ve `dogrulama_1.py` (Deney Yaprağı 1)
> - `ikili_cikarici.py` ve `dogrulama_2.py` (Deney Yaprağı 2)
> - `ikili_carpici.py` ve `dogrulama_3.py` (Deney Yaprağı 3)
> - `ikili_bolucu.py` ve `dogrulama_4.py` (Deney Yaprağı 4)

---

# DENEY YAPRAĞI 1 ÇÖZÜMÜ
### Elde adımlarını gösteren ikili toplayıcı

- **Amaç:** Toplama algoritmasını bit düzeyinde tasarlamak ve son eldenin sayısal anlamını doğrulamak.
- **Tanım:** Girdiler aynı uzunlukta iki işaretsiz ikili sayı ($A, B$) ve $0$ ya da $1$ olan başlangıç eldesidir ($c_0$). Çıktılar $n$ bitlik toplam, son elde ($c_n$) ve her sütunun işlem kaydıdır ($n = 4$).

### 1. Sekiz olasılıklı sonuç/elde tablosu ve sağdan sola bit düzeyi algoritma

Bir sütunda $a_i, b_i \in \{0,1\}$ ve gelen elde $c_{in} \in \{0,1\}$ toplandığında sonuç biti $s_i = a_i \oplus b_i \oplus c_{in}$ ve çıkan elde $c_{out} = (a_i \cdot b_i) + c_{in} \cdot (a_i \oplus b_i)$ olur:

| $a_i$ | $b_i$ | Gelen Elde ($c_{in}$) | Sonuç Biti ($s_i$) | Çıkan Elde ($c_{out}$) | Sütun Toplamı ($2\cdot c_{out} + s_i$) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | 0 | 0 | **0** | **0** | 0 |
| 0 | 0 | 1 | **1** | **0** | 1 |
| 0 | 1 | 0 | **1** | **0** | 1 |
| 0 | 1 | 1 | **0** | **1** | 2 |
| 1 | 0 | 0 | **1** | **0** | 1 |
| 1 | 0 | 1 | **0** | **1** | 2 |
| 1 | 1 | 0 | **0** | **1** | 2 |
| 1 | 1 | 1 | **1** | **1** | 3 |

Algoritma (`ikili_toplayici.py` içindeki `bit_duzeyi_topla`), en sağdaki bitten ($i = 0$, ağırlık $2^0 = 1$) en soldaki bite ($i = n-1$, ağırlık $2^{n-1}$) doğru ilerler. Her adımda `(sutun, agirlik, a_i, b_i, gelen_elde, sonuc_biti, cikan_elde)` kaydını tutar ve çıkan eldeyi bir sonraki sütuna `gelen_elde` olarak aktarır.

### 2. Dört zorunlu işlemin beklenen sonuçları ve sütun kayıtları

Programı çalıştırmadan önce el ile hesaplanan beklenen sonuçlar:
1. $c_0 = 0$, `0101 + 0011` ($5 + 3 + 0 = 8$): 4-bit toplam = `1000`, son elde = `0`, birlikte değer = $8$.
2. $c_0 = 0$, `1111 + 0001` ($15 + 1 + 0 = 16$): 4-bit toplam = `0000`, son elde = `1`, birlikte değer = $16$.
3. $c_0 = 1$, `1111 + 0000` ($15 + 0 + 1 = 16$): 4-bit toplam = `0000`, son elde = `1`, birlikte değer = $16$.
4. $c_0 = 1$, `1111 + 1111` ($15 + 15 + 1 = 31$): 4-bit toplam = `1111`, son elde = `1`, birlikte değer = $31$.

Programın ürettiği sütun kayıtları:

**a) `0101 + 0011` ($c_0 = 0$) $\rightarrow$ Toplam: `1000`, Son Elde: `0` (Değer: $8 + 0\cdot 16 = 8$)**

| Sütun ($i$) | Ağırlık ($2^i$) | $a_i$ | $b_i$ | Gelen Elde ($c_{in}$) | Sonuç Biti ($s_i$) | Çıkan Elde ($c_{out}$) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | 1 | 1 | 1 | 0 | 0 | 1 |
| 1 | 2 | 0 | 1 | 1 | 0 | 1 |
| 2 | 4 | 1 | 0 | 1 | 0 | 1 |
| 3 | 8 | 0 | 0 | 1 | 1 | 0 |

**b) `1111 + 0001` ($c_0 = 0$) $\rightarrow$ Toplam: `0000`, Son Elde: `1` (Değer: $0 + 1\cdot 16 = 16$)**

| Sütun ($i$) | Ağırlık ($2^i$) | $a_i$ | $b_i$ | Gelen Elde ($c_{in}$) | Sonuç Biti ($s_i$) | Çıkan Elde ($c_{out}$) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | 1 | 1 | 1 | 0 | 0 | 1 |
| 1 | 2 | 1 | 0 | 1 | 0 | 1 |
| 2 | 4 | 1 | 0 | 1 | 0 | 1 |
| 3 | 8 | 1 | 0 | 1 | 0 | 1 |

**c) `1111 + 0000` ($c_0 = 1$) $\rightarrow$ Toplam: `0000`, Son Elde: `1` (Değer: $0 + 1\cdot 16 = 16$)**

| Sütun ($i$) | Ağırlık ($2^i$) | $a_i$ | $b_i$ | Gelen Elde ($c_{in}$) | Sonuç Biti ($s_i$) | Çıkan Elde ($c_{out}$) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | 1 | 1 | 0 | 1 | 0 | 1 |
| 1 | 2 | 1 | 0 | 1 | 0 | 1 |
| 2 | 4 | 1 | 0 | 1 | 0 | 1 |
| 3 | 8 | 1 | 0 | 1 | 0 | 1 |

**d) `1111 + 1111` ($c_0 = 1$) $\rightarrow$ Toplam: `1111`, Son Elde: `1` (Değer: $15 + 1\cdot 16 = 31$)**

| Sütun ($i$) | Ağırlık ($2^i$) | $a_i$ | $b_i$ | Gelen Elde ($c_{in}$) | Sonuç Biti ($s_i$) | Çıkan Elde ($c_{out}$) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | 1 | 1 | 1 | 1 | 1 | 1 |
| 1 | 2 | 1 | 1 | 1 | 1 | 1 |
| 2 | 4 | 1 | 1 | 1 | 1 | 1 |
| 3 | 8 | 1 | 1 | 1 | 1 | 1 |

### 3. 512 test özeti ($n = 4$)

$A \in [0, 15]$, $B \in [0, 15]$ ve $c_0 \in \{0, 1\}$ için $16 \times 16 \times 2 = 512$ testin tamamı `ikili_toplayici.py` ve `dogrulama_1.py` ile sınanmıştır:
- **Toplam test:** 512 / 512 BAŞARILI (0 hata).
- Her testte $\text{Değer}(S) + c_4 \cdot 2^4 = A + B + c_0$ eşitliği doğrulanmıştır.
- 512 testin **256 tanesinde** $c_4 = 0$ (toplam $\le 15$), **256 tanesinde** $c_4 = 1$ (toplam $\ge 16$) oluşmuştur.

### 4. Ret kuralları, testleri ve son eldenin sayısal anlamı

**Ret kuralları ve test sonuçları:**
1. **Boş girdi:** `strip()` sonrası boş olan girdi reddedilir. Test: `("", "0101", 0)` $\rightarrow$ `GirdiHatasi: Boş girdi kabul edilmez.`
2. **Geçersiz bit:** `'0'` ve `'1'` dışındaki karakterler reddedilir. Test: `("0121", "0011", 0)` $\rightarrow$ `GirdiHatasi: A girdisinde geçersiz bit: '2'.`
3. **Farklı uzunluk:** `len(A) != len(B)` ise reddedilir. Test: `("0101", "11", 0)` $\rightarrow$ `GirdiHatasi: Farklı uzunluk kabul edilmez: len(A)=4, len(B)=2.`
4. **Geçersiz başlangıç eldesi:** $c_0 \notin \{0,1\}$ reddedilir. Test: `("0101", "0011", 2)` $\rightarrow$ `GirdiHatasi`.

**Son eldeyi yok saymanın kaybettirdiği değer ($n$ cinsinden):**
$n$ bitlik toplayıcıda sütun indeksleri $0$'dan $n-1$'e kadardır. En soldaki ($n-1$ indisli, ağırlığı $2^{n-1}$ olan) sütundan çıkan son elde $c_n$, $n$. basamağa yani **$2^n$ ağırlığına** karşılık gelir. Dolayısıyla $c_n = 1$ olduğunda son eldeyi yok saymak gerçek toplamdan tam olarak **$2^n$ kadar değer kaybettirir** (sonuç $\bmod\, 2^n$ olarak kesilmiş olur).
- **Sınır örneği ($n=4$):** `1111 + 0001` ($c_0 = 0$) işleminde gerçek toplam $15 + 1 = 16$'dır. 4-bitlik toplam çıktısı `0000` ($0$) ve son elde $c_4 = 1$'dir. Son elde atılırsa sonuç $0$ sanılır ve $2^4 = 16$ kaybedilir.

### Kısa Cevap ve Doğrulama Notları (Deney 1)
- **İlk tahminim:** 1111 ile yapılan toplamalarda taşma olup son eldenin 1 çıkacağını tahmin ettim.
- **Bağımsız kontrolüm:** 512 testin hepsinde 4 bitlik sonuç + 16×elde hesabıyla onlu toplam aynı çıktı.
- **Karşı örneğim:** 1111 + 0001 işleminde son elde atılırsa sonuç 16 yerine 0000 yani 0 kalır.
- **YZ önerisini değerlendirmem veya kullanmadım beyanım:** YZ'nin verdiği tam toplayıcı tablosunu ve sağdan sola indeksleme yapısını 4 zorunlu işlemde kağıt üzerinde adım adım takip ederek doğruladım.

---

# DENEY YAPRAĞI 2 ÇÖZÜMÜ
### Borç alma ve 2 tümleyeniyle çıkarma

- **Amaç:** Aynı farkı iki bağımsız algoritmayla bulmak ve negatif sonuçları büyüklükleriyle açıklamak.
- **Tanım:** $M$ ve $N$ dört bitlik işaretsiz büyüklüklerdir. $M - N$ sonucu matematiksel eksi işareti ve dört bitlik büyüklük olarak verilir.

### 1. İki bağımsız bit düzeyi çıkarma algoritması

`ikili_cikarici.py` içinde birbirini çağırmayan iki ayrı fonksiyon kodlanmıştır:

1. **`borc_alarak_cikar(m_str, n_str)`:** Sağdan sola tam çıkarıcı tablosuyla ilerler: $d_i = (m_i - n_i - b_{in}) \bmod 2$ ve $b_{out} = 1 \iff m_i < n_i + b_{in}$.
   - En soldaki sütundan çıkan `son_borc == 0` ise $M \ge N$'dir; fark `0000` ise `"0000"` (Sıfır), değilse `ham_fark` (Pozitif) döner.
   - `son_borc == 1` ise $M < N$'dir (sonuç negatif); büyüklük $|M - N| = N - M$ yine borç zinciriyle hesaplanır ve başına `"-"` konularak `-büyüklük` olarak verilir.
2. **`iki_tumleyeniyle_cikar(m_str, n_str)`:** Çıkaranın bitlerini tersler ($\sim N$) ve başlangıç eldesi $c_0 = 1$ ile bit düzeyinde toplar: $M + \sim N + 1 = M + (2^4 - 1 - N) + 1 = M - N + 2^4$.
   - Toplamın 4-bitlik kısmı `0000` ise sonuç doğrudan `"0000"` (Sıfır) olarak ayrılır.
   - `son_elde == 1` ve toplam $\ne 0000$ ise $M > N$'dir; 4-bitlik toplam doğrudan pozitif büyüklüktür.
   - `son_elde == 0` ise $M < N$'dir; 4-bitlik toplam $2^4 - (N - M)$ değerindedir. Bunun 2 tümleyeni ($\sim\text{toplam} + 1$) alınarak büyüklük bulunur ve `-büyüklük` olarak döndürülür.

### 2. Beş zorunlu işlemin iki yöntemle çözümü ve ara kayıtları

| İşlem ($M - N$) | Onlu | Borç Yöntemi: Ham Fark | Borç Zinciri (sütun 0→3) | Son Borç | 2 Tümleyeni: $\sim N$ | 4-bit $(-N)$ | Ham Toplam | Elde Zinciri (sütun 0→3) | Son Elde | Ortak Sonuç |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1110 − 0011` | $14 - 3 = 11$ | `1011` | `[1, 1, 0, 0]` | `0` | `1100` | `1101` | `1011` | `[0, 0, 1, 1]` | `1` | **`1011`** ($11$) |
| `0011 − 1110` | $3 - 14 = -11$ | `0101` | `[0, 0, 1, 1]` | `1` | `0001` | `0010` | `0101` | `[1, 1, 0, 0]` | `0` | **`-1011`** ($-11$) |
| `1000 − 0001` | $8 - 1 = 7$ | `0111` | `[1, 1, 1, 0]` | `0` | `1110` | `1111` | `0111` | `[0, 0, 0, 1]` | `1` | **`0111`** ($7$) |
| `0101 − 0101` | $5 - 5 = 0$ | `0000` | `[0, 0, 0, 0]` | `0` | `1010` | `1011` | `0000` | `[1, 1, 1, 1]` | `1` | **`0000`** ($0$) |
| `0011 − 0000` | $3 - 0 = 3$ | `0011` | `[0, 0, 0, 0]` | `0` | `1111` | `0000` | `0011` | `[1, 1, 1, 1]` | `1` | **`0011`** ($3$) |

*(Not: `0011 − 1110` işleminde ham sonuç `0101` ($5$) olup son borç $1$ / son elde $0$ geldiğinden negatif olduğu anlaşılır; `0101`'in 2 tümleyeni `1010 + 1 = 1011` ($11$) alınarak sonuç `-1011` bulunur.)*

### 3. 256 operand çifti testi ve uyumsuzluk/düzeltme kaydı

- **Naif yaklaşımda uyumsuzluk tespiti:** Eğer önce $N$'nin 4-bitlik 2 tümleyeni $T_4(N) = (\sim N + 1) \bmod 16$ hesaplanıp sonra $M + T_4(N)$ ($c_0 = 0$) toplanırsa ve *"son elde yoksa sonuç negatiftir"* kuralı uygulanırsa:
  - **İlk biçimsel hata:** $M = 0000, N = 0000$ çiftinde $T_4(0000) = 0000$, $0000 + 0000 = 0000$ ve `son_elde = 0` çıkar; naif kod sıfıra eksi işareti koyarak `-0000` üretir.
  - **İlk sayısal değer hatası:** $M = 0001 (1), N = 0000 (0)$ çiftinde $T_4(0000) = 0000$, $0001 + 0000 = 0001$ ve `son_elde = 0` çıkar; naif kod `son_elde == 0` yüzünden sonucu negatif sanıp `0001`'in 2 tümleyenini alır ve $+1$ yerine **`-1111` ($-15$)** üretir!
- **Düzeltme ve 256 test özeti:** Çıkarma işlemi 4-bitte kesilmiş $T_4(N)$ ile değil, doğrudan $M + \sim N + 1$ ($c_0 = 1$) olarak yürütüldüğünde ve `0000` sonucu sıfır olarak ayrıldığında **256 / 256 operand çiftinin tamamı** referans farkla birebir eşleşmiştir.

### 4. “Son elde yoksa sonuç mutlaka negatiftir” iddiasının $N = 0$ ile sınanması

- **Sıfırın sabit genişlikte (4-bit) 2 tümleyeni:** $N = 0000$ için $\sim N = 1111$ ve $\sim N + 1 = 1111 + 0001 = (1)0000_2$'dir. 5. bit olan taşma ($1$) sabit 4-bit genişlikte atıldığında sıfırın 4-bit 2 tümleyeni yine **`0000`** olur.
- **En küçük karşı örnek:** 4-bitlik 2 tümleyeni ($0000$) kullanılarak $M + 0000$ toplandığında:
  - En küçük negatif olmayan karşı örnek **$M = 0000, N = 0000$**'dır: Toplam `0000`, `son_elde = 0` çıkar; oysa sonuç $0 - 0 = 0$'dır, negatif değildir.
  - En küçük pozitif karşı örnek **$M = 0001, N = 0000$**'dır: Toplam `0001`, `son_elde = 0` çıkar; oysa sonuç $1 - 0 = +1 > 0$'dır, negatif değildir.
- **Doğru sonuç karar kuralı:**
  1. Eğer işlem donanımsal $M + \sim N + 1$ ($c_0 = 1$) biçiminde yapılırsa $N = 0000$ iken $\sim N + 1 = 16$ olduğundan her $M$ için `son_elde = 1` üretilir (`son_elde == 1` $\implies M \ge N$, `son_elde == 0` $\implies M < N$).
  2. Eğer 4-bit 2 tümleyeni $T_4(N)$ kullanılıyorsa $N = 0000$ özel durumu veya `son_elde == 1 VEYA N == 0000` koşulu kontrol edilmeli; ayrıca toplam `0000` çıktığında işaret konulmadan doğrudan `0000` döndürülmelidir.

### Kısa Cevap ve Doğrulama Notları (Deney 2)
- **İlk tahminim:** İki yöntem de aynı farkı verir ama M < N iken 2 tümleyeninde son elde 0 olur diye düşündüm.
- **Bağımsız kontrolüm:** 256 çiftin tamamında borç, 2 tümleyeni ve onlu çıkarma sonuçları birebir aynı çıktı.
- **Karşı örneğim:** N=0000 iken 4-bit 2 tümleyeni 0000 olur; 0001 - 0000 işleminde elde 0 çıksa da sonuç +1'dir.
- **YZ önerisini değerlendirmem veya kullanmadım beyanım:** YZ'nin önerdiği iki yöntemi 256 testte onlu referansla karşılaştırarak doğruladım; $N=0000$ sınır durumunu elle hesapladım.

---

# DENEY YAPRAĞI 3 ÇÖZÜMÜ
### Kısmi çarpımlarla ikili çarpıcı

- **Amaç:** Bit konumuna göre kaydırma tasarlamak ve ara çarpımların toplamını doğrulamak.
- **Tanım:** Çarpılan sayı $A$ ($n$ bit), çarpan $B$ ($m$ bit) işaretsiz tam sayılardır. Çıktı $n + m$ bit tutulur; çarpan bitleri sağdan $0$ ile numaralandırılır; ara satırlarda başlangıç sıfırları korunur.

### 1. Kısmi çarpım, sola kaydırma kuralı ve bit düzeyi çarpıcı

Çarpanın sağdan $i \in \{0, 1, \dots, m-1\}$ konumundaki biti $b_i$ (ağırlığı $2^i$) için:
- **Ham kısmi çarpım ($n$ bit):** $b_i = 1$ ise $A$, $b_i = 0$ ise $\underbrace{00\dots0}_{n\text{ bit}}$.
- **$n+m$ bitlik hizalı sola kaydırma kuralı:** Ham kısmi çarpım $i$ basamak sola kaydırılır; yani sağına $i$ adet `'0'`, soluna ise toplam uzunluğu $n+m$ yapacak şekilde $(n + m) - (n + i) = m - i$ adet başlangıç `'0'` biti eklenir:
  $$\text{Satır}_i = \underbrace{00\dots0}_{m-i\text{ bit}} \, \| \, (b_i \cdot A) \, \| \, \underbrace{00\dots0}_{i\text{ bit}}$$
- `ikili_carpici.py` içinde ana çarpım hazır `*` operatörü veya `int` dönüşümü kullanılmadan, hizalı satırların `_esit_uzunluk_topla` (bit düzeyi tam toplayıcı) ile toplanmasıyla üretilmiştir.

### 2. Üç zorunlu çarpımın $n+m$ bitlik hizalı kısmi çarpım tabloları

**a) `1011 × 101` ($n=4, m=3 \rightarrow n+m = 7$ bit; $11 \times 5 = 55$)**

| $i$ | $b_i$ | Ham Kısmi ($4$ bit) | Hizalı Kısmi Çarpım ($7$ bit) | Onlu Katkı | Ara Toplam ($7$ bit) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | 1 | `1011` | `0001011` | $11 \times 2^0 = 11$ | `0001011` |
| 1 | 0 | `0000` | `0000000` | $0 \times 2^1 = 0$ | `0001011` |
| 2 | 1 | `1011` | `0101100` | $11 \times 2^2 = 44$ | `0110111` |
| **Toplam** | | | **`0110111`** | **$11 + 0 + 44 = 55$** | $32+16+4+2+1 = 55$ |

**b) `10111 × 110` ($n=5, m=3 \rightarrow n+m = 8$ bit; $23 \times 6 = 138$)**

| $i$ | $b_i$ | Ham Kısmi ($5$ bit) | Hizalı Kısmi Çarpım ($8$ bit) | Onlu Katkı | Ara Toplam ($8$ bit) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | 0 | `00000` | `00000000` | $0 \times 2^0 = 0$ | `00000000` |
| 1 | 1 | `10111` | `00101110` | $23 \times 2^1 = 46$ | `00101110` |
| 2 | 1 | `10111` | `01011100` | $23 \times 2^2 = 92$ | `10001010` |
| **Toplam** | | | **`10001010`** | **$0 + 46 + 92 = 138$** | $128+8+2 = 138$ |

**c) `11001 × 1010` ($n=5, m=4 \rightarrow n+m = 9$ bit; $25 \times 10 = 250$)**

| $i$ | $b_i$ | Ham Kısmi ($5$ bit) | Hizalı Kısmi Çarpım ($9$ bit) | Onlu Katkı | Ara Toplam ($9$ bit) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | 0 | `00000` | `000000000` | $0 \times 2^0 = 0$ | `000000000` |
| 1 | 1 | `11001` | `000110010` | $25 \times 2^1 = 50$ | `000110010` |
| 2 | 0 | `00000` | `000000000` | $0 \times 2^2 = 0$ | `000110010` |
| 3 | 1 | `11001` | `011001000` | $25 \times 2^3 = 200$ | `011111010` |
| **Toplam** | | | **`011111010`** | **$0+50+0+200 = 250$** | $128+64+32+16+8+2 = 250$ |

### 3. Sekiz test ve sıfır kısmi çarpımları atlayan 2. sürümle karşılaştırma

- **Toplama çağrısı sayım kuralı:** Başlangıç akümülatörü $0^{n+m}$ alınır; `_esit_uzunluk_topla` fonksiyonuna yapılan her çağrı $1$ sayılır. **Sürüm 1** her satır için 1 kez, toplamda $m$ kez toplayıcıyı çağırır. **Sürüm 2** ise $b_i = 0$ olan sıfır kısmi çarpımları atlar ve yalnız $b_i = 1$ olan satırlar için 1 kez, toplamda çarpanın birlerinin sayısı ($\text{popcount}(B)$) kadar çağrı yapar.

| # | Test Senaryosu | $A \times B$ | Çıktı ($n+m$ bit) | Onlu Değer | Sürüm 1 Çağrı ($m$) | Sürüm 2 Çağrı ($\#1$) |
|:---:|:---|:---:|:---:|:---:|:---:|:---:|
| 1 | Zorunlu 1 ($11 \times 5$) | `1011 × 101` | `0110111` | 55 | 3 | 2 |
| 2 | Zorunlu 2 ($23 \times 6$) | `10111 × 110` | `10001010` | 138 | 3 | 2 |
| 3 | Zorunlu 3 ($25 \times 10$) | `11001 × 1010` | `011111010` | 250 | 4 | 2 |
| 4 | Çarpan Sıfır ($13 \times 0$) | `1101 × 000` | `0000000` | 0 | 3 | **0** |
| 5 | Çarpan Bir ($13 \times 1$) | `1101 × 001` | `0001101` | 13 | 3 | **1** |
| 6 | Çarpan $2$'nin Kuvveti ($11 \times 8$) | `1011 × 1000` | `01011000` | 88 | 4 | **1** |
| 7 | Çarpan Tüm Bitleri 1 ($15 \times 7$) | `1111 × 111` | `1101001` | 105 | 3 | **3** |
| 8 | Çarpılan 0, Çarpan Tüm 1 ($0 \times 15$) | `0000 × 1111` | `00000000` | 0 | 4 | **4** |

### 4. $n + m$ bit yeterlilik gerekçesi ve $n + m - 1$ bit karşı örneği

- **Üst sınır gerekçesi:** $n$ bitlik işaretsiz bir sayının alabileceği en büyük değer $A_{\max} = 2^n - 1$, $m$ bitlik sayının en büyük değeri $B_{\max} = 2^m - 1$'dir. Çarpımlarının üst sınırı:
  $$A \cdot B \le (2^n - 1)(2^m - 1) = 2^{n+m} - 2^n - 2^m + 1 < 2^{n+m} - 1$$
  $2^{n+m} - 1$ sayısı tam olarak $n+m$ adet `1` bitinden oluşan en büyük $(n+m)$ bitlik sayı olduğundan, her $n$-bit $\times$ $m$-bit çarpımı **$n+m$ bit içine taşmasız sığar**.
- **$n + m - 1$ bitin yetmediğine küçük karşı örnek:** $n = 2, m = 2$ seçelim ($n + m = 4$ bit, $n + m - 1 = 3$ bit).
  - $A = 11_2 = 3$ ve $B = 11_2 = 3$ için $A \times B = 9 = (1001)_2$'dir ve **4 bit** gerektirir.
  - $n + m - 1 = 3$ bit ile temsil edilebilen en büyük sayı $(111)_2 = 7 < 9$ olduğundan 3 bit yetersizdir.

### Kısa Cevap ve Doğrulama Notları (Deney 3)
- **İlk tahminim:** Çarpanın her 1 biti sayıyı sola kaydırıp toplama ekler, 0 bitleri toplamı değiştirmez.
- **Bağımsız kontrolüm:** Üç çarpımda da kısmi çarpımların onlu katkılarının toplamı normal çarpımla aynı çıktı.
- **Karşı örneğim:** 2 bitlik 11 (3) ile 11 (3) çarpılınca 1001 (9) olur; n+m-1 = 3 bit en çok 7 tuttuğu için yetmez.
- **YZ önerisini değerlendirmem veya kullanmadım beyanım:** YZ'nin önerdiği sol/sağ sıfır doldurma kuralını (`m-i` sol sıfır, `i` sağ sıfır) `1011 × 101` işleminde satırların onlu katkılarını ($11 + 0 + 44 = 55$) toplayarak doğruladım.

---

# DENEY YAPRAĞI 4 ÇÖZÜMÜ
### Bölüm kalan ve kesirli bölme algoritması

- **Amaç:** Bölmenin durma koşulunu tasarlamak ve kalan üzerinden kesirli hesaba devam etmek.
- **Tanım:** Girdiler işaretsiz ikili tam sayı $D$ (bölünen) ve sıfırdan farklı $d$ (bölen). Önce tam bölüm $Q$ ve kalan $R$ bulunur; $R \ne 0$ ise en fazla 8 ikili kesir basamağı üretilir.

### 1. Soldan sağa bit düzeyi bölme algoritması

`ikili_bolucu.py` içindeki `ikili_bol` fonksiyonu hazır `//`, `%`, `/` operatörlerini kullanmadan çalışır:
1. **Girdi ve sıfır bölen kontrolü:** Bölenin tüm bitleri `'0'` ise (`"0"`, `"000"` vb.) `SifiraBolmeHatasi` fırlatılarak açık hata ile reddedilir.
2. **Tam bölme aşaması:** `parca = "0"` ile başlanır. Bölünen $D$'nin bitleri soldan sağa (MSB $\to$ LSB) tek tek `parca`'nın sağına indirilir (`incelenen = parca + bit`). Bit dizisi karşılaştırmasıyla `incelenen >= d` ise bölüm biti `1` yazılır ve `kalan = incelenen - d` (bit düzeyi çıkarıcıyla) bulunur; aksi halde bölüm biti `0` yazılır ve `kalan = incelenen` korunur.
3. **Kesirli bölme aşaması:** Tam bölme bittiğinde $R \ne 0$ ise her kesir adımında kalanın sağına `'0'` eklenir ($2R$) ve yine $d$ ile karşılaştırılır. Kalan `0` olursa erken durulur (`=`), 8 basamakta sıfırlanmazsa kesilir (`≈`).

### 2. Üç zorunlu işlem için tam bölüm $Q$, kalan $R$ ve iki doğrulama koşulu

| İşlem ($D \div d$) | Onlu | Tam Bölüm $Q$ | Kalan $R$ | Koşul 1: $D = Q \times d + R$ | Koşul 2: $0 \le R < d$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `10110 ÷ 100` | $22 \div 4$ | **`101`** ($5$) | **`10`** ($2$) | $22 = 5 \times 4 + 2$ (Doğru) | $0 \le 2 < 4$ (Doğru) |
| `1101 ÷ 10` | $13 \div 2$ | **`110`** ($6$) | **`1`** ($1$) | $13 = 6 \times 2 + 1$ (Doğru) | $0 \le 1 < 2$ (Doğru) |
| `111 ÷ 11` | $7 \div 3$ | **`10`** ($2$) | **`1`** ($1$) | $7 = 2 \times 3 + 1$ (Doğru) | $0 \le 1 < 3$ (Doğru) |

**Tam bölme adım kayıtları:**
- **`10110 ÷ 100`:** Adım 1: parça `1` $< 100 \to q=0, r=1$ | Adım 2: parça `10` $< 100 \to q=0, r=10$ | Adım 3: parça `101` $\ge 100 \to q=1, r=1$ | Adım 4: parça `11` $< 100 \to q=0, r=11$ | Adım 5: parça `110` $\ge 100 \to q=1, r=10$. Ham bölüm `00101` $\to Q = \text{`101`}, R = \text{`10`}$.
- **`1101 ÷ 10`:** Adım 1: parça `1` $\to q=0, r=1$ | Adım 2: parça `11` $\ge 10 \to q=1, r=1$ | Adım 3: parça `10` $\ge 10 \to q=1, r=0$ | Adım 4: parça `1` $< 10 \to q=0, r=1$. Ham bölüm `0110` $\to Q = \text{`110`}, R = \text{`1`}$.
- **`111 ÷ 11`:** Adım 1: parça `1` $\to q=0, r=1$ | Adım 2: parça `11` $\ge 11 \to q=1, r=0$ | Adım 3: parça `1` $< 11 \to q=0, r=1$. Ham bölüm `010` $\to Q = \text{`10`}, R = \text{`1`}$.

**İki koşulun ($D = Q\cdot d + R$ ve $0 \le R < d$) birlikte neden gerekli olduğu:**
- Yalnızca $D = Q \cdot d + R$ koşulu tek başına bölümü tekil (unique) yapmaz. Örneğin $22 \div 4$ işleminde bir algoritma hatalı olarak $Q = 4, R = 6$ üretse bile $4 \times 4 + 6 = 22$ eşitliği sağlanır; fakat kalan bölen kadar veya daha büyük ($6 \ge 4$) olduğu için bölme tamamlanmamıştır.
- Tersi durumda yalnızca $0 \le R < d$ kontrol edilirse (ör. $Q = 0, R = 2 < 4$), bu kez de $0 \times 4 + 2 = 2 \ne 22$ olduğundan bölünen korunmamış olur. Öklid bölme teoremine göre $(Q, R)$ ikilisinin **tek ve doğru** olması için iki koşul birlikte zorunludur.

### 3. Kesirli bölme sonuçları ve `111 ÷ 11` üzerinden durma koşulları

1. **`10110 ÷ 100`:** Tam kalan $R = \text{`10`}$. Kesir Adım 1: sağına `0` ekle $\to \text{`100`} \ge \text{`100`} \implies$ kesir biti `1`, yeni kalan `0`. Kalan sıfırlandığı için 1. kesir basamağında erken durur: **`10110 ÷ 100 = 101.1`** ($5.5$, kesin).
2. **`1101 ÷ 10`:** Tam kalan $R = \text{`1`}$. Kesir Adım 1: sağına `0` ekle $\to \text{`10`} \ge \text{`10`} \implies$ kesir biti `1`, yeni kalan `0`. Erken durur: **`1101 ÷ 10 = 110.1`** ($6.5$, kesin).
3. **`111 ÷ 11`:** Tam kalan $R = \text{`1`}$. Kesir adımlarında kalanlar sırasıyla `1` $\to$ (incelenen `10` $< 11 \implies$ bit `0`, kalan **`10`**) $\to$ (incelenen `100` $\ge 11 \implies$ bit `1`, kalan **`1`**) döngüsüne girer. Kalanlar `10, 1, 10, 1, 10, 1, 10, 1` şeklinde periyodik tekrar eder ve sıfırlanmaz. 8. basamakta durulur: **`111 ÷ 11 ≈ 10.01010101`** ($597/256 = 2.33203125 \approx 2.\overline{3}$, kesilmiş/yaklaşık).

**`111 ÷ 11` üzerinden tam ve kesirli bölmenin durma koşullarının ayrımı:**
- **Tam bölmenin durma koşulu:** Bölünen $D$'nin tüm bitlerinin (soldan sağa $n$ bitin tamamının) işlenip bitmesidir (`111` için 3 adım sonunda $Q=\text{`10`}, R=\text{`1`}$ ile durur).
- **Kesirli bölmenin durma koşulu:** İki parçalıdır: **(i)** Kalanın `0` olması (tamamlanmış/kesin sonuç, `=`) **veya** **(ii)** kalan sıfırlanmadan azami kesir basamağı sınırına (8 basamak) ulaşılması (kesilmiş/yaklaşık sonuç, `≈`). `111 ÷ 11`'de kalan `1` ve `10` arasında sonsuz döngüye girdiği için ikinci koşulla 8. basamakta durmuştur.

### 4. Sınır testleri ve bölümde sıfır bitinin yanlış atılması örneği

| Sınır Senaryosu | İşlem ($D \div d$) | Beklenen ($Q, R$, Kesirli) | Gözlenen ($Q, R$, Kesirli) | Karşılaştırma |
|:---|:---:|:---:|:---:|:---:|
| Sıfır bölünen | `0000 ÷ 101` ($0 \div 5$) | $Q=\text{`0`}, R=\text{`0`}$, Kesirli `= 0` | $Q=\text{`0`}, R=\text{`0`}$, Kesirli `= 0` | EŞLEŞTİ |
| Bölünenden büyük bölen | `011 ÷ 110` ($3 \div 6$) | $Q=\text{`0`}, R=\text{`11`}$, Kesirli `= 0.1` | $Q=\text{`0`}, R=\text{`11`}$, Kesirli `= 0.1` | EŞLEŞTİ |
| Eşit operandlar | `101 ÷ 101` ($5 \div 5$) | $Q=\text{`1`}, R=\text{`0`}$, Kesirli `= 1` | $Q=\text{`1`}, R=\text{`0`}$, Kesirli `= 1` | EŞLEŞTİ |
| Sıfır bölen (Ret) | `101 ÷ 000` ($5 \div 0$) | HATA (`SifiraBolmeHatasi`) | HATA (`SifiraBolmeHatasi`) | EŞLEŞTİ |

**Bölümde sıfır bitinin yanlış atılmasını yakalayan örnek:**
- **Örnek:** `1010 ÷ 10` ($10 \div 2 = 5$).
- Adım 1 (`1` $< 10 \to q_1=0$), Adım 2 (`10` $\ge 10 \to q_2=1, r=0$), Adım 3 (gelen `1` $< 10 \to$ **`q_3=0`**, $r=1$), Adım 4 (`10` $\ge 10 \to q_4=1, r=0$).
- **Beklenen:** $Q = \text{`101`}_2 = 5$, $R = \text{`0`}$, Kesirli `= 101`. **Gözlenen:** $Q = \text{`101`}_2 = 5$, $R = \text{`0`}$, Kesirli `= 101` ($5 \times 2 + 0 = 10$).
- **Sıfır biti yanlış atılırsa:** 3. adımda `incelenen < bölen` olduğunda bölüme `0` yazmayı unutan hatalı bir algoritma $Q_{\text{hatalı}} = \text{`11`}_2 = 3$ ve $R = \text{`0`}$ üretir. Sağlama yapıldığında $Q_{\text{hatalı}} \times d + R = 3 \times 2 + 0 = 6 \ne 10$ çıkar ve hata anında yakalanır.

### Kısa Cevap ve Doğrulama Notları (Deney 4)
- **İlk tahminim:** 10110/100 ve 1101/10 kesirde hemen biter ama 111/11 devirli olduğu için 8 basamak sürer.
- **Bağımsız kontrolüm:** Üç işlemde de Q×d + R = D ve 0 <= R < d koşullarını ayrı ayrı doğruladım.
- **Karşı örneğim:** 1010 / 10 işleminde ara sıfır biti atılırsa bölüm 101 (5) yerine 11 (3) çıkar; 3×2 != 10.
- **YZ önerisini değerlendirmem veya kullanmadım beyanım:** YZ'nin önerdiği kesir döngüsünü `111 ÷ 11` işleminde kalanların `10` ve `1` olarak tekrar etmesini ve 8 basamakta `10.01010101` üretmesini elle takip ederek doğruladım.
