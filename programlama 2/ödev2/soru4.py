Liste = [2,2,3,3,8,8,9,1,1,5,4,4]

uzunluk = 12
i = 0

benzersizler = []

while i < uzunluk:
    eleman = Liste[i]
    adet = Liste.count(eleman)

    if adet == 1:
        benzersizler.append(eleman)

    i += 1

print("Benzersiz elemanlar:", benzersizler)
