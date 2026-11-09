import random

#1-25 arası rastgele sayılardan olusan 20 elemanlı liste
liste = []

#20 kere donen döngü ile listeye rastgele sayılar atıyoruz
for i in range(20):
    sayi = random.randint(1, 25) #1 ile 25 arası rastgele tamsayı uretir
    liste.append(sayi) #uretilen sayıyı diziye atar

print("20 elemanlı liste:", liste)

toplam = 0 #bastan itibaren sayıları toplayacagımız degisken
son_eleman = 0 #toplama dahil edilen en son elemanı tutcak degisken
son_index = 0 #en son hangi indexteki eleman eklendi onu tutar

#listenin basından itibaren elemanları gezip topluyoruz
for i in range(len(liste)):
    eleman = liste[i] #suanki indexteki elemanı alıyoruz
    toplam += eleman #toplama ekliyoruz
    son_eleman = eleman #son eklenen elemanı guncelliyoruz
    son_index = i #son eklenen indexi guncelliyoruz
    
    #toplam 100 ü gectigi ilk anda döngü durur
    if toplam > 100: #100 u gectiyse break ile cıkarız
        break

#sonucları ekrana yazdırma
print("Toplam:", toplam)
print("Toplama en son dahil edilen eleman:", son_eleman)
print("Bu elemanın listedeki indexi:", son_index)
