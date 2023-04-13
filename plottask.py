# squareroot.py
# Author: Joanne Feeney
# This program displays a histogram of a normal distribution of 
# a 1000 values with a mean of 5 and standard deviation of 2, 
# and a plot of the function  h(x)=x3  in the range [0, 10], on the one set of axes

# Some marks will be given for making the plot look nice (legend etc).


#Lecture 8.2
# https://www.w3schools.com/python/numpy/numpy_intro.asp
# https://www.w3schools.com/python/matplotlib_intro.asp
import numpy as np
import matplotlib.pyplot as plt

xpoints = np.array(range(1,101))
ypoints = xpoints * xpoints

plt.plot(xpoints, ypoints, label= "putwhatIwant")
plt.legend()

np.random.seed(1)
normData = np.random.normal(size=1000)

plt.hist(normData)

plt.show()