# BLM2007 Mantık Devreleri - Deney Yaprakları (Ödev 1)

**Ders:** BLM2007 Mantık Devreleri (Prof. Dr. Ali Buldu)  
**Kapsam:** Ders 2 / Sayı Sistemleri  
**Değerlendirme Kriterleri (Her yaprak için):**
- Doğruluk: 25 Puan
- Gerekçe: 25 Puan
- Doğrulama: 20 Puan
- Bireysel Açıklama: 20 Puan
- Düzen: 10 Puan
- **Toplam:** 100 Puan

---

## Deney Yaprağı 1: Hatalı Girdileri Tanıyan Sayı Sistemi Dönüştürücüsü
- **Amaç:** Tam ve kesirli sayı dönüşümlerini tasarlamak ve bağımsız testlerle doğrulamak.
- **Tanım:** Bir yazılım sayı metnini, kaynak tabanı ve hedef tabanı alacaktır. Tabanlar 2, 8, 10 ve 16; sayılar negatif olmayan değerlerdir. Kesir ayracı noktadır. (Örnek giriş: `101101.01101`, kaynak taban: `2`, hedef taban: `16`).
- **Yapılacak İşlemler:**
  1. Tam ve kesirli kısım için algoritmaları ayrı ayrı açıklayın. Bölme kalanlarının neden ters sırada, kesirli dönüşüm rakamlarının neden işlem sırasıyla yazıldığını basamak ağırlıklarıyla gösterin.
  2. Geçersiz rakamları, boş girdiyi ve birden çok kesir ayracını reddeden bir giriş kontrolü geliştirin. Örneğin tabanı 2 olan `102` ve tabanı 8 olan `128` reddedilmelidir.
  3. Kesirli dönüşüm sekiz hedef basamakta tamamlanmazsa kesin ve sonucun yaklaşık olduğunu belirtin. Tamamlanan dönüşümlerde kesinlik bilgisini gösterin.
  4. Algoritmayı kodlayın. Ana dönüşüm işlemini hazır taban dönüştürme fonksiyonlarına yaptırmayın.
  5. Beklenen sonuçlarını önceden hesapladığınız en az sekiz test hazırlayın. Sıfır, yalnızca kesirli sayı, başında sıfır bulunan sayı ve hatalı girdiler bulunsun. En az bir sonucu basamak ağırlıklarıyla denetleyin.
- **Düşünme Sorusu:** Başka tabana dönüşümden sonra başlangıç tabanına dönünce aynı değeri bulmak doğruluğu kanıtlar mı? İki yönde aynı hatayı yapan bir program üzerinden tartışın.
- **Teslim:** Algoritma, kod, beklenen ve gerçekleşen sonuçları içeren test tablosu ve bağımsız kontrol hesabı.

---

## Deney Yaprağı 2: Sınırlı Bit Sayısıyla Ölçüm Gösterimi Tasarımı
- **Amaç:** Aralık ve adım büyüklüğüne uygun en küçük ikili gösterimi gerekçelendirmek.
- **Tanım:** Bir cihaz, 0 ve 1000 dahil bu aralıktaki değerleri 0.125 adımlarla gösterecektir. İkili noktanın yeri sabittir. İşaret biti yoktur. Nokta ayraçtır ve bit sayısına katılmaz.
- **Yapılacak İşlemler:**
  1. Kesirli kısım için gereken en az bit sayısını basamak ağırlıklarından yararlanarak belirleyin.
  2. Tam kısım için gereken en az bit sayısını ve toplam bit sayısını bulun.
  3. Toplam 12 bit yeterli midir? Temsil edilebilen en büyük değer ve farklı gösterimlerin sayısı olmak üzere iki yöntemle inceleyin.
  4. Yeterli olan en küçük gösterimi tasarlayın. Tam ve kesirli kısımların bit sayılarını belirtin.
  5. 0, 0.125, 173.625 ve 1000 değerlerini aynı sabit bit uzunluğunda yazın. Baştaki ve sondaki gerekli sıfırları koruyun.
  6. 173.625 değerini sekizli ve onaltılı sistemlerde yazın. Üç gösterimin aynı değeri verdiğini doğrulayın.
- **Düşünme Sorusu:** Adım büyüklüğü 0.1 olsaydı, bütün değerleri sonlu sayıda ikili kesir basamağıyla tam olarak gösterebilir miydiniz? Yanıtınızı basamak ağırlıklarıyla gerekçelendirin.
- **Teslim:** Gösterim biçimi, iki yeterlilik hesabı, istenen değerlerin dönüşümleri ve sınır değer kontrolü.

---

## Deney Yaprağı 3: Sıfır Ekleme ve Basamak Değerinin Korunması
- **Amaç:** Gruplandırma sırasında eklenen sıfırların sayısal etkisini açıklamak.
- **Tanım:** İncelenecek sayı: $(101101.01101)_2$. Sayıyı sekizli ve onaltılı sistemlere dönüştürünüz.
- **Yapılacak İşlemler:**
  1. Üçlü ve dörtlü grupları ikili noktadan başlayarak oluşturun. Eklediğiniz sıfırları açıkça işaretleyin.
  2. Tam kısmın soluna ve kesirli kısmın sağına eklenen sıfırların neden değeri değiştirmediğini basamak ağırlıklarıyla açıklayın.
  3. Kesirli kısmı dörtlü gruplara ayırmak için `01101` yerine `00001101` yazan bir öğrencinin bulacağı onaltılı ve onluk değeri hesaplayın.
  4. "Eksik gruplar her zaman sola sıfır eklenerek tamamlanır" iddiasını bir karşı örnekle çürütün.
  5. Doğru ikili, sekizli ve onaltılı gösterimleri ayrı ayrı onluya çevirerek eşitliklerini doğrulayın.
- **Düşünme Sorusu:** `00101.100` ve `101.1` ikili gösterimleri aynı değeri mi taşır? Değerlerinin eşit olması, gösterimlerinde aynı sayıda bit bulunduğu anlamına gelir mi?
- **Teslim:** Doğru ve hatalı gruplandırmalar, sayısal karşılıkları ve sıfır ekleme kuralının gerekçesi.

---

## Deney Yaprağı 4: Kesirli Dönüşümde Kesinlik ve Yaklaşım Hatası
- **Amaç:** Sonlu gösterim, kesme ve yuvarlama arasındaki farkı sayısal olarak incelemek.
- **Tanım:** İncelenecek onluk kesirler: `0.625`, `0.1`, `0.65` ve `0.975`. Hesaplamalarda kesirli kısım için sekiz ikili basamak kullanınız.
- **Yapılacak İşlemler:**
  1. Her sayıyı ikili sisteme dönüştürün. İşlem tamamlanmazsa ilk sekiz kesir basamağında durun. Tamamlanan gösterimleri gerekirse sağdan sıfırlarla tamamlayın.
  2. Kesilmiş her gösterimi tekrar onluya çevirin ve mutlak hatayı hesaplayın.
  3. Her sayıyı en yakın sekiz basamaklı ikili değere yuvarlayın. Eşit uzaklıkta büyük olanı seçin. Yuvarlanmış değerin mutlak hatasını da bulun.
  4. Kesme ve yuvarlama sonuçlarını bir tabloda karşılaştırın. Hangi dönüşümlerde $=$, hangilerinde $\approx$ kullanılması gerektiğini belirtin.
  5. Sonlu bir ikili kesrin neden bir tam sayının 2'nin bir kuvvetine bölümü olarak yazılabildiğini gösterin. Bu bilgiyle hangi sayıların sonlu ikili gösterime sahip olduğunu açıklayın.
- **Düşünme Sorusu:** Sekiz ikili kesir basamağı ile sekiz onaltılı kesir basamağı aynı hassasiyeti sağlar mı? Son basamağın ağırlığını kullanarak karşılaştırın.
- **Teslim:** Dönüşüm adımları; kesilmiş ve yuvarlanmış değerler ile mutlak hataları içeren tablo; kesinlik açıklaması.

---

## Deney Yaprağı 5: Bir Çözümdeki Hatanın Kaynağını Bulma
- **Amaç:** Sunulan çözümü hesapla denetlemek ve yanlış iddiayı düzeltmek.
- **Tanım:** Bir öğrenci veya YZ aracı aşağıdaki raporu üretmiştir. Her iddiayı bağımsız olarak denetleyiniz:
  - **İddia A:** $(0.65)_{10} = (0.101)_2$
  - **İddia B:** $(0.975)_{10} = (0.F99)_{16}$
  - **İddia C:** $(101101.01101)_2 = (2D.0D)_{16}$
  - **İddia D:** Bir ikili tam sayının sağına sıfır eklemek değerini değiştirmez.
- **Yapılacak İşlemler:**
  1. İddiaları değerlendirin. Tam eşitlik olan ifade ile yalnızca yaklaşık değer veren ifadeyi ayırt edin.
  2. A ve B'nin sağ taraflarındaki gösterimlerin gerçek onluk değerlerini ve sol tarafla aralarındaki mutlak hataları hesaplayın.
  3. C'de hatalı sıfır tamamlamanın nerede yapıldığını gösterin ve doğru sonucu bulun.
  4. D için sıfırdan farklı bir karşı örnek verin. Sağa sıfır eklemenin genel etkisini yazın.
  5. Dört iddiayı doğru ve açık ifadelerle yeniden yazın. Yaklaşık sonuçlarda $\approx$ işaretini kullanın.
- **Düşünme Sorusu:** İşlem adımları doğru görünürken sonuç ifadesi yine de yanlış olabilir mi? A veya B üzerinden açıklayın.
- **Teslim:** Her iddia için kontrol hesabı, hata teşhisi ve düzeltilmiş ifade.

---

## Deney Yaprağı 6: Taban Bilgisi Kaybolmuş Kayıtların Çözümlenmesi
- **Amaç:** Olası tabanları elemek, ortak değeri bulmak ve belirsizliği açıklamak.
- **Tanım:** Üç cihaz aynı negatif olmayan tam sayıyı kaydetmiştir. Her cihaz 2, 8, 10 veya 16 tabanlarından birini kullanmıştır. Tabanlar birbirinden farklı olabilir; taban bilgileri kaybolmuştur.
  - Cihaz A: `17`
  - Cihaz B: `21`
  - Cihaz C: `10001`
- **Yapılacak İşlemler:**
  1. Her kayıt için rakamların geçerli olduğu bütün kaynak tabanlarını belirleyin.
  2. Her geçerli yorumun onluk karşılığını hesaplayın ve bir tabloda gösterin.
  3. Üç kaydın aynı sayıyı göstermesi koşuluyla ortak değeri ve cihazların tabanlarını bulun.
  4. Başka bir çözüm bulunup bulunmadığını bütün geçerli yorumları karşılaştırarak gösterin.
  5. Üç kayıt da `10` olsaydı tabanları tek bir şekilde belirleyebilir miydiniz? Olası yorumlarla gerekçelendirin.
  6. Taban belirsizliğini önlemek için sayı ve tabanı birlikte taşıyan açık bir kayıt biçimi tasarlayın. Üç örnek kayıt yazın.
- **Düşünme Sorusu:** Bir kaydın bütün rakamlarının belirli bir tabanda geçerli olması, kaydın gerçekten o tabanda yazıldığını kanıtlar mı?
- **Teslim:** Geçerli yorumlar tablosu, ortak çözüm ve tekliğine ilişkin gerekçe, önerilen kayıt biçimi.

---

## Deney Yaprağı 7: Tek Bit Değişiminin Sayısal Etkisi
- **Amaç:** Bit konumu ile hata büyüklüğünü ilişkilendirmek ve aralık kontrolünü sınamak.
- **Tanım:** Bir cihazda $(173)_{10}$ değeri sekiz bitlik işaretsiz ikili gösterimle tutulmaktadır. Her hata denemesi başlangıç değerinden yapılır ve yalnızca bir bit tersine döner. Geçerli değer aralığı $0 - 200$'dür.
- **Yapılacak İşlemler:**
  1. Başlangıç değerini sekiz bit ile yazın. MSB ve LSB'yi işaretleyin. Bit konumlarını LSB için 0, MSB için 7 olacak şekilde numaralandırın.
  2. Sekiz bitin her birini ayrı ayrı tersine çevirin. Oluşan ikili ve onluk değerleri bulun.
  3. Her deneme için değişimin yönünü ve mutlak hata büyüklüğünü belirleyin. Sonuçları bir tabloda gösterin.
  4. "MSB'deki hata her zaman sayıyı artırır" iddiasını başlangıç değeri üzerinden değerlendirin.
  5. Yalnızca 0-200 aralık kontrolünün hangi hataları yakalayacağını belirleyin. Aralıkta kalan hatalı bir değeri örnek gösterin.
  6. Başlangıç değerini ve sekiz hatalı değeri onaltılı sisteme çevirerek karşılaştırın.
- **Düşünme Sorusu:** "Tek bir bit değiştiği için sayısal hata küçüktür" ifadesi neden güvenilir değildir? Bit konumu ile hata büyüklüğü arasındaki genel ilişkiyi yazın.
- **Teslim:** Sekiz denemeyi içeren tablo, aralık kontrolünün sonuçları ve genel hata ilişkisi.
