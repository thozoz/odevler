public class Main {
    public static void main(String[] args) {
        Employee calisan = new Employee("Yazilim", "Ahmet Yilmaz", 50000);
        calisan.showInfos();

        System.out.println();

        Manager mudur = new Manager("Yazilim", "Mehmet Demir", 80000, 15000);
        mudur.showInfos();
    }
}
