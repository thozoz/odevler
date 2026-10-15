# -*- coding: utf-8 -*-
from fractions import Fraction
import math

print("=== DENEY YAPRAĞI 2 DOĞRULAMA ===")

adim = Fraction(1, 8)
print(f"Adım: {adim} = 2^-3 -> Kesir biti f = 3")

max_tam = 1000
tam_bit = math.ceil(math.log2(max_tam + 1))
print(f"Tam kısım için gereken bit: 2^{tam_bit} - 1 = {2**tam_bit - 1} >= 1000 -> i = {tam_bit}")
toplam_bit = tam_bit + 3
print(f"Toplam bit sayısı = {toplam_bit}")

# 12 bit yeterli mi?
max_val_12 = (2**9 - 1) + float(Fraction(7, 8))
print(f"12 bit - en büyük değer: {max_val_12} (1000'den küçük mü: {max_val_12 < 1000})")

durum_sayisi = int(1000 / 0.125) + 1
print(f"Gereken değer sayısı: {durum_sayisi}; 12 bit ile: {2**12} (Yeterli mi: {2**12 >= durum_sayisi})")

# 10 tam bit ve 3 kesir biti
def to_q10_3(val):
    tam = int(val)
    kesir = val - tam
    tam_bin = format(tam, '010b')
    kesir_val = int(round(kesir * 8))
    kesir_bin = format(kesir_val, '03b')
    return f"{tam_bin}.{kesir_bin}"


for v in [0.0, 0.125, 173.625, 1000.0]:
    print(f"Değer: {v:8.3f} -> {to_q10_3(v)}")

tam_oct = oct(173)[2:]
tam_hex = hex(173)[2:].upper()
print(f"173.625 sekizli: {tam_oct}.5")
print(f"173.625 onaltılı: {tam_hex}.A")
