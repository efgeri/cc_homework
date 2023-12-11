class PetShop:
    def __init__(self, name, pets, total_cash):
        self.name = name
        self._pets = pets
        self.pets_sold = 0
        self.total_cash = total_cash

    def stock_count(self):
        return len(self._pets)
    
    def increase_pets_sold(self):
        self.pets_sold += 1

    def increase_total_cash(self, amount):
        self.total_cash += amount

    def remove_pet(self, pet):
        self._pets.remove(pet)

    def find_pet_by_name(self, pet_name):
        for pet in self._pets:
            if pet.name == pet_name:
                return pet
            
    def sell_pet_to_customer (self, pet_name, customer):
        if self.find_pet_by_name(pet_name):
            selected = self.find_pet_by_name(pet_name)
            customer.reduce_cash(selected.price)
            self.increase_total_cash(selected.price)
            self.increase_pets_sold()
            self.remove_pet(selected)
            customer.add_pet(selected)