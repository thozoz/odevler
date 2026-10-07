import javax.swing.plaf.synth.SynthTextAreaUI;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {


        int art =6;  //5 faktoriel için 6 yazıyo çünkü why not (i=1 den başlıyo)
        int i= 1;
        int carp=1;

        while(art!=i){
            carp=i*carp;

            i++;

        }
        System.out.print(carp);
    }
}

