from models.continent import Continent
from models.country import Country

import repositories.continent_repository as continent_repo
import repositories.country_repository as country_repo

continent_repo.delete_all()
country_repo.delete_all()

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
print("Here's the current list of countrys in the datbase:")
for country in country_list:
    print(f"{country.name}")

country2.name = "South Africa"
country_repo.update(country2)

country_repo.delete(country3.id)

european_countries = country_repo.countries_by_continent(continent2)
print(f"{continent2.name} has {len(european_countries)} countries in the database. The list is:")
for country in european_countries:
    print(f"{country.name}")