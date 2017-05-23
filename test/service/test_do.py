import unittest
from unittest.mock import patch
from pyskel.service import do


class TestDoMethods(unittest.TestCase):

    def test_do_something(self):
        self.assertTrue(do.do_something([]))
        self.assertFalse(do.do_something({}))
        self.assertFalse(do.do_something(None))

    @patch('pyskel.service.do.run')
    def test_run(self, run):
        run()
        self.assertTrue(run.called)

    @patch('pyskel.service.do.main')
    def test_main(self, main):
        main()
        self.assertTrue(main.called)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestDoMethods)
    unittest.TextTestRunner(verbosity=2).run(suite)
