ages = [5, 15, 64, 27, 84, 26]

odd_ages = [age for age in ages if age % 2 == 1]
# odd_ages = []
# for age in ages:
#     if age % 2 == 1:
#         odd_ages.append(age)

print(odd_ages)

chicken_names = ["Hen Solo", "Cluck Norris", "Hennifer Lopez", "ChewPekka", "Feather Locklear"]
more_than_10 = [name for name in chicken_names if len(name) > 10]
print(more_than_10)

name_h = [name for name in chicken_names if name[0] == "H"]
print(name_h)


words = ["The", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"]

first_letter = [word[0].lower() for word in words]
print(first_letter)