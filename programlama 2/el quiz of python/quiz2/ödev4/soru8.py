L = [1, 2, 2, 3, 3, 4, 4, 5, 6, 7, 7, 8] #soruda verilen 12 elemanlı liste
uzunluk = 12 #dizi uzunluğu

#2 ve 3 elemanlı alt kümeleri bulup benzer olanları yazdıran fonksiyon
def alt_kumeler(liste):
    ikililer = [] #2 elemanlı alt kümeleri koyacağımız dizi
    ucluler = [] #3 elemanlı alt kümeleri koyacağımız dizi

    #2 elemanlı alt kümeleri çıkarma
    for i in range(uzunluk):
        for j in range(i + 1, uzunluk): #aynı elemanı bida almamak için i+1 den başlatıyoruz
            ikililer.append([liste[i], liste[j]])

    #3 elemanlı alt kümeleri çıkarma
    for i in range(uzunluk):
        for j in range(i + 1, uzunluk):
            for k in range(j + 1, uzunluk):
                ucluler.append([liste[i], liste[j], liste[k]])

    #2 elemanlılarda benzer (birden fazla olan) kümeleri bulma
    benzer_ikili = []
    for kume in ikililer:
        if ikililer.count(kume) > 1 and kume not in benzer_ikili: #birden fazla varsa ve diziye eklemediysek
            benzer_ikili.append(kume)

    #3 elemanlılarda benzer (birden fazla olan) kümeleri bulma
    benzer_uclu = []
    for kume in ucluler:
        if ucluler.count(kume) > 1 and kume not in benzer_uclu: #birden fazla varsa ve diziye eklemediysek
            benzer_uclu.append(kume)

    #benzer alt kümeleri yazdırma
    print("2 elemanlı benzer alt kümeler:", benzer_ikili)
    print("3 elemanlı benzer alt kümeler:", benzer_uclu)


#fonksiyonu çağırma
alt_kumeler(L)
