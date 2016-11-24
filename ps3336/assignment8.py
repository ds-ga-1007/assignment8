'''
Created on Nov 23, 2016
@author: peimengsui
@desc: Program to simulate investment combination daily return 
'''

from investment import *
import sys

if __name__ == "__main__":
    while True:
        try:
            positions = input("Please enter a list of the number of shares to buy in parallel: e.g. [1, 10, 100, 1000]: \n")
            if positions == "quit":
                sys.exit(1)
                break;
            if positions[0]!='[' or positions[-1]!=']' or any(x not in [1,10,100,1000] for x in [int(t) for t in positions[1:-1].split(",")]):
                raise ValueError
            num_trials = input("Please enter number of trials: \n")
            if num_trials == "quit":
                sys.exit(1)
                break;
            if not num_trials.isdigit() or int (num_trials) < 1:
                raise ValueError
            positions = [int(t) for t in positions[1:-1].split(",")]
            num_trials = int (num_trials)
            investment.invest_trial(positions, num_trials)
            break
        except ValueError:
            print ('invalid input')
        except KeyboardInterrupt:
            print ("user quit")
            sys.exit(1)
        except:
            print ('error')