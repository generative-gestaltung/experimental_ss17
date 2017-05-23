import math

TWO_PI = 2*math.pi

def sin (ph):
	return math.sin(ph)

def saw (ph):
	return 2*(ph % (TWO_PI)) / TWO_PI - 1


def sq (ph):
	v = sin(ph)
	if (v>0):
		return 1
	return -1

def pulse (ph, pw):
	v = saw(ph)
	if (v>pw):
		return 1
	return -1
