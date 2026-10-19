Liste = [1, 2, 3, 3, 4, 6, 8, 9, 8, 1, 2, 5, 4, 3]

uzunluk = 14
i = 0

while i < uzunluk:
    eleman = Liste[i]
    adet = Liste.count(eleman)

    if adet > 1:
        print(eleman, "elemanından", adet, "tane bulundu.")

        j = uzunluk - 1

        while j > i:
            if Liste[j] == eleman:
                del Liste[j]
                uzunluk -= 1

            j -= 1

    i += 1

print("Tekrarlardan arındırılmış liste:", Liste)