import unittest
from unittest.mock import patch

class TestHandle(unittest.TestCase):

    @patch('pyskel.handle.do_handle')
    def test_handle(self, do_handle):
        do_handle()
        self.assertTrue(do_handle.called)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestHandle)
    unittest.TextTestRunner(verbosity=2).run(suite)
