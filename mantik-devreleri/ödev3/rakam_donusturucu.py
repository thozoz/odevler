"""BLM2007 Mantık Devreleri - Deney Yaprağı 1: Rakam Dönüştürücüsü

Desteklenen kodlar:
- 8421 BCD
- Artı-3 (Excess-3)
- Standart Aiken (2421, self-complementing)
"""

from typing import Dict, List, Set, Tuple


# Sözlükler (Rakam -> 4-bit kod)
BCD_SOZLUK: Dict[int, str] = {
    0: "0000",
    1: "0001",
    2: "0010",
    3: "0011",
    4: "0100",
    5: "0101",
    6: "0110",
    7: "0111",
    8: "1000",
    9: "1001",
}

ARTI3_SOZLUK: Dict[int, str] = {
    d: f"{d + 3:04b}" for d in range(10)
}

# Standart Aiken 2421 (Kendinden tümleyen standart sözlük)
AIKEN_SOZLUK: Dict[int, str] = {
    0: "0000",
    1: "0001",
    2: "0010",
    3: "0011",
    4: "0100",
    5: "1011",
    6: "1100",
    7: "1101",
    8: "1110",
    9: "1111",
}

# Ters sözlükler (4-bit kod -> Rakam)
BCD_TERS: Dict[str, int] = {v: k for k, v in BCD_SOZLUK.items()}
ARTI3_TERS: Dict[str, int] = {v: k for k, v in ARTI3_SOZLUK.items()}
AIKEN_TERS: Dict[str, int] = {v: k for k, v in AIKEN_SOZLUK.items()}


def kodla_rakam(rakam_karakteri: str, kod_turu: str) -> str:
    """Tek bir onlu rakamı seçilen koda göre 4 bitlik ikili desene kodlar."""
    if not rakam_karakteri.isdigit():
        raise ValueError(f"Geçersiz karakter: '{rakam_karakteri}'. Yalnızca 0-9 rakamları desteklenir.")
    d = int(rakam_karakteri)
    tur = kod_turu.lower()
    if tur in ("bcd", "8421"):
        return BCD_SOZLUK[d]
    elif tur in ("arti3", "arti-3", "excess-3", "excess3"):
        return ARTI3_SOZLUK[d]
    elif tur in ("aiken", "2421"):
        return AIKEN_SOZLUK[d]
    else:
        raise ValueError(f"Bilinmeyen kod türü: '{kod_turu}'. 'bcd', 'arti3' veya 'aiken' olmalıdır.")


def coz_dort_bit(blok: str, kod_turu: str) -> str:
    """4 bitlik bir kod sözcüğünü çözerek onlu rakam karakterine dönüştürür."""
    if len(blok) != 4 or not all(c in "01" for c in blok):
        raise ValueError(f"Hatalı bit bloğu: '{blok}'. Her blok 4 bitten (0 ve 1) oluşmalıdır.")
    tur = kod_turu.lower()
    if tur in ("bcd", "8421"):
        if blok not in BCD_TERS:
            val = int(blok, 2)
            raise ValueError(f"Geçersiz BCD sözcüğü: '{blok}' (onlu karşılığı {val} > 9).")
        return str(BCD_TERS[blok])
    elif tur in ("arti3", "arti-3", "excess-3", "excess3"):
        if blok not in ARTI3_TERS:
            val = int(blok, 2)
            raise ValueError(f"Geçersiz Artı-3 sözcüğü: '{blok}' (onlu karşılığı {val} < 3 veya > 12).")
        return str(ARTI3_TERS[blok])
    elif tur in ("aiken", "2421"):
        if blok not in AIKEN_TERS:
            # Aiken ağırlıklı toplamı hesaplayalım:
            w = [2, 4, 2, 1]
            toplam = sum(int(b) * w[i] for i, b in enumerate(blok))
            raise ValueError(f"Geçersiz Aiken sözcüğü: '{blok}' (ağırlıklı toplamı {toplam} olsa da standart sözlükte yer almaz).")
        return str(AIKEN_TERS[blok])
    else:
        raise ValueError(f"Bilinmeyen kod türü: '{kod_turu}'.")


def kodla_dize(onlu_dize: str, kod_turu: str, bosluklu: bool = False) -> str:
    """Onlu rakam dizisini (baştaki sıfırlar dahil) seçilen koda kodlar."""
    if not onlu_dize:
        raise ValueError("Girdi boş olamaz.")
    bloklar = [kodla_rakam(ch, kod_turu) for ch in onlu_dize]
    return " ".join(bloklar) if bosluklu else "".join(bloklar)


def coz_dize(bit_dizesi: str, kod_turu: str) -> str:
    """Bit dizisini 4'er bitlik parçalara bölerek onlu rakam dizisine çözer."""
    temiz = bit_dizesi.replace(" ", "")
    if not temiz:
        raise ValueError("Bit dizisi boş olamaz.")
    if len(temiz) % 4 != 0:
        raise ValueError(f"Yanlış bit uzunluğu: {len(temiz)} bit. Toplam bit sayısı 4'ün katı olmalıdır.")
    if not all(c in "01" for c in temiz):
        raise ValueError(f"Bit dizisi '0' ve '1' dışı karakterler içeremez: '{bit_dizesi}'")
    
    sonuc = []
    for i in range(0, len(temiz), 4):
        blok = temiz[i : i + 4]
        sonuc.append(coz_dort_bit(blok, kod_turu))
    return "".join(sonuc)


def desen_kumesi_analizi() -> Dict[str, Dict[str, List[str]]]:
    """16 adet 4-bit desenin (0000 - 1111) BCD, Artı-3 ve Aiken için geçerli/geçersiz kümelerini çıkarır."""
    desenler = [f"{i:04b}" for i in range(16)]
    kume = {}
    for ad, ters_sozluk in [("BCD", BCD_TERS), ("Arti3", ARTI3_TERS), ("Aiken", AIKEN_TERS)]:
        gecerli = [d for d in desenler if d in ters_sozluk]
        gecersiz = [d for d in desenler if d not in ters_sozluk]
        kume[ad] = {"gecerli": gecerli, "gecersiz": gecersiz}
    return kume


def dokuz_tumleyen_analizi(kod_turu: str) -> List[Tuple[int, str, str, str, int, bool]]:
    """0-9 rakamlarının kod bitlerini tersleyip (1 tümleyeni) çözer ve 9 - d ilişkisini sınar.
    Dönen tuple: (d, kod, ters_kod, cozulen_veya_hata, beklenen_rakam, basarili_mi)
    """
    tur = kod_turu.lower()
    sonuclar = []
    for d in range(10):
        kod = kodla_rakam(str(d), tur)
        ters_kod = "".join("1" if b == "0" else "0" for b in kod)
        beklenen = 9 - d
        try:
            cozulen = int(coz_dort_bit(ters_kod, tur))
            basari = (cozulen == beklenen)
            sonuclar.append((d, kod, ters_kod, str(cozulen), beklenen, basari))
        except ValueError as err:
            sonuclar.append((d, kod, ters_kod, f"GECERSIZ ({err.args[0][:25]}...)", beklenen, False))
    return sonuclar


def aiken_0101_ve_1011_karsilastir() -> Dict[str, any]:
    """Aiken 2421'de 0101 ve 1011 desenlerinin ağırlıklı toplamlarını ve geçerliliklerini inceler."""
    w = [2, 4, 2, 1]
    toplam_0101 = sum(int(b) * w[i] for i, b in enumerate("0101"))
    toplam_1011 = sum(int(b) * w[i] for i, b in enumerate("1011"))
    return {
        "0101": {"agirlik_toplami": toplam_0101, "sozlukte_var_mi": "0101" in AIKEN_TERS},
        "1011": {"agirlik_toplami": toplam_1011, "sozlukte_var_mi": "1011" in AIKEN_TERS, "temsil_edilen": AIKEN_TERS.get("1011")},
        "gerekce": (
            "0101 ve 1011 desenlerinin ikisinin de 2421 ağırlıklı toplamı 5'tir (0*2+1*4+0*2+1*1 = 5 "
            "ve 1*2+0*4+1*2+1*1 = 5). Fakat standart Aiken kodunda 'kendinden tümleyen' (self-complementing) "
            "kuralı gereği 5 rakamı, 4'ün (0100) 1 tümleyeni olan 1011 olarak belirlenmiştir. "
            "Bu nedenle 0101 deseni sözlük dışı bırakılmıştır ve geçersizdir. Ağırlıklı toplamın 5 çıkması "
            "desenin standart Aiken sözlüğünde geçerli olduğunu tek başına kanıtlamaz."
        ),
    }


def sayi_263_karsilastir() -> Dict[str, any]:
    """263 sayısının saf ikili ve BCD gösterimlerini bit sayısı ve yanlış kodla okuma açısından inceler."""
    saf_ikili = bin(263)[2:]  # '100000111'
    bcd = kodla_dize("263", "bcd", bosluklu=False)  # '001001100011'
    
    # 12 bitlik BCD deseni saf ikili gibi okunursa ne olur?
    yanlis_onlu = int(bcd, 2)
    
    return {
        "sayi": 263,
        "saf_ikili": saf_ikili,
        "saf_ikili_bit_sayisi": len(saf_ikili),
        "bcd": bcd,
        "bcd_bit_sayisi": len(bcd),
        "bit_orani_artis": (len(bcd) - len(saf_ikili)) / len(saf_ikili) * 100,
        "bcd_ikili_olarak_okunursa": yanlis_onlu,
        "aciklama": (
            f"263'ün saf ikili karşılığı 9 bitlik {saf_ikili}'dir. BCD karşılığı ise her rakam için 4 bit olmak üzere "
            f"12 bitlik {bcd}'dir (BCD %33.3 daha fazla bit harcar). Bu 12 bitlik BCD dizisi saf ikili olarak okunursa "
            f"değeri 2^9 + 2^6 + 2^5 + 2^1 + 2^0 = {yanlis_onlu} olarak tamamen yanlış yorumlanır."
        ),
    }
