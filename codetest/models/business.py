from sqlalchemy import Column, Integer, String, Boolean, Float
from sqlalchemy.orm import relationship

from codetest.models.base import BaseModel
from codetest.models.hood import Hood

class Business(BaseModel):
	"""Object to keep track of businesses"""

	TYPE = 'business'	
	__tablename__ = 'business'

	id = Column(String(30), primary_key=True)

	name = Column(String(50), nullable=False)
	hoods = relationship("Hood")
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
	#schools = Column(String(100))  #XXX
	schools = relationship(
		'School',
		secondary='business_school',
		backref='business')
	url = Column(String(50))

	reviews = relationship('Review', backref='business')

	@classmethod
	def from_dict(cls, data):
		if data['type'] != cls.TYPE:
			return []

		biz = cls()
		biz.id = data['business_id']
		biz.name = data['name']
		#biz.hoods = str(data['neighborhoods'])
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
		#biz.schools = str(data['schools'])
		biz.url = data['url']

		hoods = []
		for hood_name in data['neighborhoods']:
			hood = Hood()
			hood.business_id = biz.id
			hood.name = hood_name
			hoods.append(hood)

		return [biz] + hoods

	@property
	def dict(self):
		return {
			'type': 'business',
			'business_id': self.id,
			'name': self.name,
			'neighborhoods': sorted(h.name for h in self.hoods),
			'full_address': self.full_address,
			'city': self.city,
			'state': self.state,
			'latitude': self.latitude,
			'longitude': self.longitude,
			'stars': self.stars,
			'review_count': self.review_count,
			'photo_url': self.photo_url,
			'categories': eval(self.categories), # XXX: Should *not* eval here!!
			'open': self.is_open,
			'schools': sorted(s.name for s in self.schools),
			'url': self.url,
		}

	def __str__(self):
		return "[%s] %s %.1f(%d) [%s]" % (
			self.id,
			self.name,
			self.stars,
			self.review_count,
			self.schools
		)

	@property
	def codetest_url(self):
		return '/biz?id=%s' % (self.id,)