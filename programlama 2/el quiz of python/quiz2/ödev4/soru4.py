alfabe = "abcçdefgğhıijklmnoöprsştuüvyz" #kontrol için alfabe dizisi

#harfleri sayan fonksiyon
def harf_say(metin):
    metin = metin.lower() #büyük küçük harfleri beraber saymak için küçültüyoruz

    for i in range(len(alfabe)): #alfabedeki harf sayısı kadar döngü
        harf = alfabe[i] #şu an baktığımız harfi alıyoruz
        sayac = 0 #harften kaç tane olduğunu tutacak sayaç

        for j in range(len(metin)): #metindeki karakter sayısı kadar döngü
            if metin[j] == harf: #metindeki harf alfabedeki harfle aynıysa
                sayac += 1 #sayacı 1 arttır

        print(harf, "harfi:", sayac)


#kullanıcıdan enter'a basana kadar metin alıyoruz
yazi = input("Metni giriniz: ")

#fonksiyonu çağırma
harf_say(yazi)
