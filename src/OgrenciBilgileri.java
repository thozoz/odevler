public class OgrenciBilgileri {

    private int ogrenciNumarasi;
    private String adi;
    private String tc;
    private int yas;

    public OgrenciBilgileri() {
    }

    public OgrenciBilgileri(int ogrenciNumarasi, String adi, String tc, int yas) {
        this.ogrenciNumarasi = ogrenciNumarasi;
        this.adi = adi;
        this.tc = tc;
        this.yas = yas;
    }

    public int getOgrenciNumarasi() {
        return ogrenciNumarasi;
    }

    public void setOgrenciNumarasi(int ogrenciNumarasi) {
        this.ogrenciNumarasi = ogrenciNumarasi;
    }

    public String getAdi() {
        return adi;
    }

    public void setAdi(String adi) {
        this.adi = adi;
    }

    public String getTc() {
        return tc;
    }

    public void setTc(String tc) {
        this.tc = tc;
    }

    public int getYas() {
        return yas;
    }

    public void setYas(int yas) {
        this.yas = yas;
    }
}
