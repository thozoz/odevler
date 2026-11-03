import sys
from typing import Dict, List, Tuple, Any

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except (AttributeError, OSError):
        pass


class SifiraBolmeHatasi(Exception):
    pass


class GirdiHatasi(Exception):
    pass


TAM_CIKARICI_TABLOSU: Dict[Tuple[int, int, int], Tuple[int, int]] = {
    (0, 0, 0): (0, 0),
    (0, 0, 1): (1, 1),
    (0, 1, 0): (1, 1),
    (0, 1, 1): (0, 1),
    (1, 0, 0): (1, 0),
    (1, 0, 1): (0, 0),
    (1, 1, 0): (0, 0),
    (1, 1, 1): (1, 1),
}


def _sadeles(bit_str: str) -> str:
    s = bit_str.lstrip("0")
    return s if s else "0"


def _ikili_karsilastir_ge(a_str: str, b_str: str) -> bool:
    """a >= b ise True döner (tam sayıya çevirmeden bit dizisiyle karşılaştırır)."""
    a = _sadeles(a_str)
    b = _sadeles(b_str)
    if len(a) != len(b):
        return len(a) > len(b)
    return a >= b


def _ikili_cikar(ust_str: str, alt_str: str) -> str:
    """ust >= alt koşulunda bit düzeyinde çıkarma yapar."""
    uzunluk = max(len(ust_str), len(alt_str))
    u = ust_str.zfill(uzunluk)
    a = alt_str.zfill(uzunluk)
    borc = 0
    fark: List[str] = []
    for sagdan in range(uzunluk):
        idx = uzunluk - 1 - sagdan
        ub = 1 if u[idx] == "1" else 0
        ab = 1 if a[idx] == "1" else 0
        db, borc = TAM_CIKARICI_TABLOSU[(ub, ab, borc)]
        fark.append(str(db))
    assert borc == 0
    return _sadeles("".join(reversed(fark)))


def girdi_dogrula_bolme(bolunen_str: str, bolen_str: str) -> Tuple[str, str]:
    if not isinstance(bolunen_str, str) or not isinstance(bolen_str, str):
        raise GirdiHatasi("Girdiler metin tipinde olmalıdır.")
    d_b = bolunen_str.strip()
    d_k = bolen_str.strip()
    if not d_b or not d_k:
        raise GirdiHatasi("Boş girdi kabul edilmez.")
    for ad, s in (("Bölünen (D)", d_b), ("Bölen (d)", d_k)):
        for ch in s:
            if ch not in ("0", "1"):
                raise GirdiHatasi(f"{ad} içinde geçersiz bit: '{ch}'.")
    if _sadeles(d_k) == "0":
        raise SifiraBolmeHatasi(f"Sıfır bölen ({d_k!r}) kabul edilmez: Sıfıra bölme tanımsızdır!")
    return d_b, d_k


def ikili_bol(bolunen_str: str, bolen_str: str, max_kesir_basamak: int = 8) -> Dict[str, Any]:
    d_buyuk, d_kucuk = girdi_dogrula_bolme(bolunen_str, bolen_str)
    bolen_norm = _sadeles(d_kucuk)

    parca = "0"
    bolum_bitleri: List[str] = []
    tam_adimlar: List[Dict[str, Any]] = []

    for adim_no, bit in enumerate(d_buyuk, 1):
        incelenen = _sadeles(parca + bit)
        if _ikili_karsilastir_ge(incelenen, bolen_norm):
            q_bit = "1"
            kalan = _ikili_cikar(incelenen, bolen_norm)
        else:
            q_bit = "0"
            kalan = incelenen

        bolum_bitleri.append(q_bit)
        tam_adimlar.append({
            "adim": adim_no,
            "gelen_bit": bit,
            "incelenen_parca": incelenen,
            "bolum_biti": int(q_bit),
            "kalan": kalan,
        })
        parca = kalan

    tam_bolum_ham = "".join(bolum_bitleri)
    tam_bolum = _sadeles(tam_bolum_ham)
    tam_kalan = parca

    # Kesirli kısım: kalan sıfır değilse en çok max_kesir_basamak ikili kesir basamağı üret
    kesir_bitleri: List[str] = []
    kesir_adimlar: List[Dict[str, Any]] = []
    gorulen_kalanlar: Dict[str, int] = {}
    tekrar_eden_kalanlar: List[str] = []

    mevcut_kalan = tam_kalan
    if mevcut_kalan != "0" and max_kesir_basamak > 0:
        gorulen_kalanlar[mevcut_kalan] = 0
        for k_adim in range(1, max_kesir_basamak + 1):
            incelenen = _sadeles(mevcut_kalan + "0")
            if _ikili_karsilastir_ge(incelenen, bolen_norm):
                f_bit = "1"
                yeni_kalan = _ikili_cikar(incelenen, bolen_norm)
            else:
                f_bit = "0"
                yeni_kalan = incelenen

            kesir_bitleri.append(f_bit)
            tekrar_mi = yeni_kalan in gorulen_kalanlar and yeni_kalan != "0"
            if tekrar_mi:
                tekrar_eden_kalanlar.append(yeni_kalan)
            else:
                gorulen_kalanlar[yeni_kalan] = k_adim

            kesir_adimlar.append({
                "kesir_adim": k_adim,
                "onceki_kalan": mevcut_kalan,
                "incelenen_parca": incelenen,
                "kesir_biti": int(f_bit),
                "yeni_kalan": yeni_kalan,
                "tekrar_etti_mi": tekrar_mi,
            })
            mevcut_kalan = yeni_kalan
            if mevcut_kalan == "0":
                break

    kesin_mi = (mevcut_kalan == "0")
    isaret = "=" if kesin_mi else "≈"
    kesir_str = "".join(kesir_bitleri)
    kesirli_gosterim = f"{tam_bolum}.{kesir_str}" if kesir_str else tam_bolum

    return {
        "bolunen": d_buyuk,
        "bolen": d_kucuk,
        "tam_bolum_ham": tam_bolum_ham,
        "tam_bolum": tam_bolum,
        "tam_kalan": tam_kalan,
        "tam_adimlar": tam_adimlar,
        "kesir_bitleri": kesir_str,
        "kesir_adimlar": kesir_adimlar,
        "son_kesir_kalani": mevcut_kalan,
        "tekrar_eden_kalanlar": tekrar_eden_kalanlar,
        "kesirli_gosterim": kesirli_gosterim,
        "isaret": isaret,
        "kesin_mi": kesin_mi,
    }


def uc_zorunlu_bolmeyi_calistir() -> None:
    ornekler = [
        ("10110", "100"),
        ("1101", "10"),
        ("111", "11"),
    ]
    print("2 & 3. Üç Zorunlu Bölme İşlemi, Doğrulama Koşulları ve Kesirli Devam Kayıtları:")
    for d_b, d_k in ornekler:
        res = ikili_bol(d_b, d_k, max_kesir_basamak=8)
        D_val = int(d_b, 2)
        d_val = int(d_k, 2)
        Q_val = int(res["tam_bolum"], 2)
        R_val = int(res["tam_kalan"], 2)

        kosul1 = (D_val == Q_val * d_val + R_val)
        kosul2 = (0 <= R_val < d_val)
        assert kosul1 and kosul2

        print(f"\nİşlem: {d_b} ({D_val}) ÷ {d_k} ({d_val})")
        print(f"  Tam Bölüm Q = {res['tam_bolum']} (ham: {res['tam_bolum_ham']}, onlu: {Q_val}), Kalan R = {res['tam_kalan']} (onlu: {R_val})")
        print("  Tam Bölme Adımları (Soldan Sağa):")
        for ad in res["tam_adimlar"]:
            print(f"    Adım {ad['adim']}: gelen_bit={ad['gelen_bit']}, incelenen={ad['incelenen_parca']:>4}, q_biti={ad['bolum_biti']}, kalan={ad['kalan']}")
        print(f"  Kontrol 1 (D = Q*d + R): {D_val} = {Q_val}*{d_val} + {R_val} -> {kosul1}")
        print(f"  Kontrol 2 (0 <= R < d) : 0 <= {R_val} < {d_val} -> {kosul2}")
        print(f"  Kesirli Sonuç: {d_b} ÷ {d_k} {res['isaret']} {res['kesirli_gosterim']} (Kesin mi: {res['kesin_mi']}, Tekrar eden kalanlar: {res['tekrar_eden_kalanlar']})")
        if res["kesir_adimlar"]:
            print("  Kesir Adımları:")
            for kad in res["kesir_adimlar"]:
                print(
                    f"    Kesir {kad['kesir_adim']}: incelenen={kad['incelenen_parca']:>4}, "
                    f"kesir_biti={kad['kesir_biti']}, kalan={kad['yeni_kalan']} (tekrar={kad['tekrar_etti_mi']})"
                )
    print()


def sinir_testlerini_calistir() -> None:
    print("4. Sınır Testleri ve Bölümde Sıfır Bitinin Yanlış Atılması Örneği:")
    testler = [
        ("Sıfır bölünen (0 ÷ 5)", "0000", "101", "0", "0", "0", "="),
        ("Bölünenden büyük bölen (3 ÷ 6)", "011", "110", "0", "11", "0.1", "="),
        ("Eşit operandlar (5 ÷ 5)", "101", "101", "1", "0", "1", "="),
        ("Ara sıfır bitli bölüm (10 ÷ 2 = 5)", "1010", "10", "101", "0", "101", "="),
    ]
    for ad, d_b, d_k, bek_q, bek_r, bek_kesir, bek_isaret in testler:
        res = ikili_bol(d_b, d_k)
        assert res["tam_bolum"] == bek_q and res["tam_kalan"] == bek_r
        assert res["kesirli_gosterim"] == bek_kesir and res["isaret"] == bek_isaret
        print(
            f"  [{ad}] {d_b} ÷ {d_k} -> "
            f"Beklenen: Q={bek_q}, R={bek_r}, Kesirli={bek_isaret} {bek_kesir} | "
            f"Gözlenen: Q={res['tam_bolum']}, R={res['tam_kalan']}, Kesirli={res['isaret']} {res['kesirli_gosterim']} (EŞLEŞTİ)"
        )

    try:
        ikili_bol("101", "000")
    except SifiraBolmeHatasi as e:
        print(f"  [Sıfır bölen testi] '101 ÷ 000' -> REDDEDİLDİ: {e}")
    else:
        raise AssertionError("Sıfır bölen reddedilmedi!")


if __name__ == "__main__":
    uc_zorunlu_bolmeyi_calistir()
    sinir_testlerini_calistir()
