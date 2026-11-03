from fractions import Fraction
from ikili_bolucu import SifiraBolmeHatasi, ikili_bol

print("=== DENEY YAPRAĞI 4 DOĞRULAMA ===")

zorunlu = [
    ("10110", "100", "101", "10", "101.1", "=", True),
    ("1101", "10", "110", "1", "110.1", "=", True),
    ("111", "11", "10", "1", "10.01010101", "≈", False),
]

for d_b, d_k, bek_q, bek_r, bek_kesir, bek_isaret, bek_kesin in zorunlu:
    res = ikili_bol(d_b, d_k, max_kesir_basamak=8)
    assert res["tam_bolum"] == bek_q
    assert res["tam_kalan"] == bek_r
    assert res["kesirli_gosterim"] == bek_kesir
    assert res["isaret"] == bek_isaret
    assert res["kesin_mi"] == bek_kesin

    D_val, d_val = int(d_b, 2), int(d_k, 2)
    Q_val, R_val = int(res["tam_bolum"], 2), int(res["tam_kalan"], 2)
    assert D_val == Q_val * d_val + R_val and 0 <= R_val < d_val

    tam_kisim, _, kesir_kisim = res["kesirli_gosterim"].partition(".")
    deger = Fraction(int(tam_kisim, 2))
    if kesir_kisim:
        deger += Fraction(int(kesir_kisim, 2), 2 ** len(kesir_kisim))
    gercek = Fraction(D_val, d_val)
    if bek_kesin:
        assert deger == gercek
    else:
        assert 0 < gercek - deger < Fraction(1, 2 ** 8)
    print(f"{d_b} ÷ {d_k}: Q={bek_q}, R={bek_r}, Kesirli={bek_isaret} {bek_kesir} (onlu={float(deger):.6f}): doğru")

# Bölümde ara sıfır bitinin yanlış atılmasını yakalayan örnek: 1010 (10) ÷ 10 (2) = 101 (5)
ara_sifir = ikili_bol("1010", "10")
hatali_sifir_atan = "".join(str(ad["bolum_biti"]) for ad in ara_sifir["tam_adimlar"] if ad["bolum_biti"] != 0)
assert ara_sifir["tam_bolum"] == "101" and hatali_sifir_atan == "11"
print(f"Ara sıfır testi (1010 ÷ 10): Doğru Q={ara_sifir['tam_bolum']} (5); sıfır bitleri atılırsa {hatali_sifir_atan} (3) olur ve 3*2+0=6 != 10 ile yakalanır.")

try:
    ikili_bol("111", "0")
except SifiraBolmeHatasi:
    print("Sıfır bölen hatası doğrulandı.")
else:
    raise AssertionError("Sıfır bölen yakalanmadı!")

print("Deney 4 kontrolü tamam.")
