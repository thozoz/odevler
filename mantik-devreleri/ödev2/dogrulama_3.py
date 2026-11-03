from ikili_carpici import ikili_carp_surum1, ikili_carp_surum2, sekiz_testi_calistir

print("=== DENEY YAPRAĞI 3 DOĞRULAMA ===")

zorunlu_uclu = [
    ("1011", "101", "0110111", 55, [11, 0, 44]),
    ("10111", "110", "10001010", 138, [0, 46, 92]),
    ("11001", "1010", "011111010", 250, [0, 50, 0, 200]),
]

for a, b, bek_sonuc, bek_onlu, bek_katkilar in zorunlu_uclu:
    r1 = ikili_carp_surum1(a, b)
    r2 = ikili_carp_surum2(a, b)
    assert r1["sonuc"] == r2["sonuc"] == bek_sonuc
    assert int(r1["sonuc"], 2) == bek_onlu == int(a, 2) * int(b, 2)
    katkilar = [int(st["hizali_satir"], 2) for st in r1["satirlar"]]
    assert katkilar == bek_katkilar and sum(katkilar) == bek_onlu
    print(f"{a} x {b} = {r1['sonuc']} ({bek_onlu}), katkılar={katkilar}, S1 çağrı={r1['toplama_cagrisi']}, S2 çağrı={r2['toplama_cagrisi']}: doğru")

ozet = sekiz_testi_calistir()
assert len(ozet) == 8

# n+m-1 bit karşı örneği: n=2, m=2, 11 x 11 = 1001 (4 bit, 3 bitte sığmaz)
karsi = ikili_carp_surum1("11", "11")
assert karsi["sonuc"] == "1001" and len(karsi["sonuc"].lstrip("0")) == 4
print("Karşı örnek: 11_2 (3) x 11_2 (3) = 1001_2 (9) -> n+m-1 = 3 bit (max 7) yetmez, n+m = 4 bit gerekir.")
print("Deney 3 kontrolü tamam.")
