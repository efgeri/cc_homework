def return_10():
    return 10

def add(number_1, number_2):
    combine_number = 0
    combine_number = number_1 + number_2
    return combine_number

def subtract(number_1, number_2):
    subtract_number = 0
    subtract_number = number_1 - number_2
    return subtract_number

def multiply(number_1, number_2):
    multi = 0
    multi = number_1 * number_2
    return multi

def divide(number_1, number_2):
    div = 0
    div = number_1 / number_2
    return div

def length_of_string(string):
    length = 0
    length = len(string)
    return length

def join_string(word_1, word_2):
    joint = word_1 + word_2
    return joint

def add_string_as_number(string_1, string_2):
    combined = int(string_1) + int(string_2)
    return combined

def number_to_full_month_name(month_id):

    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    return months [month_id - 1]

def number_to_short_month_name(month_id):
    
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    getmonth = months [month_id - 1]
    return getmonth [0:3]

def cube_volume(side):
    return pow(side, 3) 

def reverse_string(string):
    return string[::-1]

# Jasper's solution, pretty nice
# def reverse_string(string):
    # new_string = ""
    # for char in string:
    #     new_string = char + new_string
    # return new_string


def convert_fahrenheit(fahrenheit):
    return (fahrenheit-32) * 5 / 9