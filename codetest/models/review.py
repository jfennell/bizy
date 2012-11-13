import datetime
import json

from sqlalchemy import Column, Integer, String, DateTime, Text, Float, ForeignKey

from codetest.models.base import BaseModel

class Review(BaseModel):
	"""Object to keep track of reviews"""

	TYPE = 'review'
	__tablename__ = 'review'

	id = Column(Integer, primary_key=True)

	business_id = Column(String(30), ForeignKey('business.id'))
	user_id = Column(String(30), ForeignKey('user.id'))
	stars = Column(Integer, nullable=False)
	text = Column(Text, nullable=False)
	date = Column(DateTime, nullable=False)
	useful_votes = Column(Integer, nullable=False, default=0)
	funny_votes = Column(Integer, nullable=False, default=0)
	cool_votes = Column(Integer, nullable=False, default=0)

	@classmethod
	def from_dict(cls, data):
		if data['type'] != cls.TYPE:
			return []

		review = cls()
		review.business_id = data['business_id']
		review.user_id = data['user_id']
		review.stars = data['stars']
		review.text = data['text']
		review.date = datetime.datetime.strptime(data['date'], '%Y-%m-%d').date()
		review.useful_votes = data['votes']['useful']
		review.funny_votes = data['votes']['funny']
		review.cool_votes = data['votes']['cool']
		return [review]

	@property
	def dict(self):
		return {
			'type': 'review',
			'business_id': self.business_id, 
			'user_id': self.user_id,
			'stars': self.stars,
			'text': self.text,
			'date': str(self.date),
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
		return "[%d] (b%s,u%s) %s - %d %d/%d/%d %.40s" % (
			self.id,
			self.business_id,
			self.user_id,
			self.date,
			self.stars,
			self.useful_votes,
			self.funny_votes,
			self.cool_votes,
			self.text,
		)