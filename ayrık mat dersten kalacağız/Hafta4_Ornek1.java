package uygulama1;

import java.util.Random;

public class Ornek1 {

	public static void main(String[] args) {
		Random sayıüretici=new Random();
		int []dizi=new int[10];
		for (int i = 0; i < dizi.length; i++) {
			dizi[i]=sayıüretici.nextInt(100);
			System.out.print(dizi[i]+"\t");
		}
		System.out.println();
		int eb=maximum_bul(dizi);
		System.out.println("Dizinin en büyük sayısı:"+eb);

	}

	private static int maximum_bul(int[] dizi) {
		int max=dizi[dizi.length-1];
		for (int i = dizi.length-2; i >=0; i--) {
			if (max<dizi[i]) {
				max=dizi[i];
			}
			
			
		}
		return max;
	}

}
