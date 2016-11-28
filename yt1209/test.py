'''
Created on Nov 26, 2016

@author: Yovela
'''
import unittest
from read_input import *


class Test(unittest.TestCase):

             
    def test_input_invalid(self):
        with self.assertRaises(ValueError):
            read_position("[1,-2,10,100]")
        with self.assertRaises(ValueError):
            read_position("[1,3.6,7.8,100]")
        with self.assertRaises(ValueError):
            read_num_trials(-1000)
        with self.assertRaises(ValueError):
            read_num_trials(3.5)     


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()