import org.junit.Before;
import org.junit.Test;

import java.util.ArrayList;

import static org.junit.Assert.assertEquals;

public class WalletTest {
    private Wallet wallet;
    ArrayList<IChargeable> myCards;
    GiftCard currysCard;
    DebitCard rbs;
    DebitCard monzo;
    CreditCard capitalOne;
    CreditCard virgin;

    @Before
    public void before(){
        this.currysCard = new GiftCard(100);
        this.rbs = new DebitCard(298349, "10/25", 210, 837593, 121212);
        this.monzo = new DebitCard(634466, "03/19", 450, 293758, 140404);
        this.capitalOne = new CreditCard(634466, "03/27", 450, 2000.00);
        this.virgin = new CreditCard(928492, "06/30", 450, 1000.00);
        myCards = new ArrayList<>();
        wallet = new Wallet(myCards);
        wallet.addCard(currysCard);
        wallet.addCard(rbs);
        wallet.addCard(monzo);
        wallet.addCard(capitalOne);
        wallet.addCard(virgin);
    }

    @Test
    public void hasCards(){
        assertEquals(5, wallet.getPaymentCards().size());
    }
    @Test
    public void hasSelectedCard(){
        wallet.setSelectedCard(3);
        CreditCard selected = (CreditCard) wallet.getSelectedCard();
        assertEquals(634466, selected.getCardNumber());
    }

    @Test
    public void canChargeWithPercentage(){
        wallet.setSelectedCard(3);
        wallet.pay(100);
        wallet.pay(50);
        CreditCard selected = (CreditCard) wallet.getSelectedCard();
        assertEquals(1835.00, selected.getAvailableCredit(), 0.0);
    }

    @Test
    public void canGetLogs(){
        wallet.setSelectedCard(1);
        wallet.pay(100);
        wallet.pay(50);
        DebitCard selected = (DebitCard) wallet.getSelectedCard();
        assertEquals("[100.0, 50.0]", selected.getTransactionList().toString());
    }
}
