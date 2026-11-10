"""BLM2007 Mantık Devreleri - Deney Yaprağı 2: Gray Dönüştürücüsü ve Komşuluk Denetimi

İkili <-> Yansıtılmış Gray dönüşümleri (bit düzeyinde XOR ile).
Ardışık komşuluk, dairesel kapanış (15 -> 0 vs 9 -> 0) ve hatalı geri dönüştürücü analizi.
"""

from typing import Dict, List, Tuple


def ikili_to_gray(ikili_str: str) -> str:
    """İkili dizgiyi (en anlamlıdan en aza) yansıtılmış Gray koduna dönüştürür.
    g_{n-1} = b_{n-1}
    g_i = b_{i+1} XOR b_i (i = n-2 ... 0)
    Girdi uzunluğunu korur.
    """
    if not ikili_str:
        raise ValueError("Girdi ikili dizesi boş olamaz.")
    if not all(c in "01" for c in ikili_str):
        raise ValueError(f"Geçersiz ikili dizge: '{ikili_str}'. Yalnızca '0' ve '1' içermelidir.")
    
    n = len(ikili_str)
    gray = [ikili_str[0]]  # En anlamlı bit aynı kalır: g_{n-1} = b_{n-1}
    for i in range(1, n):
        # i. konum için bir önceki bit (i-1) ile şimdiki bit (i) XOR'lanır
        bit = str(int(ikili_str[i - 1]) ^ int(ikili_str[i]))
        gray.append(bit)
    return "".join(gray)


def gray_to_ikili(gray_str: str) -> str:
    """Gray kodunu ikili sayıya çözer.
    Önceki hesaplanan ikili biti kullanarak ilerler:
    b_{n-1} = g_{n-1}
    b_i = b_{i+1} XOR g_i (i = n-2 ... 0)
    Hazır Gray dönüştürücü kullanmaz.
    """
    if not gray_str:
        raise ValueError("Girdi Gray dizesi boş olamaz.")
    if not all(c in "01" for c in gray_str):
        raise ValueError(f"Geçersiz Gray dizesi: '{gray_str}'. Yalnızca '0' ve '1' içermelidir.")
    
    n = len(gray_str)
    ikili = [gray_str[0]]  # b_{n-1} = g_{n-1}
    for i in range(1, n):
        # Bir önceki HESAPLANAN İKİLİ BİT (ikili[i-1]) ile gelen Gray biti (gray_str[i]) XOR'lanır:
        onceki_ikili = int(ikili[i - 1])
        gelen_gray = int(gray_str[i])
        yeni_ikili = str(onceki_ikili ^ gelen_gray)
        ikili.append(yeni_ikili)
    return "".join(ikili)


def hatali_gray_to_ikili(gray_str: str) -> Tuple[str, List[Dict[str, any]]]:
    """Ters yönde de komşu Gray bitlerini XOR'layan HATALI algoritma.
    b_{n-1} = g_{n-1}
    b_i = g_{i+1} XOR g_i (önceki ikili bit yerine komşu Gray bitini kullanır!)
    """
    if not gray_str:
        raise ValueError("Girdi Gray dizesi boş olamaz.")
    if not all(c in "01" for c in gray_str):
        raise ValueError(f"Geçersiz Gray dizesi: '{gray_str}'")
    
    n = len(gray_str)
    hatali_ikili = [gray_str[0]]
    adimlar = [{"adim": 0, "konum": n - 1, "bit": gray_str[0], "islem": "MSB doğrudan aktarılır"}]
    for i in range(1, n):
        komsu_gray_onceki = int(gray_str[i - 1])
        komsu_gray_simdiki = int(gray_str[i])
        b = str(komsu_gray_onceki ^ komsu_gray_simdiki)
        hatali_ikili.append(b)
        adimlar.append({
            "adim": i,
            "konum": n - 1 - i,
            "bit": b,
            "islem": f"g_{{{n-i}}} XOR g_{{{n-1-i}}} = {komsu_gray_onceki} ^ {komsu_gray_simdiki} = {b}",
        })
    return "".join(hatali_ikili), adimlar


def bit_farki_sayisi(s1: str, s2: str) -> int:
    """Karşılık gelen konumlardaki farklı bit sayısını (Hamming mesafesi) bulur."""
    if len(s1) != len(s2):
        raise ValueError(f"Uzunluklar eşit olmalıdır: {len(s1)} != {len(s2)}")
    return sum(1 for c1, c2 in zip(s1, s2) if c1 != c2)


def tablo_0_15_uret() -> List[Dict[str, any]]:
    """0-15 arası sayılar için ikili, Gray ve geri çözülen ikili tablosu üretir."""
    satirlar = []
    for d in range(16):
        ikili = f"{d:04b}"
        gray = ikili_to_gray(ikili)
        geri_ikili = gray_to_ikili(gray)
        satirlar.append({
            "onlu": d,
            "ikili": ikili,
            "gray": gray,
            "geri_cozulen": geri_ikili,
            "birebir_esit_mi": (ikili == geri_ikili),
        })
    return satirlar


def karsilastir_kapanislar() -> Dict[str, any]:
    """15 -> 0 kapanışı ile 0-9'a kesilmiş dizinin 9 -> 0 kapanışını karşılaştırır."""
    g_15 = ikili_to_gray(f"{15:04b}")  # '1000'
    g_0 = ikili_to_gray(f"{0:04b}")    # '0000'
    fark_15_0 = bit_farki_sayisi(g_15, g_0)
    
    g_9 = ikili_to_gray(f"{9:04b}")    # '1101'
    fark_9_0 = bit_farki_sayisi(g_9, g_0)
    
    farkli_bitler_9_0 = [i for i, (c1, c2) in enumerate(zip(g_9, g_0)) if c1 != c2]
    
    return {
        "gray_0": g_0,
        "gray_15": g_15,
        "fark_15_0": fark_15_0,
        "gray_9": g_9,
        "fark_9_0": fark_9_0,
        "farkli_bitler_9_0": farkli_bitler_9_0,
        "yorum": (
            f"15'in Gray kodu {g_15}, 0'ın Gray kodu ise {g_0}'dır. Aralarındaki farklı bit sayısı {fark_15_0}'dir "
            "(yalnız en anlamlı bit farklıdır). Dolayısıyla 4 bitlik Gray kodu tam dairesel (cyclic) bir koddur. "
            f"Buna karşın dizi 0-9'da kesilirse: 9'un Gray kodu {g_9}, 0'ınki {g_0}'dır. Aralarında tam {fark_9_0} "
            f"bit (konum indeksleri: {farkli_bitler_9_0}) farklıdır. Dizi kesildiğinde dairesel tek bit komşuluk "
            "özelliği kaybolur."
        ),
    }


def hatali_ve_dogru_karsilastir_4bit() -> List[Dict[str, any]]:
    """Tüm 16 adet 4-bit Gray sözcüğünde doğru ve hatalı geri dönüştürücüyü kıyaslar.
    Ayrışan sözcükleri ve ilk ayrışan adımları belirler.
    """
    ayrisanlar = []
    for g_val in range(16):
        gray = f"{g_val:04b}"
        dogru_ikili = gray_to_ikili(gray)
        hatali_ikili, adimlar = hatali_gray_to_ikili(gray)
        if dogru_ikili != hatali_ikili:
            # İlk ayrışan adımı bulalım
            ilk_adim = next(idx for idx in range(4) if dogru_ikili[idx] != hatali_ikili[idx])
            ayrisanlar.append({
                "gray": gray,
                "dogru_ikili": dogru_ikili,
                "hatali_ikili": hatali_ikili,
                "ilk_ayrisan_indeks": ilk_adim,
                "ilk_ayrisan_konum_agirligi": 2 ** (3 - ilk_adim),
            })
    return ayrisanlar
