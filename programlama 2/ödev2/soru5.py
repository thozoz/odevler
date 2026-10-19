metin = "Merhaba dünya"

sesliler = "aeıioöuüAEIİOÖUÜ"

uzunluk = 13
sayi = 0
i = 0

while i < uzunluk:
    if metin[i] in sesliler:
        sayi += 1

    i += 1

print("Sesli harf sayısı:", sayi)
