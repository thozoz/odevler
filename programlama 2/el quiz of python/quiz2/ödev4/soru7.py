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
