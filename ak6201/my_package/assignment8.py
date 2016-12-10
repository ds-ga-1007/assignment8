'''
Created on Nov 27, 2016

@author: Akash
'''
from investment_main import investmnt
import sys

def loop():
    loop_trial = 'y'
    

    try:
        while(loop_trial == 'y'):
            print('\n INSTRUCTIONS:')
            print('You need to invest $1000 on the shares based on every denominations')
            print('You have 4 denominations : $1, $10, $100, $1000.')
            print('Hence you will buy 1000 shares to invest using $1, 1 share to invest using $1000 and same rule applies for $10 and $100.')
            print('You may enter your input as a list! Ex: [1,10,100,1000]\n')
            trial_sample = investmnt()
            
            try:
                position_list = input('> Enter the position values! ')
                trial_sample.check_valid_position_list(position_list, 1) # checks if it is valid input for positions list
            except KeyboardInterrupt:
                print("Keyboard Exit! Quitting..")
                sys.exit()
                
            if trial_sample.valid_input == 1: # if the position values entered is valid, then input num_trials
                try:
                    num_trials = input('> Enter the number of trials! (Only an integer value) ') 
                    trial_sample.check_valid_num_trials(num_trials, 1)  # checks if it is valid input for num_trials
                except KeyboardInterrupt:
                    print("Keyboard Exit! Quitting..")
                    sys.exit()
                    
                if trial_sample.valid_input == 1:
                    trial_sample.simulate(position_list, num_trials)  # it runs the simulation if the inputs are valid
                    
            loop_trial = input('Do you want to continue or not? Press y to continue or hit any other key combination to exit (including Ctrl-C)')
    except KeyboardInterrupt:
        print("Keyboard Exit! Quitting..")
        sys.exit()

    
    
if __name__ == "__main__":
    try:
        loop()
    except EOFError:
        pass