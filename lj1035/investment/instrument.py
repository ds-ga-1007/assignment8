import numpy as np
import matplotlib.pyplot as plt
from investment import myexception


# The Instrument class represents an investment and contains methods about relevant actions of this investment.
class Instrument(object):

    def __init__(self, position, num_trials):
        """
        This is the constructor of the Instrument class.
        """
        self.position = position
        self.position_value = 1000 / self.position
        self.num_trials = num_trials

    def simulate_invest(self):
        """
        This method computes and returns daily returns by repeating multiple trails.
        """
        cumu_ret = np.ones(self.num_trials)
        daily_ret = np.ones(self.num_trials)
        for trial in range(self.num_trials):
            rand_probability = np.random.uniform(size=self.position)
            win_times = len(rand_probability[rand_probability < 0.51])
            cumu_ret[trial] = win_times * self.position_value * 2
            daily_ret[trial] = (cumu_ret[trial] / 1000) - 1
        return daily_ret

    def get_mean(self):
        """
        This method computes and returns the mean of the daily return.
        """
        return np.mean(self.simulate_invest())

    def get_std(self):
        """
        This method computes and returns the standard deviation of the daily return.
        """
        return np.std(self.simulate_invest())

    def visualize_invest(self):
        """
        This method generates the histogram of daily returns and export the plot to a pdf file.
        """
        fig = plt.figure()
        plt.title('Histogram of ' + str(self.position) + ' position of $' + str(self.position_value))
        plt.hist(self.simulate_invest(), 100, range=[-1, 1])
        fig.savefig('histogram_' + str(self.position).zfill(4) + '_pos.pdf')


def num_trials_to_int(num_trials_string):
    """
    This function takes num_trials_strings as an argument and raises exceptions when necessary.
    If no exception being raised, then the function will convert num_trials_string into a value with type int and
    return this value.
    """
    # check if the input is a number, raise an error if not
    try:
        float(num_trials_string)
    except ValueError:
        raise myexception.NotNumericError()
    # check if the input is an integer, raise an error if not
    try:
        int(num_trials_string)
    except ValueError:
        raise myexception.NotIntegerError()
    # check if the input is a positive integer, raise an error if not
    if int(num_trials_string) <= 0:
        raise myexception.NotPositiveIntegerError()
    else:
        return int(num_trials_string)


def positions_to_list(positions_input):
    """
    This function takes positions_input as an argument and raises exceptions when necessary.
    If no exception being raised, then the function will convert positions_input into a list in which all elements
    are with type int and return this new list of positions.
    """
    # check if the input is in the correct format, raise an error if not
    if positions_input[1] != '[' and positions_input[-1] != ']':
        raise myexception.FormattingError()
    cleaned_input = positions_input[1: -1].replace(" ", "")
    try:
        cleaned_input_list = cleaned_input.split(',')
    except:
        raise myexception.FormattingError()
    positions = []
    for position in cleaned_input_list:
        # check if each position is numeric, raise an error if not
        try:
            float(position)
        except ValueError:
            raise myexception.NotNumericError()
        # check if each position is an integer, raise an error if not
        try:
            int(position)
        except ValueError:
            raise myexception.NotIntegerError()
        # check if each position is a positive integer, raise an error if not
        if int(position) <= 0:
            raise myexception.NotPositiveIntegerError()
        positions.append(int(position))
    return positions