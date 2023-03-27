from models.continent import Continent
from models.country import Country
from models.city import City

import repositories.continent_repository as continent_repo
import repositories.country_repository as country_repo
import repositories.city_repository as city_repo

continent_repo.delete_all()
country_repo.delete_all()
city_repo.delete_all

continent1 = Continent("Africa")
continent2 = Continent("Europe")
continent3 = Continent("Asia")

country1 = Country("Egypt", continent1)
country2 = Country("Congo", continent1)
country3 = Country("Uganda", continent1)
country4 = Country("Hungary", continent2)
country5 = Country("Belgium", continent2)
country6 = Country("France", continent2)
country7 = Country("Japan", continent3)
country8 = Country("China", continent3)
country9 = Country("South Korea", continent3)

city1 = City("Budapest", False, country4)
city2 = City("Beijing", True, country8, "07/09/2012")
city3 = City("Paris", False, country6)
city4 = City("Brussels", False, country5)

continent_repo.save(continent1)
continent_repo.save(continent2)
continent_repo.save(continent3)

country_repo.save(country1)
country_repo.save(country2)
country_repo.save(country3)
country_repo.save(country4)
country_repo.save(country5)
country_repo.save(country6)
country_repo.save(country7)
country_repo.save(country8)
country_repo.save(country9)

city_repo.save(city1)
city_repo.save(city2)
city_repo.save(city3)
city_repo.save(city4)

selected_continent = continent_repo.select(continent1.id)
print (f"The selected continent's name is: {selected_continent.name}")

continent_list = continent_repo.select_all()
print("Here's the current list of continents in the datbase:")
for continent in continent_list:
    print(f"{continent.name}")

continent2.name = "European continent"
continent_repo.update(continent2)

# continent_repo.delete(continent3.id)

selected_country = country_repo.select(country1.id)
print (f"The selected country's name is: {selected_country.name}")

country_list = country_repo.select_all()
print("Here's the current list of countries in the datbase:")
for country in country_list:
    print(f"{country.name}")

country2.name = "South Africa"
country_repo.update(country2)

# country_repo.delete(country3.id)

european_countries = country_repo.countries_by_continent(continent2)
print(f"{continent2.name} has {len(european_countries)} countries in the database. The list is:")
for country in european_countries:
    print(f"{country.name}")

selected_city = city_repo.select(city1.id)
print (f"The selected city's name is: {selected_city.name}")

city_list = city_repo.select_all()
print("Here's the current list of cities in the datbase:")
for city in city_list:
    print(f"{city.name}")

city1.visit_date = "07/06/1997"
city1.visited = True
city_repo.update(city2)

city_repo.delete(city4.id)

french_cities = city_repo.cities_by_country(country6)
print(f"{country6.name} has {len(french_cities)} cities in the database. The list is:")
for city in french_cities:
    print(f"{city.name}")