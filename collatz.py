# collatz.py
# Author: Joanne Feeney
# This script asks the user to input any positive integer and outputs 
# the successive values of the following calculation
# At each step calculate the next value by taking the current value and, if it is even, divide it by two
# but if it is odd, multiply it by three and add one
# The program ends if the current value is 1


# Tried using just if/else loops but was not working so tried while loop
# https://www.w3schools.com/python/python_while_loops.asp

def calculation(number):
    while number != 1:
        print(number, end =" ")
# You have used this end =" " formatting in lectures
        if number % 2 == 0:
# Defining a piece of code here that forces the user to input an even number only
# https://www.programiz.com/python-programming/examples/odd-even
            number //= 2
# Took a while to understand I need to do more than just number / 2
# https://www.geeksforgeeks.org/division-operators-in-python/
        else:
            number = (number * 3) + 1
    print(1)

number = int(input(f"Please type a positive integer: "))
calculation(number)
# Have to call a function for it to work
# https://www.w3schools.com/python/python_functions.asp
