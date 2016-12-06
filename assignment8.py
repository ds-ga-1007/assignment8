import sys
from investment import *
import numpy as np
import numpy.random as rand
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt

"""
This main program simulates through investments of $1, $10, $100 and $1000 in order to
see how this affects returns based on a probability 0.49 of losing the investment vs
a probability of 0.51 of getting double the investment.
"""

positions = []
def main():
    while True:
    """
    Asks user for position
    """ 
        try:
            position = input("Enter a list of the number of shares to buy in parallel: ")
            if (position == 'quit'):
                sys.exit()
            position = str(position)
            position = position.strip()
            separated = position[1:-1].split(",")
            positions = [int(s) for s in separated]
            break
        except ValueError:
            print ('Error in input: try again')
        except KeyboardInterrupt:
            print()
            sys.exit()
        except EOFError:
            print()
            sys.exit()
    
    while True:
    """
    Asks user for number of trials
    """
        try:
            num_trials = int(input('Enter the number of times you would like to repeat the test: '))
            break
        except ValueError:
            print ('Error in input: try again')
        except KeyboardInterrupt:
            print()
            sys.exit()
        except EOFError:
            print()
            sys.exit()

	resultInv = investment(positions, num_trials)

	resultInv.results(positions, num_trials)

    
if __name__ == "__main__":
    main()
            
