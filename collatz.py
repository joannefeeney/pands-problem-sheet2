# collatz.py
# Author: Joanne Feeney
# This script asks the user to input any positive integer and outputs 
# the successive values of the following calculation
# At each step calculate the next value by taking the current value and, if it is even, divide it by two
# but if it is odd, multiply it by three and add one
# The program ends if the current value is one


integer1 = int(input("Please type a positive integer: "))

x = int(even)
y = int(odd)

# Tried using if/else loops but was not working so tried while loop
# https://www.w3schools.com/python/python_while_loops.asp
while integer1 == x:
    print(integer1 / 2)
    if integer1 == y:
        print((y * 3) + 1)
    if integer1 == 1:
        break
    integer1 += 1