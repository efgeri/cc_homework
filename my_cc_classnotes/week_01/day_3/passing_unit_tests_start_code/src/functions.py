
def greet_catalan(name):
    return f"Hola, {name}"


def greet_mandarin(name):
    return f"Ni hao, {name}"

def count_eggs(list):
    total_eggs = 0
    for bird in list:
        total_eggs += bird["eggs"]
    return total_eggs

def find_chicken_by_name(list, chicken_name):
    found_chicken = None

    for chicken in list:
        if chicken["name"] == chicken_name:
            found_chicken = chicken
    return found_chicken



