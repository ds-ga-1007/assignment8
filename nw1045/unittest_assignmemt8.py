'''
Unittest 
Created on Nov 21, 2016
Last Modified        : 
Version        : 1.0
@author: Nan Wu
@email: nw1045@nyu.edu
'''
import unittest
from investment import simulation
from investment_simulation import reading_in
from UserDefinedError import InputError

class Test(unittest.TestCase):
    def test_simulation(self):
        '''
        Test the simulation class
        '''
        self.assertIn(simulation(1,1000).outcome(),[0,2000])
        self.assertIn(simulation(10,100).outcome(),list(range(0,2002,200)))
        self.assertIn(simulation(100,10).outcome(),list(range(0,2002,20)))
        self.assertIn(simulation(1000,1).outcome(),list(range(0,2001,2)))
        self.assertEqual(len(simulation(1000,1).outcome_total(10)),10)
    def test_reading_in(self):
        '''
        Test the reading_in function
        '''
        with self.assertRaises(InputError):
            reading_in('[1]','a')
        with self.assertRaises(InputError):
            reading_in('[]','1')  
        with self.assertRaises(InputError):
            reading_in('[]','-1')        
        self.assertSequenceEqual(reading_in('[1,10,100]','100'),[[1,10,100],100])
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()