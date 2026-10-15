# BLM2007 Mantık Devreleri Laboratuvarı — Ödev 1 Çözüm Raporu
## Deney Yaprağı 2 & Deney Yaprağı 4

**Öğrenci Adı Soyadı:** ............................................................  
**Öğrenci No:** .............................  
**Bölüm:** Bilgisayar Mühendisliği  
**Ders:** BLM2007 Mantık Devreleri (Prof. Dr. Ali Buldu)  
**Tarih:** 12 Ekim 2026  
**Şube / Grup:** ...................... **İmza:** ......................  

---

# BÖLÜM 1: DENEY YAPRAĞI 2 ÇÖZÜMÜ
### Sınırlı Bit Sayısıyla Ölçüm Gösterimi Tasarımı

- **Amaç:** Aralık ve adım büyüklüğüne uygun en küçük ikili gösterimi gerekçelendirmek.
- **Parametreler:**
  - Değer aralığı: $[0, 1000]$ (0 ve 1000 dahil).
  - Adım büyüklüğü (çözünürlük): $0.125$.
  - Gösterim tipi: Sabit noktalı (fixed-point), işaretsiz (unsigned).

---

### Yapılacak İşlemler ve Çözümleri

#### 1. Kesirli kısım için gereken en az bit sayısını basamak ağırlıklarından yararlanarak belirleyin.
İkili sayı sisteminde kesir basamaklarının ağırlıkları $2^{-1}, 2^{-2}, 2^{-3}, \dots$ şeklindedir:
- $2^{-1} = 0.5$
- $2^{-2} = 0.25$
- $2^{-3} = 0.125$

İstenen adım büyüklüğü $0.125 = \frac{1}{8} = 2^{-3}$ değeridir. Kesirli kısım için ayrılan bit sayısı $f$ olduğunda, en küçük çözünürlük adımı $2^{-f}$ olur.
$$2^{-f} \le 0.125 \iff 2^{-f} \le 2^{-3} \implies f \ge 3$$
Dolayısıyla kesirli kısım için **en az 3 bit** ($f = 3$) gereklidir.

#### 2. Tam kısım için gereken en az bit sayısını ve toplam bit sayısını bulun.
Temsil edilmesi gereken en büyük tam değer $1000$'dir. $i$ bitlik işaretsiz bir tam sayı gösterimi ile temsil edilebilecek en büyük sayı $2^i - 1$'dir:
- $i = 9$ için: $2^9 - 1 = 511 < 1000$ (Yetersiz)
- $i = 10$ için: $2^{10} - 1 = 1023 \ge 1000$ (Yeterli)

Dolayısıyla tam kısım için **en az 10 bit** ($i = 10$) gereklidir.  
**Toplam bit sayısı ($N$):**
$$N = i + f = 10 + 3 = 13 \text{ bit}$$

#### 3. Toplam 12 bit yeterli midir? Temsil edilebilen en büyük değer ve farklı gösterimlerin sayısı olmak üzere iki yöntemle inceleyin.

* **Yöntem 1 (Temsil Edilebilen En Büyük Değer Yöntemi):**
  $0.125$ adımlarını sağlayabilmek için kesirli kısma en az 3 bit ayrılması zorunludur ($f = 3$). Eğer toplam bit sayısı 12 olursa, tam kısma en fazla $12 - 3 = 9$ bit kalır ($i \le 9$).
  9 bit ile temsil edilebilecek en büyük tam sayı:
  $$2^9 - 1 = 511$$
  Tüm kesir bitleri de 1 yapıldığında ($2^{-1} + 2^{-2} + 2^{-3} = 0.875$), 12 bitlik sistemde temsil edilebilecek mutlak en büyük değer:
  $$(111111111.111)_2 = 511 + 0.875 = 511.875$$
  $511.875 < 1000$ olduğundan, cihaz $511.875$'ten büyük hiçbir değeri (ve dolayısıyla üst sınır olan 1000'i) gösteremez. **12 bit yetersizdir.**

* **Yöntem 2 (Farklı Gösterimlerin Sayısı / Durum Sayısı Yöntemi):**
  $0$ ile $1000$ aralığında $0.125$ adımlarla temsil edilmesi gereken toplam ayrık durum (seviye) sayısı:
  $$N_{\text{durum}} = \frac{\text{Üst Sınır} - \text{Alt Sınır}}{\text{Adım Büyüklüğü}} + 1 = \frac{1000 - 0}{0.125} + 1 = \frac{1000}{1/8} + 1 = 8000 + 1 = 8001$$
  12 bitlik bir ikili kodlama ile elde edilebilecek maksimum farklı durum sayısı:
  $$2^{12} = 4096$$
  $4096 < 8001$ olduğundan (Güvercin Yuvası İlkesi / Bilgi Teorisi gereği), 12 bit ile 8001 farklı değeri birbirinden ayırt etmek matematiksel olarak imkânsızdır. En az $\lceil \log_2(8001) \rceil = 13$ bit gereklidir. **12 bit kesinlikle yetersizdir.**

#### 4. Yeterli olan en küçük gösterimi tasarlayın. Tam ve kesirli kısımların bit sayılarını belirtin.
- **Biçim Adı:** Q10.3 (İşaretsiz Sabit Noktalı - Unsigned Fixed-Point Q-format)
- **Tam kısım bit sayısı:** 10 bit ($b_9 b_8 b_7 b_6 b_5 b_4 b_3 b_2 b_1 b_0$)
- **Kesirli kısım bit sayısı:** 3 bit ($b_{-1} b_{-2} b_{-3}$)
- **Toplam bit uzunluğu:** 13 bit
- **Ağırlık Fonksiyonu:**
  $$\text{Değer} = \sum_{k=0}^{9} b_k \cdot 2^k + \sum_{j=1}^{3} b_{-j} \cdot 2^{-j}$$

#### 5. 0, 0.125, 173.625 ve 1000 değerlerini aynı sabit bit uzunluğunda yazın. Baştaki ve sondaki gerekli sıfırları koruyun.
Her değer 10 bit tam kısım ve 3 bit kesirli kısım olmak üzere toplam 13 bit formatında (`bbbbbbbbbb.bbb`) ifade edilmiştir:

1. **$0$ Değeri:**
   - Tam kısım: $0 \implies 0000000000_2$
   - Kesirli kısım: $0 \implies 000_2$
   - **Sabit Bit Gösterimi:** `0000000000.000`

2. **$0.125$ Değeri:**
   - Tam kısım: $0 \implies 0000000000_2$
   - Kesirli kısım: $0.125 = 2^{-3} \implies 001_2$
   - **Sabit Bit Gösterimi:** `0000000000.001`

3. **$173.625$ Değeri:**
   - Tam kısım: $173 = 128 + 32 + 8 + 4 + 1 = 2^7 + 2^5 + 2^3 + 2^2 + 2^0 \implies 0010101101_2$
   - Kesirli kısım: $0.625 = 0.5 + 0.125 = 2^{-1} + 2^{-3} \implies 101_2$
   - **Sabit Bit Gösterimi:** `0010101101.101`

4. **$1000$ Değeri:**
   - Tam kısım: $1000 = 512 + 256 + 128 + 64 + 32 + 8 = 2^9 + 2^8 + 2^7 + 2^6 + 2^5 + 2^3 \implies 1111101000_2$
   - Kesirli kısım: $0 \implies 000_2$
   - **Sabit Bit Gösterimi:** `1111101000.000`

#### 6. 173.625 değerini sekizli ve onaltılı sistemlerde yazın. Üç gösterimin aynı değeri verdiğini doğrulayın.

* **İkili Gösterim:** `0010101101.101`

* **Sekizli (Octal - Taban 8) Dönüşümü:**
  İkili noktadan itibaren 3'erli gruplama yapılır (tam kısmın soluna sıfır eklenir):
  - Tam kısım: $\underbrace{000}_{0} \quad \underbrace{010}_{2} \quad \underbrace{101}_{5} \quad \underbrace{101}_{5} \implies (255)_8$
  - Kesirli kısım: $\underbrace{101}_{5} \implies (.5)_8$
  - **Sekizli Gösterim:** $(255.5)_8$

* **Onaltılı (Hexadecimal - Taban 16) Dönüşümü:**
  İkili noktadan itibaren 4'erli gruplama yapılır (tam kısmın soluna ve kesirli kısmın sağına sıfır eklenir):
  - Tam kısım: $\underbrace{0000}_{0} \quad \underbrace{1010}_{A} \quad \underbrace{1101}_{D} \implies (AD)_{16}$
  - Kesirli kısım: $\underbrace{1010}_{A} \implies (.A)_{16}$
  - **Onaltılı Gösterim:** $(AD.A)_{16}$

* **Doğrulama (Onluk Sisteme Çevrim):**
  - **İkili:**
    $$1\cdot 2^7 + 1\cdot 2^5 + 1\cdot 2^3 + 1\cdot 2^2 + 1\cdot 2^0 + 1\cdot 2^{-1} + 1\cdot 2^{-3} = 128 + 32 + 8 + 4 + 1 + 0.5 + 0.125 = 173.625_{10}$$
  - **Sekizli:**
    $$2\cdot 8^2 + 5\cdot 8^1 + 5\cdot 8^0 + 5\cdot 8^{-1} = 128 + 40 + 5 + 0.625 = 173.625_{10}$$
  - **Onaltılı:**
    $$10\cdot 16^1 + 13\cdot 16^0 + 10\cdot 16^{-1} = 160 + 13 + \frac{10}{16} = 173 + 0.625 = 173.625_{10}$$

  **Sonuç:** $(0010101101.101)_2 = (255.5)_8 = (AD.A)_{16} = (173.625)_{10}$ olduğu kanıtlanmıştır.

---

### Düşünme Sorusu (Deney 2)
> **Soru:** Adım büyüklüğü 0.1 olsaydı, bütün değerleri sonlu sayıda ikili kesir basamağıyla tam olarak gösterebilir miydiniz? Yanıtınızı basamak ağırlıklarıyla gerekçelendirin.

**Yanıt:** **Hayır, gösterilemezdi.**

**Gerekçe:**  
Bir onluk rasyonel kesrin ikili sayı sisteminde sonlu sayıda basamakla ifade edilebilmesi için, sayının en sade rasyonel biçimindeki ($p/q$, $\text{EBOB}(p,q)=1$) paydasının ($q$) asal çarpanlarının yalnızca 2'nin kuvveti ($q = 2^k$) olması gerekir.
$0.1$ kesri rasyonel olarak:
$$0.1 = \frac{1}{10} = \frac{1}{2 \times 5}$$
Paydada $5$ asal çarpanı bulunmaktadır. 2'nin hiçbir pozitif tam kuvveti ($2^k$) 5'e tam bölünemez. Sayı ikili sisteme dönüştürüldüğünde basamak ağırlıkları açılımı:
$$0.1 \times 2 = 0.2 \to 0$$
$$0.2 \times 2 = 0.4 \to 0$$
$$0.4 \times 2 = 0.8 \to 0$$
$$0.8 \times 2 = 1.6 \to 1$$
$$0.6 \times 2 = 1.2 \to 1$$
$$0.2 \times 2 = 0.4 \to 0 \quad (\text{Tekrar başa döndü!})$$

$$(0.1)_{10} = (0.0001100110011\dots)_2 = (0.0\overline{0011})_2$$
Sonuç **sonsuz devirli** bir ikili kesirdir. Bu nedenle, kaç bit kullanılırsa kullanılsın sonlu sayıda ikili basamakla tam olarak temsil edilemez; mutlaka kesme/yuvarlama (kuantalama) hatası oluşur.

---

### Kısa Cevap ve Doğrulama Notları (Deney 2)
- **İlk tahminim:** $1000$ değeri için 10 bit ($2^{10}=1024$), $0.125 = 1/8 = 2^{-3}$ adımı için 3 bit olmak üzere toplam en az 13 bit gerekecektir.
- **Bağımsız kontrolüm:** Durum sayısı formülü ile kontrol: $\frac{1000-0}{0.125} + 1 = 8001$ ayrık değer. $2^{12} = 4096 < 8001 \le 8192 = 2^{13}$. Shannon bilgi teorisi gereğince 8001 durum en az 13 bit gerektirir.
- **Karşı örneğim:** 12 bit seçilip tam kısma 9 bit verilirse maksimum değer $(111111111.111)_2 = 511.875$ olur ve 1000 temsil edilemez; tam kısma 10 bit verilirse kesre 2 bit kalır ($2^{-2}=0.25$), bu durumda $0.125$ adımı atlanarak temsil edilemez.
- **YZ önerisini değerlendirmem veya kullanmadım beyanım:** YZ desteğiyle hazırlanan Q10.3 sabit noktalı bit formatı, bağımsız el hesaplamaları ve Python doğrulama kodu (`dogrulama_2.py`) çalıştırılarak sınır değerler ($0, 1000$) ve adım çözünürlüğü açısından doğrulanmıştır.

---
---

# BÖLÜM 2: DENEY YAPRAĞI 4 ÇÖZÜMÜ
### Kesirli Dönüşümde Kesinlik ve Yaklaşım Hatası

- **Amaç:** Sonlu gösterim, kesme ve yuvarlama arasındaki farkı sayısal olarak incelemek.
- **Parametreler:**
  - İncelenecek sayılar: `0.625`, `0.1`, `0.65`, `0.975`
  - Kesirli kısım bit sınırı: Sekiz (8) ikili basamak.

---

### Yapılacak İşlemler ve Çözümleri

#### 1. Her sayıyı ikili sisteme dönüştürün. İşlem tamamlanmazsa ilk sekiz kesir basamağında durun. Tamamlanan gösterimleri gerekirse sağdan sıfırlarla tamamlayın.

* **Sayı 1: $0.625$**
  - $0.625 \times 2 = 1.25 \implies 1$ (kalan: $0.25$)
  - $0.250 \times 2 = 0.50 \implies 0$ (kalan: $0.50$)
  - $0.500 \times 2 = 1.00 \implies 1$ (kalan: $0.00 \to$ Tamamlandı!)
  - 3 basamakta tam bitti: $(0.101)_2$.
  - 8 basamağa sıfırlarla tamamlama: **`0.10100000`** (Kesin dönüşüm)

* **Sayı 2: $0.1$**
  - $0.1 \times 2 = 0.2 \implies b_1 = 0$
  - $0.2 \times 2 = 0.4 \implies b_2 = 0$
  - $0.4 \times 2 = 0.8 \implies b_3 = 0$
  - $0.8 \times 2 = 1.6 \implies b_4 = 1$
  - $0.6 \times 2 = 1.2 \implies b_5 = 1$
  - $0.2 \times 2 = 0.4 \implies b_6 = 0$
  - $0.4 \times 2 = 0.8 \implies b_7 = 0$
  - $0.8 \times 2 = 1.6 \implies b_8 = 1$
  - *(Yuvarlama kontrolü için 9. bit: $0.6 \times 2 = 1.2 \implies b_9 = 1$)*
  - İlk 8 basamak (Kesilmiş): **`0.00011001`** (Yaklaşık)

* **Sayı 3: $0.65$**
  - $0.65 \times 2 = 1.30 \implies b_1 = 1$
  - $0.30 \times 2 = 0.60 \implies b_2 = 0$
  - $0.60 \times 2 = 1.20 \implies b_3 = 1$
  - $0.20 \times 2 = 0.40 \implies b_4 = 0$
  - $0.40 \times 2 = 0.80 \implies b_5 = 0$
  - $0.80 \times 2 = 1.60 \implies b_6 = 1$
  - $0.60 \times 2 = 1.20 \implies b_7 = 1$
  - $0.20 \times 2 = 0.40 \implies b_8 = 0$
  - *(Yuvarlama kontrolü için 9. bit: $0.40 \times 2 = 0.80 \implies b_9 = 0$)*
  - İlk 8 basamak (Kesilmiş): **`0.10100110`** (Yaklaşık)

* **Sayı 4: $0.975$**
  - $0.975 \times 2 = 1.95 \implies b_1 = 1$
  - $0.950 \times 2 = 1.90 \implies b_2 = 1$
  - $0.900 \times 2 = 1.80 \implies b_3 = 1$
  - $0.800 \times 2 = 1.60 \implies b_4 = 1$
  - $0.600 \times 2 = 1.20 \implies b_5 = 1$
  - $0.200 \times 2 = 0.40 \implies b_6 = 0$
  - $0.400 \times 2 = 0.80 \implies b_7 = 0$
  - $0.800 \times 2 = 1.60 \implies b_8 = 1$
  - *(Yuvarlama kontrolü için 9. bit: $0.60 \times 2 = 1.20 \implies b_9 = 1$)*
  - İlk 8 basamak (Kesilmiş): **`0.11111001`** (Yaklaşık)

---

#### 2. Kesilmiş her gösterimi tekrar onluya çevirin ve mutlak hatayı hesaplayın.
Mutlak Hata Formülü: $\text{Hata}_{\text{kesme}} = |\text{Gerçek Değer} - \text{Kesilmiş Onluk Değer}|$

1. **$0.625$ için:**
   $$\text{Değer} = 2^{-1} + 2^{-3} = \frac{1}{2} + \frac{1}{8} = 0.5 + 0.125 = 0.625$$
   $$\text{Mutlak Hata} = |0.625 - 0.625| = 0.00000000$$

2. **$0.1$ için:**
   $$\text{Değer} = 2^{-4} + 2^{-5} + 2^{-8} = \frac{1}{16} + \frac{1}{32} + \frac{1}{256} = \frac{16 + 8 + 1}{256} = \frac{25}{256} = 0.09765625$$
   $$\text{Mutlak Hata} = |0.1 - 0.09765625| = 0.00234375$$

3. **$0.65$ için:**
   $$\text{Değer} = 2^{-1} + 2^{-3} + 2^{-6} + 2^{-7} = \frac{1}{2} + \frac{1}{8} + \frac{1}{64} + \frac{1}{128} = \frac{64 + 16 + 2 + 1}{128} = \frac{83}{128} = \frac{166}{256} = 0.6484375$$
   $$\text{Mutlak Hata} = |0.65 - 0.6484375| = 0.00156250$$

4. **$0.975$ için:**
   $$\text{Değer} = 2^{-1} + 2^{-2} + 2^{-3} + 2^{-4} + 2^{-5} + 2^{-8} = \frac{128 + 64 + 32 + 16 + 8 + 1}{256} = \frac{249}{256} = 0.97265625$$
   $$\text{Mutlak Hata} = |0.975 - 0.97265625| = 0.00234375$$

---

#### 3. Her sayıyı en yakın sekiz basamaklı ikili değere yuvarlayın. Eşit uzaklıkta büyük olanı seçin. Yuvarlanmış değerin mutlak hatasını da bulun.
*Kural:* 8 basamaktan sonraki kalan değer $2^{-9} = \frac{1}{512}$ (yarım LSB) değerinden büyük veya eşitse ($b_9 = 1$), 8. basamağa $1$ eklenir (yukarı yuvarlama). Küçükse ($b_9 = 0$), kesilmiş değer aynen korunur.

1. **$0.625$:**
   - Kalan: $0 \implies$ Yuvarlanmış değer: **`0.10100000`**
   - Onluk değer: $0.625$
   - $\text{Mutlak Hata} = |0.625 - 0.625| = 0.00000000$

2. **$0.1$:**
   - $b_9 = 1$ (Kalan $\approx 0.00234 > 2^{-9} = 0.001953$). Yukarı yuvarlanır:
     $$0.00011001_2 + 0.00000001_2 = 0.00011010_2$$
   - Yuvarlanmış ikili: **`0.00011010`**
   - Onluk değer: $\frac{25 + 1}{256} = \frac{26}{256} = \frac{13}{128} = 0.1015625$
   - $\text{Mutlak Hata} = |0.1 - 0.1015625| = 0.00156250$ *(Kesme hatasından daha küçüktür!)*

3. **$0.65$:**
   - $b_9 = 0$ (Kalan $= 0.0015625 < 2^{-9} = 0.001953125$). Aşağıda kalır:
   - Yuvarlanmış ikili: **`0.10100110`**
   - Onluk değer: $\frac{83}{128} = 0.6484375$
   - $\text{Mutlak Hata} = |0.65 - 0.6484375| = 0.00156250$

4. **$0.975$:**
   - $b_9 = 1$ (Kalan $= 0.00234375 > 2^{-9} = 0.001953125$). Yukarı yuvarlanır:
     $$0.11111001_2 + 0.00000001_2 = 0.11111010_2$$
   - Yuvarlanmış ikili: **`0.11111010`**
   - Onluk değer: $\frac{249 + 1}{256} = \frac{250}{256} = \frac{125}{128} = 0.9765625$
   - $\text{Mutlak Hata} = |0.975 - 0.9765625| = 0.00156250$ *(Kesme hatasından daha küçüktür!)*

---

#### 4. Kesme ve yuvarlama sonuçlarını bir tabloda karşılaştırın. Hangi dönüşümlerde =, hangilerinde ≈ kullanılması gerektiğini belirtin.

| Onluk Sayı | 8-Bit Kesilmiş İkili | Kesilmiş Onluk Değer | Kesme Mutlak Hatası | 8-Bit Yuvarlanmış İkili | Yuvarlanmış Onluk Değer | Yuvarlama Mutlak Hatası | Sonuç İfadesi |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **0.625** | `0.10100000` | $0.62500000$ | $0.00000000$ | `0.10100000` | $0.62500000$ | $0.00000000$ | $(0.625)_{10} = (0.101)_2$ |
| **0.1** | `0.00011001` | $0.09765625$ | $0.00234375$ | `0.00011010` | $0.10156250$ | $0.00156250$ | $(0.1)_{10} \approx (0.00011010)_2$ |
| **0.65** | `0.10100110` | $0.64843750$ | $0.00156250$ | `0.10100110` | $0.64843750$ | $0.00156250$ | $(0.65)_{10} \approx (0.10100110)_2$ |
| **0.975** | `0.11111001` | $0.97265625$ | $0.00234375$ | `0.11111010` | $0.97656250$ | $0.00156250$ | $(0.975)_{10} \approx (0.11111010)_2$ |

- **$=$ (Eşittir) Kullanımı:** Yalnızca `0.625` için kullanılır, çünkü ikili karşılığı 3. basamakta tam olarak sonlanmış ve mutlak hata $0$'dır.
- **$\approx$ (Yaklaşık) Kullanımı:** `0.1`, `0.65` ve `0.975` sayıları için kullanılır; çünkü bu sayılar ikili sistemde devirlidir ve 8 bitlik gösterimleri mutlak bir yaklaşım hatası ($\ne 0$) barındırır.

---

#### 5. Sonlu bir ikili kesrin neden bir tam sayının 2'nin bir kuvvetine bölümü olarak yazılabildiğini gösterin. Bu bilgiyle hangi sayıların sonlu ikili gösterime sahip olduğunu açıklayın.

* **İspat:**
  $k$ basamaklı sonlu bir ikili kesir ele alalım: $(0.b_1 b_2 b_3 \dots b_k)_2$, burada $b_j \in \{0, 1\}$.  
  Basamak ağırlıkları tanımından:
  $$(0.b_1 b_2 \dots b_k)_2 = b_1 \cdot 2^{-1} + b_2 \cdot 2^{-2} + \dots + b_k \cdot 2^{-k} = \sum_{j=1}^{k} b_j \cdot 2^{-j}$$
  Ortak payda $2^k$ parantezine alınırsa:
  $$\sum_{j=1}^{k} b_j \cdot 2^{-j} = \frac{b_1 \cdot 2^{k-1} + b_2 \cdot 2^{k-2} + \dots + b_k \cdot 2^0}{2^k}$$
  Paydaki ifadeye $M$ diyelim:
  $$M = b_1 \cdot 2^{k-1} + b_2 \cdot 2^{k-2} + \dots + b_k \cdot 2^0$$
  $b_j \in \{0, 1\}$ ve $2^{k-j}$ tam sayı olduğundan, $M$ ifadesi açıkça bir **tam sayıdır** ($M \in \mathbb{Z}_{\ge 0}$).  
  Böylece:
  $$(0.b_1 b_2 \dots b_k)_2 = \frac{M}{2^k}$$
  şeklinde bir tam sayının 2'nin bir kuvvetine bölümü olarak ispatlanmış olur.

* **Hangi Sayılar Sonlu İkili Gösterime Sahiptir?**
  Bir onluk rasyonel sayının en sade (indirgenmiş) kesir biçimi $\frac{p}{q}$ olsun ($p, q \in \mathbb{Z}^+$, $\text{EBOB}(p,q) = 1$).  
  Bu sayının sonlu bir ikili kesir olabilmesi için $\frac{p}{q} = \frac{M}{2^k}$ eşitliğini sağlaması, yani **paydası $q$'nun yalnızca 2 asal çarpanından oluşması ($q = 2^m, m \in \mathbb{N}$)** şarttır.
  - Eğer $q$'nun asal çarpanları arasında 2 dışında başka bir asal sayı (örneğin $3, 5, 7, \dots$) bulunursa, sayı ikili sistemde sonlu basamakla temsil edilemez; sonsuz devirli olur.
  - İncelenen sayılardan:
    - $0.625 = \frac{5}{8} = \frac{5}{2^3} \implies$ Paydada sadece 2 çarpanı var $\implies$ **Sonludur.**
    - $0.1 = \frac{1}{10} = \frac{1}{2 \times 5} \implies$ Paydada 5 çarpanı var $\implies$ **Devirlidir (Sonsuz).**
    - $0.65 = \frac{13}{20} = \frac{13}{2^2 \times 5} \implies$ Paydada 5 çarpanı var $\implies$ **Devirlidir (Sonsuz).**
    - $0.975 = \frac{39}{40} = \frac{39}{2^3 \times 5} \implies$ Paydada 5 çarpanı var $\implies$ **Devirlidir (Sonsuz).**

---

### Düşünme Sorusu (Deney 4)
> **Soru:** Sekiz ikili kesir basamağı ile sekiz onaltılı kesir basamağı aynı hassasiyeti sağlar mı? Son basamağın ağırlığını kullanarak karşılaştırın.

**Yanıt:** **Hayır, kesinlikle aynı hassasiyeti sağlamaz. Sekiz onaltılı kesir basamağı kıyaslanamayacak kadar çok daha yüksek bir hassasiyet sağlar.**

**Gerekçe:**  
Hassasiyet (çözünürlük), son kesir basamağının ağırlığı (LSB - Least Significant Bit/Digit) ile belirlenir:
- **Sekiz İkili Kesir Basamağında Son Basamak Ağırlığı:**
  $$\text{LSB}_{\text{ikili}} = 2^{-8} = \frac{1}{256} \approx 0.00390625 \quad (3.9 \times 10^{-3})$$
- **Sekiz Onaltılı Kesir Basamağında Son Basamak Ağırlığı:**
  $$\text{LSD}_{\text{onaltılı}} = 16^{-8} = (2^4)^{-8} = 2^{-32} = \frac{1}{4\,294\,967\,296} \approx 2.3283 \times 10^{-10}$$

Her 1 onaltılı basamak 4 ikili bite karşılık geldiğinden, 8 onaltılı kesir basamağı **32 ikili bite** eşdeğerdir. İki sistem arasındaki hassasiyet oranı:
$$\frac{2^{-8}}{2^{-32}} = 2^{24} = 16\,777\,216$$
Sekiz onaltılı basamak, sekiz ikili basamağa göre **yaklaşık 16.78 milyon kat daha yüksek hassasiyet** sunar.

---

### Kısa Cevap ve Doğrulama Notları (Deney 4)
- **İlk tahminim:** Verilen sayılardan yalnızca $0.625 = 5/8$ sonlu ikili basamakla ifade edilecek, diğer üç sayı 5 asal çarpanı nedeniyle sonsuz devirli çıkacaktır. Yuvarlama hatası kesme hatasına göre daha küçük veya eşit olacaktır.
- **Bağımsız kontrolüm:** Python Fractions modülü ve el ile yapılan kesir hesaplarında $\frac{25}{256}$, $\frac{83}{128}$ ve $\frac{249}{256}$ değerleri onluya çevrilerek mutlak hatalar tam olarak hesaplanmış, 8-bitlik kesme hatasının maksimum üst sınırı olan $2^{-8} = 0.00390625$'in altında kaldığı doğrulanmıştır.
- **Karşı örneğim:** "Onluk sistemde sonlu basamaklı olan her kesir ikili sistemde de sonludur" önermesinin yanlışlığı $0.1$ karşı örneği ile çürütülmüştür; onlukta 1 basamakta sonlu iken ikilide sonsuz devirlidir.
- **YZ önerisini değerlendirmem veya kullanmadım beyanım:** YZ desteği ile hazırlanan yuvarlama tablosu ve 9. bit ($b_9$) karar mekanizması, `dogrulama_4.py` scripti ile bağımsız olarak çalıştırılıp tek tek kontrol edilmiş ve matematiksel olarak onaylanmıştır.

---

# EK DOSYA: BAĞIMSIZ HESAPLAMA VE DOĞRULAMA KODU (Python)

Deney 2 için `dogrulama_2.py`, Deney 4 için `dogrulama_4.py` dosyalarını kullandım. Kodlar ayrı dosyalardadır.
