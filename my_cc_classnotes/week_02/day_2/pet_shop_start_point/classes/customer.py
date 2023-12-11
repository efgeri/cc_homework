class Customer:
    def __init__(self, name, cash):
        self.name = name
        self.cash = cash
        self._pets = []

    def reduce_cash(self, amount):
        self.cash -= amount
    
    def pet_count(self):
        return len(self._pets)
    
    def add_pet(self, pet):
        self._pets.append(pet)

    def get_total_value_of_pets(self):
        total_value = 0
        for pet in self._pets:
            total_value += pet.price
        
        return total_value
