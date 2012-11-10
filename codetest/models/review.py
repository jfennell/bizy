from sqlalchemy import Column, Integer, String, DateTime, Text, Float

from codetest.models.base import BaseModel

class Review(BaseModel):
	"""Object to keep track of reviews"""
	TYPE = 'review'

	__tablename__ = 'review'

	id = Column(Integer, primary_key=True)

	business_id = Column(String(30)) # XXX set up FK relation
	user_id = Column(String(30)) # XXX: Ditto
	stars = Column(Float, nullable=False)
	text = Column(Text, nullable=False)
	date = Column(DateTime, nullable=False)
	useful_votes = Column(Integer, nullable=False, default=0)
	funny_votes = Column(Integer, nullable=False, default=0)
	cool_votes = Column(Integer, nullable=False, default=0)

	@classmethod
	def from_dict(cls, data):
		if data['type'] != cls.TYPE:
			return None

		review = cls()
		review.business_id = data['business_id']
		review.user_id = data['user_id']
		review.stars = data['stars']
		review.text = data['text']
		review.date = datetime.datetime.strptime(data['date'], '%Y-%m-%d').date()
		review.useful_votes = data['votes']['useful']
		review.funny_votes = data['votes']['funny']
		review.cool_votes = data['votes']['cool']
		return review