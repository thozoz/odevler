class Tasit {
    String marka;
    int hiz;
    public Tasit(String marka,int hiz){
        this.marka=marka;
        this.hiz=hiz;
    }
    void bilgiVer(){
        System.out.println("Araba markası: "+marka);
        System.out.println("Araba hızı: "+hiz);
    }

}

class Otomobil extends Tasit{
    int kapiSayisi;

    public Otomobil(String marka,int hiz,int kapisayi){
        super(marka,hiz);
        this.kapiSayisi=kapisayi;
    }
    @Override
    void bilgiVer(){
        super.bilgiVer();
        System.out.println("Araba kapı sayısı: "+kapiSayisi);
    }
}

public class Main2 {
    public static void main(String[] args) {
        Otomobil oto=new Otomobil("BMW",200,4);
        oto.bilgiVer();
    }
}
