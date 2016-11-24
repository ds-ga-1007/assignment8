
from unittest import TestCase
import numpy as NP
import numpy.random as RNG
from ..trial import Trial

class TestTrial(TestCase):
    def setUp(self):
        # Assumes that the RNG across all Python 3 implementations on
        # all OS'es are the same.
        RNG.seed(1)

    def test_mean_std(self):
        trial = Trial(100, 10000)
        self.assertEqual(len(trial._cumu_ret), 10000)
        self.assertTrue(NP.isclose(trial.mean, 0.020742))
        self.assertTrue(NP.isclose(trial.std, 0.100166907889))
