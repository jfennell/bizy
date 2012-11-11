from sqlalchemy import Column, Integer, String, ForeignKey

from codetest.models.base import BaseModel

class School(BaseModel):
	"""Represents an individual school. """
	#XXX:Maybe should be in a config file...

	__tablename__ = 'school'

	id = Column(Integer, primary_key=True)
	name = Column(String(30))

	def __str__(self):
		return self.name
