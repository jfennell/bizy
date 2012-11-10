from sqlalchemy import Column, Integer, String, Float

from codetest.models.base import BaseModel

class User(BaseModel):
	"""Object to keep track of users"""
	TYPE = 'user'

	__tablename__ = 'user'

	id = Column(String, primary_key=True)

	name = Column(String(50), nullable=False)
	review_count = Column(Integer, nullable=False, default=0)
	average_stars = Column(Float, nullable=False)
	useful_votes = Column(Integer, nullable=False, default=0)
	funny_votes = Column(Integer, nullable=False, default=0)
	cool_votes = Column(Integer, nullable=False, default=0)

	@classmethod
	def from_dict(cls, data):
		if data['type'] != cls.TYPE:
			return None

		user = cls()
		user.id = data['user_id']
		user.name = data['name']
		user.review_count = data['review_count']
		user.average_stars = data['average_stars']
		user.useful_votes = data['votes']['useful']
		user.funny_votes = data['votes']['funny']
		user.cool_votes = data['votes']['cool']
		return user
