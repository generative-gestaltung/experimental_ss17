#! /usr/bin/python
import RPi.GPIO as GPIO
import tornado.ioloop
import tornado.web
import tornado.websocket


GPIO.setmode (GPIO.BOARD)
GPIO.setup (17, GPIO.OUT)
GPIO.setup (27, GPIO.OUT)
GPIO.setup (22, GPIO.OUT)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

class WSHandler(tornado.websocket.WebSocketHandler):
    def open (self):
        print "WS connection open"
    def on_message (self, message):
        print(message)
        #self.write_message(u"xxx")


favicon_path = '.'
static_path = './static'

handlers = [
            (r'/favicon.ico', tornado.web.StaticFileHandler, {'path': favicon_path}),
            (r'/static/(.*)', tornado.web.StaticFileHandler, {'path': static_path}),
            (r'/', MainHandler),
            (r'/ws', WSHandler)
]


if __name__ == "__main__":
    app = tornado.web.Application(handlers)
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
