# kullanıcıdan nokta koordinatlarını alma
x = float(input("x koordinatını giriniz: "))
y = float(input("y koordinatını giriniz: "))

# kullanıcıdan doğru katsayılarını al y = m*x + n formülü için
m = float(input("m katsayısını giriniz: "))
n = float(input("n katsayısını giriniz: "))

#kullanıcının girdiği koordinatlar doğru üzerinde mi kontrolü
if y == (m * x + n): # y = m*x + n formülünden doğru üzerinde mi bakarız
    print("Nokta doğrunun üzerindedir.")
else:
    print("Nokta doğrunun üzerinde değildir.")
