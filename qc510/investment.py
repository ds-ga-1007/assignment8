"""
Define a class investment that calculate the result of a one day investment.

@author: Qianyu Cheng
"""
import numpy as np
import pandas as pd


class investment_daily(object):
    """

    This class for investment with one specific position like: 1, 10, 100, 1000

    Methods:
        one_day: that takes a investment_daily object and calculate the daily return for the position.
    """
    def __init__(self, position, num_trials):

        # Build a constructor that save the position and number of trials from user output.

        self.position = position
        self.num_trials = num_trials

    def one_day(self):
        """
        Function that return a numpy array: that contains the daily returns for the number of trials simulations.
        """
        # Set position value equals to 1000/position
        position_value = 1000 / self.position

        # Construct matrix for cumulative returns and daily returns.
        cumu_ret = np.zeros(self.num_trials)
        daily_ret = np.zeros(self.num_trials)

        # For each trials calculate cumulative returns and investment gain.
        for i in range(self.num_trials):
            cumu_ret[i] = sum(np.random.uniform(size=self.position) <= 0.51) * 2 * position_value
            daily_ret[i] = (cumu_ret[i]/1000 - 1)

        return daily_ret


