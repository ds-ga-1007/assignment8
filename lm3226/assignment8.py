"""
Date: Nov 28, 2016
Author: Chloe Meng(lm3226)
Description: This program simulates the expected daily return of investing
different denominations. This program asks for user inputs, and
generate histogram for user inputs. It also generates histogram for a given example
denominations input as well as their corresponding statistics. Histogams would
be saved as pdf, and the statistics would be saved as text.
"""

import numpy as np
import matplotlib.pyplot as plt
import sys
from daily_investment_return import *

class InvalidUserInputException(Exception):
    pass

def validate_denominations_input(denominations):
    for i in range (0, len(denominations)):
        if denominations[i] not in [1, 10, 100, 1000]:
            raise InvalidUserInputException("Invalid input.")

def main():
    try:
        while True:
            try:
                user_input = input('''Suppose that you want to invest $1000.
                You can purchase it in $1, $10, $100, $1000 denominations.
                Please enter a list of denominations without dollar sign that
                you want to purchase and separate each denomination by a comma,
                such as 1,10,100,1000: '''
                )
                input_denominations = np.fromstring(user_input, dtype=int, sep=',')
                validate_denominations_input(input_denominations)
            except (ValueError, InvalidUserInputException) as e:
                print('Invalid input. Please try again: ')
                continue
            else:
                while True:
                    try:
                        user_num_input = input('Choose the number of times you want to invest: ')
                        user_num_trials = int(user_num_input)
                        if user_num_trials <= 0:
                            raise InvalidUserInputException
                    except (ValueError, InvalidUserInputException) as e:
                        print('Invalid input. Please try again: ')
                        continue
                    else:
                        user_invsetment = daily_investment_return(input_denominations, user_num_trials)
                        user_invsetment.generate_results()

                        print('Now generating example results with denominations of [1,10,100,1000] and 10000 trials')
                        example_investment = daily_investment_return([1,10,100,1000], 1000)
                        example_investment.generate_results()
                        break
                break

    except (KeyboardInterrupt, EOFError) as e:
        sys.exit(0)

if __name__ == '__main__':
    main()
