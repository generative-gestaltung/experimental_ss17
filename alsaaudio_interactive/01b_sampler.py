import sys
import time
import getopt
import alsaaudio
import math
import wave
from array import array




class Sample:
	def __init__(self, fname):
		wav = wave.open (fname, "rb")
		self.len = wav.getnframes()
		self.data = wav.readframes(self.len)  
		wav.close()

	def play (self, out):
		out.write(self.data)
		

def main():

	device = 'default'

	samples = [
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

	PERIOD_SIZE = 128



	out = alsaaudio.PCM(alsaaudio.PCM_PLAYBACK, device=device)


	out.setchannels(1)
	out.setrate(22500)
	out.setformat(alsaaudio.PCM_FORMAT_S16_LE)

 	out.setperiodsize(PERIOD_SIZE)


	samples[0].play(out)
	samples[1].play(out)
	samples[2].play(out)
	samples[3].play(out)
	samples[4].play(out)
	samples[5].play(out)
	samples[6].play(out)
	samples[7].play(out)
	samples[8].play(out)
	samples[9].play(out)




if __name__ == '__main__':

	main()
