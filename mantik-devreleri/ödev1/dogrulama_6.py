def deger(s, taban):
    t = 0
    for ch in s:
        t = t * taban + int(ch)
    return t

def gecerli(s, taban):
    return all(int(ch) < taban for ch in s)

TABANLAR = [2, 8, 10, 16]
kayitlar = {'A': '17', 'B': '21', 'C': '10001'}

for k, s in kayitlar.items():
    print(f"KAYIT {k} '{s}':")
    for b in TABANLAR:
        if gecerli(s, b):
            print(f"  taban {b:2d} gecerli -> {deger(s, b)}")
        else:
            print(f"  taban {b:2d} GECERSIZ")

coz = []
for ba in TABANLAR:
    if not gecerli('17', ba):
        continue
    for bb in TABANLAR:
        if not gecerli('21', bb):
            continue
        for bc in TABANLAR:
            if not gecerli('10001', bc):
                continue
            va, vb, vc = deger('17', ba), deger('21', bb), deger('10001', bc)
            if va == vb == vc:
                coz.append((va, ba, bb, bc))
print(f"\nOrtak cozum sayisi: {len(coz)}")
for va, ba, bb, bc in coz:
    print(f"  deger={va}: A taban {ba}, B taban {bb}, C taban {bc}")

print("\n'10' analizi:")
for b in TABANLAR:
    print(f"  10_{b} = {deger('10', b)}")
n5 = sum(1 for ba in TABANLAR for bb in TABANLAR for bc in TABANLAR
         if deger('10', ba) == deger('10', bb) == deger('10', bc))
print(f"  '10','10','10' ortak cozum sayisi: {n5} (tek degil)")
