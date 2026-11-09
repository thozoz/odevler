metin = "Merhaba dünya" #sesli harf kontrolü yapılacak metin

sesliler = "aeıioöuüAEIİOÖUÜ" #sesli harfler listesi (kontrol için)

uzunluk = 13 #dizi uzunluğu
sesli_sayi = 0 #sesli harf sayan sayaç

for i in range(uzunluk): #metin dizisi içindeki her harfi aramak için metindeki harf sayısı kadar döngü
    if metin[i] in sesliler: #metindeki her harf sıra sıra denenir döngü sayesinde. eğer bir harf sesliler dizisinde de varsa
        sesli_sayi += 1 #sesli harf bulundugundan sayaç 1 artar

#kaç tane sesli harf yazdıran sayaç
print("Sesli harf sayısı:", sesli_sayi)
