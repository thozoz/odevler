# BLM2007 Mantık Devreleri Laboratuvarı — Ödev 2 Çözüm Raporu
## Deney Yaprağı 3 ve Deney Yaprağı 4

**Öğrenci Adı Soyadı:** Efe Özan  
**Öğrenci No:** 170425062  
**Bölüm:** Bilgisayar Mühendisliği  
**Ders:** BLM2007 Mantık Devreleri (Prof. Dr. Ali Buldu)  
**Tarih:** 29 Ekim 2026  
**Şube / Grup:** Ali Buldu A Grubu **İmza:** ......................

---

# DENEY YAPRAĞI 3: Kısmi çarpımlarla ikili çarpıcı

- **Kod dosyaları:** `ikili_carpici.py` ve `dogrulama_3.py`.
- **Kaydırma kuralı:** Çarpanın sağdan $i$. biti $b_i$ için $n$ bitlik kısmi çarpım ($b_i=1$ ise $A$, $b_i=0$ ise $0^n$) sağına $i$ sıfır, soluna $m-i$ sıfır eklenerek $n+m$ bit genişliğinde hizalanır.
- **Üç zorunlu çarpım:**
  1. `1011 × 101` ($11 \times 5 = 55$, 7 bit): Satırlar `0001011` ($11$), `0000000` ($0$), `0101100` ($44$) $\to$ Toplam **`0110111`** ($55$).
  2. `10111 × 110` ($23 \times 6 = 138$, 8 bit): Satırlar `00000000` ($0$), `00101110` ($46$), `01011100` ($92$) $\to$ Toplam **`10001010`** ($138$).
  3. `11001 × 1010` ($25 \times 10 = 250$, 9 bit): Satırlar `000000000` ($0$), `000110010` ($50$), `000000000` ($0$), `011001000` ($200$) $\to$ Toplam **`011111010`** ($250$).
- **Sekiz test ve çağrı karşılaştırması:** Başlangıç akümülatörü $0^{n+m}$ iken Sürüm 1 her satır için 1 kez, toplamda $m$ kez toplama çağrısı yapar; Sürüm 2 yalnız $b_i=1$ olan satırlarda 1 kez, toplamda birlerin sayısı kadar çağrı yapar (`1101×000` için $3\to 0$, `1101×001` için $3\to 1$, `1011×1000` için $4\to 1$, `1111×111` için $3\to 3$).
- **Genişlik gerekçesi:** $(2^n-1)(2^m-1) = 2^{n+m}-2^n-2^m+1 < 2^{n+m}-1$ olduğundan $n+m$ bit her zaman yeterlidir. Karşı örnek: $n=2, m=2$ için `11 × 11 = 1001` ($3 \times 3 = 9$, 4 bit); $n+m-1 = 3$ bit en çok $7$ tuttuğundan yetmez.
- **YZ önerisi değerlendirme/doğrulama (Deney 3):** YZ'nin önerdiği sol/sağ sıfır doldurma kuralını (`m-i` sol sıfır, `i` sağ sıfır) `1011 × 101` işleminde satırların onlu katkılarını ($11 + 0 + 44 = 55$) toplayarak doğruladım.

---

# DENEY YAPRAĞI 4: Bölüm kalan ve kesirli bölme algoritması

- **Kod dosyaları:** `ikili_bolucu.py` ve `dogrulama_4.py`.
- **Üç zorunlu bölme ve kesirli sonuçlar:**
  1. `10110 ÷ 100` ($22 \div 4$): Tam $Q = \text{`101`}$ ($5$), $R = \text{`10`}$ ($2$). Kontrol: $22 = 5\times 4 + 2$ ve $0 \le 2 < 4$. Kesirli: **`= 101.1`** ($5.5$, 1. kesir adımında kalan `0`).
  2. `1101 ÷ 10` ($13 \div 2$): Tam $Q = \text{`110`}$ ($6$), $R = \text{`1`}$ ($1$). Kontrol: $13 = 6\times 2 + 1$ ve $0 \le 1 < 2$. Kesirli: **`= 110.1`** ($6.5$, 1. kesir adımında kalan `0`).
  3. `111 ÷ 11` ($7 \div 3$): Tam $Q = \text{`10`}$ ($2$), $R = \text{`1`}$ ($1$). Kontrol: $7 = 2\times 3 + 1$ ve $0 \le 1 < 3$. Kesirli: **`≈ 10.01010101`** (kalanlar `10, 1, 10, 1...` şeklinde tekrar eder, 8. basamakta kesilir).
- **Sınır testleri (Beklenen vs Gözlenen) ve ara sıfır örneği:**
  - `0000 ÷ 101`: Beklenen $Q=\text{`0`}, R=\text{`0`}$, Kesirli `= 0` | Gözlenen $Q=\text{`0`}, R=\text{`0`}$, Kesirli `= 0` (Eşleşti)
  - `011 ÷ 110`: Beklenen $Q=\text{`0`}, R=\text{`11`}$, Kesirli `= 0.1` | Gözlenen $Q=\text{`0`}, R=\text{`11`}$, Kesirli `= 0.1` (Eşleşti)
  - `101 ÷ 101`: Beklenen $Q=\text{`1`}, R=\text{`0`}$, Kesirli `= 1` | Gözlenen $Q=\text{`1`}, R=\text{`0`}$, Kesirli `= 1` (Eşleşti)
  - `101 ÷ 000`: Beklenen `SifiraBolmeHatasi` | Gözlenen `SifiraBolmeHatasi` (Reddedildi)
  - Ara sıfır örneği ve YZ doğrulaması: `1010 ÷ 10` ($10 \div 2 = 5$) işleminde doğru bölüm `101` ($5$) iken, ara sıfır biti atılırsa `11` ($3$) bulunur ($3 \times 2 + 0 = 6 \ne 10$). YZ'nin önerdiği kesir döngüsünü de `111 ÷ 11` işleminde kalanların `10` ve `1` olarak tekrar etmesiyle doğruladım.
