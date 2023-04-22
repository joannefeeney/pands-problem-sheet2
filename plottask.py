# plottask.py
# Author: Joanne Feeney
# This program displays a histogram of a normal distribution of 
# a 1000 values with a mean of 5 and standard deviation of 2, 
# and a plot of the function  h(x)=x3  in the range [0, 10], on the one set of axes


# Lecture 8.2 used for a lot of hte below code
# https://www.w3schools.com/python/numpy/numpy_intro.asp
# https://www.w3schools.com/python/matplotlib_intro.asp
import numpy as np
import matplotlib.pyplot as plt

xpoints = np.array(range(1,10))
ypoints = xpoints * xpoints

# To change the colour of the line to red via '-r' I used:
# https://www.w3schools.com/python/matplotlib_markers.asp
plt.plot(xpoints, ypoints, '-r', label= "h(x)=x3")
plt.legend()

np.random.seed(1)
# To get stndard deviation and mean
# https://www.w3schools.com/python/matplotlib_histograms.asp
normData = np.random.normal(5, 2, 1000)
plt.hist(normData)

# To add a title
# https://www.w3schools.com/python/matplotlib_labels.asp
plt.title("Week 08 Task")
# To add a grid
# https://www.w3schools.com/python/matplotlib_grid.asp
plt.grid(axis = 'y')
plt.show()