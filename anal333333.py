from scipy.io.wavfile import read
import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft
from scipy.io import wavfile
import csv
import pyaudio
import wave
from scipy.stats import sem

def lindistus():
	CHUNK = 1024
	FORMAT = pyaudio.paInt16
	CHANNELS = 2
	RATE = 44100
	RECORD_SECONDS = 5
	WAVE_OUTPUT_FILENAME = "output.wav"
	
	p = pyaudio.PyAudio()
	
	stream = p.open(format=FORMAT,
					channels=CHANNELS,
					rate=RATE,
					input=True,
					frames_per_buffer=CHUNK)
	
	print("* recording")
	
	frames = []
	
	for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
		data = stream.read(CHUNK)
		frames.append(data)

	print("* done recording")
	
	stream.stop_stream()
	stream.close()
	p.terminate()

	wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
	wf.setnchannels(CHANNELS)
	wf.setsampwidth(p.get_sample_size(FORMAT))
	wf.setframerate(RATE)
	wf.writeframes(b''.join(frames))
	wf.close()
	return wf
	
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
    avg = np.argmax(plotit)
    avg1 = np.amax(plotit)
    while plotit[avg] >= plotit[avg+10]+1000000:
        plotit[avg] = 0
        avg = np.argmax(plotit)
        # print("in a while: ", avg)
    plt.plot(plotit,'r')
    plt.show()
    print(avg)
    return avg

happy_array= np.loadtxt('Happy.txt')
sad_array= np.loadtxt('Sad.txt')

happy_ave = np.average(happy_array)
sad_ave = np.average(sad_array)

#happy_std = np.std(happy_array)
#sad_std = np.std(sad_array)

happy_std = sem(happy_array)
sad_std = sem(sad_array)

lindistus()
with open('testimiseks2.txt', 'r') as f:
      goodtime = f.readlines()

question1 = fftwav(goodtime[0].strip('\n'))
question = question1 - (happy_ave + sad_ave)
print("Happy ave: ", happy_ave)
print("Sad ave: ", sad_ave)
print("Question: ", question)
print("Question1: ", question1)
print("Happy std", happy_std)
print("Sad std", sad_std)

if (happy_ave - happy_std) < question1 and question1 < (happy_ave + happy_std):
    print("This is a happy person")    
elif (sad_ave - sad_std) < question1 and question1 < (sad_ave + sad_std):
    print("This is a sad person")    
elif (sad_ave + sad_std) < question1 and question1 < (happy_ave - happy_std):
    print("This is a neutral person")    
else: #(happy_ave + happy_std) < question < (sad_ave - sad_std):
    print("Unknown")
