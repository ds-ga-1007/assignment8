'''
This package is for a simulation of investment. 
It takes a input of list of positions and number of trials of user and generates a reports
about the mean and variance of the investment as well as relevant histogram. 
The simulation will stop when user inputs "QUIT".
    
This is the main script.
Created on Nov 21, 2016
Last Modified        : 
Version        : 1.0
@author: Nan Wu
@email: nw1045@nyu.edu
'''
import sys
import os
import investment_simulation
from UserDefinedError import QuitSimulation
if __name__ == '__main__':
    try:
        try:
            investment_simulation.investment_simulation()
        except QuitSimulation:
            print('Exit the Simulation...')
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
    