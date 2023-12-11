import management.Manager;
import org.junit.Before;
import org.junit.Test;
import techStaff.DatabaseAdmin;

import static org.junit.Assert.assertEquals;

public class DatabaseAdminTest {

    DatabaseAdmin databaseadmin;

    @Before
    public void before() {
        databaseadmin = new DatabaseAdmin("Karen the DbLady", "AB9395492", 50000.00);
    }

    @Test
    public void testGetName() {
        assertEquals("Karen the DbLady", databaseadmin.getName());
    }
    @Test
    public void testGetNiNumber() {
        assertEquals("AB9395492", databaseadmin.getNiNumber());
    }
    @Test
    public void testGetSalary() {
        assertEquals(50000.00, databaseadmin.getSalary(), 0.00);
    }
    @Test
    public void testRaiseSalary() {
        databaseadmin.raiseSalary(10000.50);
        assertEquals(60000.50, databaseadmin.getSalary(), 0.00);
    }
    @Test
    public void testPayBonus() {
        assertEquals(500.00, databaseadmin.payBonus(), 0.00);
    }

}
