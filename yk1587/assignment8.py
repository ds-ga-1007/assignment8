'''
Created on 2016.11.27

@author: keyaohan
'''
from program.simulations import *
from program.exceptions import *

while True:
    try:
        positions = eval(input('Please input a list of positions.\n'))
        num_trials = eval(input('Please input the number of trials.\n'))
        simulationInit = trialInput(positions, num_trials)
        simulationInit.simulate()
        break
    except InvalidListError:
        print('The position list you input is invalid. Please try again.')
    except PositionError:
        print('The positions in your list is invalid. Please try again.')
    except IntegerError:
        print('The number of trial must be an integer. Please try again.')

if __name__ == '__main__':
    pass