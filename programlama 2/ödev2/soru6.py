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
