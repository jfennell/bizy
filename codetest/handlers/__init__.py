from codetest.handlers.test import MainHandler
from codetest.handlers.school import AllSchoolHandler
from codetest.handlers.school import OneSchoolHandler

handlers = [
	MainHandler,
	AllSchoolHandler,
	OneSchoolHandler,
]
urls = [(h.url_pattern, h) for h in handlers]
