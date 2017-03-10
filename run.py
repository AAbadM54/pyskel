"""Run project"""
import logging
import sys
import os
import fire

logger = logging.getLogger(__name__)
ENVIRONMENTS = ['local', 'qa', 'prod']


def main(handler, env):
    """"
    Commandline interface to configure how pyskel should run.

    :param handler: handler to be executed
    :param env: environment (one of: local | qa | prod)
    """
    if env in ENVIRONMENTS:
        os.environ['ENVIRONMENT'] = env
    else:
        logger.error('Wrong environment choice=%s.', env)
        sys.exit(1)

    try:
        # later import to void loading all modules before adding environment variable to environment
        # to avoid any global variable loading None or from config file
        from pyskel import handle
        _handler = getattr(handle, handler)
    except AttributeError:
        logger.error('Handler not found.', exc_info=True)
        sys.exit(1)

    event, context = None, None
    return _handler(event, context)


if __name__ == '__main__':
    fire.Fire(main)
