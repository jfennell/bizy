from codetest.handlers.test import MainHandler
from codetest.handlers.school import AllSchoolHandler
from codetest.handlers.school import OneSchoolHandler
from codetest.handlers.business import AllBusinessHandler
from codetest.handlers.business import OneBusinessHandler

handlers = [
	MainHandler,
	AllSchoolHandler,
	OneSchoolHandler,
	AllBusinessHandler,
	OneBusinessHandler,
]
urls = [(h.url_pattern, h) for h in handlers]
