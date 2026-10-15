baslangic = 173
print(f"Baslangic: {baslangic} = {format(baslangic, '08b')} = {format(baslangic, '02X')}")
for k in range(7, -1, -1):
    bit = (baslangic >> k) & 1
    hatali = baslangic ^ (1 << k)
    yon = "azaldi" if hatali < baslangic else "artti"
    hata = abs(hatali - baslangic)
    aralik = "YAKALANDI" if not (0 <= hatali <= 200) else "kacar"
    assert hata == 2 ** k
    print(f"k={k} bit {bit}->{1-bit}: {format(hatali,'08b')} = {hatali} ({hatali:02X}) | {yon} | hata {hata} | {aralik}")
print("Sadece 237 aralik disinda kaldi.")
