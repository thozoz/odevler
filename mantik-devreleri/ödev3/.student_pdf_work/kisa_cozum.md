---
title: "Mantık Devreleri - Ödev 3"
subtitle: "Ders 5 / Kodlama (Deney yaprakları 1-4)"
author: "Efe Özan - 170425062"
date: "10.11.2026"
lang: tr-TR
---

Deneylerin hesapları ve ara kayıtları burada. Her deneyin programı ve doğrulama kodu `kodlar/` klasöründedir:

- Deney 1: `rakam_donusturucu.py` ve `dogrulama_1.py`
- Deney 2: `gray_donusturucu.py` ve `dogrulama_2.py`
- Deney 3: `bes_bit_ve_eslik.py` ve `dogrulama_3.py`
- Deney 4: `karakter_ve_barkod.py` ve `dogrulama_4.py`

## Deney 1 - BCD, Artı-3 ve Aiken Rakam Dönüştürücüsü
- 48: BCD `0100 1000`, Artı-3 `0111 1011`, Aiken `0100 1110`.
- 003: BCD `0000 0000 0011`, Artı-3 `0011 0011 0110`, Aiken `0000 0000 0011`.
- 263 onlu sayısı saf ikili ile 9 bit (`100000111_2`), BCD ile 12 bit (`0010 0110 0011`). BCD ikili okunursa 611 eder.
- 16 desen taramasında BCD, Artı-3 ve Aiken için 10 geçerli, 6 geçersiz desen kümesi belirlendi.
- Aiken'de 0101 ve 1011'in ağırlıklı toplamı 5'tir; ancak kendinden tümleyen kuralı gereği 5 = `1011`'dir, `0101` geçersizdir.
- Artı-3 ve Aiken kendinden tümleyen kodlardır (10/10 doğrulandı). BCD kendinden tümleyen değildir (d=2 BCD 0010, tersi 1101 geçersizdir; 7'nin BCD'si 0111'dir).

## Deney 2 - Gray Dönüştürücüsü ve Komşuluk Denetimi
- İkili -> Gray: $g_{n-1}=b_{n-1}$, $g_i = b_{i+1} \oplus b_i$.
- Gray -> İkili: $b_{n-1}=g_{n-1}$, $b_i = b_{i+1} \oplus g_i$ (önceki hesaplanan ikili bit kullanılır).
- 0-15 arası 15 ardışık geçişte Hamming mesafesi 1'dir.
- 15 -> 0 kapanışında fark 1 bittir (dairesel kod). 9 -> 0 kapanışında (0-9 kesilmiş dizi) fark 3 bittir (dairesellik bozulur).
- `101110101` -> Gray: `111001111` (9 bit); `1000101` -> Gray: `1100111` (7 bit).
- Hatalı ters yöntem ($b_i = g_{i+1} \oplus g_i$) 16 sözcükten 12'sinde yanlış sonuç verir. Gray `1100` için doğru ikili `1000` iken hatalı yöntem `1010` verir (ilk ayrışma 1. basamak).

## Deney 3 - Beş Bitte İki Bir ve Eşlik Denetimi
- 5'te 2 denetleyicisi: 5 bit ve tam 2 adet '1'. 11000 özel sıfır ataması: 00000 sıfır adet 1 içerdiği için kuralı bozar; ağırlığı 11 olan 11000 rakamlarla çakışmadığından 0'a atanmıştır.
- 50 tek bit hatasının 50'si de saptandı (%100).
- 100 iki bit hatasından 40'ı saptandı, 60'ı ise kaçtı (%60, 1 sayısı 2 kalarak başka rakama dönüştü).
- `1000011` için çift eşlik `11000011` (p=1), tek eşlik `01000011` (p=0).
- `1000001` için çift eşlik `01000001` (p=0), tek eşlik `11000001` (p=1).
- `11000011` paketinde 8 tek bit hatası saptandı; 28 iki bit hatasının tümü kaçtı.
- Tek bit hatası pariteyi değiştirir (saptanır); çift bit hatası pariteyi korur (kaçar).
- Geçersiz 01000 için 4 olası aday sözcük vardır (0, 6, 5, 4). Hata konumu tek eşlikle belirlenemez.

## Deney 4 - Karakter Kodları ve Barkodun Bağımsız Doğrulanması
- `HELP 2031` ASCII hex: `48 45 4C 50 20 32 30 33 31`, EBCDIC hex: `C8 C5 D3 D7 40 F2 F0 F3 F1`.
- H karakteri: ASCII $48_{16} = 01001000_2 = 72_{10}$; EBCDIC $C8_{16} = 11001000_2 = 200_{10}$.
- Çapraz çözüm denemesi geçersiz bayt hatası verir.
- MSB ekleme/kesme L'de (ASCII 4C -> CC != D3) ve 0'da (ASCII 30 -> B0 != F0) başarısız olur.
- `python-barcode` ile üretilen `HELP 2031`, `HELP2031`, `000123`, `123` barkodları `pyzbar` ile birebir doğrulandı.
- Üç görünüm deneyi: Özgün %100 başarı, küçültülmüş (1/4) %0 başarı (piksel bulanıklığı).
- Üreticinin metni ekranda göstermesi bir çizim işlemidir; optik okuma kanıtı değildir.
