import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class PlanetTest {
    Planet mars;

    @Before
    public void before(){
        mars = new Planet("Mars", 937659);
    }

    @Test
    public void hasName(){
        assertEquals("Mars", mars.getName());
    }

    @Test
    public void hasSize(){
        assertEquals(937659, mars.getSize());
    }

}
