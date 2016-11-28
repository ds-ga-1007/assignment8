'''
Created on Nov 22, 2016

@author: Caroline Roper, netid cer446

This program assumes you have $1,000 to invest and you'd like to simulate the result of various positions, or investment sizes.
This program takes and validates a list of positions such as 1, 10, 100, or 1000 and a number of trial, such as 10,000.
It then invests $1,000 divided into the denominations listed, iterating over the number of trials input.
Each investment will double with a 51% chance or be lost (go to $0) with a 49% chance.
The program outputs a histogram of the trial results for each denomination and the mean and standard deviation for each.
'''

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sys
import os

sys.path.append('hw8_package')

import validate_input as i
import Investment as inv
import invest as v

#ask for valid investment positions

Investments = []

while not Investments: #as long as we don't have positions
    position_input = i.take_position()
    if position_input != 'quit':
        try:
            positions = i.make_positions(position_input)
            if positions:
                try:
                    Investments = [inv.Investment(position) for position in positions]
                except Exception as err2:
                    print(err2)
        except Exception as err1:
            print(err1)
    elif position_input == 'quit':
        sys.exit('Quit')
        
#ask for valid number of trials

num_trials = 0

while num_trials == 0:
    trials = i.take_trials()
    if str(trials) != 'quit':
        try:
            trials = int(trials.replace(',', ''))
            try:
                i.validate_trials(trials)
                num_trials = trials
            except ValueError:
                    print('Must be between 0 and 1 million')
        except ValueError:
            print('Must be an integer')
    elif str(trials) == 'quit':
        sys.exit('Quit')

#invest requested investment positions for the requested number of trials

results = pd.DataFrame(index = positions, columns = ['Mean', 'Standard Deviation']) #makes empty dataframe to store results
results.index.name = 'Position'

for investment in Investments:

    cumu_ret = np.array([])
    daily_ret = np.array([])
    cumu_ret = v.simulate_trials(investment, num_trials)
    daily_ret = [x/1000 - 1 for x in cumu_ret]
    
    results.loc[investment.position, 'Mean'] = np.mean(daily_ret) #should we format this as a percentage?
    results.loc[investment.position, 'Standard Deviation'] = np.std(daily_ret)
    
    plt.hist(daily_ret,100,range=[-1,1])
    #I found "zfill" here: http://stackoverflow.com/questions/134934/display-number-with-leading-zeros
    plt.savefig('histogram_' + str(investment.position).zfill(4) + '_pos.pdf')
    plt.clf()
    plt.cla()
    
results.to_csv('results.txt', sep = '\t', na_rep = 'NaN', float_format='%.4f')

cwd = os.getcwd()
print('all files exported to ' + str(cwd))

