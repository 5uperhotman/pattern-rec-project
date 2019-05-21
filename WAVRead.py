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
    b=[(ele/2**8.)*2-1 for ele in a]  # this is 8-bit track, b is now normalized on [-1,1)
    c = fft(b)                        # create a list of complex number
    d = int(len(c)/2)                 # you only need half of the fft list
    plotit = abs(c[:(d-1)])
    plt.plot(plotit,'r')
    # savefig(list+'.png',bbox_inches='tight')   #Saves figure, not too important
    plt.show() 

with open('Addresses.txt', 'r') as f:
      readings = f.readlines()

#print(readings[0])    
fftwav(readings[0].strip('\n')) # .strip needed to remove \n 


# References
#
# Perform an FFT on WAV and plot it: https://stackoverflow.com/questions/23377665/python-scipy-fft-wav-files
# Use list as input for function: https://interactivepython.org/runestone/static/CS152f17/Lists/UsingListsasParameters.html
# Split wav file into data and sampling rate: https://stackoverflow.com/questions/2060628/reading-wav-files-in-python
# Plot wav files:   https://stackoverflow.com/questions/18625085/how-to-plot-a-wav-file
# VB kasulik Python proge:  https://github.com/crhung/Voice-Emotion-Detector
# Write array into file:    https://stackoverflow.com/questions/29918719/python-write-array-values-into-file


################################################################################################################
#Sama asi mis yleval aga mitte funktsioonina:

#Split wav file into sampling rate (fs) and numpy array (data)
# fs, data = wavfile.read('C:/Users/Nathan/Desktop/Test_wav.wav')
# 
# a = data.T[0]                    # this is a two channel soundtrack, I get the first track
# b=[(ele/2**8.)*2-1 for ele in a] # this is 8-bit track, b is now normalized on [-1,1)
# c = fft(b)                       # calculate fourier transform (complex numbers list)
# d = int(len(c)/2)                     # you only need half of the fft list (real signal symmetry)
# plotit = abs(c[:(d-1)])
# plt.plot(plotit,'r') 
# k = np.arange(len(data))
# plt.xlabel('Frequencies')
# plt.ylabel('Occurance')
# plt.show()


################################################################################################################
# Mingid lambikad katsed, vb vaja tulevikus:

# read audio samples
# input_data = read("C:/Users/Nathan/Desktop/Test_wav.wav")
# audio = input_data[1]

# print(audio[0:1024])                       #Print first 1024 samples
# np.savetxt('Wav_Array.txt', audio[0:1024]) #Writes a numpy array of numbers (first 1024 samples) into a txt file
# file = open('Wav_contents.txt', 'wb')      #Writes the entire wav file as weird symbols, only works with binary saving (wb)
 
# for line in audio:
#      file.write(line)
# file.close() 

# plot the first 1024 samples
# plt.plot(audio[0:1024])
# plt.ylabel("Amplitude")
# plt.xlabel("Time") 
# plt.title("Sample Wav")
# plt.show()
