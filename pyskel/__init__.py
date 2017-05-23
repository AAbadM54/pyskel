__version__ = '0.1.0'

from log import log
# config file load must come before getting logger
log.setup_logging(default_path='log/config.yml')
