public class Computer implements IConnectable{
    private String name;
    private String make;
    private String model;

    public Computer(String name, String make, String model) {
        this.name = name;
        this.make = make;
        this.model = model;
    }

    public String getName() {
        return name;
    }

    public String getMake() {
        return make;
    }

    public String getModel() {
        return model;
    }

    @Override
    public String getStatus() {
        return "I'm connected to " + this.name;
    }
}
