"""Do something"""
import logging
import config

logger = logging.getLogger(name=__name__)

def do_something(p):
    if isinstance(p, list):
        return True
    return False

def run():
    """Run module"""
    port = 'PORT'
    env = 'ENVIRONMENT'
    logger.info('%s=%s %s=%s', port, config.get_property(port), env, config.get_property(env))

def main(event, context):
    run()
