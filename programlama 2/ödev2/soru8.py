x1 = float(input("x1: "))
y1 = float(input("y1: "))
x2 = float(input("x2: "))
y2 = float(input("y2: "))

if x2 == x1:
    print("Eğim tanımsız (dikey doğru)")
else:
    m = (y2 - y1) / (x2 - x1)
    print("Eğim (m):", m)
