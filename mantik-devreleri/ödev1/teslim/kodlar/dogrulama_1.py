from fractions import Fraction

from sayi_donusturucu import GirdiHatasi, sayi_donustur


def onluk_deger(metin, taban):
    tam, nokta, kesir = metin.partition(".")
    deger = Fraction(int(tam or "0", taban))
    if nokta and kesir:
        deger += Fraction(int(kesir, taban), taban ** len(kesir))
    return deger


ornekler = [
    ("101101.01101", 2, 16, "2D.68", True),
    ("2D.68", 16, 8, "55.32", True),
    ("55.32", 8, 2, "101101.01101", True),
    ("0", 10, 2, "0", True),
    (".101", 2, 10, "0.625", True),
    ("001011.10", 2, 10, "11.5", True),
    ("0.1", 10, 2, "0.00011001", False),
    ("F.F", 16, 10, "15.9375", True),
    ("128", 10, 16, "80", True),
    ("7.7", 8, 16, "7.E", True),
]

for girdi, kaynak, hedef, beklenen, kesin in ornekler:
    sonuc = sayi_donustur(girdi, kaynak, hedef)
    assert sonuc["sonuc"] == beklenen, (girdi, sonuc["sonuc"], beklenen)
    assert sonuc["kesin_mi"] == kesin, (girdi, kesin)

    gercek = onluk_deger(girdi, kaynak)
    bulunan = onluk_deger(sonuc["sonuc"], hedef)
    if kesin:
        assert gercek == bulunan, girdi
    else:
        assert 0 < gercek - bulunan < Fraction(1, hedef ** 8), girdi
    print(f"{girdi} ({kaynak}) -> {sonuc['sonuc']} ({hedef}): doğru")

hatali_girdiler = [
    ("102", 2, 10),
    ("128", 8, 2),
    ("", 10, 2),
    ("10.11.01", 2, 16),
    ("-1", 10, 16),
    ("XYZ", 16, 10),
    (".", 2, 10),
]

for girdi, kaynak, hedef in hatali_girdiler:
    try:
        sayi_donustur(girdi, kaynak, hedef)
    except GirdiHatasi:
        print(f"Geçersiz girdi {girdi!r}: reddedildi")
    else:
        raise AssertionError(f"Geçersiz girdi kabul edildi: {girdi!r}")

print(f"Deney 1 kontrolü tamam: {len(ornekler)} dönüşüm, {len(hatali_girdiler)} hatalı giriş.")
