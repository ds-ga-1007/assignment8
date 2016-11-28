'''
The package is a simulation for investment. 
It takes the input by user of list of positions and number of trials and generates a txt file contains
the mean and standard deviation of the daily return as well as corresponding histograms. 
The simulation will stop when user prompts "quit".

Created on Nov 26, 2016
@author: Zhiqi Guo(zg475)
@email: zg475@nyu.edu
'''
from investment import investment
from investment import simulate
import sys

def main():
    while True:
        try:
            input_positions  = input('Plz enter a list of positions: ')
            num_trials = input('Plz enter the number of times to repeat test: ')
     
            if input_positions == 'quit' or num_trials == 'quit':
                sys.exit(0)
            if input_positions[0] != '[' or input_positions[-1] != ']':
                raise ValueError
            
            try:
                input_positions = input_positions.strip('[]').split(',')
                positions = [int(i) for i in input_positions]
            except ValueError:
                print('Invalid Input')
                
            if len(positions) != 4:
                raise ValueError
            for item in positions:
                if item not in [1,10,100,1000]:
                    raise ValueError
            
            if  not num_trials.isdigit() or int(num_trials) < 1 :
                raise ValueError
            num_trials = int(num_trials)
            
            simulate(positions,num_trials)
            
        except KeyboardInterrupt:
            print('Interrupted')
            sys.exit(0)
        except ValueError:
            print('Invalid Input')
    


if __name__ == '__main__':
    print('This is a simulation program for investment!')
    print('Need to prompt two variable, one is positions (a list of the number of shares to buy in parallel:e.g.[ 1, 10, 100, 1000])')
    print('Another is num_trials (how many times to randomly repeat the test: e.g. 10000)')
    main()