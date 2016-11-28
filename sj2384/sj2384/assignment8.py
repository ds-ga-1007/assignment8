'''
This is the main module of the program. This module will take a list of position and a number of trials
as inputs and decide if user inputs are valid. If the inputs are valid, this program will return pdf file
of histogram and text file of stats of daily return performance

Created on Nov 28, 2016

@author: sj238
'''
from investment_simulation import *
import sys

def main():
    while True:
        try:
            positions = input('Please input a list of position like[1,10,100,1000] or enter quit to end:\n')
            '''
            check if input positions is valid
            if the list of positions is valid, then ask user to input number of trials
            '''
            if (positions == 'quit'):
                sys.exit()
            if positions == '':
                raise ValueError('Please input a list or quit')
            positions = positions.strip()
            positions = positions[1:-1].split(',')
            for i, item in enumerate(positions):
                positions[i] = int(item)
            for pos in positions:
                if int(pos) <= 0:
                    raise ValueError("Invalid input, all positions should be positive")
            break
        except KeyboardInterrupt:
            sys.exit()
        except EOFError:
            sys.exit()
    while True:
        try:
            num_trials = int(input('Please input a number of trials you want or enter quit to end:\n'))
            '''
            check if input number of trials is valid
            if valid, generate and save hidtograms and stats of daily return performance.
            '''
            if num_trials == 'quit':
                sys.exit()
            if num_trials == "":
                raise ValueError("PLeas input a number or enter quit")
            if num_trials <= 0:
                raise ValueError("Invalid input, number of trails should be positive")
            break
        except KeyboardInterrupt:
            sys.exit()
        except EOFError:
            sys.exit()
    #generate and save output using investment_simulation module using valid user input
    output = Investment(positions, num_trials)
    output.output_files(positions, num_trials)
if __name__ == '__main__':
    main()