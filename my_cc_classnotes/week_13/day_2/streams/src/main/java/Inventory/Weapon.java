package Inventory;

public class Weapon extends Inventory {

    int damage;
    public Weapon(String name, int damage) {
        super(name);
        this.damage = damage;
    }


}
