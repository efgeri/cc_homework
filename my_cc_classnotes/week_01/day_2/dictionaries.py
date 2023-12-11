# meals = {
#     1: "horror",
#     True: "joke", # this will overrite the value of key 1, because True is 1
#     "breakfast": "waffles",
#     "lunch": "tuna sandwich",
#     "dinner": "pasta pizza"
# }

# meals["dinner"] = "sushi"
# meals["supper"] = "kebabs"

# del(meals["lunch"])

# today = list(meals)  # this is just a snapshot at the time when it was called
# today2 = meals.keys() # this method tracks changes in keys always
# print (today)
# print (today2)
# meals ["snack"] = "biscuit"

# print (today)
# print (today2)

countries = {
	"uk": {
		"capital": "London",
		"population": 1000
	},
	"germany": {
		"capital": "Berlin",
		"population": 5
	}
}

print(countries)
print(countries ["germany"] ["population"])
print(countries ["uk"] ["capital"])
