public class CreditCard extends PaymentCard implements IChargeable{

    double availableCredit;

    public CreditCard(int cardNumber, String expiryDate, int securityNumber, double availableCredit) {
        super(cardNumber, expiryDate, securityNumber);
        this.availableCredit = availableCredit;
    }
}
