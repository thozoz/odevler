package uygulama1;

import java.util.Scanner;

public class Ornek4 {

	public static void main(String[] args) {
		Scanner giriş=new Scanner(System.in);
		
		System.out.println("Birinci sayıyı giriniz:");
		int sayı1=giriş.nextInt();
		
		System.out.println("İkinci sayıyı giriniz:");
		int sayı2=giriş.nextInt();
		
		System.out.println("Girilen sayıların ebobu:"+ebob(sayı1,sayı2));
		giriş.close();
	}

	private static int ebob(int sayı1, int sayı2) {
		int x=sayı1;
		int y=sayı2;
		int r;
		
		while(y!=0) {
			r=x%y;
			x=y;
			y=r;
		}
		return x;
	}

}
