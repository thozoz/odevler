public class OgrenciIslemleri {

    public void ogrenciKaydet(OgrenciBilgileri ogrenci) {
        System.out.println("Ogrenci kaydi yapıldı: " + ogrenci.getAdi());
    }

    public void ogrenciBilgileriniGoster(OgrenciBilgileri ogrenci) {
        System.out.println("Numarasi : " + ogrenci.getOgrenciNumarasi());
        System.out.println("Adi      : " + ogrenci.getAdi());
        System.out.println("TC       : " + ogrenci.getTc());
        System.out.println("Yas      : " + ogrenci.getYas());
    }
}
