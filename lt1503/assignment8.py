import sys
import Position
import numpy as np


# prompt_user is the main function that a user interacts with to create intervals
def prompt_user():
    """get list of intervals to start, then get one more interval at a time.
    'quit' or ctrl+c exits"""
    positions = []
    while True:
        try:
            positions_input = input("List of positions?")
            

            # Raises a ValueError and loops back if user_input is not correctly structured
            # as a sequence of powers of 10
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

    pos_ret = np.empty((num_trials, len(positions)))
    #cumu_ret = np.empty(num_trials)
    #daily_ret = np.empty(num_trials)
    cumu_ret = np.empty((num_trials, len(positions)))
    daily_ret = np.empty((num_trials, len(positions)))
    for trial in range(num_trials):
        for pos_idx, position in enumerate(positions):
            position.total_value = 0             
            position.bet_shares_independently()
            pos_ret[trial, pos_idx] = position.total_value
        cumu_ret[trial] = pos_ret[trial,:]
        daily_ret[trial] = (cumu_ret[trial]/1000) - 1
        
    print(daily_ret)


if __name__ == '__main__':
    prompt_user()
