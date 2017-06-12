__author__ = 'Thiago Balbo'
__email__ = 'thiago.dbalbo@gmail.com'
__version__ = '0.1.0'

import logging.config
import os
from pyskel import config
import yaml
import dotenv

# load environment variables
dotenv.load_dotenv('.env')

# load logger
log_directory = config.get_property('LOGDIR')
log_filename = config.get_property('LOGFILENAME')
if not os.path.exists(log_directory):
    os.makedirs(log_directory)
logging_cfg = yaml.safe_load(open(log_filename, 'rt'))
logging.config.dictConfig(logging_cfg)
