#doğru noktalarını alma
x1 = float(input("x1: "))
y1 = float(input("y1: "))
x2 = float(input("x2: "))
y2 = float(input("y2: "))

if x2 == x1: #x ler eşitse eğim yoktur (formulde bölen 0 çıkar)
    print("Eğim tanımsız (dikey doğru)")

else:
    m = (y2 - y1) / (x2 - x1) #eğim formulu uygulanır
    print("Eğim (m):", m) #sonuç yazdırılır
