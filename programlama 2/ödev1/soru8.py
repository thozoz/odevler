#kullanıcıdan 2 basamaklı sayı alıyoruz
sayi=int(input("İki basamaklı sayı giriniz: "))

toplam=0 #toplamı tutacak değişken

if sayi<=99 and sayi>=10: #sayı 2 basamaklı mı yani 99 ile 10 arasında mı kontrolu (99 ve 10 dahil)

    #eğer 2 basamaklıysa rakamlar toplamı hesaplanır
    toplam=(sayi%10)+(sayi//10) #sayi%10 ile birler basamağı alınır, sayi//10 ile onlar basamağı alınır

    print("Sayı rakamlar toplamı: " +str(toplam)) #toplam yazdırma

else: #2 basamaklı değil, uyarı mesajı ver
   print("Hatalı işlem!") 

