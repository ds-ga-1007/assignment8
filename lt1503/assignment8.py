import sys
import Position
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# prompt_user_for_positions asks users for positions of shares
def prompt_user_for_positions():
    """get list of positions
    'quit' or ctrl+c exits"""
    positions = []
    while True:
        try:
            positions_input = input("List of positions?")

            # Raises a ValueError and loops back if user_input is not
            # a sequence of powers of 10 separated by commas
            positions = Position.get_position_list(positions_input)
            
            num_trials_input = input("num trials?")
            num_trials = Position.get_integer_if_possible(num_trials_input)
            break

        except KeyboardInterrupt:
            # Exit if the user enters Ctrl+C
            sys.exit(0)
        except EOFError:
            # Exit if the user enters Ctrl+D
            sys.exit(0)

        except ValueError:
            print("Invalid list of positions")
    return positions, num_trials


if __name__ == '__main__':
    """collect user input about investment options, then evaluate how 
    they perform over a day's random outcomes and store results to file"""
    positions, num_trials = prompt_user_for_positions()
    Position.process_one_day(positions = positions, num_trials = num_trials)
