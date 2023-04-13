# squareroot.py
# Author: Joanne Feeney
# This program reads in a text file and outputs the number of e's it contains 

'''
I assumed I could do this with a loop and the count function but I
needed help from online sources to figure out exactly how I could get the code
to look for just one letter and count/output the amount of times that letter 
appeared in the text
'''

# How to open/read a txt file 
# https://www.w3schools.com/python/python_file_handling.asp

# Help with coding to count number of es
# https://pythonexamples.org/python-count-number-of-characters-in-text-file/
# https://www.geeksforgeeks.org/count-the-number-of-times-a-letter-appears-in-a-text-file-in-python/

def number_of_es(txt_file, letter):
    
    f = open(txt_file, "r")
 
    text = f.read()
 
    return text.count(letter)
 
print(f"Number of es in txt file is: ", number_of_es('alice_in_wonderland.txt', 'e'))



