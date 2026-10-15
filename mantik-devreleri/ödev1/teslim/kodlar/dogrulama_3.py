# -*- coding: utf-8 -*-
"""Deney Yapragi 3 bagimsiz dogrulama (Fraction tabanli, float hatasiz)."""
from fractions import Fraction

def bin_frac(bits):
    return sum(int(b) * Fraction(1, 2 ** (i + 1)) for i, b in enumerate(bits))

tam_bin = "101101"
kes_bin = "01101"
tam_val = sum(int(b) * (2 ** (len(tam_bin) - 1 - i)) for i, b in enumerate(tam_bin))
kes_val = bin_frac(kes_bin)
print(f"Ikili {tam_bin}.{kes_bin} = {tam_val} + {kes_val} = {tam_val + kes_val} = {float(tam_val + kes_val)}")

oct_tam = 5 * 8 + 5
oct_kes = Fraction(3, 8) + Fraction(2, 64)
print(f"Sekizli 55.32 = {oct_tam} + {oct_kes} = {oct_tam + oct_kes} = {float(oct_tam + oct_kes)}")

hex_tam = 2 * 16 + 13
hex_kes = Fraction(6, 16) + Fraction(8, 256)
print(f"Onaltili 2D.68 = {hex_tam} + {hex_kes} = {hex_tam + hex_kes} = {float(hex_tam + hex_kes)}")

assert tam_val + kes_val == oct_tam + oct_kes == hex_tam + hex_kes == Fraction(45) + Fraction(13, 32)
print("OK: uc gosterim esit (45 + 13/32 = 45.40625)")

# Hatali ogrenci cozumu: kesre sola sifir -> 00001101
hat_kes = bin_frac("00001101")
hat_hex_kes = Fraction(0, 16) + Fraction(13, 256)
print(f"Hatali kesir 00001101 = {hat_kes} = {float(hat_kes)}, hex .0D = {hat_hex_kes} = {float(hat_hex_kes)}")
assert hat_kes == hat_hex_kes == Fraction(13, 256)
print(f"Hatali toplam = {45 + hat_kes} = {float(45 + hat_kes)}, fark = {float(Fraction(13,32) - hat_kes)}")
print("OK: hatali deger 45 + 13/256 = 45.05078125")

# Dusunme sorusu
a = 4 + 1 + Fraction(1, 2)
b = 4 + 1 + Fraction(1, 2)
print(f"00101.100 = {float(a)}, 101.1 = {float(b)}, esit mi: {a == b}")
