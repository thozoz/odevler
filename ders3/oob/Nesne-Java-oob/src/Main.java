// Soyut sınıf tanımı:
abstract class Sekil {
    // Soyut metot tanımı:
    abstract double alanHesapla();

    // Normal metot tanımı:
    void bilgiVer() {
        System.out.println("Bu bir şekildir.");
    }
}

// Soyut sınıftan türetilen alt sınıf:
class Dikdortgen extends Sekil {
    // Alt sınıfta soyut metodu uyguluyor
    @Override
    double alanHesapla() {
        System.out.println("Dikdörtgenin alanı hesaplanıyor.");
        return 4.0; // Örnek değer
    }
}

// Soyut sınıftan türetilen başka bir alt sınıf
class Ucgen extends Sekil {
    // Alt sınıfta soyut metodu uyguluyor
    @Override
    double alanHesapla() {
        System.out.println("Üçgenin alanı hesaplanıyor.");
        return 2.5; // Örnek değer
    }
}

public class Main {
    public static void main(String[] args) {
        // Sekil nesnesi oluşturulamaz, soyut sınıf olduğu için
        // Sekil sekil = new Sekil(); // Hata!

        // Alt sınıf nesnesi oluşturulabilir
        Sekil dikdortgen = new Dikdortgen();
        Sekil ucgen = new Ucgen();

        // Normal metot çağrısı
        System.out.println("Dikdörtgen Alanı: " + dikdortgen.alanHesapla());
        System.out.println("Üçgen Alanı: " + ucgen.alanHesapla());

        // Soyut metotlar (override edilmiş)
        dikdortgen.bilgiVer();
        ucgen.bilgiVer();
    }
}
