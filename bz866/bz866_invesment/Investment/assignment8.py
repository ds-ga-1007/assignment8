'''
Created on 2016年11月日

@author: bz866
'''

from Investment.investment import *
from Investment.exp_handle import *

while True:
    try:
        positions = eval(input('Please input a list of positions.\n'))
        num_trials = eval(input('Please input the number of trials.\n'))
        stimulationInit = trialInput(positions, num_trials)
        stimulationInit.stimulate()
        break
    except InvalidListError:
        print('Invalid position list.')
    except PositionError:
        print('Invalid positions in your list.')
    except IntegerError:
        print('Invalid Value. Trail number must be a integer.')

if __name__ == '__main__':
    pass 