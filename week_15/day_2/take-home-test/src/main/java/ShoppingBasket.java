import java.util.ArrayList;
import java.util.HashMap;
import java.util.Objects;

public class ShoppingBasket {
    private HashMap<Item, Integer> items;
    private Customer customer;

    public ShoppingBasket(Customer customer) {
        this.items = new HashMap<>();
        this.customer = customer;
    }

    public void addItem(Item item) {
        boolean itemExists = false;

        for (Item basketItem : items.keySet()) {
            if (item.getName() == basketItem.getName()) {
                items.put(basketItem, items.get(basketItem) + (Integer) 1);
                itemExists = true;
                break;
            }
            }
        if (!itemExists){
            items.put(item, 1);
        }
        }


    public void removeItem(Item item) {
        items.remove(item);
    }
    public void emptyBasket() {
        items.clear();
    }

    public HashMap<Item, Integer> getItems() {
        return items;
    }

        public double calculateTotal() {
        double loyaltyDiscount = 1;
        if (customer.hasLoyaltyCard()){
        loyaltyDiscount = 0.98;
        }
        double runningTotal = 0.0;
        for (Item basketItem : items.keySet()) {
            if (basketItem.isBogoFree()) {
                runningTotal += Math.ceil(items.get(basketItem) / 2.0) * basketItem.getPrice();
            }
            else {
                runningTotal += items.get(basketItem) * basketItem.getPrice();
            }
        }
        if (runningTotal > 20.0) {
            return runningTotal * loyaltyDiscount * 0.9;
        }
        else return runningTotal * loyaltyDiscount;
    }


}
