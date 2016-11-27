"""
Unit tests for simulation module.
For running the unit test use the command 'python -m unittest discover' in the netid (ak6179) directory.
The command will automatically discover unit tests and will run them.
I had previously added a main function allowing standalone running of tests. I have removed that
functionality because you can't do relative imports using that procedue.
Eg: The statement from ..simulation import * would be invalid. There is a workaround to this
problem as indicated by this answer: http://stackoverflow.com/questions/16981921/relative-imports-in-python-3 .
I went through a number of online resources and unit tests implementation in python (eg: sklearn) and
the standard way to run tests is using the command 'python -m unittest discover'.
"""
import unittest
from ..simulation import *


class SimulationTest(unittest.TestCase):
    def test_constructor(self):
        sim = Simulation([1, 10, 100, 1000], 1000)
        self.assertEqual(str(sim), "positions: [1, 10, 100, 1000], num_trials: 1000")
        sim = Simulation([1], 10)
        self.assertEqual(str(sim), "positions: [1], num_trials: 10")
        sim = Simulation([100, 1000], 100)
        self.assertEqual(str(sim), "positions: [100, 1000], num_trials: 100")
        sim = Simulation([1000, 100, 10, 1, 10, 100, 1000], 10)
        self.assertEqual(str(sim), "positions: [1000, 100, 10, 1, 10, 100, 1000], num_trials: 10")
        with self.assertRaises(ValueError):
            _ = Simulation(100, 1000)
        with self.assertRaises(ValueError):
            _ = Simulation([100, 1000], -1)
        with self.assertRaises(ValueError):
            _ = Simulation([1, 10, 100, 1000, 2000], 20)
        with self.assertRaises(ValueError):
            _ = Simulation([], 1000)
        with self.assertRaises(ValueError):
            _ = Simulation([100], "20")
        with self.assertRaises(ValueError):
            _ = Simulation(["1000"], 200)

    def test_simulation(self):
        # Test for running a sample simulation. To reduce execution time number of trials are kept small.
        try:
            sim = Simulation([1, 10, 100, 1000], 10)
            sim.simulate()
        except Exception as e:
            self.fail()

