import org.junit.Before;
import org.junit.Test;

import java.util.ArrayList;

import static org.junit.Assert.assertEquals;

public class CreditCardTest {

    private CreditCard creditCard;

    @Before
    public void before(){
        creditCard = new CreditCard(985945984, "10/23", 270, 1000.00);
    }

    @Test
    public void canChargeWithPercentage(){
        creditCard.charge(100);
        creditCard.charge(50);
        assertEquals(835.00, creditCard.getAvailableCredit(), 0.00);
    }

    @Test
    public void canGetLogs(){
        creditCard.charge(100);
        creditCard.charge(50);
        assertEquals("[100.0, 50.0]", creditCard.getTransactionList().toString());
    }
}
