'''
Created on Nov 28, 2016

@author: Zahra Kadkhodaie
'''
### Assignment 8
### Zahra Kadkhodaie
### 11/28/2016
'''This program implements the investment class to run an investment simulation. It asks the user to enter a list of positions
and number of days. The total gain for each of the positions over the period of number of days is calculated in parallel. After 
program is run, one histogram daily returns is saved for each entered position. Also, a result file containing mean and standard 
deviations of the daily return distribution is saved on the current path. Users incorrect input is handled using specific 
exceptions and custom exception.'''

from investment import *
from total_gain import *

import matplotlib.pyplot as plt
from numpy import mean, std

while True: 
    '''This while gets a positions list from the user and checks for any possible invalid input.'''
    
    positions = input('Enter a list of the number of shares to buy in parallel: e.g. [1, 10, 100, 1000]: ')    
    try: 
        positions_revised = []   
        for items in positions.split(','):
            items = items.strip("'[]{}()")
            positions_revised.append(int(items))
            if int(items) not in [1,10,100,1000]:
                raise Not_a_Valid_Position()
                
        break  #break the while loop if the above block runs smoothly
    
    except ValueError:
        print('This is not a valid list of numbers. Please Try again.')
    
    except Not_a_Valid_Position: #Custom exception
        print('A position must be either of these values: 1, 10, 100, 1000')  

while True:
    '''This while gets the number of trials and makes sure the input is valid.'''
    num_trials = input('How many times to randomly repeat the test? ')
    if num_trials.isdigit():
        if int(num_trials) == 0:
            print('Zero is not a valid number. Please Try again.')
        else:
            num_trials = int(num_trials)
            break
    else: 
        print('Number of trials must be apositive integer. Please Try again.')

        
results = open("results.txt", "w")
for position in positions_revised:
    total_gain_postion = total_gain(position, num_trials) #find the total gain for any position in the input list
    expected_gain_total = mean(total_gain_postion) 
    std_postion = std(total_gain_postion)
    
    with open('results.txt', 'a') as myfile:
        myfile.write('mean and standard deviation for postion ' + str(position) + 
                    ' are: ' + str(expected_gain_total) + ' and ' + str(std_postion) + "\n")
        plt.clf()
        plt.hist(total_gain_postion, 100, range=[-1,1])
        plt.xlabel('daily gain')
        plt.title('Daily gain frequencies over ' + str(num_trials)+ ' days, for position ' + str(position))
        filename = 'histogram_' + str(position) + '_pos.pdf'
        plt.savefig(filename)