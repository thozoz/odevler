# BLM2007 Mantık Devreleri Laboratuvarı — Ödev 3 Toplu Çözüm Raporu
### Ders 5 / Kodlama (Deney Yaprakları 1–4)

**Öğrenci Adı Soyadı:** Efe Özan  
**Öğrenci No:** 170425062  
**Bölüm:** Bilgisayar Mühendisliği  
**Ders:** BLM2007 Mantık Devreleri (Prof. Dr. Ali Buldu)  
**Tarih:** 10 Kasım 2026  
**Şube / Grup:** Ali Buldu A Grubu  

> **Kod Dosyaları:**
> - `rakam_donusturucu.py` ve `dogrulama_1.py` (Deney Yaprağı 1)
> - `gray_donusturucu.py` ve `dogrulama_2.py` (Deney Yaprağı 2)
> - `bes_bit_ve_eslik.py` ve `dogrulama_3.py` (Deney Yaprağı 3)
> - `karakter_ve_barkod.py` ve `dogrulama_4.py` (Deney Yaprağı 4)

---

# DENEY YAPRAĞI 1 ÇÖZÜMÜ
### BCD Artı 3 ve Aiken için Rakam Dönüştürücüsü

- **Amaç:** Rakam kodlarını ayırmak, geçersiz sözcükleri reddetmek ve 9 tümleyenini doğrulamak.
- **Tanım:** Kod türü seçilebilen bir rakam dönüştürücüsü tasarlayınız. 8421 BCD, Artı-3 ve standart Aiken 2421 ders tablolarını kullanınız. Her rakam dört bit olacak; baştaki sıfırlar korunacaktır.

### 1. Kodlayıcı ve Çözümleyici Mimarisi
Algoritma `rakam_donusturucu.py` içinde modüler olarak tasarlandı.
- **8421 BCD:** Doğrudan ikili ağırlıklar ($8, 4, 2, 1$).
- **Artı-3 (Excess-3):** Rakamın değerine $3$ eklenerek oluşturulur ($d+3$).
- **Standart Aiken 2421:** Kendinden tümleyen (self-complementing) standart sözlük:
  $0 \to 0000, 1 \to 0001, 2 \to 0010, 3 \to 0011, 4 \to 0100,$  
  $5 \to 1011, 6 \to 1100, 7 \to 1101, 8 \to 1110, 9 \to 1111.$

**Giriş Denetimi:**
Boş girdi (`""`), rakam dışı karakterler (`"12a"`), 4'ün katı olmayan bit dizileri ve sözlük dışı 4 bitlik kodlar gerekçeli hata fırlatarak (`ValueError`) reddedilir.

### 2. Zorunlu Dönüşümler ve 263 Sayısı Analizi
- **48 ve 003 Testleri:**
  - `48`: BCD = `0100 1000`, Artı-3 = `0111 1011`, Aiken = `0100 1110`.
  - `003`: BCD = `0000 0000 0011`, Artı-3 = `0011 0011 0110`, Aiken = `0000 0000 0011`. Baştaki sıfırlar aynen korunur.
- **263 Sayısının Saf İkili vs BCD Gösterimi:**
  - Saf İkili: $263 = 256 + 4 + 2 + 1 = \mathbf{100000111_2}$ (**9 bit**).
  - BCD: $2\to 0010, 6\to 0110, 3\to 0011 \implies \mathbf{001001100011_{BCD}}$ (**12 bit**). BCD $\%33.3$ daha fazla bit harcar.
  - Yanlış Kodla Okunması: 12 bitlik BCD deseni saf ikili olarak okunursa:
    $$2^9 + 2^6 + 2^5 + 2^1 + 2^0 = 512 + 64 + 32 + 2 + 1 = \mathbf{611_{10}}$$
    olarak tamamen yanlış anlaşılır.

### 3. 16 Desen Geçerlilik Kümeleri ve Aiken 0101 vs 1011
- **BCD (8421):** 10 geçerli (`0000`--`1001`), 6 geçersiz (`1010`--`1111`).
- **Artı-3:** 10 geçerli (`0011`--`1100`), 6 geçersiz (`0000`--`0010` ve `1101`--`1111`).
- **Standart Aiken (2421):** 10 geçerli (`0000, 0001, 0010, 0011, 0100, 1011, 1100, 1101, 1110, 1111`), 6 geçersiz (`0101, 0110, 0111, 1000, 1001, 1010`).

**Aiken 0101 ve 1011 Ağırlıklı Toplam Kıyaslaması:**
$2421$ ağırlıklarıyla:
- `0101` $\to 0\cdot 2 + 1\cdot 4 + 0\cdot 2 + 1\cdot 1 = 5$
- `1011` $\to 1\cdot 2 + 0\cdot 4 + 1\cdot 2 + 1\cdot 1 = 5$
İkisinin de ağırlıklı toplamı 5 olmasına rağmen, standart Aiken'de kendinden tümleyen (self-complementing) kuralı gereği 5 rakamı 4'ün (`0100`) 1 tümleyeni olan `1011` olarak sabitlenmiştir. `0101` sözlük dışıdır. Bu durum ağırlıklı toplamın tek başına geçerlilik kanıtı olmadığını gösterir.

### 4. 9 Tümleyeni ve BCD Karşı Örneği
- **Artı-3:** $15 - (d + 3) = 12 - d = (9 - d) + 3 \implies 9 - d$'nin kodudur (**10/10 doğrulandı**).
- **Aiken:** Simetrik yapı gereği bitler terslendiğinde doğrudan $9 - d$'nin koduna eşittir (**10/10 doğrulandı**).
- **BCD Karşı Örneği:** BCD kendinden tümleyen değildir (0/10). $d=2$ için BCD = `0010`, tersi `1101` ($13_{10}$) geçersizdir; $9-2=7$'nin BCD'si ise `0111`'dir.

---

# DENEY YAPRAĞI 2 ÇÖZÜMÜ
### Gray Dönüştürücüsü ve Komşuluk Denetimi

- **Amaç:** İki yönlü Gray dönüşümünü ve komşuluk sınırını bağımsız kontrollerle incelemek.

### 1. XOR Tabanlı Dönüşüm Algoritmaları
- **İkili $\rightarrow$ Gray:** $g_{n-1} = b_{n-1}$, $g_i = b_{i+1} \oplus b_i$.
- **Gray $\rightarrow$ İkili:** $b_{n-1} = g_{n-1}$, $b_i = b_{i+1} \oplus g_i$ (önceki hesaplanan ikili bit $b_{i+1}$ kullanılır).

### 2. 0--15 Tablosu ve Kapanışlar
0--15 arasındaki tüm 15 ardışık geçişte bit farkı (Hamming mesafesi) tam 1'dir.
- **15 $\rightarrow$ 0 Kapanışı:** $\text{Gray}(15) = 1000 \to \text{Gray}(0) = 0000$ (fark: **1 bit**, dairesel kod).
- **9 $\rightarrow$ 0 Kapanışı (0--9 kesilmiş dizi):** $\text{Gray}(9) = 1101 \to \text{Gray}(0) = 0000$ (fark: **3 bit**; 0., 2. ve 3. bitler). Dizi kesildiğinde komşuluk kapanışı bozulur.

### 3. Uzun Bit Dizileri
- `101110101` (9 bit) $\to$ Gray: `111001111` $\to$ Geri: `101110101`.
- `1000101` (7 bit) $\to$ Gray: `1100111` $\to$ Geri: `1000101`. Bit uzunlukları korunur.

### 4. Hatalı Ters Yöntem ve Karşı Örnek
Ters yönde $b_i = g_{i+1} \oplus g_i$ kullanan hatalı yöntem:
- **Karşı Örnek (\texttt{1100}):** Onlu 8'in Gray'i `1100`'dır. Doğru ikili `1000` iken, hatalı yöntem 1. basamakta ($2^1$) ayrılarak `1010` (10) üretir.
- **Rastgele Gray Sözcükleri:** Yalnız ardışık sayılarda tek bit farkı garanti edilir. Rastgele iki sözcük arasında (örn. 0 ile 2 arasında 2 bit, 0 ile 10 arasında 4 bit) çoklu bit farkları bulunabilir.

---

# DENEY YAPRAĞI 3 ÇÖZÜMÜ
### Beş Bitte İki Bir ve Eşlik Denetimi

- **Amaç:** İki hata denetim kuralını kurmak ve saptama ile düzeltmenin sınırını açıklamak.

### 1. Denetleyiciler ve 11000 Özel Ataması
- **11000 Özel Sıfır Ataması Gerekçesi:** 7-4-2-1-0 ağırlıklarıyla 0 normalde `00000` (sıfır adet 1) verir. Ancak kodun güvenlik koşulu tam iki adet 1 içermesidir. Ağırlık toplamı 11 olan `11000` hiçbir tekil onlu rakamla çakışmaz; invariantı korumak için 0'a `11000` atanmıştır.
- **Eşlik Paketleri:** 7 veri biti + $p$ eşlik biti = 8 bit.

### 2. 5'te 2 Hata Taramaları (50 ve 100 Deney)
- **50 Tek Bit Hatası:** **50/50'si saptandı (\%100)**. 1 sayısı 1 veya 3'e dönüştü.
- **100 İki Bit Hatası:** **40 saptandı**, **60 KAÇTI (\%60)**. Kaçan hatalarda bir 1 ve bir 0 yer değiştirerek 1 sayısı 2 kaldı ve başka bir geçerli rakama dönüştü (Örn: Rakam 0 `11000`, 0. ve 2. bitler terslenirse `01100` = Rakam 6 olur).

### 3. Eşlik Paketleri ve Hata Taramaları
- `1000011` (3 adet 1) $\to$ Çift eşlik: `11000011` ($p=1$), Tek eşlik: `01000011` ($p=0$).
- `1000001` (2 adet 1) $\to$ Çift eşlik: `01000001` ($p=0$), Tek eşlik: `11000001` ($p=1$).
- `11000011` çift eşlikli paketinde:
  - 8 tek bit hatası: **8/8 saptandı**.
  - 28 iki bit hatası: **0/28 saptandı (28/28 KAÇTI)**.
- **Tek/Çift Tersleme Kuralı:** Tek sayıda bit hatası pariteyi değiştirir (daima saptanır); çift sayıda bit hatası pariteyi korur (daima kaçar).

### 4. Düzeltme Sınırı ve 01000 Analizi
Geçersiz `01000` deseni için olası özgün geçerli sözcükler: `11000` (0), `01100` (6), `01010` (5) ve `01001` (4)'dir (4 aday). Hatanın yeri bilinemez.
- Yalnız $p$ terslenirse veri bitleri sağlam olduğu halde eşlik hatası alarmı verilir.
- Hata saptama, hatanın yerini bulma ve veri bütünlüğü kavramsal olarak birbirinden bağımsızdır.

---

# DENEY YAPRAĞI 4 ÇÖZÜMÜ
### Karakter Kodları ve Barkodun Bağımsız Doğrulanması

- **Amaç:** ASCII ve EBCDIC’i ayırmak ve optik gösterimin doğru okunmasını bağımsız doğrulamak.

### 1. Karakter Kodlayıcı/Çözümleyici ve H Karakteri Ağırlık Denetimi
- `HELP 2031` metni:
  - ASCII: `48 45 4C 50 20 32 30 33 31`
  - EBCDIC: `C8 C5 D3 D7 40 F2 F0 F3 F1`
- **H Karakteri Bit Ağırlıkları:**
  - ASCII H: $48_{16} = 4\cdot 16 + 8 = 72_{10}$; $01001000_2 = 2^6 + 2^3 = 72_{10}$.
  - EBCDIC H: $C8_{16} = 12\cdot 16 + 8 = 200_{10}$; $11001000_2 = 2^7 + 2^6 + 2^3 = 200_{10}$.

### 2. Çapraz Çözüm ve Üst Bit Yetersizliği
- `48 45 4C 50` EBCDIC ile ve `C8 C5 D3 D7` ASCII ile çözülemez (reddedilir).
- **Üst Bit (MSB) Yöntemi Neden Yetmez?** L karakterinde ASCII `4C` iken EBCDIC `D3`'tür; MSB 1 yapılırsa `CC` olur ($CC \ne D3$). 0 rakamında ASCII `30` iken EBCDIC `F0`'dır ($B0 \ne F0$). ASCII ve EBCDIC farklı bölge yapılarına sahiptir; dönüşüm birebir tablo eşlemesi gerektirir.

### 3. Code 128 Üretimi ve Bağımsız Okuma
Üretici: `python-barcode` | Okuyucu: `pyzbar` (libzbar)
- `HELP 2031` (9 karakter), `HELP2031` (8 karakter), `000123` (6 karakter) ve `123` (3 karakter) bağımsız okuyucuyla karakter karakter birebir doğrulandı.
- Boşluk optik bir çubuk sembolü olarak taşınır.
- Başlangıç sıfırları metin tabanlı optik kodlama sayesinde korunur.

### 4. Üç Görünüm Deney Kaydı ve Ekranda Metin Gösterme Kanıtı
- **1. Özgün ($350\times 280$ px):** 5/5 (\%100 başarı).
- **2. Küçültülmüş ($87\times 70$ px):** 0/5 (\%0 başarı, piksel bulanıklığı).
- **3. Daraltılmış Sessiz Alan ($358\times 288$ px):** Çerçeve kontrastına bağlı kritik sınır.
- **Ekranda Metin Gösterme Kanıtı:** Üretici yazılımlar görselin altına girdi metnini standart sistem yazı tipiyle çizer; optik çubukların taranmasıyla elde edilmez. Bağımsız bir optik okuyucuyla (`pyzbar`) taranmadıkça kodlamanın çalıştığı kanıtlanamaz.
