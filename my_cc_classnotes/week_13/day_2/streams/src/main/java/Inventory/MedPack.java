package Inventory;

public class MedPack extends Inventory{
    private int heal;

    public MedPack(String name, int heal) {
        super(name);
        this.heal = heal;
    }
}
