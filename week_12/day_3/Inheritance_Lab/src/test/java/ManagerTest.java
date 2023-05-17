import management.Manager;
import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class ManagerTest {

    Manager manager;

    @Before
    public void before() {
        manager = new Manager("Johnny Boy", "AB9395492", 50000.00, "HR");
    }

    @Test
    public void testGetName() {
        assertEquals("Johnny Boy", manager.getName());
    }
    @Test
    public void testNameCantBeNull() {
        manager.nameChange(null);
        assertEquals("Johnny Boy", manager.getName());
    }
    @Test
    public void testNameChange() {
        manager.nameChange("Yooooo");
        assertEquals("Yooooo", manager.getName());
    }
    @Test
    public void testGetDeptName() {
        assertEquals("HR", manager.getDeptName());
    }
    @Test
    public void testGetNiNumber() {
        assertEquals("AB9395492", manager.getNiNumber());
    }
    @Test
    public void testGetSalary() {
        assertEquals(50000.00, manager.getSalary(), 0.00);
    }
    @Test
    public void testRaiseSalary() {
        manager.raiseSalary(10000.50);
        assertEquals(60000.50, manager.getSalary(), 0.00);
    }
    @Test
    public void testCantRaiseSalary() {
        manager.raiseSalary(-10292394.50);
        assertEquals(50000.00, manager.getSalary(), 0.00);
    }
    @Test
    public void testPayBonus() {
        assertEquals(500.00, manager.payBonus(), 0.00);
    }

}
