import management.Director;

import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class DirectorTest {

    Director director;

    @Before
    public void before() {
        director = new Director("Aneeqa", "AB9395492", 50000.00, "HR", 1000000.00);
    }

    @Test
    public void testGetName() {
        assertEquals("Aneeqa", director.getName());
    }
    @Test
    public void testGetDeptName() {
        assertEquals("HR", director.getDeptName());
    }
    @Test
    public void testGetNiNumber() {
        assertEquals("AB9395492", director.getNiNumber());
    }
    @Test
    public void testGetSalary() {
        assertEquals(50000.00, director.getSalary(), 0.00);
    }
    @Test
    public void testRaiseSalary() {
        director.raiseSalary(10000.50);
        assertEquals(60000.50, director.getSalary(), 0.00);
    }
    @Test
    public void testCantRaiseSalary() {
        director.raiseSalary(-10292394.50);
        assertEquals(50000.00, director.getSalary(), 0.00);
    }
    @Test
    public void testPayBonus() {
        assertEquals(1000.00, director.payBonus(), 0.00);
    }

    @Test
    public void TestGetBudget() {
        assertEquals(1000000.00, director.getBudget(), 0.00);
    }
}
