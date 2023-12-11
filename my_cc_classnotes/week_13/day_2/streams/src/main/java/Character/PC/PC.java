package Character.PC;

import Inventory.Treasure;

import java.util.ArrayList;
import Character.Characters;

public abstract class PC extends Characters {
    private ArrayList<Treasure> treasures;

    public PC(int HP, int defence, String name) {
        super(HP, defence, name);
        this.treasures = new ArrayList<>();
    }

    public void setTreasures(ArrayList<Treasure> treasures) {
        this.treasures = treasures;
    }
}
