"""
Handlers dealing with displaying school data to the user.
"""

import tornado.web
# from codetest.handlers.base import BaseHandler

from codetest import models
from codetest import views

class AllSchoolHandler(tornado.web.RequestHandler):

	url_pattern = r'^/school/all$'

	def get(self):
		session = models.Session()
		schools = session.query(models.School).all()
		schools.sort(key=lambda s: s.name)
		session.close()

		self.write(
			views.render(
				"all_school.html",
				env=dict(
					schools=schools,
				)
			)
		)

class OneSchoolHandler(tornado.web.RequestHandler):

	url_pattern = r'^/school$'

	def get(self):
		school_id = self.get_argument('id')

		session = models.Session()
		school = session.query(models.School).filter_by(id=school_id).first()
		if school is None:
			self.send_error(status_code=400)

		self.write(
			'<!DOCTYPE html><html><body>%s</body></html>' % (school.name,)
		)
