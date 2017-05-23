import sys
import time
import getopt
import alsaaudio
import math
from array import array





def calc (ph) :
	return int (math.sin(ph*0.15 + math.sin(ph*0.001)*200)*127+128)
	


def main():

	device = 'default'
	f = open ("star_wars.wav", 'rb')
	PERIOD_SIZE = 128



	out = alsaaudio.PCM(alsaaudio.PCM_PLAYBACK, device=device)


	out.setchannels(1)
	out.setrate(22500)
	out.setformat(alsaaudio.PCM_FORMAT_U8)

 	out.setperiodsize(PERIOD_SIZE)


	ph = 0


	while True:

	 	data = array("B")
		for i in range (0, PERIOD_SIZE):
			data.append (calc(ph))
			ph += 1
		

		out.write(data)




if __name__ == '__main__':

	main()
