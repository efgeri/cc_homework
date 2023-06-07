public class Item {

    private String name;
    private double price;
    private boolean bogoFree;

    public Item(String name, double price, boolean bogoFree) {
        this.name = name;
        this.price = price;
        this.bogoFree = bogoFree;
    }

    public String getName() {
        return name;
    }

    public double getPrice() {
        return price;
    }

    public boolean isBogoFree() {
        return bogoFree;
    }
}
