'''
Created on 2016Äê11ÔÂ28ÈÕ

@author: wxy
'''
import unittest
from investment import investment


class Test(unittest.TestCase):

    def test0(self) :
        with self.assertRaise(ValueError) as error:
            investment("a")
        self.assertTrue("Please select from one of the four options: 1, 10, 100, 1000!" in str(error.exception))
    
    def test1(self) :
        test1 = investment(1)
        self.assertEqual(test1.position, 1)
        self.assertEqual(test1.position_value, 1000)
        self.assertIn(test1.one_day_outcome(), range(2001))
    
    def test2(self) :
        test2 = investment(10)
        self.assertEqual(test2.position, 10)
        self.assertEqual(test2.position_value, 100)
        self.assertIn(test2.one_day_outcome(), range(2001))
            
    def investment_test3(self) :
        test3 = investment(100)
        self.assertEqual(test3.position, 100)
        self.assertEqual(test3.position_value, 10)
        self.assertIn(test3.one_day_outcome(), range(2001))
    
    def investment_test4(self) :
        test4 = investment(1000)
        self.assertEqual(test4.position, 1000)
        self.assertEqual(test4.position_value, 1)
        self.assertIn(test4.one_day_outcome(), range(2001))


if __name__ == "__main__":
    unittest.main()
