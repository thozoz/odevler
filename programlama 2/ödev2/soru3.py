liste = [1,2,3,1,2,3,4,5,6,5,6,7,8]

gecici = [liste[0]]
en_uzun = []
sayi = 1
en_sayi = 0

i = 1
while i < 13:
    if liste[i] == liste[i - 1] + 1:
        gecici.append(liste[i])
        sayi += 1
    else:
        if sayi > en_sayi:
            en_uzun = gecici
            en_sayi = sayi

        gecici = [liste[i]]
        sayi = 1

    i += 1

if sayi > en_sayi:
    en_uzun = gecici

print(en_uzun)
