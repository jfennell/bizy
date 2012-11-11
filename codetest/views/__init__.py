import tornado.template

loader = None
def setup_loader():
	global loader
	if loader is None:
		loader = tornado.template.Loader('codetest/views')

def render(path, env=None):
	"""Convenience method for rendering templates"""
	env = env or {}
	if loader is None:
		setup_loader()
	tmpl = loader.load(path)
	return tmpl.generate(**env)