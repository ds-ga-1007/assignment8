'''
Created on Nov 28, 2016

@author: muriel820
'''
import numpy as np
import matplotlib as plt
import sys
from ym1495_assignment8.exceptions import *
from ym1495_assignment8.investments import *
from ym1495_assignment8.simulations import *
def main():
    while True:
        positions_input = input('Input a list of the number of shares: ')
        num_trials_input = input('Input how many times to ramdomly repeat the test, please type quit if you want to quit: ')
        try:
            positions = investments(positions_input)
            num_trials = trials(num_trials_input)
            position_value = position_values(positions)
            with open('results.txt', 'w') as f:   #save the results to result.txt
                for i in range(len(positions)):
                    daily_ret = multiple_trials(position_value[i], positions[i], num_trials)
                    plot_investment(position_value[i], positions[i], num_trials)
                    f.write('\n' + 'Positions: ' + str(positions[i]) + ' Position values: '+ str(position_value[i]) + ' trial numbers: ' + str(num_trials))
                    f.write('\n' + 'the mean of the daily return is: ' + str(np.mean(daily_ret)))
                    f.write('\n' + 'the standard deviation of the daily return is: ' + str(np.std(daily_ret)))

        except input_bound_exception and input_value_exception and input_trial_number_exception:
            print("Invalid input, please try again") 
        loop_continue = input('continue for another loop? \n (Enter no/n to exit the program, enter other words to start a new loop)')
        if str.lower(loop_continue) == 'no' or str.lower(loop_continue) == 'n':   #enter no/n(upper is allowed) to exit the program
            sys.exit()
if __name__ == '__main__':
    main()