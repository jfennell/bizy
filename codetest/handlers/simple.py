from codetest.handlers.base import BaseHandler
from codetest import models

class BizReviewsHandler(BaseHandler):
	def get(self):
		session = models.Session()
		business = self.get_from_model_by_id_arg(session, models.Business)
		self.render_as_json([r.dict for r in business.reviews])
		session.close()

class UserReviewsHandler(BaseHandler):
	def get(self):
		session = models.Session()
		user = self.get_from_model_by_id_arg(session, models.User)
		self.render_as_json([r.dict for r in user.reviews])
		session.close()

class BizUsersHandler(BaseHandler):
	def get(self):
		session = models.Session()
		business = self.get_from_model_by_id_arg(session, models.Business)
		self.render_as_json([u.dict for u in business.users])
		session.close()

class SchoolBusinessesHandler(BaseHandler):
	def get(self):
		session = models.Session()
		school = self.get_from_model_by_id_arg(session, models.School)
		self.render_as_json([b.dict for b in school.businesses])
		session.close()