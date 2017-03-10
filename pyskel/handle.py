"""Module handler"""
import logging
from pyskel.handler import do_handler

logger = logging.getLogger(__name__)

def do_handle(event, context):
    """Do handler"""
    logger.info('do handler called')
    do_handler.handle()
