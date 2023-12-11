# counter = 0
# target = 5

# while(counter <= target):
#     # print("The counter is at" + counter)
#     print(f"The counter is at {counter}")
#     counter += 1

# correct_answer = 24
# current_guess = int(input("What number am I thinking? "))

# while(current_guess != correct_answer):
#     if (current_guess > correct_answer):
#         print("Too high!")
#     else:
#         print("Too low!")
#     current_guess = int(input("Try again.. "))

# print("You did it!")

# numbers = [1, 2, 3, 4, 5]

# for number in numbers:
#     print(number * 3)

# chickens  = ["Margaret", "Hetty", "Henrietta", "Audrey", "Mabel"]

# for chicken in chickens:
#     print(chicken)

chickens = [
  {"name": "Margaret", "age": 2, "eggs": 0},
  {"name": "Hetty", "age": 1, "eggs": 2},
  {"name": "Henrietta", "age": 3, "eggs": 1},
  {"name": "Audrey", "age": 2, "eggs": 0},
  {"name": "Mabel", "age": 5, "eggs": 1},
]

total_eggs = 0

for chicken in chickens:
    # print(f'{chicken ["name"]} is {chicken["age"]}')
    # print(chicken["name"] + " is " + str(chicken["age"]))
    total_eggs += chicken["eggs"]
    chicken["eggs"] = 0

print(f"{total_eggs} eggs collected")
print(chickens)
