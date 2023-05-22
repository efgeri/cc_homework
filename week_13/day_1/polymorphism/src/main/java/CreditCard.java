public class CreditCard extends PaymentCard{

    double availableCredit;

    public CreditCard(int cardNumber, String expiryDate, int securityNumber, double availableCredit) {
        super(cardNumber, expiryDate, securityNumber);
        this.availableCredit = availableCredit;
    }

    @Override
    public void charge(double amount) {
        super.charge(amount);
        double punishmentPercentage = 1.10;
        this.availableCredit -= amount * punishmentPercentage;

    }

    public double getAvailableCredit() {
        return availableCredit;
    }
}
