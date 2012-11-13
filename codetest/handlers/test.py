from codetest.handlers.base import BaseHandler

class MainHandler(BaseHandler):

	url_pattern = r"/"

	def get(self):
		self.write("Hello, world")

class TestHandler(BaseHandler):
	def get(self):
		self.render("test.html")