import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner girdi = new Scanner(System.in);
        System.out.print("sayı gir: ");
        int sayi = girdi.nextInt();
        int ters = 0;

        while (sayi != 0) {
            int sonRakam = sayi % 10;
            ters = ters * 10 + sonRakam;
            sayi = sayi / 10;
        }

        System.out.print("ters : " + ters);
    }
}

