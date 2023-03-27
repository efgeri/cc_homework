from models.continent import Continent
from models.country import Country
from models.city import City
from models.user import User
from models.visit import Visit
# import pdb

import repositories.continent_repository as continent_repo
import repositories.country_repository as country_repo
import repositories.city_repository as city_repo
import repositories.user_repository as user_repo
import repositories.visit_repository as visit_repo

continent_repo.delete_all()
country_repo.delete_all()
city_repo.delete_all()
user_repo.delete_all()
visit_repo.delete_all()

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

user1 = User("efgeri", "Gergely Farkas")
user2 = User("Visitor 1", "John Doe")
user3 = User("Visitor 2", "Jane Doe")

visit1 = Visit(user1, city1)
visit2 = Visit(user1, city2)
visit3 = Visit(user2, city3)
visit4 = Visit(user3, city1)

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

user_repo.save(user1)
user_repo.save(user2)
user_repo.save(user3)

visit_repo.save(visit1)
visit_repo.save(visit2)
visit_repo.save(visit3)
visit_repo.save(visit4)

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

# city_repo.delete(city4.id)

french_cities = city_repo.cities_by_country(country6)
print(f"{country6.name} has {len(french_cities)} cities in the database. The list is:")
for city in french_cities:
    print(f"{city.name}")

selected_user = user_repo.select(user1.id)
print (f"The selected user's name is: {selected_user.name}")

user_list = user_repo.select_all()
print("Here's the current list of users in the datbase:")
for user in user_list:
    print(f"{user.username}")

user2.username = "Traveller"
user_repo.update(user2)

# user_repo.delete(user3.id)

user_visits = user_repo.visited_cities(user1)
print(f"{user1.username} has visited {len(user_visits)} cities. The list is:")
for visit in user_visits:
    print(f"{visit.name}")


visit_list = visit_repo.select_all()
print("Here's the current list of visits in the datbase:")
for visit in visit_list:
    # pdb.set_trace()
    user = user_repo.select(visit.user.id)
    city = city_repo.select(visit.city.id)
    print(f"{user.username} visited {city.name}")

visit4.user = user2
visit_repo.update(visit4)

visit_repo.delete(visit3.id)    