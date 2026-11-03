from ikili_cikarici import borc_alarak_cikar, iki_tumleyeniyle_cikar, iki_tumleyeni_naif_hatali

print("=== DENEY YAPRAĞI 2 DOĞRULAMA ===")

zorunlu_islemler = [
    ("1110", "0011", "1011", 11, 0, 1),
    ("0011", "1110", "-1011", -11, 1, 0),
    ("1000", "0001", "0111", 7, 0, 1),
    ("0101", "0101", "0000", 0, 0, 1),
    ("0011", "0000", "0011", 3, 0, 1),
]

for m, n, bek_gost, bek_onlu, bek_son_borc, bek_son_elde in zorunlu_islemler:
    b = borc_alarak_cikar(m, n)
    t = iki_tumleyeniyle_cikar(m, n)
    assert b["gosterim"] == t["gosterim"] == bek_gost
    assert b["onlu_sonuc"] == t["onlu_sonuc"] == bek_onlu
    assert b["son_borc"] == bek_son_borc
    assert t["son_elde"] == bek_son_elde
    print(f"{m} - {n}: Borç={b['gosterim']} (son_borç={b['son_borc']}), 2-Tümleyen={t['gosterim']} (son_elde={t['son_elde']}) -> {bek_onlu} doğru")

sayac = 0
for m_val in range(16):
    for n_val in range(16):
        m_s = format(m_val, "04b")
        n_s = format(n_val, "04b")
        ref = m_val - n_val
        ref_gost = "0000" if ref == 0 else (f"-{format(-ref, '04b')}" if ref < 0 else format(ref, "04b"))
        b = borc_alarak_cikar(m_s, n_s)
        t = iki_tumleyeniyle_cikar(m_s, n_s)
        assert b["onlu_sonuc"] == t["onlu_sonuc"] == ref
        assert b["gosterim"] == t["gosterim"] == ref_gost
        sayac += 1

assert sayac == 256
print(f"256 operand çiftinin tamamında iki algoritma ve referans fark eşleşti: {sayac}/256")

karsi_00 = iki_tumleyeni_naif_hatali("0000", "0000")
karsi_01 = iki_tumleyeni_naif_hatali("0001", "0000")
assert karsi_00["son_elde"] == 0 and karsi_00["gosterim"] == "-0000"
assert karsi_01["son_elde"] == 0 and karsi_01["onlu"] == -15
print(f"Karşı örnek N=0: M=0000 iken naif son_elde={karsi_00['son_elde']} ({karsi_00['gosterim']}); M=0001 iken naif son_elde={karsi_01['son_elde']} ({karsi_01['gosterim']} = {karsi_01['onlu']}, gerçek +1)")
print("Deney 2 kontrolü tamam.")
