"""Module handler"""
import logging
from pyskel.handler import do_handler

logger = logging.getLogger(__name__)

def default_handle():
    logger.info('default handler called')

def do_handle():
    logger.info('do handler called')
    do_handler.handle()

if __name__ == '__main__':
    do_handle()
