//soruda istenen maaş hesaplama işlemi için interface tanımlıyoruz
interface MaasHesaplanabilir {
    double maasHesapla(); //tüm çalışan sınıflarının uygulayacağı maaş hesaplama metodu
}

//ortak çalışan özelliklerini tutacak abstract sınıf
abstract class Calisan implements MaasHesaplanabilir {

    String isim; //çalışanın ismi
    int id; //çalışanın id numarası

    public Calisan(String isim, int id) {
        this.isim = isim; //gelen ismi sınıfın değişkenine atıyoruz
        this.id = id; //gelen id yi sınıfın değişkenine atıyoruz
    }

    //her çalışan kendi bilgilerini farklı yazdıracağı için abstract metot olarak bırakıyoruz
    public abstract void bilgileriYazdir();

}

//tam zamanlı çalışan sınıfı Calisan dan miras alır
class TamZamanliCalisan extends Calisan {

    double aylikMaas; //sabit aylık maaş değişkeni

    public TamZamanliCalisan(String isim, int id, double aylikMaas) {
        super(isim, id); //üst sınıf olan Calisan a isim ve id gönderiyoruz
        this.aylikMaas = aylikMaas; //aylık maaş değerini atıyoruz
    }

    @Override
    public double maasHesapla() {
        return aylikMaas; //tam zamanlı sabit maaş aldığı için direkt aylikMaas ı döndürüyoruz
    }

    @Override
    public void bilgileriYazdir() {
        System.out.println("Çalışan Türü: Tam Zamanlı Çalışan");
        System.out.println("İsim: " + isim);
        System.out.println("ID: " + id);
        System.out.println("Maaş: " + maasHesapla());
    }

}

//yarı zamanlı çalışan sınıfı Calisan dan miras alır
class YariZamanliCalisan extends Calisan {

    double saatlikUcret; //saatlik aldığı ücret
    int calistigiSaat; //toplam çalıştığı saat sayısı

    public YariZamanliCalisan(String isim, int id, double saatlikUcret, int calistigiSaat) {
        super(isim, id); //üst sınıf olan Calisan a isim ve id gönderiyoruz
        this.saatlikUcret = saatlikUcret;
        this.calistigiSaat = calistigiSaat;
    }

    @Override
    public double maasHesapla() {
        return saatlikUcret * calistigiSaat; //saatlik ücret ile çalışılan saati çarpıp maaşı buluyoruz
    }

    @Override
    public void bilgileriYazdir() {
        System.out.println("Çalışan Türü: Yarı Zamanlı Çalışan");
        System.out.println("İsim: " + isim);
        System.out.println("ID: " + id);
        System.out.println("Saatlik Ücret: " + saatlikUcret);
        System.out.println("Çalıştığı Saat: " + calistigiSaat);
        System.out.println("Maaş: " + maasHesapla());
    }

}

//serbest çalışan sınıfı Calisan dan miras alır
class SerbestCalisan extends Calisan {

    double projeBasiUcret; //proje başına aldığı ücret
    int tamamlananProjeSayisi; //tamamladığı toplam proje sayısı

    public SerbestCalisan(String isim, int id, double projeBasiUcret, int tamamlananProjeSayisi) {
        super(isim, id); //üst sınıf olan Calisan a isim ve id gönderiyoruz
        this.projeBasiUcret = projeBasiUcret;
        this.tamamlananProjeSayisi = tamamlananProjeSayisi;
    }

    @Override
    public double maasHesapla() {
        return projeBasiUcret * tamamlananProjeSayisi; //proje başı ücretle proje sayısını çarpıp maaşı hesaplıyoruz
    }

    @Override
    public void bilgileriYazdir() {
        System.out.println("Çalışan Türü: Serbest Çalışan");
        System.out.println("İsim: " + isim);
        System.out.println("ID: " + id);
        System.out.println("Proje Başı Ücret: " + projeBasiUcret);
        System.out.println("Tamamlanan Proje Sayısı: " + tamamlananProjeSayisi);
        System.out.println("Maaş: " + maasHesapla());
    }

}

public class soru {
    public static void main(String[] args) {

        //tüm çalışan türlerini tutmak için Calisan tipinde dizi oluşturuyoruz
        Calisan[] calisanlar = new Calisan[3];

        //dizinin elemanlarına farklı çalışan türlerinden nesneler oluşturup koyuyoruz
        calisanlar[0] = new TamZamanliCalisan("Ahmet Yılmaz", 101, 25000);
        calisanlar[1] = new YariZamanliCalisan("Ayşe Demir", 102, 200, 80);
        calisanlar[2] = new SerbestCalisan("Mehmet Kaya", 103, 5000, 4);

        double toplamMaasGideri = 0; //sistemin toplam maaş giderini tutacak değişken

        //döngü ile dizideki bütün çalışanları gezip bilgilerini yazdırıyoruz
        for (int i = 0; i < calisanlar.length; i++) {
            calisanlar[i].bilgileriYazdir(); //çalışanın bilgilerini ekrana yazdırma
            toplamMaasGideri += calisanlar[i].maasHesapla(); //her çalışanın maaşını toplam gidere ekliyoruz
        }

        //en son sistemin toplam maaş giderini ekrana yazdırıyoruz
        System.out.println("Toplam Maaş Gideri: " + toplamMaasGideri);

    }
}
