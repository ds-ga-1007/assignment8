import numpy as np
from Investment.InvestmentError import *


class Investment:
    """Representation of an investment."""

    def __init__(self, investment_amount):
        """Constructor for an Investment instance

        :param investment_amount: user-provided input representing
            initial investment into investment instrument
        """

        # Validate our initial investment.
        self.validate_input(investment_amount)

        # Populate our Investment instance with the investment amount
        # and a return amount
        self.position = investment_amount

    @staticmethod
    def validate_input(position):
        """Validate user input is a valid integer denomination

        :param position: user's input to call to Investment constructor
        :return: raises InvalidInvestmentException if invalid, otherwise continues construction
        """

        if type(position) not in [int, float] or position < 0:
            raise InvestmentPositionException(position)

    def __repr__(self):
        """Unambiguous representation of Investment object -- its instantiation."""
        return "Investment({})".format(self.position)


def biased_gamble(times: int):
    """Perform :times draws from a biased distribution.

    :param times: number of times we'd like to draw from distribution.
    :return: numpy array where ~49% = 0 and ~51% = 2.
    """

    # As per assignment instructions:
    #   Probability our investment is a failure: 49%. (P(0) = 0.49)
    #   Probability our investment doubles: 51%.      (P(2) = 0.51)
    # Note we circumvent the future translation of -1 => 0 and
    # 1 => 2 by accounting for it here.
    return np.random.choice(a=[0, 2], p=[0.49, 0.51], size=times)
