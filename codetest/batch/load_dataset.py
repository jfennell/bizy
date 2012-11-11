"""
Batch to load data from the academic dataset JSON
into our app's DB.
"""

import json
import optparse

from codetest.batch.base import BaseBatch
from codetest import models

class LoadDataset(BaseBatch):
	def define_opts(self):
		super(LoadDataset, self).define_opts()
		opts = optparse.OptionGroup(self.option_parser, 'Load Dataset Options')
		opts.add_option(
			'--path',
			default='data/yelp_academic_dataset.json',
			help='Path to the file to load data from (default: %default)'
		)
		opts.add_option(
			'--dry-run',
			action='store_true',
			default=False,
			help='Do not load data into the DB (default: %default)')
		self.option_parser.add_option_group(opts)

	def run(self):
		# We are going to buffer review data till all users and businesses
		# are loaded, so that the parents are guaranteed to exist
		review_data = []
		with open(self.options.path) as f:
			for line_no, line in enumerate(f):
				entry = json.loads(line)
				self.log.debug('Loading line %d, type %s' % (
					line_no, entry['type']))

				if entry['type'] == models.Review.TYPE:
					# objs = models.Review.from_dict(entry)
					review_data.append(entry)
					continue
				elif entry['type'] == models.Business.TYPE:
					objs = self._setup_business(entry)
				elif entry['type'] == models.User.TYPE:
					objs = models.User.from_dict(entry)
				else:
					raise ValueError(
						'Line %d, Unknown object type: "%s"' % (
							line_no, data['type'],))

				if not objs:
					raise ValueError('Line %d, model building failed' % (line_no,))

				for obj in objs:
					self.session.add(obj)

				# XXX add baching later
				# ...not sure it is safe w/ the stuff I do to add schools...
				self._safe_commit()

		self.log.debug('Starting to load reviews')
		for review_num, review_datum in enumerate(review_data):
			self.log.debug('Loading review num %d' % (review_num,))
			objs = models.Review.from_dict(review_datum)
			for obj in objs:
				self.session.add(obj)

			if review_num and review_num % 50 == 0:
				self._safe_commit()
		self._safe_commit()


	def _setup_business(self, biz_entry):
		objs = models.Business.from_dict(biz_entry)
		school_names = biz_entry['schools']
		existing_schools = self.session.query(
			models.School
		).filter(
			models.School.name.in_(school_names)
		).all()
		new_schools = []
		existing_school_names = set(s.name for s in existing_schools)
		for school_name in (set(school_names) - existing_school_names):
			school = models.School()
			school.name = school_name
			new_schools.append(school)
		biz = objs[0] # XXX: ugh... depending on business being first...
		biz.schools = existing_schools + new_schools
		objs += new_schools
		return objs



if __name__ == '__main__':
	LoadDataset().run()