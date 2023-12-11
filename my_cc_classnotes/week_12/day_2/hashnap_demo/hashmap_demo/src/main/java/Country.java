public class Country {

    private String name;
    private String continent;
    private String capital;
    private int population;

    public Country (String name, String continent, String capital, int population){
        this.name = name;
        this.continent = continent;
        this.capital = capital;
        this.population = population;
    }

    public void getCountryInfo(){
        System.out.printf("In %s there are %d people. The capital of %s is %s and it is in %s.%n", this.name, this.population, this.name, this.capital, this.continent);
    }
}
