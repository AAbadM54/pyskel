""" pyskel.cli
"""
import os
import sys
import logging
import json
import click
from pyskel import handle


class DictParamType(click.ParamType):
    """Custom Click Type"""
    name = 'dict'

    def convert(self, value, param, ctx):
        try:
            parsed = json.loads(value)
            if isinstance(parsed, dict):
                return parsed
            raise ValueError
        except ValueError:
            self.fail('JSON parameter could not be cast to dictionary')


@click.command()
@click.argument('handler', type=click.STRING)
@click.option('--env', default=os.getenv('ENVIRONMENT', 'local'),
              type=click.Choice(['local', 'qa', 'prod']),
              help='env variable: local, qa, or prod. defaults to local')
@click.option('--event', '-e', type=DictParamType())
@click.option('--context', '-c', type=DictParamType())
def main(handler, env, event, context):
    """Define how pyskel will execute."""
    logger = logging.getLogger(__name__)

    logger.info('Setting up environment variable...')
    os.environ['ENVIRONMENT'] = env

    try:
        logger.info('Assign handler...')
        _handler = getattr(handle, handler)
    except AttributeError:
        logger.error('Handler not found.', exc_info=True)
        sys.exit(1)

    logger.info('All set up: handler=%s env=%s', handler, env)
    logger.info('Calling handler...')
    return _handler(event, context)


if __name__ == '__main__':
    main()
