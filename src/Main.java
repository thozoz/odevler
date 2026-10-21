public class Main {

    public static void gecersizNumaralariGoster(String[] dizi) {
        System.out.println("Biçimi uygun olmayan numaralar:");

        for (String eleman : dizi) {
            try {
                Integer.parseInt(eleman);
            } catch (NumberFormatException error) {
                System.out.println("- " + eleman);
            }
        }
    }

    public static void main(String[] args) {
        String[] dizi = {"1", "6", "1g", "10", "d"};
        gecersizNumaralariGoster(dizi);
    }
}
