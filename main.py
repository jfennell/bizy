import tornado.ioloop
import tornado.web

import codetest.handlers
import codetest.models

print codetest.handlers.urls
application = tornado.web.Application(
    codetest.handlers.urls
)

if __name__ == "__main__":
    application.listen(8888)
    codetest.models.setup_model()
    tornado.ioloop.IOLoop.instance().start()

