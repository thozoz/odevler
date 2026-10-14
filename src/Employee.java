public class Employee {
    private String department;
    private String name;
    private double salary;
    private static int numberOfEmployees = 0;

    public Employee() {
        numberOfEmployees++;
    }

    public Employee(String department, String name, double salary) {
        this.department = department;
        this.name = name;
        this.salary = salary;
        numberOfEmployees++;
    }

    public static int getNumberOfEmployees() {
        return numberOfEmployees;
    }

    public void riseSalary(double amount) {
        this.salary += amount;
    }


    public void showInfos() {
        System.out.println("Department : " + department);
        System.out.println("Name        : " + name);
        System.out.println("Salary       : " + salary);
    }
}
