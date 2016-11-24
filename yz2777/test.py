""" Unittest for class invest """ 

import unittest
from class_invest import invest
import numpy as np
import matplotlib.pyplot as plt

# test the class invest
# create a function to read the results and return as a string
# set the seed to see whether the output results can be reproduceable
def read_result(pos_list, num_tests):
    np.random.seed(777)
    invest(pos_list,num_tests).bet()
    
    with open('results.txt','r') as string:
        read_result = string.read()
    return read_result

# based on different cases [1],[10],[100],[1000], and [1,10,100,1000] to test
class Test(unittest.TestCase):
    def test_equal_invest(self):
        self.assertEqual(read_result([1],10000), 'Position: 1, Position Value: $1000.0, Mean: 0.0142, Standard Deviation: 0.9998991749171514\n')
        self.assertEqual(read_result([10],10000), 'Position: 10, Position Value: $100.0, Mean: 0.017519999999999994, Standard Deviation: 0.31686755845305464\n')
        self.assertEqual(read_result([100],10000), 'Position: 100, Position Value: $10.0, Mean: 0.019450000000000005, Standard Deviation: 0.09932682165457626\n')
        self.assertEqual(read_result([1000],10000), 'Position: 1000, Position Value: $1.0, Mean: 0.019663200000000016, Standard Deviation: 0.032163174062271926\n')
        self.assertEqual(read_result([1,10,100,1000],10000), 'Position: 1, Position Value: $1000.0, Mean: 0.0142, Standard Deviation: 0.9998991749171514\nPosition: 10, Position Value: $100.0, Mean: 0.01665999999999999, Standard Deviation: 0.3158202723068929\nPosition: 100, Position Value: $10.0, Mean: 0.01941600000000001, Standard Deviation: 0.09935743024052103\nPosition: 1000, Position Value: $1.0, Mean: 0.019743000000000017, Standard Deviation: 0.03222631147059808\n')
if __name__ == "__main__":
    unittest.main()
