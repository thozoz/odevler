public class soru1 {
    public static void main(String[] args) {

        int i = 1; // 1den 50ye kadar oldugundan 1 ile başlatıyoruz i yi

        //tek ve çift toplamlarını tutacak değişkenler
        int cifttoplam = 0;
        int tektoplam = 0;

        while (i <= 50) { // 1 den 50ye kadar oldugundan 50 dahil, i değişkeni 50 sayısını geçene kadar
                          // döngü çalışacak

            if (i % 2 == 0) { // 2 ye bölümünün kalanı 0 olan sayı çift sayıdır
                cifttoplam += i; //çift sayılar cifttoplam değişkenine toplanır
            }

            else { // 2 ye bölümünün kalanı 0 değilse sayı tek sayıdır
                tektoplam += i; //tek sayılar tektoplam değişkenine toplanır
            }
            i++; //döngüde 1 den 50 ye kadar i gitsin diye i yi her döngüde 1 arttırıyoruz

        }

        System.out.println("1'den 50'ye kadar olan bütün sayıların toplamı: " + (tektoplam + cifttoplam)); //çift ve teklerin toplamı genel toplamı verir
        System.out.println("1'den 50'ye kadar olan tek sayıların toplamı: " + tektoplam); //tek sayıların toplamını yazdırma
        System.out.println("1'den 50'ye kadar olan çift sayıların toplamı: " + cifttoplam); //çift sayıların toplamını yazdırma



        int sayi = 12345; //7 rakamını arayacağımız sayı

        int b1 = sayi % 10;              // 5 rakamını alırız (12345 % 10 = 5)
        int b2 = (sayi / 10) % 10;       // 4 rakamını alırız (12345/10 = 1234, 1234 % 10 = 4)
        int b3 = (sayi / 100) % 10;      // 3 rakamını alırız (12345/100 = 123, 123 % 10 = 3)
        int b4 = (sayi / 1000) % 10;     // 2 rakamını alırız (12345/1000 = 12, 12 % 10 = 2)
        int b5 = (sayi / 10000) % 10;    // 1 rakamını alırız (12345/10000 = 1, 1 % 10 = 1)  (%10 gerek yok ama kalanıyla uyumlu olsun diye)

        if (b1 == 7 || b2 == 7 || b3 == 7 || b4 == 7 || b5 == 7) { //her basamağını or ile 7 var mı diye bakıyoruz, bi tane basamagının rakamı bile 7 ye eşitse 7 rakamı vardır yazdırıyor
            System.out.println("12345 sayısında 7 rakamı vardır.");
        } else {
            System.out.println("12345 sayısında 7 rakamı yoktur."); //7 rakamı bulunamazsa yoktur yazdırır
        }


    }

}
