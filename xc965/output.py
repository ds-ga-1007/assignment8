'''
This module exports the output of daily return performances in PDF and TXT files.
    - PDF: histograms of Daily Returns
    - TXT: averages and standard deviations of Daily Returns

Author: Xianzhi Cao (xc965)
'''

import numpy as np
import matplotlib.pyplot as plt
from investment import *


def result_output(positions_set, num_trials):
    '''
    This function outputs daily return performances in both PDF and TXT files.
    '''
    text_file = open('results.txt', 'w')

    for p in positions_set:
        # for each position value, get investment performance result as a numpy array
        daily_ret = investment(int(p), num_trials).daily_returns()

        # plot the histogram of daily return and export PDF file for each position
        fig = plt.figure(figsize=(7, 4))
        plt.hist(daily_ret, 100, range=[-1, 1], alpha=0.5)
        plt.title('The histogram of the result for {}-position of ${:d}'.format(p, int(1000/int(p))))
        plt.xlabel('Regularized Daily Return')
        plt.ylabel('Number of Trials')
        pdf_name = 'histogram_{}_pos.pdf'.format(str(p).zfill(4))
        fig.savefig(pdf_name)

        # write the daily return's mean and standard deviation for each position to a txt file
        mean = np.average(daily_ret)
        std = np.std(daily_ret)
        text_file.write('For position = {}, the mean of daily return is {:f}, and the standard deviation is {:f}.\n'.format(p, mean, std))

    text_file.close()
