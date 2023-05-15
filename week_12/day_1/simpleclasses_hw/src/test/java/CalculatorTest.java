import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class CalculatorTest {
    Calculator calculator;
    @Before
    public void before(){
        calculator = new Calculator();
    }

    @Test
    public void canAdd(){
        assertEquals(32.00, calculator.add(25.00, 7.00), 0.0);
    }
    @Test
    public void canSubtract(){
        assertEquals(18.00, calculator.subtract(25.00, 7.00), 0.0);
    }
    @Test
    public void canMultiply(){
        assertEquals(70.00, calculator.multiply(10.00, 7.00), 0.0);
    }
    @Test
    public void canDivide(){
        assertEquals(6.00, calculator.divide(36.00, 6.00), 0.0);
    }

}

