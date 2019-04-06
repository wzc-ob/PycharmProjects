# -*- encoding:utf-8 -*-
import tornado.ioloop
import tornado.web
class MainHdl(tornado.web.RequestHandler):
    def get(self,uid = '0'):
        self.write('你好，你的uid号是：%s!'%uid)
app = tornado.web.Application([(r'/([0-9]+)',MainHdl)],debug=True)
if __name__ == '__main__':
    app.listen(8888)
    tornado.ioloop.IOLoop.instance().start()