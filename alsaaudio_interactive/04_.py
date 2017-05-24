import sys
import time
import getopt
import alsaaudio
import math
import wave
import struct
from func import *
from array import array
from audioengine import AudioDevice




class Sample:
	def __init__(self, fname):

		# read wavedata as string of bytes
		wav = wave.open (fname, "rb")
		l = wav.getnframes()
		dat = wav.readframes(l)

		# unpack as little endian 2byte signed shorts
		dat = struct.unpack ("<%dh"%(len(dat)/2), dat)
		
		# extract left and right channel

		if (wav.getnchannels()==2):
			self.datL = dat[0::2]
			self.datR = dat[1::2]
		
		else:
			self.datL = dat
			self.datR = dat
			
		# get sample length in shorts
		self.len = len(self.datL)


		wav.close()
		self.inc = 0
		self.pos = 0
		self.running = False

	def getNextValue (self):
		
		ret = self.datL[self.pos%self.len]
 		self.pos = (self.pos+self.inc)
		return ret

	def start (self):
		self.inc = 1



def main():

	device = 'default'

	samples = [
		Sample("WAV/beat01.wav"),
		Sample("WAV/DT_Clap.wav"),
		Sample("WAV/DT_Closedhat.wav"),
		Sample("WAV/DT_Cowbell.wav"),
		Sample("WAV/DT_Crash.wav"),
		Sample("WAV/DT_Openhat.wav"),
		Sample("WAV/DT_Ride.wav"),
		Sample("WAV/DT_Rimshot.wav"),
		Sample("WAV/DT_Snare.wav"),
		Sample("WAV/DT_Tamborine.wav"),
		Sample("WAV/DT_Tom01.wav"),
		Sample("WAV/DT_Tom02.wav"),
	];

	
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

	cnt = 0
	MIN = -32767
	MAX = 32766

	for i in range(0, len(samples)):
		samples[i].start()

	while True:

		for i in range (0, PERIOD_SIZE):
			
			mix = samples[0].getNextValue()
			mix += samples[1].getNextValue()/2
			mix += samples[2].getNextValue()/4
			mix += samples[4].getNextValue()/3
			mix += samples[5].getNextValue()
			outData[i] = constrain (mix, MIN, MAX)
	
		out.write (outData)


if __name__ == '__main__':
	main()






