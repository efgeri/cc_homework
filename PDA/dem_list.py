def powerlevel(list1, list2):
    user_input = int(input("Type in a number between 1 and 5 "))
    print(f"{list1[user_input - 1]}'s power level is level {list2[user_input - 1]}")

heroes = ["Superman", "Batman", "Flash", "Green Lantern", "Wonder Woman"]
level = ["Over9k", 3456, 2967, 4563.2, 5555]

powerlevel(heroes, level)