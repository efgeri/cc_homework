package Inventory;

public class Spell extends Inventory{
    public int damage;

    public Spell(String name, int damage) {
        super(name);
        this.damage = damage;
    }
}
