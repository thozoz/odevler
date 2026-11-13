package uygulama1;

public class Ornek3 {

	public static void main(String[] args) {
		int dizi[]= {1,2,3,4,5,6,7,8,9,10,12,13,15,16,18,19,20,22};
		for (int i = 0; i < dizi.length; i++) {
			System.out.print(dizi[i]+"\t");
		}
		System.out.println();
		int aranan=25;
		int konum=ikili_arama(aranan,dizi);
		if (konum!=-1) {
			System.out.println("Aranan eleman "+ konum+" indisindedir.");
		} else {
			System.out.println("Aranan eleman dizide yoktur....");	
		}
	}

	private static int ikili_arama(int aranan, int[] dizi) {
		int i=0;
		int j=dizi.length;
		while(i<j) {
			int m=(int) Math.floor(((i+j)/2));
			if (aranan>dizi[m]) {
				i=m+1;
			}else {
				j=m;
			}
		}
		if(aranan==dizi[i-1]) {
			return i;
		}
		else {
			return -1;
		}
		
	}}
