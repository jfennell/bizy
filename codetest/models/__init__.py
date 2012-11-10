from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from codetest.models.base import BaseModel
from codetest.models.user import User
from codetest.models.review import Review
from codetest.models.business import Business

engine = None
Session = None

def setup_model():
	global engine
	global Session

	if engine is None and Session is None:
		engine = create_engine('sqlite:///codetest.sqlite', echo=False)
		BaseModel.metadata.create_all(engine)
		Session = sessionmaker(bind=engine)