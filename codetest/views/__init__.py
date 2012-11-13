import tornado.template

loader = None
def setup_loader():
	global loader
	if loader is None:
		loader = tornado.template.Loader('codetest/views')