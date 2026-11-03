#10 elemanlı liste için boş liste tanımlıyoruz
liste = []

#listenin 10 elemanı dolana kadar while döngüsü calısacak
while len(liste) < 10:
    sayi = int(input(str(len(liste) + 1) + ". sayıyı giriniz: ")) #kullanıcıdan sayıyı alıyoruz
    
    #liste boşsa ilk girilen sayıyı direk listeye ekleriz karsılastırcak onceki sayı olmadıgından
    if len(liste) == 0:
        liste.append(sayi) #sayıyı listeye ekleme
        print("İlk sayı eklendi:", sayi)
    else:
        #girilen sayı bir onceki sayıdan buyuk mu bakarız (listenin son elemanından)
        if sayi > liste[-1]: #eger buyukse kurala uyar listeye ekleriz
            liste.append(sayi)
            print("Sayı eklendi:", sayi)
        else: #kucukse yada esitse goz ardı edilir listeye alınmaz
            print("Girilen sayı onceki sayıdan buyuk degil, göz ardı edildi.")

print()
print("Oluşan 10 elemanlı liste:", liste)

#listeyi ters sırada ekrana yazdırma
print("Listenin tersten yazılmıs hali:")
for i in range(len(liste) - 1, -1, -1): #son indexten 0. indexe kadar -1 azalarak gider
    print(liste[i], end=" ") #yanyana yazsın diye end koyduk

print() #alt satıra gecmek icin print
