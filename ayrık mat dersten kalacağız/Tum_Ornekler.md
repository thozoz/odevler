# Java Örnekleri

## Hafta4_Ornek1.java

```java
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
```

---

## Hafta4_Ornek2.java

```java
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
```

---

## Hafta4_Ornek3.java

```java
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
		if(i<dizi.length && dizi[i]==aranan) {
			return i;
		}
		else {
			return -1;
		}
		
	}}
```

---

## Hafta7_Ornek4.java

```java
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
```
