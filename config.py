"""Configuration Handler"""
import configparser
import os

_cfg = configparser.ConfigParser()
_cfg.read('config.ini')

def get_property(name, default=None):
    """Fallback rule to get property value"""
    return os.getenv(name, _cfg.get(os.getenv('ENVIRONMENT'), name, fallback=default))
