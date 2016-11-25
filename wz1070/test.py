import unittest
from assignment8 import get_positions

class ExceptionTest(unittest.TestCase):
    
    def test_3_positions(self):
        self.assertEqual(get_positions('[1, 10, 100]'), [1, 10, 100])
    
    def test_3_positions_reverse(self):
        self.assertEqual(get_positions('[100, 10, 1]'), [100, 10, 1])

if __name__ == '__main__':
    unittest.main()