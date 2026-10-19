dizi = [12, 45, 7, 45, 23, 89, 3]

en_buyuk = dizi[0]
ikinci = -1

i = 1
while i < 7:
    if dizi[i] > en_buyuk:
        ikinci = en_buyuk
        en_buyuk = dizi[i]
    elif dizi[i] > ikinci and dizi[i] != en_buyuk:
        ikinci = dizi[i]

    i += 1

print("İkinci en büyük sayı:", ikinci)
