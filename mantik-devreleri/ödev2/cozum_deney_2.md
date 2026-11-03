# BLM2007 Mantık Devreleri Laboratuvarı — Ödev 2 Çözüm Raporu
## Deney Yaprağı 2: Borç alma ve 2 tümleyeniyle çıkarma

**Öğrenci Adı Soyadı:** Efe Özan  
**Öğrenci No:** 170425062  
**Bölüm:** Bilgisayar Mühendisliği  
**Ders:** BLM2007 Mantık Devreleri (Prof. Dr. Ali Buldu)  
**Tarih:** 29 Ekim 2026  
**Şube / Grup:** Ali Buldu A Grubu **İmza:** ......................

---

- **Amaç:** Aynı farkı iki bağımsız algoritmayla bulmak ve negatif sonuçları büyüklükleriyle açıklamak.
- **Kod dosyaları:** `ikili_cikarici.py` ve `dogrulama_2.py`.

---

### 1. İki bağımsız bit düzeyi algoritma

1. **Borç alarak doğrudan çıkarma (`borc_alarak_cikar`):** Tam çıkarıcı tablosuyla sağdan sola ilerler. Son borç `0` ise sonuç `ham_fark` (veya `0000`), son borç `1` ise sonuç negatiftir ve büyüklük $N - M$ borç zinciriyle bulunup `-büyüklük` olarak verilir.
2. **2 tümleyeniyle çıkarma (`iki_tumleyeniyle_cikar`):** $M + \sim N + 1$ ($c_0 = 1$) toplamını bit düzeyinde yapar. Ham toplam `0000` ise sonuç `0000` (sıfır durumu); `son_elde == 1` ise pozitif (`ham_toplam`); `son_elde == 0` ise negatiftir ve `ham_toplam`'ın 2 tümleyeni alınarak `-büyüklük` olarak verilir.

### 2. Beş zorunlu işlemin iki yöntemle çözümü ve ara kayıtları

| İşlem | Borç Yöntemi: Ham Fark | Borç Zinciri (sütun 0→3) | Son Borç | 2 Tümleyeni: $\sim N$ | 4-bit $(-N)$ | Ham Toplam | Elde Zinciri (sütun 0→3) | Son Elde | Sonuç (Onlu) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1110 − 0011` | `1011` | `[1,1,0,0]` | `0` | `1100` | `1101` | `1011` | `[0,0,1,1]` | `1` | `1011` ($11$) |
| `0011 − 1110` | `0101` | `[0,0,1,1]` | `1` | `0001` | `0010` | `0101` | `[1,1,0,0]` | `0` | `-1011` ($-11$) |
| `1000 − 0001` | `0111` | `[1,1,1,0]` | `0` | `1110` | `1111` | `0111` | `[0,0,0,1]` | `1` | `0111` ($7$) |
| `0101 − 0101` | `0000` | `[0,0,0,0]` | `0` | `1010` | `1011` | `0000` | `[1,1,1,1]` | `1` | `0000` ($0$) |
| `0011 − 0000` | `0011` | `[0,0,0,0]` | `0` | `1111` | `0000` | `0011` | `[1,1,1,1]` | `1` | `0011` ($3$) |

### 3. 256 test özeti ve uyumsuzluk düzeltmesi

- $0\text{--}15$ aralığındaki $16 \times 16 = 256$ çiftin tamamında iki yöntem ve referans fark eşleşmiştir (256/256 başarılı).
- **Uyumsuzluk ve YZ doğrulama kaydı:** 4-bit 2 tümleyeni ($N=0000 \to 0000$) ile $c_0=0$ toplaması yapan naif yaklaşımda `0000 - 0000` çiftinde `-0000`, `0001 - 0000` çiftinde ise `son_elde=0` yüzünden `+1` yerine `-1111` (`-15`) çıkar; bu yüzden işlem $M + \sim N + 1$ ($c_0=1$) şeklinde kurulmuştur. YZ'nin önerdiği iki yöntemi 256 testte onlu referansla karşılaştırarak doğruladım; $N=0000$ sınır durumunu elle hesapladım.

### 4. $N = 0$ ile karşı örnek ve karar kuralı

- Sıfırın (`0000`) 4-bit 2 tümleyeni $\sim 0000 + 1 = 1111 + 1 = (1)0000 \to \text{`0000`}$'dır.
- 4-bit tümleyenle $M + 0000$ yapıldığında `son_elde = 0` çıkar. En küçük karşı örnek $M = 0000, N = 0000$ (sonuç $0$), en küçük pozitif karşı örnek **$M = 0001, N = 0000$** (sonuç $+1$, negatif değil).
