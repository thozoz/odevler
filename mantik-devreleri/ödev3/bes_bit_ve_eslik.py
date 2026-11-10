"""BLM2007 Mantık Devreleri - Deney Yaprağı 3: Beş Bitte İki Bir ve Eşlik Denetimi

5'te 2 (2-out-of-5) ve Çift/Tek Eşlik (Parity) algoritmaları,
Hata saptama/kaçırma oranları, tek/iki bit hata taramaları ve düzeltme sınırı.
"""

from itertools import combinations
from typing import Dict, List, Optional, Tuple


# 5'te 2 Sözlüğü (7-4-2-1-0 Ağırlıkları)
BES_TE_IKI_SOZLUK: Dict[int, str] = {
    0: "11000",
    1: "00011",
    2: "00101",
    3: "00110",
    4: "01001",
    5: "01010",
    6: "01100",
    7: "10001",
    8: "10010",
    9: "10100",
}

BES_TE_IKI_TERS: Dict[str, int] = {v: k for k, v in BES_TE_IKI_SOZLUK.items()}


def denetle_beste_iki(sozcuk: str) -> Tuple[bool, str, Optional[int]]:
    """5'te 2 sözcük geçerliliğini denetler.
    Kural: Tam 5 bit olmalı, karakterler '0'/'1' olmalı, tam olarak iki adet '1' bulunmalıdır.
    Dönen: (gecerli_mi, aciklama, rakam)
    """
    if len(sozcuk) != 5:
        raise ValueError(f"Hatalı bit uzunluğu: '{sozcuk}' ({len(sozcuk)} bit). 5 bit olmalıdır.")
    if not all(c in "01" for c in sozcuk):
        raise ValueError(f"Geçersiz karakter: '{sozcuk}'. Yalnızca '0' ve '1' içermelidir.")
    
    bir_sayisi = sozcuk.count("1")
    if bir_sayisi != 2:
        return False, f"Geçersiz: 1 sayısı {bir_sayisi} (tam 2 adet '1' olmalıdır)", None
    
    if sozcuk not in BES_TE_IKI_TERS:
        return False, f"Geçersiz sözcük (sözlükte yok)", None
    
    rakam = BES_TE_IKI_TERS[sozcuk]
    return True, f"Geçerli (Rakam: {rakam})", rakam


def eslik_paketi_olustur(veri_7bit: str, mod: str = "cift") -> str:
    """7 veri bitinin soluna p eşlik bitini ekleyerek 8 bitlik paket üretir.
    mod: 'cift' (even) veya 'tek' (odd).
    """
    if len(veri_7bit) != 7:
        raise ValueError(f"Veri 7 bit olmalıdır: '{veri_7bit}' ({len(veri_7bit)} bit)")
    if not all(c in "01" for c in veri_7bit):
        raise ValueError(f"Geçersiz veri karakteri: '{veri_7bit}'")
    
    veri_bir_sayisi = veri_7bit.count("1")
    m = mod.lower()
    if m in ("cift", "even"):
        # Toplam 1 sayısı çift olmalı
        p = "0" if veri_bir_sayisi % 2 == 0 else "1"
    elif m in ("tek", "odd"):
        # Toplam 1 sayısı tek olmalı
        p = "1" if veri_bir_sayisi % 2 == 0 else "0"
    else:
        raise ValueError(f"Bilinmeyen eşlik modu: '{mod}'. 'cift' veya 'tek' olmalıdır.")
    
    return p + veri_7bit


def denetle_eslik_paketi(paket_8bit: str, mod: str = "cift") -> Tuple[bool, str, int]:
    """8 bitlik pakette (p + 7 veri biti) eşlik kuralını denetler.
    Dönen: (gecerli_mi, aciklama, bir_sayisi)
    """
    if len(paket_8bit) != 8:
        raise ValueError(f"Paket 8 bit olmalıdır: '{paket_8bit}' ({len(paket_8bit)} bit)")
    if not all(c in "01" for c in paket_8bit):
        raise ValueError(f"Geçersiz paket karakteri: '{paket_8bit}'")
    
    bir_sayisi = paket_8bit.count("1")
    m = mod.lower()
    if m in ("cift", "even"):
        gecerli = (bir_sayisi % 2 == 0)
        durum = "Geçerli (1 sayısı çift)" if gecerli else f"HATA: Eşlik bozuldu (1 sayısı {bir_sayisi}, tek)"
    elif m in ("tek", "odd"):
        gecerli = (bir_sayisi % 2 != 0)
        durum = "Geçerli (1 sayısı tek)" if gecerli else f"HATA: Eşlik bozuldu (1 sayısı {bir_sayisi}, çift)"
    else:
        raise ValueError(f"Bilinmeyen eşlik modu: '{mod}'")
    
    return gecerli, durum, bir_sayisi


def beste_iki_tek_bit_taramasi() -> Dict[str, any]:
    """10 geçerli 5'te 2 sözcüğünde tüm tek bit terslemelerini (10 x 5 = 50) sınar."""
    saptanan = 0
    kacan = 0
    kayitlar = []
    
    for rakam, sozcuk in BES_TE_IKI_SOZLUK.items():
        for bit_idx in range(5):
            # bit_idx konumunu tersle
            bit_list = list(sozcuk)
            bit_list[bit_idx] = "0" if bit_list[bit_idx] == "1" else "1"
            hatali = "".join(bit_list)
            
            gecerli, aciklama, yeni_rakam = denetle_beste_iki(hatali)
            if not gecerli:
                saptanan += 1
            else:
                kacan += 1
            kayitlar.append({
                "eski_rakam": rakam,
                "eski_sozcuk": sozcuk,
                "terslenen_bit": bit_idx,
                "hatali_sozcuk": hatali,
                "saptandi_mi": not gecerli,
            })
    return {"toplam": len(kayitlar), "saptanan": saptanan, "kacan": kacan, "kayitlar": kayitlar}


def beste_iki_iki_bit_taramasi() -> Dict[str, any]:
    """10 geçerli 5'te 2 sözcüğünde tüm iki bit terslemelerini (10 x C(5,2) = 100) sınar."""
    saptanan = 0
    kacan = 0
    kacan_ornekler = []
    
    for rakam, sozcuk in BES_TE_IKI_SOZLUK.items():
        for i, j in combinations(range(5), 2):
            bit_list = list(sozcuk)
            bit_list[i] = "0" if bit_list[i] == "1" else "1"
            bit_list[j] = "0" if bit_list[j] == "1" else "1"
            hatali = "".join(bit_list)
            
            gecerli, aciklama, yeni_rakam = denetle_beste_iki(hatali)
            if not gecerli:
                saptanan += 1
            else:
                kacan += 1
                kacan_ornekler.append({
                    "eski_rakam": rakam,
                    "eski_sozcuk": sozcuk,
                    "terslenen_bitler": (i, j),
                    "hatali_sozcuk": hatali,
                    "yeni_rakam": yeni_rakam,
                })
    return {
        "toplam": saptanan + kacan,
        "saptanan": saptanan,
        "kacan": kacan,
        "kacan_ornekler": kacan_ornekler,
    }


def eslik_paketi_hata_taramasi(paket: str = "11000011", mod: str = "cift") -> Dict[str, any]:
    """8 bitlik pakette 8 tek bit ve 28 iki bit terslemelerini sınar."""
    # 8 Tek bit terslemesi
    tek_saptanan = 0
    tek_kacan = 0
    for i in range(8):
        plist = list(paket)
        plist[i] = "0" if plist[i] == "1" else "1"
        h = "".join(plist)
        gecerli, _, _ = denetle_eslik_paketi(h, mod)
        if not gecerli:
            tek_saptanan += 1
        else:
            tek_kacan += 1
            
    # 28 İki bit terslemesi
    cift_saptanan = 0
    cift_kacan = 0
    for i, j in combinations(range(8), 2):
        plist = list(paket)
        plist[i] = "0" if plist[i] == "1" else "1"
        plist[j] = "0" if plist[j] == "1" else "1"
        h = "".join(plist)
        gecerli, _, _ = denetle_eslik_paketi(h, mod)
        if not gecerli:
            cift_saptanan += 1
        else:
            cift_kacan += 1
            
    return {
        "paket": paket,
        "mod": mod,
        "tek_bit_toplam": 8,
        "tek_bit_saptanan": tek_saptanan,
        "tek_bit_kacan": tek_kacan,
        "iki_bit_toplam": 28,
        "iki_bit_saptanan": cift_saptanan,
        "iki_bit_kacan": cift_kacan,
    }


def analiz_gecersiz_01000() -> Dict[str, any]:
    """Geçersiz 01000 desenini inceleyerek olası özgün geçerli 5'te 2 sözcüklerini bulur."""
    desen = "01000"
    olasi_sozcukler = []
    # Eğer tek bir 1 -> 0 hatası olmuşsa, 0 olan 4 bitten biri 1 idi:
    for idx, char in enumerate(desen):
        if char == "0":
            aday = list(desen)
            aday[idx] = "1"
            aday_str = "".join(aday)
            if aday_str in BES_TE_IKI_TERS:
                olasi_sozcukler.append((aday_str, BES_TE_IKI_TERS[aday_str], idx))
    return {
        "desen": desen,
        "bir_sayisi": desen.count("1"),
        "olasi_ozgun_sozcukler": olasi_sozcukler,
    }
