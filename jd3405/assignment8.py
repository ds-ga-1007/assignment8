# Solution for DS-GA 1007 Assignment#8
# Author: Jiaming Dong (jd3405@nyu.edu)
# NYU Center for Data Science
# This program is the main program.
# You can run it by type "python assignment8.py"
# You can enter the positions by space separated numbers such as:
#   1 10 100 1000
# You can enter the number of trials as one number such as:
#   10000
# Enter an enter to break.

from investment import Investment
import matplotlib.pyplot as plt
from statistics import mean, stdev
from error import *


def solve(positions, num_trials):
    """
    For a given position list and number of trials, run the experiments
    and draw the plots.
    """
    for position in positions:
        # create a new class
        investment = Investment(position)
        daily_ret = []
        for trial in range(num_trials):
            # do a invest each time
            investment.invest()
            # calculate the corresponding daily_ret, using double
            daily_ret.append(investment.ret * 1.0 / 1000.0 - 1.0)
        print("The mean of position", position, "is", mean(daily_ret))
        print("The standard deviation of position", position, "is", stdev(daily_ret))
        plt.hist(daily_ret, 100, range=[-1, 1])
        plt.show()


def trans_to_int(s):
    """handle the invalid input exception"""
    # empty string
    if len(s) == 0:
        raise InvalidInputException
    # non-number characters
    for i in s:
        if ord(i) > ord("9") or ord(i) < ord("0"):
            raise InvalidInputException
    ret = int(s)
    # zero or can not divide 1000
    if ret == 0 or 1000 % ret != 0:
        raise InvalidInputException
    return ret


def main():
    while True:
        positions = []
        pos_input = input("Input positions, empty line for break: ")
        if len(pos_input) == 0:
            break
        position_str = pos_input.split(" ")
        for pos in position_str:
            try:
                positions.append(trans_to_int(pos))
            except InvalidInputException:
                print("Input is invalid")
                return
        trial_input = input("Input number of trials:")
        num_trials = int(trial_input)
        solve(positions, num_trials)


if __name__ == "__main__":
    main()
