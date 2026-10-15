# -*- coding: utf-8 -*-
"""Deney Yapragi 5 bagimsiz dogrulama (Fraction tabanli, float hatasiz)."""
from fractions import Fraction

# Iddia A: (0.65) vs (0.101)_2
sag_a = Fraction(1, 2) + Fraction(1, 8)  # 5/8
gercek_a = Fraction(65, 100)
print(f"A sag (0.101)_2 = {sag_a} = {float(sag_a)}, hata = {float(abs(gercek_a - sag_a))}")
assert sag_a == Fraction(5, 8) and abs(gercek_a - sag_a) == Fraction(1, 40)

# Iddia B: (0.975) vs (0.F99)_16
sag_b = Fraction(15, 16) + Fraction(9, 256) + Fraction(9, 4096)  # 3993/4096
gercek_b = Fraction(975, 1000)
print(f"B sag (0.F99)_16 = {sag_b} = {float(sag_b)}, hata = {float(abs(gercek_b - sag_b))}")
assert sag_b == Fraction(3993, 4096)

# Iddia C: dogru 2D.68 vs hatali 2D.0D
dogru_kesir = Fraction(6, 16) + Fraction(8, 256)  # 13/32
hatali_kesir = Fraction(13, 256)
print(f"C dogru kesir .68 = {dogru_kesir} = {float(dogru_kesir)}")
print(f"C hatali kesir .0D = {hatali_kesir} = {float(hatali_kesir)}")
assert dogru_kesir == Fraction(13, 32) and hatali_kesir == Fraction(13, 256)
print(f"C fark = {float(dogru_kesir - hatali_kesir)} (mutlak hata 0.35546875)")

# Iddia D: saga sifir = x2
for v in [1, 5]:
    print(f"D ornek: {v} -> saga 1 sifir -> {v * 2} (x2, degisir)")
print("OK: A,B yaklasik; C hatali basamak; D yanlis (saga sifir x2).")
