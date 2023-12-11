package Inventory;

public class Treasure extends Inventory {
    private int gold;
    public Treasure(String name, int gold) {
        super(name);
        this.gold = gold;
    }
}
