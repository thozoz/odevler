sayi=int(input("Sayi giriniz: "))
a=100


while a<1000: #a değişkenini 100 den 999'a kadar yükselten while döngüsü

    if a%sayi==0: #tam bölünüyorsa kontrolü, bölünürse kalan 0 olur (% kalan verir)
        print(str(a)+" sayısı "+str(sayi)+" sayısına tam bölünür!")

    a=a+1