"""
Association table between businesses and schools.
"""

from codetest.models.base import BaseModel

from sqlalchemy import Table, Integer, ForeignKey, Column

business_school = Table(
	'business_school',
	BaseModel.metadata,
	Column('business_id', Integer, ForeignKey('business.id')),
	Column('school_id', Integer, ForeignKey('school.id')),
)