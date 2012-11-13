import json

from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship

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

	reviews = relationship('Review', backref='user')

	@classmethod
	def from_dict(cls, data):
		if data['type'] != cls.TYPE:
			return []

		user = cls()
		user.id = data['user_id']
		user.name = data['name']
		user.review_count = data['review_count']
		user.average_stars = data['average_stars']
		user.useful_votes = data['votes']['useful']
		user.funny_votes = data['votes']['funny']
		user.cool_votes = data['votes']['cool']
		return [user]

	@property
	def dict(self):
		return {
			'type': 'user',
			'user_id': self.id,
			'name': self.name,
			'review_count': self.review_count,
			'average_stars': self.average_stars,
			'votes': {
				'useful': self.useful_votes,
				'funny': self.funny_votes,
				'cool': self.cool_votes,
			}
		}

	@property
	def json(self):
		return json.dumps(self.dict)

	def __str__(self):
		return "[%s] %s: %.1f(%d) %d/%d/%d" % (
			self.id,
			self.name,
			self.review_count,
			self.average_stars,
			self.useful_votes,
			self.funny_votes,
			self.cool_votes
		)