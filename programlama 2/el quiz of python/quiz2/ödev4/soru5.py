#Adım 1: şehirlerin ülke ve kıta bilgilerini tutan sözlük
sehirler_sozlugu = {
    'İstanbul': {'ülke': 'Turkey', 'kıta': 'Europe'},
    'Tokyo': {'ülke': 'Japan', 'kıta': 'Asia'},
    'New_york': {'ülke': 'United States', 'kıta': 'North America'},
    'Mumbai': {'ülke': 'India', 'kıta': 'Asia'},
    'Cairo': {'ülke': 'Egypt', 'kıta': 'Africa'},
    'Seoul': {'ülke': 'South Korea', 'kıta': 'Asia'},
    'London': {'ülke': 'United Kingdom', 'kıta': 'Europe'}
}

#Adım 2: şehirleri kıtalara göre gruplayan fonksiyon
def sehirleri_kitalara_göre_grupla(sehirler):
    gruplar = {} #kıtaları tutacak boş sözlük

    for sehir in sehirler: #sözlükteki her şehre bakıyoruz
        kita = sehirler[sehir]['kıta'] #şehrin kıtasını alıyoruz
        ulke = sehirler[sehir]['ülke'] #şehrin ülkesini alıyoruz

        if kita not in gruplar: #eğer kıta sözlükte yoksa
            gruplar[kita] = [] #o kıta için boş liste açıyoruz

        gruplar[kita].append(sehir + " (" + ulke + ")") #şehri ve ülkesini o kıtanın listesine ekliyoruz

    return gruplar


#fonksiyonu çağırıyoruz
sonuc = sehirleri_kitalara_göre_grupla(sehirler_sozlugu)

#Adım 3: gruplanmış şehirleri ekrana yazdırma
for kita in sonuc:
    print(kita, ":", sonuc[kita])
