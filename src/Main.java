public class Main {
    public static void main(String[] args) {

        OgrenciBilgileri ogrenci1 = new OgrenciBilgileri();
        ogrenci1.setOgrenciNumarasi(101);
        ogrenci1.setAdi("Can Satar Sattı");
        ogrenci1.setTc("171425025");
        ogrenci1.setYas(20);


        OgrenciIslemleri ogrenciIslemleri = new OgrenciIslemleri();
        ogrenciIslemleri.ogrenciKaydet(ogrenci1);
        ogrenciIslemleri.ogrenciBilgileriniGoster(ogrenci1);
    }
}
