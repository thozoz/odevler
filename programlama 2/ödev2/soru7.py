cumle = input("Bir cümle girin: ")

kelimeler = cumle.split()
en_uzun = kelimeler[0]

for kelime in kelimeler:
    if len(kelime) > len(en_uzun):
        en_uzun = kelime

print("En uzun kelime:", en_uzun)
