import org.junit.Before;
import org.junit.Test;
import techStaff.Developer;

import static org.junit.Assert.assertEquals;

public class DeveloperTest {

    Developer developer;

    @Before
    public void before() {
        developer = new Developer("Bob the Dev", "AB9395492", 50000.00);
    }

    @Test
    public void testGetName() {
        assertEquals("Bob the Dev", developer.getName());
    }
    @Test
    public void testGetNiNumber() {
        assertEquals("AB9395492", developer.getNiNumber());
    }
    @Test
    public void testGetSalary() {
        assertEquals(50000.00, developer.getSalary(), 0.00);
    }
    @Test
    public void testRaiseSalary() {
        developer.raiseSalary(10000.50);
        assertEquals(60000.50, developer.getSalary(), 0.00);
    }

    @Test
    public void testCantRaiseSalary() {
        developer.raiseSalary(-10292394.50);
        assertEquals(50000.00, developer.getSalary(), 0.00);
    }
    @Test
    public void testPayBonus() {
        assertEquals(500.00, developer.payBonus(), 0.00);
    }

}
