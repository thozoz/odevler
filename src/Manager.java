public class Manager {
    private String department;
    private String name;
    private double salary;
    private double bonus;

    public Manager() {
    }

    public Manager(String department, String name, double salary, double bonus) {
        this.department = department;
        this.name = name;
        this.salary = salary;
        this.bonus = bonus;
    }

    public double getBonus() {
        return bonus;
    }

    public void setBonus(double bonus) {
        this.bonus = bonus;
    }

    public void showInfos() {
        System.out.println("Department : " + department);
        System.out.println("Name        : " + name);
        System.out.println("Salary       : " + salary);
        System.out.println("Bonus      : " + bonus);
    }
}
