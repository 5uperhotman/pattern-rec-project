from scipy.io.wavfile import read
import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft
from scipy.io import wavfile
import csv

def fftwav(list, title):
    #for position in range(len(list)):
       #list[position] = 2 * list[position]
      
    fs, data = wavfile.read(list)     # load the data
    a = data.T[0]                     # this is a two channel soundtrack, I get the first track
    b=[(ele/2**2.)*2-1 for ele in a]  # this is 8-bit track, b is now normalized on [-1,1)
    c = fft(b)                        # create a list of complex number
    d = int(len(c)/2)-75000           # you only need half of the fft list
    plotit = abs(c[:(d-1)])
    # plt.plot(plotit,'r')
    # savefig(list+'.png',bbox_inches='tight')   #Saves figure, not too important
    plotit[plotit <= 2.0e+02] = 0
    np.savetxt('%s.txt' %title, np.nonzero(plotit))
    # plt.show() 
    return plotit
    

# Happy
with open('Addresses_happy.txt', 'r') as f:
      readings_happy = f.readlines()

fftwav(readings_happy[0].strip('\n'), "Happy_1") # .strip needed to remove \n 
fftwav(readings_happy[1].strip('\n'), "Happy_2")
fftwav(readings_happy[2].strip('\n'), "Happy_3")
fftwav(readings_happy[3].strip('\n'), "Happy_4")
fftwav(readings_happy[4].strip('\n'), "Happy_5")
fftwav(readings_happy[5].strip('\n'), "Happy_6")
fftwav(readings_happy[6].strip('\n'), "Happy_7")
fftwav(readings_happy[7].strip('\n'), "Happy_8")


# Sad

with open('Adresses_sad.txt', 'r') as f:
      readings_sad = f.readlines()

fftwav(readings_sad[0].strip('\n'), "Sad_1") 
fftwav(readings_sad[1].strip('\n'), "Sad_2")
fftwav(readings_sad[2].strip('\n'), "Sad_3")
fftwav(readings_sad[3].strip('\n'), "Sad_4")
fftwav(readings_sad[4].strip('\n'), "Sad_5")
fftwav(readings_sad[5].strip('\n'), "Sad_6")
fftwav(readings_sad[6].strip('\n'), "Sad_7")




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
