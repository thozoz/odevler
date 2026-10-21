public class Main {
    public static int diziTopla(int[] dizi, int boyut) {
        int toplam = 0;
        try {
            for (int i = 0; i < boyut; i++) {
                toplam += dizi[i];
            }
        } catch (ArrayIndexOutOfBoundsException error) {
            System.out.println("Hatalı boyut girildi!");
        }
        return toplam;
    }

    public static void main(String[] args) {


        int[] dizi = {1, 2, 3, 4, 5};
        System.out.println();
        System.out.println("Toplam: " + diziTopla(dizi, 3));
        System.out.println("Toplam: " + diziTopla(dizi, 10));
    }
}
