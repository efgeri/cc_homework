heroes = ["Superman", "Batman", "Flash", "Green Lantern", "Wonder Woman"]
level = ["Over9k", 3456, 2967, 4563.2, 5555]

user_input = int(input("Type in a number between 1 and 5 "))

print(f"{heroes[user_input - 1]}'s power level is level {level[user_input - 1]}")