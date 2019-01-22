import unittest
from problem1 import print_depth



class TestPrintDictKeys(unittest.TestCase):

    def test_empty(self):
        self.assertAlmostEqual(print_depth({}), None)

    def test_bad_data_with_string(self):
        with self.assertRaises(ValueError):
            print_depth("")

    def test_bad_data_with_int(self):
        with self.assertRaises(ValueError):
            print_depth(1)        

    

if __name__ == '__main__':
    unittest.main()
