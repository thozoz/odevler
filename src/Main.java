import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner girdi = new Scanner(System.in);

        int ah = 0;
        int sayi;
        int toplam=0;
        while (ah != 5) {
            System.out.print("sayı gir: ");
            sayi = girdi.nextInt();
            toplam+=sayi;
            ah++;

        }
        System.out.print(toplam/5);    }
}

