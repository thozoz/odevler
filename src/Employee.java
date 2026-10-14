public class Employee {
    private String department;
    private String name;
    private double salary;

    public Employee() {
    }

    public Employee(String department, String name, double salary) {
        this.department = department;
        this.name = name;
        this.salary = salary;
    }


    public void showInfos() {
        System.out.println("Department : " + department);
        System.out.println("Name        : " + name);
        System.out.println("Salary       : " + salary);
    }
}
