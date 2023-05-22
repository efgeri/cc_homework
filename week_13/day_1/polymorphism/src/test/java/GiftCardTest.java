import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class GiftCardTest {
    private GiftCard giftCard;

    @Before
    public void before(){
        giftCard = new GiftCard(2000.00);
    }

    @Test
    public void canCharge(){
        giftCard.charge(100);
        assertEquals(1900, giftCard.getBalance(), 0.00);
    }
}
