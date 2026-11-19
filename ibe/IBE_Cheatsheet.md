# İBE Cheatsheet

> BLM2003 İnsan Bilgisayar Etkileşimi · Vize: 20 Kasım 2026 Cuma 15:00 · RTE.T4.Z05/Z06/Z07
> Format: yazılı, birkaç kısa soru + bir uzun soru (tasarım değerlendirme)

---

## Konu 1: İBE nedir, kullanılabilirlik nedir?

**İBE'nin derdi tek cümle:** İnsanlar teknolojiyi nasıl kullanıyor, nasıl tasarlarsak rahat ve hatasız kullanırlar?

Bunu yaparken hep **4 şeye** bakarsın:

- **Kullanıcı:** Kim kullanıyor? 20 yaşında bilgisayar mühendisi mi, 70 yaşında teyze mi?
- **Görev:** Ne yapmaya çalışıyor? Para çekmek mi, oy vermek mi?
- **Araç/arayüz:** Neyle yapıyor? ATM, telefon, kâğıt pusula.
- **Bağlam:** Nerede, hangi koşulda? Sakin evde mi, kuyrukta acele içinde mi, savaş gemisinde stres altında mı?

Önemli fikir şu: **"Bu arayüz iyi" diye tek başına bir şey yok.** Bir arayüz genç biri için harika, yaşlı biri için felaket olabilir. Sakin ortamda sorunsuz, stres altında ölümcül olabilir (USS Vincennes tam bu). Sınavda bir tasarımı yorumlarken ilk cümlen hep **"kullanıcı kim, görev ne, ortam ne"** olmalı.

### Kullanılabilirlik (ISO 9241-11)

Belirli kullanıcıların, belirli görevleri, belirli bir bağlamda **etkili, verimli ve memnuniyetle** yapabilmesi.

Üçünü bir örnekle düşün. Bir yemek sipariş uygulaması:

- **Etkililik = işi yapabildin mi?** Doğru yemeği doğru adrese sipariş edebildin mi? Yanlış adrese gittiyse etkililik düşük.
- **Verimlilik = ne kadar uğraştın?** 30 saniyede mi verdin, 12 ekran gezip 5 dakikada mı? İkisinde de sipariş verildi (etkili), ama ikincisi verimsiz.
- **Memnuniyet = nasıl hissettin?** "Ya ne güzel uygulama" mı, yoksa "bir daha açmam" mı?

**Neden üçü ayrı?** Çünkü biri iyi olup diğeri kötü olabilir. Banka uygulaması işi yaptırır (etkili) ama 4 onay, 2 SMS kodu ister (verimsiz) ve sinir eder (memnuniyetsiz).

**"Bu uygulama kullanışlıdır" neden kötü?** Ölçülemez. Kimin için, hangi işte, neye göre? Doğrusu ölçülebilir yazmak:

> "Kullanıcıların %90'ı, eğitimsiz, siparişi 1 dakikada, hatasız veriyor ve 5 üzerinden 4 memnuniyet veriyor."

Bu cümlede üçü de var: hatasız = etkililik, 1 dakika = verimlilik, 4/5 = memnuniyet.

> **Sınavda kullan:** Ödev 2'de hoca "yüzde kaç etkili, verimli, memnun edici" diye sordu. Uzun soruda da büyük ihtimalle bu üçünü ayrı ayrı gerekçelendirmeni isteyecek.

---

## Konu 2: Norman

Norman sınavın kalbi, çünkü tasarım yorumlarken kullanacağın en güçlü araç onun modeli. Bunu iyi anlarsan uzun sorunun yarısı biter.

**Norman'ın temel fikri:** Kullanıcı bir şey yapmak istiyor (hedef). Bunu yapmak için iki engeli aşması gerekiyor. Bu engellere **körfez** diyor.

Bir köprü düşün: bir tarafta **kullanıcının kafası** (ne istediği), diğer tarafta **makine** (ne yapabildiği). Arada iki uçurum var:

### 1. Gerçekleştirme körfezi (kafadan makineye giderken)

Kullanıcının sorusu: **"Bunu nasıl yapacağım? Neye basmalıyım?"**

Örnek: Yeni bir mikrodalgaya bakıyorsun, 15 tuş var, "sadece 1 dakika ısıtmak istiyorum" ama hangi tuş belli değil. İşte bu körfez geniş.

### 2. Değerlendirme körfezi (makineden kafaya dönerken)

Kullanıcının sorusu: **"Ne oldu? İstediğim oldu mu?"**

Örnek: Butona bastın, ekranda hiçbir şey değişmedi. Çalıştı mı, çalışmadı mı, bir daha mı basayım? Bu körfez geniş.

**İyi tasarım = iki körfeze köprü kurmak.** Kullanıcı ne yapacağını görsün, yaptıktan sonra ne olduğunu anlasın.

Florida ve Vincennes'i hatırla, hocanın tanıtım slaytında böyle etiketlenmişti:

- **Florida oy pusulası = gerçekleştirme körfezi.** Seçmen "Gore'a oy vermek için hangi deliği delmeliyim?" sorusunu çözemedi.
- **Vincennes = değerlendirme körfezi.** Mürettebat "bu uçak ne yapıyor, alçalıyor mu yükseliyor mu?" sorusunu ekrandan okuyamadı.

### 7 aşama

Bu iki körfezin adım adım hali:

- **Gerçekleştirme tarafı:** hedef → niyet → hareketi planla → hareketi yap
- **Değerlendirme tarafı:** sonucu algıla → yorumla → hedefle karşılaştır

Ezber ipucu: ilk 4'ü "yapma", son 3'ü "anlama".

### Norman'ın 4 prensibi (köprü kurmanın aletleri)

- **Görülebilirlik:** Ne yapılabileceği gözüküyor mu? (Gizli menü, ikonsuz buton = kötü)
- **Anlamlı eşleştirme (mapping):** Düğme ile etkisi doğal bir ilişkide mi? (Ocaktaki 4 düğme, 4 gözle aynı dizilimde mi? Florida'da değildi.)
- **Kavramsal model:** Kullanıcı sistemin nasıl çalıştığını doğru tahmin edebiliyor mu? (Çöp kutusu metaforu: "sildim ama geri alabilirim" modelini verir.)
- **Geri bildirim:** Yaptığın şeyin sonucu hemen gösteriliyor mu? (Yükleme çubuğu, "gönderildi" tiki)

İlk ikisi daha çok gerçekleştirme körfezine, geri bildirim değerlendirme körfezine köprü kurar. Kavramsal model ikisine birden.

### Hata türleri

- **Kayma (slip):** Ne yapacağını biliyorsun ama elin kayıyor. "Kaydet"e basacaktın, yanındaki "Sil"e bastın. Çözüm kolay: butonları ayır, onay iste.
- **Yanılgı (mistake):** Sistemi yanlış anlamışsın, bilerek yanlış şeyi yapıyorsun. Mesela "X'e basınca kaydeder sanıyordum". Çözüm zor: kullanıcıya doğru kavramsal modeli vermen gerekiyor.

### Çaresizlik

Norman'ın önemli bir sözü daha var: **hata etkileşimin doğal parçasıdır.** Yani kullanıcı hata yaptıysa suç kullanıcıda değil, tasarımda aranır.

- Kullanıcı sürekli başarısız olursa "ben bilgisayardan anlamıyorum" der ve vazgeçer. Buna **öğrenilmiş çaresizlik** denir.
- Dışarıdan "sen yapamazsın" denmesine ise **öğretilmiş çaresizlik** denir.

---

## Konu 3: Shneiderman ve Suchman

### Shneiderman

Norman'ın yanında duran adam. Norman "etkileşim nasıl işler" diye modeller, Shneiderman "arayüzü nasıl daha iyi yaparım" diye **pratik kurallar** verir. Sınavda tasarım yorumlarken en çok bu 8 kuralı kullanacaksın, çünkü her biri doğrudan bir artı ya da eksi cümlesine dönüşüyor.

**8 altın kural**, her biri tanıdığın bir örnekle:

1. **Tutarlılık:** Aynı şey her yerde aynı görünsün. Bir sayfada "Kaydet" butonu sağ altta yeşil, diğerinde sol üstte gri "Tamam" ise kullanıcı her ekranda yeniden öğrenmek zorunda.
2. **Evrensel kullanılabilirlik:** Acemi de uzman da, yaşlı da engelli de kullanabilsin. Uzmana kısayol, acemiye menü. Merdivenin altındaki engelli tuvaleti bunun ihlali.
3. **Kaliteli geri bildirim:** Her eylemin görünür bir cevabı olsun. (Wi-Fi örneği.)
4. **Kapanış sağlayan diyalog:** İşin başı, ortası, sonu belli olsun. "Siparişiniz alındı ✓" mesajı. ATM'de para alınca iş bitti sanılması bunun sorunu.
5. **Hatadan koruma:** Hata yapmayı zorlaştır. Tarih alanına harf yazdırma, "kalıcı olarak sil" için onay iste. (ATM çözümü.)
6. **Geri alma:** Ctrl+Z. Kullanıcı geri alabileceğini bilirse rahat dener, korkmaz.
7. **Kontrol kullanıcıda:** Sistem sürpriz yapmasın. Kendi kendine sayfa değiştiren, kapatılamayan reklam, zorla güncelleme ihlal.
8. **KSH yükünü azalt:** Kullanıcı bir şeyi aklında tutmak zorunda kalmasın. Önceki ekrandaki kodu ezberleyip sonrakine yazdırma; göster.

**Ezber cümlesi:** "Tutarlı, Evrensel Geri bildirimle Kapanan, Hatadan korunan, Geri alınabilen, Kontrolü kullanıcıda, KSH'si hafif arayüz."

### Suchman

Norman ve Shneiderman'a karşı duruş. Onlar kullanıcıyı planlı hareket eden bir bilgi işlemci gibi görür: hedef koy, plan yap, uygula. Suchman diyor ki **insanlar öyle davranmaz.** Duruma göre anlık tepki verirler (**situated action**, "durumsal eylem"). Planlar her zaman eksiktir, yolda değişir.

Örnek: Google Maps'te bir rota planladın ama yolda trafik var, bir kafe gördün, arkadaşın aradı. Planın sürekli değişiyor. Suchman'a göre iyi sistem bunu anlamalı, **seninle konuşur gibi, durumuna göre** davranmalı.

Yani:

- **Norman & Shneiderman:** Etkileşim = makinenin mesajı kullanıcıya iyi sunması. **Bugünün** sorunları için.
- **Suchman:** Etkileşim = iletişim, makine kullanıcıyı anlamalı. **Geleceğin** sistemleri için. (Bugünkü yapay zekâ asistanları buna daha yakın.)
- **Licklider (1960)** de Suchman tarafında: bilgisayarla çalışmak bir meslektaşla çalışmak gibi olmalı.

---

## Konu 4: İnsan zihni nasıl çalışır? (Ders 4)

Hocanın bu dersteki tek mesajı: **kullanıcı bilgisayar değil.** Dikkati, hafızası, algısı sınırlı. İyi arayüz bu sınırları zorlamaz, onlara göre tasarlanır.

### İBE'nin 4 boyutu

| Boyut | Neyle ilgili |
|---|---|
| **Algısal** | Görme, işitme |
| **Bilişsel** | Hafıza, öğrenme, dikkat |
| **Fizyolojik** | Fiziksel ergonomi (oturuş, ekran açısı, tuş boyu) |
| **Sosyal** | Organizasyon, grup içinde kullanım |

Bu dersin konusu **bilişsel** ve **algısal** boyut.

### Bilgi işleme modeli (Wickens / Card-Moran-Newell)

Ekrana baktığın andan tıkladığın ana kadar beyninde olan zincir:

| Aşama | Ne yapar | Özelliği |
|---|---|---|
| **1. Algısal ön işlemci** | Göze/kulağa gelen ham veriyi alır | Bilinçsiz, çok hızlı, **1 saniyeden kısa** sürede silinir |
| **2. Dikkat** | Bu verinin hangisine odaklanacağını seçer | Sınırlı. Ön işlemciden **sonra** devreye girer |
| **3. Algı** | Seçilen şeyi tanır, kategoriye koyar ("bu bir buton") | Bilinçli |
| **4. Kısa süreli hafıza (KSH)** | O an üzerinde çalışılan bilgi | 7±2 birim, 10-30 sn |
| **5. Uzun süreli hafıza (UZH)** | Bilgi, deneyim, alışkanlık | Kapasite sınırsız, yavaş, anlamla saklanır |
| **6. Karar ve tepki seçimi** | Ne yapacağına karar verir | Otomatik (alışık işler) ya da kontrollü (yeni işler) |
| **7. Tepkinin gerçekleşmesi** | Tıklama, yazma | Fiziksel hareket |
| **8. Geri bildirim** | Sonucu görüp döngüye tekrar girer | Norman'ın döngüsüyle aynı fikir |

**Arayüzle bağlantısı:** Her aşama bir darboğaz. Kötü tasarım genelde bunlardan birini zorlar:

- Ekran kalabalık → **dikkat** dağılır
- Kullanıcıdan bilgi aklında tutması istenir → **KSH** taşar
- Alışılmadık bir düzen → **UZH**'deki deneyim işe yaramaz, karar yavaşlar

### Kısa süreli hafıza (KSH)

O an aklında tuttuğun şey. Biri telefon numarası söylüyor, sen tuşlayana kadar tekrar ediyorsun, işte orası.

- **Küçük:** Aynı anda **7±2** birim (5 ile 9 arası)
- **Kısa:** Tekrar etmezsen **10-30 saniyede** silinir
- **Kırılgan:** Yeni bilgi gelince eskisi gider (araya biri soru sorarsa numara uçar)
- **Tekrar** bilgiyi tutar, **gruplama** kapasiteyi genişletir
- Hocanın deyişiyle: **arayüz tasarımının en kritik unsurlarından biri**

**KSH mi UZH mi?** Kullanıcı adın, doğum tarihin, sık kullandığın şifren **UZH**'de, unutmazsın. KSH, o an yeni gördüğün ve ezberinde olmayan bilgi içindir: SMS kodu, sipariş numarası, önceki ekranda görüp sonrakine yazman gereken referans kodu. **"Bu bilgiyi kullanıcı zaten biliyor mu?"** diye sor. Biliyorsa KSH sorunu değil.

**KSH deneyi (derste yapılan):** 10 sayı okunuyor, sırayla yazılması isteniyor. Sonuç: **ilk ve son** sayılar iyi hatırlanıyor, **ortadakiler** kayboluyor (U eğrisi). Sayılara **ipucu** eklenince (vurgu, renk, aşinalık) ortadakiler de hatırlanıyor.

İpucu türleri:
- **İşitsel:** aksan, vurgu, aşinalık
- **Görsel:** renk, etiket, büyüklük, ayırt edici özellik

Arayüzdeki karşılığı: önemli bilgiyi renk, boyut, etiketle ayırırsan kullanıcı onu hatırlar.

### Uzun süreli hafıza (UZH)

- Teorik olarak **sınırsız**
- **Yavaş** işler
- Bilgiyi **anlamla** saklar

Arayüzdeki karşılığı: **tutarlılık** ve **metaforlar** UZH'yi kullanır. Kullanıcı "çöp kutusu = sil", "X = kapat" bilgisini zaten biliyor; buna uyarsan düşünmeden kullanır.

### Gruplama (chunking)

Bilgiyi **anlamlı** parçalara bölmek. KSH'ye daha fazlası sığar.

- `TDKUSBTRTSSKDNATSK` → 18 harf, 7±2'nin çok üstünde, ezberlenemez
- `TDK · USB · TRT · SSK · DNA · TSK` → 6 tanıdık grup, kolay
- `SUNIBMMAC` → `SUN IBM MAC` · `3122103683` → `312 210 3683`

**Gruplar anlamlı olmalı.** Rastgele bölmek işe yaramaz. Anlamı veren şey kullanıcının **geçmiş deneyimi** (UZH).

Arayüzde gruplama iki boyutta yapılır:
- **Fiziksel:** Menü düzeni, benzer butonların yan yana olması, başlıklar, boşluklar
- **Bilişsel:** Komutların mantıklı sırası (önce seç, sonra işlem yap)

### Algı aktiftir

Göz kamera gibi kaydetmez, beyin gördüğünü **yorumlar.** İki yönden çalışır:

| | Aşağıdan yukarı | Yukarıdan aşağı |
|---|---|---|
| **Kaynağı** | Gözün gördüğü ham görüntü | Kafandaki deneyim ve beklenti |
| **Arayüzde sorun** | Küçük, soluk, düşük kontrastlı, kalabalıkta kaybolan öğe | Beklentiye ters düşen konum, renk, ikon |
| **Örnek** | Açık gri üstüne açık gri yazı | "Kapat" sol altta (herkes sağ üstte bekler), "Sil" butonu yeşil |
| **Ayırt etme testi** | Görmesi mi zor? | Aklına gelmesi mi zor? |

**Kanıtı illüzyonlar:**
- **Zöllner:** Paralel çizgiler, üstündeki kısa çizgiler yüzünden paralel görünmüyor
- **Jastrow:** Aynı boyuttaki iki yaydan biri daha büyük görünüyor

İkisinde de beyin **bağlama** bakıp yanlış yorumluyor. Arayüzde de hizasız, karışık bir ekran kullanıcıyı yanıltır.

Derste çıkan sonuçlar:
- Uyaranlar **düzenliyse** etkileşim otomatikleşir (düşünmeden kullanırsın)
- **Düzensiz** uyaranlar eski deneyime göre yorumlanır, yorum bazen **eksik ya da yanlış** olur
- Kullanıcılar arası farklılık bilgiyi farklı algılamaya yol açar
- **Deneyim ve sürekli kullanım** kullanıcılar arasındaki farkı azaltır

### Biliş düzen arar

Beyin her şeyi bir kategoriye koymak ve **işlem eforunu azaltmak** için kalıp arar.

- **CAPTCHA:** Bozuk harfleri sen deneyiminle tamamlarsın (yukarıdan aşağı), bot tamamlayamaz
- **Okuma:** Kelimenin sadece ilk 4-5 harfine bakarız, gerisini beyin tamamlar. Tanımadığımız kelimede daha uzun dururuz. Deneyimli okur daha kısa durur.
- **BÜYÜK HARFLE YAZILMIŞ METİN** daha zor okunur, çünkü bütün kelimeler aynı dikdörtgen şekle sahip. KaRıŞıK hArF ise daha da zor, çünkü düzen yok.

### Tutarlılığın iki türü

- **İç tutarlılık:** Uygulama kendi içinde tutarlı mı? (Kapat her ekranda aynı yerde mi?)
- **Dış tutarlılık:** Platform standardıyla, diğer uygulamalarla tutarlı mı? (Herkes sağ üstte koyuyorsa sen de mi?)

İç tutarlılık varsa düzenli kullanıcı zamanla alışır. Dış tutarlılık yoksa yeni kullanıcının beklentisiyle (UZH) çelişir. **Sınavda ikisini birlikte yazarsan hem artı hem eksi vermiş olursun.**

### Hangi aşamada sorun var? (teşhis)

| Kullanıcının durumu | Sorun |
|---|---|
| Öğeyi **göremiyor** (küçük, soluk) | Algı (aşağıdan yukarı) |
| Öğeyi **beklemediği yerde** olduğu için bulamıyor | Algı (yukarıdan aşağı), dış tutarlılık |
| Görüyor ama **neye bakacağını bilmiyor** | Dikkat, görsel hiyerarşi yok |
| Gördüğünü **aklında tutamıyor** | KSH, gruplama yok |
| Ne yapacağını **biliyor ama yanlış yaptı** | Kayma (Norman) |
| Sistemin nasıl çalıştığını **yanlış anlamış** | Yanılgı, kavramsal model (Norman) |

### Tasarıma etkisi (sınavda hazır cümle)

- Arayüz **algısal gruplamayı desteklemeli:** benzer öğeler yan yana, başlıklar, boşluklar.
- **Görsel taramaya yardım etmeli:** önemli öğe büyük, belirgin, öne çıkan yerde.
- **İkonlara etiket eklenmeli:** sadece ikon tanımayı zorlaştırır, etiket hatırlamaya yardım eder.
- **Kullanıcıya ezberletilmemeli, gösterilmeli:** hatırlamak yerine tanısın (Shneiderman'ın 8. kuralı).
- **Tekrar ve tutarlı yerleşim** gruplamayı ve hatırlamayı kolaylaştırır.
- **Tasarımcı ürünü kullanıcının gözünden göremez.** Sistemi o tasarladığı için her şeyi biliyor. **Bailey (1993):** 81 tasarımcının **%95'i** gerçekte en iyi performans veren arayüzü değil, diğerini seçti. Sonuç: tasarımcının zevkine değil, **kullanıcı testine** güvenilmeli.

### Kullanıcıların temel özellikleri (kısa soru gelebilir, ezberle)

1. Deneyimle değişirler
2. Aktif öğrenirler
3. Dikkatleri kısıtlıdır
4. Hata yaparlar
5. Hepsi farklıdır
6. Hedef merkezlidirler
7. Sistemi kafalarında modellerler

**Nielsen (1993) kullanıcı tipleri:** İki eksen var. **Bilgisayar deneyimi** (düşük/yüksek) ve **alan bilgisi** (bilgili/bilgisiz). Mesela muhasebe programında: muhasebeyi bilen ama bilgisayarı az kullanan bir muhasebeci ile bilgisayarı iyi kullanan ama muhasebeden anlamayan bir stajyer farklı kullanıcılardır, arayüz ikisine de hizmet etmeli.

### Çözümlü kontrol soruları

**1. Ayarlar menüsünde etiketli 40 seçenek alt alta, grup başlığı yok. Sorun ne?**

> Sorun gruplama eksikliği ve buna bağlı dikkat ile KSH yükü. Her seçenek okunabildiği için algı sorunu yoktur; ancak 40 öğe tek listede olduğundan görsel hiyerarşi yoktur, göz neye odaklanacağını bilemez ve görsel tarama uzar. Kullanıcı aşağı indikçe yukarıda gördüklerini aklında tutamaz, çünkü 40 öğe KSH'nin 7±2 kapasitesinin çok üstündedir. Sonuç olarak aradığı ayarı geç bulur, verimlilik düşer. Çözüm: seçenekleri "Bağlantılar", "Ses ve ekran", "Gizlilik" gibi 5-7 anlamlı başlık altında gruplamak ve en üste bir arama kutusu eklemek.

**2. Bir uygulamada "kapat" butonu sol altta. Kullanıcı neden zorlanır?**

> Sorun yukarıdan aşağı algı ve dış tutarlılık ihlalidir. Buton görünür durumdadır, yani görme (aşağıdan yukarı) sorunu yoktur. Ancak kullanıcılar diğer uygulamalardan "kapat"ın sağ üstte olduğunu öğrenmiştir; beyin oraya bakar, sol altı aramaz. Sonuç olarak kullanıcı butonu bulmakta zorlanır, zaman kaybeder (verimlilik) ve yanlış öğeye tıklayabilir (kayma). Uygulama kendi içinde her ekranda aynı yeri kullanıyorsa iç tutarlılık sağlanmıştır ve düzenli kullanıcı zamanla alışır; ama yeni kullanıcı için butonun platform standardı olan sağ üste taşınması daha doğrudur.

---

## Konu 5: Ders 1 ve 2'den kalanlar

### İBE çalışmalarının çerçevesi (Ders 1)

İBE şu soruları sorar:
- İnsanların teknoloji kullanımını etkileyen özellikleri neler?
- Teknolojinin, insanların onu kullanımını etkileyen yönleri neler?
- İnsanlar etkileşim becerilerini nasıl edinir ve kavramlaştırır?
- İnsan ihtiyaçlarını teknik olanaklarla nasıl eşleştiririz?
- Teknoloji organizasyonları nasıl etkiler?
- Kullanılabilir teknolojiler nasıl tasarlanır?

### Neden İBE? (Ders 1, kısa soru gelebilir)

1. **Sıradan kullanıcı nüfusu arttı:** artık teknik olmayan herkes bilgisayar kullanıyor.
2. **Organizasyonlar bilişim sistemlerine bağımlı.**
3. **Üretkenlik ikilemi** (aşağıda).
4. **Donanım ucuzladı, yazılım ve insan maliyeti arttı:** pahalı olan artık insanın zamanı.
5. **Kritik uygulama alanları:** tıp, ordu, bankacılık. Hata can ya da para kaybettirir.

### İBE'nin ilişkili olduğu disiplinler

Bilgisayar bilimi, psikoloji, bilişsel psikoloji, ergonomi, örgütsel psikoloji, yazılım mühendisliği, grafik ve endüstriyel tasarım, sosyoloji, antropoloji, eğitim. **İBE çok disiplinlidir.**

### Kullanılabilirliğin ek ölçütleri

ISO üçlüsüne ek olarak slaytta geçenler: **kullanım kolaylığı, kullanımdaki başarı ve hız, hata sayısı, öğrenme kolaylığı, kalıcılık** (bir süre kullanmayınca hatırlanması), **kullanıcı memnuniyeti.**

Memnuniyeti etkileyen başka şeyler: diğer teknolojilerle kişisel deneyim, çalışma tarzı, kullanıcının kişiliği, ürün estetiği.

**İdeal kullanılabilirlik:** ürünü kullanmak, içinden çıktığı kutuyu açmak kadar kolay olmalı.

**Slayttaki ölçülebilir kriter örnekleri:**
- "Ürün X, kullanıcıların **%70'i** tarafından, **ek eğitim olmadan**, tüm görevleri **%95 doğrulukla**, mevcut uygulamadan **%25 daha hızlı** ve **en az eşit memnuniyetle** kullanılmaktadır."
- "Ürün Y, kullanıcıların **¾'ü** tarafından, **20 dakikalık eğitimle**, görevlerin **%100'ü** doğru, her görev **2 dakikada**, **5 üzerinden 4** memnuniyetle kullanılmaktadır."
- Kötü örnekler: "Ürün X kullanışlıdır" (anlamsız), "Yeni uygulama öncekinden daha kullanışlı" (hangi anlamda, kimin için, nerede?).

### Üretkenlik ikilemi ve Landauer (Ders 2)

**Tanım:** Bilişim teknolojisine yatırım çok hızlı artıyor, ekonomik üretkenlik artışı yavaş kalıyor.

- **Landauer (1995):** Üretkenlik ile BT verisi negatif ilişkili. Karşı fikirlerin ("zamanla görülecek", "satışlar iyi", "insanlar öyle söylüyor", "ölçme sorunu") temeli zayıf.
- Konu güncel: 2014'te "Solow paradoksunun dönüşü" (Acemoglu vd.), 2016'da "verimlilik durgunluğu" (Derviş & Qureshi).
- **Sebepler:** yazılımların zayıf tasarlanması; teknik otomasyon oldu ama kullanım süreçleriyle bütünleşmedi.
- **Çözüm:** tek çözüm kullanıcı merkezli tasarım.
  - Kullanılabilirlikle iş verimliliğinde **%25'e kadar** artış.
  - "Tipik arayüzde **40 sorun** vardır, **20'sini** düzeltmek kullanılabilirliği **%50** artırır."
- **Karşı örnekler** (ikilemin her yerde geçerli olmadığı): bankacılık, çevrimiçi alışveriş, e-devlet, e-posta.

**Shneiderman (1992, 2016) ile Landauer farkı:** Landauer ekonomik ve kurumsal bakar (verimlilik, süreç). Shneiderman bireye bakar: bilgisayarlar **yaşam kalitesini artırır**, sistemler **insanlar arası çeşitliliği** dikkate almalı, **ölçülebilir hedefler** konmalı.

### Etkileşim ve arayüz tanımları (Ders 2)

- **Etkileşim (TDK):** her şeyin hem kendisinin bağlı olduğu hem de kendisine bağlı olan karşılıklı etkiler bütünlüğü içinde olması; neden ile sonucun iç içe olup sürekli yer değiştirmesi. İBE'deki karşılığı: 4 bileşen birbirini sürekli etkiler.
- **Arayüz (TDK):** bilgisayar yazılımlarının kullanıcı tarafından çalıştırılmasını sağlayan, resim, grafik ve yazıların yer aldığı ön sayfa.
- **Arayüz (İBE):** bilginin kullanıcı ile araç arasında aktarılmasını sağlayan **iletişim kanalı.**

**Arayüz türleri:**
- **Fiziksel:** klavye, fare, ekran
- **Kavramsal (metaforik):** masaüstü, çöp kutusu, dosya, klasör

**Giriş/çıkış cihazları:**
- Giriş: klavye, fare, joystick, dokunmatik ekran, çizim tabletı, elektronik eldiven, mikrofon, tarayıcı
- Çıkış: ekran, hoparlör, yazıcı, hareketli platform, titreşimli cihazlar, hologram
- Hem giriş hem çıkış: çizim tableti, elektronik eldiven

**Etkileşim tipleri:**
- Geleneksel: **komutlar, menüler, formlar**
- Yeni: **doğal dil, duygular, beyin-bilgisayar**

**Hangi arayüz? (İBE bağlam kuralı):** Kullanılabilirlik kullanıcı tipine, görevlerine ve kullanım ortamına bağlıdır. Tek doğru arayüz yok.

**Metafor: gerçekçi resim mi, çizim mi? (bölüm sonu sorusu):** Sade çizim genelde daha iyi. Gerçekçi fotoğraf gereksiz detay getirir, bilişsel yükü artırır, küçük boyutta seçilemez. Metaforun amacı kullanıcının zaten bildiği şeyi (UZH) çağırmak, bunun için tanınabilir bir sembol yeter.

### Norman'a göre kullanılabilir arayüz (5 soru)

Kullanıcı arayüzle etkileşirken ne kadar kolay:
1. Aracın fonksiyonlarını anlıyor?
2. Yapmak istediğini fiziksel hareketle eşleştirebiliyor?
3. Görevi gerçekleştiriyor?
4. Sistemin bulunduğu durumu anlıyor?
5. Sistemin istenen durumda olduğunu söyleyebiliyor?

İlk 3'ü gerçekleştirme, son 2'si değerlendirme körfezi.

### Norman'ın etkileşim görüşü (madde madde)

- Etkileşim, mesajların makineden kullanıcıya etkin şekilde sunulmasıdır.
- Hata etkileşimin doğal bir parçasıdır.
- Kullanıcı sistem modelini **parçalı bilgilerle** oluşturur.
- Kararlarımızı fiziksel harekete çevirir, sonra sonuçlarını yorumlarız.
- Olaylar tepkimizi tetikler, dünya ile etkileşimimiz sürekli bir döngüdür.

### Suchman'a göre etkileşim (madde madde)

- Davranış bağlamla ilişkilidir.
- Planlar daima eksik ve değiştirilebilirdir.
- Etkileşim bir tür iletişimdir.
- Bir eylem yapmadan önce tepki beklenir.
- **Sadece bilişsel modelleri temel alan tasarımın başarı şansı düşüktür.**
- Yüz yüze konuşan iki kişi karşısındakinin modunu, eğitim düzeyini anlayıp ona göre cevap verir; bilgisayar da öyle davranmalı.

**TÜBİTAK Vizyon 2023:** "İnsanlar bilgisayara ayak uyduracağına, bilgisayarlar insanlara ayak uydurmalı", yani "insan okur-yazarlığı olan bilgisayarlar". Hedef: kullanımı eğitim gerektirmeyen bilgisayarlar. Suchman çizgisinde.

### Bailey (1993) deneyi, ayrıntılı

81 arayüz tasarımcısı, 4 arayüz. Önce demo izleyip değerlendirdiler, sonra kısa test, sonra gerçek görevlerle kullandılar.

| Arayüz | Tasarımcı tercihi | Gerçek performans |
|---|---|---|
| Yazı ile giriş | 4. | **1.** |
| 1 seviyeli menü | 3. | 2. |
| 2 seviyeli menü | **1.** | 3. |
| Çoklu menüler | 2. | 4. |

Tasarımcıların **%95'i** en yüksek performansı gösterdikleri arayüzü değil, diğerini seçti.

### Kullanılabilirlik çalışma yöntemleri (Ders 1)

**Göz izleme:** Kullanıcının nereye, ne kadar baktığına dair **nesnel ve nicel** veri. Bilgi arama davranışını, en çok odaklanılan noktaları bulmak ve tasarımları karşılaştırmak için kullanılır. ("Gözler yalan söylemez.")

Ölçülen veriler: ilk odaklanma zamanı, odaklanma sayısı, odaklanma süresi, ilgi alanları arası geçiş yoğunluğu, gezinme yörüngesi, gezinme süresi.

**CogTool:** Açık kaynak araç. Bir arayüzde kullanıcının nasıl davranacağını **biliş, algı ve motor** davranışları simüle ederek modeller. İki tasarım modellenip karşılaştırılabilir.

### Tarihçe (Ders 1)

| Yıl | Olay |
|---|---|
| 1945 | **Vannevar Bush, MEMEX** ("As we may think"): PC, internet ve İBE'yi öngören vizyoner makale |
| 1959 | Shackel, bilgisayar için ergonomi |
| 1960 | **Licklider, insan-bilgisayar simbiyozu** |
| 1965 | **Engelbart, fare** ve etkileşim |
| 1969 | International Journal of Man-Machine Studies |
| 1970 | İngiltere'de HUSAT, ABD'de Xerox PARC |
| 1971 | Weinberg, The Psychology of Computer Programming |
| 1976 | NATO çalıştayı: "İnsan Bilgisayar Etkileşimi" |
| 1970'ler | **"Kullanıcı dostu"** kavramı doğdu |
| 1980 | Shneiderman, Software Psychology |
| 1982 | **ACM SIGCHI ve CHI konferansı** |
| 1985 | Hipertext sistemleri, 4 yeni İBE dergisi |
| 1980'ler sonu | Kullanılabilirlik laboratuvarları |
| 1990'lar | WWW, üniversitelerde İBE programları, mobil, sosyal ağlar |
| 2000'ler | Sanal/artırılmış gerçeklik, giyilebilir teknoloji, duygusal etkileşim |
| 2015 | Beyin-bilgisayar etkileşimi |

Etkileşimin evrimi: ana bilgisayarlar → delikli kart (1980'ler) → fare ve grafik arayüz → dokunmatik, ses, beyin.

### Ders 1'in görsel örnekleri

| Örnek | Ne oldu | Kavram |
|---|---|---|
| **ATM** | Para alınca kart unutuluyor, bankaya yılda 2-4,5 milyon $ | Kayma, kapanış, hatadan koruma. Çözüm: önce kart, sonra para |
| **Arngren.net** | Her yer ürün, animasyon, odak yok | Gruplama yok, görsel hiyerarşi yok, dikkat dağılıyor |
| **Nokia 3650** | Tuşlar dairesel dizilmiş | Dış tutarlılık, alışkanlığa ters |
| **Nokia E50** | Hoparlör açık kaldı, gizli görüşme yayıldı | Geri bildirim, sistem durumunun görünürlüğü |
| **Karışık yol tabelaları** | Hızla giderken oklar çözülemiyor | Eşleştirme, bilişsel yük |
| **Zıt yönlü bisiklet işaretleri** | Aynı şeritte çelişen yön | Tutarlılık |
| **Engelli tuvaleti merdivenden aşağıda** | Kullanıcının kısıtı yok sayılmış | Evrensel kullanılabilirlik |
| **Vites kolu önünde içecek tutucu** | El kutulara çarpıyor | Fiziksel ergonomi ("zararsız problem") |
| **Florida 2000 kelebek pusulası** | Adaylar iki sütunda, delikler ortada, Gore'un oyları Buchanan'a | Eşleştirme, gerçekleştirme körfezi ("ölümcül problem") |
| **USS Vincennes (3 Temmuz 1988)** | Yükseklik ve konum iki ayrı ekranda, stres altında yanlış yorumlandı, İran yolcu uçağı düşürüldü, **290 ölü** | Değerlendirme körfezi, bilgi sunumu |
| **Singapur Havayolları** | Fırtınada kapalı piste girildi, **79 yolcu + 4 kabin ekibi** öldü | Görülebilirlik, yönlendirme |
| **Uçları buluşmayan köprü** | Parçalar birbirinden habersiz yapılmış | Bütünleşme sorunu |
| **QWERTY / Dvorak / F klavye** | Daha verimli düzen var ama standart değişmiyor | **"İyiler her zaman kazanmaz"** |
| **Pasta menü** | Seçenekler merkeze eşit uzaklıkta | Alternatif tasarım mümkün, verimlilik |
| **"Mükemmel kullanıcı" karikatürü** | Süper yetenekli hayali yaratık | Tasarımcı gerçek kullanıcının sınırlarını yok sayıyor |

**Vincennes'ten alınan dersler:** NATO standartları oluşturuldu. "NATO Guidelines on Human Engineering Testing and Evaluation" raporu bilişim sistemlerinin daha kullanılabilir olması için nasıl test edileceğini açıklar. İnsan merkezli tasarım savunma sanayinin kritik konusu oldu (Corona, 1997).

### Ders etkinlikleri (hocanın kendi soruları)

- **Ders 1:** Telefonunu farklı marka kullanan arkadaşına ver, takvime randevu eklemesini iste. Zorlukları listele. Aynısını yaşlı bir yakınınla yap.
- **Ders 2:** Bir alışveriş sitesini Shneiderman'ın 8 kuralıyla analiz et. Metaforlarda gerçekçi resim mi çizim mi?
- **Ders 3:** Buzdolabı ve TV kumandasını Norman'ın 7 aşamasıyla değerlendir, hangisi kolay, neden? Marketlerdeki self-servis kasayı körfez yaklaşımıyla analiz et.
- **Ders 4:** 4 rakam ve 10 sayılık KSH deneyi.
- **Tasarım günlüğü (her ders):** çevrendeki bir kullanılabilirlik problemini bul, dersle değerlendir, çözüm öner.

---

## Konu 6: Slayt görsellerindeki ek detaylar (NotebookLM'den)

> Bunlar slayt görsellerinde var, metinde yok. Önceliği düşük, kısa soruda bonus olarak işe yarar. Zamanın azsa atla.

**Ders kitabı:** Kürşat Çağıltay, *İnsan Bilgisayar Etkileşimi ve Kullanılabilirlik Mühendisliği: Teoriden Pratiğe* (ODTÜ Yayıncılık). Diğer kaynaklar: Booth (1989), Hacer Karacan ders notları.

**Kullanılabilirlik laboratuvarı:** tek taraflı ayna, ses yalıtımlı test odası, video mikseri, gözlem monitörleri. Kullanıcı test odasında görev yapar, araştırmacılar aynanın arkasından izler.

**Göz izleme ek terimler:**
- **İlgi alanı (AOI, area of interest):** ekranda incelenen bölge
- **Gezinme yörüngesi (gaze plot / scanpath):** gözün sırayla gezdiği noktalar
- **Isı haritası:** en çok bakılan yerler kırmızı
- **F-şekli tarama:** Google, eBay gibi sonuç sayfalarında kullanıcı önce üstte yatay, sonra biraz aşağıda yatay, sonra sol kenardan aşağı tarar. Sonuç: önemli bilgi sol üste ve satır başlarına konmalı.
- **Hürriyet (2006) ısı haritası:** yoğun sayfada bakışlar sol üst manşette toplanıyor, gerisi görülmüyor.
- **Banner körlüğü (ODTÜ ana sayfa):** kullanıcı reklam gibi görünen alanlara hiç bakmıyor, gezinme butonlarına odaklanıyor.

**Üretkenlik ikilemi ek kaynak:** Roach (1992), hizmet sektöründe bilişim yatırımı artarken verimliliğin durduğunu gösterir.

**Duygusal etkileşim (affective computing):** yeni etkileşim tiplerinden biri. Slaytta Didem Gökçay ve Gülsen Yıldırım'ın kitabı ile ODTÜ COGS 595 dersi geçiyor.

**Öğrenme eğrisi grafiği (dostça vs dostça olmayan arayüz):** x ekseni kullanım günü, y ekseni hata sayısı.
- Dostça arayüz: ~40 hatayla başlar, hızla düşer.
- Dostça olmayan arayüz: ~110 hatayla başlar, ancak 8. günde eşitlenir.
- Çıkarım: kötü arayüz de öğrenilir ama başlangıç maliyeti çok yüksek, öğrenme kolaylığı ölçütü bu.

**Klavye:** Dvorak düzeninde en sık kullanılan harflerin büyük kısmı (~%35) ana sırada (home row). Yine de QWERTY kazandı: "İyiler her zaman kazanmaz."

**Model Human Processor (Card, Moran, Newell 1983), işlemci süreleri:**

| Bileşen | Ortalama süre |
|---|---|
| Algı işlemcisi | ~100 ms |
| Bilişsel işlemci | ~70 ms |
| Motor işlemci | ~70 ms |
| Göz hareketi | ~230 ms |
| Görsel depo | ~200 ms tutar, ~17 harf |
| İşitsel depo | ~1500 ms tutar, ~5 harf |
| Çalışan bellek | 7±2 birim |
| Uzun süreli bellek | sınırsız kapasite, sınırsız süre, anlamsal kodlama |

Sayıları ezberlemene gerek yok. Bilmen gereken: görsel bilgi çok hızlı siliniyor, işitsel bilgi biraz daha uzun kalıyor. Arayüzde önemli bilgi ekranda kalmalı, bir an görünüp kaybolmamalı.

**Okuma deneyi (Cambridge metni):** harflerin sırası karışık olsa bile ilk ve son harf doğruysa kelime okunabiliyor. Beyin kelimeyi bütün olarak tanıyor, düzen arıyor.

---

## Konu 7: Uzun soru (tasarım değerlendirme)

Hocanın duyurusu: **birkaç kısa soru + bir uzun soru.** Uzun soru büyük ihtimalle bir arayüz görseli verip yorumlatacak. Ödevler de bu tarzdaydı:
- **Ödev 1:** çevrende bir tasarım problemi bul, problem nedir, sen olsan nasıl çözerdin.
- **Ödev 2:** iyi bir tasarım bul, yüzde kaç etkili, verimli, memnun edici.

### Cevabın iskeleti

1. **Bağlam (1-2 cümle):** Kullanıcı kim, görev ne, ortam ne?
2. **Tasarımcının amacı (1-2 cümle):** "Tasarımcı muhtemelen ... için böyle yapmış."
3. **Artılar (en az 1-2):** gözlem + kavram + neden iyi
4. **Eksiler (en az 3):** gözlem + kavram + sonuç + öneri
5. **Etkililik / verimlilik / memnuniyet:** üçüne kısaca nasıl etkilediğini yaz
6. **Genel değerlendirme ve öneri:** ölçülebilir hedefle bitir

### Her eksi için 4 halka

> **Gözlem:** Giriş ve şifre sıfırlama butonları aynı renkte ve yan yana.
> **Kavram:** Bu, Norman'ın kayma hatasına açık ve Shneiderman'ın hatadan koruma kuralını ihlal ediyor.
> **Sonuç:** Acele eden kullanıcı yanlış butona basıp şifresini sıfırlatabilir, zaman kaybeder.
> **Öneri:** Birincil eylem olan "Giriş" belirgin renkte, "Şifremi sıfırla" sade bir bağlantı olarak ayrılmalı.

### Kontrol listesi (ekrana bakarken sırayla sor)

| Soru | Kavram |
|---|---|
| Ne yapılabileceği görünüyor mu? Neyin tıklanabilir olduğu belli mi? | Görülebilirlik, gerçekleştirme körfezi |
| Eylemin sonucu gösteriliyor mu (başarıda da)? | Geri bildirim, değerlendirme körfezi |
| Hata mesajı görünür yerde mi, ne yapılacağını söylüyor mu? | Geri bildirim, hatadan koruma |
| Kritik butonlar birbirine yakın veya benzer mi? | Kayma, hatadan koruma |
| Silme, ödeme gibi işlemler geri alınabilir mi, onay var mı? | Geri alma, hatadan koruma |
| Ekran kalabalık mı, öğeler gruplanmış mı, önemli şey öne çıkıyor mu? | Gruplama, dikkat, görsel hiyerarşi, KSH |
| Yazılar okunur mu (boyut, kontrast)? | Aşağıdan yukarı algı, evrensel kullanılabilirlik |
| Konum, renk, ikon alışılmış standarda uyuyor mu? | Yukarıdan aşağı algı, dış tutarlılık |
| Aynı şey her ekranda aynı mı? | İç tutarlılık |
| Kullanıcıdan bir şeyi aklında tutması isteniyor mu? | KSH yükü (ama UZH'deki bilgi için değil) |
| Kontrol ile etkisi doğal eşleşiyor mu? | Anlamlı eşleştirme |
| Yaşlı, engelli, acemi kullanabilir mi? Uzmana kısayol var mı? | Evrensel kullanılabilirlik |
| Sistem kendiliğinden sürpriz bir şey yapıyor mu? | Kontrol kullanıcıda |
| İşin bittiği belli mi? | Kapanış |

### Tasarımcıyı anlamak: ödünleşimler

"Tasarımcı neden böyle yapmış?" sorusunun en güçlü cevabı genelde bir **ödünleşim (trade-off):**

- **Güvenlik vs kullanılabilirlik:** "Kullanıcı adı veya şifre hatalı" mesajı hangisinin yanlış olduğunu söylemez. Kullanılabilirliği biraz düşürür, ama saldırganın geçerli kullanıcı adlarını bulmasını engeller. Bilinçli tercih.
- **Alan vs okunabilirlik:** Florida pusulasında adaylar tek sayfaya sığsın diye iki sütuna bölündü, eşleştirme bozuldu.
- **Estetik vs alışkanlık:** Nokia 3650 farklı görünmek için tuşları dairesel dizdi, kullanım zorlaştı.
- **Güvenlik vs kayma riski:** ATM kartı işlem boyunca içeride tutuyor (güvenlik), ama para sonra gelince kart unutuluyor.

Bir eksiyi yazarken "ama tasarımcı bunu ... için yapmış olabilir" dersen hem artıyı hem eksiyi görmüş olursun. Hocanın istediği bu denge.

### Sık yapılan hatalar (bu gece yaptıklarımız)

- **Geri bildirimi unutmak:** Bir şey ters gidiyorsa önce "kullanıcı ne olduğunu biliyor mu?" diye sor. Başarıda da geri bildirim gerekir.
- **Kavramı zorlamak:** Kullanıcı adının silinmesi KSH sorunu değil (kullanıcı adı UZH'de), verimlilik sorunu. Kavram uymuyorsa sonucu düz cümleyle yaz.
- **Güvenlik tercihini eksi saymak:** Önce "bunun bir sebebi olabilir mi?" diye düşün.
- **Hızı memnuniyet sanmak:** Hız verimlilik, his memnuniyet.
- **Algı yönlerini karıştırmak:** Görmesi zorsa aşağıdan yukarı, aklına gelmiyorsa yukarıdan aşağı.
- **Tek taraflı cevap:** En az bir artı yaz.

### Deneme sorusu: OBS giriş ekranı

**Ekran:** Üstte küçük gri yazıyla bir sürü link (Duyurular, Akademik Takvim, Yemek Listesi, KVKK...), altında 4 gri duyuru kutusu. Ortada küçük açık gri etiketli "kullanıcı adı" ve "şifre" kutuları. Altında yan yana aynı renkte "Giriş" ve "Şifremi sıfırla" butonları. Yanlış girişte sayfa yenileniyor, iki kutu da boşalıyor, sayfanın en altında sağda küçük soluk kırmızı "hatalı giriş" yazısı çıkıyor.

**Model cevap:**

> **Bağlam:** Kullanıcılar öğrenciler; görev sisteme hızlıca giriş yapmak. Kayıt dönemlerinde yoğun ve aceleyle kullanılan bir ekran.
>
> **Tasarımcının amacı:** Duyuruları ve sık kullanılan bağlantıları giriş ekranına koyarak öğrencinin önemli bilgileri giriş yapmadan görmesini istemiş. Şifre sıfırlamayı girişin yanına koyarak kolay bulunmasını sağlamış.
>
> **Artılar:** Giriş formu sadece iki alandan oluşuyor, sade. Şifre sıfırlama kolay bulunuyor. Hata mesajının kullanıcı adı mı şifre mi yanlış belirtmemesi güvenlik açısından doğru bir tercih, saldırganın geçerli kullanıcı adlarını bulmasını engelliyor.
>
> **Eksi 1:** "Hatalı giriş" mesajı sayfanın en altında, küçük ve soluk. Geri bildirim var ama görülmüyor, değerlendirme körfezi açık kalıyor. Kullanıcı neden giremediğini anlamadan tekrar deniyor. Mesaj kutuların hemen üstünde, belirgin renkte gösterilmeli.
>
> **Eksi 2:** "Giriş" ve "Şifremi sıfırla" aynı renkte ve bitişik. Bu kayma hatasına açık, hatadan koruma kuralını ihlal ediyor. Kullanıcı yanlışlıkla şifresini sıfırlatabilir. Giriş birincil renkli buton, sıfırlama sade bir bağlantı olmalı.
>
> **Eksi 3:** Etiketler ve linkler küçük, açık gri. Aşağıdan yukarı algı ve evrensel kullanılabilirlik sorunu, gözü zayıf kullanıcı okuyamaz. Ayrıca üstteki yazıların link mi düz yazı mı olduğu belli değil (görülebilirlik).
>
> **Eksi 4:** Duyurular ve linkler düzensiz, giriş formu öne çıkmıyor. Görsel hiyerarşi ve gruplama yok, dikkat dağılıyor, asıl görev geri planda kalıyor. Giriş formu ortada ve büyük, duyurular ayrı bir bölümde gruplanmalı.
>
> **Eksi 5:** Hatalı girişte kullanıcı adı da siliniyor. Şifrenin silinmesi güvenlik için mantıklı, ama kullanıcı adının silinmesinin güvenlik faydası yok; kullanıcı aynı şeyi tekrar yazmak zorunda kalıyor (verimlilik), tekrar yazarken yeni hata yapabiliyor (kayma). Sadece şifre alanı temizlenmeli.
>
> **ISO üçlüsü:** Etkililik orta (öğrenci sonunda giriş yapabiliyor ama yanlışlıkla sıfırlama riski var). Verimlilik düşük (hata mesajı görülmüyor, kullanıcı adı tekrar yazılıyor). Memnuniyet düşük (karmaşık, soluk, kullanıcıyı belirsizlikte bırakan bir ekran).
>
> **Öneri:** Bu düzeltmelerle hedef: "Öğrencilerin %95'i, hatalı denemeden sonra en fazla 30 saniyede doğru giriş yapabilmeli."
