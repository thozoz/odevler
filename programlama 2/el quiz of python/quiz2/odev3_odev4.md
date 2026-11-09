# ÖDEV 3

**Verilen Tarih:** 27.10.2026  
**Son Teslim Tarihi:** 03.11.2026 - 23:59

## Soru 1

10 elemanlı bir tamsayı listesine kullanıcı tarafından sayılar girilecektir. Kural olarak; girilen her sayı, bir önceki sayıdan büyükse bu sayı listeye sırayla alınacak, küçükse göz ardı edilecektir. Bu kurala göre liste oluştuktan sonra (yani listenin 10 elemanı da dolduktan sonra) bu listeyi ters sırada ekrana çıkaran PYTHON kodunu yazınız.

**Cevap:**

```python
#10 elemanlı liste için boş liste tanımlıyoruz
liste = []

#listenin 10 elemanı dolana kadar while döngüsü calısacak
while len(liste) < 10:
    sayi = int(input(str(len(liste) + 1) + ". sayıyı giriniz: ")) #kullanıcıdan sayıyı alıyoruz
    
    #liste boşsa ilk girilen sayıyı direk listeye ekleriz karsılastırcak onceki sayı olmadıgından
    if len(liste) == 0:
        liste.append(sayi) #sayıyı listeye ekleme
        print("İlk sayı eklendi:", sayi)
    else:
        #girilen sayı bir onceki sayıdan buyuk mu bakarız (listenin son elemanından)
        if sayi > liste[-1]: #eger buyukse kurala uyar listeye ekleriz
            liste.append(sayi)
            print("Sayı eklendi:", sayi)
        else: #kucukse yada esitse goz ardı edilir listeye alınmaz
            print("Girilen sayı onceki sayıdan buyuk degil, göz ardı edildi.")

print()
print("Oluşan 10 elemanlı liste:", liste)

#listeyi ters sırada ekrana yazdırma
print("Listenin tersten yazılmıs hali:")
for i in range(len(liste) - 1, -1, -1): #son indexten 0. indexe kadar -1 azalarak gider
    print(liste[i], end=" ") #yanyana yazsın diye end koyduk

print() #alt satıra gecmek icin print
```

## Soru 2

Elemanları [1-25] arasındaki rastgele tamsayılardan oluşan 20 elemanlı bir liste oluşturunuz. Daha sonra bu listenin elemanları baştan itibaren toplandığında bu toplamın 100’ü geçtiği ilk anda duran ve en son olarak listenin hangi elemanının bu toplama dahil edildiğini bulan PYTHON kodunu yazınız.

**Cevap:**

```python
import random

#1-25 arası rastgele sayılardan olusan 20 elemanlı liste
liste = []

#20 kere donen döngü ile listeye rastgele sayılar atıyoruz
for i in range(20):
    sayi = random.randint(1, 25) #1 ile 25 arası rastgele tamsayı uretir
    liste.append(sayi) #uretilen sayıyı diziye atar

print("20 elemanlı liste:", liste)

toplam = 0 #bastan itibaren sayıları toplayacagımız degisken
son_eleman = 0 #toplama dahil edilen en son elemanı tutcak degisken
son_index = 0 #en son hangi indexteki eleman eklendi onu tutar

#listenin basından itibaren elemanları gezip topluyoruz
for i in range(len(liste)):
    eleman = liste[i] #suanki indexteki elemanı alıyoruz
    toplam += eleman #toplama ekliyoruz
    son_eleman = eleman #son eklenen elemanı guncelliyoruz
    son_index = i #son eklenen indexi guncelliyoruz
    
    #toplam 100 ü gectigi ilk anda döngü durur
    if toplam > 100: #100 u gectiyse break ile cıkarız
        break

#sonucları ekrana yazdırma
print("Toplam:", toplam)
print("Toplama en son dahil edilen eleman:", son_eleman)
print("Bu elemanın listedeki indexi:", son_index)
```

## Soru 3

3 basamaklı sayılar içinde, ilk ve son rakamlarının toplamı ortadaki rakamdan büyük olan tüm sayıları ekrana çıkaran Python kodunu yazınız.

**Cevap:**

```python
#3 basamaklı sayılar 100 ile 999 arasıdır
#kural: ilk rakam + son rakam > ortadaki rakam olcak

print("Kurala uyan 3 basamaklı sayılar:")

for sayi in range(100, 1000): #100 den 999 a kadar tum 3 basamaklıları gezer
    #basamakları buluyoruz
    yuzler = sayi // 100 #ilk rakamı verir (yuzler basamagı)
    onlar = (sayi // 10) % 10 #ortadaki rakamı verir (onlar basamagı)
    birler = sayi % 10 #son rakamı verir (birler basamagı)
    
    #ilk ve son rakamın toplamı ortadakinden buyuk mu diye bakarız
    if (yuzler + birler) > onlar:
        print(sayi, end=" ") #yanyana yazdırsın diye end="" oto \n koymasın diye

print() #en son alt satıra gecmek icin bos print (\n işlevi gördü)
```

## Soru 4

```python
fiyat{'muz': 4, 'elma': 2, 'portakal': 1.5, 'armut': 3}
stok{'muz': 6, 'elma': 8, 'portakal': 32, 'armut': 15}
```

Yukarıda 2 tane sözlük verilmiştir. Fiyat sözlüğü meyvelerin fiyat bilgisini tutarken, stok hangi meyveden kaç tane olduğu bilgisini tutmaktadır. 3 müşterinin olduğu ve her bir müşterinin istediği miktarda meyve satın alacağı bir python programı yazınız. Her müşterinin satın alımından sonra o meyveye ait stok azaltılmalıdır. Her satın alım sonunda müşteriye toplam alışveriş fiyatı çıktı olarak gösterilmelidir.

**Not:** Meyvelerde stok kalmadı ise “Stok bitmiştir.” uyarısı vermeli.

**Cevap:**

```python
#soruda verilen sözlükleri girme
fiyat = {'muz': 4, 'elma': 2, 'portakal': 1.5, 'armut': 3}
stok = {'muz': 6, 'elma': 8, 'portakal': 32, 'armut': 15}

#3 musteri oldugundan 1 den 3 e kadar donen for dongusu
for musteri in range(1, 4):
    print("\n--- " + str(musteri) + ". Müşteri ---")
    toplam_tutar = 0 #bu musterinin odeyecegi toplam tutarı tutcak degisken
    
    while True: #musteri alısverisi bitirene kadar döner
        meyve = input("Almak istediginiz meyve (bitirmek icin 'bitti' yazın): ")
        
        if meyve == "bitti": #musteri alısverisi bitirmek isterse dönguden cık
            break
            
        if meyve not in fiyat: #manavda olmayan meyve girildiginde uyar
            print("Bu meyve bulunmamaktadır!")
            continue #basa sarar
            
        if stok[meyve] <= 0: #meyvenin stogu kalmamıssa uyarı verir
            print("Stok bitmiştir.")
            continue
            
        miktar = int(input("Kaç adet " + meyve + " istiyorsunuz? (kalan stok: " + str(stok[meyve]) + "): "))
        
        if miktar <= 0: #hatalı sayı girildiginde uyar
            print("Gecersiz miktar girdiniz.")
            continue
            
        if miktar > stok[meyve]: #istenen miktar mevcut stoktan fazlaysa uyar
            print("Yeterli stok yok! En fazla " + str(stok[meyve]) + " adet alabilirsiniz.")
        else: #stok yetiyorsa satısı yap
            stok[meyve] -= miktar #meyvenin stogunu azalt
            tutar = miktar * fiyat[meyve] #bu alımın fiyatını hesapla
            toplam_tutar += tutar #musterinin toplamına ekle
            print(str(miktar) + " adet " + meyve + " alındı. Kalan stok: " + str(stok[meyve]))
            
            #satın alım sonrası stok 0 olduysa stok bitti uyarısı verir
            if stok[meyve] == 0:
                print("Stok bitmiştir.")

    #her satın alım sonunda musteriye toplam alısveris fiyatını yazdır
    print(str(musteri) + ". Müşteri toplam alışveriş fiyatı: " + str(toplam_tutar))

#son kalan stok durumunu yazdır
print("\nSon kalan stoklar:", stok)
```

## Soru 5

```python
yazi= ["Ahmet", "altı", "yaşında", "zeynep", "dört", "yaşında", "esra", "iki", "yaşında", "ayşe", "bir", "yaşında"]
```

Output = “Ahmet 6 yaşında zeynep 4 yaşında esra 2 yaşında ayşe 1 yaşında”

Yukarıda yazi adında bir string dizisi verilmiştir. Verilen stringdeki sayıları rakamla yazılmasını sağlayacak python kodunu yazınız.

**Not:** Hazır kütüphane ya da fonksiyon kullanılmamalıdır.  
**İpucu:** Sözlük yapısını kullanabilirsiniz.

**Cevap:**

```python
#soruda verilen listeyi oluşturma
yazi = ["Ahmet", "altı", "yaşında", "zeynep", "dört", "yaşında", "esra", "iki", "yaşında", "ayşe", "bir", "yaşında"]

#sayıların rakam karsılıklarını tutan sozluk olusturma
sozluk = {
    "sıfır": "0",
    "bir": "1",
    "iki": "2",
    "üç": "3",
    "dört": "4",
    "beş": "5",
    "altı": "6",
    "yedi": "7",
    "sekiz": "8",
    "dokuz": "9"
}

output = "" #hazır fonksiyon olmadan stringleri birlestirecegimiz bos degisken

#listedeki her kelimeye tek tek bakıyoruz
for kelime in yazi:
    #kelime sozlukte var mı (yani sayı ismi mi) bakarız
    if kelime in sozluk:
        ekle = sozluk[kelime] #sozlukteki rakam halini alıyoruz
    else:
        ekle = kelime #sayı degilse direk kelimeyi alıyoruz
        
    #hazır fonksiyon (join fln) kullanmadan kelimeleri birlestirme
    if output == "":
        output = ekle #ilk kelimeyse direk eklenir
    else:
        output = output + " " + ekle #araya bosluk koyup ekliyoruz

#cıktıyı yazdırma
print('Output = "' + output + '"')
```

## Soru 6

Kullanıcının gireceği derece(c ) değerine karşılık fahrenhait değerini hesaplayan python kodunu yazınız. `[f = 32+(c*1.8)]`

**Cevap:**

```python
#kullanıcıdan derece c degerini alıyoruz
c = float(input("Derece (c) değerini giriniz: "))

#soruda verilen fahrenheit formulu: f = 32+(c*1.8)
f = 32 + (c * 1.8) #formul uygulanır

#hesaplanan fahrenheit degeri yazdırılır
print("Fahrenheit değeri:", f)
```

## Soru 7

Vize1-> %20, Vize2->%20, Final %60. Kullanıcıdan isim ve not girişinden sonra, yanda verilen değerleri de göz önünde bulundurarak ortalamasını hesaplayıp” ad-soyad ortalaması:z” sonucunu verecek kodu yazınız.

**Cevap:**

```python
#kullanıcıdan isim ve sınav notlarını alıyoruz
ad_soyad = input("Ad soyad giriniz: ")
vize1 = float(input("Vize 1 notunu giriniz: "))
vize2 = float(input("Vize 2 notunu giriniz: "))
final = float(input("Final notunu giriniz: "))

#vize1 %20, vize2 %20, final %60 etkili ortalama hesabı
#yuzdeleri carpıp topluyoruz
ortalama = (vize1 * 0.20) + (vize2 * 0.20) + (final * 0.60)

#ad-soyad ortalaması:z seklinde cıktı yazdırma
print(ad_soyad + " ortalaması:" + str(ortalama))
```

## Soru 8

Bir önceki sorunun sonuçlarını kullanarak ortalaması 30 ve altı olan kişiler için “Kaldı!”, 31 ve 69 olanlar için “Kritik!”, 70’in üzerinde olanlar için “Geçti!” mesajlarını ekrana çıkartan kodu yazınız.

**Cevap:**

```python
#kullanıcıdan bilgileri ve notları alıyoruz (önceki sorudaki gibi)
ad_soyad = input("Ad soyad giriniz: ")
vize1 = float(input("Vize 1 notunu giriniz: "))
vize2 = float(input("Vize 2 notunu giriniz: "))
final = float(input("Final notunu giriniz: "))

#ortalama hesabı vize1 %20 vize2 %20 final %60
ortalama = (vize1 * 0.20) + (vize2 * 0.20) + (final * 0.60)

print(ad_soyad + " ortalaması:" + str(ortalama))

#ortalamaya gore durum kosulları
if ortalama <= 30: #30 ve altı ise kaldı
    print("Kaldı!")
elif ortalama <= 69: #31 ve 69 arası ise kritik
    print("Kritik!")
else: #70 uzerinde ise gecti
    print("Geçti!")
```

---

# ÖDEV 4

**Verilen Tarih:** 3.11.2026  
**Son Teslim Tarihi:** 9.11.2026 - 23:59

## Soru 1

3 ayrı kullanıcı için yaş hesaplama fonksiyonu oluşturunuz. Doğum yılını ve emeklilik yaşını girmesini isteyiniz. Ardından bu bilgilere dayalı olarak emeklilik yılını hesaplayın ve kullanıcıya bir mesaj döndürün. Eğer kişi zaten emekliyse veya emekliliği geçtiyse, buna dair bir mesaj yazdırın. Tüm işlevleri içeren modülü yazınız.

**Cevap:**

```python
#yaş ve emeklilik hesaplayan fonksiyon
def yas_hesapla(dogum_yili, emeklilik_yasi):
    yas = 2026 - dogum_yili #2026 yılından doğum yılını çıkarıp yaşı buluyoruz
    emeklilik_yili = dogum_yili + emeklilik_yasi #doğum yılı ile emeklilik yaşını toplayıp emekli olacağı yılı buluyoruz

    if emeklilik_yili > 2026: #eğer emeklilik yılı 2026 dan büyükse daha emekli olmamıştır
        kalan = emeklilik_yili - 2026 #emekliliğe kaç yıl kaldığını buluyoruz
        print("Yaşınız:", yas, ", Emeklilik yılınız:", emeklilik_yili, ", Emekliliğe", kalan, "yıl kaldı.")
    elif emeklilik_yili == 2026: #emeklilik yılı 2026 ise bu yıl emekli oluyordur
        print("Yaşınız:", yas, ", Emeklilik yılınız:", emeklilik_yili, ", Bu yıl emekli oluyorsunuz.")
    else: #emeklilik yılı 2026 dan küçükse zaten emekli olmuştur
        gecen = 2026 - emeklilik_yili #kaç yıl önce emekli olduğunu buluyoruz
        print("Yaşınız:", yas, ", Zaten", emeklilik_yili, "yılında emekli oldunuz.", gecen, "yıldır emeklisiniz.")


#3 ayrı kullanıcı için döngü
for i in range(1, 4): #1 den 3 e kadar 3 kullanıcı için dönecek
    print(i, ". kullanıcı")
    dogum = int(input("Doğum yılınızı giriniz: ")) #kullanıcıdan doğum yılını alıyoruz
    emeklilik = int(input("Emeklilik yaşınızı giriniz: ")) #kullanıcıdan emeklilik yaşını alıyoruz

    yas_hesapla(dogum, emeklilik) #fonksiyonu çağırıyoruz
    print() #alt satıra geçmek için print
```

## Soru 2

“Hava kirliliği, dünya genelinde büyük bir çevresel sorun olarak karşımıza çıkmaktadır. Hava kirliliği, atmosferdeki zararlı gazlar, kimyasallar, tozlar ve partiküllerin yüksek seviyelerde bulunması sonucu ortaya çıkar. Bu kirleticiler, sanayi tesisleri, araç emisyonları, enerji üretimi ve tarım gibi kaynaklardan atmosfere salınır. Hava kirliliği, ciddi sağlık sorunlarına yol açabilir ve doğal ekosistemlere zarar verebilir.

Hava kirliliği, insan sağlığına bir dizi olumsuz etki yapar. Kirli hava solumak, solunum yolu hastalıklarının, kalp hastalıklarının, kanser riskinin artmasına ve genel yaşam kalitesinin düşmesine neden olabilir. Ayrıca, çocuklar, yaşlılar ve kronik sağlık sorunları olanlar, hava kirliliğinin etkilerine daha fazla maruz kalabilirler.

Hava kirliliği aynı zamanda ekosistemlere zarar verir. Bitkiler, hayvanlar ve su kaynakları üzerinde olumsuz etkiler yaratabilir, biyolojik çeşitliliği azaltabilir ve tarım verimliliğini etkileyebilir.

Bu sorunun çözümü için dünya genelinde çevresel düzenlemeler ve temiz enerji kaynaklarına geçiş gibi adımlar atılmaktadır. Ayrıca, bireysel olarak daha çevre dostu seçimler yaparak da hava kirliliğinin azaltılmasına katkı sağlayabiliriz. Hava kirliliği ile mücadele, hem insan sağlığını hem de gezegenimizin geleceğini korumak için önemlidir.”

Yukarıdaki metinde “hava” kelimesinin kaç defa geçtiğini hesaplayan modülü yazınız.

**Cevap:**

```python
#soruda verilen metin, biraz uzun
metin = "Hava kirliliği, dünya genelinde büyük bir çevresel sorun olarak karşımıza çıkmaktadır. Hava kirliliği, atmosferdeki zararlı gazlar, kimyasallar, tozlar ve partiküllerin yüksek seviyelerde bulunması sonucu ortaya çıkar. Bu kirleticiler, sanayi tesisleri, araç emisyonları, enerji üretimi ve tarım gibi kaynaklardan atmosfere salınır. Hava kirliliği, ciddi sağlık sorunlarına yol açabilir ve doğal ekosistemlere zarar verebilir. Hava kirliliği, insan sağlığına bir dizi olumsuz etki yapar. Kirli hava solumak, solunum yolu hastalıklarının, kalp hastalıklarının, kanser riskinin artmasına ve genel yaşam kalitesinin düşmesine neden olabilir. Ayrıca, çocuklar, yaşlılar ve kronik sağlık sorunları olanlar, hava kirliliğinin etkilerine daha fazla maruz kalabilirler. Hava kirliliği aynı zamanda ekosistemlere zarar verir. Bitkiler, hayvanlar ve su kaynakları üzerinde olumsuz etkiler yaratabilir, biyolojik çeşitliliği azaltabilir ve tarım verimliliğini etkileyebilir. Bu sorunun çözümü için dünya genelinde çevresel düzenlemeler ve temiz enerji kaynaklarına geçiş gibi adımlar atılmaktadır. Ayrıca, bireysel olarak daha çevre dostu seçimler yaparak da hava kirliliğinin azaltılmasına katkı sağlayabiliriz. Hava kirliliği ile mücadele, hem insan sağlığını hem de gezegenimizin geleceğini korumak için önemlidir."

#hava kelimesini sayan fonksiyon
def hava_say(yazi):
    yazi = yazi.lower() #büyük küçük harf ikisini de algılasın diye bütün harfleri küçültüyoruz
    sayac = yazi.count("hava") #metinde kaç tane hava kelimesi geçtiğini sayıyoruz

    print("Metinde hava kelimesi", sayac, "defa geçiyor.")


#fonksiyonu çağırma
hava_say(metin)
```

## Soru 3

```python
matrix= [ [1, 2, 3],
          [4, 5, 6],
          [7, 8, 9] ]
```

Yukarıda verilen 3x3 boyutlu matrisin determinantını hesaplayan modülü yazınız.

**Cevap:**

```python
#soruda verilen 3x3 matris
matrix = [ [1, 2, 3],
           [4, 5, 6],
           [7, 8, 9] ]

#determinant hesaplayan fonksiyon
def determinant_hesapla(m):
    #1. satır elemanları
    a = m[0][0]
    b = m[0][1]
    c = m[0][2]

    #2. satır elemanları
    d = m[1][0]
    e = m[1][1]
    f = m[1][2]

    #3. satır elemanları
    g = m[2][0]
    h = m[2][1]
    i = m[2][2]

    #3x3 matris determinant formülü
    det = a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)
    print("Matrisin determinantı:", det)


#fonksiyonu çağırma
determinant_hesapla(matrix)
```

## Soru 4

Kullanıcının “enter” e basıncaya dek girdiği metin içerisinde alfabenin her harfinin kaç kez bulunduğunu bulan (büyük ve küçük harfleri beraber sayın) python kodunu modül kullanarak yazınız.

**Not:** Bu sorunuzda hazır fonksiyon kullanmayınız. Sadece `lower()` ve `len()` kullanabilirsiniz.

**Cevap:**

```python
alfabe = "abcçdefgğhıijklmnoöprsştuüvyz" #kontrol için alfabe dizisi

#harfleri sayan fonksiyon
def harf_say(metin):
    metin = metin.lower() #büyük küçük harfleri beraber saymak için küçültüyoruz

    for i in range(len(alfabe)): #alfabedeki harf sayısı kadar döngü
        harf = alfabe[i] #şu an baktığımız harfi alıyoruz
        sayac = 0 #harften kaç tane olduğunu tutacak sayaç

        for j in range(len(metin)): #metindeki karakter sayısı kadar döngü
            if metin[j] == harf: #metindeki harf alfabedeki harfle aynıysa
                sayac += 1 #sayacı 1 arttır

        print(harf, "harfi:", sayac)


#kullanıcıdan enter'a basana kadar metin alıyoruz
yazi = input("Metni giriniz: ")

#fonksiyonu çağırma
harf_say(yazi)
```

## Soru 5

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

**Cevap:**

```python
#Adım 1: şehirlerin ülke ve kıta bilgilerini tutan sözlük
sehirler_sozlugu = {
    'İstanbul': {'ülke': 'Turkey', 'kıta': 'Europe'},
    'Tokyo': {'ülke': 'Japan', 'kıta': 'Asia'},
    'New_york': {'ülke': 'United States', 'kıta': 'North America'},
    'Mumbai': {'ülke': 'India', 'kıta': 'Asia'},
    'Cairo': {'ülke': 'Egypt', 'kıta': 'Africa'},
    'Seoul': {'ülke': 'South Korea', 'kıta': 'Asia'},
    'London': {'ülke': 'United Kingdom', 'kıta': 'Europe'}
}

#Adım 2: şehirleri kıtalara göre gruplayan fonksiyon
def sehirleri_kitalara_göre_grupla(sehirler):
    gruplar = {} #kıtaları tutacak boş sözlük

    for sehir in sehirler: #sözlükteki her şehre bakıyoruz
        kita = sehirler[sehir]['kıta'] #şehrin kıtasını alıyoruz
        ulke = sehirler[sehir]['ülke'] #şehrin ülkesini alıyoruz

        if kita not in gruplar: #eğer kıta sözlükte yoksa
            gruplar[kita] = [] #o kıta için boş liste açıyoruz

        gruplar[kita].append(sehir + " (" + ulke + ")") #şehri ve ülkesini o kıtanın listesine ekliyoruz

    return gruplar


#fonksiyonu çağırıyoruz
sonuc = sehirleri_kitalara_göre_grupla(sehirler_sozlugu)

#Adım 3: gruplanmış şehirleri ekrana yazdırma
for kita in sonuc:
    print(kita, ":", sonuc[kita])
```

## Soru 6

İki tarih arasındaki gün ve hafta sayısını hesaplayan kodu yazınız. Kodunuz `'gun_sayisi_hesapla'` fonksiyonu ve `'hafta_sayisi_hesapla'` fonksiyonu içermelidir. Kodunuzda `tarih1` ve `tarih2` parametreleri, `"YYYY-MM-DD"` formatında olmalıdır. Kodlarınızı modül kullanarak yazınız.

**Not:** Bu soru için `datetime()` kullanmayınız.

**Cevap:**

```python
#iki tarih arasındaki gün sayısını hesaplayan fonksiyon
def gun_sayisi_hesapla(tarih1, tarih2):
    #1. tarihi - işaretinden bölüp yıl, ay, gün olarak alıyoruz
    t1 = tarih1.split("-")
    yil1 = int(t1[0])
    ay1 = int(t1[1])
    gun1 = int(t1[2])

    #2. tarihi - işaretinden bölüp yıl, ay, gün olarak alıyoruz
    t2 = tarih2.split("-")
    yil2 = int(t2[0])
    ay2 = int(t2[1])
    gun2 = int(t2[2])

    #tarihleri toplam güne çeviriyoruz (1 yıl 365 gün, 1 ay 30 gün)
    toplam1 = yil1 * 365 + ay1 * 30 + gun1
    toplam2 = yil2 * 365 + ay2 * 30 + gun2

    fark = toplam2 - toplam1 #iki tarih arasındaki gün farkı
    if fark < 0: #eğer fark eksi çıkarsa artıya çeviriyoruz (mutlak değer alıyoruz gibi)
        fark = fark * -1

    return fark

#iki tarih arasındaki hafta sayısını hesaplayan fonksiyon
def hafta_sayisi_hesapla(tarih1, tarih2):
    gun = gun_sayisi_hesapla(tarih1, tarih2) #önce gün sayısını buluyoruz
    hafta = gun // 7 #gün sayısını 7 ye bölerek hafta sayısını buluyoruz
    return hafta


#kullanıcıdan tarihleri alma
tarih1 = input("1. tarihi giriniz (YYYY-MM-DD): ")
tarih2 = input("2. tarihi giriniz (YYYY-MM-DD): ")

print("Gün sayısı:", gun_sayisi_hesapla(tarih1, tarih2))
print("Hafta sayısı:", hafta_sayisi_hesapla(tarih1, tarih2))
```

## Soru 7

İki tane liste oluşturunuz. Bu listeleriniz 10’ar elemanlı olsun ve random değerler atayınız. Ardından bu iki listeyi birleştirip sıralanmış halini ekrana bastıran python kodunu modül kullanarak yazınız.

**Not:** Bu sorunuzda **sıralama** ile ilgili hazır hiçbir fonksiyon kullanmayınız.

**Cevap:**

```python
import random

#rastgele doldurulacak 2 boş dizi oluşturuyoruz
dizi1 = []
dizi2 = []

#dizi boyutunu 10 yaptık. her 10 alana 1-100 arası sayı atadık her dizi için
for i in range(10):
    dizi1.append(random.randint(1, 100))
    dizi2.append(random.randint(1, 100))

birlesik = dizi1 + dizi2 #dizileri birleştirme

#diziyi küçükten büyüğe sıralayan fonksiyon
def sirala(dizi):
    uzunluk = len(dizi) #dizinin uzunluğu

    #the sort of bubble (bubble sort)
    for i in range(uzunluk - 1):
        for j in range(uzunluk - 1 - i):
            if dizi[j] > dizi[j + 1]: 
                gecici = dizi[j] 
                dizi[j] = dizi[j + 1] 
                dizi[j + 1] = gecici 

    print("Sıralanmış dizi:", dizi)


#sıralama fonksiyonunu çağırma
sirala(birlesik)
```

## Soru 8

`L = [1, 2, 2, 3, 3, 4, 4, 5, 6, 7, 7, 8]` Verilen 12 elemanlı listeyi kullanarak bu listenin 2 ve 3 elemanlı alt kümeleri çıkarınız. Bu alt kümelerde benzer olanları ekrana yazdırınız.

**Cevap:**

```python
L = [1, 2, 2, 3, 3, 4, 4, 5, 6, 7, 7, 8] #soruda verilen 12 elemanlı liste
uzunluk = 12 #dizi uzunluğu

#2 ve 3 elemanlı alt kümeleri bulup benzer olanları yazdıran fonksiyon
def alt_kumeler(liste):
    ikililer = [] #2 elemanlı alt kümeleri koyacağımız dizi
    ucluler = [] #3 elemanlı alt kümeleri koyacağımız dizi

    #2 elemanlı alt kümeleri çıkarma
    for i in range(uzunluk):
        for j in range(i + 1, uzunluk): #aynı elemanı bida almamak için i+1 den başlatıyoruz
            ikililer.append([liste[i], liste[j]])

    #3 elemanlı alt kümeleri çıkarma
    for i in range(uzunluk):
        for j in range(i + 1, uzunluk):
            for k in range(j + 1, uzunluk):
                ucluler.append([liste[i], liste[j], liste[k]])

    #2 elemanlılarda benzer (birden fazla olan) kümeleri bulma
    benzer_ikili = []
    for kume in ikililer:
        if ikililer.count(kume) > 1 and kume not in benzer_ikili: #birden fazla varsa ve diziye eklemediysek
            benzer_ikili.append(kume)

    #3 elemanlılarda benzer (birden fazla olan) kümeleri bulma
    benzer_uclu = []
    for kume in ucluler:
        if ucluler.count(kume) > 1 and kume not in benzer_uclu: #birden fazla varsa ve diziye eklemediysek
            benzer_uclu.append(kume)

    #benzer alt kümeleri yazdırma
    print("2 elemanlı benzer alt kümeler:", benzer_ikili)
    print("3 elemanlı benzer alt kümeler:", benzer_uclu)


#fonksiyonu çağırma
alt_kumeler(L)
```

