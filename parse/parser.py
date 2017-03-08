import argparse
import os

class Parser:
    def export_arguments(self):
        parser = argparse.ArgumentParser(description='python project skeleton')
        parser.add_argument('-e', '--env', dest='ENVIRONMENT', default='local',
                            choices=('prod', 'qa', 'local'), help='current environment')
        args = parser.parse_args()
        # export arguments
        for key, value in args.__dict__.items():
            os.environ[key] = value

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Parser, cls).__new__(cls)
        return cls.instance
