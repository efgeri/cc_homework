# Make a dictionary called avengers. It should contain keys for Iron Man and Hulk.

# Each avenger is represented by another dictionary, and has a name (Tony Stark and Bruce Banner respectively) and another dictionary containing their attacks.

# Each attack should have an int value of the attack's power. Iron man can punch (10) and kick (100) and Hulk can smash (1000) and roll (500).

# Once you have created the dictionary, retrieve and print out the attack power of Hulks smash move.

avengers = {
    "Iron Man": {
        "name": "Tony Stark",
        "attacks": {
            "punch": 10,
            "kick": 100
        }
    
    },

    "Hulk": {
        "name": "Bruce Banner",
        "attacks": {
            "smash": 1000,
            "roll": 500
        }
    
    }
}

print(avengers ["Hulk"]["attacks"]["smash"])