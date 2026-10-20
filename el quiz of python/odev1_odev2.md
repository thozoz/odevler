# ÖDEV 1

**Son Teslim Tarihi:** 13.10.2026 - 23:59

## Soru 1

Kullanıcı tarafından girilen **iki basamaklı iki farklı sayının** ortak rakamlarını bulan bir Python programı yazınız. Sayıların birler ve onlar basamaklarını ayrı ayrı belirleyiniz. İki sayıda ortak bulunan rakamları ekrana yazdırınız. Eğer ortak rakam yoksa **"Ortak rakam yoktur."** mesajını gösteriniz.

**Cevap:**

```python
#ortak rakam varsa true yapılacak değişken
ortak=False

#kullanıcıdan 2 basamaklı sayılar alıyoruz
sayi1=int(input("1. sayıyı giriniz: "))
sayi2=int(input("2. sayıyı giriniz: "))

#sayı 1 birler ve onlar basamagı alma

sayi1b=sayi1%10 #birler basamagı

sayi1o=sayi1//10 #onlar basamagı


#sayı 2 birler ve onlar basamagı alma

sayi2b=sayi2%10 #birler basamagı

sayi2o=sayi2//10 #onlar basamagı


#karşılaştırma
if sayi1o==sayi2o or sayi1o==sayi2b: 
    print("Ortak rakam "+ str(sayi1o) + "")
    ortak=True

if (sayi1b==sayi2o or sayi1b==sayi2b) and sayi1b != sayi1o: #sayi1b != sayi1o mi diye bakarak aynı ortak rakam bida yazdırılmasın yapıyoruz
    print("Ortak rakam "+ str(sayi1b) + "")
    ortak=True  

#ortak rakam yoksa
if ortak==False:
    print("Ortak rakam yoktur")
```

## Soru 2

Kullanıcıdan bir N sayısı alan ve bu sayı kadar yıldızı (\*) **yan yana** ekrana yazdıran Python programını yazınız.

**Cevap:**

```python
yildiz=int(input("Yıldız sayısını giriniz: "))

for i in range(yildiz): #bu döngü yildiz değişkeni kadar çalışacak
    print("*", end="") #end="" parametresi print fonksiyonunun otomatik sona koydugu \n i koymamasını ve otomatik alt satıra geçmemesini sağlar. böylece yıldızlar yanyana olur
```

## Soru 3

Kullanıcıdan karenin kenar uzunluğunu alan ve girilen kenar uzunluğuna göre yıldızlardan oluşan **içi dolu bir kare** çizen Python programını yazınız.

**Cevap:**

```python
kare=int(input("Kare kenar uzunluğunu giriniz: "))

for i in range(kare): #bu döngü dikeye yıldız koyduran döngü

    for j in range(kare): #bu döngü yataya kare değişkeni kadar yıldız koyduruyo
        print("*", end="") #end parametresi 2. sorudaki işlevini sürdürüyor. bu print yatay yıldızları koyan print fonksiyonu

    print() #yataya koyulan yıldızlardan sonra \n ile alt line a geçsin diye koyulan print, olmazsa butun yıldızlar yanyana olur
```

## Soru 4

Kullanıcıdan kaç adet sayı gireceğini öğrenen ve daha sonra kullanıcının girdiği sayıların **aritmetik ortalamasını** hesaplayarak ekrana yazdıran Python programını yazınız.

**Cevap:**

```python
#kullanıcının kaç sayı girceğini kullanıcıdan alma
say=int(input("Kaç sayı girilecek: "))

toplam=0 #aritmetik hesaplamak için girilen sayıların toplamını tutacak değişken

for i in range(1,say+1): #kullanıcının istediği kadar sayıyı alma döngüsü

    sayi=int(input(str(i)+". sayıyı gir: ")) #kullanıcıdan aritmetiği hesaplanacak sayıları alma
    toplam+=sayi #kullanıcıdan alınan sayıları toplama


print("Aritmetik ortalamaları: "+ str(toplam/say)) #aritmetik ortalamanın hesaplanıp yazdırılması
```

## Soru 5

Kullanıcıdan bir N sayısı alan ve **100 ile 999 arasındaki**, N sayısına tam bölünebilen tüm sayıları ekrana yazdıran Python programını yazınız.

- Bu soruda döngü olarak **while** kullanılmalıdır.

**Cevap:**

```python
sayi=int(input("Sayi giriniz: "))
a=100


while a<1000: #a değişkenini 100 den 999'a kadar yükselten while döngüsü

    if a%sayi==0: #tam bölünüyorsa kontrolü, bölünürse kalan 0 olur (% kalan verir)
        print(str(a)+" sayısı "+str(sayi)+" sayısına tam bölünür!")

    a=a+1
```

## Soru 6

Kullanıcıdan sürekli olarak sayılar alan ve kullanıcı **0** girene kadar girilen tüm sayıların toplamını hesaplayan Python programını yazınız.

**Cevap:**

```python
i=1 #kaçıncı sayı giriliyo tutmak için
toplam=0 #girilen sayıların toplamını tutacak değişken

while True: #kullanıcı 0 girene kadar sayı alma döngüsü

    sayi=int(input(str(i)+". sayıyı gir: ")) #kullanıcıdan toplamı hesaplanacak sayıları alma
    if sayi==0: break
    toplam+=sayi #kullanıcıdan alınan sayıları toplama
    i+=1 


print("Sayı toplamları: "+ str(toplam)) #sayıların toplamının yazdırılması
```

## Soru 7

Kullanıcıdan bir noktanın koordinatlarını **P(x, y)** ve doğrunun denklemini oluşturan katsayıları **m** ve **n** değerlerini alınız. Bu bilgilere göre noktanın **y = m·x + n** doğrusu **üzerinde olup olmadığını** kontrol eden bir **Python programı** yazınız. Bir nokta, doğrunun üzerinde ise denklem sağlanır: y=m×x+n. Bu eşitlik doğruysa nokta doğrunun üzerindedir, yanlışsa değildir.

**Cevap:**

```python
# kullanıcıdan nokta koordinatlarını alma
x = float(input("x koordinatını giriniz: "))
y = float(input("y koordinatını giriniz: "))

# kullanıcıdan doğru katsayılarını al y = m*x + n formülü için
m = float(input("m katsayısını giriniz: "))
n = float(input("n katsayısını giriniz: "))

#kullanıcının girdiği koordinatlar doğru üzerinde mi kontrolü
if y == (m * x + n): # y = m*x + n formülünden doğru üzerinde mi bakarız
    print("Nokta doğrunun üzerindedir.")
else:
    print("Nokta doğrunun üzerinde değildir.")
```

## Soru 8

Kullanıcıdan **iki basamaklı bir sayı** alınız. Program, bu sayının **rakamları toplamını** bulacaktır. Eğer kullanıcı **10'dan küçük veya 99'dan büyük** bir sayı girerse, ekrana **"Hatalı işlem!"** uyarısı verilecektir.

**Cevap:**

```python
#kullanıcıdan 2 basamaklı sayı alıyoruz
sayi=int(input("İki basamaklı sayı giriniz: "))

toplam=0 #toplamı tutacak değişken

if sayi<=99 and sayi>=10: #sayı 2 basamaklı mı yani 99 ile 10 arasında mı kontrolu (99 ve 10 dahil)

    #eğer 2 basamaklıysa rakamlar toplamı hesaplanır
    toplam=(sayi%10)+(sayi//10) #sayi%10 ile birler basamağı alınır, sayi//10 ile onlar basamağı alınır

    print("Sayı rakamlar toplamı: " +str(toplam)) #toplam yazdırma

else: #2 basamaklı değil, uyarı mesajı ver
   print("Hatalı işlem!") 
```

---

# ÖDEV 2

**Verilen Tarih:** 13.10.2026

**Son Teslim Tarihi:** 20.10.2026 - 23:59

## Soru 1

İki rastgele dizi (elemanları 1-50 arası) oluşturun. Dizileri birleştirin, ardından ortak elemanları çıkarın ve son olarak bir birleştirilmiş ve ortak elemanları çıkarılmış diziyi küçükten büyüğe sıralayın.

Not: Hazır fonksiyon ya da kütüphane kullanılmamalıdır. Yalnızca `append()` kullanılabilir.

**Cevap:**

```python
import random

#rastgele doldurulacak 2 boş dizi oluşturuyoruz
dizi1 = []
dizi2 = []

#dizi boyutunu 5 yaptık. her 5 alana 1-50 arası sayı atadık her dizi için
for i in range(5):
    dizi1.append(random.randint(1, 50))
    dizi2.append(random.randint(1, 50))

print("1. dizi:", dizi1)
print("2. dizi:", dizi2)

#dizilerde bulunan ortak elemanları koyacağımız dizi
ortaklar = []

for eleman in dizi1: #dizi 1 deki her eleman için
    if eleman in dizi2 and eleman not in ortaklar:#eğer o elemandaki sayı dizi2 de de varsa ve ortaklar dizisinde yoksa
        #bu sayı ortak elemandır (hem dizi1 hem dizi2 de var)
        ortaklar.append(eleman) # o sayıyı ortaklar dizisinin son indexine ekle

print("Ortak elemanlar:", ortaklar)

birlesik = dizi1 + dizi2 #dizileri birleştirme

son_dizi = []#birleşmiş ve ortak elemanları çıkmış dizi yapacağız bu diziyi
son_uzunluk = 0 #son_dizi nin uzunluğunu tutan değişken

for eleman in birlesik: #birleşmiş dizilerdeki elemanlarda
    if eleman not in ortaklar: #eğer dizideki eleman ortaklar dizisinde yoksa ortak eleman değildir. son_dizi ye ekleyebiliriz
        son_dizi.append(eleman) #ortak olmayan elemanı son diziye ekleriz
        son_uzunluk += 1 #dizi uzunluk sayacını 1 arttırırız

print("Birleşmiş dizi:", birlesik)
print("Ortaklar çıkarılmış dizi:", son_dizi)


#diziyi küçükten büyüğe sıralama
#bubble sort ile
for i in range (son_uzunluk - 1):

    for j in range (son_uzunluk - 1-i):

        if son_dizi[j] > son_dizi[j + 1]: #soldaki sayı sağdakinden büyükse yer değiştir (swap)

            gecici = son_dizi[j] #soldaki sayıyı geçici değişkene al
            son_dizi[j] = son_dizi[j + 1] #sağdaki sayıyı sola aktar
            son_dizi[j + 1] = gecici #geçicideki eski sol sayıyı sağa aktar


#son küçükten büyüğe sıralanmış dizi yazdırılır
print("Sıralanmış dizi:", son_dizi)
```

## Soru 2

`Liste=[1,2,3,3,4,6,8,9,8,1,2,5,4,3]`

Yukarıda verilen listedeki tekrar eden elemanları bulup silen python programını yazınız. Silmeden önce o elemandan kaç tane bulunduğu bilgisi de çıktı olarak verilmelidir.

Not: Hazır fonksiyon kullanılmamalıdır. Yalnızca `list.count` kullanılabilir.

**Cevap:**

```python
Liste = [1,2,3,3,4,6,8,9,8,1,2,5,4,3] #soruda verilen liste

uzunluk = 14 #dizi uzunluğu

i = 0
while i < uzunluk: #while ile döng. for kullanmama nedenizim döngünüün uzunluk değiştikce değişmesi için
    eleman = Liste[i] #şuan baktığımız index teki elemanı eleman değişkenine atıyoruz
    adet = Liste.count(eleman) #eleman değişkeninden Liste dizisinde kaç tane var bakıyoruz ve adet değişkenine atıyoruz

    if adet > 1: #eğer adet 1 den fazlaysa o eleman tekrar eden elemandır
        print(eleman, "elemanından", adet, "tane bulundu.") #dizide bu elemandan kaç tane olduğunu yazdırıyoruz

        j = uzunluk - 1 #uzunluk-1 ile son elemandan başlıyoruz ve tekrar ettiğini farkettiğimiz sayıya doğru ilerliyoruz ters olarak

        while j > i: #ilk buldugumuz sayıyı silmiyoruz. ondan sonra gelen tekrar edenleri silceğimiz için j>i yapıyoruz
            if Liste[j] == eleman: #tersten giderken eğer tekrar eden elemanın olduğu indexi bulursak
                del Liste[j] #o indexi siliyoruz
                uzunluk -= 1 #index silindiğinden uzunluk 1 azalıyor

            j -= 1 #liste de ters gitmeye devam ediyoruz indexleri sıra sıra

    i += 1

#tekrar eden elemanların silinmiş halini yazdırıyoruz
print("Tekrarlardan arındırılmış liste:", Liste)
```

## Soru 3

Bir listede herhangi bir sayının en uzun artan ardışık alt dizisini (sublist) bulan kodu yazın. Örneğin, `[1, 2, 3, 1, 2, 3, 4, 5, 6, 5, 6, 7, 8]` listesi verildiğinde, işlev en uzun artan ardışık alt diziyi `[1, 2, 3, 4, 5, 6]` döndürmelidir.

Not: Hazır kütüphane ya da fonksiyon kullanılmamalıdır.

**Cevap:**

```python
liste = [1,2,3,1,2,3,4,5,6,5,6,7,8] #soruda verilen örnek liste

gecici = [liste[0]] #o an taranan aktif ardışık alt diziyi tutacak değişken
en_uzun = [] #en uzun artan ardışık alt diziyi tutacak değişken

sayi = 1 #gecici dizisinin eleman sayısını sayan değişken
en_sayi = 0 #en uzun dizinin eleman sayısı (rekor)

for i in range(1, 13):
    if liste[i] == liste[i - 1] + 1: #ardışık artan mı kontrol ediyor
        gecici = gecici + [liste[i]] #ardışıksa gecici dizisinin sonunda liste[i] sayısını ekler. gecici.append(liste[i]) ile aynı işlev 
        sayi += 1 #gecici dizisinin eleman sayısını 1 arttırıyoruz (liste[i] eklediğimizden sonunda)

    else: #ardışık olmayı kesince
        if sayi > en_sayi: #eğer bu yeni ardışık alt dizi daha uzunsa eski en uzundan
            en_uzun = gecici #yeni en uzun ardışık alt diziyi tanımlıyoruz
            en_sayi = sayi #yeni en uzun ardışık alt dizinin eleman sayısını tanımlıyoruz

        gecici = [liste[i]] #gecici yi kaldığımız yere aldık
        sayi = 1 #gecici dizisi eleman sayısı 1 e geri döndü onu atıyoruz
 
#eğer ardışık alt dizi en son diziyse hiç ardışık olmayı kesmeyeceğinden else: içine girmez. ondan bu kodla onu alırız else e girmese de
if sayi > en_sayi: 
    en_uzun = gecici

#en uzun artan ardışık alt diziyi yazdırma
print("En uzun artan ardışık alt dizi:", en_uzun)
```

## Soru 4

Bir dizideki benzersiz elemanları (tekrar etmeyen elemanları) yeni bir listeye ekleyen programı yazınız. Örneğin; `[2, 2, 3, 3, 8, 8, 9, 1, 1, 5, 4, 4]` dizisinde benzersiz elemanlar `[3, 5]` olmalıdır.

**Cevap:**

```python
Liste = [2,2,3,3,8,8,9,1,1,5,4,4] #sorudaki liste

uzunluk = 12 #dizi uzunluğu

benzersizler = [] #tekrar etmeyen elemanları koyacağımız dizi

for i in range(uzunluk): #sıra sıra indexleri gezerek bakıyoruz
    eleman = Liste[i]  #suanki indexte bulunan sayıyı elemana atıyoruz
    adet = Liste.count(eleman) #eleman listede kaç tane var bakıyoruz

    if adet == 1: #eğer elemandan dizide sade 1 tane varsa
        benzersizler.append(eleman) #benzersiz oldugundan benzersizler dizisine atanır

#benzersizleri yazdırma
print("Benzersiz elemanlar:", benzersizler)
```

## Soru 5

Bir string içindeki sesli harfleri sayan programı yazınız. Hazır fonksiyon kullanılmayacaktır.

**Cevap:**

```python
metin = "Merhaba dünya" #sesli harf kontrolü yapılacak metin

sesliler = "aeıioöuüAEIİOÖUÜ" #sesli harfler listesi (kontrol için)

uzunluk = 13 #dizi uzunluğu
sesli_sayi = 0 #sesli harf sayan sayaç

for i in range(uzunluk): #metin dizisi içindeki her harfi aramak için metindeki harf sayısı kadar döngü
    if metin[i] in sesliler: #metindeki her harf sıra sıra denenir döngü sayesinde. eğer bir harf sesliler dizisinde de varsa
        sesli_sayi += 1 #sesli harf bulundugundan sayaç 1 artar

#kaç tane sesli harf yazdıran sayaç
print("Sesli harf sayısı:", sesli_sayi)
```

## Soru 6

Bir dizideki ikinci en büyük sayıyı bulan Python kodunu yazınız. `max()` kullanılmayacaktır.

**Cevap:**

```python
dizi = [12, 45, 7, 45, 23, 89, 3]

en_buyuk = dizi[0] #en buyuk sayının atanacağı değişken
ikinci = -1 #ikinci en büyük sayının atanacağı değişken

for i in range(1,7):
    if dizi[i] > en_buyuk: #şuan baktığımız eleman en buyukten buyukse
        ikinci = en_buyuk #daha büyüğü bulunduğundan önceki en büyüğü 2. en büyük yapıyoruz
        en_buyuk = dizi[i] #elemanı en büyüğe atıyoruz
    elif dizi[i] > ikinci and dizi[i] != en_buyuk: #eğer en büyük değilse ama 2. en büyükten daha büyükse
        ikinci = dizi[i] #ikinci en büyüğe atıyoruz

#ikinci en büyüğü yazdırma
print("İkinci en büyük sayı:", ikinci)
```

## Soru 7

Kullanıcıdan alınan bir cümlede en uzun kelimeyi bulan Python programını yazınız.

**Cevap:**

```python
cumle = input("Bir cümle girin: ")

mevcut_kelime = "" #mevcut kelimeyi tutcak değişken
en_uzun = "" #en uzun kelimeyi tutcak değişken

#cümlede boşluk gelene kadar teker teker harfleri alırız
for harf in cumle + " ": #cümle sonuna boşluk ekledik ki son kelimenin sonunda da boşluk olsun kelimeyi çıkarabilelim
    if harf != " ": #aldığımız harf boşluk mu diye bakarız
        mevcut_kelime += harf  #boşluk değilse kelime devam ediyordur. mevcut kelime stringine ekleriz.

    else: #aldığımız harf boşluk ise kelime bitmiştir
        if len(mevcut_kelime) > len(en_uzun): #aldıgımız kelime en_uzun değişkenindeki kelimeden uzunsa
            en_uzun = mevcut_kelime #yeni en uzun kelime o olur.
        mevcut_kelime = ""  #mevcut kelimeyi sıfırlarız

#bulduğumuz en uzun kelimeyi yazdırma
print("En uzun kelime:", en_uzun)
```

## Soru 8

Kullanıcıdan bir doğrunun iki noktasını (x₁, y₁) ve (x₂, y₂) şeklinde alarak, bu iki noktadan geçen doğrunun **eğimini (m)** hesaplayan **Python programını** yazınız.

**İpucu Eğim formülü:** m = (y₂ − y₁) / (x₂ − x₁)

**Cevap:**

```python
#doğru noktalarını alma
x1 = float(input("x1: "))
y1 = float(input("y1: "))
x2 = float(input("x2: "))
y2 = float(input("y2: "))

if x2 == x1: #x ler eşitse eğim yoktur (formulde bölen 0 çıkar)
    print("Eğim tanımsız (dikey doğru)")

else:
    m = (y2 - y1) / (x2 - x1) #eğim formulu uygulanır
    print("Eğim (m):", m) #sonuç yazdırılır
```
