# squareroot.py
# Author: Joanne Feeney
# This program takes a positive floating-point number 
# as input and outputs an approximation of its square root
# You should create a function called <tt>sqrt</tt> that takes a positive 
# floating-point number as input and outputs an approximation of its square root

# Watched lecture 8.1 again
# Some of my failed attempts below
'''def sqrt(number, base):
    x = number
    count = 0

    while (base):
        count += base
        root = 0.5 * (x + (number / x))
        if (abs(root - x) < base):
            break
        else:
            print(f"The square root of your number is", sqrt(number, base))

def sqrt(number, base):
        approx_root = 0.5 * number
        for i in range(base):
            betterapprox = 0.5 * (approx_root + n/approx_root)
            approx_root = betterapprox
        return betterapprox

print("the square root of your number is ",sqrt)
'''
# Used three wesbites to help me with this one
# https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/
# https://tutorialsinhand.com/Articles/python-program-to-find-square-root-
# of-a-number-using-newton-square-root-formula.aspx#:~:text=If%20a%20given%20number%20is,
# correct%20square%20root%20of%20N.
# https://www.goeduhub.com/3398/python-program-to-find-the-square-root-number-newtons-method
def sqrt(number, number_iters = 100):

    a = float(number) 

    for i in range(number_iters): 

        number = 0.5 * (number + a / number) 

    return number

a = float(input("Enter a positive number:"))
# Output formatted with {:.2f} same as my bank.py program
print("The square root of your number is approximately {:.2f}".format(sqrt(a)))