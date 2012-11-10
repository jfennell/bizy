from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from codetest.models.base import Base

engine = None
Session = None

def setup_model():
	global engine
	global Session

	if engine is None and Session is None:
		engine = create_engine('sqlite:///codetest.sqlite', echo=False)
		Base.metadata.create_all(engine)
		Session = sessionmaker(bind=engine)