from fractions import Fraction

print("=== DENEY YAPRAĞI 4 DOĞRULAMA ===")

sayilar = [Fraction(625, 1000), Fraction(1, 10), Fraction(65, 100), Fraction(975, 1000)]

for s in sayilar:
    bits = []
    rem = s
    for _ in range(9):
        rem *= 2
        b = int(rem)
        bits.append(b)
        rem -= b

    b8_trunc = bits[:8]
    val_trunc = sum(b8_trunc[i] * Fraction(1, 2**(i+1)) for i in range(8))
    err_trunc = abs(s - val_trunc)

    b9 = bits[8]
    rem_after_8 = s - val_trunc
    if rem_after_8 >= Fraction(1, 2**9):
        val_round = val_trunc + Fraction(1, 2**8)
    else:
        val_round = val_trunc

    err_round = abs(s - val_round)
    trunc_str = "0." + "".join(map(str, b8_trunc))

    r_bits = []
    r_rem = val_round
    for _ in range(8):
        r_rem *= 2
        b = int(r_rem)
        r_bits.append(b)
        r_rem -= b
    round_str = "0." + "".join(map(str, r_bits))

    print(f"Sayı: {float(s)}")
    print(f"  Kesilmiş: {trunc_str} = {float(val_trunc)} ({val_trunc}), Mutlak Hata: {float(err_trunc):.8f}")
    print(f"  Yuvarlanmış: {round_str} = {float(val_round)} ({val_round}), Mutlak Hata: {float(err_round):.8f}")
    print(f"  9. bit: {b9}, Kalan: {float(rem_after_8)}")
