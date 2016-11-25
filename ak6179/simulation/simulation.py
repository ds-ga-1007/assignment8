"""
TODO: Describe the behavior here. Also mention that you have adapted the pattern for documentation, comments
from the sklearn class
"""
# Author: Abhishek Kadian <ak6179@nyu.edu>

from . import simulation_utils as utils


class Simulation(object):
    """
    Simulation class for the investment instrument.
    """
    @staticmethod
    def _validate_positions(positions):
        utils.check_positions_instance(positions)
        utils.check_positions_value(positions)

    @staticmethod
    def _validate_trials(trials):
        utils.check_trials_instance(trials)
        utils.check_trials_positive(trials)

    def __repr__(self):
        return "positions: " + str(self._positions) + ", trials: " + str(self._trials)

    def __init__(self, positions, trials):
        self._validate_positions(positions)
        self._validate_trials(trials)
        self._positions = positions.copy()
        self._trials = trials
