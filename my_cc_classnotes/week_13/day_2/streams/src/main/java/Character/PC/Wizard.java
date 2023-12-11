package Character.PC;

import Inventory.Spell;
import Inventory.Treasure;
import NPC.Familiar;
import Character.IAttack;

import java.util.ArrayList;
import java.util.HashMap;

public class Wizard extends PC implements IAttack {
    private Familiar familiar;
    private ArrayList<Spell> spells;
    private Spell selectedSpell;

    public Wizard (int HP, int defence, String name, Familiar familiar, ArrayList<Spell> spells) {
        super(HP, defence, name);
        this.familiar = familiar;
        this.spells = spells;
    }

    public void attack(Character target){

    }

    public Spell getSelectedSpell() {
        return selectedSpell;
    }

    public void setSelectedSpell(Spell selectedSpell) {
        this.selectedSpell = selectedSpell;
    }

    public void castSpell(){

    }

    public void commandFamiliar(){

    }
}
