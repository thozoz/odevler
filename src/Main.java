public class Main {
    public static void main(String[] args) {

        OgrenciBilgileri ogrenci1 = new OgrenciBilgileri();
        ogrenci1.ogrenciNumarasi = 101;
        ogrenci1.adi = "Can Satar Sattı";
        ogrenci1.tc = "171425025";
        ogrenci1.yas = 20;


        OgrenciIslemleri ogrenciIslemleri = new OgrenciIslemleri();
        ogrenciIslemleri.ogrenciKaydet(ogrenci1);
        ogrenciIslemleri.ogrenciBilgileriniGoster(ogrenci1);
    }
}
