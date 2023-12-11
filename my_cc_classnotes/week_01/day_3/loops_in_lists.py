# chickens = [
#   { "name": "Margaret", "age": 2, "eggs": 0 },
#   { "name": "Hetty", "age": 1, "eggs": 2 },
#   { "name": "Henrietta", "age": 3, "eggs": 1 },
#   { "name": "Audrey", "age": 2, "eggs": 0 },
#   { "name": "Mabel", "age": 5, "eggs": 1 },
# ]

# def find_chicken_by_name( list, chicken_name ):
#     for chicken in list:
#         if chicken["name"] == chicken_name:
#             return chicken
    
#     return None
    

# print(find_chicken_by_name(chickens, "Henrietta"))

# Another, better way of doing the above
# def find_chicken_by_name(list, chicken_name):
#     found_chicken = None

#     for chicken in list:
#         if chicken["name"] == chicken_name:
#             found_chicken = chicken

#     return found_chicken

users = [
  { "user_id": 1, "first_name": "Guido", "last_name": "van Rossum" },
  { "user_id": 2, "first_name": "Katherine", "last_name": "Johnson" },
  { "user_id": 3, "first_name": "Dorothy", "last_name": "Vaughan" },
  { "user_id": 4, "first_name": "Hen", "last_name": "Solo" },
  { "user_id": 5, "first_name": "Mary", "last_name": "Jackson" },
]
# Given a list of users, write a function to find a user by id. Test your function works with a specific id (e.g. 4).

def find_user(list, user_id):
    found_user = None

    for user in list:
        if user ["user_id"] == user_id:
            found_user = user

    return found_user

print(find_user(users, 4))