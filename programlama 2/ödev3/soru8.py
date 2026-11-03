#kullanıcıdan bilgileri ve notları alıyoruz (önceki sorudaki gibi)
ad_soyad = input("Ad soyad giriniz: ")
vize1 = float(input("Vize 1 notunu giriniz: "))
vize2 = float(input("Vize 2 notunu giriniz: "))
final = float(input("Final notunu giriniz: "))

#ortalama hesabı vize1 %20 vize2 %20 final %60
ortalama = (vize1 * 0.20) + (vize2 * 0.20) + (final * 0.60)

print(ad_soyad + " ortalaması:" + str(ortalama))

#ortalamaya gore durum kosulları
if ortalama <= 30: #30 ve altı ise kaldı
    print("Kaldı!")
elif ortalama <= 69: #31 ve 69 arası ise kritik
    print("Kritik!")
else: #70 uzerinde ise gecti
    print("Geçti!")
