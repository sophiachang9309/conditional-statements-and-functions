'''
IF & IF-ELSE & ELSE-IF Ex:

number = 5
if number > 3:
    print("The number is greater than 3!")


number = 10

if number % 2 == 0:
    print("The number is EVEN!")
else:
    print("The number is ODD!")


number = 7

if number > 0:
    print("The number is GREATER than 0!")
elif number < 0:
    print("The number is LESS than 0!")
else:
    print("The number is EQUAL to 0!")

'''
'''
AND & OR Ex:

has_ticket = True
height_in_inches = 50

if height_in_inches > 45 and has_ticket:
    print("You CAN ride the rollercoaster!")
else:
    print("You can NOT ride the rollercoaster!")


age = 23

if age <= 12 or age >= 65:
    print("You get a discount!")
else:
    print("You DON'T get a discount!")
'''
'''
FUNCTION Ex:

def make_tacos(): #makes it easier so that you don't always have to type out every single instruciton
    print("Get a tortilla")
    print("Add meat")
    print("Add cheese")
    print("Add salsa")
    print("Enjoy your taco!")

#we can reuse our make_tacos() function as many times
make_tacos()
make_tacos()
make_tacos()


PARAMETERS & ARGUMENTS Ex:

person_one_age = 16
person_two_age = 18
person_three_age = 20

#Ex of making life harder:
if person_one_age >= 18:
    print("Old enough to drive!")
else:
    print("NOT old enough to drive!")

if person_two_age >= 18:
    print("Old enough to drive!")
else:
    print("NOT old enough to drive!")

if person_three_age >= 18:
    print("Old enough to drive!")
else:
    print("NOT old enough to drive!")

#Ex of making life easier that funcitons the same:
def check_age(person_age):
    if person_age >= 18:
        print("Old enough to drive!")
    else:
        print("NOT old enough to drive!")


check_age(person_one_age)
check_age(person_two_age)
check_age(person_three_age)

#another ex:
first_num = 5
second_num = 4

def add_nums(num_one, num_two):
    sum = num_one + num_two
    print(sum)

add_nums(first_num, second_num)

SCOPE Ex:

first_num = 5
second_num = 4
sum = 0

def add_nums(num_one, num_two):
    sum = num_one + num_twp
    print(sum) #this will only print if the variable "sum" is createad outside of this function

add_nums(first_num, second_num)


RETURN Ex:
number_to_square = 5

def square_number(number):
    square_result = number * number
    return square_result #The result is returned and stored inside of the “result” variable outside of the function!

result = square_number(number_to_square)
'''
