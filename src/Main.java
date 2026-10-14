public class Main {
    public static void toplama(int a, int b) {
        System.out.println("Toplamları: " + (a + b));
    }

    public static void toplama(int a, int b, int c) {
        System.out.println("Toplamları: " + (a + b + c));
    }

    public static void toplama(int a, int b, int c, int d) {
        System.out.println("Toplamları: " + (a + b + c + d));
    }

    public static void main(String[] args) {
        toplama(5, 10);
        toplama(5, 10, 15);
        toplama(5, 10, 15, 20);
    }
}
