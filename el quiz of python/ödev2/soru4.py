Liste = [2,2,3,3,8,8,9,1,1,5,4,4] #sorudaki liste

uzunluk = 12 #dizi uzunluğu

benzersizler = [] #tekrar etmeyen elemanları koyacağımız dizi

for i in range(uzunluk): #sıra sıra indexleri gezerek bakıyoruz
    eleman = Liste[i]  #suanki indexte bulunan sayıyı elemana atıyoruz
    adet = Liste.count(eleman) #eleman listede kaç tane var bakıyoruz

    if adet == 1: #eğer elemandan dizide sade 1 tane varsa
        benzersizler.append(eleman) #benzersiz oldugundan benzersizler dizisine atanır

#benzersizleri yazdırma
print("Benzersiz elemanlar:", benzersizler)
