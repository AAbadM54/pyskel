"""test.test_handle"""
from pyskel import handle


def test_do_handle():
    event, context = None, None
    resp = handle.do_handle(event, context)
    assert resp is None
