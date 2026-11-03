# NYP Lab Soruları ve Hocanın Cevapları

Kaynak: `NYP-hafta1.pdf`, `NYP_Hafta3.pdf`, `NYP_Hafta3.1.pdf`, `NYP_4.pdf`.
Kodlar slaytlardaki ekran görüntülerinden aktarıldı. `⚠️ Not` = hocanın cevabında belirgin hata/eksik.

---

## Hafta 1

### Örnek 1 – String birleştirme (çıktı ne olur?)

```java
public class Main {
    public static void main(String[] args) {
        int x = 5;
        int y = 10;
        System.out.println(x+y);
        System.out.println("x+y");
        System.out.println("" + x + y);
        System.out.println("5" + "10");
        System.out.println(5 + 10 + x + y);
        System.out.println("output " + (x + y));
        System.out.println("output " + x + y);
    }
}
```

Çıktı:
```
15
x+y
510
510
30
output 15
output 510
```

### Örnek 2 – Kullanıcıdan veri alma (Scanner)

```java
import java.util.*;
// import Java'da dahil etmek anlamında kullanılmaktadır.
public class Main {
    public static void main(String[] args) {
        int yas;
        Scanner girdi = new Scanner(System.in);
        System.out.print("Adınızı giriniz: ");
        String ad = girdi.next();
        System.out.print("Soyadınızı giriniz: ");
        String soyad = girdi.next();
        System.out.print("Yasinizi giriniz: ");
        yas = girdi.nextInt();
        System.out.println("Adı: "+ad+"\nSoyadı: "+soyad+"\nYaş: "+yas);
    }
}
```

Scanner metotları: `nextInt()` tam sayı, `nextDouble()` ondalıklı, `next()` tek kelime String, `nextLine()` satırın tamamı.

### Soru 1 – Dairenin alanını hesaplayan programı kodlayınız.

```java
import java.util.*;
public class Main {
    public static void main(String[] args) {
        int r, pi = 3;
        double alan, cevre;

        Scanner girdi = new Scanner(System.in); //Kullanıcıdan değer alabilmek için Scanner sınıfını kullandık

        System.out.println("Daire yarı çapını giriniz : ");
        r = girdi.nextInt();
        cevre = 2 * pi * r;
        alan = pi * (r*r);
        System.out.println("Dairenin Alanı : " + alan);
        System.out.println("Dairenin Çevresi : " + cevre);
    }
}
```

Çıktı (r=5): `Dairenin Alanı : 75.0`, `Dairenin Çevresi : 30.0`

> ⚠️ Not: Hoca `pi = 3` (int) almış, sonuç yaklaşık. Doğrusu `double pi = Math.PI;` (r=5 için alan 78.54).

### Soru 2 – Girilen sayının son rakamını ekrana basan programı kodlayınız.

```java
import java.util.*;
public class Main {
    public static void main(String[] args) {
        System.out.print("Bir sayı giriniz : ");
        // Kullanıcıdan sayı istenir

        Scanner sayim = new Scanner(System.in);
        // sayim isimli Scanner sınıfı oluşturuyoruz. Bu konsoldan giriş almamızı sağlar.

        int sayi = sayim.nextInt();
        // Tamsayı tipinde(int) sayi değişkenini oluşturup bu değişkene konsoldan alınan değeri atıyoruz.

        System.out.println(sayi % 10);
        // Sayıyının 10 ile modu alınır (yani sayıyı 10'a böldüğümüzde kalan sayı döner) ve ekrana yazdırılır.
    }
}
```

Çıktı (1453): `3`

### Soru 3 – Verilen sayıyı ters çeviren programı yazınız.

```java
import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner giris = new Scanner(System.in);

        System.out.print("Bir sayi giriniz: ");
        int sayi = giris.nextInt();

        System.out.print("Girdiğiniz sayinin tersten yazılısı = ");
        while (sayi > 0) {
            System.out.print(sayi % 10);
            sayi /= 10;
        }
    }
}
```

Çıktı (2023): `Girdiğiniz sayinin tersten yazılısı = 3202`

### Soru 4 – Kullanıcıdan alınan 5 adet sayının ortalamasını alan programı kodlayınız.

```java
import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner klavye = new Scanner(System.in);
        System.out.println("ilk sayiyi giriniz: ");
        int sayi1 = klavye.nextInt();
        System.out.println("İkinci sayiyi giriniz: ");
        int sayi2 = klavye.nextInt();
        System.out.println("Üçüncü sayiyi giriniz: ");
        int sayi3 = klavye.nextInt();
        System.out.println("Dördüncü sayiyi giriniz: ");
        int sayi4 = klavye.nextInt();
        System.out.println("Beşinci sayiyi giriniz: ");
        int sayi5 = klavye.nextInt();

        int toplam = sayi1+sayi2+sayi3+sayi4+sayi5;
        double ortalama = toplam/5.0;
        System.out.println("Bu 5 sayinin ortalaması: "+ortalama);
    }
}
```

Çıktı (1,2,3,4,5): `Bu 5 sayinin ortalaması: 3.0`

> `5.0` ile bölmek önemli: `toplam/5` tam sayı bölmesi yapar, küsurat kaybolur.

### Soru 5 – Sayı Tahmin Oyunu

> Belirlenen sabit bir sayıyı bulmaya çalışan bir oyuncu için sayı tahmin oyununu kodlayınız. Oyun kullanıcının tahmini doğru olmadığı sürece devam edecek. Bilgisayarın sayı üretmesi için **Random** sınıfı kullanılacaktır.
>
> Sözde kod: DONGU (tahmin ≠ sayı): tahmin al; tahmin < sayı ise "Daha büyük", tahmin > sayı ise "Daha küçük". Sonra "Tahmin Doğru, Oyun Sonlandı".

```java
import java.util.*;
import java.util.Random;
public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        Random rnd = new Random();
        System.out.println("Sayı tahmin oyununa hoş geldiniz!");
        System.out.println("Lütfen 1-100 arasında bir sayı giriniz: ");
// Kullanıcıdan sayı alıyoruz
        int tahmin = input.nextInt();
// Bilgisayardan rastgele sayı alıyoruz
        int sayi = rnd.nextInt(101);
        while (tahmin != sayi) {
            if (tahmin < 0 || tahmin > 100) {
                System.out.println("1 ile 100 arasında bir değer giriniz: ");
                tahmin = input.nextInt(); }

            else if (tahmin < sayi) {
                System.out.println("Daha büyük bir sayı giriniz: ");
                tahmin = input.nextInt(); }
            else {
                System.out.println("Daha küçük bir sayı giriniz: ");
                tahmin = input.nextInt(); }
        }
// Eğer sayımız ve tahmin birbirine eşitse while döngüsüne girmez
// ve print komutunu yazdırırız
        System.out.println("Tebrikler, kazandınız!");
    }
}
```

### Soru 6 – Int tipindeki bir değişkene 1-12 arası değer atayarak, yılın aylarını ekranda yazdıran programı switch-case yapısını kullanarak yazınız.

```java
public class Main {
    public static void main(String[] args) {
        //Secilen ay degeri
        int ayDegeri = 5;
        //Yazdırılacak ay degeri
        String ayDegeriStr = null;

        //switch - case ile hangi ayın hangi sayıya denk geldiğinin belirtildiği bölüm
        switch (ayDegeri) {
            case 1:
                ayDegeriStr = "Ocak";
                break;
            case 2:
                ayDegeriStr = "Şubat";
                break;
            case 3:
                ayDegeriStr = "Mart";
                break;
            case 4:
                ayDegeriStr = "Nisan";
                break;
            case 5:
                ayDegeriStr = "Mayıs";
                break;
            case 6:
                ayDegeriStr = "Haziran";
                break;
            case 7:
                ayDegeriStr = "Temmuz";
                break;
            case 8:
                ayDegeriStr = "Ağustos";
                break;
            case 9:
                ayDegeriStr = "Eylül";
                break;
            case 10:
                ayDegeriStr = "Ekim";
                break;
            case 11:
                ayDegeriStr = "Kasım";
                break;
            case 12:
                ayDegeriStr = "Aralık";
                break;
            default:
                break;
        }
        //Konsol ekranına seçilen ayın yazdırıldığı bölüm
        System.out.println("Seçilen Ay Değeri: " + ayDegeriStr);
    }
}
```

### Soru 7 – 0'dan başlayarak 150'ye kadar olan sayıları döngü kullanıp 3'er 3'er arttırarak ekrana yazınız.

```java
public class Main {
    public static void main(String[] args) {
        for (int i = 0; i <= 150; i += 3) {
            System.out.println("Sayi: " + i);
        }
    }
}
```

Çıktı: `Sayi: 0`, `Sayi: 3`, `Sayi: 6` ... `Sayi: 150`

### Soru 8 – N faktöriyel değerini while döngüsü kullanarak hesaplayan programı yazınız.

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner reader = new Scanner(System.in);
        System.out.print("Bir Sayı Girin:");

        int num = reader.nextInt();
        int sayac = num;
        long faktoriyel = 1;
        while (sayac > 1)
        {
            faktoriyel *= sayac;
            sayac--;
        }
        /* for(int i = 1; i <= num; ++i)
        {
            faktoriyel *= i;
        }*/
        System.out.printf("%d Sayısının Faktöriyeli = %d \n", num, faktoriyel);
    }
}
```

Çıktı (12): `12 Sayısının Faktöriyeli = 479001600`

### Ödev_1

- 1'den 50'ye kadar olan tek ve çift sayıların toplamını bulan programı kodlayınız.
  (`1'den 50 kadar olan tek sayıların toplamı:…` / `çift sayıların toplamı:…`)
- 12345 sayısının içinde 7 rakamının olup olmadığını kontrol eden programı yazınız.

> Hocanın cevabı slaytta yok.

### Ödev_2

Diziler, çok boyutlu diziler/matrisler, String'ler ve fonksiyonlar/metotlar konularını tekrar edin. (Kod sorusu değil.)

---

## Hafta 3 – Sınıf / Nesne

### Örnek – Musteri sınıfı (Classlar referans tiptir)

`Musteri.java`
```java
public class Musteri {
    public void Add (){
        System.out.println("Musteri Eklendi");
    }

    public void Remove (){
        System.out.println("Musteri Silindi");
    }

    public void Update (){
        System.out.println("Musteri Bilgileri Güncellendi");
    }
}
```

`Main.java` (ilk hali)
```java
public class Main {
    public static void main(String[] args) {
        Musteri musteri1 = new Musteri();

        musteri1.Add();
        musteri1.Remove();
        musteri1.Update();
    }
}
```

Çıktı:
```
Musteri Eklendi
Musteri Silindi
Musteri Bilgileri Güncellendi
```

`Main.java` (referans tip örneği)
```java
public class Main {
    public static void main(String[] args) {
        Musteri musteri1 = new Musteri();
        Musteri musteri2 = new Musteri();

        musteri1 = musteri2;

        musteri1.Add();
        musteri1.Remove();
        musteri1.Update();
    }
}
```

`musteri1 = musteri2` sonrası iki değişken aynı nesneyi gösterir; ilk `musteri1` nesnesi sahipsiz kalır ve **Garbage Collection (çöp toplayıcı)** tarafından temizlenir (otomatik bellek yönetim mekanizması).

### Soru – Hesap Makinesi Tasarımı

> 1. 'HesapMakinesi' isimli yeni proje oluşturunuz.
> 2. src klasörü içine 'DortIslem' isimli yeni class oluşturunuz.
> 3. DortIslem class içinde toplama, çıkartma, çarpma ve bölme işlemlerini gerçekleştiren fonksiyonlar tanımlayınız. (2 parametreli)
> 4. Main içerisinde sınıfı çağırınız. 5,12 sayıları için fonksiyonları çalıştırınız.

`DortIslem.java`
```java
public class DortIslem {

    public int Topla (int sayi1, int sayi2){
        return sayi1 + sayi2;
    }

    public int Cikar (int sayi1, int sayi2){
        return sayi1 - sayi2;
    }

    public int Carp (int sayi1, int sayi2){
        return sayi1 * sayi2;
    }

    public int Bol (int sayi1, int sayi2){
        return sayi1 / sayi2;
    }
}
```

`Main.java`
```java
public class Main {
    public static void main(String[] args) {

        DortIslem islem = new DortIslem();

        int deger = islem.Topla(5,12);

        System.out.println("İki sayının toplama sonucu= " + deger);

        deger = islem.Cikar(5,12);

        System.out.println("İki sayının çıkartma sonucu= " + deger);

        deger = islem.Carp(5,12);

        System.out.println("İki sayının çarpma sonucu= " + deger);

        deger = islem.Bol(5,12);

        System.out.println("İki sayının bölme sonucu= " + deger);
    }
}
```

Çıktı:
```
İki sayının toplama sonucu= 17
İki sayının çıkartma sonucu= -7
İki sayının çarpma sonucu= 60
İki sayının bölme sonucu= 0
```

(Bölme 0 çünkü `int / int` tam sayı bölmesi: 5/12 = 0.)

### Soru – Okul (Sınıf içinde field tanımlama ve sınıf içinde sınıf çağırma)

> 1. 'Okul' isimli yeni proje oluşturunuz.
> 2. 'OgrenciBilgileri' isimli yeni class oluşturunuz ve ogrenciNumarasi, ogrenciAdi, ogrenciTc, ogrenciYas değişkenlerini tanımlayınız.
> 3. 'OgrenciIslemleri' isimli yeni class oluşturunuz ve öğrenciye dair fonksiyonları giriniz. (Öğrenci ekleme, silme, güncelleme)
> 4. Main içerisinde sınıfları çağırınız. Bir öğrenci kaydı gerçekleştiriniz.

`OgrenciBilgileri.java`
```java
public class OgrenciBilgileri {

    int ogrenciNumarasi;
    String ogrenciAdi;
    int ogrenciTc;
    int ogrenciYas;
}
```

`OgrenciIslemleri.java`
```java
public class OgrenciIslemleri {
    public void Ekle (OgrenciBilgileri ogrenciBilgileri){
        //Veritabanı veya dosyalama

        System.out.println("Öğrenci başarı ile kayıt edilmiştir.");
    }

    public void Sil (OgrenciBilgileri ogrenciBilgileri){
        //Veritabanı veya dosyalama

        System.out.println("Öğrenci bilgileri silinmiştir.");
    }

    public void Guncelle (OgrenciBilgileri ogrenciBilgileri){

        System.out.println("Öğrenci bilgileri güncellenmiştir .");
    }
}
```

`Main.java`
```java
public class Main {
    public static void main(String[] args) {
        OgrenciBilgileri ogrenciBilgileri = new OgrenciBilgileri();
        ogrenciBilgileri.ogrenciAdi = "Zeynep Şeyda";
        ogrenciBilgileri.ogrenciYas=3;
        ogrenciBilgileri.ogrenciTc=12345;
        ogrenciBilgileri.ogrenciNumarasi=1;

        System.out.println(ogrenciBilgileri.ogrenciAdi);

        OgrenciIslemleri ogrenciIslemleri = new OgrenciIslemleri();

        ogrenciIslemleri.Ekle(ogrenciBilgileri);
    }
}
```

Çıktı:
```
Zeynep Şeyda
Öğrenci başarı ile kayıt edilmiştir.
```

### Encapsulation (Kapsülleme) – private alan + Getter/Setter

Erişim belirteçleri:
- **public**: Bütün sınıflar erişebilir (diğer projelerden de).
- **private**: Sadece tanımlandığı sınıftan erişilebilir.
- **internal**: Aynı derleyici (assembly) içindeki tüm sınıflardan erişilir. (Slayttaki bilgi; Java'da yok, C#'tan. Java'daki karşılığı "default/package-private".)
- **protected**: Tanımlandığı sınıf ve ondan türetilen sınıflar erişebilir.

`ogrenciNumarasi` alanı `private` yapılınca Main'deki `ogrenciBilgileri.ogrenciNumarasi=1;` satırı derlenmez:

```
java: ogrenciNumarasi has private access in OgrenciBilgileri
```

**Çözüm = Getter ve Setter**

`OgrenciBilgileri.java`
```java
public class OgrenciBilgileri {

    private int ogrenciNumarasi;
    private String ogrenciAdi;
    private int ogrenciTc;
    private int ogrenciYas;

    public int getOgrenciNumarasi(){
        return ogrenciNumarasi;
    }

    public String getOgrenciAdi(){
        return ogrenciAdi;
    }

    public int getOgrenciTc(){
        return ogrenciTc;
    }

    public int getOgrenciYas(){
        return ogrenciYas;
    }

    public void setOgrenciNumarasi (int ogrenciNumarasi){
        this.ogrenciNumarasi = ogrenciNumarasi;
    }

    public void setOgrenciAdi (String ogrenciAdi){
        this.ogrenciAdi = ogrenciAdi;
    }

    public void setOgrenciTc (int ogrenciTc){
        this.ogrenciTc = ogrenciTc;
    }

    public void setOgrenciYas (int ogrenciYas){
        this.ogrenciYas = ogrenciYas;
    }
}
```

`Main.java`
```java
public class Main {
    public static void main(String[] args) {
        OgrenciBilgileri ogrenciBilgileri = new OgrenciBilgileri();

        ogrenciBilgileri.setOgrenciNumarasi(1);
        ogrenciBilgileri.setOgrenciAdi("Zeynep Şeyda");
        ogrenciBilgileri.setOgrenciYas(3);
        ogrenciBilgileri.setOgrenciTc(12345);

        System.out.println(ogrenciBilgileri.getOgrenciAdi());

        OgrenciIslemleri ogrenciIslemleri = new OgrenciIslemleri();

        ogrenciIslemleri.Ekle(ogrenciBilgileri);
    }
}
```

Çıktı:
```
Zeynep Şeyda
Öğrenci başarı ile kayıt edilmiştir.
```

### Constructor (Yapıcı Metot)

- `new` ile nesne oluşturulurken ilk çalışan metottur. Tanımlamasak da her class'ın bir **default (varsayılan)** constructor'ı vardır.
- Kullanım amacı: nesneye ilk değer atamak, kullanıcıyı belli değerleri vermeye zorlamak, nesne oluşurken ekstra iş yapmak.
- Diğer metotlardan **iki farkı**: geri dönüş değeri yoktur (void yazılmaz), ismi class ismiyle aynı olmak zorundadır.
- Overload edilebilir. İstenilen anda çağrılamaz, nesne oluşurken otomatik çalışır. `new` ile çağrılmadan Heap'te nesne üretilmez.

**Constructor Örneği**
```java
public class Ogrenci {

    private int ogrenciNumarasi;
    private String ogrenciAdi;
    private int ogrenciYas;

    public Ogrenci() {
        // Default değerler atama
        this.ogrenciNumarasi = 0;
        this.ogrenciAdi = "Bilinmiyor";
        this.ogrenciYas = 0;
    }

    public Ogrenci(int ogrenciNumarasi, String ogrenciAdi, int ogrenciYas) {
        this.ogrenciNumarasi = ogrenciNumarasi;
        this.ogrenciAdi = ogrenciAdi;
        this.ogrenciYas = ogrenciYas;
    }

    public int getOgrenciNumarasi() {
        return ogrenciNumarasi;
    }

    public String getOgrenciAdi() {
        return ogrenciAdi;
    }

    public int getOgrenciYas() {
        return ogrenciYas;
    }

    public void ogrenciBilgileriniYazdir() {
        System.out.println("Öğrenci Numarası: " + ogrenciNumarasi);
        System.out.println("Öğrenci Adı: " + ogrenciAdi);
        System.out.println("Öğrenci Yaşı: " + ogrenciYas);
    }

    public static void main(String[] args) {
        // Parametresiz yapıcı ile nesne oluşturma
        Ogrenci ogrenci1 = new Ogrenci();
        ogrenci1.ogrenciBilgileriniYazdir();

        Ogrenci ogrenci2 = new Ogrenci(12345, "Ali Veli", 20);
        ogrenci2.ogrenciBilgileriniYazdir();
    }
}
```

---

## Hafta 3.1

### Method Overloading – toplama

Önce tek metot:
```java
public class Main {

    public static void toplama(int a,int b,int c) {
        System.out.println("Toplamları: " + (a+b+c));
    }
    public static void main(String[] args) {
        toplama(3,4,5);
    }
}
```
Çıktı: `Toplamları: 12`

Overload edilmiş hali (aynı isim, farklı parametre sayısı):
```java
public class Main {

    public static void toplama(int a,int b,int c) {
        System.out.println("Toplamları: " + (a+b+c));
    }
    public static void toplama(int a,int b) {
        System.out.println("Toplamları: " + (a+b));
    }
    public static void toplama(int a,int b,int c ,int d) {
        System.out.println("Toplamları: " + (a+b+c+d));
    }
    public static void main(String[] args) {
        toplama(3,4,5);
        toplama(10,20);
        toplama(10,20,30,40);
    }
}
```
Çıktı:
```
Toplamları: 12
Toplamları: 30
Toplamları: 100
```

### Method Overloading – skorHesapla

Önce tek metot:
```java
public class Main {

    public static void skorHesapla(String name,int score) {
        System.out.println(name + " isimli oyuncunun puanı: " + score);
    }
    public static void main(String[] args) {
        skorHesapla("Murat",3000);
    }
}
```
Çıktı: `Murat isimli oyuncunun puanı: 3000`

Overload edilmiş hali (farklı parametre tipi/sayısı):
```java
public class Main {

    public static void skorHesapla(String name,int score) {
        System.out.println(name + " isimli oyuncunun puanı: " + score);
    }
    public static void skorHesapla(int score) {
        System.out.println("İsimsiz oyuncunun puanı: " + score);
    }
    public static void main(String[] args) {
        skorHesapla("Murat",3000);
        skorHesapla(1000);
    }
}
```
Çıktı:
```
Murat isimli oyuncunun puanı: 3000
İsimsiz oyuncunun puanı: 1000
```

### Array

```java
public class Main {
    public static void main(String[] args) {
      int[] arr1 = {10, 20, 30, 40, 50};
      int[] arr2 = new int[5];

      arr2[0]=1;
      arr2[1]=2;
      arr2[2]=3;
      arr2[3]=4;
      arr2[4]=5;

      System.out.println("Arr2'nin birinci elemanı: " + arr2[0]);
      System.out.println("Arr1'nin ikinci elemanı: " + arr1[1]);
    }
}
```
Çıktı:
```
Arr2'nin birinci elemanı: 1
Arr1'nin ikinci elemanı: 20
```

### ArrayList

```java
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
      ArrayList<String> marvel = new ArrayList<String>();

      marvel.add("Iron Man");
      marvel.add("Dr. Strange");
      marvel.add("Thor");
      marvel.add("Captain America");
      marvel.add("Hulk");

      for (int i=0; i<marvel.size(); i++){
        System.out.println("Marvel members: "+marvel.get(i));
      }
    }
}
```
Çıktı:
```
Marvel members: Iron Man
Marvel members: Dr. Strange
Marvel members: Thor
Marvel members: Captain America
Marvel members: Hulk
```

`remove` ile:
```java
      marvel.remove("Hulk");   // değere göre siler
      marvel.remove(2);        // indekse göre siler (Thor)
```
Çıktı:
```
Marvel members: Iron Man
Marvel members: Dr. Strange
Marvel members: Captain America
```

### Inheritance (Kalıtım)

`Employee.java`
```java
public class Employee {

  private String name;
  private String department;
  private int salary;

  public Employee(String name, String department, int salary) {
    this.name = name;
    this.department = department;
    this.salary = salary;
  }

  public void showInfos(){
    System.out.println("BİLGİLER: ");
    System.out.println("Isim: " + this.name);
    System.out.println("Departman: "+ this.department);
    System.out.println("Maaş: "+ this.salary);
  }
}
```

`Manager.java`
```java
public class Manager extends Employee {
  private int num_of_employees;

  public Manager(String name, String department, int salary, int num_of_employees){

  super(name, department, salary);
  this.num_of_employees = num_of_employees;

}
  public void riseSalary(int amount){
    System.out.println ("Çalışanlara" + amount + "tl zam verildi.");
  }

  }
```

`Main.java`
```java
public class Main {
    public static void main(String[] args) {
      /*Employee employee = new Employee("Damla Mengüş","Yazılım",5000);
      employee.showInfos();*/

      Manager manager = new Manager("Damla Mengüş","Yazılım",5000, 100);
      manager.showInfos();
      manager.raiseSlary(500);
    }
}
```

> ⚠️ Not: Slaytta `manager.raiseSlary(500);` yazım hatası var, metot adı `riseSalary`. Bu haliyle derlenmez; `manager.riseSalary(500);` olmalı.

### Override

`Manager.java`
```java
public class Manager extends Employee {
  private int num_of_employees;

  public Manager(String name, String department, int salary, int num_of_employees){

  super(name, department, salary);
  this.num_of_employees = num_of_employees;

}
  public void riseSalary(int amount){
    System.out.println ("Çalışanlara" + amount + "tl zam verildi.");
  }

 /* @Override
  public void showInfos(){
    System.out.println("Name: " + getName());
    System.out.println("Department: " + getDepartment());
    System.out.println("Salary: " + getSalary());
    System.out.println("Sorumlu kişi sayısı: " + this.num_of_employees);
  }*/

  @Override
  public void showInfos(){
    super.shoInfos();
    System.out.println("Sorumlu kişi sayısı: " + this.num_of_employees);
  }
}
```

> ⚠️ Not: Slaytta `super.shoInfos();` yazım hatası var (IDE'de de kırmızı), doğrusu `super.showInfos();`. Yorum satırındaki versiyon da Employee'de `getName()` vb. getter olmadığı için derlenmez.

---

## Hafta 4 – İstisna Yönetimi (Exceptions)

- İstisnalar, kod blokları arasında oluşan anormal durumlardır.
- Java'da `try-catch-finally` blokları ile yönetilir.

Sık karşılaşılan hata türleri:

| Hata | Anlamı |
|---|---|
| ArithmeticException | Aritmetik hata, sıfıra bölme gibi |
| ArrayIndexOutOfBoundsException | Dizi indeks sınırı dışı |
| ArrayStoreException | Diziye uymayan tipte değer kaydetme |
| ClassCastException | Uygunsuz class dönüşümü |
| IllegalArgumentException | Uygun olmayan argüman |
| NullPointerException | İlk değer atanmamış nesneyi kullanma |
| IllegalMonitorStateException | Uygun olmayan monitör işlemi |
| IllegalStateException | Sistem uygun durumda değil |
| IOException | Giriş/çıkış hataları |
| NumberFormatException | Uygun olmayan sayı formatı |
| SecurityException | Güvenlik hatası |
| StringIndexOutOfBounds | String sınırı dışı |
| NoSuchMethodException | Metot bulunamadı |

### Soru – Aşağıdaki programın çıktısı ne olur? Tartışınız.

```java
try
{
    int x = 0;
    int y = 5 / x;
}
catch (Exception e)
{
    System.out.println("Exception");
}
catch (ArithmeticException ae)
{
    System.out.println(" Arithmetic Exception");
}
System.out.println("finished");
```

> Hocanın cevabı slaytta yok ("tartışınız").

### Hata Kontrol – Soru 1

> Bir tamsayı dizisinin toplamını bulan `diziTopla(int[] dizi, int boyut)` şeklinde bir metot yazılıyor. Girilen boyut, parametre olarak verilen dizinin boyutundan fazla ise oluşacak istisnayı yakalayarak «Hatalı Boyut Girildi» şeklinde mesaj veriniz.

```java
public class Main {

    public static void main(String[] args) {

        int[] dizi = {1, 2, 3};

        diziTopla(dizi, 5);
    }

    static void diziTopla(int[] dizi, int boyut) {

        int toplam = 0;

        try {
            for (int i = 0; i < boyut; i++) {
                toplam += dizi[i];
            }

            System.out.println("Toplam: " + toplam);
        }
        catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("Hatalı Boyut Girildi");
        }
    }
}
```

Çıktı: `Hatalı Boyut Girildi`

### Hata Kontrol – Soru 2

> String bir dizide numaralar tutulmaktadır: `String s[]={"1" , "6" , "1g", "10", "d"};`
> Bu dizideki biçimi uygun olmayan numaraları bulan ve gösteren bir uygulama tasarlayınız. (İstisna kullanılacaktır.)

```java
public class Main {

    public static void main(String[] args) {

        String[] s = {"1", "6", "1g", "10", "d"};

        soru2(s);
    }

    static void soru2(String[] dizi) {

        for (int i = 0; i < dizi.length; i++) {

            try {
                int sayi = Integer.parseInt(dizi[i]);
            }
            catch (NumberFormatException e) {
                System.out.println("Hatali numara: " + dizi[i]);
            }
        }
    }
}
```

Çıktı:
```
Hatali numara: 1g
Hatali numara: d
```

### Hata Kontrol 3 (ÖDEV)

> - `Ogrenci` sınıfında notlarını tutan bir `ArrayList<Integer>` olsun.
> - `notEkle` metoduyla bu listeye not eklensin. Eklenmek istenen not:
>   - 0'dan küçükse `KucukDegerHatasi` fırlatsın
>   - 100'den büyükse `BuyukDegerHatasi` fırlatsın
> - Kendi özel Exception sınıflarınızı tanımlayarak kodu test edin. 0-100 aralığında olmayan not eklendiğinde hatayı yakalayıp şu mesajları verin:
>   - `KucukDegerHatasi: -5 not olarak eklenemez`
>   - `BuyukDegerHatasi: 125 not olarak eklenemez`

> Hocanın cevabı slaytta yok.

### Soyut Sınıf (Abstract Class)

```java
// Soyut sınıf tanımı
abstract class Sekil {
    // Soyut metot tanımı
    abstract double alanHesapla();

    // Normal metot tanımı
    void bilgiVer() {
        System.out.println("Bu bir şekildir.");
    }
}

// Soyut sınıftan türetilen alt sınıf
class Dikdortgen extends Sekil {
    // Alt sınıfın soyut metodu uygulanıyor
    @Override
    double alanHesapla() {
        System.out.println("Dikdörtgenin alanı hesaplanıyor.");
        return 4.0; // Örnek değer
    }
}

// Soyut sınıftan türetilen başka bir alt sınıf
class Ucgen extends Sekil {
    // Alt sınıfın soyut metodu uygulanıyor
    @Override
    double alanHesapla() {
        System.out.println("Üçgenin alanı hesaplanıyor.");
        return 2.5; // Örnek değer
    }
}

public class Main {
    public static void main(String[] args) {
        // Soyut sınıfın nesnesi oluşturulamaz, ancak alt sınıflarından nesne oluşturabiliriz.
        Sekil dikdortgen = new Dikdortgen();
        Sekil ucgen = new Ucgen();

        // Her iki nesne de ortak olan soyut metodu çağırabilir.
        System.out.println("Dikdörtgen Alanı: " + dikdortgen.alanHesapla());
        System.out.println("Üçgen Alanı: " + ucgen.alanHesapla());

        // Normal metotları çağırabilirler
        dikdortgen.bilgiVer();
        ucgen.bilgiVer();
    }
}
```

Çıktı:
```
Dikdörtgenin alanı hesaplanıyor.
Dikdörtgen Alanı: 4.0
Üçgenin alanı hesaplanıyor.
Üçgen Alanı: 2.5
Bu bir şekildir.
Bu bir şekildir.
```
