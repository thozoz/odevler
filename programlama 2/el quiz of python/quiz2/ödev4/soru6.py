#iki tarih arasındaki gün sayısını hesaplayan fonksiyon
def gun_sayisi_hesapla(tarih1, tarih2):
    #1. tarihi - işaretinden bölüp yıl, ay, gün olarak alıyoruz
    t1 = tarih1.split("-")
    yil1 = int(t1[0])
    ay1 = int(t1[1])
    gun1 = int(t1[2])

    #2. tarihi - işaretinden bölüp yıl, ay, gün olarak alıyoruz
    t2 = tarih2.split("-")
    yil2 = int(t2[0])
    ay2 = int(t2[1])
    gun2 = int(t2[2])

    #tarihleri toplam güne çeviriyoruz (1 yıl 365 gün, 1 ay 30 gün)
    toplam1 = yil1 * 365 + ay1 * 30 + gun1
    toplam2 = yil2 * 365 + ay2 * 30 + gun2

    fark = toplam2 - toplam1 #iki tarih arasındaki gün farkı
    if fark < 0: #eğer fark eksi çıkarsa artıya çeviriyoruz (mutlak değer alıyoruz gibi)
        fark = fark * -1

    return fark

#iki tarih arasındaki hafta sayısını hesaplayan fonksiyon
def hafta_sayisi_hesapla(tarih1, tarih2):
    gun = gun_sayisi_hesapla(tarih1, tarih2) #önce gün sayısını buluyoruz
    hafta = gun // 7 #gün sayısını 7 ye bölerek hafta sayısını buluyoruz
    return hafta


#kullanıcıdan tarihleri alma
tarih1 = input("1. tarihi giriniz (YYYY-MM-DD): ")
tarih2 = input("2. tarihi giriniz (YYYY-MM-DD): ")

print("Gün sayısı:", gun_sayisi_hesapla(tarih1, tarih2))
print("Hafta sayısı:", hafta_sayisi_hesapla(tarih1, tarih2))
