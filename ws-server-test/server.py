import tornado.ioloop
import tornado.web
import tornado.websocket

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

class WSHandler(tornado.websocket.WebSocketHandler):

    connections = set()

    def open (self):
        self.connections.add(self)
        print "WS connection open "
        [con.write_message("1") for con in self.connections]

    def on_message (self, message):
        print ("msg")
        if message=="on_g":
            [con.write_message("1") for con in self.connections]
        if message=="off_g":
            [con.write_message("0") for con in self.connections]



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
