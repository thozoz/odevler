"""BLM2007 Mantık Devreleri - Deney Yaprağı 4 Doğrulama Betiği
"""

from karakter_ve_barkod import (
    kodla_karakter_dizesi,
    coz_karakter_dizesi,
    agirlik_hesapla_h,
    ust_bit_donusum_sinamasi,
    barkod_metin_karsilastirma_deneyi,
    uc_gorunum_deney_kaydi,
    KARAKTER_TABLOSU,
)


def main():
    print("=== DENEY YAPRAĞI 4 DOĞRULAMA RAPORU ===\n")
    
    # 1. HELP 2031 Kodlama ve Geri Çözme
    print("--- 1. 'HELP 2031' Karakter Kodlamaları ---")
    metin = "HELP 2031"
    ascii_hex = kodla_karakter_dizesi(metin, "ASCII")
    ebcdic_hex = kodla_karakter_dizesi(metin, "EBCDIC")
    
    ascii_cozulen = coz_karakter_dizesi(" ".join(ascii_hex), "ASCII")
    ebcdic_cozulen = coz_karakter_dizesi(" ".join(ebcdic_hex), "EBCDIC")
    
    print(f"Özgün Metin   : '{metin}'")
    print(f"ASCII Hex     : {' '.join(ascii_hex)} -> Çözülen: '{ascii_cozulen}'")
    print(f"EBCDIC Hex    : {' '.join(ebcdic_hex)} -> Çözülen: '{ebcdic_cozulen}'")
    assert ascii_cozulen == metin
    assert ebcdic_cozulen == metin
    print("  => Her iki kodda da kodlama ve geri çözüm kusursuz eşleşti.\n")
    
    # H karakteri bağımsız bit ağırlıkları hesabı:
    print("H Karakterinin İki Kodda Ağırlık Analizi:")
    h_analiz = agirlik_hesapla_h()
    for k, v in h_analiz.items():
        print(f"  [{k}] Hex: {v['hex']} ({v['hex_agirlik_hesabi']}) | Bin: {v['bin']} ({v['bin_agirlik_hesabi']}) -> Eşleşti: {v['eslesiyor_mu']}")
        assert v["eslesiyor_mu"]
        
    # 2. Çapraz Çözüm ve Üst Bit Sınaması
    print("\n--- 2. Çapraz Çözüm ve Üst Bit Yetersizliği ---")
    dize_ascii = "48 45 4C 50"
    dize_ebcdic = "C8 C5 D3 D7"
    
    print(f"ASCII Dizesi ('{dize_ascii}') Çözüm Denemesi:")
    print(f"  ASCII ile : '{coz_karakter_dizesi(dize_ascii, 'ASCII')}' [BAŞARILI]")
    try:
        coz_karakter_dizesi(dize_ascii, "EBCDIC")
        assert False, "EBCDIC ile çözülememeliydi!"
    except ValueError as e:
        print(f"  EBCDIC ile: [REDDEDİLDİ / HATA] {e}")
        
    print(f"\nEBCDIC Dizesi ('{dize_ebcdic}') Çözüm Denemesi:")
    print(f"  EBCDIC ile: '{coz_karakter_dizesi(dize_ebcdic, 'EBCDIC')}' [BAŞARILI]")
    try:
        coz_karakter_dizesi(dize_ebcdic, "ASCII")
        assert False, "ASCII ile çözülememeliydi!"
    except ValueError as e:
        print(f"  ASCII ile : [REDDEDİLDİ / HATA] {e}")
        
    print("\nÜst Bit (MSB) Ekleme/Kesme Yönteminin Neden Yetmediği:")
    msb_test = ust_bit_donusum_sinamasi()
    for o in msb_test["ornekler"]:
        print(f"  Karakter '{o['karakter']}': ASCII {o['ascii_hex']} ({o['ascii_bin']}) -> MSB 1 yapılırsa: {o['msb_eklenmis_hex']} | Gerçek EBCDIC: {o['ebcdic_hex']} ({o['ebcdic_bin']}) => {'UYUŞTU' if o['basarili_mi'] else 'UYUŞMADI / YANLIŞ'}")
    print(f"\nGerekçe: {msb_test['gerekce']}")
    
    # 3. Dört Barkodun Üretimi ve Bağımsız Okuyucu ile Doğrulanması
    print("\n--- 3. Code 128 Barkod Üretim ve Bağımsız Okuma Deneyi ---")
    barkodlar = barkod_metin_karsilastirma_deneyi()
    for b in barkodlar:
        print(f"Girdi: '{b['girdi']}' (Uzunluk: {b['uzunluk']})")
        print(f"  Üretici : {b['uretici']}")
        print(f"  Okuyucu : {b['okuyucu']}")
        print(f"  Okunan  : '{b['okunan']}'")
        print(f"  Durum   : {'Karakter Karakter EŞİT [DOĞRULANDI]' if b['karakter_karakter_esit'] else 'UYUŞMAZLIK'}\n")
        assert b["karakter_karakter_esit"]
        
    print(
        "Boşluk ve Başlangıç Sıfırının Etkisi:\n"
        "- 'HELP 2031' ve 'HELP2031': Boşluk barkodda ayrı bir optik karakter sembolü (Code 128 değeri 0) olarak kodlanır.\n"
        "  Boşluksuz metin 8 sembol, boşluklu metin 9 sembol içerir ve bağımsız okuyucu boşluğu aynen korur.\n"
        "- '000123' ve '123': Barkod sayısal bir değer değil, bir dizge (string) kodlar. '000123' girdisinde baştaki üç adet\n"
        "  sıfır ('000') optik desende ayrı çubuk kombinasyonlarıyla kodlanır ve bağımsız okuyucu tarafından 6 karakter olarak okunur;\n"
        "  '123' ise 3 karakter olarak okunur. Sayısal aritmetikteki önemsiz sıfır kuralı optik barkod kodlamasında geçerli değildir."
    )
    
    # 4. Üç Görünüm Deney Kaydı ve Ekranda Metin Gösterme Kanıtı Analizi
    print("\n--- 4. Üç Görünüm Deney Kaydı ---")
    gorunumler = uc_gorunum_deney_kaydi("HELP 2031")
    for g in gorunumler:
        print(f"{g['gorunum']}:")
        print(f"  Boyut: {g['boyut']} | Deneme: {g['deneme_sayisi']} | Başarı: {g['basari_sayisi']} ({g['basari_orani']}) -> {g['durum']}")
        
    print(
        "\nÜreticinin Metni Ekranda Göstermesinin Neden Bağımsız Okuma Kanıtı Olmadığı:\n"
        "Barkod üreten yazılımlar görselin altına metni (insan tarafından okunabilir metin / human readable text) basarlar.\n"
        "Bu metin doğrudan kullanıcının girdiği dizgenin standart yazı tipiyle (font) ekrana çizilmesidir; optik çubukların\n"
        "taranıp deşifre edilmesiyle üretilmez. Çubuk deseni eksik basılsa, pikseller bulanıklaşsa veya sessiz alanlar bozulsa bile\n"
        "alttaki metin doğru gözükmeye devam eder. Bu nedenle bağımsız bir optik okuyucu (örneğin pyzbar kütüphanesi) piksel desenini\n"
        "tarayıp başarıyla deşifre etmedikçe, optik kodlamanın çalıştığı kanıtlanmış sayılamaz."
    )
    
    print("\n>>> DENEY 4 TÜM TESTLER BAŞARIYLA TAMAMLANDI! <<<")


if __name__ == "__main__":
    main()
