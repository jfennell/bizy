"""
Module providing convenience and generator functionality to the
other handler classes.
"""

from codetest import models
from codetest import views
from codetest.handlers.base import BaseHandler


def make_get_one_handler(model):
	"""
	Generates a handler that will serve up a json version of a given model.

	The model must implement a `dict` property that returns a JSON-encodeable
	dict representation of the object.

	The generated handler has a single required parameter (id). It looks up
	objects directly by their id.
	"""

	class GetOneHandler(BaseHandler):

		def get(self):
			id_ = self.get_argument('id')

			session = models.Session()
			obj = session.query(model).filter_by(id=id_).first()
			if obj is None:
				self.send_error(status_code=400)

			self.render_as_json(obj.dict)
			session.close()

	return GetOneHandler


def make_get_all_handler(model, sort_items=True):
	"""
	Generates a handler to serve a page listing all rows of a given model.

	The model must implement `name` for display & sorting, and `codetest_url` for 
	the view to link to a single instance of the object. XXX: Get rid of this...

	The view requires the model to implement the properties `codetest_url` and
	`name`.
	"""

	class GetAllHandler(BaseHandler):

		def get(self):
			session = models.Session()
			objs = session.query(model).all()
			if sort_items:
				objs.sort(key=lambda b: b.name)
			session.close()

			# try:
			# 	out = reverse_url(objs[0].__tablename__, objs[0].id)
			# except Exception:
			# 	import pdb; pdb.set_trace()
			# 	print 'hi'
			# print out

			self.render(
				"all.html",
				objs=objs,
			)
	return GetAllHandler