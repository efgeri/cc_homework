import Character.PC.Knight;
import Inventory.Armor;
import Inventory.Weapon;
import org.junit.Before;
import org.junit.Test;

import java.util.ArrayList;

import static org.junit.Assert.assertEquals;

public class KnightTest {
    Knight knight;
    Armor armor;
    Armor armor1;
    Weapon weapon;
    Weapon weapon1;
    @Before
    public void before(){
        weapon = new Weapon("Axe", 20);
        weapon1 = new Weapon("Dagger", 10);
        armor = new Armor("Plate", 8);
        armor1 = new Armor("Leather", 6);
        knight = new Knight(50, 5, "Johnny the Defender", weapon);
    }

    @Test
    public void canEquipArmor(){
        knight.equipArmor(armor1);
        assertEquals(11, knight.getDefence());
    }

}
