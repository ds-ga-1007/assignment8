'''
Created on Nov 27, 2016

@author: Akash
'''

import sys
sys.path.append('..')

import unittest
from investment_main import investmnt

class Test(unittest.TestCase):  #checks for all possible incorrect inputs for the position values and number of trails
    def setUp(self):
        self.test_position = investmnt()
    
    def test_check_positions_list_incomplete_denominations_1(self):
        self.test_position.check_valid_position_list('[1,10,100]', 0)
        self.assertEqual(self.test_position.valid_input, 0)
    
    def test_check_positions_list_incomplete_denominations_2(self):
        self.test_position.check_valid_position_list('[1,10]', 0)
        self.assertEqual(self.test_position.valid_input, 0)
    
    def test_check_positions_list_incomplete_denominations_3(self):
        self.test_position.check_valid_position_list('[1]', 0)
        self.assertEqual(self.test_position.valid_input, 0)
    
    def test_check_positions_list_incomplete_denominations_4(self):
        self.test_position.check_valid_position_list('[1,10,100,10000,100,10,1]', 0)
        self.assertEqual(self.test_position.valid_input, 0)
    
    def test_check_positions_list_invalid_format(self):
        self.test_position.check_valid_position_list('10 shares', 0)
        self.assertEqual(self.test_position.valid_input, 0)
    
    def test_check_positions_list_invalid_format_1(self):
        self.test_position.check_valid_position_list('10 shares', 0)
        self.assertEqual(self.test_position.valid_input, 0)
    
    def test_check_positions_list_invalid_format_2(self):
        self.test_position.check_valid_position_list('10,100,1000', 0)
        self.assertEqual(self.test_position.valid_input, 0)
    
    def test_check_positions_list_invalid_format_3(self):
        self.test_position.check_valid_position_list('oneshare', 0)
        self.assertEqual(self.test_position.valid_input, 0)
        
    def test_check_positions_list_invalid_format_4(self):
        self.test_position.check_valid_position_list('[1,10,100,thousand]', 0)
        self.assertEqual(self.test_position.valid_input, 0)
        
    def test_check_positions_list_no_brackets(self):
        self.test_position.check_valid_position_list('1,10,100,1000', 0)
        self.assertEqual(self.test_position.valid_input, 0)
    
    def test_invalid_num_trials_1(self):
        self.test_position.check_valid_num_trials('0', 0)
        self.assertEqual(self.test_position.valid_input, 0)
    
    def test_invalid_num_trials_2(self):
        self.test_position.check_valid_num_trials('-100', 0)
        self.assertEqual(self.test_position.valid_input, 0)
        
    def test_num_trial_as_a_string(self):
        self.test_position.check_valid_num_trials('hundred', 0)
        self.assertEqual(self.test_position.valid_input, 0)
    
    
       
        


if __name__ == "__main__":
    unittest.main()