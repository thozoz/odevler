# BLM2007 Mantık Devreleri — Deney Yaprağı 2 Çözümü
### Gray Dönüştürücüsü ve Komşuluk Denetimi

**Öğrenci:** Efe Özan (170425062)  
**Tarih:** 10.11.2026  
**Şube / Grup:** Ali Buldu A Grubu  
**İlgili Kodlar:** `gray_donusturucu.py`, `dogrulama_2.py`

---

### 1. XOR Tabanlı İki Yönlü Gray Algoritması

1. **İkili $\rightarrow$ Gray:**
   $$g_{n-1} = b_{n-1}$$
   $$g_i = b_{i+1} \oplus b_i \quad (i = n-2, \dots, 0)$$
   Bit uzunluğu daima korunur.
2. **Gray $\rightarrow$ İkili:**
   $$b_{n-1} = g_{n-1}$$
   $$b_i = b_{i+1} \oplus g_i \quad (i = n-2, \dots, 0)$$
   Burada kritik nokta, ters dönüşümde gelen Gray bitinin bir önceki adımda **hesaplanmış olan ikili bit ($b_{i+1}$)** ile XOR'lanmasıdır.

---

### 2. 0--15 İkili / Gray Tablosu ve Kapanış Analizi

| Onlu ($d$) | İkili ($B$) | Gray ($G$) | Geri Çözülen İkili | Ardışık Bit Farkı ($d \to d+1$) |
|:---:|:---:|:---:|:---:|:---:|
| 0 | `0000` | `0000` | `0000` | - |
| 1 | `0001` | `0001` | `0001` | 1 bit |
| 2 | `0010` | `0011` | `0010` | 1 bit |
| 3 | `0011` | `0010` | `0011` | 1 bit |
| 4 | `0100` | `0110` | `0100` | 1 bit |
| 5 | `0101` | `0111` | `0101` | 1 bit |
| 6 | `0110` | `0101` | `0110` | 1 bit |
| 7 | `0111` | `0100` | `0111` | 1 bit |
| 8 | `1000` | `1100` | `1000` | 1 bit |
| 9 | `1001` | `1101` | `1001` | 1 bit |
| 10 | `1010` | `1111` | `1010` | 1 bit |
| 11 | `1011` | `1110` | `1011` | 1 bit |
| 12 | `1100` | `1010` | `1100` | 1 bit |
| 13 | `1101` | `1011` | `1101` | 1 bit |
| 14 | `1110` | `1001` | `1110` | 1 bit |
| 15 | `1111` | `1000` | `1111` | 1 bit |

#### Kapanış Karşılaştırması (15 $\rightarrow$ 0 vs 9 $\rightarrow$ 0)
- **15 $\rightarrow$ 0 Kapanışı:**
  $\text{Gray}(15) = 1000$, $\text{Gray}(0) = 0000$. Karşılık gelen konumlarda yalnız en anlamlı bit ($b_3$) farklıdır. **Fark: 1 bit.** Dolayısıyla 4 bitlik Gray kodu tam dairesel (cyclic) kapanışa sahiptir.
- **9 $\rightarrow$ 0 Kapanışı (0--9'a kesilmiş dizi):**
  $\text{Gray}(9) = 1101$, $\text{Gray}(0) = 0000$. Aralarında $2^3$, $2^2$ ve $2^0$ konumlarındaki bitler farklıdır. **Fark: 3 bit.** Dizi 0--9 aralığına kesildiğinde dairesel tek bit komşuluk kuralı bozulur.

---

### 3. Uzun Bit Dizileri Doğrulaması

1. **Girdi:** `101110101` (9 bit)
   - $g_8 = 1$
   - $g_7 = 1 \oplus 0 = 1$
   - $g_6 = 0 \oplus 1 = 1$
   - $g_5 = 1 \oplus 1 = 0$
   - $g_4 = 1 \oplus 1 = 0$
   - $g_3 = 1 \oplus 0 = 1$
   - $g_2 = 0 \oplus 1 = 1$
   - $g_1 = 1 \oplus 0 = 1$
   - $g_0 = 0 \oplus 1 = 1$
   - **Gray Sonucu:** `111001111` (9 bit).
   - **Geri Çözüm:** `101110101` (uzunluk ve içerik birebir korundu).
2. **Girdi:** `1000101` (7 bit)
   - **Gray Sonucu:** `1100111` (7 bit).
   - **Geri Çözüm:** `1000101` (uzunluk ve içerik birebir korundu).

---

### 4. Hatalı Yöntem İncelemesi ve Karşı Örnek

Ters yönde de komşu Gray bitlerini XOR'layan hatalı yöntem:
$$b_i = g_{i+1} \oplus g_i$$
16 adet 4 bitlik Gray sözcüğünden 12'sinde yanlış sonuç verir.

#### Karşı Örnek: Gray `1100` (Onlu 8)
- **Doğru Yöntem ($b_i = b_{i+1} \oplus g_i$):**
  - $b_3 = g_3 = 1$
  - $b_2 = b_3 \oplus g_2 = 1 \oplus 1 = 0$
  - $b_1 = b_2 \oplus g_1 = 0 \oplus 0 = 0$
  - $b_0 = b_1 \oplus g_0 = 0 \oplus 0 = 0$
  - **Sonuç:** `1000` (Onlu 8, DOĞRU).
- **Hatalı Yöntem ($b_i = g_{i+1} \oplus g_i$):**
  - $b_3 = g_3 = 1$
  - $b_2 = g_3 \oplus g_2 = 1 \oplus 1 = 0$
  - $b_1 = g_2 \oplus g_1 = 1 \oplus 0 = \mathbf{1} \quad \leftarrow$ **İlk ayrışan adım (1. basamak, ağırlık $2^1$).**
  - $b_0 = g_1 \oplus g_0 = 0 \oplus 0 = 0$
  - **Sonuç:** `1010` (Onlu 10, YANLIŞ).

#### Rastgele İki Gray Sözcüğü Arasındaki Mesafe
Gray kodu yalnız **ardışık sayıların** kod sözcükleri arasında tek bit farkı (Hamming mesafesi = 1) garanti eder. Rastgele seçilen iki sözcük arasında tek bit farkı olmak zorunda değildir:
- Örneğin $\text{Gray}(0) = 0000$ ile $\text{Gray}(2) = 0011$ arasında **2 bit**,
- $\text{Gray}(0) = 0000$ ile $\text{Gray}(10) = 1111$ arasında **4 bit** fark vardır.
