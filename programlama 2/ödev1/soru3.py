kare=int(input("Kare kenar uzunluğunu giriniz: "))

for i in range(kare): #bu döngü dikeye yıldız koyduran döngü

    for j in range(kare): #bu döngü yataya kare değişkeni kadar yıldız koyduruyo
        print("*", end="") #end parametresi 2. sorudaki işlevini sürdürüyor. bu print yatay yıldızları koyan print fonksiyonu

    print() #yataya koyulan yıldızlardan sonra \n ile alt line a geçsin diye koyulan print, olmazsa butun yıldızlar yanyana olur