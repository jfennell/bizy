"""
Base handler. Avoids some annoyance of maitaining an overall url list.

XXX Doesn't quite work
"""
import json

import tornado.web

# urls = []

# class HandlerMetaclass(type):
# 	def __new__(mcl, name, bases, attrs):
# 		global urls
# 		cls = type(name, bases, attrs)
# 		print urls
# 		print name
# 		print bases
# 		print attrs
# 		if hasattr(cls, 'url_pattern') and cls.url_pattern is not None:
# 			urls.append(cls.url_pattern, cls)
# 		return cls

# class BaseHandler(tornado.web.RequestHandler):
# 	__metaclass__ = HandlerMetaclass

class BaseHandler(tornado.web.RequestHandler):
	def render_as_json(self, data, indent=2):
		self.set_header('Content-Type', 'application/json')
		self.write(json.dumps(data, indent=indent))
