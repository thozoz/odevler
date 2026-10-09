"""
BLM2007 Mantık Devreleri - Deney Yaprağı 1
Hatalı Girdileri Tanıyan Sayı Sistemi Dönüştürücüsü

Öğrenci: Efe Özan (thozoz)
Ders: BLM2007 Mantık Devreleri (Prof. Dr. Ali Buldu)

Açıklama:
Bu modül; 2, 8, 10 ve 16 tabanları arasında negatif olmayan tam ve kesirli sayıların
dönüşümünü hiçbir hazır taban dönüştürme fonksiyonu (int(s, base), bin, oct, hex vb.)
kullanmadan, basamak ağırlıkları prensibine dayalı olarak sıfırdan gerçekleştirir.
Girdi doğrulama, kesirli basamak kesinliği (8 basamak sınırı) ve hata yakalama mekanizmalarını içerir.
"""

import sys
import io

# Windows konsolunda Türkçe ve Unicode (≈ vb.) karakterlerin düzgün görüntülenmesi için UTF-8 ayarı
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass
from typing import Tuple, Optional, List, Dict


# İzin verilen geçerli tabanlar
GECERLI_TABANLAR = {2, 8, 10, 16}

# Karakter - Sayısal Değer dönüşüm tabloları (Hazır fonksiyon kullanılmaz)
CHAR_TO_VAL = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
    '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
    'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15
}

VAL_TO_CHAR = {
    0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
    5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
    10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'
}


class GirdiHatasi(Exception):
    """Kullanıcı girdisi doğrulama hataları için özel istisna sınıfı."""
    pass


def girdi_dogrula(sayi_metni: str, kaynak_taban: int, hedef_taban: int) -> Tuple[str, str]:
    """
    Kullanıcı girdisini katı kurallarla denetler.
    
    Kontroller:
    1. Tabanların geçerliliği (2, 8, 10, 16).
    2. Boş girdi ve yalnızca boşluk içeren girdi kontrolü.
    3. Negatif sayı engeli ('-' karakteri).
    4. Kesir ayracı kontrolü (sadece '.' ve en fazla 1 adet).
    5. Sayı gövdesinde hiç rakam olmaması durumu (yalnızca '.' girilmesi vb.).
    6. Kaynak tabana göre geçersiz karakter kontrolü (örn. Taban 2'de '2', Taban 8'de '8').
    
    Dönüş:
        (tam_kisim_str, kesir_kisim_str) ikilisi.
    """
    if kaynak_taban not in GECERLI_TABANLAR:
        raise GirdiHatasi(f"Geçersiz kaynak taban ({kaynak_taban}). İzin verilenler: {sorted(list(GECERLI_TABANLAR))}")
    if hedef_taban not in GECERLI_TABANLAR:
        raise GirdiHatasi(f"Geçersiz hedef taban ({hedef_taban}). İzin verilenler: {sorted(list(GECERLI_TABANLAR))}")

    if not isinstance(sayi_metni, str):
        raise GirdiHatasi("Girdi metin (string) tipinde olmalıdır.")

    metin = sayi_metni.strip()
    if len(metin) == 0:
        raise GirdiHatasi("Girdi boş olamaz.")

    if metin.startswith('-'):
        raise GirdiHatasi("Negatif sayılar kabul edilmez. Sayı negatif olmayan bir değer olmalıdır.")

    nokta_sayisi = metin.count('.')
    if nokta_sayisi > 1:
        raise GirdiHatasi(f"Birden fazla kesir ayracı ('.') bulundu ({nokta_sayisi} adet).")

    if nokta_sayisi == 1:
        parcalar = metin.split('.')
        tam_str, kesir_str = parcalar[0], parcalar[1]
    else:
        tam_str, kesir_str = metin, ""

    # Eğer '.5' girildiyse tam_str="", '5.' girildiyse kesir_str="" olur.
    # Ancak her ikisi birden boşsa (yalnızca '.') geçersizdir.
    if len(tam_str) == 0 and len(kesir_str) == 0:
        raise GirdiHatasi("Kesir ayracı haricinde hiçbir rakam girilmedi.")

    # Boş kalan kısımları '0' olarak varsayabiliriz (.5 -> 0.5, 5. -> 5.0)
    if len(tam_str) == 0:
        tam_str = "0"
    if len(kesir_str) == 0:
        kesir_str = ""

    # Rakam geçerliliği denetimi
    for ch in tam_str:
        if ch not in CHAR_TO_VAL:
            raise GirdiHatasi(f"Tanımsız karakter: '{ch}'.")
        val = CHAR_TO_VAL[ch]
        if val >= kaynak_taban:
            raise GirdiHatasi(
                f"Karakter '{ch}' (değer={val}) taban {kaynak_taban} için geçersizdir! "
                f"Taban {kaynak_taban} rakamları 0 ile {kaynak_taban - 1} arasında olmalıdır."
            )

    for ch in kesir_str:
        if ch not in CHAR_TO_VAL:
            raise GirdiHatasi(f"Tanımsız karakter: '{ch}'.")
        val = CHAR_TO_VAL[ch]
        if val >= kaynak_taban:
            raise GirdiHatasi(
                f"Karakter '{ch}' (değer={val}) taban {kaynak_taban} için geçersizdir! "
                f"Taban {kaynak_taban} rakamları 0 ile {kaynak_taban - 1} arasında olmalıdır."
            )

    return tam_str, kesir_str


def tam_kisim_onluya_cevir(tam_str: str, kaynak_taban: int) -> int:
    """
    Kaynak tabandaki tam sayıyı basamak ağırlıkları formülüyle (Horner yöntemi)
    onluk tabana çevirir.
    I_10 = sum_{i=0}^{n-1} d_i * r^i
    """
    toplam = 0
    for ch in tam_str:
        val = CHAR_TO_VAL[ch]
        toplam = toplam * kaynak_taban + val
    return toplam


def tam_kisim_hedefe_cevir(onlu_deger: int, hedef_taban: int) -> str:
    """
    Onluk tabandaki tam sayıyı ardışık bölme (repeated division) yöntemiyle
    hedef tabana çevirir.
    
    Kalanlar en küçük ağırlıklı basamaktan (LSB) başlanarak elde edilir.
    Bu nedenle sonuç listesi ters çevrilerek (MSB'den LSB'ye) birleştirilir.
    """
    if onlu_deger == 0:
        return "0"

    kalanlar = []
    sayi = onlu_deger
    while sayi > 0:
        kalan = sayi % hedef_taban
        kalanlar.append(VAL_TO_CHAR[kalan])
        sayi = sayi // hedef_taban

    # Kalanlar LSB'den üretildiği için ters sırada yazılır
    kalanlar.reverse()
    return "".join(kalanlar)


def kesir_onlu_rasyonel(kesir_str: str, kaynak_taban: int) -> Tuple[int, int]:
    """
    Kaynak tabandaki kesirli kısmı kayan nokta (float) hassasiyet kaybı olmadan
    tam rasyonel (pay, payda) ikilisi olarak hesaplar.
    
    Örnek: taban 2'de '01101' -> pay = 0*16 + 1*8 + 1*4 + 0*2 + 1*1 = 13
                               payda = 2^5 = 32
                               Değer = 13 / 32
    """
    if not kesir_str:
        return 0, 1

    pay = 0
    payda = 1
    for ch in kesir_str:
        val = CHAR_TO_VAL[ch]
        pay = pay * kaynak_taban + val
        payda = payda * kaynak_taban

    return pay, payda


def kesir_hedefe_cevir_rasyonel(pay: int, payda: int, hedef_taban: int, max_basamak: int = 8) -> Tuple[str, bool]:
    """
    Rasyonel kesri (pay / payda) ardışık çarpma yöntemiyle hedef tabana dönüştürür.
    
    Her adımda:
    (pay * hedef_taban) // payda -> Hedef basamak (en büyük ağırlıklıdan başlar)
    (pay * hedef_taban) % payda  -> Yeni pay
    
    Dönüş:
        (basamaklar_str, kesin_mi)
        kesin_mi: True ise dönüşüm tam basamakta bitmiştir (=).
                  False ise 8 basamakta bitmemiş, kesilmiştir (approximate, ≈).
    """
    if pay == 0:
        return "0", True

    basamaklar = []
    mevcut_pay = pay
    kesin = False

    for _ in range(max_basamak):
        carpim = mevcut_pay * hedef_taban
        basamak = carpim // payda
        mevcut_pay = carpim % payda
        basamaklar.append(VAL_TO_CHAR[basamak])

        if mevcut_pay == 0:
            kesin = True
            break

    return "".join(basamaklar), kesin


def sayi_donustur(sayi_metni: str, kaynak_taban: int, hedef_taban: int) -> Dict[str, any]:
    """
    Ana dönüşüm fonksiyonu. Girdiyi denetler, dönüşümü gerçekleştirir ve
    ayrıntılı sonuç nesnesi döndürür.
    """
    # 1. Girdi Doğrulama
    tam_str, kesir_str = girdi_dogrula(sayi_metni, kaynak_taban, hedef_taban)

    # 2. Tam Kısım Dönüşümü
    tam_onlu = tam_kisim_onluya_cevir(tam_str, kaynak_taban)
    tam_hedef = tam_kisim_hedefe_cevir(tam_onlu, hedef_taban)

    # 3. Kesirli Kısım Dönüşümü
    if kesir_str:
        pay, payda = kesir_onlu_rasyonel(kesir_str, kaynak_taban)
        kesir_hedef, kesin_mi = kesir_hedefe_cevir_rasyonel(pay, payda, hedef_taban, max_basamak=8)
        
        # Sonuç gösterimi
        sonuc_metni = f"{tam_hedef}.{kesir_hedef}"
        isaret = "=" if kesin_mi else "≈"
        durum = "KESİN (EXACT)" if kesin_mi else "YAKLAŞIK (APPROXIMATE - 8 basamakta kesildi)"
        kesir_onlu_ondalik = pay / payda
    else:
        kesir_hedef = ""
        kesin_mi = True
        sonuc_metni = tam_hedef
        isaret = "="
        durum = "KESİN (EXACT - Tam Sayı)"
        kesir_onlu_ondalik = 0.0

    return {
        "girdi": sayi_metni,
        "kaynak_taban": kaynak_taban,
        "hedef_taban": hedef_taban,
        "tam_kaynak": tam_str,
        "kesir_kaynak": kesir_str,
        "tam_onlu": tam_onlu,
        "kesir_onlu_ondalik": kesir_onlu_ondalik,
        "toplam_onlu": tam_onlu + kesir_onlu_ondalik,
        "tam_hedef": tam_hedef,
        "kesir_hedef": kesir_hedef,
        "sonuc": sonuc_metni,
        "isaret": isaret,
        "kesin_mi": kesin_mi,
        "durum": durum
    }


def test_suite_calistir() -> List[Dict]:
    """
    Deney Yaprağı 1 için tanımlanan en az 8 senaryoyu ve sınır durumları içeren
    kapsamlı test paketini çalıştırır.
    """
    senaryolar = [
        # (Açıklama, Girdi, Kaynak Taban, Hedef Taban, Beklenen Hata Mı?, Beklenen Sonuç)
        ("Örnek Giriş (Kesin Kesirli Dönüşüm)", "101101.01101", 2, 16, False, "2D.68"),
        ("Sıfır Değeri (Tam)", "0", 10, 2, False, "0"),
        ("Yalnızca Kesirli Sayı (. ile başlayan)", ".101", 2, 10, False, "0.625"),
        ("Başında Sıfırlar Bulunan Sayı", "001011.10", 2, 10, False, "11.5"),
        ("Sekiz Basamakta Tamamlanmayan Kesir (Yaklaşık)", "0.1", 10, 2, False, "0.00011001"),
        ("Onaltılıdan Sekizliye Dönüşüm", "2D.68", 16, 8, False, "55.32"),
        ("Hatalı Girdi 1: İkili Tabanda Geçersiz Rakam (2)", "102", 2, 10, True, "Geçersiz karakter"),
        ("Hatalı Girdi 2: Sekizli Tabanda Geçersiz Rakam (8)", "128", 8, 2, True, "Geçersiz karakter"),
        ("Hatalı Girdi 3: Boş Girdi", "   ", 10, 2, True, "Girdi boş olamaz"),
        ("Hatalı Girdi 4: Çoklu Kesir Ayracı", "10.11.01", 2, 16, True, "Birden fazla kesir ayracı"),
        ("Hatalı Girdi 5: Negatif Sayı Girişi", "-101.1", 2, 10, True, "Negatif sayılar kabul edilmez"),
        ("Hatalı Girdi 6: Geçersiz Taban Seçimi", "101", 5, 2, True, "Geçersiz kaynak taban")
    ]

    sonuclar = []
    print("=" * 80)
    print("BLM2007 MANTIK DEVRELERİ - DENEY YAPRAĞI 1 TEST ÇIKTILARI")
    print("=" * 80)

    for i, (tanim, girdi, r_kaynak, r_hedef, hata_bekleniyor, beklenen) in enumerate(senaryolar, 1):
        print(f"\n[TEST {i:02d}] {tanim}")
        print(f"  Girdi: '{girdi}' | Kaynak Taban: {r_kaynak} | Hedef Taban: {r_hedef}")
        try:
            res = sayi_donustur(girdi, r_kaynak, r_hedef)
            if hata_bekleniyor:
                print(f"  BAŞARISIZ: Hata fırlatılması bekleniyordu ancak sonuç üretildi: {res['sonuc']}")
                basarili = False
            else:
                eslesme = (res['sonuc'] == beklenen)
                print(f"  Gerçekleşen: {res['sonuc']} ({res['isaret']}) [{res['durum']}]")
                print(f"  Beklenen:    {beklenen}")
                print(f"  Onluk Ara Değer: {res['toplam_onlu']}")
                print(f"  Durum: {'BAŞARILI (PASSED)' if eslesme else 'UYARI: Beklenenle tam eşleşmedi'}")
                basarili = eslesme
            sonuclar.append({"test_no": i, "tanim": tanim, "girdi": girdi, "r1": r_kaynak, "r2": r_hedef,
                             "basarili": basarili, "cikti": res['sonuc'], "durum": res['durum']})
        except GirdiHatasi as e:
            if hata_bekleniyor:
                print(f"  Beklenen Hata Başarıyla Yakalandı: {e}")
                print("  Durum: BAŞARILI (PASSED - Hata Doğrulandı)")
                basarili = True
            else:
                print(f"  BEKLENMEYEN HATA: {e}")
                basarili = False
            sonuclar.append({"test_no": i, "tanim": tanim, "girdi": girdi, "r1": r_kaynak, "r2": r_hedef,
                             "basarili": basarili, "cikti": f"HATA: {e}", "durum": "REDDEDİLDİ"})

    print("\n" + "=" * 80)
    print("TEST ÖZETİ:")
    toplam_test = len(sonuclar)
    basarili_test = sum(1 for s in sonuclar if s['basarili'])
    print(f"Toplam Test: {toplam_test} | Başarılı: {basarili_test} | Başarısız: {toplam_test - basarili_test}")
    print("=" * 80)
    return sonuclar


if __name__ == "__main__":
    test_suite_calistir()
