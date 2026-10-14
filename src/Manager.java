public class Manager extends Employee {
    private double bonus;

    public Manager() {
    }

    public Manager(String department, String name, double salary, double bonus) {
        super(department, name, salary);
        this.bonus = bonus;
    }

    public double getBonus() {
        return bonus;
    }

    public void setBonus(double bonus) {
        this.bonus = bonus;
    }

    @Override
    public void showInfos() {
        super.showInfos();
        System.out.println("Bonus      : " + bonus);
    }

    @Override
    public void riseSalary(double amount) {
        super.riseSalary(amount);
    }
}
