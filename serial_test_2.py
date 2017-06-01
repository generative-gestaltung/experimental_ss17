import time
import serial


def playSound (data):
    

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

vals = [0,0,0,0]
cnt = 0
while 1 :
    time.sleep(0.1)
    out = ""

    while ser.inWaiting() > 3:
        out = ord(ser.read(1))
        if (out==127):
            cnt = 0
        if (cnt==2):
            playSound(vals)
        if (cnt>3):
            cnt = 3
        vals[cnt] = out
        cnt = (cnt+1)
