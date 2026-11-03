#kullanıcıdan isim ve sınav notlarını alıyoruz
ad_soyad = input("Ad soyad giriniz: ")
vize1 = float(input("Vize 1 notunu giriniz: "))
vize2 = float(input("Vize 2 notunu giriniz: "))
final = float(input("Final notunu giriniz: "))

#vize1 %20, vize2 %20, final %60 etkili ortalama hesabı
#yuzdeleri carpıp topluyoruz
ortalama = (vize1 * 0.20) + (vize2 * 0.20) + (final * 0.60)

#ad-soyad ortalaması:z seklinde cıktı yazdırma
print(ad_soyad + " ortalaması:" + str(ortalama))
