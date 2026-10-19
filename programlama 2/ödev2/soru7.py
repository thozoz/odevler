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
