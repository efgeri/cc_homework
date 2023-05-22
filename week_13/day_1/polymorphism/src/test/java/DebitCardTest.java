import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class DebitCardTest {

    private DebitCard debitCard;

    @Before
    public void before(){
        debitCard = new DebitCard(985945984, "10/23", 270, 72833223,122446);
    }

    @Test
    public void canGetLogs(){
        debitCard.charge(100);
        debitCard.charge(50);
        assertEquals("[100.0, 50.0]", debitCard.getTransactionList().toString());
    }
}
