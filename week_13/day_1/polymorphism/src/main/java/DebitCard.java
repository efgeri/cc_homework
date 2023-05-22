public class DebitCard extends PaymentCard implements IChargeable {
    int accountNumber;
    int sortCode;


    public DebitCard(int cardNumber, String expiryDate, int securityNumber, int accountNumber, int sortCode) {
        super(cardNumber, expiryDate, securityNumber);
        this.accountNumber = accountNumber;
        this.sortCode = sortCode;
    }
}
