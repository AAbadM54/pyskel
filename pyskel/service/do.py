"""Do something"""
import logging
from pyskel import config

logger = logging.getLogger(name=__name__)


def run():
    """Run module"""
    logger.info('Environment=%s', config.get_property('ENVIRONMENT'))


def main(event, context):
    """Main"""
    run()
