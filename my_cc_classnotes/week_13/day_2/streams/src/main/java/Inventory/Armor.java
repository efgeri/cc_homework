package Inventory;

public class Armor extends Inventory{
    private int defense;
    public Armor(String name, int defense) {
        super(name);
        this.defense = defense;
    }

    public int getDefense() {
        return defense;
    }
}
