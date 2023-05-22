import java.util.ArrayList;

public class Wallet {
    ArrayList<IChargeable> paymentCards;
    IChargeable selectedCard;

    public Wallet(ArrayList<IChargeable> paymentCards) {
        this.paymentCards = paymentCards;
    }

    public void addCard (IChargeable card){
        this.paymentCards.add(card);
    }

    public void setSelectedCard(int index) {
        this.selectedCard = paymentCards.get(index);
    }

    public void pay (double amount){
        selectedCard.charge(amount);
    }

    public ArrayList<IChargeable> getPaymentCards() {
        return paymentCards;
    }

    public IChargeable getSelectedCard() {
        return selectedCard;
    }
}
