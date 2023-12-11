import java.util.HashMap;

public class Runner {

    public static void main(String[] args) {
        HashMap<String, String> meals = new HashMap<>();
        meals.put("breakfast", "yoghurt");
        meals.put("lunch", "roll");
        meals.put("dinner", "steak");
        System.out.println(meals);
        System.out.println(meals.get("dinner"));
        System.out.println(meals.replace("breakfast", "cereal"));
        System.out.println(meals);
    }
}
