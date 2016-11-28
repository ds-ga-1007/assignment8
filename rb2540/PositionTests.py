import unittest
import numpy as np
from Position import *

class PositionTests(unittest.TestCase) :
    def test_init(self) :
        """Tests the constructor properly sets member variables"""
        p = Position(2,10,.6)

        self.assertEqual(p.value,500)
        self.assertEqual(p.bias,.6)
        self.assertEqual(len(p.cumu_ret),10)
        self.assertEqual(len(p.daily_ret),10)

    def test_computeTrial1(self) :
        """Tests computeTrial with bias = 1"""
        p = Position(2,2,1)
        p.computeTrial(0)
        self.assertEqual(p.cumu_ret[0],2000)
        np.testing.assert_almost_equal(p.daily_ret[0],1,decimal=7)
        p.computeTrial(1)
        self.assertEqual(p.cumu_ret[1],2000)
        np.testing.assert_almost_equal(p.daily_ret[1],1,decimal=7)
        
    def test_computeTrial2(self) :
        """Tests computeTrial with bias = 0"""
        p = Position(2,2,0)
        p.computeTrial(0)
        self.assertEqual(p.cumu_ret[0],0)
        np.testing.assert_almost_equal(p.daily_ret[0],-1,decimal=7)
        
    def test_computeAllTrials1(self) :
        """Tests computeAllTrials with bias = 1, and tests getMean and getStd"""
        p = Position(2,100,1)
        p.computeAllTrials()
        self.assertEqual(p.cumu_ret[1],2000)
        np.testing.assert_almost_equal(p.daily_ret[1],1,decimal=7)
        np.testing.assert_almost_equal(p.getMean(),1,decimal=7)
        np.testing.assert_almost_equal(p.getStd(),0,decimal=7)

    def test_computeAllTrials2(self) :
        """Tests computeAllTrials with bias = 0, and tests getMean and getStd"""
        p = Position(2,100,0)
        p.computeAllTrials()
        self.assertEqual(p.cumu_ret[1],0)
        np.testing.assert_almost_equal(p.daily_ret[1],-1,decimal=7)
        np.testing.assert_almost_equal(p.getMean(),-1,decimal=7)
        np.testing.assert_almost_equal(p.getStd(),0,decimal=7)

if __name__ == '__main__':
    unittest.main()
