"""Do something"""
import logging
import config

logger = logging.getLogger(name=__name__)

def do_something(p):
    if isinstance(p, list):
        return True
    return False

def run():
    """Run"""
    logger.info('run')

    varname = 'Port'
    logger.info('var %s=%s', varname, config.get_property(varname))


if __name__ == '__main__':
    run()
