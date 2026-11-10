"""BLM2007 Mantık Devreleri - Deney Yaprağı 3 Doğrulama Betiği
"""

from bes_bit_ve_eslik import (
    denetle_beste_iki,
    eslik_paketi_olustur,
    denetle_eslik_paketi,
    beste_iki_tek_bit_taramasi,
    beste_iki_iki_bit_taramasi,
    eslik_paketi_hata_taramasi,
    analiz_gecersiz_01000,
    BES_TE_IKI_SOZLUK,
)


def main():
    print("=== DENEY YAPRAĞI 3 DOĞRULAMA RAPORU ===\n")
    
    # 1. 11000 Özel Sıfır Ataması Gerekçesi
    print("--- 1. 11000 Özel Sıfır Ataması Gerekçesi ---")
    print(
        "7-4-2-1-0 ağırlıklarıyla 0 değeri normalde 0*7+0*4+0*2+0*1+0*0 = 0 (yani 00000) ile elde edilir.\n"
        "Ancak 5'te 2 kodunun temel güvenlik kuralı her sözcükte TAM İKİ ADET 1 bulunmasıdır.\n"
        "00000 deseninde hiç 1 yoktur. 11000 deseninin ağırlık toplamı 7+4 = 11'dir ve 0-9 aralığında hiçbir\n"
        "tekil onlu rakama denk gelmez. Bu nedenle koddaki 2-bir kuralını korumak için 0 rakamına 11000 atanmıştır."
    )
    
    # Uzunluk ve karakter hataları hem sözcükte hem eşlik paketinde reddedilmeli.
    for denetleyici, girdiler in [
        (denetle_beste_iki, ["0100", "01a00"]),
        (denetle_eslik_paketi, ["0100001", "01a00011"]),
    ]:
        for girdi in girdiler:
            try:
                denetleyici(girdi)
            except ValueError as hata:
                print(f"  [REDDEDİLDİ] {girdi}: {hata}")
            else:
                raise AssertionError(f"Geçersiz girdi kabul edildi: {girdi}")

    # 2. 5'te 2 Hata Taramaları (50 ve 100 Deney)
    print("\n--- 2. 5'te 2 Kodunda Hata Taramaları ---")
    tek_tarama = beste_iki_tek_bit_taramasi()
    print(f"Tek Bit Hata Taraması: Toplam {tek_tarama['toplam']} deney -> Saptanan: {tek_tarama['saptanan']}, Kaçan: {tek_tarama['kacan']}")
    assert tek_tarama["saptanan"] == 50 and tek_tarama["kacan"] == 0
    print("  => Tek bit hatalarının %100'ü (50/50) saptandı (1 sayısı 1 veya 3'e dönüştü).\n")
    
    iki_tarama = beste_iki_iki_bit_taramasi()
    print(f"İki Bit Hata Taraması: Toplam {iki_tarama['toplam']} deney -> Saptanan: {iki_tarama['saptanan']}, Kaçan: {iki_tarama['kacan']}")
    assert iki_tarama["saptanan"] == 40 and iki_tarama["kacan"] == 60
    print("  => İki bit hatalarında 40 hata saptandı (1 sayısı 0 veya 4 oldu), 60 hata ise KAÇTI!")
    print("\nKaçan Hata Örnekleri (1 sayısı 2 kalarak başka bir geçerli rakama dönüşenler):")
    for ornek in iki_tarama["kacan_ornekler"][:5]:
        agirliklar = tuple([7, 4, 2, 1, 0][i] for i in ornek["terslenen_bitler"])
        print(f"  Eski Rakam {ornek['eski_rakam']} ({ornek['eski_sozcuk']}) -> Terslenen bitler {agirliklar} ağırlıkları -> Yeni Sözcük {ornek['hatali_sozcuk']} => YENİ RAKAM: {ornek['yeni_rakam']} [KAÇTI]")
        
    # 3. Eşlik Denetimi: 1000011 ve 1000001
    print("\n--- 3. Eşlik Paketleri ve Hata Taramaları ---")
    v1 = "1000011"  # 3 adet 1
    v2 = "1000001"  # 2 adet 1
    
    p_cift_v1 = eslik_paketi_olustur(v1, "cift")
    p_tek_v1 = eslik_paketi_olustur(v1, "tek")
    p_cift_v2 = eslik_paketi_olustur(v2, "cift")
    p_tek_v2 = eslik_paketi_olustur(v2, "tek")
    
    print(f"Veri '{v1}' (1 sayısı: 3): Çift Eşlik Paketi: '{p_cift_v1}' (p={p_cift_v1[0]}), Tek Eşlik Paketi: '{p_tek_v1}' (p={p_tek_v1[0]})")
    print(f"Veri '{v2}' (1 sayısı: 2): Çift Eşlik Paketi: '{p_cift_v2}' (p={p_cift_v2[0]}), Tek Eşlik Paketi: '{p_tek_v2}' (p={p_tek_v2[0]})")
    assert p_cift_v1 == "11000011"
    assert p_tek_v1 == "01000011"
    assert p_cift_v2 == "01000001"
    assert p_tek_v2 == "11000001"
    
    # Çift eşlikli 11000011 paketinde 8 tek bit ve 28 iki bit terslemesi:
    eslik_sonuc = eslik_paketi_hata_taramasi("11000011", "cift")
    print(f"\nPaket '11000011' (Çift Eşlik) Taraması:")
    print(f"  8 Tek Bit Hatası : Saptanan: {eslik_sonuc['tek_bit_saptanan']}/8, Kaçan: {eslik_sonuc['tek_bit_kacan']}/8")
    print(f"  28 İki Bit Hatası: Saptanan: {eslik_sonuc['iki_bit_saptanan']}/28, Kaçan: {eslik_sonuc['iki_bit_kacan']}/28")
    assert eslik_sonuc["tek_bit_saptanan"] == 8 and eslik_sonuc["tek_bit_kacan"] == 0
    assert eslik_sonuc["iki_bit_saptanan"] == 0 and eslik_sonuc["iki_bit_kacan"] == 28
    print("  => Tek/Çift Tersleme Kuralı: Tek sayıda bit hatası pariteyi değiştirir (daima saptanır); çift sayıda bit hatası pariteyi korur (daima kaçar).")
    
    # 4. Geçersiz 01000 ve Yalnızca p'nin Terslenmesi Analizi
    print("\n--- 4. Düzeltme Sınırı, Hata Konumu ve 01000 Analizi ---")
    analiz_01000 = analiz_gecersiz_01000()
    print(f"Geçersiz Desen: '{analiz_01000['desen']}' (1 sayısı: {analiz_01000['bir_sayisi']})")
    print("Olası özgün geçerli 5'te 2 sözcükleri (tek bit hatası varsayımıyla):")
    for sz, rk, bit_konumu in analiz_01000["olasi_ozgun_sozcukler"]:
        print(f"  Sözcük: '{sz}' -> Rakam: {rk} (Eğer {[7, 4, 2, 1, 0][bit_konumu]} ağırlıklı bit bozulduysa)")
    assert len(analiz_01000["olasi_ozgun_sozcukler"]) >= 2
    
    # Yalnız p'nin terslenmesi:
    paket_p_hatali = "01000011"  # Orijinal '11000011' idi, yalnız p=1 biti 0 yapıldı
    gecerli, durum, _ = denetle_eslik_paketi(paket_p_hatali, "cift")
    print(f"\nYalnızca p Biti Terslendiğinde (11000011 -> {paket_p_hatali}):")
    print(f"  Eşlik Denetimi: {durum}")
    print("  Açıklama: Eşlik denetleyicisi hata uyarısı verir; ancak iletilen veri bitleri ('1000011') tamamen doğrudur!")
    print(
        "  Kavramsal Ayrım:\n"
        "  - Hata Saptama (Detection): Pakette/sözcükte bir kural ihlali olduğunu fark etme (yapılabiliyor).\n"
        "  - Hatanın Yerini Bulma (Localization): Hangi bitin bozulduğunu bilme (tek eşlik veya 5'te 2 bunu yapamaz).\n"
        "  - Veri Bitlerinin Doğruluğu: Parite hatası oluştuğunda bile verinin kendisi doğru kalmış olabilir."
    )
    
    print("\n>>> DENEY 3 TÜM TESTLER BAŞARIYLA TAMAMLANDI! <<<")


if __name__ == "__main__":
    main()
