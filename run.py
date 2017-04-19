"""Run project"""
import logging
import sys
import os
import fire
from log import log

log.setup_logging(default_path='log/config.yml') # config file load must come before getting logger
logger = logging.getLogger(__name__)
ENVIRONMENTS = ['local', 'qa', 'prod']


def main(handler, env):
    """"
    Commandline interface to configure how pyskel should run.

    :param handler: handler to be executed
    :param env: environment (one of: local | qa | prod)
    """
    logger.info('Setting environment...')
    if env in ENVIRONMENTS:
        os.environ['ENVIRONMENT'] = env
    else:
        logger.error('Wrong environment choice=%s.', env)
        sys.exit(1)

    try:
        logger.info('Assigning handler...')
        # later import to avoid loading all modules before adding environment variable to environment
        # to avoid any global variable loading None or from config file
        from pyskel import handle
        _handler = getattr(handle, handler)
    except AttributeError:
        logger.error('Handler not found.', exc_info=True)
        sys.exit(1)

    logger.info('All set up. Calling handler...')
    event, context = None, None
    return _handler(event, context)


if __name__ == '__main__':
    fire.Fire(main)
