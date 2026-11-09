#yaş ve emeklilik hesaplayan fonksiyon
def yas_hesapla(dogum_yili, emeklilik_yasi):
    yas = 2026 - dogum_yili #2026 yılından doğum yılını çıkarıp yaşı buluyoruz
    emeklilik_yili = dogum_yili + emeklilik_yasi #doğum yılı ile emeklilik yaşını toplayıp emekli olacağı yılı buluyoruz

    if emeklilik_yili > 2026: #eğer emeklilik yılı 2026 dan büyükse daha emekli olmamıştır
        kalan = emeklilik_yili - 2026 #emekliliğe kaç yıl kaldığını buluyoruz
        print("Yaşınız:", yas, ", Emeklilik yılınız:", emeklilik_yili, ", Emekliliğe", kalan, "yıl kaldı.")
    elif emeklilik_yili == 2026: #emeklilik yılı 2026 ise bu yıl emekli oluyordur
        print("Yaşınız:", yas, ", Emeklilik yılınız:", emeklilik_yili, ", Bu yıl emekli oluyorsunuz.")
    else: #emeklilik yılı 2026 dan küçükse zaten emekli olmuştur
        gecen = 2026 - emeklilik_yili #kaç yıl önce emekli olduğunu buluyoruz
        print("Yaşınız:", yas, ", Zaten", emeklilik_yili, "yılında emekli oldunuz.", gecen, "yıldır emeklisiniz.")


#3 ayrı kullanıcı için döngü
for i in range(1, 4): #1 den 3 e kadar 3 kullanıcı için dönecek
    print(i, ". kullanıcı")
    dogum = int(input("Doğum yılınızı giriniz: ")) #kullanıcıdan doğum yılını alıyoruz
    emeklilik = int(input("Emeklilik yaşınızı giriniz: ")) #kullanıcıdan emeklilik yaşını alıyoruz

    yas_hesapla(dogum, emeklilik) #fonksiyonu çağırıyoruz
    print() #alt satıra geçmek için print
