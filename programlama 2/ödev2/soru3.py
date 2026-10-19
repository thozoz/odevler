liste = [1,2,3,1,2,3,4,5,6,5,6,7,8] #soruda verilen örnek liste

gecici = [liste[0]] #o an taranan aktif ardışık alt diziyi tutacak değişken
en_uzun = [] #en uzun artan ardışık alt diziyi tutacak değişken

sayi = 1 #gecici dizisinin eleman sayısını sayan değişken
en_sayi = 0 #en uzun dizinin eleman sayısı (rekor)

for i in range(1, 13):
    if liste[i] == liste[i - 1] + 1: #ardışık artan mı kontrol ediyor
        gecici = gecici + [liste[i]] #ardışıksa gecici dizisinin sonunda liste[i] sayısını ekler. gecici.append(liste[i]) ile aynı işlev 
        sayi += 1 #gecici dizisinin eleman sayısını 1 arttırıyoruz (liste[i] eklediğimizden sonunda)

    else: #ardışık olmayı kesince
        if sayi > en_sayi: #eğer bu yeni ardışık alt dizi daha uzunsa eski en uzundan
            en_uzun = gecici #yeni en uzun ardışık alt diziyi tanımlıyoruz
            en_sayi = sayi #yeni en uzun ardışık alt dizinin eleman sayısını tanımlıyoruz

        gecici = [liste[i]] #gecici yi kaldığımız yere aldık
        sayi = 1 #gecici dizisi eleman sayısı 1 e geri döndü onu atıyoruz
 
#eğer ardışık alt dizi en son diziyse hiç ardışık olmayı kesmeyeceğinden else: içine girmez. ondan bu kodla onu alırız else e girmese de
if sayi > en_sayi: 
    en_uzun = gecici

#en uzun artan ardışık alt diziyi yazdırma
print("En uzun artan ardışık alt dizi:", en_uzun)
