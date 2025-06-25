import unittest
from string_utils import *

class TestStringUtils(unittest.TestCase):
    def test1(self):
        self.assertEqual(reverse_string('mochi'), 'ihcom')
    
    def test2(self):
        self.assertEqual(capitalize_string('mochi'), 'Mochi')

    def test3(self):
        self.assertTrue(is_capitalized('Mochi'))
        

if __name__ == '__main__':
    unittest.main()