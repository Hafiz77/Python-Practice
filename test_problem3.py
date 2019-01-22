import unittest
from problem3 import lca

class TestLeastCommonAncestor(unittest.TestCase):

    def test_empty(self):
        with self.assertRaises(ValueError):
            lca(None, None)

    def test_invalid_with_string(self):
        with self.assertRaises(ValueError):
            lca("", "")

    def test_invalid_with_int(self):
        with self.assertRaises(ValueError):
            lca(22, 33)        

    

if __name__ == '__main__':
    unittest.main()  
