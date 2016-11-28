
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def random_outcome():
    '''
    This function generates a random number of -1.0 or 1.0, with probability 0.49 and 0.51 respectively.
    '''
    return np.random.choice([-1.0, 1.0], p = [0.49, 0.51])

def daily_ret_trial(position):
    '''
    Given a position, this function calculates the daily return of one trial.
    '''
    position_value = 1000 / position
    cumu_ret_trial = 0
    daily_ret_trial = 0
    share = 0
    
    # Simulate the outcome of one day of investment
    while share < position:
        cumu_ret_trial += position_value*(1 + random_outcome())
        share += 1
    daily_ret_trial = cumu_ret_trial/1000 - 1
    return daily_ret_trial

def daily_ret(position, num_trials): 
    '''
    This function simulates num_trials single days of trading independently,
    and calculates the daily returns of all trials.
    '''
    daily_ret = [[]] * num_trials
    trial = 0
    while trial < num_trials:
        daily_ret[trial] = daily_ret_trial(position)
        trial += 1
    return daily_ret

def result(position, num_trials):
    '''
    This function presents the histograms, mean and standard deviation of the daily returns.
    '''
    # Plot the daily returns in a histogram with X axis from -1.0 to +1.0, and Y axis as the number of trials with that result.
    f = plt.figure()
    plt.hist(daily_ret(position, num_trials), 100, range=[-1,1])
    filename = 'histogram_' + str(position).zfill(4) + '_pos.pdf'
    f.savefig(filename)   # Reference: http://stackoverflow.com/questions/11328958/matplotlib-pyplot-save-the-plots-into-a-pdf
    
    # Calculate the mean and standard deviation of the daily returns
    mean = np.mean(daily_ret(position, num_trials))
    std = np.std(daily_ret(position, num_trials))
    return [position, mean, std]





    
