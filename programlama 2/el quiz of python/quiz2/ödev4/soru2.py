#soruda verilen metin, biraz uzun
metin = "Hava kirliliği, dünya genelinde büyük bir çevresel sorun olarak karşımıza çıkmaktadır. Hava kirliliği, atmosferdeki zararlı gazlar, kimyasallar, tozlar ve partiküllerin yüksek seviyelerde bulunması sonucu ortaya çıkar. Bu kirleticiler, sanayi tesisleri, araç emisyonları, enerji üretimi ve tarım gibi kaynaklardan atmosfere salınır. Hava kirliliği, ciddi sağlık sorunlarına yol açabilir ve doğal ekosistemlere zarar verebilir. Hava kirliliği, insan sağlığına bir dizi olumsuz etki yapar. Kirli hava solumak, solunum yolu hastalıklarının, kalp hastalıklarının, kanser riskinin artmasına ve genel yaşam kalitesinin düşmesine neden olabilir. Ayrıca, çocuklar, yaşlılar ve kronik sağlık sorunları olanlar, hava kirliliğinin etkilerine daha fazla maruz kalabilirler. Hava kirliliği aynı zamanda ekosistemlere zarar verir. Bitkiler, hayvanlar ve su kaynakları üzerinde olumsuz etkiler yaratabilir, biyolojik çeşitliliği azaltabilir ve tarım verimliliğini etkileyebilir. Bu sorunun çözümü için dünya genelinde çevresel düzenlemeler ve temiz enerji kaynaklarına geçiş gibi adımlar atılmaktadır. Ayrıca, bireysel olarak daha çevre dostu seçimler yaparak da hava kirliliğinin azaltılmasına katkı sağlayabiliriz. Hava kirliliği ile mücadele, hem insan sağlığını hem de gezegenimizin geleceğini korumak için önemlidir."

#hava kelimesini sayan fonksiyon
def hava_say(yazi):
    yazi = yazi.lower() #büyük küçük harf ikisini de algılasın diye bütün harfleri küçültüyoruz
    sayac = yazi.count("hava") #metinde kaç tane hava kelimesi geçtiğini sayıyoruz

    print("Metinde hava kelimesi", sayac, "defa geçiyor.")


#fonksiyonu çağırma
hava_say(metin)
