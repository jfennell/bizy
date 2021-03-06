from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from codetest.models.base import BaseModel

class School(BaseModel):
	"""Represents an individual school. """
	#XXX:Maybe should be in a config file...

	__tablename__ = 'school'

	id = Column(Integer, primary_key=True)
	name = Column(String(30))

	businesses = relationship(
		'Business',
		secondary='business_school',
		backref='school')

	def __str__(self):
		return self.name

	@property
	def dict(self):
		return {
			'id': self.id,
			'name': self.name,
		}


