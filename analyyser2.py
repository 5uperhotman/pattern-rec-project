from scipy.io.wavfile import read
import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft
from scipy.io import wavfile
import csv

def fftwav(list):
    #for position in range(len(list)):
       #list[position] = 2 * list[position]
      
    fs, data = wavfile.read(list)     # load the data
    a = data.T[0]                     # this is a two channel soundtrack, I get the first track
    b=[(ele/2**2.)*2-1 for ele in a]  # this is 8-bit track, b is now normalized on [-1,1)
    c = fft(b)                        # create a list of complex number
    d = int(len(c)/2)-75000           # you only need half of the fft list
    plotit = abs(c[:(d-1)])
    
    # savefig(list+'.png',bbox_inches='tight')   #Saves figure, not too important
    #plotit[plotit <= 2.0e+02] = 0
    plotit = plotit[100:5000]
    n = 0
    threshold = 55000                 # Siit saab muuta thresholdi, millest allapoole väärtused lükatakse nulliks
    for i in plotit:
        if plotit[n] <= threshold:
            plotit[n]=0
        n = n + 1
    ave = np.median(np.nonzero(plotit))
    return ave

happy_array= np.loadtxt('happy/happy_1.txt')
sad_array= np.loadtxt('sad/sad_1.txt')

happy_ave = np.median(np.nonzero(happy_array)) 
sad_ave = np.median(np.nonzero(sad_array)) 

with open('siia tuleb failinimi', 'r') as f:
      goodtime = f.readlines()

question = fftwav(goodtime)

a1 = abs(happy_array-question)
a2 = abs(sad_ave-question)

if a1 < a1:
    print("This is a happy person")
else:
    print("This is a sad person")

