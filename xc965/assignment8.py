'''
This is the main module of the program, which allows users to:
    - decide whether to use default settings
    - select positions set and number of trials, if not default
    - export daily return performances with histograms and statistical analysis

Author: Xianzhi Cao (xc965)
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re
import sys
import seaborn as sns
from investment import *
from formatchecking import *
from output import *
from errors import *


def user_invest():
    """
    This function allows users to self-define
    the positions set and number of trials.

    Choose:
        - 'Y' to use the default set
        - 'N' to enter self-defined values
    Inputs:
        - positions set as a list
        - number of trials as a postive integer
    Outputs:
        - PDF: histograms of Daily Returns
        - TXT: averages and standard deviations of Daily Returns
    """
    while True:
        try:
            # input: choose whether to use default settings
            user_input = input('Do you want to use the default settings?\n(positions set: [1, 10, 100, 1000] and number of trials: 10000)(Y/N)\n')

            if user_input == '':
                raise EmptyInputError

            elif user_input.upper() == 'Y':
                # set the default positions set as below
                positions_set = [1, 10, 100, 1000]
                num_trials = 10000
                break

            elif user_input.upper() == 'N':
                # user not using default settings
                while True:
                    try:
                        # allows users to input self-defined positions value
                        pos = input('Please enter your positions set, eg.[1, 10, 100, 1000]: ')
                        positions_set = get_positions_set(pos)
                        break
                    except InputFormatError as x:
                        print(x)
                    except ZeroPositionError as x:
                        print(x)
                    except EmptyInputError as x:
                        print(x)

                while True:
                    try:
                        # input should be an integer
                        num = input('How many trials do you want to run?\nPlease enter a number: ')
                        num_trials = get_num_trials(num)
                        break
                    except NonPositiveIntegerError as x:
                        print(x)
                    except NonNumericError as x:
                        print(x)
                break

            else:
                raise YesOrNoError  # users' initial input command should only be 'Y' or 'N'

        except EmptyInputError as x:
            print(x)

        except YesOrNoError as x:
            print(x)


    # output: call this function in investment module to export results
    result_output(positions_set, num_trials)
    print('Completed')


if __name__ == '__main__':
    try:
        user_invest()
    except EOFError:
        # Allow force quit command to quit the program while no input entered
        sys.exit()
    except KeyboardInterrupt:
        # Allow user to quit the program using ctrl+c command
        print('Quitted')
        sys.exit()
