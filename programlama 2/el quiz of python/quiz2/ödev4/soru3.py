#soruda verilen 3x3 matris
matrix = [ [1, 2, 3],
           [4, 5, 6],
           [7, 8, 9] ]

#determinant hesaplayan fonksiyon
def determinant_hesapla(m):
    #1. satır elemanları
    a = m[0][0]
    b = m[0][1]
    c = m[0][2]

    #2. satır elemanları
    d = m[1][0]
    e = m[1][1]
    f = m[1][2]

    #3. satır elemanları
    g = m[2][0]
    h = m[2][1]
    i = m[2][2]

    #3x3 matris determinant formülü
    det = a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)
    print("Matrisin determinantı:", det)


#fonksiyonu çağırma
determinant_hesapla(matrix)
