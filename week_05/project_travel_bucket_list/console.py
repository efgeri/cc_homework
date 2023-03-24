from models.continent import Continent

import repositories.continent_repository as continent_repo

continent_repo.delete_all()

continent1 = Continent("Africa")
continent2 = Continent("Europe")
continent3 = Continent("Asia")

continent_repo.save(continent1)
continent_repo.save(continent2)
continent_repo.save(continent3)

selected_continent = continent_repo.select(continent1.id)
print (f"The selected continent's name is: {selected_continent.name}")

continent_list = continent_repo.select_all()
print("Here's the current list of continents in the datbase:")
for continent in continent_list:
    print(f"{continent.name}")

continent2.name = "European continent"
continent_repo.update(continent2)

continent_repo.delete(continent3.id)
