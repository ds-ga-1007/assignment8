# -*- coding: utf-8 -*-

import unittest
import Utils as ut

'''Test the class singlePosition()'''
class myTestsSinglePosition(unittest.TestCase):
    
    def test_singlePosition(self):
        self.assertEqual(ut.singlePosition('8').numShares, 8)
        self.assertEqual(ut.singlePosition('8').position, '8')
        self.assertEqual(ut.singlePosition(8).numShares, 8)
        self.assertEqual(ut.singlePosition(8).position, 8)
        self.assertEqual(ut.singlePosition(8).position_value, 1000/8)
        
    def exceptionHandling(self):
        self.assertRaises(ut.textInputedException, ut.singlePosition, 'foo')
        self.assertRaises(ut.positionOver1000, ut.singlePosition, '1001')
        self.assertRaises(ut.negativeNumber, ut.singlePosition, '-1')

'''Test the class number_trials()'''
class myTestsNumber_trials(unittest.TestCase):
    
    def test_singlePosition(self):
        self.assertEqual(ut.number_trials('8').number, 8)
        self.assertEqual(ut.number_trials('10000').number, 10000)
        
    def exceptionHandling(self):
        self.assertRaises(ut.textInputedException, ut.number_trials, 'foo')
        self.assertRaises(ut.textInputedException, ut.number_trials, '[8]')

'''Test the function uniform01ToBinary()'''
class myTestsUniformToBinary(unittest.TestCase):
    
    def test_uniform01ToBinary(self):
        self.assertEqual(ut.uniform01ToBinary(0.3), 0)
        self.assertEqual(ut.uniform01ToBinary(0), 0)
        self.assertEqual(ut.uniform01ToBinary(0.490), 0)
        self.assertEqual(ut.uniform01ToBinary(1), 1)
        self.assertEqual(ut.uniform01ToBinary(0.51), 1)
        self.assertEqual(ut.uniform01ToBinary(0.491), 1)
        
'''Test the function singleSimulation()'''
class singleSimulationTest(unittest.TestCase): 
    
    def test_singleSimulation(self):   
        self.assertEqual(ut.singleSimulation(0.49, ut.singlePosition(2)), 0)
        self.assertEqual(ut.singleSimulation(0.51, ut.singlePosition(2)), (1000/2)*2)
        self.assertEqual(ut.singleSimulation(0.51, ut.singlePosition(100)), (1000/100)*2)
        self.assertEqual(ut.singleSimulation(0.49, ut.singlePosition(100)), 0)
 
        
if __name__ == '__main__':
    unittest.main()