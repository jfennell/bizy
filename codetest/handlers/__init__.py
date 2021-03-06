from tornado.web import URLSpec

from codetest.handlers.test import MainHandler, TestHandler
from codetest.handlers.simple import BizReviewsHandler, UserReviewsHandler, BizUsersHandler, SchoolBusinessesHandler
from codetest.handlers._helper import make_get_one_handler, make_get_all_handler
from codetest import models

def _one_and_all_urlspecs(model):
	return [
		URLSpec(
			r'^/%s$' % (model.__tablename__,),
			make_get_one_handler(model),
			name=model.__tablename__,
		),
		URLSpec(
			r'^/%s/all$' % (model.__tablename__,),
			make_get_all_handler(model),
			name='all_%s' % (model.__tablename__,)
		),
	]

urls = [
	URLSpec(r'^/$', MainHandler, name='root'),
	URLSpec(r'^/test$', TestHandler, name='test'),
	URLSpec(r'^/review$', make_get_one_handler(models.Review), name='review'),
	URLSpec(r'^/business/reviews$', BizReviewsHandler, name='biz_reviews'),
	URLSpec(r'^/user/reviews$', UserReviewsHandler, name='user_reviews'),
	URLSpec(r'^/business/users$', BizUsersHandler, name='biz_users'),
	URLSpec(r'^/school/businesses$', SchoolBusinessesHandler, name='school_businesses'),
]

urls.extend(_one_and_all_urlspecs(models.Business))
urls.extend(_one_and_all_urlspecs(models.User))
urls.extend(_one_and_all_urlspecs(models.School))