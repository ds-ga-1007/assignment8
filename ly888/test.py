import unittest
from invest import invest
import numpy as np
import matplotlib.pyplot as plt

# test the class invest
# set fixed seed, create a function to read the results and check the output again
def read_result(positions, num_trials):
    invest(positions, num_trials).invest_sub()
    
    with open('results.txt','r') as string:
        read_result = string.read()
    return read_result

# based on positions [1,10,100,1000] and num_trials 100 to test
# based on positions [1,10,100,1000] and num_trials 1000 to test
# based on positions [1,10,100,1000] and num_trials 10000 to test
class Test(unittest.TestCase):
    def test_equal_invest(self):
        self.assertEqual(read_result([1,10,100,1000],100), 'Position:  1   Position Value:  1000.0  Mean:  0.08  Standard Deviation:  0.9967948635501689 \nPosition:  10   Position Value:  100.0  Mean:  0.046  Standard Deviation:  0.31094050877941265 \nPosition:  100   Position Value:  10.0  Mean:  0.03300000000000001  Standard Deviation:  0.10021476937058728 \nPosition:  1000   Position Value:  1.0  Mean:  0.02674000000000002  Standard Deviation:  0.03180019496795581 \n')
        self.assertEqual(read_result([1,10,100,1000],1000), 'Position:  1   Position Value:  1000.0  Mean:  0.06  Standard Deviation:  0.9981983770774222 \nPosition:  10   Position Value:  100.0  Mean:  0.021799999999999993  Standard Deviation:  0.3216904723488092 \nPosition:  100   Position Value:  10.0  Mean:  0.02018000000000001  Standard Deviation:  0.10525572478492559 \nPosition:  1000   Position Value:  1.0  Mean:  0.019406000000000017  Standard Deviation:  0.0321045037961966 \n')
        self.assertEqual(read_result([1,10,100,1000],10000), 'Position:  1   Position Value:  1000.0  Mean:  0.0168  Standard Deviation:  0.9998588700411675 \nPosition:  10   Position Value:  100.0  Mean:  0.01299999999999999  Standard Deviation:  0.3181430495861885 \nPosition:  100   Position Value:  10.0  Mean:  0.020506000000000014  Standard Deviation:  0.09975662365978512 \nPosition:  1000   Position Value:  1.0  Mean:  0.02000200000000002  Standard Deviation:  0.031688483649426995 \n')
if __name__ == "__main__":
    unittest.main()