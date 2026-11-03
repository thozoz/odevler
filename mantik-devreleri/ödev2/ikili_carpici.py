import sys
from typing import Dict, List, Tuple, Any

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except (AttributeError, OSError):
        pass


class GirdiHatasi(Exception):
    pass


TAM_TOPLAYICI_TABLOSU: Dict[Tuple[int, int, int], Tuple[int, int]] = {
    (0, 0, 0): (0, 0),
    (0, 0, 1): (1, 0),
    (0, 1, 0): (1, 0),
    (0, 1, 1): (0, 1),
    (1, 0, 0): (1, 0),
    (1, 0, 1): (0, 1),
    (1, 1, 0): (0, 1),
    (1, 1, 1): (1, 1),
}


def girdi_dogrula_carpma(a_str: str, b_str: str) -> Tuple[str, str]:
    if not isinstance(a_str, str) or not isinstance(b_str, str):
        raise GirdiHatasi("Girdiler metin tipinde olmalıdır.")
    a = a_str.strip()
    b = b_str.strip()
    if not a or not b:
        raise GirdiHatasi("Boş girdi kabul edilmez.")
    for ad, s in (("Çarpılan (A)", a), ("Çarpan (B)", b)):
        for ch in s:
            if ch not in ("0", "1"):
                raise GirdiHatasi(f"{ad} içinde geçersiz bit: '{ch}'.")
    return a, b


def _esit_uzunluk_topla(x_str: str, y_str: str) -> Tuple[str, int]:
    """Aynı uzunluktaki iki bit dizisini sağdan sola bit düzeyinde toplar."""
    uzunluk = len(x_str)
    elde = 0
    sonuc: List[str] = []
    for sagdan in range(uzunluk):
        idx = uzunluk - 1 - sagdan
        xb = 1 if x_str[idx] == "1" else 0
        yb = 1 if y_str[idx] == "1" else 0
        sb, elde = TAM_TOPLAYICI_TABLOSU[(xb, yb, elde)]
        sonuc.append(str(sb))
    return "".join(reversed(sonuc)), elde


def kismi_carpim_uret(a_str: str, b_bit: str, i: int, toplam_genislik: int) -> Dict[str, Any]:
    """i konumundaki çarpan biti (b_i) için kısmi çarpımı ve (n+m) bitlik sola kaydırılmış hizalı satırı üretir."""
    n = len(a_str)
    ham_kismi = a_str if b_bit == "1" else ("0" * n)
    sag_sifir = "0" * i
    sol_sifir_sayisi = toplam_genislik - (n + i)
    sol_sifir = "0" * sol_sifir_sayisi
    hizali = f"{sol_sifir}{ham_kismi}{sag_sifir}"

    return {
        "i": i,
        "b_i": int(b_bit),
        "ham_kismi": ham_kismi,
        "sol_sifir_sayisi": sol_sifir_sayisi,
        "sag_kaydirma": i,
        "hizali_satir": hizali,
        "ifade": f"{sol_sifir}[{ham_kismi}]{sag_sifir}",
    }


def ikili_carp_surum1(a_str: str, b_str: str) -> Dict[str, Any]:
    """Sürüm 1: Başlangıç akümülatörü 0^(n+m); her kısmi çarpım (0 dahil) bit düzeyi toplayıcıya gönderilir (m çağrı)."""
    a, b = girdi_dogrula_carpma(a_str, b_str)
    n, m = len(a), len(b)
    genislik = n + m

    akumulator = "0" * genislik
    toplama_cagrisi = 0
    satirlar: List[Dict[str, Any]] = []

    for i in range(m):
        b_bit = b[m - 1 - i]
        kp = kismi_carpim_uret(a, b_bit, i, genislik)
        akumulator, tasma = _esit_uzunluk_topla(akumulator, kp["hizali_satir"])
        assert tasma == 0, "n+m bit genişliğinde taşma olmamalıdır!"
        toplama_cagrisi += 1
        kp["ara_toplam"] = akumulator
        satirlar.append(kp)

    return {
        "surum": 1,
        "a": a,
        "b": b,
        "n": n,
        "m": m,
        "genislik": genislik,
        "sonuc": akumulator,
        "toplama_cagrisi": toplama_cagrisi,
        "satirlar": satirlar,
    }


def ikili_carp_surum2(a_str: str, b_str: str) -> Dict[str, Any]:
    """Sürüm 2: Başlangıç akümülatörü 0^(n+m); yalnız b_i == 1 olan kısmi çarpımlar toplayıcıya gönderilir (#1(B) çağrı)."""
    a, b = girdi_dogrula_carpma(a_str, b_str)
    n, m = len(a), len(b)
    genislik = n + m

    akumulator = "0" * genislik
    toplama_cagrisi = 0
    satirlar: List[Dict[str, Any]] = []

    for i in range(m):
        b_bit = b[m - 1 - i]
        kp = kismi_carpim_uret(a, b_bit, i, genislik)
        if b_bit == "1":
            akumulator, tasma = _esit_uzunluk_topla(akumulator, kp["hizali_satir"])
            assert tasma == 0
            toplama_cagrisi += 1
            kp["toplandi_mi"] = True
        else:
            kp["toplandi_mi"] = False
        kp["ara_toplam"] = akumulator
        satirlar.append(kp)

    return {
        "surum": 2,
        "a": a,
        "b": b,
        "n": n,
        "m": m,
        "genislik": genislik,
        "sonuc": akumulator,
        "toplama_cagrisi": toplama_cagrisi,
        "satirlar": satirlar,
    }


def uc_carpimi_goster() -> None:
    ornekler = [
        ("1011", "101"),
        ("10111", "110"),
        ("11001", "1010"),
    ]
    print("2. Üç Zorunlu Çarpım İçin n+m Bitlik Hizalı Kısmi Çarpım Tabloları:")
    for a, b in ornekler:
        s1 = ikili_carp_surum1(a, b)
        s2 = ikili_carp_surum2(a, b)
        assert s1["sonuc"] == s2["sonuc"]

        a_onlu = int(a, 2)
        b_onlu = int(b, 2)
        sonuc_onlu = int(s1["sonuc"], 2)
        assert sonuc_onlu == a_onlu * b_onlu

        print(f"\nİşlem: {a} ({a_onlu}) x {b} ({b_onlu})  [n={s1['n']}, m={s1['m']}, çıktı={s1['genislik']} bit]")
        print("  i | b_i | Kısmi Çarpım | Hizalı (n+m bit) | Onlu Katkı | Ara Toplam")
        katki_toplami = 0
        for st in s1["satirlar"]:
            katki = int(st["hizali_satir"], 2)
            katki_toplami += katki
            print(f"  {st['i']} |  {st['b_i']}  |     {st['ham_kismi']}    |     {st['hizali_satir']}     |    {katki:4d}    |  {st['ara_toplam']}")
        assert katki_toplami == sonuc_onlu
        print(f"  Sonuç: {s1['sonuc']} (Onlu: {sonuc_onlu}, Bağımsız kontrol: {a_onlu}x{b_onlu}={a_onlu*b_onlu})")
    print()


def sekiz_testi_calistir() -> List[Dict[str, Any]]:
    # Sıfır, bir, ikinin kuvveti ve tüm bitleri 1 olan çarpanları içeren 8 test
    testler = [
        ("Zorunlu 1 (11 x 5)", "1011", "101"),
        ("Zorunlu 2 (23 x 6)", "10111", "110"),
        ("Zorunlu 3 (25 x 10)", "11001", "1010"),
        ("Çarpan Sıfır (13 x 0)", "1101", "000"),
        ("Çarpan Bir (13 x 1)", "1101", "001"),
        ("Çarpan 2'nin Kuvveti (11 x 8)", "1011", "1000"),
        ("Çarpan Tüm Bitleri 1 (15 x 7)", "1111", "111"),
        ("Çarpılan 0, Çarpan Tüm 1 (0 x 15)", "0000", "1111"),
    ]
    print("3. Sekiz Senaryo ve İki Sürümün Toplama Çağrısı Karşılaştırması:")
    print("   Sayım kuralı: Başlangıç akümülatörü 0^(n+m) alınır; her `_esit_uzunluk_topla` çağrısı +1 sayılır.")
    print("   Sürüm 1 her satır için 1 kez, toplamda m kez çağrı yapar; Sürüm 2 yalnız b_i=1 olan satırlar için 1 kez, toplamda birlerin sayısı kadar çağrı yapar.\n")
    print(f"  {'#':<2} | {'Senaryo':<32} | {'A x B':<14} | {'Çıktı (n+m bit)':<10} | {'Onlu':<5} | {'S1 Çağrı':<8} | {'S2 Çağrı':<8}")
    print("  " + "-" * 96)

    ozet = []
    for idx, (ad, a, b) in enumerate(testler, 1):
        r1 = ikili_carp_surum1(a, b)
        r2 = ikili_carp_surum2(a, b)
        assert r1["sonuc"] == r2["sonuc"]
        ref = int(a, 2) * int(b, 2)
        assert int(r1["sonuc"], 2) == ref
        assert r1["toplama_cagrisi"] == len(b)
        assert r2["toplama_cagrisi"] == b.count("1")

        print(f"  {idx:<2} | {ad:<32} | {a+'x'+b:<14} | {r1['sonuc']:<10} | {ref:<5} | {r1['toplama_cagrisi']:<8} | {r2['toplama_cagrisi']:<8}")
        ozet.append({"ad": ad, "a": a, "b": b, "sonuc": r1["sonuc"], "onlu": ref, "s1": r1["toplama_cagrisi"], "s2": r2["toplama_cagrisi"]})
    print()
    return ozet


def genislik_gerekcesi_goster() -> None:
    print("4. Çıktı Genişliği (n + m Bit) Üst Sınır Gerekçesi ve Karşı Örnek:")
    print("  - n bitlik en büyük işaretsiz sayı: A_max = 2^n - 1")
    print("  - m bitlik en büyük işaretsiz sayı: B_max = 2^m - 1")
    print("  - En büyük çarpım: A_max * B_max = (2^n - 1)(2^m - 1) = 2^(n+m) - 2^n - 2^m + 1 < 2^(n+m) - 1.")
    print("  - Çarpım 2^(n+m)'den kesin küçük olduğundan her zaman (n + m) bitte taşmasız temsil edilir.")
    ornek = ikili_carp_surum1("11", "11")
    print(f"  - (n + m - 1) bitin yetmediğine küçük karşı örnek (n=2, m=2 -> n+m-1 = 3 bit):")
    print(f"    A = 11_2 (3), B = 11_2 (3) -> A x B = {ornek['sonuc']}_2 (9). 3 bit en fazla 111_2 (7) tutabilir; 9 için 4 bit zorunludur.")


if __name__ == "__main__":
    uc_carpimi_goster()
    sekiz_testi_calistir()
    genislik_gerekcesi_goster()
