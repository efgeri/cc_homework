def powerlevel(dict):
    user_input = (input("Type in a hero's name: "))
    print(f"{user_input}'s power level is level {dict[user_input]}")


hero_attributes = {
    "Superman":"Over9k",
    "Batman":3456,
    "Flash":2967,
    "Green Lantern":4563.2,
    "Wonder Woman":5555
}

powerlevel(hero_attributes)
