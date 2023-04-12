# account.py
# Author: Joanne Feeney
# This script reads in a 10 character account number and outputs the account number 
# with only the last 4 digits showing (and the first 6 digits replaced with Xs)

'''
What I think should be done to modify the program to allow any amount of integers
is done below, where the first 6 digits are always covered by an X thanks to slicing. 
There is probably a better way to do this with a loop where only the last 
4 digits are shown for any length of input whereas mine just blocks out the first
6 digits regardless on length
'''

# User input
# https://www.w3schools.com/python/python_user_input.asp
account_number = input("Please enter your 10 digit account number: ")

# Use of string multiplication and concatenation
# https://realpython.com/python-string-split-concatenate-join/
covered_account = "X" * 6 + account_number[6:]

# Slicing and the - index of -4: which allows the last 4 digits to be seen
# https://www.w3schools.com/python/python_strings_slicing.asp
last_4_digits = covered_account[-4:]

# Print account number
print(f"Your account number is:", covered_account)