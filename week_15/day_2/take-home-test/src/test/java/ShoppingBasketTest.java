import org.junit.Before;
import org.junit.Test;

import java.util.HashMap;

import static org.junit.Assert.assertEquals;

public class ShoppingBasketTest {
    Item item1;
    Item item2;
    Item item3;
    Item item4;
    Item item5;
    Item item6;
    Item item7;
    Item item8;
    ShoppingBasket shoppingBasket;
    ShoppingBasket shoppingBasketLoyal;

    @Before
    public void before(){
        item1 = new Item("milk", 1.60, true);
        item2 = new Item("rolls", 0.80, false);
        item3 = new Item("milk", 1.60, true);
        item4 = new Item("salami", 2.50, false);
        item5 = new Item("tomatoes", 3.00, false);
        item6 = new Item("milk", 1.60, true);
        item7 = new Item("salami", 2.50, false);
        item8 = new Item("couch", 20.00, false);

        Customer notLoyal = new Customer(false);
        Customer loyal = new Customer(true);
        shoppingBasket = new ShoppingBasket(notLoyal);
        shoppingBasketLoyal = new ShoppingBasket(loyal);
        shoppingBasket.addItem(item1);
        shoppingBasket.addItem(item2);
    }


    @Test
    public void canSaveItems(){
        HashMap <Item, Integer> basketContent = shoppingBasket.getItems();
        assertEquals(2, basketContent.size());
    }

    @Test
    public void canHaveMoreThanOne() {
        shoppingBasket.addItem(item3);
        HashMap <Item, Integer> basketContent = shoppingBasket.getItems();
        assertEquals((Integer)2, basketContent.get(item1));
    }

    @Test
    public void canCalculateNoDiscount() {
        shoppingBasket.addItem(item4);
        shoppingBasket.addItem(item5);
        assertEquals(7.9, shoppingBasket.calculateTotal(), 0.1);

    }

    @Test
    public void canCalculateWithBogoFree() {
        shoppingBasket.addItem(item3);
        shoppingBasket.addItem(item4);
        shoppingBasket.addItem(item5);
        assertEquals(7.9, shoppingBasket.calculateTotal(), 0.1);
    }
    @Test
    public void canCalculateWithOddNumberBogoFree() {
        shoppingBasket.addItem(item3);
        shoppingBasket.addItem(item4);
        shoppingBasket.addItem(item5);
        shoppingBasket.addItem(item6);
        assertEquals(9.5, shoppingBasket.calculateTotal(), 0.1);
    }
    @Test
    public void canIgnoreNotBogoFree() {
        shoppingBasket.addItem(item4);
        shoppingBasket.addItem(item7);
        assertEquals(7.4, shoppingBasket.calculateTotal(), 0.1);
    }
    @Test
    public void canCalculateWithBogoFreeAndTenPercent() {
        shoppingBasket.addItem(item3);
        shoppingBasket.addItem(item4);
        shoppingBasket.addItem(item5);
        shoppingBasket.addItem(item7);
        shoppingBasket.addItem(item8);
        assertEquals(27.36, shoppingBasket.calculateTotal(), 0.1);

    }
    @Test
    public void canCalculateWithAllDiscount() {
        shoppingBasketLoyal.addItem(item1);
        shoppingBasketLoyal.addItem(item2);
        shoppingBasketLoyal.addItem(item3);
        shoppingBasketLoyal.addItem(item4);
        shoppingBasketLoyal.addItem(item5);
        shoppingBasketLoyal.addItem(item6);
        shoppingBasketLoyal.addItem(item7);
        shoppingBasketLoyal.addItem(item8);
        assertEquals(28.224, shoppingBasketLoyal.calculateTotal(), 0.1);
    }
    @Test
    public void canCalculateLoyalUnder20() {
        shoppingBasketLoyal.addItem(item1);
        shoppingBasketLoyal.addItem(item2);
        assertEquals(2.352, shoppingBasketLoyal.calculateTotal(), 0.0001);
    }



}
