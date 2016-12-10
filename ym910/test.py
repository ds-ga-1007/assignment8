import unittest
import numpy as np
from investment import *
from input_error import *

class TestInv(unittest.TestCase):
    #test if the input value is valid (positive integer).
    def test_input(self):
        with self.assertRaises(ValueError):
            input_positions("[-2,1,10,100]")
        with self.assertRaises(ValueError):
            input_trials(-10)
    #test if the outcome and result function produce correct result.
    def test_outcome(self):
        inv=user_input(10,10000)
        result=outcome(10,10000)
        self.assertEqual(len(result),10000)
        self.assertTrue(result.all()<=1)
        self.assertTrue(result.all()>=-1)

if __name__=="__main__":
    unittest.main()
