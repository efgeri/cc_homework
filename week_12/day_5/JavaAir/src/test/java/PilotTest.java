import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class PilotTest {
    Pilot pilot;

    @Before
    public void before(){
        pilot = new Pilot("Maverick", "LOL");
    }
    @Test
    public void canGetName() {
        assertEquals("Maverick", pilot.getName());
    }
    @Test
    public void canGetRank() {
        assertEquals(Rank.CAPTAIN, pilot.getRank());
    }
    @Test
    public void canGetLicence() {
        assertEquals("LOL", pilot.getLicenceNumber());
    }

    @Test
    public void pilotCanFly() {
        assertEquals( "Punch it!", pilot.fly());
    }
}
