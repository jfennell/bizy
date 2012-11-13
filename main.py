import os

import tornado.ioloop
import tornado.web

import codetest.handlers
import codetest.models
import codetest.views


settings = dict(
	debug=True,
	template_path=os.path.join(os.path.dirname(__file__), "codetest/views")
)
print settings

print codetest.handlers.urls

application = tornado.web.Application(
    codetest.handlers.urls,
    **settings
)

if __name__ == "__main__":
    application.listen(8888)
    codetest.models.setup_model()
    codetest.views.setup_loader()
    tornado.ioloop.IOLoop.instance().start()

