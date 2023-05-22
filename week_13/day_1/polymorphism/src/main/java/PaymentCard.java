import java.util.ArrayList;

public abstract class PaymentCard implements IChargeable{
   int cardNumber;
    String expiryDate;
    int securityNumber;
    double availableCredit;
    ArrayList<Double> transactionList;

    public PaymentCard(int cardNumber, String expiryDate, int securityNumber) {
        this.cardNumber = cardNumber;
        this.expiryDate = expiryDate;
        this.securityNumber = securityNumber;
        this.transactionList = new ArrayList<>();
    }

    public int getCardNumber() {
        return cardNumber;
    }

    @Override
    public void charge(double amount) {
        this.transactionList.add(amount);
    }

    public ArrayList<Double> getTransactionList() {
        return transactionList;
    }
}
