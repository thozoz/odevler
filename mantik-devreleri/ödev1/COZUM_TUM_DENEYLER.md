# BLM2007 Mantik Devreleri Laboratuvari - Odev 1 Toplu Cozum Raporu

**Ogrenci Adi Soyadi:** Efe Özan  **Ogrenci No:** 170425062  **Bolum:** Bilgisayar Muhendisligi
**Ders:** BLM2007 Mantik Devreleri (Prof. Dr. Ali Buldu)  **Tarih:** 12 Ekim 2026
**Sube / Grup:** .... **Imza:** ....

> Bu dosya tek kaynak: yapilanlar buraya toplandi, yeni deneyler buraya eklenecek.
> Kodlar: sayi_donusturucu.py (Deney 1), dogrulama_2.py (Deney 2), dogrulama_3.py (Deney 3), dogrulama_4.py (Deney 4), dogrulama_5.py (Deney 5), dogrulama_6.py (Deney 6), dogrulama_7.py (Deney 7).
> Ayrinti mdler (cozum_deney_1.md, cozum_deney_2_ve_4.md, cozum_deney_3.md) arsiv sayilir.

---

# DENEY YAPRAĞI 1 ÇÖZÜMÜ
### Hatalı Girdileri Tanıyan Sayı Sistemi Dönüştürücüsü

- **Amaç:** Tam ve kesirli sayı dönüşümlerini tasarlamak ve bağımsız testlerle doğrulamak.
- **Tanım:** Yazılım sayı metni + kaynak taban + hedef taban alır. Tabanlar {2, 8, 10, 16}; sayılar negatif olmayan değerler; kesir ayracı `.` noktadır.
- **Kod dosyası:** `sayi_donusturucu.py` (bu raporun ekidir; çalıştırınca 12 testi kendisi basar).

---

### 1. Tam ve kesirli kısım algoritmaları (basamak ağırlıklarıyla gerekçe)

Dönüşüm iki aşamalıdır: kaynak taban → onluk ara değer (rasyonel) → hedef taban. Dönüşüm hesaplarında `float` kullanılmaz; kesir `pay/payda` tam sayısıyla taşınır, hassasiyet kaybı olmaz. Test çıktısındaki bilgilendirici onluk gösterim için ayrıca `float` kullanılır; bu yaklaşık gösterim dönüşüm sonucunu etkilemez.

**a) Tam kısım: kaynak taban → onluk (Horner / ağırlık toplamı)**

$$I_{10} = \sum_{i=0}^{n-1} d_i \cdot r^i$$

Kod (`tam_kisim_onluya_cevir`) bunu Horner biçiminde soldan sağa kurar:

```
toplam = 0
her karakter ch için:
    toplam = toplam * kaynak_taban + değer(ch)
```

Bu, en anlamlı basamağın en büyük ağırlığı alması demektir. Örnek `101101_2`: `(((1·2+0)·2+1)·2+1)·2+0)·2+1 = 45`.

**b) Tam kısım: onluk → hedef taban (ardışık bölme, kalanlar ters sırada)**

```
kalanlar = []
sayı > 0 iken:
    kalan = sayı % hedef_taban   # en küçük ağırlıklı basamak önce bulunur
    kalanlar.append(karakter(kalan))
    sayı = sayı // hedef_taban
sonucu ters çevir, birleştir
```

Kalanların ters sırada yazılma nedeni: ilk bölmenin kalanı $r^0$ (birler) basamağıdır, yani en küçük ağırlıktır. Basamak dizisi MSB→LSB yazıldığı için üretim sırası (LSB→MSB) ters çevrilmek zorundadır. Örnek: $45_{10} \to 16$: $45 \div 16 = 2$ kalan $13$ (D) önce bulunur (birler), sonra $2 \div 16 = 0$ kalan $2$ (onaltılar). Sıra `D,2` üretilir, tersi `2D` yazılır.

**c) Kesirli kısım: kaynak taban → rasyonel (ağırlık toplamı)**

$$F = \sum_{j=1}^{m} c_j \cdot r^{-j} = \frac{\text{pay}}{\text{payda}}$$

Kod (`kesir_onlu_rasyonel`): payı Horner ile kurar, paydayı $r^m$ yapar. Örnek taban 2'de `01101`: pay $= 0·16+1·8+1·4+0·2+1 = 13$, payda $= 2^5 = 32$, değer $= 13/32$.

**d) Kesirli kısım: rasyonel → hedef taban (ardışık çarpma, işlem sırasıyla)**

```
her adımda:
    basamak = (pay * hedef_taban) // payda   # en büyük ağırlıklı kesir basamağı önce
    pay     = (pay * hedef_taban) % payda
```

Kesir basamaklarının işlem sırasıyla yazılma nedeni: ilk çarpma $r^{-1}$ (en büyük kesir ağırlığı) basamağını verir, yani hedef yazım sırası (MSB→LSB) ile üretim sırası aynıdır; ters çevirme yoktur. Örnek $13/32 \to 16$: $(13·16)//32 = 6$ (ilki $16^{-1}$), kalan $16$; $(16·16)//32 = 8$ (ikincisi $16^{-2}$) → `68`.

---

### 2. Girdi kontrolü (reddetme kuralları)

`girdi_dogrula` fonksiyonu, dönüşümden önce şu sırayla denetler:

1. Taban geçerliliği: kaynak ve hedef $\{2,8,10,16\}$ içinde olmalı (örn. taban `5` reddedilir).
2. Boş girdi: `strip()` sonrası uzunluk 0 ise reddet (`"   "` → hata).
3. Negatif engeli: `-` ile başlıyorsa reddet.
4. Kesir ayracı: `.` sayısı $>1$ ise reddet (`10.11.01` → hata); gövdede hiç rakam yoksa (yalnız `.`) reddet.
5. Rakam geçerliliği: her karakter `CHAR_TO_VAL` tablosunda olmalı ve değeri kaynak tabandan küçük olmalı. Taban 2'de `102` (`2` geçersiz), taban 8'de `128` (`8` geçersiz) bu kurala takılır.

Boş kalan taraf toleransı: `.101` → `0.101`, `5.` → `5` sayılır (negatif olmayan sayı varsayımı); ikisi birden boşsa hata.

Hazır taban fonksiyonu kullanılmaz: `int(s, base)`, `bin`, `oct`, `hex` ana dönüşümde yoktur. Yalnızca elle kurulan `CHAR_TO_VAL` / `VAL_TO_CHAR` tabloları + `//`, `%`, `*` işlemleri vardır (`int()` yalnızca sayısal `Fraction` kesmesinde kullanılır, taban çözümlemez).

---

### 3. Kesinlik bilgisi (8 basamak sınırı, = vs ≈)

`kesir_hedefe_cevir_rasyonel(pay, payda, hedef, max_basamak=8)`:

- Kalan `pay == 0` olursa 8 basamaktan önce biter → `kesin = True`, sonuç `=` ile işaretlenir (`KESİN`).
- 8 basamak üretilip kalan sıfırlanmazsa → `kesin = False`, sonuç `≈` ile işaretlenir (`YAKLAŞIK - 8 basamakta kesildi`).
- Kesirsiz tam sayılar her zaman `=` + `KESİN (Tam Sayı)`.

Örnek: `101101.01101_2 → 2D.68_16` kalan sıfırlandığı için `=`; `0.1_10 → 0.00011001_2` 8 basamakta bitmediği için `≈`.

---

### 4. Kod

Tam kod `sayi_donusturucu.py` dosyasındadır. Ana giriş:

```python
sayi_donustur("101101.01101", 2, 16)
# -> {"sonuc": "2D.68", "isaret": "=", "kesin_mi": True, ...}
```

Çalıştırma: `python sayi_donusturucu.py` → 12 testi koşar, beklenen/gerçekleşen tablosunu basar. Çıktı Bölüm 5'teki tabloyla birebir aynıdır (12/12 BAŞARILI).

---

### 5. Test tablosu (beklenen önceden el ile hesaplandı, 8 zorunlu senaryo + ekler)

| # | Senaryo | Girdi | Kaynak→Hedef | Beklenen | Gerçekleşen | Durum |
|---|---------|-------|--------------|----------|-------------|-------|
| 01 | Örnek giriş (kesin kesirli) | `101101.01101` | 2→16 | `2D.68` (=) | `2D.68` (=) | BAŞARILI |
| 02 | Sıfır (zorunlu) | `0` | 10→2 | `0` (=) | `0` (=) | BAŞARILI |
| 03 | Yalnızca kesirli (zorunlu, `.` ile başlayan) | `.101` | 2→10 | `0.625` (=) | `0.625` (=) | BAŞARILI |
| 04 | Başında sıfır (zorunlu) | `001011.10` | 2→10 | `11.5` (=) | `11.5` (=) | BAŞARILI |
| 05 | 8 basamakta bitmeyen (yaklaşık) | `0.1` | 10→2 | `0.00011001` (≈) | `0.00011001` (≈) | BAŞARILI |
| 06 | Hex→Octal | `2D.68` | 16→8 | `55.32` (=) | `55.32` (=) | BAŞARILI |
| 07 | Hatalı: `102` taban 2 (zorunlu örnek) | `102` | 2→10 | HATA | Geçersiz karakter yakalandı | BAŞARILI |
| 08 | Hatalı: `128` taban 8 (zorunlu örnek) | `128` | 8→2 | HATA | Geçersiz karakter yakalandı | BAŞARILI |
| 09 | Hatalı: boş girdi (zorunlu) | `   ` | 10→2 | HATA | Boş girdi yakalandı | BAŞARILI |
| 10 | Hatalı: çoklu ayraç (zorunlu) | `10.11.01` | 2→16 | HATA | Çoklu ayraç yakalandı | BAŞARILI |
| 11 | Hatalı: negatif | `-101.1` | 2→10 | HATA | Negatif reddi yakalandı | BAŞARILI |
| 12 | Hatalı: geçersiz taban | `101` | 5→2 | HATA | Geçersiz taban yakalandı | BAŞARILI |

Zorunlu kapsama: sıfır (02), yalnızca kesirli (03), başında sıfır (04), hatalı girdiler (07–10) tamamdır. Toplam 12/12 BAŞARILI.

**Bağımsız kontrol (en az bir sonuç, basamak ağırlıklarıyla):** Test 01/06'nın ortak değeri $45.40625$:

- İkili: $1·2^5+1·2^3+1·2^2+1·2^0 = 45$; kesir $1·2^{-2}+1·2^{-3}+1·2^{-5} = 1/4+1/8+1/32 = 13/32 = 0.40625$.
- Hex `2D.68`: $2·16+13 = 45$; $6/16+8/256 = 104/256 = 13/32 = 0.40625$.
- Oct `55.32`: $5·8+5 = 45$; $3/8+2/64 = 26/64 = 13/32 = 0.40625$.

Üçü de $45.40625$ verir; kod çıktısıyla aynıdır.

---

### Düşünme Sorusu
> **Soru:** Başka tabana dönüşümden sonra başlangıç tabanına dönünce aynı değeri bulmak doğruluğu kanıtlar mı? İki yönde aynı hatayı yapan bir program üzerinden tartışın.

**Yanıt:** **Hayır, kanıtlamaz. Gidiş-dönüş (round-trip) tutarlılık gösterir, doğruluk göstermez.**

Gerekçe: iki yönde birbirini götüren sistematik bir hata, yanlış değeri kararlı hale getirebilir. Örnek olarak programın onaltılı `C` ve `D` sembollerini iki tabloda da birbiriyle karıştırdığını varsayalım. Hatalı `VAL_TO_CHAR` tablosu 13 değeri için `D` yerine `C` yazar; hatalı `CHAR_TO_VAL` tablosu da `C` okuduğunda 12 yerine 13 kabul eder. Diğer basamaklar normal işlenir.

- Gidiş: `101101.01101_2` (gerçek $45.40625$) → hatalı çıkış tablosuyla `2C.68_16` üretir. Standart onaltılı gösterim kurallarında `2C.68` aslında $44.40625$ eder.
- Dönüş: aynı program `2C.68_16` metnini okurken `C`'yi hatalı olarak 13 kabul eder; böylece ara değeri yine $45.40625$ bulur ve `101101.01101_2` üretir.
- Kullanıcı `101101.01101 → 2C.68 → 101101.01101` görünce dönüşümün doğru olduğunu sanır; oysa ortadaki metin standart onaltılı kurallara göre yanlış değerdedir. İki yönlü test, aynı tablo hatasını yakalayamamıştır.

Aynı durum çift yönlü kesme için de geçerlidir: gidişte $0.1 \to 0.00011001$ (kesilmiş), dönüşte aynı 8-bit değeri geri okuyup $0.09765625 \approx 0.1$ diye yuvarlarsa tutarlı görünür ama ilk adımda bilgi kaybolmuştur. Bu yüzden doğruluk için gidiş-dönüş değil, **basamak ağırlıklarıyla bağımsız ara-değer hesabı** (yukarıdaki gibi $13/32$ kontrolü) gerekir.

---

### Kısa Cevap ve Doğrulama Notları (Deney 1)
- **İlk tahminim:** Örnek giriş `101101.01101_2 = 45.40625 = 2D.68_16` kesin çıkacak; `0.1_10 → 2` yaklaşık (`0.00011001`) olacak; `102`/`128`/boş/çoklu-nokta reddedilecek.
- **Bağımsız kontrolüm:** Test 01/06 ağırlık hesabıyla el ile doğrulandı (tam $45$, kesir $13/32$); `python sayi_donusturucu.py` 12/12 BAŞARILI verdi, beklenenlerle birebir eşleşti.
- **Karşı örneğim:** `C` ve `D` sembollerini hem yazarken hem okurken ters eşleyen program, gidiş-dönüşte aynı ikili değeri döndürür; ara onaltılı gösterim yanlış olduğu halde round-trip testi geçer.
- **YZ önerisini değerlendirmem veya kullanmadım beyanım:** YZ desteğiyle üretilen tablo ve açıklamalar, `sayi_donusturucu.py` çalıştırılıp ağırlık hesaplarıyla karşılaştırılarak doğrulandı; hazır `int(s,base)/bin/oct/hex` kullanılmadığı kod taramasıyla denetlendi.

---

# DENEY YAPRAĞI 2 ÇÖZÜMÜ
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


---

# DENEY YAPRAĞI 3 ÇÖZÜMÜ
### Sıfır Ekleme ve Basamak Değerinin Korunması

- **Amaç:** Gruplandırma sırasında eklenen sıfırların sayısal etkisini açıklamak.
- **İncelenecek sayı:** $(101101.01101)_2$

---

### 1. Üçlü ve dörtlü grupları ikili noktadan başlayarak oluşturun. Eklediğiniz sıfırları açıkça işaretleyin.

Kural: gruplama **ikili noktadan** başlar. Tam kısım sağdan sola, kesirli kısım soldan sağa gruplanır. Köşeli parantez `[0]` eklenen sıfırı gösterir.

**a) Sekizli sistem için (3'erli gruplama):**

Tam kısım `101101` (6 bit, 3'e tam bölünür, ek sıfır gerekmez):

```
101 101
 5   5
```

Kesirli kısım `01101` (5 bit, 3'e tamamlamak için sağa 1 sıfır gerekir):

```
011 01[0]
 3   2
```

- **Sekizli sonuç:** $(55.32)_8$

**b) Onaltılı sistem için (4'erli gruplama):**

Tam kısım `101101` (6 bit, 4'e tamamlamak için sola 2 sıfır gerekir):

```
[0][0]10 1101
   2    D
```

Kesirli kısım `01101` (5 bit, 4'e tamamlamak için sağa 3 sıfır gerekir):

```
0110 1[0][0][0]
  6     8
```

- **Onaltılı sonuç:** $(2D.68)_{16}$

Özet: sola eklenen `[0]` yalnızca tam kısımda, sağa eklenen `[0]` yalnızca kesirli kısımda geçerlidir.

---

### 2. Tam kısmın soluna ve kesirli kısmın sağına eklenen sıfırların neden değeri değiştirmediğini basamak ağırlıklarıyla açıklayın.

Basamak ağırlığı tanımı:

$$\text{Değer} = \sum_i b_i \cdot 2^i$$

- **Tam kısım, sola sıfır ekleme:** Mevcut en büyük basamak $2^n$ olsun. Sola eklenen her sıfır $2^{n+1}, 2^{n+2}, \dots$ ağırlıklı yeni basamak demektir. Katsayı $b = 0$ olduğundan katkı $0 \cdot 2^{n+k} = 0$ olur.
  - Örnek: $101101_2 = 1\cdot2^5+0\cdot2^4+1\cdot2^3+1\cdot2^2+0\cdot2^1+1\cdot2^0 = 45$.
  - Başına `00` eklenirse: $0\cdot2^7+0\cdot2^6 + (\text{aynı toplam}) = 0 + 45 = 45$. Değişmez.

- **Kesirli kısım, sağa sıfır ekleme:** Mevcut en küçük basamak $2^{-m}$ olsun. Sağa eklenen her sıfır $2^{-(m+1)}, 2^{-(m+2)}, \dots$ ağırlıklı yeni basamak demektir. Katsayı $0$ olduğundan katkı $0 \cdot 2^{-(m+k)} = 0$ olur.
  - Örnek: $0.01101_2 = 0\cdot2^{-1}+1\cdot2^{-2}+1\cdot2^{-3}+0\cdot2^{-4}+1\cdot2^{-5} = 0.40625$.
  - Sonuna `000` eklenirse ($0.01101000_2$): ek terimler $0\cdot2^{-6}+0\cdot2^{-7}+0\cdot2^{-8} = 0$. Toplam yine $0.40625$. Değişmez.

Bu yüzden doğru yönde eklenen sıfır salt gösterim uzunluğunu değiştirir, sayısal değeri değiştirmez.

---

### 3. Kesirli kısmı dörtlü gruplara ayırmak için `01101` yerine `00001101` yazan bir öğrencinin bulacağı onaltılı ve onluk değeri hesaplayın.

Hata: kesirli kısımda eksik grup **sola** sıfır eklenerek tamamlanmış. Yani öğrenci noktadan sonra `01101` (5 bit) yerine `00001101` (8 bit) okumuş.

Gruplama hatalı da olsa 4'e tam bölündüğü için öğrenci fark etmez:

```
yanlış kesir: 0000 1101
                0    D
```

- **Öğrencinin bulduğu onaltılı sonuç:** $(2D.0D)_{16}$ (doğrusu $2D.68$ iken).
- **Gerçek onluk değeri:**
  - Tam kısım: $2D_{16} = 2\cdot16+13 = 45$.
  - Kesir: $.0D_{16} = 0\cdot16^{-1} + 13\cdot16^{-2} = 13/256 = 0.05078125$.
  - **Toplam:** $45.05078125_{10}$.
- **İkili karşılıkla doğrulama:** $(0.00001101)_2 = 1\cdot2^{-5}+1\cdot2^{-6}+1\cdot2^{-8} = 1/32+1/64+1/256 = (8+4+1)/256 = 13/256 = 0.05078125$. Aynı sonuç.
- **Hatanın büyüklüğü:** Doğru değer $45.40625$, yanlış değer $45.05078125$. Mutlak hata $= 0.35546875$. Kesir neredeyse 8 kat küçülmüş ($104/256$ yerine $13/256$).

Teşhis: sola eklenen 3 sıfır kesir bitlerini 3 konum sağa itmiş, her biti $2^{-3} = 1/8$ ile çarpmış gibi etki yapmış + ayrıca grup kayması hex basamak değerini bozmuş.

---

### 4. "Eksik gruplar her zaman sola sıfır eklenerek tamamlanır" iddiasını bir karşı örnekle çürütün.

**Karşı örnek:** Yukarıdaki kesirli kısım `01101`.

- Sola sıfırla tamamlama (iddianın önerdiği): `.00001101_2 = 13/256 = 0.05078125 \to (0D)_{16}`. **Yanlış.**
- Sağa sıfırla tamamlama (doğrusu): `.01101000_2 = 104/256 = 0.40625 \to (68)_{16}`. **Doğru.**
- $0.05078125 \ne 0.40625$ olduğundan iddia çürür.

Tam kısımda da tersi geçerlidir: `101` tam sayısını 4'lü gruba sağa sıfırla tamamlamak `1010_2 = A_{16} = 10` verir, oysa sola sıfırla tamamlama `0101_2 = 5_{16} = 5` doğrudur. Yani yön karıştırılırsa tam kısımda da hata olur.

**Doğru kural:** tam kısımda eksik grup **sola**, kesirli kısımda eksik grup **sağa** sıfır eklenerek tamamlanır. Gerekçe: değer taşımayan ağırlıksız taraf (tam kısımda yüksek basamaklar, kesirde düşük basamaklar) doldurulmalıdır.

---

### 5. Doğru ikili, sekizli ve onaltılı gösterimleri ayrı ayrı onluya çevirerek eşitliklerini doğrulayın.

Beklenen ortak değer: $45.40625_{10}$.

**a) İkili $(101101.01101)_2$:**
$$1\cdot2^5+0\cdot2^4+1\cdot2^3+1\cdot2^2+0\cdot2^1+1\cdot2^0 = 32+8+4+1 = 45$$
$$0\cdot2^{-1}+1\cdot2^{-2}+1\cdot2^{-3}+0\cdot2^{-4}+1\cdot2^{-5} = 1/4+1/8+1/32 = (8+4+1)/32 = 13/32 = 0.40625$$
Toplam $= 45.40625$.

**b) Sekizli $(55.32)_8$:**
$$5\cdot8^1+5\cdot8^0 = 40+5 = 45$$
$$3\cdot8^{-1}+2\cdot8^{-2} = 3/8+2/64 = (24+2)/64 = 26/64 = 13/32 = 0.40625$$
Toplam $= 45.40625$.

**c) Onaltılı $(2D.68)_{16}$:**
$$2\cdot16^1+13\cdot16^0 = 32+13 = 45$$
$$6\cdot16^{-1}+8\cdot16^{-2} = 6/16+8/256 = (96+8)/256 = 104/256 = 13/32 = 0.40625$$
Toplam $= 45.40625$.

**Sonuç:** $(101101.01101)_2 = (55.32)_8 = (2D.68)_{16} = (45.40625)_{10}$ kanıtlandı.

---

### Düşünme Sorusu
> **Soru:** `00101.100` ve `101.1` ikili gösterimleri aynı değeri mi taşır? Değerlerinin eşit olması, gösterimlerinde aynı sayıda bit bulunduğu anlamına gelir mi?

**Yanıt:** **Evet, aynı değeri taşırlar; hayır, aynı sayıda bit bulunması gerekmez.**

- `00101.100`: tam $= 0\cdot16+0\cdot8+1\cdot4+0\cdot2+1\cdot1 = 5$; kesir $= 1\cdot1/2+0\cdot1/4+0\cdot1/8 = 0.5$. Toplam $5.5$.
- `101.1`: tam $= 1\cdot4+0\cdot2+1\cdot1 = 5$; kesir $= 1\cdot1/2 = 0.5$. Toplam $5.5$.
- Değerler eşit ($5.5 = 5.5$), çünkü başa eklenen `00` ve sona eklenen `00` sıfır ağırlıklı katkılar yaptı (Bölüm 2'deki gerekçe).
- Bit sayıları farklı: birincisi 5+3 = 8 bit, ikincisi 3+1 = 4 bit. Değer eşitliği gösterim uzunluğu eşitliği gerektirmez; sıfır ekleme değeri koruyarak uzunluğu değiştirir.

---

### Kısa Cevap ve Doğrulama Notları (Deney 3)
- **İlk tahminim:** $101101_2 = 45$, kesir $13/32 = 0.40625$ olacak; sekizli $55.32$, onaltılı $2D.68$ çıkacak. Sola-sıfır hatası kesri $13/256$ yapacak.
- **Bağımsız kontrolüm:** Basamak ağırlıkları el ile toplandı, `dogrulama_3.py` (Fraction tabanlı, kayan-nokta hatasız) ile üç tabanın da $45 + 13/32$ verdiği ve hatalı yazımın $45 + 13/256$ verdiği doğrulandı.
- **Karşı örneğim:** `.01101` kesrinde sola tamamlama $0.05078125$, sağa tamamlama $0.40625$ verir; "hep sola" iddiası bu tek örnekle çürür.
- **YZ önerisini değerlendirmem veya kullanmadım beyanım:** YZ desteğiyle hazırlanan gruplama tablosu, bağımsız el hesabı ve `dogrulama_3.py` çıktısıyla tek tek karşılaştırılıp doğrulandı; ezbere alınmadı.

---

# DENEY YAPRAĞI 4 ÇÖZÜMÜ
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

Deney 2 için `dogrulama_2.py`, Deney 4 için `dogrulama_4.py` dosyalarını kullandım. Kodlar ayrı dosyalardadır.


---

# DENEY YAPRAĞI 5 ÇÖZÜMÜ
### Bir Çözümdeki Hatanın Kaynağını Bulma

- **Amaç:** Sunulan çözümü hesapla denetlemek ve yanlış iddiayı düzeltmek.
- **Denetlenen iddialar:**
  - A: $(0.65)_{10} = (0.101)_2$
  - B: $(0.975)_{10} = (0.F99)_{16}$
  - C: $(101101.01101)_2 = (2D.0D)_{16}$
  - D: Bir ikili tam sayının sağına sıfır eklemek değerini değiştirmez.

---

### 1. İddiaları değerlendirin. Tam eşitlik olan ifade ile yalnızca yaklaşık değer veren ifadeyi ayırt edin.

- **A: yaklaşık (≈), `=` yanlış.** Sağ taraf 3 bitlik kesilmiş değerdir, hata $0.025 \ne 0$.
- **B: yaklaşık (≈), `=` yanlış.** Sağ taraf 3 basamaklık kesilmiş değerdir, hata $\approx 0.0001465 \ne 0$.
- **C: yanlış basamak, tümden hatalı.** Sağ tarafın kesir basamakları (`0D` yerine `68`) hatalıdır; `=` de `≈` de kurtarmaz, basamaklar düzeltilmelidir.
- **D: yanlış genelleme.** Sıfırdan farklı her tam sayıda sağa sıfır değeri değiştirir (2 katına çıkarır).

Sonuç: dört iddiada da `=` ile yazılmış tam eşitlik yoktur; A ve B `≈` ile kurtarılabilir, C ve D içerik olarak düzeltilmelidir.

---

### 2. A ve B'nin sağ taraflarındaki gösterimlerin gerçek onluk değerlerini ve sol tarafla aralarındaki mutlak hataları hesaplayın.

Mutlak hata: $|\text{Gerçek} - \text{Gösterim}|$.

**A: $(0.101)_2$:**
$$\text{Değer} = 1\cdot2^{-1}+0\cdot2^{-2}+1\cdot2^{-3} = 1/2+1/8 = 5/8 = 0.625$$
$$\text{Hata} = |0.65 - 0.625| = 0.025 = 1/40$$

Kontrol: $0.65$'in ilk 3 ikili basamağı gerçekten `101` çıkar ($0.65·2=1.3\to1$; $0.3·2=0.6\to0$; $0.6·2=1.2\to1$). Yani basamaklar doğru, `=` işareti yanlıştır.

**B: $(0.F99)_{16}$:**
$$\text{Değer} = 15\cdot16^{-1}+9\cdot16^{-2}+9\cdot16^{-3} = 15/16+9/256+9/4096 = 3993/4096 \approx 0.9748535156$$
$$\text{Hata} = |0.975 - 3993/4096| = |3993.6/4096 - 3993/4096| = 0.6/4096 \approx 0.0001464844$$

Kontrol: $0.975·16=15.6\to F$; $0.6·16=9.6\to 9$; $0.6·16=9.6\to 9$; devamı $999\dots$ devirlidir. Yani basamaklar doğru kesilmiştir, `=` işareti yanlıştır.

---

### 3. C'de hatalı sıfır tamamlamanın nerede yapıldığını gösterin ve doğru sonucu bulun.

Hata kesirli kısımda, dörtlü gruplamada yapılmıştır:

- Doğrusu: `.01101` soldan sağa gruplanır, sağa `000` eklenir → `0110 1000` → `.68`.
- Hatalısı: `.01101` sola `000` eklenerek `0000 1101` yapılmış → `.0D`. Yani sıfır yanlış tarafa (sola) eklenmiş.

Değerler:
- Doğru: $(2D.68)_{16} = 2·16+13 + (6/16+8/256) = 45 + 13/32 = 45.40625$.
- Hatalı: $(2D.0D)_{16} = 45 + 13/256 = 45.05078125$.
- Mutlak hata: $13/32 - 13/256 = 91/256 = 0.35546875$.

**Doğru sonuç:** $(101101.01101)_2 = (2D.68)_{16} = (55.32)_8 = (45.40625)_{10}$ (tam eşitlik, `=` doğrudur).

---

### 4. D için sıfırdan farklı bir karşı örnek verin. Sağa sıfır eklemenin genel etkisini yazın.

**Karşı örnek:** $(101)_2 = 5$. Sağına bir sıfır eklenirse $(1010)_2 = 8+2 = 10 \ne 5$. En küçük örnek: $(1)_2 = 1 \to (10)_2 = 2$.

**Genel etki:** $n$ bitlik tam sayının sağına $k$ sıfır eklemek her biti $k$ konum sola kaydırmaktır (sola kaydırma / left shift):

$$[\,b_{n-1}\dots b_0\,0\dots0\,]_2 = \left(\sum b_i 2^i\right)\cdot 2^k$$

Yani değer $2^k$ ile çarpılır (1 sıfır → ×2, 2 sıfır → ×4, ...). Değeri değiştirmeyen sıfır, tam sayıda **soluna** eklenendir ($0\cdot2^{n} = 0$).

---

### 5. Dört iddiayı doğru ve açık ifadelerle yeniden yazın. Yaklaşık sonuçlarda $\approx$ işaretini kullanın.

- **A (düzeltilmiş):** $(0.65)_{10} \approx (0.101)_2$ (3 bit kesilmiş, hata $0.025$). Daha iyi 8-bit sürüm: $(0.65)_{10} \approx (0.10100110)_2$ (hata $0.0015625$).
- **B (düzeltilmiş):** $(0.975)_{10} \approx (0.F99)_{16}$ (3 basamak kesilmiş, hata $\approx 0.0001465$).
- **C (düzeltilmiş):** $(101101.01101)_2 = (2D.68)_{16}$ (tam eşitlik). Rapordaki $(2D.0D)_{16}$ yanlıştır (kesre sola sıfır ekleme hatası, hata $0.35546875$).
- **D (düzeltilmiş):** Bir ikili tam sayının **soluna** sıfır eklemek değeri değiştirmez; **sağına** eklenen her sıfır değeri 2 katına çıkarır (sağa $k$ sıfır → $\times 2^k$).

---

### Düşünme Sorusu
> **Soru:** İşlem adımları doğru görünürken sonuç ifadesi yine de yanlış olabilir mi? A veya B üzerinden açıklayın.

**Yanıt:** **Evet, olabilir. Hesap adımlarının doğruluğu, sonuç iddiasının doğruluğunu garanti etmez.**

Örnek A: $0.65$'in ilk üç basamağı doğru bulunur (`1,0,1`). Adımlar doğrudur. Hata son adımdadır: kesilmiş 3-bitlik değeri `=` ile tam eşitlik gibi sunmak. Doğru basamak + yanlış kesinlik iddiası = yanlış sonuç ifadesi. Aynı durum B'de de vardır: `F,9,9` basamakları doğru üretilir ama sonsuz devirli sayının kesilmiş hali `=` ile bitirilirse ifade yanlış olur. Yani denetim yalnız basamakları değil, `=` / `≈` seçimini de kapsamalıdır.

---

### Kısa Cevap ve Doğrulama Notları (Deney 5)
- **İlk tahminim:** A ve B'de basamaklar doğru ama `=` yanlış (`≈` olmalı); C'de kesir basamağı tümden yanlış (`0D` yerine `68`); D sağ-sol karıştırması, sağa sıfır ×2 yapar.
- **Bağımsız kontrolüm:** Sağ taraflar ağırlıklarla el ile toplandı ($5/8$, $3993/4096$, $13/256$); `dogrulama_5.py` (Fraction tabanlı) hataları aynen verdi ($0.025$; $\approx 0.0001465$; $0.35546875$).
- **Karşı örneğim:** D için $(1)_2=1 \to (10)_2=2$ (veya $5 \to 10$); C için `.00001101$ vs `.01101000` ($13/256$ vs $13/32$).
- **YZ önerisini değerlendirmem veya kullanmadım beyanım:** YZ desteğiyle hazırlanan tablo, bağımsız el hesabı ve `dogrulama_5.py` çıktısıyla tek tek karşılaştırılıp doğrulandı.

---

# DENEY YAPRAĞI 6 ÇÖZÜMÜ
### Taban Bilgisi Kaybolmuş Kayıtların Çözümlenmesi

- **Amaç:** Olası tabanları elemek, ortak değeri bulmak ve belirsizliği açıklamak.
- **Kayıtlar:** A = `17`, B = `21`, C = `10001`. Aday tabanlar {2, 8, 10, 16}. Tabanlar birbirinden farklı olabilir (zorunlu değil).

---

### 1. Her kayıt için rakamların geçerli olduğu bütün kaynak tabanlarını belirleyin.

Kural: sayıdaki her rakam değeri kaynak tabandan küçük olmalı.

- **A `17`:** rakam `7` içerir → taban 2 geçersiz (`7 ≥ 2`). **Geçerli: 8, 10, 16.**
- **B `21`:** rakam `2` içerir → taban 2 geçersiz (`2 ≥ 2`). **Geçerli: 8, 10, 16.**
- **C `10001`:** yalnız `0` ve `1` içerir → **Geçerli: 2, 8, 10, 16** (dördü de).

---

### 2. Her geçerli yorumun onluk karşılığını hesaplayın ve bir tabloda gösterin.

| Kayıt | Taban 2 | Taban 8 | Taban 10 | Taban 16 |
|:-----:|:-------:|:-------:|:--------:|:--------:|
| **A `17`** | — (geçersiz, `7`) | $1·8+7 = 15$ | $17$ | $1·16+7 = 23$ |
| **B `21`** | — (geçersiz, `2`) | $2·8+1 = 17$ | $21$ | $2·16+1 = 33$ |
| **C `10001`** | $1·2^4+1 = 17$ | $1·8^4+1 = 4097$ | $10001$ | $1·16^4+1 = 65537$ |

C satırı açılımı: $10001_8 = 1·4096+0·512+0·64+0·8+1$; $10001_{16} = 1·65536+1$.

---

### 3. Üç kaydın aynı sayıyı göstermesi koşuluyla ortak değeri ve cihazların tabanlarını bulun.

Kesişim: A kümesi {15, 17, 23}, B kümesi {17, 21, 33}, C kümesi {17, 4097, 10001, 65537}.

- Ortak değer: **$17_{10}$**.
- Tabanlar: **A = 10** (`17_10 = 17`), **B = 8** (`21_8 = 17`), **C = 2** (`10001_2 = 17`).

Sağlama: $2·8+1 = 17$; $1·2^4+1 = 17$; `17_10` zaten 17.

---

### 4. Başka bir çözüm bulunup bulunmadığını bütün geçerli yorumları karşılaştırarak gösterin.

Geçerli kombinasyon sayısı $3·3·4 = 36$'dır; `dogrulama_6.py` hepsini tarar, eşitlik koşulunu sağlayan **1** kombinasyon bulur.

Kısa ispat: A∩B = {17} tek elemanlıdır ({15,17,23} ∩ {17,21,33} = {17}). Bu durumda A tabanı 10, B tabanı 8 olmak zorundadır. C'nin 17 vermesi için tek seçenek taban 2'dir (4097, 10001, 65537 elenir). Dolayısıyla çözüm **tektir**, başka çözüm yoktur.

---

### 5. Üç kayıt da `10` olsaydı tabanları tek bir şekilde belirleyebilir miydiniz? Olası yorumlarla gerekçelendirin.

**Hayır, tek şekilde belirlenemezdi; 4 çözüm olurdu.**

`10` dört tabanda da geçerlidir ve değerleri farklıdır: $10_2 = 2$, $10_8 = 8$, $10_{10} = 10$, $10_{16} = 16$ (genel olarak değeri tabanın kendisidir).

Üç kayıt aynı sayıyı göstermeli → üç değer eşit olmalı → üç taban eşit olmalı (değerler birebir olduğundan farklı tabanlar farklı değer verir). Çözümler:

1. Üçü de taban 2 → değer 2.
2. Üçü de taban 8 → değer 8.
3. Üçü de taban 10 → değer 10.
4. Üçü de taban 16 → değer 16.

Hangi çözümün gerçek olduğu kayıtlardan anlaşılmaz. (Not: "tabanlar farklı olabilir" izin demektir, zorunluluk değil; zorunlu farklılık okunsaydı bu durumda **hiç** çözüm olmazdı.)

---

### 6. Taban belirsizliğini önlemek için sayı ve tabanı birlikte taşıyan açık bir kayıt biçimi tasarlayın. Üç örnek kayıt yazın.

**Biçim:** `(sayı)_taban` — sayı ve taban aynı yazımda, taban onluk belirtilir; boşluk yok, taban alta değil düz yazıda `_` ile ayrılır. Reddetme kuralı: rakam ≥ taban ise kayıt geçersizdir.

Örnekler (çözüme karşılık):

- `(17)_10` → A cihazı, değer 17.
- `(21)_8` → B cihazı, değer 17.
- `(10001)_2` → C cihazı, değer 17.

Aynı bilgiyi tutan eşdeğer yazımlar da kabul: `10#17`, `8#21`, `2#10001` veya `17(d10)`. Yeter ki taban sayıdan ayrılamaz şekilde bitişik yazılsın.

---

### Düşünme Sorusu
> **Soru:** Bir kaydın bütün rakamlarının belirli bir tabanda geçerli olması, kaydın gerçekten o tabanda yazıldığını kanıtlar mı?

**Yanıt:** **Hayır, kanıtlamaz. Geçerlilik gerekli koşuldur, yeterli değildir.**

Örnek: `17` taban 8'de geçerlidir ($15$ değerini verir) ama bu deneyde gerçekten taban 10'da yazılmıştır ($17$). Aynı kayıt üç tabanda geçerli, gerçek biri. Benzer: `10` dört tabanda geçerli ama gerçek yazım biri. Geçerlilik yalnız eleme yapar; gerçek tabanı bulmak için ek bilgi (bu deneyde üç kaydın eşitliği koşulu, genel durumda açık taban etiketi) gerekir.

---

### Kısa Cevap ve Doğrulama Notları (Deney 6)
- **İlk tahminim:** `17` ve `21` taban 2'de elenecek; kesişim 17'de birleşecek (A=10, B=8, C=2); `10,10,10` durumunda 4 çözüm çıkacak.
- **Bağımsız kontrolüm:** Tablo el ile ağırıklarla hesaplandı; `dogrulama_6.py` 36 kombinasyonu taradı: 1 ortak çözüm (17) ve `10` durumunda 4 çözüm doğrulandı.
- **Karşı örneğim:** `17` taban 8'de geçerli ama gerçek taban 10 — geçerlilik yazımı kanıtlamaz; `10` kaydının 4 tabanda 4 farklı değeri belirsizliğin sürdüğünü gösterir.
- **YZ önerisini değerlendirmem veya kullanmadım beyanım:** YZ desteğiyle hazırlanan tablo ve sayım, bağımsız el hesabı ve `dogrulama_6.py` çıktısıyla tek tek karşılaştırılıp doğrulandı.

---

# DENEY YAPRAĞI 7 ÇÖZÜMÜ
### Tek Bit Değişiminin Sayısal Etkisi

- **Amaç:** Bit konumu ile hata büyüklüğünü ilişkilendirmek ve aralık kontrolünü sınamak.
- **Tanım:** $(173)_{10}$ sekiz bit işaretsiz tutulur. Her deneme başlangıç değerinden yapılır, yalnız bir bit tersine döner. Geçerli aralık 0–200.

---

### 1. Başlangıç değerini sekiz bit ile yazın. MSB ve LSB'yi işaretleyin. Bit konumlarını LSB için 0, MSB için 7 olacak şekilde numaralandırın.

$$173 = 128+32+8+4+1 = (10101101)_2$$

```
konum:  7 6 5 4 3 2 1 0
bit:    1 0 1 0 1 1 0 1
        ^             ^
       MSB           LSB
```

MSB = $b_7 = 1$ (ağırlık $2^7 = 128$), LSB = $b_0 = 1$ (ağırlık $2^0 = 1$).

---

### 2-3. Sekiz bitin her birini ayrı ayrı tersine çevirin. İkili ve onluk değerler, yön ve mutlak hata.

Mutlak hata: $|\text{Hatalı} - 173|$. Yön: hatalı > 173 ise arttı, küçükse azaldı.

| Deneme (konum $k$) | Orijinal bit | Hatalı ikili | Hatalı onluk | Yön | Mutlak hata |
|:--:|:--:|:--:|:--:|:--:|:--:|
| $k=7$ (MSB) | $1\to0$ | `00101101` | 45 | azaldı | 128 |
| $k=6$ | $0\to1$ | `11101101` | 237 | arttı | 64 |
| $k=5$ | $1\to0$ | `10001101` | 141 | azaldı | 32 |
| $k=4$ | $0\to1$ | `10111101` | 189 | arttı | 16 |
| $k=3$ | $1\to0$ | `10100101` | 165 | azaldı | 8 |
| $k=2$ | $1\to0$ | `10101001` | 169 | azaldı | 4 |
| $k=1$ | $0\to1$ | `10101111` | 175 | arttı | 2 |
| $k=0$ (LSB) | $1\to0$ | `10101100` | 172 | azaldı | 1 |

Kural doğrulanır: hata $= 2^k$ ($128, 64, 32, 16, 8, 4, 2, 1$); yön orijinal bite bağlıdır ($0\to1$ arttırır, $1\to0$ azaltır).

---

### 4. "MSB'deki hata her zaman sayıyı artırır" iddiasını başlangıç değeri üzerinden değerlendirin.

**Yanlış.** Bu değerde MSB $1$ olduğundan tersinmesi $1\to0$ olur ve sayı $173 \to 45$ **azalır** (hata $-128$). MSB hatasının yönü orijinal bite bağlıdır: bit $0$ ise artırır ($+128$), bit $1$ ise azaltır ($-128$). Tek örnekle ($k=7$: arttı değil azaldı) iddia çürür.

---

### 5. Yalnızca 0–200 aralık kontrolünün hangi hataları yakalayacağını belirleyin. Aralıkta kalan hatalı bir değeri örnek gösterin.

Değerler: 45, 237, 141, 189, 165, 169, 175, 172.

- **Yakalanan (aralık dışı):** yalnız $k=6$ → 237 (> 200). 8 denemede 1'i.
- **Kaçan (aralık içi ama hatalı):** kalan 7'si (45, 141, 189, 165, 169, 175, 172).

**Örnek:** $k=4$ hatası 189 aralıktadır ama hatalıdır (gerçek 173, hata 16). Daha çarpıcı örnek: $k=7$ hatası 45 aralıktadır ama hata 128'dir — büyük hata aralık kontrolünden kaçar. Yani aralık kontrolü gerekli ama yetersizdir.

---

### 6. Başlangıç değerini ve sekiz hatalı değeri onaltılı sisteme çevirerek karşılaştırın.

$173 = AD_{16}$ ($10·16+13$). Dörtlü gruplama: `1010 1101` → `A D`.

| Konum $k$ | İkili | Hex | Yorum |
|:--:|:--:|:--:|:---|
| — (başlangıç) | `10101101` | `AD` | referans |
| 7 | `00101101` | `2D` | yüksek nibble `A→2` (128'lik değişim) |
| 6 | `11101101` | `ED` | yüksek nibble `A→E` |
| 5 | `10001101` | `8D` | yüksek nibble `A→8` |
| 4 | `10111101` | `BD` | yüksek nibble `A→B` |
| 3 | `10100101` | `A5` | düşük nibble `D→5` |
| 2 | `10101001` | `A9` | düşük nibble `D→9` |
| 1 | `10101111` | `AF` | düşük nibble `D→F` |
| 0 | `10101100` | `AC` | düşük nibble `D→C` |

Örüntü: $k \ge 4$ hataları yüksek hex basamağını, $k < 4$ hataları düşük hex basamağını değiştirir (1 hex basamak = 4 bit olduğundan). Hex büyüklük sırası onluk sırayla aynıdır ($2D < 8D < A5 < A9 < AC < AD < AF < BD < ED$).

---

### Düşünme Sorusu
> **Soru:** "Tek bir bit değiştiği için sayısal hata küçüktür" ifadesi neden güvenilir değildir? Bit konumu ile hata büyüklüğü arasındaki genel ilişkiyi yazın.

**Yanıt:** **Güvenilmez, çünkü hata bit sayısına değil bit konumuna bağlıdır ve üstel büyür.**

Genel ilişki: $k$ konumundaki tek-bit hatasının mutlak büyüklüğü

$$|\text{Hata}| = 2^k$$

($k=0$ için 1, $k=7$ için 128). Bu deneyde tek-bit hatalar 1'den 128'e kadar değişir — 128 kat fark. "Tek bit" sayısal küçüklük garantilemez; hangi bit olduğu belirler. MSB hatası (128) 8-bit aralığın yarısıdır.

---

### Kısa Cevap ve Doğrulama Notları (Deney 7)
- **İlk tahminim:** 173 = `10101101` (AD); hatalar $173 \pm 2^k$ olacak; MSB $1\to0$ azalış verecek; aralık yalnız 237'yi yakalayacak.
- **Bağımsız kontrolüm:** Tablo el ile ağırıklarla hesaplandı; `dogrulama_7.py` 8 flipi taradı: hatalar $2^k$, hex değerler ve aralık sonucu birebir tuttu (7 kaçan, 1 yakalanan).
- **Karşı örneğim:** "MSB artırır" → $k=7$: $173\to45$ azaldı. "Tek bit küçüktür" → $k=7$ hatası 128. "Aralık yeter" → 45 ve 189 aralıkta ama hatalı.
- **YZ önerisini değerlendirmem veya kullanmadım beyanım:** YZ desteğiyle hazırlanan tablo, bağımsız el hesabı ve `dogrulama_7.py` çıktısıyla tek tek karşılaştırılıp doğrulandı.
