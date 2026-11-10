"""BLM2007 Mantık Devreleri - Deney Yaprağı 2 Doğrulama Betiği
"""

from gray_donusturucu import (
    ikili_to_gray,
    gray_to_ikili,
    hatali_gray_to_ikili,
    bit_farki_sayisi,
    tablo_0_15_uret,
    karsilastir_kapanislar,
    hatali_ve_dogru_karsilastir_4bit,
)


def main():
    print("=== DENEY YAPRAĞI 2 DOĞRULAMA RAPORU ===\n")
    
    # 1. 0-15 Tablosu ve Ardışık Komşuluk
    print("--- 1. 0-15 İkili / Gray / Geri Çözülen Tablosu ---")
    tablo = tablo_0_15_uret()
    print("Onlu | İkili | Gray | Geri Çözülen | Durum")
    print("-" * 45)
    for row in tablo:
        print(f"{row['onlu']:4d} | {row['ikili']}  | {row['gray']} | {row['geri_cozulen']:12s} | {'EŞLEŞTİ' if row['birebir_esit_mi'] else 'HATA'}")
        assert row["birebir_esit_mi"]
        
    print("\nArdışık Geçişlerdeki Bit Farkı (Hamming Mesafesi):")
    for i in range(15):
        g1 = tablo[i]["gray"]
        g2 = tablo[i + 1]["gray"]
        fark = bit_farki_sayisi(g1, g2)
        assert fark == 1, f"Hata: {i} -> {i+1} geçişinde bit farkı {fark} != 1"
    print("  0'dan 15'e kadar tüm 15 ardışık geçişte bit farkı tam olarak 1'dir [DOĞRULANDI].")
    
    # 2. Kapanış Karşılaştırması (15->0 vs 9->0)
    print("\n--- 2. Kapanış Karşılaştırması (15 -> 0 vs 9 -> 0) ---")
    kapanis = karsilastir_kapanislar()
    print(f"15 -> 0 Kapanışı: Gray(15) = {kapanis['gray_15']} -> Gray(0) = {kapanis['gray_0']} => Fark: {kapanis['fark_15_0']} bit.")
    print(f"9  -> 0 Kapanışı: Gray(9)  = {kapanis['gray_9']} -> Gray(0) = {kapanis['gray_0']} => Fark: {kapanis['fark_9_0']} bit.")
    print(f"Yorum: {kapanis['yorum']}")
    assert kapanis["fark_15_0"] == 1
    assert kapanis["fark_9_0"] == 3
    
    # 3. Uzun Örnekler: 101110101 ve 1000101
    print("\n--- 3. Uzun Girdi Testleri (Bit Uzunluğunun Korunması) ---")
    ornekler = ["101110101", "1000101"]
    for ornek in ornekler:
        gray = ikili_to_gray(ornek)
        geri = gray_to_ikili(gray)
        assert len(gray) == len(ornek), "Bit uzunluğu korunmalı!"
        assert geri == ornek, f"Geri dönüşüm hatası: {ornek} != {geri}"
        print(f"Girdi İkili : {ornek} ({len(ornek)} bit)")
        print(f"Gray Çıktı  : {gray} ({len(gray)} bit)")
        print(f"Geri Çözülen: {geri} ({len(geri)} bit) [KORUNDU VE DOĞRULANDI]\n")
        
    # 4. Hatalı Yöntem İncelemesi
    print("--- 4. Hatalı Ters Yöntem (Komşu Gray Bitlerini XOR'lama) ---")
    ayrisanlar = hatali_ve_dogru_karsilastir_4bit()
    print(f"16 adet 4-bit Gray sözcüğünden {len(ayrisanlar)} tanesinde hatalı yöntem yanlış sonuç verdi.")
    print("\nÖrnek ayrışan sözcükler:")
    for a in ayrisanlar[:5]:
        print(f"  Gray: {a['gray']} -> Doğru İkili: {a['dogru_ikili']} | Hatalı: {a['hatali_ikili']} (İlk ayrışan adım: indeks {a['ilk_ayrisan_indeks']}, ağırlık 2^{3-a['ilk_ayrisan_indeks']})")
    
    # Özellikle 1100 örneğini adım adım gösterelim:
    ornek_gray = "1100"
    dogru_ik = gray_to_ikili(ornek_gray)
    hatali_ik, adimlar = hatali_gray_to_ikili(ornek_gray)
    print(f"\nAyrıntılı İnceleme Girişi: Gray '{ornek_gray}'")
    print(f"  Doğru Çözüm: '{dogru_ik}' (Onlu {int(dogru_ik, 2)})")
    print(f"  Hatalı Çözüm: '{hatali_ik}' (Onlu {int(hatali_ik, 2)})")
    for adim in adimlar:
        print(f"    Adım {adim['adim']}: Konum {adim['konum']} -> {adim['islem']}")
    print("  Açıklama: Doğru yöntemde b_1 = b_2 ^ g_1 = 0 ^ 0 = 0 olurken, hatalı yöntem g_2 ^ g_1 = 1 ^ 0 = 1 hesaplar!")
    
    # Rastgele iki Gray sözcüğü arasındaki mesafe:
    print("\nRastgele İki Gray Sözcüğü Analizi:")
    g_a = ikili_to_gray("0000")  # 0 -> 0000
    g_b = ikili_to_gray("0010")  # 2 -> 0011
    fark_ab = bit_farki_sayisi(g_a, g_b)
    g_c = ikili_to_gray("1010")  # 10 -> 1111
    fark_ac = bit_farki_sayisi(g_a, g_c)
    print(f"  Gray('0000') = {g_a}, Gray('0010') = {g_b} -> Fark: {fark_ab} bit.")
    print(f"  Gray('0000') = {g_a}, Gray('1010') = {g_c} -> Fark: {fark_ac} bit.")
    print("  Gerekçe: Gray kodu yalnız ARDIŞIK onlu değerler (k ve k+1) arasında tek bit farkı garanti eder. Rastgele seçilen sözcükler arasında 2, 3 veya 4 bit fark bulunabilir.")
    
    print("\n>>> DENEY 2 TÜM TESTLER BAŞARIYLA TAMAMLANDI! <<<")


if __name__ == "__main__":
    main()
