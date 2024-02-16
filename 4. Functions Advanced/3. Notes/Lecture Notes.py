"""
Functions Arguments Order
"""


def arguments_order(a, b=6, *args, **kwargs):
    pass


"""
Unpacking Arguments
"""


# def print_nums(a,b,c):
#     print(a,b,c)
#
# print_nums(1,2,3)

def print_nums(a, b, c):
    print(a, b, c)


nums = [1, 2, 3]

print(*nums)

"""
Unpacking Dictionaries
"""


def some_func(name, age):
    print(f"{name} is {age} years old")


person = {"age": 20, "name": "Peter"}

# some_func(person["name"], person["age"]) # Peter is 20 years old

some_func(**person)  # Peter is 20 years old

"""

FUNCTIONS SORTING

"""

a = {10, -2, 3}

print(a)
print(sorted(a))
print(a)

# Sorted always returns list

print(sorted(a, reverse=True))
print(sorted(a, reverse=False))

my_dict = {'Peter': 21, 'George': 18, 'John': 45}
sorted_dict = sorted(my_dict.items(), key=lambda kvp: kvp[1])
# sorted_dict = sorted(my_dict.items(), key=lambda kvp: -kvp[1]) - only for numbers
sorted_dict2 = sorted(my_dict.items(), key=lambda kvp: kvp[1], reverse=True)

"""
NESTED FUNCTIONS
"""


def func1():
    def func2():
        return 5

    print(func2())

    return 6


print(func1())


# Functions can return other functions

def calculator(operator):
    def addition(a, b):
        return a + b

    def subtraction(a, b):
        return a - b

    if operator == "+":
        return addition
    elif operator == "-":
        return subtraction


# Lexical Closures


def outside_function(number):
    def inside_function():
        return number

    return inside_function


print(outside_function(10)())  # 10


