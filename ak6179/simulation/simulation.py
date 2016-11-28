"""
Simulation class for investment instrument. Requires numpy and matplotlib to be installed.
"""

from . import simulation_utils as utils
import numpy as np
from matplotlib import pyplot as plt


class Simulation(object):
    @property
    def cumu_ret(self):
        return self._cumu_ret

    @property
    def daily_ret(self):
        return self._daily_ret

    @staticmethod
    def _validate_positions(positions):
        """
        Check if positions contains valid position.
        The list of positions should be non-empty.
        A valid position can take a value from [1, 10, 100, 1000].
        A valid position should be an integer.
        """
        utils.check_positions_instance(positions)
        utils.check_positions_value(positions)

    @staticmethod
    def _validate_num_trials(num_trials):
        """
        Check if num_trials is valid.
        A valid num_trials should be a positive integer.
        """
        utils.check_trials_instance(num_trials)
        utils.check_trials_positive(num_trials)

    def __repr__(self):
        """
        :return: string representation of a Simulation object.
        The representation contains a list of positions and number of trials.
        """
        return "positions: " + str(self._positions) + ", num_trials: " + str(self._num_trials)

    def __init__(self, positions, num_trials):
        """
        :param positions: list of positions. Positions can take any value from: [1, 10, 100, 1000]. The list
        should contain only integers.
        :param num_trials: number of times the simulation is run. num_trials should be a positive value.
        """
        self._validate_positions(positions)
        self._validate_num_trials(num_trials)
        self._positions = positions[:]
        self._num_trials = num_trials
        # Calculating value of a position.
        self._position_values = [1000 / p for p in positions]
        self._cumu_ret = np.zeros((self._num_trials, len(self._positions)))
        self._daily_ret = np.zeros((self._num_trials, len(self._positions)))

    def _calculate_mean_std(self):
        self._mean_ret = np.mean(self._daily_ret, axis=0)
        self._std_ret = np.std(self._daily_ret, axis=0)

    def simulate(self, bias=0.51):
        """
        Simulates different positions for num_trials.
        The daily returns, cumulative returns, mean and std-dev for the simulation is also calculated.
        :param bias: probability by which the value of position doubles. Default value is 0.51.
        """
        for trial in range(self._num_trials):
            for i, (position, value) in enumerate(zip(self._positions, self._position_values)):
                cumulative_return = 0
                for p in range(position):
                    p_return = np.random.random()
                    if p_return < bias:
                        cumulative_return += 2.0 * value
                self._cumu_ret[trial, i] = cumulative_return
                # Normalizing daily return to [-1, 1] range
                daily_return = (cumulative_return / 1000.0) - 1
                self._daily_ret[trial, i] = daily_return
        # Calculating mean and std-deviation for the daily returns.
        self._calculate_mean_std()

    def mean_returns(self):
        """
        :return: a list of means for results of simulation of all the positions.
        This method should be called after running the simulate method.
        """
        return self._mean_ret

    def std_dev_returns(self):
        """
        :return: a list of standard-deviations for results of simulation of all the positions.
        This method should be called after running the simulate method.
        """
        return self._std_ret

    def write_summary(self, filepath):
        """
        Writes summary of the simulation to filepath.
        Summary includes the mean and standard deviation for different positions.
        :param filepath: output file path for the results file.
        """
        with open(filepath, "w") as f:
            f.write("positions: " + str(self._positions) + "\n")
            f.write("num_trials: " + str(self._num_trials) + "\n")
            for i, p in enumerate(self._positions):
                f.write("position: " + str(p) + ", mean return: " + str(
                    self._mean_ret[i]) + ", standard deviation of return: " + str(self._std_ret[i]) + "\n")

    def plot_trials_histogram(self, filepaths):
        """
        Plots histograms for all the positions of simulation.
        :param filepaths: list of paths for histogram files. The number of filepaths should be
        equal to the number of positions.
        """
        for i, path in enumerate(filepaths):
            # Plot histogram of daily returns.
            plt.hist(self._daily_ret[:, i], 100, range=[-1, 1])
            plt.xlabel("return on investment")
            plt.ylabel("count of trials")
            plt.savefig(path, format='pdf')
            plt.clf()
