package NPC.Foes;
import Character.Characters;
import Character.IAttack;
public class Foe extends Characters implements IAttack{
    int attack;
    public Foe(int HP, int defence, String name, int attack) {
        super(HP, defence, name);
        this.attack = attack;
    }

    public void attack(Character target){

    }
}
