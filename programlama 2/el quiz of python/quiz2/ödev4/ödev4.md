# ÖDEV 4

**Verilen Tarih:** 3.11.2026  
**Son Teslim Tarihi:** 9.11.2026 - 23:59

---

### Soru 1:
3 ayrı kullanıcı için yaş hesaplama fonksiyonu oluşturunuz. Doğum yılını ve emeklilik yaşını girmesini isteyiniz. Ardından bu bilgilere dayalı olarak emeklilik yılını hesaplayın ve kullanıcıya bir mesaj döndürün. Eğer kişi zaten emekliyse veya emekliliği geçtiyse, buna dair bir mesaj yazdırın. Tüm işlevleri içeren modülü yazınız.

---

### Soru 2:
“Hava kirliliği, dünya genelinde büyük bir çevresel sorun olarak karşımıza çıkmaktadır. Hava kirliliği, atmosferdeki zararlı gazlar, kimyasallar, tozlar ve partiküllerin yüksek seviyelerde bulunması sonucu ortaya çıkar. Bu kirleticiler, sanayi tesisleri, araç emisyonları, enerji üretimi ve tarım gibi kaynaklardan atmosfere salınır. Hava kirliliği, ciddi sağlık sorunlarına yol açabilir ve doğal ekosistemlere zarar verebilir.

Hava kirliliği, insan sağlığına bir dizi olumsuz etki yapar. Kirli hava solumak, solunum yolu hastalıklarının, kalp hastalıklarının, kanser riskinin artmasına ve genel yaşam kalitesinin düşmesine neden olabilir. Ayrıca, çocuklar, yaşlılar ve kronik sağlık sorunları olanlar, hava kirliliğinin etkilerine daha fazla maruz kalabilirler.

Hava kirliliği aynı zamanda ekosistemlere zarar verir. Bitkiler, hayvanlar ve su kaynakları üzerinde olumsuz etkiler yaratabilir, biyolojik çeşitliliği azaltabilir ve tarım verimliliğini etkileyebilir.

Bu sorunun çözümü için dünya genelinde çevresel düzenlemeler ve temiz enerji kaynaklarına geçiş gibi adımlar atılmaktadır. Ayrıca, bireysel olarak daha çevre dostu seçimler yaparak da hava kirliliğinin azaltılmasına katkı sağlayabiliriz. Hava kirliliği ile mücadele, hem insan sağlığını hem de gezegenimizin geleceğini korumak için önemlidir.”

Yukarıdaki metinde “hava” kelimesinin kaç defa geçtiğini hesaplayan modülü yazınız.

---

### Soru 3:
```python
matrix= [ [1, 2, 3],
          [4, 5, 6],
          [7, 8, 9] ]
```

Yukarıda verilen 3x3 boyutlu matrisin determinantını hesaplayan modülü yazınız.

---

### Soru 4:
Kullanıcının “enter” e basıncaya dek girdiği metin içerisinde alfabenin her harfinin kaç kez bulunduğunu bulan (büyük ve küçük harfleri beraber sayın) python kodunu modül kullanarak yazınız.

**Not:** Bu sorunuzda hazır fonksiyon kullanmayınız. Sadece `lower()` ve `len()` kullanabilirsiniz.

---

### Soru 5:
Şehirleri kıtalara göre gruplayan bir fonksiyon yazınız.

```python
cities = {
    'İstanbul': {'population': 15000000, 'continent': 'Europe', 'country': 'Turkey'},
    'Tokyo': {'population': 37000000, 'continent': 'Asia', 'country': 'Japan'},
    'New_york': {'population': 8400000, 'continent': 'North America', 'country': 'United States'},
    'Mumbai': {'population': 20000000, 'continent': 'Asia', 'country': 'India'},
    'Cairo': {'population': 20000000, 'continent': 'Africa', 'country': 'Egypt'},
    'Seoul': {'population': 9765000, 'continent': 'Asia', 'country': 'South Korea'},
    'London': {'population': 8908081, 'continent': 'Europe', 'country': 'United Kingdom'}
}
```

(Örnek sözlük yukarıda verilmiştir.)

- **Adım 1:** ‘sehirler_sozlugu’ adında bir sözlük oluşturunuz. Bu sözlük, her şehri bir alt sözlük ile temsil eder ve her şehrin ‘ülke’ ve ‘kıta’ bilgileri içermelidir.
- **Adım 2:** ‘sehirleri_kitalara_göre_grupla’ fonksiyonunuz şehirleri kıtalara göre gruplamalıdır. Bu fonksiyon her kıtayı anahtar olarak içeren bir başka sözlük döndürür.
- **Adım 3:** En son gruplanmış olan şehir bilgilerini düzenli bir şekilde ekrana yazdırın.

---

### Soru 6:
İki tarih arasındaki gün ve hafta sayısını hesaplayan kodu yazınız. Kodunuz `'gun_sayisi_hesapla'` fonksiyonu ve `'hafta_sayisi_hesapla'` fonksiyonu içermelidir. Kodunuzda `tarih1` ve `tarih2` parametreleri, `"YYYY-MM-DD"` formatında olmalıdır. Kodlarınızı modül kullanarak yazınız.

**Not:** Bu soru için `datetime()` kullanmayınız.

---

### Soru 7:
İki tane liste oluşturunuz. Bu listeleriniz 10’ar elemanlı olsun ve random değerler atayınız. Ardından bu iki listeyi birleştirip sıralanmış halini ekrana bastıran python kodunu modül kullanarak yazınız.

**Not:** Bu sorunuzda **sıralama** ile ilgili hazır hiçbir fonksiyon kullanmayınız.

---

### Soru 8:
`L = [1, 2, 2, 3, 3, 4, 4, 5, 6, 7, 7, 8]` Verilen 12 elemanlı listeyi kullanarak bu listenin 2 ve 3 elemanlı alt kümeleri çıkarınız. Bu alt kümelerde benzer olanları ekrana yazdırınız.

