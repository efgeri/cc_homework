package staff;

public abstract class Employee {

    String name;
    String niNumber;
    double salary;

    public Employee(String name, String niNumber, double salary) {
        this.name = name;
        this.niNumber = niNumber;
        this.salary = salary;

    }

    public String getName() {
        return this.name;
    }
    public String getNiNumber() {
        return this.niNumber;
    }
    public double getSalary() {
        return this.salary;
    }
    public void raiseSalary(double raise) {
        this.salary += raise;
    }
    public double payBonus() {
        return this.salary * 0.01;
    }


}
