import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class WaterBottleTest {
    private WaterBottle waterBottle;

    @Before
    public void before(){
        waterBottle = new WaterBottle();
    }

    @Test
    public void canDrink(){
        waterBottle.drink();
        waterBottle.drink();
        assertEquals(80, waterBottle.getVolume());
    }
    @Test
    public void cantGoBelowZero(){
        waterBottle.drink();
        waterBottle.drink();
        waterBottle.drink();
        waterBottle.drink();
        waterBottle.drink();
        waterBottle.drink();
        waterBottle.drink();
        waterBottle.drink();
        waterBottle.drink();
        waterBottle.drink();
        waterBottle.drink();
        assertEquals(0, waterBottle.getVolume());
    }
    @Test
    public void canEmpty(){
        waterBottle.empty();
        assertEquals(0, waterBottle.getVolume());
    }
    @Test
    public void canFill(){
        waterBottle.empty();
        waterBottle.fill();
        assertEquals(100, waterBottle.getVolume());
    }
}
