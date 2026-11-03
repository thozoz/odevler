// Mekan sınıfı (public YAZMA)
class Mekan {
    String ad;
    String konum;
    public Mekan(String ad,String konum){
        this.ad=ad;
        this.konum=konum;
    }

    public void mekanBilgisi(){
        System.out.println("Mekan adı: "+this.ad);
        System.out.println("Mekan konum: "+this.konum);
    }
}

// Restoran sınıfı (public YAZMA)
class Restoran extends Mekan {
    String menu;
    public Restoran(String ad,String konum, String menu){
        super(ad,konum);
        this.menu=menu;
    }
    @Override
    public void mekanBilgisi(){
        System.out.println("Mekan adı: "+this.ad);
        System.out.println("Mekan konum: "+this.konum);
        //or super.mekanBilgisi(); works the same
        System.out.println("Mekan menu: "+this.menu);
    }
}

// Main sınıfı (sadece bu public olabilir)
public class Main {
    public static void main(String[] args) {
        Restoran rest= new Restoran("Lezzet durağı","İstanbul","Turk Mutfağı");
        rest.mekanBilgisi();
    }
}
