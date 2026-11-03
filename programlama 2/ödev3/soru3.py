#3 basamaklı sayılar 100 ile 999 arasıdır
#kural: ilk rakam + son rakam > ortadaki rakam olcak

print("Kurala uyan 3 basamaklı sayılar:")

for sayi in range(100, 1000): #100 den 999 a kadar tum 3 basamaklıları gezer
    #basamakları buluyoruz
    yuzler = sayi // 100 #ilk rakamı verir (yuzler basamagı)
    onlar = (sayi // 10) % 10 #ortadaki rakamı verir (onlar basamagı)
    birler = sayi % 10 #son rakamı verir (birler basamagı)
    
    #ilk ve son rakamın toplamı ortadakinden buyuk mu diye bakarız
    if (yuzler + birler) > onlar:
        print(sayi, end=" ") #yanyana yazdırsın diye end="" oto \n koymasın diye

print() #en son alt satıra gecmek icin bos print (\n işlevi gördü)
