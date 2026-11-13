package uygulama1;

import java.util.Random;

public class Ornek2 {

	public static void main(String[] args) {
		Random sayıüretici=new Random();
		int []dizi=new int[10];
		for (int i = 0; i < dizi.length; i++) {
			dizi[i]=sayıüretici.nextInt(100);
			System.out.print(dizi[i]+"\t");
		}
		int aranan=23;
		System.out.println();
		int konum=aranan_elemanin_konumunu_bul(aranan,dizi);
		if (konum!=-1) {
			System.out.println("Aranan sayının dizideki indisi:"+konum);
		} else {
			System.out.println("Aranan sayı dizide bulunmamaktadır....");	
		}
	}

	private static int aranan_elemanin_konumunu_bul(int aranan, int[] dizi) {
		int i=0;
		while(i<dizi.length&&aranan!=dizi[i]) {
			i++;
		}
		if(i<dizi.length) {
			return i;
		}else {
			return -1;
		}
		
	}

}
