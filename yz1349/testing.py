import unittest
from investment import investment
class investment_test(unittest.TestCase):
    def testInvestment1(self):
        with self.assertRaises(ValueError) as cm:
            investment("999")
        thisexception = cm.exception
        self.assertEquals(str(thisexception), 'Invalid position value, must be either of 1, 10, 100, 1000.')
        
        with self.assertRaises(ValueError) as cm:
            investment("hahaha")
        thisexception = cm.exception
        self.assertEquals(str(thisexception), 'Invalid position value, must be either of 1, 10, 100, 1000.')
        
        with self.assertRaises(ValueError) as cm:
            investment(-100)
        thisexception = cm.exception
        self.assertEquals(str(thisexception), 'Invalid position value, must be either of 1, 10, 100, 1000.')

    def testInvestment2(self):
        
        self.assertEqual(investment(1).position, 1 )
        self.assertEqual(investment(1000).position, 1000 )

    def testInvestment3(self):

        self.assertEqual(investment(100).position_value, 10)
        self.assertEqual(investment(1).position_value, 1000)
        
    def testInvestment4(self): 
       
        self.assertTrue(investment(10).cumu_ret[5] in [200,0])
        self.assertTrue(investment(1).cumu_ret[0] in [2000,0])
    
if __name__ == "__main__":
    unittest.main()