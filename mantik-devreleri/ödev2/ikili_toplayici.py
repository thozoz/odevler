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


def girdi_dogrula(a_str: str, b_str: str, c0: int) -> Tuple[str, str, int]:
    if not isinstance(a_str, str) or not isinstance(b_str, str):
        raise GirdiHatasi("Girdiler metin (string) tipinde olmalıdır.")

    a = a_str.strip()
    b = b_str.strip()

    if not a or not b:
        raise GirdiHatasi("Boş girdi kabul edilmez.")

    for ad, metin in (("A", a), ("B", b)):
        for ch in metin:
            if ch not in ("0", "1"):
                raise GirdiHatasi(f"{ad} girdisinde geçersiz bit: '{ch}'. Sadece '0' ve '1' kullanılabilir.")

    if len(a) != len(b):
        raise GirdiHatasi(f"Farklı uzunluk kabul edilmez: len(A)={len(a)}, len(B)={len(b)}.")

    if c0 not in (0, 1) or isinstance(c0, bool):
        raise GirdiHatasi(f"Başlangıç eldesi 0 veya 1 olmalıdır (verilen: {c0!r}).")

    return a, b, c0


def bit_duzeyi_topla(a_str: str, b_str: str, c0: int = 0) -> Dict[str, Any]:
    a, b, elde = girdi_dogrula(a_str, b_str, c0)
    n = len(a)
    adimlar: List[Dict[str, int]] = []
    sonuc_bitleri: List[str] = []

    for sagdan_indeks in range(n):
        str_indeks = n - 1 - sagdan_indeks
        agirlik = 2 ** sagdan_indeks
        a_bit = 1 if a[str_indeks] == "1" else 0
        b_bit = 1 if b[str_indeks] == "1" else 0
        gelen_elde = elde

        toplam_biti, cikan_elde = TAM_TOPLAYICI_TABLOSU[(a_bit, b_bit, gelen_elde)]
        sonuc_bitleri.append(str(toplam_biti))

        adimlar.append({
            "sutun": sagdan_indeks,
            "agirlik": agirlik,
            "a_i": a_bit,
            "b_i": b_bit,
            "gelen_elde": gelen_elde,
            "sonuc_biti": toplam_biti,
            "cikan_elde": cikan_elde,
        })
        elde = cikan_elde

    toplam_str = "".join(reversed(sonuc_bitleri))
    n_bit_deger = sum(adim["sonuc_biti"] * adim["agirlik"] for adim in adimlar)
    son_elde_katkisi = elde * (2 ** n)
    birlikte_deger = n_bit_deger + son_elde_katkisi

    return {
        "a": a,
        "b": b,
        "c0": c0,
        "n": n,
        "toplam_bitleri": toplam_str,
        "son_elde": elde,
        "tam_sonuc_bitleri": f"{elde}{toplam_str}",
        "n_bit_onlu": n_bit_deger,
        "son_elde_katkisi": son_elde_katkisi,
        "birlikte_onlu": birlikte_deger,
        "adimlar": adimlar,
    }


def tablo_yazdir() -> None:
    print("1. Tam Toplayıcı Sonuç/Elde Tablosu (8 Olasılık):")
    print("a_i | b_i | c_in || s_i | c_out")
    print("----+-----+------++-----+------")
    for (ai, bi, cin), (si, cout) in TAM_TOPLAYICI_TABLOSU.items():
        print(f" {ai}  |  {bi}  |  {cin}   ||  {si}  |   {cout}")
    print()


def dort_islemi_calistir() -> List[Dict[str, Any]]:
    ornekler = [
        ("0101", "0011", 0, "1000", 0, 8),
        ("1111", "0001", 0, "0000", 1, 16),
        ("1111", "0000", 1, "0000", 1, 16),
        ("1111", "1111", 1, "1111", 1, 31),
    ]
    print("2. Dört Zorunlu İşlem ve Sütun Kayıtları:")
    kayitlar = []
    for a, b, c0, beklenen_toplam, beklenen_elde, beklenen_onlu in ornekler:
        sonuc = bit_duzeyi_topla(a, b, c0)
        assert sonuc["toplam_bitleri"] == beklenen_toplam
        assert sonuc["son_elde"] == beklenen_elde
        assert sonuc["birlikte_onlu"] == beklenen_onlu
        kayitlar.append(sonuc)

        print(f"\nİşlem: {a} + {b} (c0 = {c0})")
        print(f"  Beklenen : toplam={beklenen_toplam}, son_elde={beklenen_elde}, değer={beklenen_onlu}")
        print(f"  Gözlenen : toplam={sonuc['toplam_bitleri']}, son_elde={sonuc['son_elde']}, değer={sonuc['birlikte_onlu']}")
        print("  Sütun | Ağırlık | a_i | b_i | c_in | s_i | c_out")
        for adim in sonuc["adimlar"]:
            print(
                f"    {adim['sutun']}   |    {adim['agirlik']:2d}   |  {adim['a_i']}  |  {adim['b_i']}  |"
                f"  {adim['gelen_elde']}   |  {adim['sonuc_biti']}  |   {adim['cikan_elde']}"
            )
    print()
    return kayitlar


def tum_512_testi_calistir() -> Dict[str, int]:
    toplam_test = 0
    basarili = 0
    elde_1_sayisi = 0

    for c0 in (0, 1):
        for a_val in range(16):
            for b_val in range(16):
                a_str = format(a_val, "04b")
                b_str = format(b_val, "04b")
                sonuc = bit_duzeyi_topla(a_str, b_str, c0)

                referans = a_val + b_val + c0
                n_bit_deger = int(sonuc["toplam_bitleri"], 2)
                birlikte = n_bit_deger + sonuc["son_elde"] * (2 ** 4)

                assert birlikte == referans == sonuc["birlikte_onlu"]
                toplam_test += 1
                basarili += 1
                if sonuc["son_elde"] == 1:
                    elde_1_sayisi += 1

    print(f"3. 512 Test Özeti: {basarili}/{toplam_test} başarılı (Son elde=1 olan: {elde_1_sayisi}, Son elde=0 olan: {toplam_test - elde_1_sayisi}).\n")
    return {"toplam": toplam_test, "basarili": basarili, "elde_1": elde_1_sayisi}


def ret_testlerini_calistir() -> None:
    print("4. Hatalı Girdi (Ret) Testleri:")
    hatali_ornekler = [
        ("Boş girdi", "", "0101", 0),
        ("Geçersiz bit", "0121", "0011", 0),
        ("Farklı uzunluk", "0101", "11", 0),
        ("Geçersiz başlangıç eldesi", "0101", "0011", 2),
    ]
    for ad, a, b, c0 in hatali_ornekler:
        try:
            bit_duzeyi_topla(a, b, c0)
        except GirdiHatasi as e:
            print(f"  [{ad}] ({a!r}, {b!r}, c0={c0}) -> REDDEDİLDİ: {e}")
        else:
            raise AssertionError(f"Hatalı girdi reddedilmedi: {ad}")


if __name__ == "__main__":
    tablo_yazdir()
    dort_islemi_calistir()
    tum_512_testi_calistir()
    ret_testlerini_calistir()
