import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class BearTest {
    Bear bear;
    @Before
    public void before(){
        bear = new Bear("Baloo", 27, 342.987);
    }

    @Test
    public void hasName(){
        assertEquals("Baloo", bear.getName());
    }
    @Test
    public void hasAge(){
        assertEquals(27, bear.getAge());
    }
    @Test
    public void hasWeight(){
        assertEquals(342.987, bear.getWeight(), 0.0);
    }

    @Test
    public void readyToHibernateIfGreaterThan80(){
        assertEquals(true, bear.readyToHibernate());
    }
    @Test
    public void notReadyToHibernateIfLowerThan80(){
        Bear thinBear = new Bear("Yogi", 23, 67);
        assertEquals(false, thinBear.readyToHibernate());
    }
}
