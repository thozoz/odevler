# BLM2007 Mantık Devreleri Laboratuvarı — Ödev 2 Çözüm Raporu
## Deney Yaprağı 1: Elde adımlarını gösteren ikili toplayıcı

**Öğrenci Adı Soyadı:** Efe Özan  
**Öğrenci No:** 170425062  
**Bölüm:** Bilgisayar Mühendisliği  
**Ders:** BLM2007 Mantık Devreleri (Prof. Dr. Ali Buldu)  
**Tarih:** 29 Ekim 2026  
**Şube / Grup:** Ali Buldu A Grubu **İmza:** ......................

---

- **Amaç:** Toplama algoritmasını bit düzeyinde tasarlamak ve son eldenin sayısal anlamını doğrulamak.
- **Tanım:** Girdiler aynı uzunlukta iki işaretsiz ikili sayı ve $0$ ya da $1$ olan başlangıç eldesidir. Çıktılar $n$ bitlik toplam, son elde ve her sütunun işlem kaydıdır ($n = 4$).
- **Kod dosyaları:** `ikili_toplayici.py` ve `dogrulama_1.py`.

---

### 1. İki bit ve gelen elde için sonuç/elde tablosu ve algoritma

Her sütunda $a_i, b_i \in \{0,1\}$ ve gelen elde $c_{in} \in \{0,1\}$ için 8 olasılık:

| $a_i$ | $b_i$ | $c_{in}$ | Sonuç Biti ($s_i$) | Çıkan Elde ($c_{out}$) |
|:---:|:---:|:---:|:---:|:---:|
| 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 1 | 0 |
| 0 | 1 | 0 | 1 | 0 |
| 0 | 1 | 1 | 0 | 1 |
| 1 | 0 | 0 | 1 | 0 |
| 1 | 0 | 1 | 0 | 1 |
| 1 | 1 | 0 | 0 | 1 |
| 1 | 1 | 1 | 1 | 1 |

Algoritma (`bit_duzeyi_topla`), sağdan sola ($i = 0 \dots n-1$) ilerler; her adımda sütun ağırlığı $2^i$, girdi bitleri $a_i, b_i$, gelen elde $c_{in}$, sonuç biti $s_i$ ve çıkan elde $c_{out}$ değerlerini kaydeder.

### 2. Dört işlemin beklenen sonuçları ve sütun kayıtları

- **Beklenenler:**
  - $c_0 = 0$: `0101 + 0011` $\to$ toplam `1000`, son elde `0` (değer $8$)
  - $c_0 = 0$: `1111 + 0001` $\to$ toplam `0000`, son elde `1` (değer $16$)
  - $c_0 = 1$: `1111 + 0000` $\to$ toplam `0000`, son elde `1` (değer $16$)
  - $c_0 = 1$: `1111 + 1111` $\to$ toplam `1111`, son elde `1` (değer $31$)

| İşlem | Sütun 0 ($2^0=1$) $(a_0,b_0,c_{in}\to s_0,c_{out})$ | Sütun 1 ($2^1=2$) $(a_1,b_1,c_{in}\to s_1,c_{out})$ | Sütun 2 ($2^2=4$) $(a_2,b_2,c_{in}\to s_2,c_{out})$ | Sütun 3 ($2^3=8$) $(a_3,b_3,c_{in}\to s_3,c_{out})$ | Çıktı ($S$, Son Elde) |
|:---|:---:|:---:|:---:|:---:|:---:|
| `0101+0011` ($c_0=0$) | `1,1,0 -> 0,1` | `0,1,1 -> 0,1` | `1,0,1 -> 0,1` | `0,0,1 -> 1,0` | `1000`, elde `0` ($8$) |
| `1111+0001` ($c_0=0$) | `1,1,0 -> 0,1` | `1,0,1 -> 0,1` | `1,0,1 -> 0,1` | `1,0,1 -> 0,1` | `0000`, elde `1` ($16$) |
| `1111+0000` ($c_0=1$) | `1,0,1 -> 0,1` | `1,0,1 -> 0,1` | `1,0,1 -> 0,1` | `1,0,1 -> 0,1` | `0000`, elde `1` ($16$) |
| `1111+1111` ($c_0=1$) | `1,1,1 -> 1,1` | `1,1,1 -> 1,1` | `1,1,1 -> 1,1` | `1,1,1 -> 1,1` | `1111`, elde `1` ($31$) |

### 3. 512 test özeti

$16 \times 16 \times 2 = 512$ kombinasyonun tamamında $\text{Değer}(S) + c_4 \cdot 16 = A + B + c_0$ eşitliği sağlanmıştır (512/512 başarılı; 256 testte $c_4=0$, 256 testte $c_4=1$).

### 4. Ret kuralları ve son eldenin sayısal anlamı

- **Ret testleri:** Boş girdi `("", "0101", 0)` $\to$ Reddedildi; Geçersiz bit `("0121", "0011", 0)` $\to$ Reddedildi; Farklı uzunluk `("0101", "11", 0)` $\to$ Reddedildi.
- **Son elde gerekçesi:** $n$ bitlik toplamada son elde $c_n$, $2^n$ basamak ağırlığını taşır. Yok sayılırsa sonuçtan **$2^n$** değer eksilir. Sınır örneği: $n=4$ için `1111 + 0001` ($15+1=16$) işleminde $S=\text{`0000`}, c_4=1$ çıkar; son elde atılırsa $16$ yerine $0$ elde edilir ($2^4=16$ kayıp).
- **YZ önerisi değerlendirme/doğrulama:** YZ'nin verdiği tam toplayıcı tablosunu ve sağdan sola döngü yapısını 4 zorunlu işlemde kağıt üzerinde adım adım takip ederek doğruladım.
