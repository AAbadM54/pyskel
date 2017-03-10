"""Run project"""
import logging
import sys
import os
import fire
from pyskel import handle

logger = logging.getLogger(__name__)
ENVIRONMENTS = ['local', 'qa', 'prod']


def main(handler, env):
    """"
    Commandline interface to configure how pyskel should run.

    :param handler: handler to be executed
    :param env: environment (one of: local | qa | prod)
    """
    try:
        _handler = getattr(handle, handler)
    except AttributeError:
        logger.error('Handler not found.', exc_info=True)
        sys.exit(1)

    if env in ENVIRONMENTS:
        _env = env
    else:
        logger.warning('Wrong environment choice=%s.', env)
        sys.exit(1)

    os.environ['ENVIRONMENT'] = _env

    event, context = None, None
    return _handler(event, context)


if __name__ == '__main__':
    fire.Fire(main)
