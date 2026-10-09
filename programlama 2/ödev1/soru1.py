#ortak rakam varsa true yapılacak değişken
ortak=False

#kullanıcıdan 2 basamaklı sayılar alıyoruz
sayi1=int(input("1. sayıyı giriniz: "))
sayi2=int(input("2. sayıyı giriniz: "))

#sayı 1 birler ve onlar basamagı alma

sayi1b=sayi1%10 #birler basamagı

sayi1o=sayi1//10 #onlar basamagı


#sayı 2 birler ve onlar basamagı alma

sayi2b=sayi2%10 #birler basamagı

sayi2o=sayi2//10 #onlar basamagı


#karşılaştırma
if sayi1o==sayi2o or sayi1o==sayi2b: 
    print("Ortak rakam "+ str(sayi1o) + "")
    ortak=True

if (sayi1b==sayi2o or sayi1b==sayi2b) and sayi1b != sayi1o: #sayi1b != sayi1o mi diye bakarak aynı ortak rakam bida yazdırılmasın yapıyoruz
    print("Ortak rakam "+ str(sayi1b) + "")
    ortak=True  

#ortak rakam yoksa
if ortak==False:
    print("Ortak rakam yoktur.")