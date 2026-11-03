import java.util.ArrayList; //notları tutacagımız dinamik liste için arraylist i ekliyoruz

//soruda istenen 0 dan küçük degerler için özel hata sınıfı
class KucukDegerHatasi extends Exception {
    public KucukDegerHatasi(String mesaj) {
        super(mesaj); //üst sınıf olan Exception a hata mesajını gönderiyoruz
    }
}

//soruda istenen 100 den büyük degerler için özel hata sınıfı
class BuyukDegerHatasi extends Exception {
    public BuyukDegerHatasi(String mesaj) {
        super(mesaj); //üst sınıf olan Exception a hata mesajını gönderiyoruz
    }
}

class Ogrenci {

    private ArrayList<Integer> notlar; //ögrencinin notlarını tutacak liste

    public Ogrenci() {
        this.notlar = new ArrayList<>(); //ögrenci olusturuldugunda boş not listesini başlatıyoruz
    }

    //ögrenciye not ekleme metodu
    public void notEkle(int not) throws KucukDegerHatasi, BuyukDegerHatasi { //fırlatılabilecek hataları belirtiyoruz

        if (not < 0) { //eger girilen not 0 dan küçükse
            throw new KucukDegerHatasi(not + " not olarak eklenemez"); //küçük değer hatası fırlatıyoruz
        } 
        else if (not > 100) { //eger girilen not 100 den büyükse
            throw new BuyukDegerHatasi(not + " not olarak eklenemez"); //büyük değer hatası fırlatıyoruz
        }

        notlar.add(not); //not 0 ile 100 arasındaysa sorun yoktur listeye ekleriz
        System.out.println("Not başarıyla eklendi: " + not); //eklendiğini görmek için yazdırıyoruz

    }

    public ArrayList<Integer> getNotlar() {
        return notlar; //notları listeden alıp görebilmek için listeyi döndürüyoruz
    }

}

public class soru {
    public static void main(String[] args) {

        Ogrenci ogrenci = new Ogrenci(); //ögrenci nesnesini oluşturuyoruz


        //ilk başta geçerli normal bir not eklemeyi deniyoruz
        try {
            ogrenci.notEkle(75); //geçerli not ekliyoruz hata vermemesi lazım
        } catch (KucukDegerHatasi e) {
            System.out.println("KucukDegerHatasi: " + e.getMessage()); //hata olursa yakalayıp ekrana yazdırır
        } catch (BuyukDegerHatasi e) {
            System.out.println("BuyukDegerHatasi: " + e.getMessage()); //hata olursa yakalayıp ekrana yazdırır
        }


        //0 dan küçük not eklemeyi deniyoruz hata vermesi lazım
        try {
            ogrenci.notEkle(-5); //0 dan küçük sayı veriyoruz hata vermeli
        } catch (KucukDegerHatasi e) {
            System.out.println("KucukDegerHatasi: " + e.getMessage()); //küçük değer hatasını yakalayıp ekrana yazdırıyoruz
        } catch (BuyukDegerHatasi e) {
            System.out.println("BuyukDegerHatasi: " + e.getMessage());
        }


        //100 den büyük not eklemeyi deniyoruz hata vermesi lazım
        try {
            ogrenci.notEkle(125); //100 den büyük sayı veriyoruz hata vermeli
        } catch (KucukDegerHatasi e) {
            System.out.println("KucukDegerHatasi: " + e.getMessage());
        } catch (BuyukDegerHatasi e) {
            System.out.println("BuyukDegerHatasi: " + e.getMessage()); //büyük değer hatasını yakalayıp ekrana yazdırıyoruz
        }


        //kontrol amaçlı geçerli bir not daha ekliyoruz
        try {
            ogrenci.notEkle(90); //normal not ekleme
        } catch (KucukDegerHatasi e) {
            System.out.println("KucukDegerHatasi: " + e.getMessage());
        } catch (BuyukDegerHatasi e) {
            System.out.println("BuyukDegerHatasi: " + e.getMessage());
        }


        System.out.println("Öğrencinin notları: " + ogrenci.getNotlar()); //en son listeye eklenen geçerli notları ekrana yazdırma

    }
}
