import javax.swing.plaf.synth.SynthTextAreaUI;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Musteri musteri1=new Musteri();
        Musteri musteri2=new Musteri();

        musteri1=musteri2;

        musteri1.Add();
        musteri1.Remove();
        musteri1.Update();


    }
}

