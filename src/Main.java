public class Main {
    public static void main(String[] args) {
        Employee calisan = new Employee("Yazilim", "Ahmet Yilmaz", 50000);
        Manager mudur = new Manager("Yazilim", "Mehmet Demir", 80000, 15000);

        calisan.riseSalary(5000);
        mudur.riseSalary(10000);

        calisan.showInfos();

        System.out.println();

        mudur.showInfos();

        System.out.println();
        System.out.println("Toplam calisan sayisi: " + Employee.getNumberOfEmployees());
    }
}
