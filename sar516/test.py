import unittest
from investment import investment

class Test(unittest.TestCase):
    
    def investment_test1(self) :
        inv1 = investment(1)
        self.assertEqual(inv1.position, 1)
        self.assertEqual(inv1.position_value, 1000)
        self.assertIn(inv1.day_instance(), range(2001))
    
    def investment_test2(self) :
        inv2 = investment(10)
        self.assertEqual(inv2.position, 10)
        self.assertEqual(inv2.position_value, 100)
        self.assertIn(inv2.day_instance(), range(2001))
    
    def investment_test3(self) :
        inv3 = investment(100)
        self.assertEqual(inv3.position, 100)
        self.assertEqual(inv3.position_value, 10)
        self.assertIn(inv3.day_instance(), range(2001))
    
    def investment_test4(self) :
        inv4 = investment(1000)
        self.assertEqual(inv4.position, 1000)
        self.assertEqual(inv4.position_value, 1)
        self.assertIn(inv4.day_instance(), range(2001))
    
    def investment_test5(self) :
        with self.assertRaise(ValueError) as error:
            investment("a")
        self.assertTrue("Improper type for this class" in str(error.exception))
    
    def investment_test6(self) :
        with self.assertRaise(ValueError) as error:
            investment(4)
        self.assertTrue("Improper values passed for this class" in str(error.exception))
        
if __name__ == '__main__':
    unittest.main()
    