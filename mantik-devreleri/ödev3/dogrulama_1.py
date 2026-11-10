"""BLM2007 Mantık Devreleri - Deney Yaprağı 1 Doğrulama Betiği
"""

import sys
from rakam_donusturucu import (
    kodla_dize,
    coz_dize,
    desen_kumesi_analizi,
    dokuz_tumleyen_analizi,
    aiken_0101_ve_1011_karsilastir,
    sayi_263_karsilastir,
    BCD_SOZLUK,
    ARTI3_SOZLUK,
    AIKEN_SOZLUK,
)


def main():
    print("=== DENEY YAPRAĞI 1 DOĞRULAMA RAPORU ===\n")
    
    # 1. 48 ve 003 testleri
    print("--- 1. 48 ve 003 Dönüşümleri ---")
    for test_girdi in ["48", "003"]:
        print(f"\nGirdi: '{test_girdi}'")
        for kod in ["BCD", "Arti3", "Aiken"]:
            kodlu = kodla_dize(test_girdi, kod, bosluklu=True)
            cozulen = coz_dize(kodlu, kod)
            assert cozulen == test_girdi, f"Hata: {test_girdi} != {cozulen}"
            print(f"  {kod:6s}: {kodlu} -> Çözülen: '{cozulen}' [BAŞARILI]")
            
    # 2. 263 Karşılaştırması
    print("\n--- 2. 263 Sayısı Analizi (Saf İkili vs BCD) ---")
    analiz_263 = sayi_263_karsilastir()
    print(f"Saf İkili: {analiz_263['saf_ikili']} ({analiz_263['saf_ikili_bit_sayisi']} bit)")
    print(f"BCD      : {analiz_263['bcd']} ({analiz_263['bcd_bit_sayisi']} bit)")
    print(f"BCD biti ikili olarak okunursa onlu değeri: {analiz_263['bcd_ikili_olarak_okunursa']}")
    print(f"Açıklama: {analiz_263['aciklama']}")
    
    # 3. 16 Desen Geçerlilik Kümeleri ve Aiken 0101 vs 1011
    print("\n--- 3. 16 Desen Taraması (Geçerli / Geçersiz Kümeler) ---")
    kume = desen_kumesi_analizi()
    for kod, veriler in kume.items():
        print(f"{kod:6s}: {len(veriler['gecerli'])} geçerli ({', '.join(veriler['gecerli'])})")
        print(f"        {len(veriler['gecersiz'])} geçersiz ({', '.join(veriler['gecersiz'])})")
        assert len(veriler["gecerli"]) == 10
        assert len(veriler["gecersiz"]) == 6
        
    print("\nAiken 0101 ve 1011 Ağırlıklı Toplam Kıyaslaması:")
    aiken_ozel = aiken_0101_ve_1011_karsilastir()
    print(f"  0101 ağırlıklı toplam: {aiken_ozel['0101']['agirlik_toplami']}, sözlükte var mı: {aiken_ozel['0101']['sozlukte_var_mi']}")
    print(f"  1011 ağırlıklı toplam: {aiken_ozel['1011']['agirlik_toplami']}, sözlükte var mı: {aiken_ozel['1011']['sozlukte_var_mi']} (rakam: {aiken_ozel['1011']['temsil_edilen']})")
    print(f"  Gerekçe: {aiken_ozel['gerekce']}")
    
    # 4. 9 Tümleyeni ve BCD Karşı Örneği
    print("\n--- 4. 9 Tümleyeni Analizi (0-9 Bitlerini Tersleme) ---")
    for kod in ["Arti3", "Aiken", "BCD"]:
        print(f"\n[{kod} 9 Tümleyeni]")
        sonuclar = dokuz_tumleyen_analizi(kod)
        dogru_sayisi = 0
        for d, k, tk, coz, beklenen, basari in sonuclar:
            durum = "DOĞRULANDI" if basari else "BAŞARISIZ / GEÇERSİZ"
            print(f"  d={d} ({k}) -> Ters: {tk} -> Çözülen: {coz} (Beklenen: {beklenen}) -> {durum}")
            if basari:
                dogru_sayisi += 1
        if kod in ("Arti3", "Aiken"):
            assert dogru_sayisi == 10, f"{kod} kendinden tümleyen olmalıdır, 10/10 sağlanamadı!"
            print(f"  => {kod} kendinden tümleyendir (10/10 doğrulandı).")
        else:
            print(f"  => BCD kendinden tümleyen DEĞİLDİR ({dogru_sayisi}/10).")
            print(f"     Örn: d=2 (0010) tersi 1101 olup BCD'de geçersizdir; 9-2=7'nin BCD'si ise 0111'dir.")
            
    # 5. Hata Fırlatma Doğrulaması
    print("\n--- 5. Hata Yönetimi Doğrulaması ---")
    hatalar = []
    try:
        kodla_dize("", "bcd")
    except ValueError as e:
        hatalar.append(("Boş girdi", str(e)))
    try:
        kodla_dize("12a", "bcd")
    except ValueError as e:
        hatalar.append(("Geçersiz karakter", str(e)))
    try:
        coz_dize("000100", "bcd")
    except ValueError as e:
        hatalar.append(("Yanlış bit uzunluğu (6 bit)", str(e)))
    try:
        coz_dize("1111", "bcd")
    except ValueError as e:
        hatalar.append(("Geçersiz BCD sözcüğü (1111)", str(e)))
    try:
        coz_dize("0101", "aiken")
    except ValueError as e:
        hatalar.append(("Geçersiz Aiken sözcüğü (0101)", str(e)))
        
    for baslik, msg in hatalar:
        print(f"  [YAKALANDI] {baslik}: {msg}")
    assert len(hatalar) == 5, "Bütün sınır hata durumları fırlatılmalı!"
    
    print("\n>>> DENEY 1 TÜM TESTLER BAŞARIYLA TAMAMLANDI! <<<")


if __name__ == "__main__":
    main()
