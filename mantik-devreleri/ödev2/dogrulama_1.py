from ikili_toplayici import GirdiHatasi, TAM_TOPLAYICI_TABLOSU, bit_duzeyi_topla

print("=== DENEY YAPRAĞI 1 DOĞRULAMA ===")

assert len(TAM_TOPLAYICI_TABLOSU) == 8
for (ai, bi, cin), (si, cout) in TAM_TOPLAYICI_TABLOSU.items():
    assert ai + bi + cin == cout * 2 + si

zorunlu_testler = [
    ("0101", "0011", 0, "1000", 0, 8),
    ("1111", "0001", 0, "0000", 1, 16),
    ("1111", "0000", 1, "0000", 1, 16),
    ("1111", "1111", 1, "1111", 1, 31),
]

for a, b, c0, bek_top, bek_elde, bek_onlu in zorunlu_testler:
    res = bit_duzeyi_topla(a, b, c0)
    assert res["toplam_bitleri"] == bek_top
    assert res["son_elde"] == bek_elde
    assert res["birlikte_onlu"] == bek_onlu
    print(f"{a} + {b} (c0={c0}) -> toplam={res['toplam_bitleri']}, son_elde={res['son_elde']}, onlu={res['birlikte_onlu']}: doğru")

sayac = 0
for c0 in (0, 1):
    for a_val in range(16):
        for b_val in range(16):
            res = bit_duzeyi_topla(format(a_val, "04b"), format(b_val, "04b"), c0)
            ref = a_val + b_val + c0
            n_bit = int(res["toplam_bitleri"], 2)
            assert n_bit + res["son_elde"] * 16 == ref
            sayac += 1
assert sayac == 512
print(f"4-bit 512 kombinasyon referans aritmetik ile doğrulandı: {sayac}/512")

sinir = bit_duzeyi_topla("1111", "0001", 0)
assert sinir["n_bit_onlu"] == 0 and sinir["birlikte_onlu"] == 16
print(f"Sınır örneği 1111 + 0001: son elde atılırsa {sinir['n_bit_onlu']}, korunursa {sinir['birlikte_onlu']} (kayıp 2^4 = 16)")

for hatali in [("", "0000", 0), ("0102", "0001", 0), ("0101", "101", 0), ("0101", "0011", 5)]:
    try:
        bit_duzeyi_topla(*hatali)
    except GirdiHatasi:
        pass
    else:
        raise AssertionError(f"Hatalı girdi yakalanmadı: {hatali}")

print("Deney 1 kontrolü tamam: 8 tablo satırı, 4 zorunlu işlem, 512 test ve ret kuralları doğrulandı.")
