import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

with open('happy/happy_1.txt') as my_file:
    happy_array = my_file.readlines()

with open('sad/sad_1.txt') as my_file:
    sad_array = my_file.readlines()

# Calculate the mean vectors per class
mean_happy = np.mean(happy_array,axis=1).reshape(2,1) # Creates a 2x1 vector consisting of the means of the dimensions 
mean_sad = np.mean(sad_array,axis=1).reshape(2,1)

#mean_circles = np.mean(circles,axis=1).reshape(2,1)
# Calculate the scatter matrices for the SW (Scatter within) and sum the elements up

scatter_happy = np.dot((happy_array-mean_happy),(happy_array-mean_happy).T)

# Mind that we do not calculate the covariance matrix here because then we have to divide by n or n-1 as shown below
#print((1/7)*np.dot((rectangles-mean_rectangles),(rectangles-mean_rectangles).T))
#print(np.var(rectangles[0],ddof=0))
scatter_sad = np.dot((sad_array-mean_sad),(sad_array-mean_sad).T)

#scatter_circles = np.dot((circles-mean_circles),(circles-mean_circles).T)
# Calculate the SW by adding the scatters within classes 
SW = scatter_sad+scatter_happy
print(SW)
plt.show()