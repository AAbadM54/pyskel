__author__ = 'Thiago Balbo'
__email__ = 'thiago.dbalbo@gmail.com'
__version__ = '0.1.0'

import dotenv
from log import log

# load environment variables
dotenv.load_dotenv('.env')

# config file load must come before getting logger
log.setup_logging(default_path='log/config.yml')
