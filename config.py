import logging
import configparser
import argparse
import sys

DEFAULT_ENVIRONMENT = 'local'
logger = logging.getLogger(__name__)

# if unittest is in the command executed avoid parsing arguments
# because those are not the default arguments expected by this module
if not any(True for arg in sys.argv if 'unittest' in arg):
    parser = argparse.ArgumentParser(description='<edit:your module description>')
    parser.add_argument('-e', '--env', dest='Environment', default='local',
                        choices=('prod', 'qa', 'local'), help='current environment')
    args = parser.parse_args()
    environment = args.Environment
else:
    environment = DEFAULT_ENVIRONMENT

config_vars = configparser.ConfigParser()
config_vars.read('config.ini')


def get_property(name, default=None):
    if config_vars:
        return config_vars.get(environment, name, fallback=default)
    return default
