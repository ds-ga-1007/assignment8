import unittest
from simulation import *

'''This class contains two functions. First one tests the mean generated by the module "simulation", and
the second one tests the standard deviation of the previous result. Both pass successfully'''

class tests(unittest.TestCase):
    def test_mean(self):
        s1 = simulation(10, 10000)
        s2 = simulation(100, 10000)
        self.assertTrue(abs(s1.mean - 0.01588) < 0.01)
        self.assertTrue(abs(s2.mean - 0.021166) < 0.01)

    def test_std(self):
        s3 = simulation(100, 10000)
        s4 = simulation(1000, 10000)
        self.assertTrue(abs(s3.std - 0.099479648391) < 0.01)
        self.assertTrue(abs(s4.std - 0.03175307467) < 0.01)


if __name__ == "__main__":
    unittest.main()