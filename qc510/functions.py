import numpy as np
from investment import *
from UserDefinedError import *
import re
import sys
import matplotlib.pyplot as plt
"""
Functions for positions and trial input and out put
@author: Qianyu Cheng
"""


def investment_input_pos(positions):

    # This function takes in user input: positions as string

    # Meet certain format: in 1, 10, 100, 1000 and contain values in '[]'.

    if not re.match(r'^[\[]\d+(\,\d+)*[\]]$', positions):
        raise InputErrorPositions

    # Get all numbers
    positions_set = re.findall(r'\d+', positions)

    # Find out if all numbers are within 1, 10, 100, 1000 since these are all denominations available.

    for i in range(len(positions_set)):
        if positions_set[i] not in ['1', '10', '100', '1000']:
            raise InputErrorPositions

    # Return the cleansed positions sets as list.

    return positions_set


def investment_input_trials(num_trials):

    # This function takes in user input: num_trials as string

    # Test to see if the input is integer.

    try:

        trials = int(num_trials)

    except ValueError:

        print("There is error in your input. Please enter a positive integer. e.g.: 100000.")

    # And check to see if the input is positive.

    if int(num_trials) <= 0:

        raise InputErrorTrials

    # Return the trials as a integer if the input is validated.

    return trials


def investment_output(positions_set,trials):

    # Take positions_set and trials that got from the functions above as user input.

    # Print the txt and pdf that are needed for questions.

    # Write the result on a text file

    output_text = open('results.txt', 'w')

    # Run each value in positions_set that we got from user input.

    for val in positions_set:

        # Run the program inside investment_daily class

        daily_ret = investment_daily(int(val), trials).one_day()

        # Define the size of the figure

        fig = plt.figure(figsize=(6, 6))

        # Print out the histogram.

        plt.hist(daily_ret, 100, range=[-1, 1])

        # Print out pdf with name 0001, 0010, 0100, 1000

        pdf_name = 'histogram_{}_pos.pdf'.format(str(val).zfill(4))

        # Save the pdf to different file

        fig.savefig(pdf_name)

        # Calculate mean and standard deviation

        mean = np.average(daily_ret)

        std = np.std(daily_ret)

        # Output the mean and standard deviation to a text file.

        output_text.write('When position = {}, mean = {:f}, '
                          'standard deviation = {:f}.\n'.format(val, mean, std))

    # Close the text output.

    output_text.close()


