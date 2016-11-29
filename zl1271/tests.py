'''
Created on Nov 27, 2016

@author: felix
'''
import unittest
import numpy as np
from simu_funcs import *

class Test(unittest.TestCase):

    def test_valid_share_str(self):
        corr_list = ['10,20,30,40','42,32,22,12','10','1,10']
        for this_str in corr_list:
            self.assertEqual(valid_share_str(this_str), True)
            
        wrong_list = ['dfksdaf','9,fgk','9,0,8.','42,32,22,1a2']
        for this_str in wrong_list:
            self.assertEqual(valid_share_str(this_str), False)

    def test_rm_ws(self):
        self.assertEqual(rm_ws(' 1 , 23, 432 ,3 3'), '1,23,432,33')
    
    def test_valid_trial_str(self):
        corr_list = ['10','500','1000','20000']
        for this_str in corr_list:
            self.assertEqual(valid_trial_str(this_str), True)
            
        wrong_list = ['dfksdaf','9,fgk','10.4','-12']
        for this_str in wrong_list:
            self.assertEqual(valid_trial_str(this_str), False)
    
    def test_invest_return(self):
        seed = np.random.randint(9999999)
        np.random.seed(0) 
        return_collector = []
        for ii in np.arange(0,10000):
            this_return = invest_return()
            return_collector.append(this_return)
        np.random.seed(seed) # After test, the random generator should be random again, this idea is adapted from http://nullege.com/codes/show/src@s@t@statsmodels-0.5.0@statsmodels@sandbox@tsa@examples@ex_mle_garch.py/88/numpy.random.seed
        self.assertEqual(np.mean(return_collector), 0.0332) # 0.0332 is calculated for the seed 0
        
    def test_get_invest_return_vec(self):
        seed = np.random.randint(9999999)
        np.random.seed(0) 
        ans_list = [52.0, 20.0, 0.0, 1000.0]
        test_list = [1,10,100,1000]
        result_list = [];
        for value in test_list:
            result_list.append(sum(get_invest_return_vec(value,1000/value)))
        np.random.seed(seed)
        self.assertEqual(result_list, ans_list)
        
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()