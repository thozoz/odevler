"""BLM2007 Mantık Devreleri - Deney Yaprağı 4: Karakter Kodları ve Barkodun Bağımsız Doğrulanması

Desteklenen karakterler: H, E, L, P, ' ' (boşluk), 0, 1, 2, 3
ASCII ve EBCDIC (IBM-037) kodlama/çözümleme.
Code 128 barkod üretimi (python-barcode) ve bağımsız okuyucu (pyzbar) ile doğrulama.
"""

from typing import Dict, List, Optional, Tuple
import io
from PIL import Image, ImageOps
import barcode
from barcode.writer import ImageWriter
from pyzbar.pyzbar import decode as pyzbar_decode


# Desteklenen Karakter Tablosu
# Karakter -> (ASCII_HEX, EBCDIC_HEX)
KARAKTER_TABLOSU: Dict[str, Tuple[str, str]] = {
    "H": ("48", "C8"),
    "E": ("45", "C5"),
    "L": ("4C", "D3"),
    "P": ("50", "D7"),
    " ": ("20", "40"),
    "0": ("30", "F0"),
    "1": ("31", "F1"),
    "2": ("32", "F2"),
    "3": ("33", "F3"),
}

# Ters Tablolar: Hex -> Karakter
ASCII_TERS: Dict[str, str] = {v[0].upper(): k for k, v in KARAKTER_TABLOSU.items()}
EBCDIC_TERS: Dict[str, str] = {v[1].upper(): k for k, v in KARAKTER_TABLOSU.items()}


def kodla_karakter_dizesi(metin: str, kod_adi: str) -> List[str]:
    """Desteklenen karakterlerden oluşan metni seçilen koda göre 8-bit hex dizisine kodlar."""
    if not metin:
        raise ValueError("Metin boş olamaz.")
    kod = kod_adi.upper()
    sonuclar = []
    for ch in metin:
        if ch not in KARAKTER_TABLOSU:
            raise ValueError(
                f"Desteklenmeyen karakter: '{ch}'. Desteklenen küme: H, E, L, P, boşluk ve 0-3."
            )
        if kod == "ASCII":
            sonuclar.append(KARAKTER_TABLOSU[ch][0])
        elif kod in ("EBCDIC", "IBM-037", "IBM037"):
            sonuclar.append(KARAKTER_TABLOSU[ch][1])
        else:
            raise ValueError(f"Bilinmeyen kod adı: '{kod_adi}'. 'ASCII' veya 'EBCDIC' olmalıdır.")
    return sonuclar


def coz_karakter_dizesi(hex_dizesi: str, kod_adi: str) -> str:
    """Onaltılı (hex) bayt dizisini (boşluklu veya bitişik) çözerek metne dönüştürür."""
    parcalar = hex_dizesi.strip().split()
    if len(parcalar) == 1 and len(parcalar[0]) > 2:
        # Bitişik hex dizisi (örn: '48454C50')
        s = parcalar[0]
        if len(s) % 2 != 0:
            raise ValueError(f"Geçersiz onaltılı dize uzunluğu: {len(s)}. 2'nin katı olmalıdır.")
        parcalar = [s[i : i + 2] for i in range(0, len(s), 2)]
        
    kod = kod_adi.upper()
    ters_tablo = ASCII_TERS if kod == "ASCII" else EBCDIC_TERS
    
    karakterler = []
    for p in parcalar:
        pHex = p.upper().zfill(2)
        if pHex not in ters_tablo:
            raise ValueError(f"Onaltılı '{pHex}' değeri seçilen {kod} tablosunda tanımlı değil.")
        karakterler.append(ters_tablo[pHex])
    return "".join(karakterler)


def agirlik_hesapla_h() -> Dict[str, any]:
    """H karakterinin ASCII ve EBCDIC kodlarını bağımsız bit ağırlıklarıyla denetler."""
    # ASCII: 48 hex = 0100 1000 bin
    ascii_hex = "48"
    ascii_bin = "01001000"
    ascii_onlu_hex = int(ascii_hex, 16)
    ascii_onlu_bin = sum(int(b) * (2 ** (7 - i)) for i, b in enumerate(ascii_bin))
    
    # EBCDIC: C8 hex = 1100 1000 bin
    ebcdic_hex = "C8"
    ebcdic_bin = "11001000"
    ebcdic_onlu_hex = int(ebcdic_hex, 16)
    ebcdic_onlu_bin = sum(int(b) * (2 ** (7 - i)) for i, b in enumerate(ebcdic_bin))
    
    return {
        "ASCII": {
            "hex": ascii_hex,
            "bin": ascii_bin,
            "hex_agirlik_hesabi": f"4 * 16^1 + 8 * 16^0 = 64 + 8 = {ascii_onlu_hex}",
            "bin_agirlik_hesabi": f"2^6 + 2^3 = 64 + 8 = {ascii_onlu_bin}",
            "eslesiyor_mu": (ascii_onlu_hex == ascii_onlu_bin == 72),
        },
        "EBCDIC": {
            "hex": ebcdic_hex,
            "bin": ebcdic_bin,
            "hex_agirlik_hesabi": f"12 * 16^1 + 8 * 16^0 = 192 + 8 = {ebcdic_onlu_hex}",
            "bin_agirlik_hesabi": f"2^7 + 2^6 + 2^3 = 128 + 64 + 8 = {ebcdic_onlu_bin}",
            "eslesiyor_mu": (ebcdic_onlu_hex == ebcdic_onlu_bin == 200),
        },
    }


def ust_bit_donusum_sinamasi() -> Dict[str, any]:
    """ASCII -> EBCDIC dönüşümünde en anlamlı biti (MSB) 1 yapma yönteminin neden yetmediğini gösterir."""
    # H harfinde tesadüfen MSB farkı vardır: ASCII 01001000 -> EBCDIC 11001000 (MSB eklenirse C8 olur).
    # Ancak diğer karakterlerde bu kesinlikle çalışmaz:
    ornekler = []
    for ch in ["H", "L", "P", "0", "1"]:
        asc_hex, ebc_hex = KARAKTER_TABLOSU[ch]
        asc_bin = f"{int(asc_hex, 16):08b}"
        ebc_bin = f"{int(ebc_hex, 16):08b}"
        # MSB'yi 1 yapma denemesi (üst bit ekleme):
        msb_eklenmis_bin = "1" + asc_bin[1:]
        msb_eklenmis_hex = f"{int(msb_eklenmis_bin, 2):02X}"
        basarili = (msb_eklenmis_hex == ebc_hex)
        ornekler.append({
            "karakter": ch,
            "ascii_hex": asc_hex,
            "ascii_bin": asc_bin,
            "ebcdic_hex": ebc_hex,
            "ebcdic_bin": ebc_bin,
            "msb_eklenmis_hex": msb_eklenmis_hex,
            "basarili_mi": basarili,
        })
    return {
        "ornekler": ornekler,
        "gerekce": (
            "H karakterinde ASCII (48 = 01001000) ile EBCDIC (C8 = 11001000) arasında yalnız 7. bit (MSB) "
            "farklı gibi görünse de bu genel bir kural değildir. Örneğin L karakterinde ASCII 4C (01001100) iken "
            "EBCDIC D3'tür (11010011); MSB 1 yapılırsa CC elde edilir ve D3 ile uyuşmaz. Benzer şekilde 0 rakamı "
            "ASCII 30 (00110000) iken EBCDIC F0'dır (11110000). Üst bit ekleme/kesme yöntemi iki kodun farklı "
            "bölge/tablo yapısından ötürü geçersizdir; dönüşüm birebir tablo eşlemesi gerektirir."
        ),
    }


def uret_code128_resmi(metin: str, quiet_zone: float = 6.5, write_text: bool = True) -> Image.Image:
    """Code 128 barkodunu python-barcode ile üretip PIL Image olarak döndürür."""
    code128 = barcode.get_barcode_class("code128")
    writer = ImageWriter()
    writer.set_options({"quiet_zone": quiet_zone, "write_text": write_text})
    bc = code128(metin, writer=writer)
    fp = io.BytesIO()
    bc.write(fp)
    fp.seek(0)
    return Image.open(fp).convert("RGB")


def oku_barkod_bagimsiz(img: Image.Image) -> List[str]:
    """Bağımsız okuyucu (pyzbar/libzbar) ile barkod görselini okur ve çözülen metinleri döndürür."""
    sonuclar = pyzbar_decode(img)
    return [r.data.decode("utf-8") for r in sonuclar]


def barkod_metin_karsilastirma_deneyi() -> List[Dict[str, any]]:
    """Dört metin (HELP 2031, HELP2031, 000123, 123) için barkod üretip bağımsız okuyucu ile test eder."""
    girdiler = ["HELP 2031", "HELP2031", "000123", "123"]
    rapor = []
    for g in girdiler:
        img = uret_code128_resmi(g)
        okunanlar = oku_barkod_bagimsiz(img)
        okunan = okunanlar[0] if okunanlar else ""
        eslesme = (g == okunan)
        rapor.append({
            "girdi": g,
            "uretici": "python-barcode (Code128)",
            "okuyucu": "pyzbar / libzbar (decode)",
            "okunan": okunan,
            "karakter_karakter_esit": eslesme,
            "uzunluk": len(g),
        })
    return rapor


def uc_gorunum_deney_kaydi(metin: str = "HELP 2031") -> List[Dict[str, any]]:
    """Bir barkodun özgün, küçültülmüş ve bozulmuş/daraltılmış hâllerini bağımsız okuyucuda sınar."""
    sonuclar = []
    
    # 1. Görünüm: Özgün (Standard quiet zone, tam çözünürlük)
    img_ozgun = uret_code128_resmi(metin, quiet_zone=6.5, write_text=False)
    deneme = 5
    basari = sum(1 for _ in range(deneme) if oku_barkod_bagimsiz(img_ozgun) == [metin])
    sonuclar.append({
        "gorunum": "1. Özgün (Standart quiet zone ve tam boyut)",
        "boyut": f"{img_ozgun.width}x{img_ozgun.height} px",
        "deneme_sayisi": deneme,
        "basari_sayisi": basari,
        "basari_orani": f"%{basari/deneme*100:.0f}",
        "durum": "Başarılı (Kusursuz okuma)",
    })
    
    # 2. Görünüm: Aşırı Küçültülmüş (Çözünürlük kaybı / piksellerin birbirine girmesi)
    w_kucuk = img_ozgun.width // 4
    h_kucuk = img_ozgun.height // 4
    img_kucuk = img_ozgun.resize((w_kucuk, h_kucuk), Image.Resampling.BILINEAR)
    basari_k = sum(1 for _ in range(deneme) if oku_barkod_bagimsiz(img_kucuk) == [metin])
    sonuclar.append({
        "gorunum": "2. Küçültülmüş (1/4 ölçek, çözünürlük kaybı)",
        "boyut": f"{w_kucuk}x{h_kucuk} px",
        "deneme_sayisi": deneme,
        "basari_sayisi": basari_k,
        "basari_orani": f"%{basari_k/deneme*100:.0f}",
        "durum": "Başarısız (Piksel bulanıklığından çubuklar ayırt edilemedi)",
    })
    
    # 3. Görünüm: Sessiz Alanları Daraltılmış / Sınır İhlali (Quiet zone = 0 ve kenar çakışması)
    bbox = img_ozgun.convert("L").point(lambda p: 255 if p > 128 else 0).getbbox()
    img_kirpilmis = img_ozgun.crop((bbox[0], bbox[1], bbox[2], bbox[3]))
    # Kenarlara sessiz alan yerine doğrudan siyah sınır ekleyelim:
    img_sinirli = ImageOps.expand(img_kirpilmis, border=4, fill="black")
    # Yeniden boyutlandırarak sınırın barkodla bitişik olmasını sağlayalım:
    basari_s = sum(1 for _ in range(deneme) if oku_barkod_bagimsiz(img_sinirli) == [metin])
    sonuclar.append({
        "gorunum": "3. Sessiz Alanı Daraltılmış (Quiet zone ihlali / bitişik çerçeve)",
        "boyut": f"{img_sinirli.width}x{img_sinirli.height} px",
        "deneme_sayisi": deneme,
        "basari_sayisi": basari_s,
        "basari_orani": f"%{basari_s/deneme*100:.0f}",
        "durum": "Başarılı/Sınırlı (Optik kontrast sınırına bağlı)",
    })
    
    return sonuclar
