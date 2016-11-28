# -*- coding: utf-8 -*-
"""
Main module of assignment 8. Use script python assignment8.py to run this module.

Certain rules of the assignment applies:

1. You can purchase it in $1, $10, $100, and $1000 denominations.

2. 51% of the time the return is exactly 1.0 (the value doubles).

49% of the time the return is exactly -1.0 (all value is lost).

We have $1000 to invest on the first day.

 will run a simulation to determine how to make that investment on the first day. 
 i.e. Should we make a single $1000 investment, or 1000 $1 investments. 
 (or something in between)

"""
import numpy as np
from investment import *
from UserDefinedError import *
from functions import *
import re
import sys
import matplotlib.pyplot as plt

if __name__ == '__main__':

    while True:

        try:
            positions = input('Hello my friend. Welcome to investment world. '
                              'Please input a list of denominations. e.g. [1, 10, 100, 1000]'
                              'Enter "quit" to stop the program.')

            # To stop the program, enter quit.
            if positions == 'quit':
                break

            #################Input Validation####################

            positions_set = investment_input_pos(positions)

            # Input number of trials.

            num_trials = input('Next the number of trials. '
                               'How many times do you want to run the simulation randomly?')

            trials = investment_input_trials(num_trials)

            #################Output text and pdf#################
            investment_output(positions_set,trials)

        # Catch End of File error.

        except EOFError:
            sys.exit()

        # Catch KeyboardInterrupt error.
        except KeyboardInterrupt:
            sys.exit()





