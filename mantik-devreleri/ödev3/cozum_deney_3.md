# BLM2007 Mantık Devreleri — Deney Yaprağı 3 Çözümü
### Beş Bitte İki Bir ve Eşlik Denetimi

**Öğrenci:** Efe Özan (170425062)  
**Tarih:** 10.11.2026  
**Şube / Grup:** Ali Buldu A Grubu  
**İlgili Kodlar:** `bes_bit_ve_eslik.py`, `dogrulama_3.py`

---

### 1. 5'te 2 ve Eşlik Denetleyicileri Mimarisi

1. **5'te 2 (2-out-of-5) Sözcük Denetleyicisi:**
   - 7-4-2-1-0 ağırlıklarına dayanır.
   - Her geçerli sözcük tam olarak 5 bit uzunluğunda olmalı ve **tam olarak iki adet '1'** içermelidir.
   - **11000'ın Özel Sıfır Ataması Gerekçesi:**
     Normal ağırlık aritmetiğinde $0\cdot 7 + 0\cdot 4 + 0\cdot 2 + 0\cdot 1 + 0\cdot 0 = 0$ olduğu için sıfır sayısı `00000` (hiç 1 içermeyen desen) ile elde edilir. Ancak bu kodun hata denetim kuralı "her sözcükte kesinlikle iki adet 1 bulunması"dır. `00000` bu kuralı ihlal eder. Ağırlık toplamı $7+4=11$ olan `11000` deseni ise 0--9 onlu rakamlarının hiçbiriyle çakışmaz (en büyük rakam 9'dur). Kodun temel güvenlik koşulunu korumak adına sıfır rakamına özel olarak `11000` sözcüğü atanmıştır.
2. **Eşlik (Parity) Paket Denetleyicisi:**
   - 7 veri bitinin soluna bir $p$ eşlik biti eklenerek 8 bitlik paket ($p\ d_6 d_5 d_4 d_3 d_2 d_1 d_0$) oluşturulur.
   - Çift eşlik modunda paketteki toplam 1 sayısı çift, tek eşlik modunda tek olmalıdır.

---

### 2. 5'te 2 Kodunda Hata Taramaları (50 ve 100 Deney)

- **Tek Bit Hata Taraması (50 Deney):**
  10 geçerli sözcüğün her birinde 5 farklı bit konumu terslendi ($10 \times 5 = 50$).
  - 1 olan bit 0 olursa toplam 1 sayısı 1'e düşer.
  - 0 olan bit 1 olursa toplam 1 sayısı 3'e çıkar.
  - Her iki durumda da 1 sayısı 2 olamayacağından hataların **50/50'si (\%100)** denetleyici tarafından saptandı (0 hata kaçtı).
- **İki Bit Hata Taraması (100 Deney):**
  10 geçerli sözcüğün her birinde $\binom{5}{2} = 10$ farklı bit çifti terslendi ($10 \times 10 = 100$).
  - İki adet 1 bitinin 0 yapıldığı $\binom{2}{2} = 1$ durum $\to$ 1 sayısı 0 olur (**saptandı**, $1\times 10 = 10$).
  - İki adet 0 bitinin 1 yapıldığı $\binom{3}{2} = 3$ durum $\to$ 1 sayısı 4 olur (**saptandı**, $3\times 10 = 30$).
  - Bir 1 bitinin 0, bir 0 bitinin 1 yapıldığı $2 \times 3 = 6$ durum $\to$ 1 sayısı yine 2 kalır!
  - 5 bitte 2 adet 1 içeren toplam desen sayısı $\binom{5}{2} = 10$'dur ve bu 10 desenin 10'u da 0--9 rakamlarına atanmıştır. Bu nedenle 1 sayısı 2 kalan her iki bit hatası başka bir geçerli rakama dönüşür ve **KAÇAR** ($6 \times 10 = \mathbf{60}$ hata kaçtı).
  - **Kaçan Hata Örneği:** Eski rakam 0 (`11000`), 7 ve 2 ağırlıklı bitler terslenirse `01100` olur; bu da Rakam 6'nın geçerli kodudur.

---

### 3. Eşlik Denetimi: 1000011 ve 1000001 Paketleri

| Veri (7 bit) | 1 Sayısı | Çift Eşlik ($p$) | Çift Eşlik Paketi | Tek Eşlik ($p$) | Tek Eşlik Paketi |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `1000011` | 3 (Tek) | `1` | `11000011` (4 adet 1) | `0` | `01000011` (3 adet 1) |
| `1000001` | 2 (Çift) | `0` | `01000001` (2 adet 1) | `1` | `11000001` (3 adet 1) |

#### Çift Eşlikli 11000011 Paketinde Hata Taraması
- **8 Tek Bit Terslemesi:** 1 sayısı 3 veya 5 olur (tek sayı). Çift eşlik kuralı bozulur $\to$ **8/8 saptandı**.
- **28 İki Bit Terslemesi:** İki bit değiştiğinde toplam 1 sayısı $\pm 2$ veya $0$ değişir; parite (teklik/çiftlik) değişmez. Toplam 1 sayısı çift (2, 4 veya 6) kalır $\to$ **28'i de KAÇTI (0/28 saptandı)**.
- **Tek/Çift Tersleme Kuralı:** Tek sayıda bit hatası pariteyi daima bozar ve saptanır; çift sayıda bit hatası pariteyi korur ve denetimden daima kaçar.

---

### 4. Düzeltme Sınırı, Hata Yeri ve 01000 Analizi

Geçersiz `01000` deseninde yalnızca 4 ağırlıklı bit 1’dir. Soruda istenen iki özgün sözcük örneği `11000` ve `01100`’dır; toplam dört aday vardır. Tek bit hatası varsayımıyla olası özgün geçerli 5'te 2 sözcükleri:
1. `11000` (Rakam 0, eğer 7 ağırlıklı bit bozulduysa)
2. `01100` (Rakam 6, eğer 2 ağırlıklı bit bozulduysa)
3. `01010` (Rakam 5, eğer 1 ağırlıklı bit bozulduysa)
4. `01001` (Rakam 4, eğer 0 ağırlıklı bit bozulduysa)

Birden fazla (4 adet) olası özgün aday bulunduğu için alıcı hatanın hangi bitte olduğunu tespit edemez (hata yeri belirlenemez) ve düzeltme yapamaz.

- **Yalnızca $p$ Bitinin Terslenmesi:** Çift eşlikli `11000011` paketinde yalnız $p$ biti terslenip 0 olursa paket `01000011` olur ve denetleyici eşlik hatası verir. Fakat pakette taşınan 7 veri biti (`1000011`) tamamen sağlamdır!
- **Kavramsal Ayrım:**
  - *Hata Saptama (Detection):* Kodun söz dizimsel kuralının bozulduğunu fark etme.
  - *Hatanın Yerini Bulma (Localization):* Bozuk bitin konumunu belirleme (en az Hamming mesafesi 3 gerektirir).
  - *Veri Bitlerinin Doğruluğu:* Eşlik hatası oluştuğunda bile verinin kendisi sağlam kalmış olabilir.
