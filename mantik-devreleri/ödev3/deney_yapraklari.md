# BLM2007 Mantık Devreleri Laboratuvarı — Deney Yaprakları (Ders 5: Kodlama)

## Deney Yaprağı 1: BCD Artı 3 ve Aiken için rakam dönüştürücüsü
- **Amaç:** Rakam kodlarını ayırmak, geçersiz sözcükleri reddetmek ve 9 tümleyenini doğrulamak.
- **Tanım:** Kod türü seçilebilen bir rakam dönüştürücüsü tasarlayınız. 8421 BCD, Artı-3 ve standart Aiken 2421 ders tablolarını kullanınız. Her rakam dört bit olacak; baştaki sıfırlar korunacaktır.

### Yapılacak işlemler
1. Üç kod için kodlayıcı ve çözümleyici tasarlayın. Artı-3’te her rakama 3 ekleyin; Aiken’de standart sözlüğü kullanın. Boş giriş, geçersiz karakter, yanlış bit uzunluğu ve geçersiz sözcükleri gerekçeli reddedin.
2. 48 ve 003 dizilerini üç kodla elle yazın ve programla karşılaştırın. 263’ün BCD ve saf ikili gösterimlerini bit sayısıyla karşılaştırıp aynı bit dizisinin yanlış kodla okunmasının sonucunu açıklayın.
3. Her kodda 16 dört bit desenini tarayıp geçerli/geçersiz kümeleri çıkarın. Aiken’de 0101 ve 1011’in toplamlarını karşılaştırarak ağırlıklı toplamın neden tek başına geçerlilik kanıtı olmadığını gösterin.
4. Artı-3 ve Aiken’de 0–9’un bütün kod bitlerini tersleyip çözün; 9 − d ilişkisini hesapla gerekçelendirin. BCD’nin aynı özelliğe sahip olup olmadığını bir karşı örnekle sınayın.
- **Teslim:** Algoritma/kod, dönüşüm tablosu, geçerlilik kümeleri, 9 tümleyeni gerekçesi ve BCD karşı örneği.

---

## Deney Yaprağı 2: Gray dönüştürücüsü ve komşuluk denetimi
- **Amaç:** İki yönlü Gray dönüşümünü ve komşuluk sınırını bağımsız kontrollerle incelemek.
- **Tanım:** Dört bitlik yansıtılmış ikili Gray kodunu kullanınız. Bitler soldan sağa en anlamlıdan en az anlamlıya sıralıdır. Farklı bit sayısını karşılık gelen konumları karşılaştırarak bulunuz.

### Yapılacak işlemler
1. İkili → Gray ve Gray → ikili algoritmalarını XOR ile kodlayın. Ters yönde önceki hesaplanan ikili bitin kullanılmasını gösterin; hazır Gray dönüştürücü kullanmayın.
2. 0–15 için ikili/Gray/geri çözülen ikili tablosu hazırlayın; ders tablosuyla bağımsız kontrol edin. Ardışık geçişleri ve 15 → 0 kapanışını, 0–9’a kesilmiş dizinin 9 → 0 geçişiyle karşılaştırın.
3. 101110101 ve 1000101 için Gray sonuçlarını elle bulup programla doğrulayın. Algoritmanızda giriş bit uzunluğunun korunduğunu gösterin.
4. Ters yönde komşu Gray bitlerini XOR’layan hatalı yöntemi sınayın. Doğru yöntemi ayıran dört bitlik giriş ve ilk ayrışan adımı gösterin; rastgele iki Gray sözcüğünün tek bit farkı taşımak zorunda olmadığını açıklayın.
- **Teslim:** İki algoritma, 16 satırlık tablo, geçişler, kaynak örnekleri ve hatalı yönteme karşı örnek.

---

## Deney Yaprağı 3: Beş bitte iki bir ve eşlik denetimi
- **Amaç:** İki hata denetim kuralını kurmak ve saptama ile düzeltmenin sınırını açıklamak.
- **Tanım:** 5’te 2 sözlüğü: 0=11000, 1=00011, 2=00101, 3=00110, 4=01001, 5=01010, 6=01100, 7=10001, 8=10010, 9=10100. Ağırlıklar 7–4–2–1–0’dır. Eşlik deneyinde yedi veri bitinin soluna p eklenecek; paket sekiz bit olacaktır.

### Yapılacak işlemler
1. 5’te 2 için sözcük geçerliliği denetleyicisi ve çift/tek eşlik için paket denetleyicisi kurun. Birincide tam iki 1, ikincide p dâhil toplam 1 sayısını kullanın; uzunluk/karakter hatalarını reddedin. 11000’ın özel sıfır atamasını açıklayın.
2. On geçerli 5’te 2 sözcüğünde bütün tek bit terslemelerini (50) ve iki farklı bit terslemelerini (100) tarayın. Saptanan/kaçan sayıları yazın; kaçan bir hatada eski ve yeni rakamı gösterin.
3. 1000011 ve 1000001 verilerini iki eşlik modunda elle kodlayın. Çift eşlikli 11000011 paketinin sekiz tek bit ve 28 iki bit terslemesini sınayın; sonuçları tek/çift tersleme kuralıyla açıklayın.
4. Geçersiz 01000 için iki olası özgün 5’te 2 sözcüğü bulun. Eşlikte yalnız p’nin terslenmesini ayrıca inceleyin. Bu örneklerle hata saptama, hatanın yerini bulma ve veri bitlerinin doğruluğunu ayırın.
- **Teslim:** Denetleyiciler, 50/100 ve 8/28 deneyin sayımları, eşlik örnekleri ve düzeltme sınırı.

---

## Deney Yaprağı 4: Karakter kodları ve barkodun bağımsız doğrulanması
- **Amaç:** ASCII ve EBCDIC’i ayırmak ve optik gösterimin doğru okunmasını bağımsız doğrulamak.
- **Tanım:** Yalnız H, E, L, P, boşluk ve 0–3 karakterlerini destekleyiniz. EBCDIC kod sayfası IBM-037’dir. ASCII, başa 0 eklenerek sekiz bitlik alanda taşınacaktır. Barkod için hazır Code 128 üreticisi ve bağımsız okuyucu kullanmak serbesttir.

| Karakter | ASCII / onaltılı | EBCDIC IBM-037 / onaltılı |
|:---:|:---:|:---:|
| H / E / L / P | 48 / 45 / 4C / 50 | C8 / C5 / D3 / D7 |
| Boşluk | 20 | 40 |
| 0 / 1 / 2 / 3 | 30 / 31 / 32 / 33 | F0 / F1 / F2 / F3 |

### Yapılacak işlemler
1. Verilen tabloyla kod adı seçen bir karakter kodlayıcı/çözümleyici yazın; destek dışı girdileri reddedin. HELP 2031 metnini ASCII ve EBCDIC ile yazıp geri çözün. H karakterinin iki kodunu bağımsız bit ağırlıklarıyla denetleyin.
2. 48 45 4C 50 ve C8 C5 D3 D7 dizilerini doğru ve yanlış kod adıyla çözmeyi deneyin. ASCII → EBCDIC için üst bit ekleme/kesme yönteminin neden yetmediğini H örneğiyle gösterin.
3. HELP 2031, HELP2031, 000123 ve 123 için Code 128 üretin. Bağımsız okuyucunun döndürdüğü metinleri karakter karakter karşılaştırın; boşluk ve başlangıç sıfırının etkisini açıklayın. Üretici ve okuyucu adlarını kaydedin.
4. Bir barkodun özgün, küçültülmüş ve sessiz alanları daraltılmış hâllerini aynı okuyucuda sınayın. Boyut, deneme sayısı ve başarı durumlarını kaydedin; üreticinin metni ekranda göstermesinin neden bağımsız okuma kanıtı olmadığını açıklayın.
- **Teslim:** Karakter kodu tablosu/kod, dört barkodun okuma sonuçları ve üç görünümün deney kaydı.
