import RPi.GPIO as GPIO
import sys
import time
import getopt
import alsaaudio
import math
import wave
import struct
from func import *
from array import array
import audioengine as audio
from audioengine import Sample
import threading


samples = [
	Sample ("WAV/beat01.wav"),
	Sample ("WAV/DT_Clap.wav"),
	Sample ("WAV/DT_Closedhat.wav"),
	Sample ("WAV/DT_Cowbell.wav"),
	Sample ("WAV/DT_Crash.wav"),
	Sample ("WAV/DT_Openhat.wav"),
	Sample ("WAV/DT_Ride.wav"),
	Sample ("WAV/DT_Rimshot.wav"),
	Sample ("WAV/DT_Snare.wav"),
	Sample ("WAV/DT_Tamborine.wav"),
	Sample ("WAV/DT_Tom01.wav"),
	Sample ("WAV/DT_Tom02.wav"),
];


def setTimeout (time, f):
	t = threading.Timer(time, f)
	t.start()

def setInterval (time, f):
	def fwrapper ():
		setInterval(time, f)
		f()
	t = threading.Timer(time, fwrapper)
	t.start()


def onEdge (ch):
	samples[0].start()

def main():

	PERIOD_SIZE = 256

	GPIO.setmode (GPIO.BCM)
	GPIO.setup (4, GPIO.IN)
	GPIO.add_event_detect (4, GPIO.RISING, onEdge, 200)

	#audio = AudioDevice(1024)
	audio.initAudio (PERIOD_SIZE)
	samples[0].start()

	while True:

		for i in range (0, PERIOD_SIZE):

			sum = samples[0].getNextValue()
			sum += samples[1].getNextValue()
			sum += samples[3].getNextValue()
			sum += samples[4].getNextValue()
			#sum += samples[5].getNextValue()
			#sum += samples[6].getNextValue()
			#sum += samples[7].getNextValue()

			audio.writeSample (sum)



if __name__ == '__main__':

	main()
