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


def girdi_dogrula_4bit(m_str: str, n_str: str) -> Tuple[str, str]:
    if not isinstance(m_str, str) or not isinstance(n_str, str):
        raise GirdiHatasi("Girdiler metin tipinde olmalıdır.")
    m = m_str.strip()
    n = n_str.strip()
    if len(m) != 4 or len(n) != 4:
        raise GirdiHatasi(f"M ve N dört bitlik olmalıdır (verilen: {m!r}, {n!r}).")
    for ad, s in (("M", m), ("N", n)):
        for ch in s:
            if ch not in ("0", "1"):
                raise GirdiHatasi(f"{ad} içinde geçersiz bit: '{ch}'.")
    return m, n


def _borc_zinciri_uygula(ust: str, alt: str) -> Tuple[str, int, List[Dict[str, int]]]:
    n = len(ust)
    borc = 0
    fark_bitleri: List[str] = []
    adimlar: List[Dict[str, int]] = []

    for sagdan in range(n):
        idx = n - 1 - sagdan
        u_bit = 1 if ust[idx] == "1" else 0
        a_bit = 1 if alt[idx] == "1" else 0
        gelen_borc = borc
        d_bit, cikan_borc = TAM_CIKARICI_TABLOSU[(u_bit, a_bit, gelen_borc)]
        fark_bitleri.append(str(d_bit))
        adimlar.append({
            "sutun": sagdan,
            "agirlik": 2 ** sagdan,
            "ust_bit": u_bit,
            "alt_bit": a_bit,
            "gelen_borc": gelen_borc,
            "fark_biti": d_bit,
            "cikan_borc": cikan_borc,
        })
        borc = cikan_borc

    return "".join(reversed(fark_bitleri)), borc, adimlar


def borc_alarak_cikar(m_str: str, n_str: str) -> Dict[str, Any]:
    m, n = girdi_dogrula_4bit(m_str, n_str)
    ham_fark, son_borc, ilk_adimlar = _borc_zinciri_uygula(m, n)

    if son_borc == 0:
        buyukluk_str = ham_fark
        duzeltme_adimlari = None
        if buyukluk_str == "0000":
            isaret = ""
            gosterim = "0000"
            durum = "Sıfır"
        else:
            isaret = ""
            gosterim = buyukluk_str
            durum = "Pozitif"
    else:
        # M < N durumu: son borç = 1. Büyüklük N - M borç zinciriyle (veya 2^4 - ham_fark) bulunur.
        buyukluk_str, _, duzeltme_adimlari = _borc_zinciri_uygula(n, m)
        isaret = "-"
        gosterim = f"-{buyukluk_str}"
        durum = "Negatif"

    buyukluk_onlu = sum((1 if ch == "1" else 0) * (2 ** (3 - i)) for i, ch in enumerate(buyukluk_str))
    onlu_sonuc = -buyukluk_onlu if isaret == "-" else buyukluk_onlu

    return {
        "yontem": "Borç Alarak Doğrudan Çıkarma",
        "m": m,
        "n": n,
        "ham_fark": ham_fark,
        "son_borc": son_borc,
        "borc_zinciri": [adim["cikan_borc"] for adim in ilk_adimlar],
        "isaret": isaret,
        "buyukluk": buyukluk_str,
        "gosterim": gosterim,
        "durum": durum,
        "onlu_sonuc": onlu_sonuc,
        "adimlar": ilk_adimlar,
        "negatif_buyukluk_adimlari": duzeltme_adimlari,
    }


def _bit_tersle(bit_str: str) -> str:
    return "".join("1" if ch == "0" else "0" for ch in bit_str)


def _topla_bit_duzeyi(a_str: str, b_str: str, c0: int = 0) -> Tuple[str, int, List[Dict[str, int]]]:
    n = len(a_str)
    elde = c0
    toplam_bitleri: List[str] = []
    adimlar: List[Dict[str, int]] = []

    for sagdan in range(n):
        idx = n - 1 - sagdan
        a_bit = 1 if a_str[idx] == "1" else 0
        b_bit = 1 if b_str[idx] == "1" else 0
        gelen_elde = elde
        s_bit, cikan_elde = TAM_TOPLAYICI_TABLOSU[(a_bit, b_bit, gelen_elde)]
        toplam_bitleri.append(str(s_bit))
        adimlar.append({
            "sutun": sagdan,
            "agirlik": 2 ** sagdan,
            "a_i": a_bit,
            "b_i": b_bit,
            "gelen_elde": gelen_elde,
            "toplam_biti": s_bit,
            "cikan_elde": cikan_elde,
        })
        elde = cikan_elde

    return "".join(reversed(toplam_bitleri)), elde, adimlar


def iki_tumleyeniyle_cikar(m_str: str, n_str: str) -> Dict[str, Any]:
    m, n = girdi_dogrula_4bit(m_str, n_str)

    n_1_tumleyen = _bit_tersle(n)
    n_2_tumleyen, n_tumleyen_elde, _ = _topla_bit_duzeyi(n_1_tumleyen, "0001", 0)

    # M + (~N + 1) işlemini M + ~N + (c0 = 1) olarak tek 4-bit toplayıcıda yürütelim:
    ham_toplam, son_elde, toplama_adimlari = _topla_bit_duzeyi(m, n_1_tumleyen, 1)

    # N = 0000 iken ~N + 1 = 1111 + 1 = (1)0000 -> 4-bit 2'nin tümleyeni 0000 olur ve M + ~N + 1 her zaman son_elde = 1 üretir.
    if ham_toplam == "0000":
        # Sıfır durumu ayrıca ele alınır (ör. 0101 - 0101 veya 0000 - 0000)
        isaret = ""
        buyukluk_str = "0000"
        gosterim = "0000"
        durum = "Sıfır"
        buyukluk_tumleyen = None
    elif son_elde == 1:
        # Son elde = 1 ve sonuç != 0000 ise M > N (Pozitif)
        isaret = ""
        buyukluk_str = ham_toplam
        gosterim = buyukluk_str
        durum = "Pozitif"
        buyukluk_tumleyen = None
    else:
        # Son elde = 0 ve ham_toplam != 0000 ise M < N (Negatif); büyüklük ham_toplam'ın 2'nin tümleyenidir
        isaret = "-"
        ters = _bit_tersle(ham_toplam)
        buyukluk_str, _, _ = _topla_bit_duzeyi(ters, "0001", 0)
        gosterim = f"-{buyukluk_str}"
        durum = "Negatif"
        buyukluk_tumleyen = {"ters": ters, "buyukluk": buyukluk_str}

    buyukluk_onlu = sum((1 if ch == "1" else 0) * (2 ** (3 - i)) for i, ch in enumerate(buyukluk_str))
    onlu_sonuc = -buyukluk_onlu if isaret == "-" else buyukluk_onlu

    return {
        "yontem": "2 Tümleyeniyle Çıkarma",
        "m": m,
        "n": n,
        "n_1_tumleyen": n_1_tumleyen,
        "n_2_tumleyen_4bit": n_2_tumleyen,
        "n_2_tumleyen_tasma": n_tumleyen_elde,
        "ham_toplam": ham_toplam,
        "son_elde": son_elde,
        "elde_zinciri": [adim["cikan_elde"] for adim in toplama_adimlari],
        "isaret": isaret,
        "buyukluk": buyukluk_str,
        "gosterim": gosterim,
        "durum": durum,
        "onlu_sonuc": onlu_sonuc,
        "adimlar": toplama_adimlari,
        "negatif_buyukluk_hesabi": buyukluk_tumleyen,
    }


def iki_tumleyeni_naif_hatali(m_str: str, n_str: str) -> Dict[str, Any]:
    """N'nin 4-bit 2'nin tümleyenini alıp c0=0 ile M'ye ekleyen ve 'son_elde==0 ise negatiftir' diyen naif sürüm."""
    m, n = girdi_dogrula_4bit(m_str, n_str)
    n_1 = _bit_tersle(n)
    n_2, _, _ = _topla_bit_duzeyi(n_1, "0001", 0)  # N=0000 için n_2 = 0000 (5. bit olan 1 kayboldu!)
    ham_toplam, son_elde, _ = _topla_bit_duzeyi(m, n_2, 0)
    # Naif iddia: "Son elde yoksa (son_elde == 0) sonuç mutlaka negatiftir"
    if son_elde == 0:
        ters = _bit_tersle(ham_toplam)
        buyukluk_str, _, _ = _topla_bit_duzeyi(ters, "0001", 0)
        isaret = "-"
        gosterim = f"-{buyukluk_str}"
        buyukluk_onlu = sum((1 if ch == "1" else 0) * (2 ** (3 - i)) for i, ch in enumerate(buyukluk_str))
        onlu = -buyukluk_onlu
    else:
        isaret = ""
        buyukluk_str = ham_toplam
        gosterim = buyukluk_str
        onlu = sum((1 if ch == "1" else 0) * (2 ** (3 - i)) for i, ch in enumerate(buyukluk_str))
    return {"m": m, "n": n, "n_2": n_2, "ham_toplam": ham_toplam, "son_elde": son_elde, "gosterim": gosterim, "onlu": onlu}


def bes_islemi_coz() -> None:
    islemler = [
        ("1110", "0011"),
        ("0011", "1110"),
        ("1000", "0001"),
        ("0101", "0101"),
        ("0011", "0000"),
    ]
    print("2. Beş Zorunlu İşlemin İki Yöntemle Çözümü ve Ara Kayıtları:")
    for m, n in islemler:
        b_res = borc_alarak_cikar(m, n)
        t_res = iki_tumleyeniyle_cikar(m, n)
        assert b_res["gosterim"] == t_res["gosterim"]
        assert b_res["onlu_sonuc"] == t_res["onlu_sonuc"] == int(m, 2) - int(n, 2)

        print(f"\nİşlem: {m} ({int(m,2)}) - {n} ({int(n,2)})")
        print(f"  [Borç Yöntemi]     Ham fark={b_res['ham_fark']}, Borç zinciri(sütun 0->3)={b_res['borc_zinciri']}, Son borç={b_res['son_borc']} -> Sonuç: {b_res['gosterim']} ({b_res['onlu_sonuc']})")
        print(f"  [2 Tümleyeni Yön.] ~N={t_res['n_1_tumleyen']}, 4-bit(-N)={t_res['n_2_tumleyen_4bit']}, Ham toplam={t_res['ham_toplam']}, Elde zinciri(sütun 0->3)={t_res['elde_zinciri']}, Son elde={t_res['son_elde']} -> Sonuç: {t_res['gosterim']} ({t_res['onlu_sonuc']})")
    print()


def tum_256_testi_calistir() -> None:
    print("3. 0-15 Aralığındaki 256 Operand Çiftinin Sınanması:")
    naif_ilk_hata = None
    dogru_sayac = 0

    for m_val in range(16):
        for n_val in range(16):
            m_str = format(m_val, "04b")
            n_str = format(n_val, "04b")
            ref = m_val - n_val
            ref_gosterim = "0000" if ref == 0 else (f"-{format(-ref, '04b')}" if ref < 0 else format(ref, "04b"))

            naif = iki_tumleyeni_naif_hatali(m_str, n_str)
            if (naif["onlu"] != ref or naif["gosterim"] != ref_gosterim) and naif_ilk_hata is None:
                naif_ilk_hata = (m_str, n_str, ref, ref_gosterim, naif)

            b_res = borc_alarak_cikar(m_str, n_str)
            t_res = iki_tumleyeniyle_cikar(m_str, n_str)
            assert b_res["onlu_sonuc"] == ref, (m_str, n_str, b_res)
            assert t_res["onlu_sonuc"] == ref, (m_str, n_str, t_res)
            assert b_res["gosterim"] == t_res["gosterim"]
            dogru_sayac += 1

    print(f"  Doğrudan borç ve düzeltilmiş 2 tümleyeni algoritmaları: {dogru_sayac}/256 başarılı.")
    if naif_ilk_hata:
        m_s, n_s, ref, ref_gost, naif = naif_ilk_hata
        print(f"  [Naif Sürüm Uyumsuzluk Kaydı] İlk hatalı çift: M={m_s}, N={n_s} (beklenen={ref_gost} [{ref}], naif çıktı={naif['gosterim']} [{naif['onlu']}])")
        naif_01 = iki_tumleyeni_naif_hatali("0001", "0000")
        print(f"  [Sayısal Fark Hatalı İlk Çift] M=0001, N=0000 (beklenen=0001 [+1], naif çıktı={naif_01['gosterim']} [{naif_01['onlu']}])")
        print(f"    Ara adım: N={n_s} için 4-bit 2 tümleyeni {naif['n_2']} alındığında M + N_2 = {naif['ham_toplam']} ve son_elde={naif['son_elde']} üretildi.")
        print("    Düzeltme: Çıkarma M + ~N + 1 (başlangıç eldesi c0=1) olarak yapılmalı ve sıfır durumu (0000) işaret atamasından önce ayrılmalıdır.\n")


def sifir_karsi_ornek_analizi() -> None:
    print("4. 'Son elde yoksa sonuç mutlaka negatiftir' İddiasının N = 0 ile Sınanması:")
    print("  a) 4-bit kesilmiş 2 tümleyeni yaklaşımında (M + two_comp_4bit(N)):")
    print("     N = 0000'ın 4-bit 2 tümleyeni ~0000 + 1 = 1111 + 1 = (1)0000 -> 4 bitte 0000'dır.")
    print("     En küçük karşı örnek M = 0000, N = 0000: 0000 + 0000 = 0000, son_elde = 0.")
    print("     Pozitif karşı örnek M = 0001, N = 0000: 0001 + 0000 = 0001 (+1), son_elde = 0 (Sonuç negatif değil, +1!).")
    print("  b) Standart donanım yaklaşımında (M + ~N + 1):")
    print("     N = 0000 iken ~N = 1111 ve c0 = 1 olduğundan M + 1111 + 1 = M + 10000_2 her M için son_elde = 1 üretir.")


if __name__ == "__main__":
    bes_islemi_coz()
    tum_256_testi_calistir()
    sifir_karsi_ornek_analizi()
