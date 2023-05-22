public class GiftCard implements IChargeable{
    double balance;

    public GiftCard(double balance) {
        this.balance = balance;
    }

    @Override
    public void charge(double amount) {
        this.balance -= amount;
    }

    public double getBalance() {
        return balance;
    }
}
