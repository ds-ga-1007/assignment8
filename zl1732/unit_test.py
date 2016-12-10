import unittest
from assignment8 import *
from investment import investment

class solutionTest(unittest.TestCase):
    '''
    setup the unit_test
    print messages
    '''
    def setUp(self):
        print("Unit_test starting")
        pass
    
    '''
    test constructor in investment class
    '''
    def test_constructor(self):
        i = investment("[1, 10]","10000")     
        self.assertEqual(i.positions,"[1, 10]")
        self.assertEqual(i.num_trails, "10000")

    '''
    test str2num function
    '''
    def test_str2num(self):
        i = investment("[1, 10]","10000")  
        positions = "[1, 10, 100, 1000]"
        trails = "10000"
        positions_result, trails_result = i.str2num(positions, trails)
        position_true = [1, 10, 100, 1000]
        trails_true = 10000
        self.assertEqual(positions_result,position_true)
        self.assertEqual(trails_result, trails_true)
    
    '''
    test simulation_one function
    '''
    def test_simulation_one(self):
        i = investment("[1, 10]","10000")  
        positions = 1
        trails_1 = 10
        trails_2 = 100
        trails_3 = 1000
        self.assertEqual(len(i.simulation_one(positions,trails_1)),trails_1)
        self.assertEqual(len(i.simulation_one(positions,trails_2)),trails_2)
        self.assertEqual(len(i.simulation_one(positions,trails_3)),trails_3)
    
    '''
    test simulation function
    '''
    def test_simulation(self):
        i = investment("[1, 10]","10000")  
        positions_1 = [1,10]
        positions_2 = [1,10,100]
        positions_3 = [1,10,1000]
        trails = 10000
        self.assertEqual(len(i.simulation(positions_1,trails).keys()),len(positions_1))
        self.assertEqual(len(i.simulation(positions_2,trails).keys()),len(positions_2))
        self.assertEqual(len(i.simulation(positions_3,trails).keys()),len(positions_3))

            
if __name__ == "__main__":
    unittest.main()