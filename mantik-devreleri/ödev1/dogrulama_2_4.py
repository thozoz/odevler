# -*- coding: utf-8 -*-
from fractions import Fraction
import math

print("=== DENEY YAPRAĞI 2 DOĞRULAMA ===")
# Adım 0.125
adim = Fraction(1, 8)
print(f"Adım: {adim} = 2^-3 -> Kesir biti f = 3")

# Aralık [0, 1000]
max_tam = 1000
tam_bit = math.ceil(math.log2(max_tam + 1))
print(f"Tam kısım için gereken bit: 2^{tam_bit} - 1 = {2**tam_bit - 1} >= 1000 -> i = {tam_bit}")
toplam_bit = tam_bit + 3
print(f"Toplam bit sayısı = {toplam_bit}")

# 12 bit yeterlilik
# Yöntem 1: Maksimum değer
max_val_12 = (2**9 - 1) + float(Fraction(7, 8))
print(f"12 bit Yöntem 1 Max Değer: {max_val_12} (1000'den küçük mü: {max_val_12 < 1000})")

# Yöntem 2: Durum sayısı
durum_sayisi = int(1000 / 0.125) + 1
print(f"Gereken durum sayısı: {durum_sayisi}, 12 bit kapasitesi: {2**12} (Yeterli mi: {2**12 >= durum_sayisi})")

# Değerlerin 13 bit gösterimleri (Q10.3)
def to_q10_3(val):
    tam = int(val)
    kesir = val - tam
    tam_bin = format(tam, '010b')
    kesir_val = int(round(kesir * 8))
    kesir_bin = format(kesir_val, '03b')
    return f"{tam_bin}.{kesir_bin}"

for v in [0.0, 0.125, 173.625, 1000.0]:
    print(f"Değer: {v:8.3f} -> Q10.3: {to_q10_3(v)}")

# 173.625 sekizli ve onaltılı
v = 173.625
tam_oct = oct(173)[2:]
# 0.625 * 8 = 5.0
print(f"173.625 Sekizli: {tam_oct}.5_8")
tam_hex = hex(173)[2:].upper()
# 0.625 * 16 = 10 -> A
print(f"173.625 Onaltılı: {tam_hex}.A_16")

print("\n=== DENEY YAPRAĞI 4 DOĞRULAMA ===")
sayilar = [Fraction(625, 1000), Fraction(1, 10), Fraction(65, 100), Fraction(975, 1000)]

for s in sayilar:
    flt = float(s)
    # İkili kesir basamakları (ilk 12 basamağı bulalım)
    bits = []
    rem = s
    for _ in range(12):
        rem *= 2
        b = int(rem)
        bits.append(b)
        rem -= b
    
    b8_trunc = bits[:8]
    val_trunc = sum(b8_trunc[i] * Fraction(1, 2**(i+1)) for i in range(8))
    err_trunc = abs(s - val_trunc)
    
    # Yuvarlama: 9. basamağa bakarak
    b9 = bits[8]
    # Kalan kesir tam yarımsa veya büyükse
    rem_after_8 = s - val_trunc
    half_lsb = Fraction(1, 2**9)
    if rem_after_8 > half_lsb or (rem_after_8 == half_lsb): # eşitlikte büyüğü seç
        val_round = val_trunc + Fraction(1, 2**8)
    else:
        val_round = val_trunc
    
    err_round = abs(s - val_round)
    
    trunc_str = "0." + "".join(map(str, b8_trunc))
    # round_str
    r_bits = []
    r_rem = val_round
    for _ in range(8):
        r_rem *= 2
        b = int(r_rem)
        r_bits.append(b)
        r_rem -= b
    round_str = "0." + "".join(map(str, r_bits))
    
    print(f"Sayı: {flt}")
    print(f"  Kesilmiş: {trunc_str} = {float(val_trunc)} ({val_trunc}), Mutlak Hata: {float(err_trunc):.8f}")
    print(f"  Yuvarlanmış: {round_str} = {float(val_round)} ({val_round}), Mutlak Hata: {float(err_round):.8f}")
    print(f"  9. bit: {b9}, Kalan: {float(rem_after_8)}")

