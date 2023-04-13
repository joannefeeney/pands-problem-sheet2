# weekday.py
# Author: Joanne Feeney
# This program outputs whether or not today is a weekday

# How to import datetime module 
# https://www.w3schools.com/python/python_datetime.asp

import datetime

x = datetime.datetime.now()

# Used the below site to help me create an if loop that reads in the day of the week
# as an int and then output whether today is a weekday or weekend day
# https://pynative.com/python-get-the-day-of-week/
# Was thinking I would have to use '%w' however this site showed me I don't have to
no = x.weekday()

if no < 5:
    print("Yes, unfortunately today is a weekday")
else:
    print("It is the weekend, yay!")