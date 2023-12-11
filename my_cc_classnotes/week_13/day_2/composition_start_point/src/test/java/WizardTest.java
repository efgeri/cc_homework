import static org.junit.Assert.*;

import behaviours.IFlyable;
import org.junit.*;
import wizard_management.beasts.Dragon;
import wizard_management.carpets.MagicCarpet;
import wizard_management.cleaning.Broomstick;
import wizard_management.people.Wizard;


public class WizardTest {
    Dragon dragon;
    Wizard wizard;
    Broomstick broomstick;
    MagicCarpet carpet;

    @Before
    public void before(){
        dragon = new Dragon("Tilly");
        broomstick = new Broomstick("Nimbus", 10);
        wizard = new Wizard("Toby", broomstick);
        carpet = new MagicCarpet("Purple");
    }

    @Test
    public void hasName(){
        assertEquals("Toby", wizard.getName());
    }

    @Test
    public void hasBroomstick(){
        Broomstick ride = (Broomstick)wizard.getRide();
        assertEquals("Nimbus", ride.getBrand());
    }

    @Test
    public void canFly(){
        assertEquals(wizard.fly(),"mounting broom, running, skipping, flying!");
    }

    @Test
    public void canFlyDragon(){
        wizard = new Wizard("Toby", dragon);
        assertEquals("Standing up tall, beating wings, lift off!", wizard.fly());
    }
    @Test
    public void canFlyMagicCarpet(){
        wizard = new Wizard("Toby", carpet);
        assertEquals("Hovering up, straightening out, flying off!", wizard.fly());
    }
    @Test
    public void canSetRide(){
        wizard = new Wizard("Toby", carpet);
        wizard.setRide(broomstick);
        assertEquals("mounting broom, running, skipping, flying!", wizard.fly());
    }


}
