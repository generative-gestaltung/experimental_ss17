import sys
import time
import getopt
import alsaaudio
import math
import wave
from array import array



def main():

	device = 'default'

	PERIOD_SIZE = 16



	out = alsaaudio.PCM(alsaaudio.PCM_PLAYBACK, device=device)
	out.setchannels(1)
	out.setrate(22500)
	out.setformat(alsaaudio.PCM_FORMAT_S16_LE)

 	out.setperiodsize (PERIOD_SIZE)


	inp = alsaaudio.PCM (alsaaudio.PCM_CAPTURE, device=device)
	inp.setchannels(1)
	inp.setrate(22500)
	inp.setformat(alsaaudio.PCM_FORMAT_S16_LE)
	

	while True:
		l, data = inp.read()
	
		if l:
			out.write(data)


if __name__ == '__main__':

	main()
