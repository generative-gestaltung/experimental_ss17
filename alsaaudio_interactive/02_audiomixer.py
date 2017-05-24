import sys
import time
import getopt
import alsaaudio
import math
import wave
import struct
from func import *
from array import array
from audioengine import *
import threading


samples = [
	Sample("beat01.wav"),
	Sample("DT_Clap.wav"),
	Sample("DT_Closedhat.wav"),
	Sample("DT_Cowbell.wav"),
	Sample("DT_Crash.wav"),
	Sample("DT_Openhat.wav"),
	Sample("DT_Ride.wav"),
	Sample("DT_Rimshot.wav"),
	Sample("DT_Snare.wav"),
	Sample("DT_Tamborine.wav"),
	Sample("DT_Tom01.wav"),
	Sample("DT_Tom02.wav"),
];



def s1():
	samples[1].start()

def s2():
	samples[2].start()

def s3():
	samples[3].start()

def s4():
	samples[4].start()




def setTimeout (time, f):
	t = threading.Timer(time, f)
	t.start()

def setInterval (time, f):
	def fwrapper ():
		setInterval(time, f)
		f()
	t = threading.Timer(time, fwrapper)
	t.start()


def main():

	device = 'default'


	PERIOD_SIZE = 32



	out = alsaaudio.PCM(alsaaudio.PCM_PLAYBACK, device=device)
	out.setchannels(1)
	out.setrate(44100)

	# out format little endian signed short
	out.setformat(alsaaudio.PCM_FORMAT_S16_LE)
 	out.setperiodsize(PERIOD_SIZE)


	# outdata array in signed short
	outData = array("h")

	# init array of period size
	for i in range (0, PERIOD_SIZE):
		outData.append(0)



	setInterval (0.1, s2)
	setInterval (0.4, s3)
	setInterval (1.2, s4)

	MIN = -32000
	MAX = 32000

	while True:

		for i in range (0, PERIOD_SIZE):
			outData[i] = 0
			sum = 0
			sum += samples[0].getNextValue()
			sum += samples[1].getNextValue()
			sum += samples[2].getNextValue()
			sum += samples[3].getNextValue()
			sum += samples[4].getNextValue()
			#sum += samples[5].getNextValue()
			#sum += samples[6].getNextValue()
			#sum += samples[7].getNextValue()
			#sum += samples[8].getNextValue()
			#sum += samples[9].getNextValue()
			#sum += samples[10].getNextValue()
			#sum += samples[11].getNextValue()

	
			outData[i] = constrain(sum, MIN, MAX)
	
		out.write (outData)


if __name__ == '__main__':

	main()
