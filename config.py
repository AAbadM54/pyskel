import logging
import configparser
import argparse
import sys
import os

logger = logging.getLogger(__name__)
DEFAULT_ENV = 'local'

# if unittest is in the command executed avoid parsing arguments
# because those are not the default arguments expected by this module
if not any(True for arg in sys.argv if 'unittest' in arg):
    parser = argparse.ArgumentParser(description='<edit:your module description>')
    parser.add_argument('-e', '--env', dest='Environment', default='local',
                        choices=('prod', 'qa', 'local'), help='current environment')
    args = parser.parse_args()

try:
    env = args.Environment
except NameError:
    logger.warning('Commandline arguments not set.')
    env = DEFAULT_ENV
finally:
    logger.info('Environment: %s', env)

cfg = configparser.ConfigParser()
cfg.read('config.ini')

def get_property(name, default=None):
    return args.__dict__.get(name, os.getenv(name, cfg.get(env, name, fallback=default)))
