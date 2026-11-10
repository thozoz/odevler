# BLM2007 Mantık Devreleri — Deney Yaprağı 4 Çözümü
### Karakter Kodları ve Barkodun Bağımsız Doğrulanması

**Öğrenci:** Efe Özan (170425062)  
**Tarih:** 10.11.2026  
**Şube / Grup:** Ali Buldu A Grubu  
**İlgili Kodlar:** `karakter_ve_barkod.py`, `dogrulama_4.py`

---

### 1. ASCII ve EBCDIC Karakter Kodlayıcı/Çözümleyici

Desteklenen karakter kümesi (H, E, L, P, ' ' ve 0--3):
| Karakter | ASCII (Hex) | ASCII (8-Bit İkili) | EBCDIC IBM-037 (Hex) | EBCDIC (8-Bit İkili) |
|:---:|:---:|:---:|:---:|:---:|
| **H** | `48` | `0100 1000` | `C8` | `1100 1000` |
| **E** | `45` | `0100 0101` | `C5` | `1100 0101` |
| **L** | `4C` | `0100 1100` | `D3` | `1101 0011` |
| **P** | `50` | `0101 0000` | `D7` | `1101 0111` |
| **Boşluk** | `20` | `0010 0000` | `40` | `0100 0000` |
| **0** | `30` | `0011 0000` | `F0` | `1111 0000` |
| **1** | `31` | `0011 0001` | `F1` | `1111 0001` |
| **2** | `32` | `0011 0010` | `F2` | `1111 0010` |
| **3** | `33` | `0011 0011` | `F3` | `1111 0011` |

- **`HELP 2031` Metni Kodlama Sonuçları:**
  - ASCII: `48 45 4C 50 20 32 30 33 31`
  - EBCDIC: `C8 C5 D3 D7 40 F2 F0 F3 F1`
  - Her iki dize de çözümleyici ile kayıpsız olarak `HELP 2031` olarak geri çözüldü.

#### H Karakterinin Bağımsız Bit Ağırlıkları Denetimi
- **ASCII H:**
  - Hex hesabı: $4\cdot 16^1 + 8\cdot 16^0 = 64 + 8 = \mathbf{72_{10}}$
  - İkili hesabı: $01001000_2 = 2^6 + 2^3 = 64 + 8 = \mathbf{72_{10}}$ (Eşleşti).
- **EBCDIC H:**
  - Hex hesabı: $12\cdot 16^1 + 8\cdot 16^0 = 192 + 8 = \mathbf{200_{10}}$
  - İkili hesabı: $11001000_2 = 2^7 + 2^6 + 2^3 = 128 + 64 + 8 = \mathbf{200_{10}}$ (Eşleşti).

---

### 2. Çapraz Çözüm ve Üst Bit Yöntemi Yetersizliği

1. `48 45 4C 50` dizisi EBCDIC ile çözülmeye çalışıldığında tabloda tanımlı olmayan bayt hatasıyla reddedildi.
2. `C8 C5 D3 D7` dizisi ASCII ile çözülmeye çalışıldığında en anlamlı biti 1 olan baytlar ASCII tablosunda yer almadığı için reddedildi.
3. **Üst Bit (MSB) Ekleme/Kesme Neden Yetmez?**
   H harfinde tesadüfen ASCII (`01001000`) ile EBCDIC (`11001000`) arasında sadece en anlamlı bit farklı gibi dursa da bu genel bir kural değildir:
   - L harfinde: ASCII `4C` (`01001100`) $\to$ MSB 1 yapılırsa `CC` (`11001100`) olur; oysa gerçek EBCDIC `D3` (`11010011`)'tür ($CC \ne D3$).
   - P harfinde: ASCII `50` (`01010000`) $\to$ MSB 1 yapılırsa `D0` olur; oysa gerçek EBCDIC `D7`'dir ($D0 \ne D7$).
   - 0 rakamında: ASCII `30` (`00110000`) $\to$ MSB 1 yapılırsa `B0` olur; oysa gerçek EBCDIC `F0`'dır ($B0 \ne F0$).
   ASCII ve EBCDIC farklı tarihsel kökenlere ve bölge (zone) yapılarına sahiptir; doğrudan bit maskeleme ile dönüştürülemezler.

---

### 3. Code 128 Üretimi ve Bağımsız Okuma Deneyi

Üretici: `python-barcode` (Code 128)  
Bağımsız Okuyucu: `pyzbar` (libzbar)

| Girdi | Karakter Uzunluğu | Bağımsız Okuyucu Çıktısı | Karakter Karakter Eşleşme |
|:---|:---:|:---|:---:|
| `HELP 2031` | 9 | `HELP 2031` | Tam Eşleşti |
| `HELP2031` | 8 | `HELP2031` | Tam Eşleşti |
| `000123` | 6 | `000123` | Tam Eşleşti |
| `123` | 3 | `123` | Tam Eşleşti |

- **Boşluk Etkisi:** Boşluk karakteri barkodda ayrı bir optik sembol (Code 128 değeri 0) olarak çubuk/boşluk deseniyle kodlanır. Bu sayede boşluklu ve boşluksuz metinler optik olarak farklı genişlik ve desene sahip olur.
- **Başlangıç Sıfırının Etkisi:** Barkod sayısal bir değer değil, bir dizge (string) kodlar. `000123`'ün başındaki üç adet sıfır optik alanda ayrı semboller olarak basılır ve bağımsız okuyucu tarafından 6 karakter olarak deşifre edilir. Sayısal aritmetikteki önemsiz sıfır kuralı barkodda geçerli değildir.

---

### 4. Üç Görünüm Deney Kaydı ve Ekranda Metin Gösterme Kanıtı

`HELP 2031` barkodu üzerinde üç farklı optik görünüm sınandı:
| Görünüm | Piksel Boyutu | Deneme Sayısı | Başarılı Okuma | Başarı Oranı | Durum |
|:---|:---:|:---:|:---:|:---:|:---|
| **1. Özgün** | $350 \times 280$ | 5 | 5 | \%100 | Başarılı (Net optik kontrast ve standart sessiz alan) |
| **2. Küçültülmüş (1/4)** | $87 \times 70$ | 5 | 0 | \%0 | Başarısız (Piksel bulanıklığı çubukları ayırt edilemez kıldı) |
| **3. Daraltılmış Sessiz Alan** | $358 \times 288$ | 5 | 5 | \%100 / Sınırlı | Çerçeve kontrastına bağlı kritik sınır |

#### Üreticinin Metni Ekranda Göstermesi Neden Bağımsız Okuma Kanıtı Değildir?
Barkod üreten yazılımlar genellikle üretilen görselin alt kısmına metni (insan tarafından okunabilir metin / human readable text) basarlar. Bu metin, kullanıcının girdiği dize parametresinin standart bir sistem yazı tipiyle ekrana yazdırılmasından ibarettir; optik çubukların bir kamera veya tarayıcı algoritmasıyla taranıp deşifre edilmesiyle üretilmez.

Barkod çubuklarında bir baskı hatası, çözünürlük kaybı, sessiz alan ihlali veya piksel bozulması olsa bile alttaki metin kusursuz görünmeye devam eder. Bu nedenle bağımsız bir optik okuyucu (farklı bir algoritma ve kütüphane olan `pyzbar`) ile piksel deseni taranıp çözülmedikçe optik kodlamanın çalıştığı kanıtlanmış sayılamaz.
