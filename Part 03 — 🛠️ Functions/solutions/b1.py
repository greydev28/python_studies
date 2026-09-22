#function for square of a number
def square_number(a:int)->int:
    return a**2
#return highest number
def larger_out_of_two(a,b):
    if a > b:
        return a
    return b
#return positive number
def ispostive(n):
    if n > 0:
        return True
    return False

print(larger_out_of_two(6,4))
print(ispostive(2))

def vowels(*n):
    count  = 0
    vowels_letter = ["a","e","i","o","u"]
    for item, letter in zip(n,vowels_letter):
        if item == letter:
            count = count + 1
    return count

print(vowels("a","e","i","o"))

def average(*n):
    total_count = 0
    length_of_number = len(n)
    for item in n:
        total_count += item
    print(total_count)
    average_item = total_count/length_of_number
    return average_item

print(average(1,4,3))


def convert_to_fahrenheit():
    
    try:
        number_in_ceisus = float(input("enter digit in ceisus.. "))
    except ValueError:
        print("please enter a valid number")
        return None
   
    else:
         fahrenheit = f'{(number_in_ceisus * 9/5) + 32}' 
    return fahrenheit

def convert_to_celsius():

    try:
        number_in_fahrenheit= float(input("enter digit in fahrenheit.. "))
    except ValueError:
        print("please enter a valid number")
        return None
   
    else:
         celsius = (number_in_fahrenheit - 32) * 5/9
    return celsius


def convert_miles(kilometers):
       miles = kilometers * 0.621371 
       return miles
print(f'{convert_miles(4):.2f}')


def add_item(items):
    items.append("Python")

langs = ["Go"]
add_item(langs)
print(langs)

	

    
