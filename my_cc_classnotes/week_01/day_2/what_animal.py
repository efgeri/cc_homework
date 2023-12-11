# SET animal = Input "What animal are you?"
# If animal is a "chicken"
#   THEN PRINT "This is my favourite animal"
# ELSE
#   IF animal is "kitten"
#     THEN print "I love kittens"
#   ELSE
#     PRINT "Sad, not my favourite"
# End

animal = input("What animal are you? ")

if animal == "chicken":
    print("This is my favourite animal")
elif animal == "kitten":
    print("I love kittens")    
else:
    print("Sad, not my favourite")

score = 6

result = "pass" if score > 5 else "fail"

# Checking multiple conditions
