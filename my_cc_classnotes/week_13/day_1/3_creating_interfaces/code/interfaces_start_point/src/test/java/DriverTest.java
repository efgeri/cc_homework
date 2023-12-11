import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class DriverTest {
    @Test
    public void canDrive(){
        Driver claire = new Driver();
        Car car = new Car ("Mini", "Cooper");
        claire.drive(car, 20);
        assertEquals(20, car.getOdometerReading());
    }
}
