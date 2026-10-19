#kullanıcının kaç sayı girceğini kullanıcıdan alma
say=int(input("Kaç sayı girilecek: "))

toplam=0 #aritmetik hesaplamak için girilen sayıların toplamını tutacak değişken

for i in range(1,say+1): #kullanıcının istediği kadar sayıyı alma döngüsü

    sayi=int(input(str(i)+". sayıyı gir: ")) #kullanıcıdan aritmetiği hesaplanacak sayıları alma
    toplam+=sayi #kullanıcıdan alınan sayıları toplama


print("Aritmetik ortalamaları: "+ str(toplam/say)) #aritmetik ortalamanın hesaplanıp yazdırılması