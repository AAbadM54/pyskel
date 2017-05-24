"""Module handler"""
import logging
from pyskel.service import do

logger = logging.getLogger(__name__)


def do_handle(event, context):
    """Do handler"""
    logger.info('do_handler called')
    do.main(event, context)
