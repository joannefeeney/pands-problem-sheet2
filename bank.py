# bank.py
# Author: Joanne Feeney
# This script prompts the user and reads in two money amounts (in cents)
# Adds the two amounts
# Prints out the answer in a human readable format 
# With a euro sign and decimal point between the euro and cent of the amount


# First integer which will be input by user
# https://www.w3schools.com/python/python_user_input.asp
cent1 = int(input("Enter the first amount in cent: "))

# Second integer which will be input by user
cent2 = int(input("Enter the second amount in cent: "))


total_cent = cent1 + cent2
total_euro = 0
# Use of if loop here to ensure it counts in euros if higher than 100
if total_cent >= 100:
    total_euro += 1
    total_cent -= 100

# Output formatted with {:.2f} so the number will be formatted with two decimal placess
# https://www.freecodecamp.org/news/2f-in-python-what-does-it-mean/ 
print("The total amount is €{:.2f}".format(total_euro + total_cent/100))
