import tornado.ioloop
import tornado.web
import tornado.websocket
import RPi.GPIO as GPIO
import threading

GPIO.setmode (GPIO.BCM)
GPIO.setup (17, GPIO.OUT)
GPIO.setup (27, GPIO.OUT)
GPIO.setup (22, GPIO.OUT)


def setTimeout (time, f):
	t = threading.Timer(time, f)
	t.start()

def setInterval (time, f):
	def fwrapper ():
		setInterval(time, f)
		f()
	t = threading.Timer(time, fwrapper)
	t.start()

class PinsGame:
	def __init__(self):
		self.pins = [5,6,13,19]
		self.time = [0.05,0.05,0.1,0.1]
		for i in range (0,4):
			GPIO.setup (self.pins[i], GPIO.OUT)

	def fOut (self):
		print("off")
		for i in range(0,4):
			GPIO.output(self.pins[i], GPIO.LOW)

	def trigger (self, pin):
		if (pin>3):
			return
		print(pin)
		GPIO.output (self.pins[pin], GPIO.HIGH)
		setTimeout(self.time[pin], self.fOut)



class PinThread:
    def __init__(self,T):
        self.T = T
        self.on = [0,0,0]
        self.pins = [17,27,22]

    def changeT (self,T):
        self.T = T

    def toggle(self):

        for i in range(0,3):
            if (self.on[i]==0):
                GPIO.output(self.pins[i], GPIO.HIGH)
                self.on[i] = 1
            else:
                GPIO.output(self.pins[i], GPIO.LOW)
                self.on[i] = 0

    def start (self):
        #print(self.T)
    	def fwrapper ():
    		self.start()
    		self.toggle()
    	t = threading.Timer (self.T, fwrapper)
    	t.start()



p = PinThread(0.1)
p.start()

p2 = PinsGame()

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

class WSHandler(tornado.websocket.WebSocketHandler):

    connections = set()
    def open (self):
        self.connections.add(self)
        print "WS connection open "
        #[con.write_message("1") for con in self.connections]

    def on_message (self, message):

        if (message[0]=="b"):
            b = message[1]
            on = message[2]
            print("button")
            print(b)
            print(on)

        if (message[0]=="g"):
			p2.trigger(int(message[1]))

        if (message[0]=="x"):
            val = int(message[1:])

        if (message[0]=="y"):
            val = int(message[1:])

        if (message[0]=="z"):
            val = int(message[1:])
            p.changeT ((val+90)*0.002+0.05)


        '''
        if (self._on==0):
            self._on = 1
            GPIO.output (4, GPIO.HIGH)
        else:
            self._on = 0
            GPIO.output (4, GPIO.LOW)

        if message=="on_g":
            [con.write_message("1") for con in self.connections]
        if message=="off_g":
            [con.write_message("0") for con in self.connections]
        '''


favicon_path = '.'
static_path = './static'

handlers = [
            (r'/favicon.ico', MainHandler),
            (r'/static/(.*)', tornado.web.StaticFileHandler, {'path': static_path}),
            (r'/', MainHandler),
            (r'/ws', WSHandler)
]

'''
def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])
'''

if __name__ == "__main__":
    #app = make_app()
    app = tornado.web.Application(handlers)
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
