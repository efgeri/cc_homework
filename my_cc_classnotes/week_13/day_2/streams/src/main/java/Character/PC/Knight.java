package Character.PC;

import Inventory.Armor;
import Inventory.Treasure;
import Inventory.Weapon;
import Character.IAttack;

import java.util.ArrayList;

public class Knight extends PC implements IAttack{
    private Weapon weapon;
    private Armor armor;

    public Knight(int HP, int defence, String name, Weapon weapon) {
        super (HP, defence, name);
        this.weapon = weapon;
    }

    public void attack(Character target){

    }
    public void equipWeapon(Weapon weapon){
        this.weapon = weapon;
    }
    public void equipArmor(Armor armor){
        this.armor = armor;
        int newDefence = this.getDefence() + this.armor.getDefense();
        this.setDefence(newDefence);
    }
}
