import sys
from typing import Tuple, List, Dict, Any

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except (AttributeError, OSError):
        pass

GECERLI_TABANLAR = {2, 8, 10, 16}

CHAR_TO_VAL = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
    '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
    'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15
}

VAL_TO_CHAR = {
    0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
    5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
    10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'
}


class GirdiHatasi(Exception):
    pass


def girdi_dogrula(sayi_metni: str, kaynak_taban: int, hedef_taban: int) -> Tuple[str, str]:
    if kaynak_taban not in GECERLI_TABANLAR:
        raise GirdiHatasi(f"Geçersiz kaynak taban ({kaynak_taban}). İzin verilenler: {sorted(GECERLI_TABANLAR)}")
    if hedef_taban not in GECERLI_TABANLAR:
        raise GirdiHatasi(f"Geçersiz hedef taban ({hedef_taban}). İzin verilenler: {sorted(GECERLI_TABANLAR)}")

    if not isinstance(sayi_metni, str):
        raise GirdiHatasi("Girdi metin (string) tipinde olmalıdır.")

    metin = sayi_metni.strip()
    if not metin:
        raise GirdiHatasi("Girdi boş olamaz.")

    if metin.startswith('-'):
        raise GirdiHatasi("Negatif sayılar kabul edilmez. Sayı negatif olmayan bir değer olmalıdır.")

    if metin.count('.') > 1:
        raise GirdiHatasi(f"Birden fazla kesir ayracı ('.') bulundu ({metin.count('.')} adet).")

    tam_str, _, kesir_str = metin.partition('.')
    if not tam_str and not kesir_str:
        raise GirdiHatasi("Kesir ayracı haricinde hiçbir rakam girilmedi.")

    tam_str = tam_str or "0"
    for ch in tam_str + kesir_str:
        if ch not in CHAR_TO_VAL:
            raise GirdiHatasi(f"Tanımsız karakter: '{ch}'.")
        val = CHAR_TO_VAL[ch]
        if val >= kaynak_taban:
            raise GirdiHatasi(
                f"Karakter '{ch}' (değer={val}) taban {kaynak_taban} için geçersizdir! "
                f"Taban {kaynak_taban} rakamları 0 ile {kaynak_taban - 1} arasında olmalıdır."
            )
    return tam_str, kesir_str


def tam_kisim_onluya_cevir(tam_str: str, kaynak_taban: int) -> int:
    toplam = 0
    for ch in tam_str:
        val = CHAR_TO_VAL[ch]
        toplam = toplam * kaynak_taban + val
    return toplam


def tam_kisim_hedefe_cevir(onlu_deger: int, hedef_taban: int) -> str:
    if onlu_deger == 0:
        return "0"

    kalanlar = []
    while onlu_deger > 0:
        kalan = onlu_deger % hedef_taban
        kalanlar.append(VAL_TO_CHAR[kalan])
        onlu_deger //= hedef_taban

    return "".join(reversed(kalanlar))


def kesir_onlu_rasyonel(kesir_str: str, kaynak_taban: int) -> Tuple[int, int]:
    if not kesir_str:
        return 0, 1

    pay = 0
    payda = 1
    for ch in kesir_str:
        val = CHAR_TO_VAL[ch]
        pay = pay * kaynak_taban + val
        payda = payda * kaynak_taban

    return pay, payda


def kesir_hedefe_cevir_rasyonel(pay: int, payda: int, hedef_taban: int, max_basamak: int = 8) -> Tuple[str, bool]:
    if pay == 0:
        return "0", True

    basamaklar = []
    mevcut_pay = pay
    for _ in range(max_basamak):
        carpim = mevcut_pay * hedef_taban
        basamak = carpim // payda
        mevcut_pay = carpim % payda
        basamaklar.append(VAL_TO_CHAR[basamak])

        if mevcut_pay == 0:
            return "".join(basamaklar), True

    return "".join(basamaklar), False


def sayi_donustur(sayi_metni: str, kaynak_taban: int, hedef_taban: int) -> Dict[str, Any]:
    tam_str, kesir_str = girdi_dogrula(sayi_metni, kaynak_taban, hedef_taban)

    tam_onlu = tam_kisim_onluya_cevir(tam_str, kaynak_taban)
    tam_hedef = tam_kisim_hedefe_cevir(tam_onlu, hedef_taban)

    if kesir_str:
        pay, payda = kesir_onlu_rasyonel(kesir_str, kaynak_taban)
        kesir_hedef, kesin_mi = kesir_hedefe_cevir_rasyonel(pay, payda, hedef_taban, max_basamak=8)

        sonuc_metni = f"{tam_hedef}.{kesir_hedef}"
        isaret = "=" if kesin_mi else "≈"
        durum = "Kesin" if kesin_mi else "Yaklaşık (8 basamakta kesildi)"
        kesir_onlu_ondalik = pay / payda
    else:
        kesir_hedef = ""
        kesin_mi = True
        sonuc_metni = tam_hedef
        isaret = "="
        durum = "Kesin"
        kesir_onlu_ondalik = 0.0

    return {
        "girdi": sayi_metni,
        "kaynak_taban": kaynak_taban,
        "hedef_taban": hedef_taban,
        "tam_kaynak": tam_str,
        "kesir_kaynak": kesir_str,
        "tam_onlu": tam_onlu,
        "kesir_onlu_ondalik": kesir_onlu_ondalik,
        "toplam_onlu": tam_onlu + kesir_onlu_ondalik,
        "tam_hedef": tam_hedef,
        "kesir_hedef": kesir_hedef,
        "sonuc": sonuc_metni,
        "isaret": isaret,
        "kesin_mi": kesin_mi,
        "durum": durum
    }


def test_suite_calistir() -> List[Dict]:
    senaryolar = [
        ("İkiliden onaltılıya", "101101.01101", 2, 16, False, "2D.68"),
        ("Sıfır", "0", 10, 2, False, "0"),
        ("Noktadan başlayan sayı", ".101", 2, 10, False, "0.625"),
        ("Baştaki sıfırlar", "001011.10", 2, 10, False, "11.5"),
        ("Bitmeyen kesir", "0.1", 10, 2, False, "0.00011001"),
        ("Onaltılıdan sekizliye", "2D.68", 16, 8, False, "55.32"),
        ("İkili tabanda 2", "102", 2, 10, True, "taban 2 için geçersizdir"),
        ("Sekizli tabanda 8", "128", 8, 2, True, "taban 8 için geçersizdir"),
        ("Boş giriş", "   ", 10, 2, True, "Girdi boş olamaz"),
        ("İki tane nokta", "10.11.01", 2, 16, True, "Birden fazla kesir ayracı"),
        ("Negatif sayı", "-101.1", 2, 10, True, "Negatif sayılar kabul edilmez"),
        ("Geçersiz taban", "101", 5, 2, True, "Geçersiz kaynak taban")
    ]

    sonuclar = []
    print("Deney 1 - Dönüştürücü testleri")

    for i, (tanim, girdi, r_kaynak, r_hedef, hata_bekleniyor, beklenen) in enumerate(senaryolar, 1):
        try:
            res = sayi_donustur(girdi, r_kaynak, r_hedef)
            if hata_bekleniyor:
                print(f"{i}. {tanim}: hata vermesi gerekiyordu, {res['sonuc']} çıktı")
                basarili = False
            else:
                eslesme = (res['sonuc'] == beklenen)
                print(f"{i}. {tanim}: {res['sonuc']} ({'doğru' if eslesme else 'yanlış, beklenen: ' + beklenen})")
                basarili = eslesme
            sonuclar.append({"test_no": i, "tanim": tanim, "girdi": girdi, "r1": r_kaynak, "r2": r_hedef,
                             "basarili": basarili, "cikti": res['sonuc'], "durum": res['durum']})
        except GirdiHatasi as e:
            if hata_bekleniyor:
                basarili = beklenen.casefold() in str(e).casefold()
                print(f"{i}. {tanim}: {'beklenen hatayı verdi' if basarili else 'yanlış hata verdi'}")
            else:
                print(f"{i}. {tanim}: beklenmeyen hata: {e}")
                basarili = False
            sonuclar.append({"test_no": i, "tanim": tanim, "girdi": girdi, "r1": r_kaynak, "r2": r_hedef,
                             "basarili": basarili, "cikti": f"HATA: {e}", "durum": "REDDEDİLDİ"})

    basarili_test = sum(1 for s in sonuclar if s['basarili'])
    print(f"\n{basarili_test}/{len(sonuclar)} test doğru.")
    return sonuclar


if __name__ == "__main__":
    sonuclar = test_suite_calistir()
    if not all(test['basarili'] for test in sonuclar):
        raise SystemExit(1)
