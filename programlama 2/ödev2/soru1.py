import random

dizi1 = []
dizi2 = []

i = 0
while i < 5:
    dizi1.append(random.randint(1, 50))
    dizi2.append(random.randint(1, 50))
    i += 1


print("1. dizi:", dizi1)
print("2. dizi:", dizi2)

ortaklar = []

for eleman in dizi1:
    if eleman in dizi2 and eleman not in ortaklar:
        ortaklar.append(eleman)

print("Ortak elemanlar:", ortaklar)

birlesik = dizi1 + dizi2
son_dizi = []
son_uzunluk = 0

for eleman in birlesik:
    if eleman not in ortaklar:
        son_dizi.append(eleman)
        son_uzunluk += 1

print("Birleşmiş dizi:", birlesik)
print("Ortaklar çıkarılmış dizi:", son_dizi)

i = 0

while i < son_uzunluk - 1:
    j = 0

    while j < son_uzunluk - 1 - i:
        if son_dizi[j] > son_dizi[j + 1]:
            gecici = son_dizi[j]
            son_dizi[j] = son_dizi[j + 1]
            son_dizi[j + 1] = gecici

        j += 1

    i += 1

print("Sıralanmış dizi:", son_dizi)