# -*- coding: utf-8 -*-
"""
Main module of assignment 8. Use script python assignment8.py to run this module.

Certain rules of the assignment applies:

1. You can purchase it in $1, $10, $100, and $1000 denominations.
2. 51% of the time the return is exactly 1.0 (the value doubles).
49% of the time the return is exactly -1.0 (all value is lost).
We have $1000 to invest on the first day.

What this module do is to first get a list of positions from user in format like [1,10,100,1000] or [10,100,1000].
Next the module will ask for another number to randomly simulate the program.
After accepting two correct input, the module will generate one pdf for each position input,
and a text file that contains mean and standard deviation for that specific position.

@author: Qianyu Cheng
"""

import numpy as np
from investment import *
from UserDefinedError import *
from functions import *
import re
import sys
import matplotlib.pyplot as plt

if __name__ == '__main__':

    Running = True

    while Running:

        try:

            positions = input('Hello my friend. Welcome to investment world. '
                              'Please input a list of denominations. e.g. [1, 10, 100, 1000]'
                              'Enter "quit" to stop the program.')

            # To stop the program, enter quit.

            if positions == 'quit':
                break

            # Input set of positions in parallels

            # The functions that takes in the input as string and return a list of positions as integer.

            positions_set = investment_input_pos(positions)

            # Input number of trials.

            num_trials = input('Next the number of trials. '
                               'How many times do you want to run the simulation randomly?')

            # Run function that takes trials input and see if the input is correct.

            trials = investment_input_trials(num_trials)

            # Output text and pdf files for each position in positions_set.

            investment_output(positions_set,trials)

        # Enter Ctrl + D and exit.

        except EOFError:
            sys.exit(0)

        # Enter Ctrl + C and exit.

        except KeyboardInterrupt:
            sys.exit(0)





