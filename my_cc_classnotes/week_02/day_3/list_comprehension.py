# Remember, this effectively gives us a list of [1,2,3,4,5,6,7,8,9,10]
# numbers = range(1, 11)
# evens_squared = []
# for number in numbers:
#     if number % 2 == 0:
#         evens_squared.append(number * number)

# We can write this above code shorter with list comprehension

evens_squared = [number * number for number in range(1, 11) if number % 2 == 0]

print(evens_squared)