# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(shop):
    return shop["name"]

def get_total_cash(shop):
    return shop["admin"]["total_cash"]

def add_or_remove_cash(shop, amount):
    shop["admin"]["total_cash"] += amount
    # return get_total_cash(shop)  This line is not needed, because this function doesn't have to return anything.

def get_pets_sold(shop):
    return shop["admin"]["pets_sold"]

def increase_pets_sold(shop, sold):
    shop["admin"]["pets_sold"] += sold
    # return get_pets_sold(shop)   This is not needed for the same reason as above

def get_stock_count(shop):
    return len(shop["pets"])

def get_pets_by_breed(shop, breed):
    breed_selection = []
    for pet in shop["pets"]:
        if pet["breed"] == breed:
            breed_selection.append(pet)
    return breed_selection

def find_pet_by_name(shop, name):
    for pet in shop["pets"]:
        if pet["name"] == name:
            return pet
        
def remove_pet_by_name(shop, name):
    for pet in shop["pets"]:
        if pet["name"] == name:
            shop["pets"].remove(pet)

def add_pet_to_stock(shop, new_pet):
    shop["pets"].append(new_pet)

def get_customer_cash(customer):
    return customer["cash"]

def remove_customer_cash(customer, amount):
    customer["cash"] -= amount
    # return get_customer_cash(customer)  Same as return lines above

def get_customer_pet_count(customer):
    return len(customer["pets"])

def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)

def customer_can_afford_pet(customer, new_pet):
    can_afford = False
    if customer["cash"] >= new_pet["price"]:
        can_afford = True
    return can_afford

# alteratively: return customer["cash"] >= pet["price"]

def sell_pet_to_customer(shop, new_pet, customer):
    if new_pet != None:
        if customer_can_afford_pet(customer, new_pet) == True:
            remove_customer_cash(customer, new_pet["price"])
            add_or_remove_cash(shop, new_pet["price"])
            add_pet_to_customer(customer, new_pet)
            remove_pet_by_name(shop, new_pet)
            increase_pets_sold(shop, 1)

