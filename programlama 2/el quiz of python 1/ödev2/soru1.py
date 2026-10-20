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