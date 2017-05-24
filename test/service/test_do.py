"""test.service.test_do"""
from pyskel.service import do


def test_do_something():
    assert do.do_something([]) is True
    assert do.do_something({}) is False


def test_run():
    assert do.run() is None
