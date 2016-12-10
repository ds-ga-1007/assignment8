'''
Created on Nov 27, 2016

This module contains the functions used in main

@author: ShashaLin
'''
import numpy as np
import matplotlib.pyplot as plt


def cumu_return (value, position):
    'get cumulative return after one day'
    cumu_ret = []
    for share in range(position):
        returns = np.array([0, value*2])
        probabilities = np.array([.49, .51])
        cumu_ret.append(np.random.choice(returns, p = probabilities))
    cumu_ret = np.sum(cumu_ret)
    return cumu_ret

def repeat(num, value, position):
    'get daily return for repeated simulations'
    cumu_ret = []
    for iteration in range(num):
        cumu_ret.append(cumu_return(value, position))
    daily_ret = (np.array(cumu_ret)/1000) -1
    return daily_ret

def makefig(index, value, positions, num_trials):
    'saves plot for different purchasing scenarios in separate pdf files'
    daily_ret = repeat(num_trials, value, positions[index])
    fig = plt.figure()
    plt.hist(daily_ret, 100, range = [-1,1])
    plt.title('Simulation of Return with {} trials and {} shares'.format(num_trials, positions[index]))
    plt.xlabel('daily return')
    plt.ylabel('numbers of trials')
    fig.savefig('histogram_{0:04}_pos.pdf'.format(positions[index]))
    return daily_ret
    
def save_results(positions, index, daily_ret):
    'stores descriptive statistics for daily return in each scenario to one single text file'
    f = open('results.txt', 'a')
    f.write('{} shares: mean = {}, standard deviation = {} \n \n'.format(positions[index], np.mean(daily_ret), np.std(daily_ret)))
    f.close
    