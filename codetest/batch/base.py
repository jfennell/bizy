import logging                                                                                                                                                
import optparse
import os
import sys

from codetest import models

# List of log levels getting more noisy as index increases
# We don't list WARNING so that a -v goes ERROR->INFO then INFO->DEBUG
LOG_LEVELS = [logging.ERROR, logging.INFO, logging.DEBUG]
CONSOLE_FORMAT = '%(asctime)s - %(name)-12s: %(levelname)-8s %(message)s'
    
class BaseBatch(object):
    """Base batch class.

    Supports logging, database connections, and option parsing.
    """

    def __init__(self):
        self.log = logging.getLogger(__name__)
        self.option_parser = optparse.OptionParser()
        
        self.initialize()
        
    def initialize(self):
        self.process_opts()
        self._setup_logging()
        self._setup_db()
        
    def process_opts(self, args=None):
        self.define_opts()
        if args is None:
            args = sys.argv[1:]
        self.options, self.args = self.option_parser.parse_args(args=args)

    def define_opts(self):
        base_options = optparse.OptionGroup(self.option_parser, 'Base Batch Options')
        base_options.add_option(
            '-v', '--verbose',
            action='count',
            default=0,
            help='Adjust log level. Multiple options adds more logging.')
        self.option_parser.add_option_group(base_options)

    def _setup_logging(self):
        # Set loggers to DEBUG level so handlers can decide to log or not log
        batch_logger = logging.getLogger(__name__)
        batch_logger.setLevel(logging.DEBUG)
        root_logger = logging.getLogger()
        root_logger.setLevel(logging.DEBUG)

        console = logging.StreamHandler()
        console.setFormatter(logging.Formatter(CONSOLE_FORMAT))
        console.setLevel(LOG_LEVELS[min(self.options.verbose, len(LOG_LEVELS)-1)])
        root_logger.addHandler(console)

    def _setup_db(self):
        models.setup_model()
        self.session = models.Session()

    def _safe_commit(self):
        try:
            self.session.commit()
        except Exception:
            self.log.exception('Failure trying to commit')
            self.session.rollback()
            raise

    def run(self):
        pass    