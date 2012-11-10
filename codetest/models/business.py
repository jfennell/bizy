from sqlalchemy import Column, Integer, String, Boolean, Float

from codetest.models.base import BaseModel

class Business(BaseModel):
	"""Object to keep track of businesses"""
	TYPE = 'business'

	__tablename__ = 'business'

	id = Column(String, primary_key=True)

	name = Column(String(50), nullable=False)
	hoods = Column(String(100)) # how to handle a list?
	full_address = Column(String(70))
	city = Column(String(30))
	state = Column(String(3))
	latitude = Column(Float)
	longitude = Column(Float)
	stars = Column(Float)
	review_count = Column(Integer)
	photo_url = Column(String(50))
	categories = Column(String(100)) # XXX
	is_open = Column(Boolean)
	schools = Column(String(100))  #XXX
	url = Column(String(50))

	@classmethod
	def from_dict(cls, data):
		if data['type'] != cls.TYPE:
			return None

		biz = cls()
		biz.name = data['name']
		biz.hoods = str(data['neighborhoods'])
		biz.full_address = data['full_address']
		biz.city = data['city']
		biz.state = data['state']
		biz.latitude = data['latitude']
		biz.longitude = data['longitude']
		biz.stars = data['stars']
		biz.review_count = data['review_count']
		biz.photo_url = data['photo_url']
		biz.categories = str(data['categories'])
		biz.is_open = data['open']
		biz.schools = str(data['schools'])
		biz.url = data['url']
		return biz