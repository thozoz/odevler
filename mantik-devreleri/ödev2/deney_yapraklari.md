# MARMARA ÜNİVERSİTESİ
## Teknoloji Fakültesi / Bilgisayar Mühendisliği Bölümü
### MANTIK DEVRELERİ — Ders 3 / İkili Aritmetik

---

## Deney Yaprağı 1: Elde adımlarını gösteren ikili toplayıcı

**Ad Soyad:** ............................................................ **Öğrenci No:** .............................  
**Tarih:** ....................... **Şube / Grup:** ...................... **İmza:** ......................  

- **Amaç:** Toplama algoritmasını bit düzeyinde tasarlamak ve son eldenin sayısal anlamını doğrulamak.
- **Tanım:** Girdiler aynı uzunlukta iki işaretsiz ikili sayı ve 0 ya da 1 olan başlangıç eldesidir. Çıktılar $n$ bitlik toplam, son elde ve her sütunun işlem kaydıdır. Önce $n = 4$ için çalışınız.

### Yapılacak İşlemler
1. İki bit ve gelen elde için sekiz olasılığın sonuç/elde tablosunu hazırlayın. Sağdan sola çalışan bit düzeyindeki algoritmayı kodlayın; ağırlık, girdi bitleri, gelen elde, sonuç biti ve çıkan elde kaydedilsin.
2. Başlangıç eldesi 0 iken `0101 + 0011` ve `1111 + 0001`; elde 1 iken `1111 + 0000` ve `1111 + 1111` işlemlerini yapın. Beklenen sonuçları programdan önce yazın.
3. Dört bitlik bütün operand çiftlerini iki başlangıç eldesiyle sınayın: toplam 512 test. $n$ bitlik çıktı ile son eldenin birlikte taşıdığı değeri onlu referans toplamla karşılaştırın; referansta hazır aritmetik serbesttir.
4. Boş girdi, geçersiz bit ve farklı uzunluk için ret kuralları ve birer test verin. Son eldeyi yok saymanın kaybettirdiği değeri $n$ cinsinden açıklayıp sınır örneği gösterin.

### Teslim
Sütun tablosu ve kod, dört işlem kaydı, 512 test özeti ve son elde gerekçesi.

### Kısa Cevap ve Doğrulama Notları
- **İlk tahminim:** ................................................................................................
- **Bağımsız kontrolüm:** ..........................................................................................
- **Karşı örneğim:** ...............................................................................................
- **YZ önerisini değerlendirmem veya kullanmadım beyanım:** ........................................................

> **Not:** Kod ve ayrıntılı hesapları yaprak numarasını belirterek ek dosyada veriniz. YZ desteği kullanıldıysa bir önerinin nasıl doğrulandığını veya düzeltildiğini açıklayınız.  
> **Değerlendirme:** Doğruluk 25, Gerekçe 25, Doğrulama 20, Bireysel Açıklama 20, Düzen 10 puan.  
> *Mantık Devreleri Laboratuvarı / Deney yaprağı 1 / 4*

---

## Deney Yaprağı 2: Borç alma ve 2 tümleyeniyle çıkarma

**Ad Soyad:** ............................................................ **Öğrenci No:** .............................  
**Tarih:** ....................... **Şube / Grup:** ...................... **İmza:** ......................  

- **Amaç:** Aynı farkı iki bağımsız algoritmayla bulmak ve negatif sonuçları büyüklükleriyle açıklamak.
- **Tanım:** $M$ ve $N$ dört bitlik işaretsiz büyüklüklerdir. $M - N$ sonucu matematiksel eksi işareti ve dört bitlik büyüklük olarak verilecektir. Operandların en soldaki bitini işaret biti olarak yorumlamayınız.

### Yapılacak İşlemler
1. Borç alarak doğrudan çıkarma ve 2 tümleyeniyle çıkarma için ayrı bit düzeyi fonksiyonlar yazın. Biri diğerini çağırarak sonucu üretmesin. Negatif sonucu eksi işareti ve büyüklükle verin; sıfır durumunu ayrıca ele alın.
2. `1110 − 0011`, `0011 − 1110`, `1000 − 0001`, `0101 − 0101` ve `0011 − 0000` işlemlerini iki yöntemle çözün. Borç zincirlerini ve son eldeyi ara kayıtlarda gösterin.
3. 0–15 aralığındaki bütün 256 operand çiftini onlu referans farkla karşılaştırın. Uyumsuzluk varsa ilk hatalı çifti, ara adımları ve düzeltmeyi kaydedin.
4. “Son elde yoksa sonuç mutlaka negatiftir” iddiasını $N = 0$ ile sınayın. En küçük karşı örneği verin; sıfırın sabit genişlikte 2 tümleyeni ve sonuç karar kuralını açıklayın.

### Teslim
İki algoritma, beş işlemin ara kayıtları, 256 test özeti ve sıfır girdisine karşı örnek.

### Kısa Cevap ve Doğrulama Notları
- **İlk tahminim:** ................................................................................................
- **Bağımsız kontrolüm:** ..........................................................................................
- **Karşı örneğim:** ...............................................................................................
- **YZ önerisini değerlendirmem veya kullanmadım beyanım:** ........................................................

> **Not:** Kod ve ayrıntılı hesapları yaprak numarasını belirterek ek dosyada veriniz. YZ desteği kullanıldıysa bir önerinin nasıl doğrulandığını veya düzeltildiğini açıklayınız.  
> **Değerlendirme:** Doğruluk 25, Gerekçe 25, Doğrulama 20, Bireysel Açıklama 20, Düzen 10 puan.  
> *Mantık Devreleri Laboratuvarı / Deney yaprağı 2 / 4*

---

## Deney Yaprağı 3: Kısmi çarpımlarla ikili çarpıcı

**Ad Soyad:** ............................................................ **Öğrenci No:** .............................  
**Tarih:** ....................... **Şube / Grup:** ...................... **İmza:** ......................  

- **Amaç:** Bit konumuna göre kaydırma tasarlamak ve ara çarpımların toplamını doğrulamak.
- **Tanım:** Çarpılan sayı $n$ bit, çarpan $m$ bit uzunluğunda işaretsiz tam sayılardır. Çıktı $n + m$ bit olarak tutulacaktır. Çarpan bitleri en sağdan 0 ile numaralandırılır. Başlangıç sıfırlarını ara satırlarda koruyunuz.

### Yapılacak İşlemler
1. $i$ konumundaki çarpan biti için kısmi çarpımı ve sola kaydırma kuralını yazın. Kısmi çarpımları bit düzeyindeki toplamayla birleştiren çarpıcıyı kodlayın; ana sonucu hazır çarpma veya tam sayıya dönüşümle üretmeyin.
2. `1011 × 101`, `10111 × 110` ve `11001 × 1010` için $n + m$ bitlik hizalı kısmi çarpımları ve onlu katkılarını tabloya kaydedin; sonucu bağımsız hesapla denetleyin.
3. Sıfır, bir, ikinin kuvveti ve tüm bitleri 1 olan çarpanları içeren en az sekiz test hazırlayın. Sıfır kısmi çarpımları atlayan ikinci sürümle sonuçları ve toplama çağrılarını karşılaştırın; sayım kuralını belirtin.
4. $n + m$ bitin çarpım için yeterliliğini üst sınırla gerekçelendirin. $n + m - 1$ bitin her zaman yetmediğini küçük bir karşı örnekle gösterin.

### Teslim
Üç kısmi çarpım tablosu, iki sürümün kodu, sekiz test ve çıktı genişliği gerekçesi.

### Kısa Cevap ve Doğrulama Notları
- **İlk tahminim:** ................................................................................................
- **Bağımsız kontrolüm:** ..........................................................................................
- **Karşı örneğim:** ...............................................................................................
- **YZ önerisini değerlendirmem veya kullanmadım beyanım:** ........................................................

> **Not:** Kod ve ayrıntılı hesapları yaprak numarasını belirterek ek dosyada veriniz. YZ desteği kullanıldıysa bir önerinin nasıl doğrulandığını veya düzeltildiğini açıklayınız.  
> **Değerlendirme:** Doğruluk 25, Gerekçe 25, Doğrulama 20, Bireysel Açıklama 20, Düzen 10 puan.  
> *Mantık Devreleri Laboratuvarı / Deney yaprağı 3 / 4*

---

## Deney Yaprağı 4: Bölüm kalan ve kesirli bölme algoritması

**Ad Soyad:** ............................................................ **Öğrenci No:** .............................  
**Tarih:** ....................... **Şube / Grup:** ...................... **İmza:** ......................  

- **Amaç:** Bölmenin durma koşulunu tasarlamak ve kalan üzerinden kesirli hesaba devam etmek.
- **Tanım:** Girdiler işaretsiz ikili tam sayı $D$ ve sıfırdan farklı bölen $d$'dir. Önce tam bölüm $Q$ ve kalan $R$ bulunacak, istenirse en fazla sekiz ikili kesir basamağı üretilecektir. Kesirli hesap erken tamamlanırsa ek sıfır üretmek zorunlu değildir.

### Yapılacak İşlemler
1. Bitleri soldan sağa işleyen bölme algoritmasını kodlayın. Her adımda incelenen parça, bölüm biti ve kalan kaydedilsin. Ana hesapta hazır bölme/kalan operatörü kullanmayın; sıfır böleni açık hata olarak reddedin.
2. `10110 ÷ 100`, `1101 ÷ 10` ve `111 ÷ 11` için tam bölüm $Q$ ile kalan $R$'yi bulun. $D = Q \times d + R$ ve $0 \le R < d$ koşullarını ayrı doğrulayın; ikisinin birlikte neden gerekli olduğunu açıklayın.
3. Kalan sıfır değilse en çok sekiz ikili kesir basamağı üretin. Tamamlanmış sonuçta $=$, kesilmiş sonuçta $\approx$ kullanın; tekrar eden kalanları kaydedin. `111 ÷ 11` üzerinden tam ve kesirli bölmenin durma koşullarını ayırın.
4. Sıfır bölünen, bölünenden büyük bölen ve eşit operandlarla sınama yapın. Beklenen ve gözlenen sonuçları karşılaştırıp bölümde sıfır bitinin yanlış atılmasını yakalayan bir örnek gösterin.

### Teslim
Algoritma ve kod, üç işlem kaydı, bölüm/kalan kontrolleri, kesirli sonuçlar ve sınır testleri.

### Kısa Cevap ve Doğrulama Notları
- **İlk tahminim:** ................................................................................................
- **Bağımsız kontrolüm:** ..........................................................................................
- **Karşı örneğim:** ...............................................................................................
- **YZ önerisini değerlendirmem veya kullanmadım beyanım:** ........................................................

> **Not:** Kod ve ayrıntılı hesapları yaprak numarasını belirterek ek dosyada veriniz. YZ desteği kullanıldıysa bir önerinin nasıl doğrulandığını veya düzeltildiğini açıklayınız.  
> **Değerlendirme:** Doğruluk 25, Gerekçe 25, Doğrulama 20, Bireysel Açıklama 20, Düzen 10 puan.  
> *Mantık Devreleri Laboratuvarı / Deney yaprağı 4 / 4*
