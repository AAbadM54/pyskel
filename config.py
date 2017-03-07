import logging
import configparser
import sys
import os
from parse.parser import Parser

logger = logging.getLogger(__name__)
DEFAULT_ENV = 'local'

# if unittest is in the command executed avoid parsing arguments
# because those are not the default arguments expected by this module
if 'test' not in sys.argv:
    parser = Parser()
    parser.export_arguments()

cfg = configparser.ConfigParser()
cfg.read('config.ini')

env = os.getenv('ENVIRONMENT', DEFAULT_ENV)
logger.info('Environment: %s', env)

def get_property(name, default=None):
    return os.getenv(name, cfg.get(env, name, fallback=default))
