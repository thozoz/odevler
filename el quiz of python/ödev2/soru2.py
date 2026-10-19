Liste = [1,2,3,3,4,6,8,9,8,1,2,5,4,3] #soruda verilen liste

uzunluk = 14 #dizi uzunluğu

i = 0
while i < uzunluk: #while ile döng. for kullanmama nedenizim döngünüün uzunluk değiştikce değişmesi için
    eleman = Liste[i] #şuan baktığımız index teki elemanı eleman değişkenine atıyoruz
    adet = Liste.count(eleman) #eleman değişkeninden Liste dizisinde kaç tane var bakıyoruz ve adet değişkenine atıyoruz

    if adet > 1: #eğer adet 1 den fazlaysa o eleman tekrar eden elemandır
        print(eleman, "elemanından", adet, "tane bulundu.") #dizide bu elemandan kaç tane olduğunu yazdırıyoruz

        j = uzunluk - 1 #uzunluk-1 ile son elemandan başlıyoruz ve tekrar ettiğini farkettiğimiz sayıya doğru ilerliyoruz ters olarak

        while j > i: #ilk buldugumuz sayıyı silmiyoruz. ondan sonra gelen tekrar edenleri silceğimiz için j>i yapıyoruz
            if Liste[j] == eleman: #tersten giderken eğer tekrar eden elemanın olduğu indexi bulursak
                del Liste[j] #o indexi siliyoruz
                uzunluk -= 1 #index silindiğinden uzunluk 1 azalıyor

            j -= 1 #liste de ters gitmeye devam ediyoruz indexleri sıra sıra

    i += 1

#tekrar eden elemanların silinmiş halini yazdırıyoruz
print("Tekrarlardan arındırılmış liste:", Liste)