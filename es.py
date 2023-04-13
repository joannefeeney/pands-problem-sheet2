# squareroot.py
# Author: Joanne Feeney
# This program reads in a text file and outputs the number of e's it contains 

# Think about what is being asked here, document any assumptions you are making
# The program should take the filename from an argument on the command line

# How to open/read etc. a txt file 
# https://www.w3schools.com/python/python_file_handling.asp

f = open("alice_in_wonderland.txt", "r")
print(f.read())
