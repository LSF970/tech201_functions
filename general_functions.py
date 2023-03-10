# Functions

# D R Y
# Don't Repeat Yourself

# Creating a function

# def print_something():
#     print("Something has been printed")
#
# print_something()

# Functions and arguements

# def print_something(print_string):
#     print(print_string)
#
# print_something("this is my variable")
#
# print_something("This is the second time I called this function")

# In Java:
# public void print_string(String_text)

# def greetings(name):
#     print("Hello, my name is " + name)
#
# greetings("Luke")
# greetings("Flo")
# greetings("Belal")
# greetings("Bakar")

# The Return statement

# def addition(int1, int2):
#     return int1 + int2
#
# print(addition(2, 2))

# Default arguements

# def addition(int1=5, int2=5):
#     return int1 + int2
#
# print(addition())
# print(addition(10, 10))
# print(addition())

# Multiple arguements

# def multi_args(*multiargs):
#     print(type(multiargs))
#
#     for arg in multiargs:
#         print(arg)
#
# multi_args(1, 2, 3, 4, 5 ,6, 7 , 8 ,9, 10)
#
# multi_args(1, 2, 3, 4, 5)

# Type Hints

# def greeting(name: str):
#     print("Hello, my name is " + name)
#
# greeting(24601)


# def division(num1: int = 5, num2: int = 2) -> float:
#     return num1 / num2
#
# print(division())

# Functions best practices

## Name your functions clearly using lower case and underscores
## All arguements should be clear in their need and where possible include their expected type
## Remember the return statement or your function will return None
## Keep functions small to preserve readbility and simplicity
## Use comments in your functions/methods to give instrucutons on how to use them
## Consider using type hints to avoid type errors when you run your code.