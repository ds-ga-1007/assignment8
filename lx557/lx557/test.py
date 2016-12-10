'''
Created on 2016.11.28

@author: xulei
'''

import unittest
import numpy as np
from methods import *
from input_object import *

class TestClass(unittest.TestCase):
    def setUp(self):
        pass
    
    def test_ListPos(self):
        self.assertSequenceEqual(ListPos('[1,10,20,1000]').int_list, [1,10,20,1000])
        
        with self.assertRaises(ValueError):
            ListPos('[ssasd,0]').int_list
            
        with self.assertRaises(listException):
            ListPos('bdieowmsl')
            
        with self.assertRaises(divisionException):
            ListPos('[1,3,33,55]').int_list
            
if __name__ =='__main__':
    unittest.main()
        
