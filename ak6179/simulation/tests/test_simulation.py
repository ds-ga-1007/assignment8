"""
Unit tests for simulation moduel.
For running the unit test use the command 'python -m unittest discover' in the netid (ak6179) directory.
The command will automatically discover unit tests and will run them.
"""
import unittest
from ..simulation import *


class SimulationTest(unittest.TestCase):
    def test_constructor(self):
        sim = Simulation([1, 10, 100, 1000], 1000)
        self.assertEqual(str(sim), "positions: [1, 10, 100, 1000], trials: 1000")
        with self.assertRaises(ValueError):
            _ = Simulation(100, 1000)
        with self.assertRaises(ValueError):
            _ = Simulation([100, 1000], -1)


if __name__ == "__main__":
    unittest.main()
