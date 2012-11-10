import tornado.web

class MainHandler(tornado.web.RequestHandler):

	url_pattern = r"/"

	def get(self):
		self.write("Hello, world")