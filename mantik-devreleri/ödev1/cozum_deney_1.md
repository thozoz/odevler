# BLM2007 Mantık Devreleri Laboratuvarı — Ödev 1 Çözüm Raporu
## Deney Yaprağı 1

**Öğrenci Adı Soyadı:** ............................................................
**Öğrenci No:** .............................
**Bölüm:** Bilgisayar Mühendisliği
**Ders:** BLM2007 Mantık Devreleri (Prof. Dr. Ali Buldu)
**Tarih:** 12 Ekim 2026
**Şube / Grup:** ...................... **İmza:** ......................

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
