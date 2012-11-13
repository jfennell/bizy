from codetest.handlers.base import BaseHandler

class MainHandler(BaseHandler):

	url_pattern = r"/"

	def get(self):
		self.write("Hello, world")