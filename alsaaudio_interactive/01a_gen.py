import sys
import time
import getopt
import alsaaudio
import math
from array import array
from func import *




def calc (ph) :
	A = 0.5-(saw(ph*0.001)*0.5)
	fm = 0
	f = 0.02
	pw = sin(ph*0.0001)*0.5+0.5


	ret = pulse (ph*f+fm, pw)*A
	ret *= 0.5;


	A = pulse (ph*0.001, 0)*0.5+0.5
 	A = 1
	ret = pulse(ph*f*4,0)*A*0.5

	return int (ret*127+127)
	


def main():

	device = 'default'
	f = open ("star_wars.wav", 'rb')
	PERIOD_SIZE = 2048


	out = alsaaudio.PCM(alsaaudio.PCM_PLAYBACK, device=device)


	out.setchannels(1)
	out.setrate(32000)
	out.setformat(alsaaudio.PCM_FORMAT_U8)

 	out.setperiodsize(PERIOD_SIZE)


	ph = 0
	
 	data = array("B")
	for i in range (0, PERIOD_SIZE):
		data.append(0)
	

	while True:

		for i in range (0, PERIOD_SIZE):
			data[i] = calc(ph)
			ph += 1
		
		out.write(data)




if __name__ == '__main__':

	main()
