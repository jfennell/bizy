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
		with open(self.options.path) as f:
			for line_no, line in enumerate(f):
				entry = json.loads(line)

				if entry['type'] == models.Review.TYPE:
					obj = models.Review.from_dict(entry)
				elif entry['type'] == models.Business.TYPE:
					obj = models.Business.from_dict(entry)
				elif entry['type'] == models.User.TYPE:
					obj = models.User.from_dict(entry)
				else:
					raise ValueError(
						'Line %d, Unknown object type: "%s"' % (
							line_no, data['type'],))

				if obj is None:
					raise ValueError('Line %d, model building failed' % (line_no,))

				self.session.add(obj)

				# XXX add baching later
				self._safe_commit()



if __name__ == '__main__':
	LoadDataset().run()