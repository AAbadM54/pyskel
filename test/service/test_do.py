import unittest
from pyskel.service import do

class TestStringMethods(unittest.TestCase):

    def test_do_something(self):
        self.assertTrue(do.do_something([]))
        self.assertFalse(do.do_something({}))
        self.assertFalse(do.do_something(None))

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
    unittest.TextTestRunner(verbosity=2).run(suite)
