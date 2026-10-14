public class OgrenciIslemleri {

    public void ogrenciKaydet(OgrenciBilgileri ogrenci) {
        System.out.println("Ogrenci kaydi yapıldı: " + ogrenci.adi);
    }

    public void ogrenciBilgileriniGoster(OgrenciBilgileri ogrenci) {
        System.out.println("Numarasi : " + ogrenci.ogrenciNumarasi);
        System.out.println("Adi      : " + ogrenci.adi);
        System.out.println("TC       : " + ogrenci.tc);
        System.out.println("Yas      : " + ogrenci.yas);
    }
}
