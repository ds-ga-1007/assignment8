'''
Created on Nov 27, 2016

@author: Christine
'''

import sys
from investment import investment
from errors import *
'''
This is the main program that runs simulation 10000 times to determine how to make investment on a single day.
Also, it plots histogram for position 1, 10, 100, and 1000, and calculates mean and standard deviation for each position.
'''
while True:
    try:
        position_input = input("Please enter a list of number of shares to buy in parallel.")
        position_input = position_input.replace(' ','')
        if position_input == 'quit':
            break
        else:
            positions = PositionInput(position_input).positions
            break
    except KeyboardInterrupt:
        sys.exit(0)
    except EOFError:
        sys.exit(0)
            
while True:
    try:
        trial_input = input("How many times to randomly repeat this test?")
        trial_input = int(trial_input)
        if trial_input == 'quit':
            break
        else:
            num_trials = TrialInput(trial_input).num_trials
            break
    except KeyboardInterrupt:
        sys.exit(0)
    except EOFError:
        sys.exit(0)

#Create a text file and write mean and standard deviation for each position in this text file
f = open('results.txt','w')
for position in positions:
    invest = investment(position,num_trials)
    invest.histogram() 
    f.write('Position:' + str(position) + ',' + 'mean:' + str(invest.stats()[0]) + ',' + 'std:' + str(invest.stats()[1]) + '\r\n')
f.close()
            