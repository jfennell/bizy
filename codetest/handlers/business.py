"""
Handlers dealing with displaying business data to the user.
"""

import tornado.web
# from codetest.handlers.base import BaseHandler

from codetest import models
from codetest import views

class AllBusinessHandler(tornado.web.RequestHandler):

	url_pattern = r'^/biz/all$'

	def get(self):
		session = models.Session()
		bizs = session.query(models.Business).all()
		bizs.sort(key=lambda b: b.name)
		session.close()

		self.write(
			views.render(
				"all_biz.html",
				env=dict(
					bizs=bizs,
				)
			)
		)

class OneBusinessHandler(tornado.web.RequestHandler):

	url_pattern = r'^/biz$'

	def get(self):
		biz_id = self.get_argument('id')

		session = models.Session()
		biz = session.query(models.Business).filter_by(id=biz_id).first()
		if biz is None:
			self.send_error(status_code=400)

		self.write(
			'<!DOCTYPE html><html><body>%s</body></html>' % (biz.name,)
		)
