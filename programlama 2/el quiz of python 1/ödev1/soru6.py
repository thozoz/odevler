i=1 #kaçıncı sayı giriliyo tutmak için
toplam=0 #girilen sayıların toplamını tutacak değişken

while True: #kullanıcı 0 girene kadar sayı alma döngüsü

    sayi=int(input(str(i)+". sayıyı gir: ")) #kullanıcıdan toplamı hesaplanacak sayıları alma
    if sayi==0: break
    toplam+=sayi #kullanıcıdan alınan sayıları toplama
    i+=1 


print("Sayı toplamları: "+ str(toplam)) #sayıların toplamının yazdırılması