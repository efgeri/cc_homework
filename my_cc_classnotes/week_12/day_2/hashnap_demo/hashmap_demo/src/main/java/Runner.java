import java.util.HashMap;

public class Runner {

    public static void main(String[] args) {
        Country uk = new Country("UK", "Europe", "London", 64100000);
        Country germany = new Country("Germany", "Europe", "Berlin", 80620000);
        Country france = new Country("France", "Europe", "Paris", 66030000);
        Country japan = new Country("Japan", "Asia", "London", 127300000);

        HashMap <String, String> favouriteFruits = new HashMap <>();
        HashMap <String, Integer> populationOfCountries = new HashMap <>();
        HashMap <String, Country> countries = new HashMap <>();
        favouriteFruits.put("Alice", "Apple");
        favouriteFruits.put("Sarah", "Banana");
        favouriteFruits.put("Bob", "Strawberry");
        System.out.println(favouriteFruits.get("Bob"));

        populationOfCountries.put("UK", 64100000);
        populationOfCountries.put("Germany", 80620000);
        populationOfCountries.put("France", 66030000);
        populationOfCountries.put("Japan", 127300000);
        System.out.println(populationOfCountries.get("Japan"));
        System.out.println("Values method:" + populationOfCountries.values());
        System.out.println("Keyset method:" + populationOfCountries.keySet());

        countries.put("UK", uk);
        countries.put("Germany", germany);
        countries.put("France", france);
        countries.put("Japan", japan);

        countries.get("UK").getCountryInfo();
        countries.get("Germany").getCountryInfo();
        countries.get("France").getCountryInfo();
        countries.get("Japan").getCountryInfo();
    }

}
