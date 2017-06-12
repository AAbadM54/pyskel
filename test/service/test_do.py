"""test.service.test_do"""
from pyskel.service import do


def test_run():
    assert do.run() is None
