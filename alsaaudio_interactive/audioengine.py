import sys
import time
import getopt
import alsaaudio
import math
import wave
import struct
from func import *
from array import array




class Sample:
	def __init__(self, fname, loop=False):

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
		self.pos = 0
		self.speed = 1
		self.loop = loop
		self.running = False


	def setSpeed (self, speed):
		self.speed = speed

	def start (self):
		
		self.pos = 0
		self.running = True


	def getNextValue (self):

		ret = 0
		'''
		if (self.running):
			ret = self.datL[self.pos]
			self.pos += 1
		
			if (self.pos >= self.len):
				self.pos = 0
				if (self.loop==False):
					self.running = False

		'''

		self.pos = (self.pos+1) % self.len
		ret = self.datL[self.pos]

		return ret




_out = None
_outData = None
_cnt = 0
PERIOD_SIZE = 0
MIN = -32000
MAX =  32000


def initAudio (periodSize):
	

	global PERIOD_SIZE
	global _out
	global _outData

	PERIOD_SIZE = periodSize


	_out = alsaaudio.PCM(alsaaudio.PCM_PLAYBACK, device="default")
	_out.setchannels(1)
	_out.setrate(44100)

	# out format little endian signed short
	_out.setformat(alsaaudio.PCM_FORMAT_S16_LE)
 	_out.setperiodsize(PERIOD_SIZE)

	# outdata array in signed short
	_outData = array("h")

	# init array of period size
	for i in range (0, PERIOD_SIZE):
		_outData.append(0)



def writeSample (s):

	global MIN
	global MAX
	global _out
	global _outData
	global _cnt

	_outData[_cnt] = constrain (s, MIN, MAX)
	_cnt = (_cnt+1) % PERIOD_SIZE

	if (_cnt==0):
		_out.write (_outData)


class AudioDevice:

	def __init__(self, periodSize):

		device = 'default'
		self.PERIOD_SIZE = periodSize
		self.MIN = -32767
		self.MAX =  32766

		self.out = alsaaudio.PCM(alsaaudio.PCM_PLAYBACK, device=device)
		self.out.setchannels(1)
		self.out.setrate(44100)

		# out format little endian signed short
		self.out.setformat(alsaaudio.PCM_FORMAT_S16_LE)
 		self.out.setperiodsize(self.PERIOD_SIZE)


		# outdata array in signed short
		self.outData = array("h")

		# init array of period size
		for i in range (0, self.PERIOD_SIZE):
			self.outData.append(0)

		self.cnt = 0

	def writeSample (self, s):

		self.outData[self.cnt] = constrain (s, self.MIN, self.MAX)
		self.cnt = (self.cnt+1) % self.PERIOD_SIZE

		if (self.cnt==0):
			#print("w")
			self.out.write (self.outData)

