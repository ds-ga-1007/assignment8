"""
TODO: Describe the behavior here. Also mention that you have adapted the pattern for documentation, comments
from the sklearn class. Mention that numpy and matplotlib packages are required to be installed
"""
# Author: Abhishek Kadian <ak6179@nyu.edu>

from . import simulation_utils as utils
import numpy as np
from matplotlib import pyplot as plt


class Simulation(object):
    """
    Simulation class for the investment instrument.
    """

    @property
    def cumu_ret(self):
        return self._cumu_ret

    @property
    def daily_ret(self):
        return self._daily_ret

    @staticmethod
    def _validate_positions(positions):
        utils.check_positions_instance(positions)
        utils.check_positions_value(positions)

    @staticmethod
    def _validate_num_trials(num_trials):
        utils.check_trials_instance(num_trials)
        utils.check_trials_positive(num_trials)

    def __repr__(self):
        return "positions: " + str(self._positions) + ", num_trials: " + str(self._num_trials)

    def __init__(self, positions, num_trials):
        self._validate_positions(positions)
        self._validate_num_trials(num_trials)
        self._positions = positions[:]
        self._num_trials = num_trials
        self._position_values = [1000 / p for p in positions]
        self._cumu_ret = np.zeros((self._num_trials, len(self._positions)))
        self._daily_ret = np.zeros((self._num_trials, len(self._positions)))

    def _calculate_mean_std(self):
        self._mean_ret = np.mean(self._daily_ret, axis=0)
        self._std_ret = np.std(self._daily_ret, axis=0)

    def simulate(self, bias=0.51):
        for trial in range(self._num_trials):
            for i, (position, value) in enumerate(zip(self._positions, self._position_values)):
                cumulative_return = 0
                for p in range(position):
                    p_return = np.random.random()
                    if p_return < bias:
                        cumulative_return += 2.0 * value
                self._cumu_ret[trial, i] = cumulative_return
                daily_return = (cumulative_return / 1000.0) - 1
                self._daily_ret[trial, i] = daily_return
        self._calculate_mean_std()

    def mean_returns(self):
        return self._mean_ret

    def std_dev_returns(self):
        return self._std_ret

    def write_summary(self, filepath):
        with open(filepath, "w") as f:
            f.write("positions: " + str(self._positions) + "\n")
            f.write("num_trials: " + str(self._num_trials) + "\n")
            for i, p in enumerate(self._positions):
                f.write("position: " + str(p) + ", mean return: " + str(
                    self._mean_ret[i]) + ", standard deviation of return: " + str(self._std_ret[i]) + "\n")

    def plot_trials_histogram(self, filepaths):
        for i, path in enumerate(filepaths):
            plt.hist(self._daily_ret[:, i], 100, range=[-1, 1])
            plt.xlabel("return on investment")
            plt.ylabel("count of trials")
            plt.savefig(path, format='pdf')
            plt.clf()
