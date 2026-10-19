yildiz=int(input("Yıldız sayısını giriniz: "))

for i in range(yildiz): #bu döngü yildiz değişkeni kadar çalışacak
    print("*", end="") #end="" parametresi print fonksiyonunun otomatik sona koydugu \n i koymamasını ve otomatik alt satıra geçmemesini sağlar. böylece yıldızlar yanyana olur
    