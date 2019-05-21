import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

#with open('happy/happy_1.txt') as my_file:
#    happy_array = my_file.readlines()

happy_array= np.loadtxt('happy/happy_1.txt')
sad_array= np.loadtxt('sad/sad_1.txt')

#with open('sad/sad_1.txt') as my_file:
#    sad_array = my_file.readlines()

# Calculate the mean vectors per class
mean_happy = np.array([np.mean(happy_array, axis=0)]
mean_sad = np.array([np.mean(sad_array, axis=0)])
Mu = (mean_sad + mean_happy)/2.0

# Calculate the scatter matrices for the SW (Scatter within) and sum the elements up

scatter_happy = np.dot((happy_array-mean_happy),(happy_array-mean_happy).T)

# Mind that we do not calculate the covariance matrix here because then we have to divide by n or n-1 as shown below
# Calculate the SW by adding the scatters within classes 
scatter_sad = np.dot((sad_array-mean_sad),(sad_array-mean_sad).T)
SW = scatter_sad+scatter_happy

r,N1 = happy_array.shape
r,N2 = sad_array.shape
mean_happy = mean_happy.transpose()
mean_sad = mean_sad.transpose()
m1 = hean_happy-Mu
m2 = mean_sad-Mu
Sb1 = N1*np.matmul(m1,m1.transpose())
Sb2 = N2*np.matmul(m2,m2.transpose())
# between-class scatter matrix
Sb = Sb1 + Sb2

# LDA projection
SwSb = np.matmul(np.linalg.pinv(SW),Sb)

print("Whitin class scatter matrix: ",SW)
print("Between class scatter matrix: ",Sb)
print("LDA projection: ", SwSb)

# projection vector
w, v = np.linalg.eig(SwSb)
# w - eigenvalues
# v - eigenvectors
print("Eigenvalues")
print(w)
print("Eigenvectors")
print(v)

# project data samplesalong he projection axes
new_happy = np.matmul(happy_array,W1)
new_sad = np.matmul(sad_array,W1)