#soruda verilen listeyi oluşturma
yazi = ["Ahmet", "altı", "yaşında", "zeynep", "dört", "yaşında", "esra", "iki", "yaşında", "ayşe", "bir", "yaşında"]

#sayıların rakam karsılıklarını tutan sozluk olusturma
sozluk = {
    "sıfır": "0",
    "bir": "1",
    "iki": "2",
    "üç": "3",
    "dört": "4",
    "beş": "5",
    "altı": "6",
    "yedi": "7",
    "sekiz": "8",
    "dokuz": "9"
}

output = "" #hazır fonksiyon olmadan stringleri birlestirecegimiz bos degisken

#listedeki her kelimeye tek tek bakıyoruz
for kelime in yazi:
    #kelime sozlukte var mı (yani sayı ismi mi) bakarız
    if kelime in sozluk:
        ekle = sozluk[kelime] #sozlukteki rakam halini alıyoruz
    else:
        ekle = kelime #sayı degilse direk kelimeyi alıyoruz
        
    #hazır fonksiyon (join fln) kullanmadan kelimeleri birlestirme
    if output == "":
        output = ekle #ilk kelimeyse direk eklenir
    else:
        output = output + " " + ekle #araya bosluk koyup ekliyoruz

#cıktıyı yazdırma
print('Output = "' + output + '"')
