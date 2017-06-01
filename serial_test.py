import time
import serial
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
	Sample ("WAV/DT_Cowbell.wav"),
	Sample ("WAV/DT_Crash.wav"),
	Sample ("WAV/DT_Ride.wav"),
	Sample ("WAV/DT_Tamborine.wav")
]

PERIOD_SIZE = 1024
audio.initAudio (PERIOD_SIZE)
samples[0].start()
samples[1].start()
samples[2].start()
samples[3].start()





# configure the serial connections (the parameters differs on the device you are connecting to)
ser = serial.Serial(
    port='/dev/cu.usbmodem621',
    baudrate=9600,
    parity=serial.PARITY_ODD,
    stopbits=serial.STOPBITS_TWO,
    bytesize=serial.SEVENBITS
)

ser.isOpen()

input=1

def sendData (channel, value):
    print(channel)
    print(value)
    print("......")

while 1 :


    # READ SERIAL
    #time.sleep(0.1)
    out = ""

    while ser.inWaiting() > 0:
        c = ser.read(1)
        out += c

        # new line, data complete, get channeldata
        if (c=='\n'):
            values = out.split(" ")
            for i in range(0,len(values)):
                if (len(values[i])>2):
                    sendData (i, int(values[i]))

            out = ""

    # WRITE AUDIO DATA
    for i in range (0, PERIOD_SIZE):
        sum = samples[0].getNextValue()*0.2
    	sum += samples[1].getNextValue()*0.2
    	sum += samples[3].getNextValue()*0.2
    	sum += samples[4].getNextValue()*0.2

    audio.writeSample (int(sum))
