#soruda verilen sözlükleri girme
fiyat = {'muz': 4, 'elma': 2, 'portakal': 1.5, 'armut': 3}
stok = {'muz': 6, 'elma': 8, 'portakal': 32, 'armut': 15}

#3 musteri oldugundan 1 den 3 e kadar donen for dongusu
for musteri in range(1, 4):
    print("\n--- " + str(musteri) + ". Müşteri ---")
    toplam_tutar = 0 #bu musterinin odeyecegi toplam tutarı tutcak degisken
    
    while True: #musteri alısverisi bitirene kadar döner
        meyve = input("Almak istediginiz meyve (bitirmek icin 'bitti' yazın): ")
        
        if meyve == "bitti": #musteri alısverisi bitirmek isterse dönguden cık
            break
            
        if meyve not in fiyat: #manavda olmayan meyve girildiginde uyar
            print("Bu meyve bulunmamaktadır!")
            continue #basa sarar
            
        if stok[meyve] <= 0: #meyvenin stogu kalmamıssa uyarı verir
            print("Stok bitmiştir.")
            continue
            
        miktar = int(input("Kaç adet " + meyve + " istiyorsunuz? (kalan stok: " + str(stok[meyve]) + "): "))
        
        if miktar <= 0: #hatalı sayı girildiginde uyar
            print("Gecersiz miktar girdiniz.")
            continue
            
        if miktar > stok[meyve]: #istenen miktar mevcut stoktan fazlaysa uyar
            print("Yeterli stok yok! En fazla " + str(stok[meyve]) + " adet alabilirsiniz.")
        else: #stok yetiyorsa satısı yap
            stok[meyve] -= miktar #meyvenin stogunu azalt
            tutar = miktar * fiyat[meyve] #bu alımın fiyatını hesapla
            toplam_tutar += tutar #musterinin toplamına ekle
            print(str(miktar) + " adet " + meyve + " alındı. Kalan stok: " + str(stok[meyve]))
            
            #satın alım sonrası stok 0 olduysa stok bitti uyarısı verir
            if stok[meyve] == 0:
                print("Stok bitmiştir.")

    #her satın alım sonunda musteriye toplam alısveris fiyatını yazdır
    print(str(musteri) + ". Müşteri toplam alışveriş fiyatı: " + str(toplam_tutar))

#son kalan stok durumunu yazdır
print("\nSon kalan stoklar:", stok)
