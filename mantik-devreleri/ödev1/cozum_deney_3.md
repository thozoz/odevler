# BLM2007 Mantık Devreleri Laboratuvarı — Ödev 1 Çözüm Raporu
## Deney Yaprağı 3

**Öğrenci Adı Soyadı:** ............................................................
**Öğrenci No:** .............................
**Bölüm:** Bilgisayar Mühendisliği
**Ders:** BLM2007 Mantık Devreleri (Prof. Dr. Ali Buldu)
**Tarih:** 12 Ekim 2026
**Şube / Grup:** ...................... **İmza:** ......................

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
