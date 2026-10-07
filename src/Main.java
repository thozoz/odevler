import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner girdi = new Scanner(System.in);

        int tahmin=15;


        while (true) {
            System.out.print("tahmn et: ");
            int sayi=girdi.nextInt();
            if (sayi>tahmin){
                System.out.print("daha küçük gir \n");
            }
            if(sayi<tahmin){
                System.out.print("daha büyük gir \n");
            }
            if(sayi==tahmin){
                System.out.print("başardın. \n");
                break;
            }



        }





    }
}

