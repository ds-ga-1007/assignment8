import unittest
from simulation import simulation
import numpy as np



class SimpleTest(unittest.TestCase):

   

    def test_daily_ret(self):
        testSimu1 = simulation(100, 1000)
        #test the position value
        self.assertEqual(testSimu1.position_value, 10)
        
        
        #test the single return and total return
        daily_ret = testSimu1.cumu_return()
        self.assertTrue(daily_ret[1].mean() <= 1 and daily_ret[1] >= -1)
        self.assertTrue(np.mean(daily_ret) <= 1 and np.mean(daily_ret) >= -1)
        
        #test the length of the list
        self.assertEqual(len(daily_ret), 1000)



        testSimu1 = simulation(50, 2000)
        #test the position value
        self.assertEqual(testSimu1.position_value, 20)
        
        
        #test the single return and total return
        daily_ret = testSimu1.cumu_return()
        self.assertTrue(daily_ret[1].mean() <= 1 and daily_ret[1] >= -1)
        self.assertTrue(np.mean(daily_ret) <= 1 and np.mean(daily_ret) >= -1)
        
        #test the length of the list
        self.assertEqual(len(daily_ret), 2000)


    
if __name__ =="__main__":
    unittest.main()     