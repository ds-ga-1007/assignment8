'''This is an test module
   Author:Liwei Song
   NetID:ls4408
   Creation date: 11/28/2016
 '''
import unittest
from assignment8 import *
from simulation import *


'''inheritence from unittest.TestCase'''
class assignment8_Test(unittest.TestCase):
    #test the initial definition of simulation class
    def test_initial(self):
        test_i = simulation([1, 10],1000)     
        self.assertEqual(test_i.position,[1, 10])
        self.assertEqual(test_i.numb, 1000)
    # test  if the length of the simulation is correct or not   
    def test_get_simulation_len(self):
        test_ii = simulation([100, 10],2000) 
        test_ii.get_simulation()
        self.assertEqual(len(test_ii.diff_posit_ret[100]),2000)
        self.assertEqual(len(test_ii.diff_posit_ret[10]),2000)
    
    # test if the daily return is going above or below the [-1,1], possible values
    def test_get_simulation_ret(self):
        test_iii = simulation([1, 10],1000) 
        test_iii.get_simulation()
        self.assertTrue(all(x <=1 for x in test_iii.diff_posit_ret[1]))
        self.assertTrue(all(x >= -1 for x in test_iii.diff_posit_ret[1]))
        self.assertTrue(all(x <=1 for x in test_iii.diff_posit_ret[10]))
        self.assertTrue(all(x >= -1 for x in test_iii.diff_posit_ret[10]))
    #The use of all() function is looked up from the website below:
        #http://stackoverflow.com/questions/20229822/check-if-all-values-in-list-are-greater-than-a-certain-number
    
    # test if an error will be raised for invalid position list input
    def test_correct_input(self):
        with self.assertRaises(inputError):
            correct_input_position('[1,2,3]')
        with self.assertRaises(inputError):
            correct_input_position('')
    # test if an error will be raised for the invalid simulation number
    def test_correct_input_numb(self):
        with self.assertRaises(inputError):
            correct_input_numb('x')
        with self.assertRaises(inputError):
            correct_input_position('')
    
            
if __name__ == '__main__':
    unittest.main()
