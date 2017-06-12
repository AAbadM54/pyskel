"""test.test_handle"""
from pyskel.handle import do_handle


def test_do_handle():
    resp = do_handle(None, None)
    assert resp is None
