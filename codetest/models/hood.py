from sqlalchemy import Column, Integer, String, ForeignKey

from codetest.models.base import BaseModel

class Hood(BaseModel):

	__tablename__ = 'hood'

	id = Column(Integer, primary_key=True)
	business_id = Column(String(30), ForeignKey('business.id'))

	name = Column(String(30))

	def __str__(self):
		return self.name
