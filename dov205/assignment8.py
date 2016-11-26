"""
    Author:
        Danny Vilela

    Program Behavior:
        This script can be run from the terminal like so:

            $ python assignment8.py

        The program will prompt you (the user) for a list of positions. Until
        the user-provided input is valid, the program will either (1) terminate
        if you provide 'q', 'quit', or 'exit' or (2) continue to prompt the user
        for valid input while demonstrating what was invalid in the most recent input.

        Next, the program will prompt you for a valid simulation count. This
        validation follows effectively the same validation schema as before: it
        will terminate if you indicate a common termination synonym, tell you
        what was incorrect about your most recent input, or continue with valid
        inputs.

        The program uses the above two components in order to perform its
        simulations. All output files are written to the local directory.

    Efficiency:
        On my machine, running the full-fledged simulation in IPython:

            %timeit simulate([1, 10, 100, 1000], 10000)

        takes approximately 2.35 seconds. I figure this is efficient enough.
        There *is* room for improvement: I believe utilizing numpy's
        broadcasting would allow us to get this done in under 2 seconds.
"""

from Investment.Investment import *
from Investment.UserError import *

from typing import List
import matplotlib.pyplot as plt
import numpy as np
import sys
import re

INITIAL_HOLDINGS = 1000


def main():

    # Receive, parse initial input.
    positions, num_trials = receive_initial_input()

    # Run simulation for all positions in :positions.
    simulate(positions, num_trials)


def receive_initial_input() -> (List[int], int):
    """Encapsulation for user-interfacing prompts.

    :return: positions: list of positions we would like to simulate.
    :return: num_trials: number of trials we would like to simulate.
    """

    # Prompt user for requested positions.
    positions = receive_positions_input()

    # Prompt user for requested trial count.
    num_trials = receive_num_trials_input()

    # Return valid positions and trial count for simulation.
    return positions, num_trials


def receive_positions_input() -> List[int]:
    """Prompt user for position list. Reject if any invalid, accept if all valid.

    :return: positions: strictly-valid list of potential positions.
    """

    # Define our user-interfacing prompt for positions.
    prompt = "Please enter a comma-separated list (e.g. '1, 10, 100, 1000') of shares to buy in parallel: "

    # Ad-infinitum.
    while True:

        # Prompt our user for input.
        response = prompt_input(prompt)

        # Quit if user wants to quit.
        if response.lower() in ['q', 'quit', 'exit']:
            sys.exit(1)

        try:
            # Attempt to parse user-provided positions.
            positions = parse_positions(response)

            # Return valid positions if we make it this far.
            return positions

        # Catch exception thrown in parse_positions().
        # Inform user of their invalid entry and repeat.
        except InvalidPositionException as ipe:
            print(ipe, file=sys.stderr)


def prompt_input(prompt):
    """Modular way to get a user's response that also handles exceptions.

    :param prompt: string shown to user describing what to respond with.
    :return: string representation of user's response.
    """

    try:
        # Prompt user for their input response.
        response = input(prompt)

        # Return user's response, if we make it this far.
        return response

    # Handle termination errors and interrupts.
    except EOFError:
        print("")
        sys.exit(1)

    except (KeyboardInterrupt, SystemExit):
        print("")
        sys.exit(1)


def parse_positions(positions: str) -> List[int]:
    """Validate each of our user's positions. Reject if any are invalid.

    :param positions: user-input string of potentially-valid positions.
    :return: valid_positions: list of valid positions. Raises exception if any invalid.
    """

    # Split user input on commas and initialize valid position container.
    split = positions.split(',')
    valid_positions = []

    # Evaluate each proposed position.
    for position in split:

        # Run both regular expressions on our proposed position.
        # If only expected_match() matches, our position is valid.
        if expected_match(position) and not float_match(position):
            valid_positions.append(int(position))

        else:
            # Raise exception if any position in positions is invalid.
            raise InvalidPositionException(position.strip())

    return valid_positions


def expected_match(user_input):
    """Perform first-pass pattern-match against user input.

    :param user_input: user-provided position or trial input.
    :return: boolean denoting whether our traditional-matching succeeded (true).
    """

    # Return whether our expression matches the proposed input.
    # If it *does*, we have a valid input that should be further
    # evaluated in float_match().
    # This expression handles:
    # \s*    Any leading whitespace (e.g. '   10')
    # [+]?   An optional indication of positive-signed integer.
    # [0]*   Zero or more leading zeros.
    # [1-9]  Single match on digits in the interval [1, 9]
    # [\d]*  Zero or more digit values in the interval [0, 9].
    # \s*    Any trailing whitespace (e.g. '10      ')
    # Note: our expression does not accept negative positions (e.g. '-20').
    return re.match(r'\s*[+]?[0]*[1-9][\d]*\s*', user_input) is not None


def float_match(user_input):
    """Perform second-pass match to detect float-y input.

    :param user_input: user-provided position or trial input.
    :return: boolean denoting whether our float-matching succeeded (true).
    """

    # Return whether our expression matches the proposed input.
    # If it *does*, we have a valid input that can be accepted.
    # \s*    Any leading whitespace (e.g. '   10')
    # [+]?   An optional indication of positive-signed integer.
    # [0]*   Zero or more leading zeros.
    # [1-9]  Single match on digits in the interval [1, 9]
    # [\d]*  Zero or more digit values in the interval [0, 9].
    # \s*    Any trailing whitespace (e.g. '10      ')
    # Note: our expression does not accepts negative positions (e.g. '-20').
    return re.match(r'\s*[+]?[0]*[1-9][\d]*\.[\d]*\s*', user_input) is not None


def receive_num_trials_input() -> int:
    """Prompt user for simulation count. Reject if invalid, accept if valid.

    :return: num_trials: strictly-valid integer representing simulation
    """

    # Define our user-interfacing prompt for trial count.
    prompt = "How many times (e.g. 10) would you like to simulate those purchases? "

    # Ad-infinitum.
    while True:

        # Prompt our user for input.
        response = prompt_input(prompt)

        # Quit if user wants to quit.
        if response.lower() in ['q', 'quit', 'exit']:
            sys.exit(1)

        try:
            # Attempt to parse user-provided simulation count.
            num_trials = parse_trial(response)

            # Return valid trial count if we make it this far.
            return num_trials

        # Catch exception thrown in parse_trial().
        # Inform user of their invalid entry and repeat.
        except InvalidTrialException as ite:
            print(ite, file=sys.stderr)


def parse_trial(trial: str) -> int:
    """Validate our user's proposed simulation count. Reject if invalid.

    :param trial: user-input string representing requested trial count.
    :return: integer-casted :trial if valid. Raises exception if invalid.
    """

    # Run both regular expressions on our proposed position.
    # If only expected_match() matches, our position is valid.
    if expected_match(trial) and not float_match(trial):
        return int(trial)

    else:
        # Raise exception if our trial is invalid.
        raise InvalidTrialException(trial)


def simulate(positions: List[int], num_trials: int):
    """Simulate :num_trials independent days of trading :positions-value investments.

    :param positions: list of positions we would like to simulate.
    :param num_trials: number of trials we would like to simulate.
    :return:
    """

    # Open stream to output file that'll close itself.
    with open('results.txt', 'w') as file:

        # Perform :num_trials simulations for each position in positions
        for position in positions:

            # Simulate position :position a :num_trials number of times.
            # (e.g., len(cumu_ret) == len(daily_ret) == num_trials)
            cumu_ret, daily_ret = simulate_position(position, num_trials)

            # Obtain mean and standard deviation of daily returns across all trials.
            daily_ret_mean, daily_ret_std = np.mean(daily_ret), np.std(daily_ret)

            # Write requested information to results file for each position.
            file.write('For position = {:4}: mean = {:.4}, standard deviation = {:.4}.\n'.format(position,
                                                                                                 daily_ret_mean,
                                                                                                 daily_ret_std))

            # For the given position, plot and save a detailed histogram
            # of our daily returns across :num_trials trials.
            output_plot(daily_ret, position)


def simulate_position(position: int, num_trials: int) -> (np.ndarray, np.ndarray):
    """ Perform :num_trials simulations of :position investments.

    :param position: amount of money we're investing into each investment.
    :param num_trials: number of days we'll be simulating.
    :return: cumu_ret: for each day, a cumulative sum of returns on investment(s).
    :return: daily_ret: for each day, a standardized return on investment(s).
    """

    # Split your initial holdings evenly over the number of investments
    # you'd like to make (e.g. if positions = 1, you have 1 $1000
    # investment; positions = 5 you have 5 $200 investments, etc.).
    position_value = INITIAL_HOLDINGS / position

    # Create :position investments, each with :position_value invested.
    investment_returns = build_investment_array(position_value, position)

    # Initialize cumulative return container to a vector of zeros.
    cumu_ret = np.zeros(num_trials)

    # For each day of maturing investments, simulate results.
    for day in range(num_trials):

        # Obtain cumulative and daily return values.
        cumulative_results = accumulate_returns(investment_returns, position)

        # Save our results in their respective containers
        cumu_ret[day] = cumulative_results

    # Define :daily_ret to be each element of :cumu_ret divided by our
    # initial holdings (1000), subtract 1.
    daily_ret = np.divide(cumu_ret, INITIAL_HOLDINGS) - 1

    # Return our cumulative and daily return results across all days.
    return cumu_ret, daily_ret


def build_investment_array(position_value: [int, float], position: int):
    """Build numpy array of Investment positions.

    :param position_value: ratio of initial holdings over number of investments.
    :param position: number of investments to be made.
    :return: investments: array of Investment positions.
    """

    # Define initial array containing a single investment's position.
    base = np.array([Investment(position_value).position])

    # Utilize numpy's repeat method to create an array of size :position
    # containing copies of our :base array.
    investments = np.repeat(base, position)

    # Return our array of Investment positions.
    return investments


def accumulate_returns(investments: np.ndarray, position: int) -> np.ndarray:
    """Calculate one day's worth of returns on investment(s).

    :param investments: array of Investment positions.
    :param position: number of random values to generate (equal to the number
        of investments, e.g. len(investments))
    :return: dot product (sum of pairwise multiplication) of investment amounts
        and a randomly-generated array of 0 or 2 (denoting investment failure or
        success, respectively).
    """

    # Generate numpy array of length :position containing either 0 or 2.
    # These values will be one-to-one with each investment in order to
    # determine whether the investment failed or doubled.
    gamble_returns = biased_gamble(position)

    # Our cumulative results are calculated by taking the product
    # of each investment's position and return multiplier (0 or 2)
    # and summing it up. So, return the dot product.
    return np.dot(investments, gamble_returns)


def output_plot(daily_ret: np.ndarray, position: int):
    """Build and save output plot representing distribution of returns.

    :param position: amount of money invested into each investment.
    :param daily_ret: numpy array of normalized returns across all simulated days.
    :return: PDF containing detailed plot of returns on investment over all simulations.
    """

    # Establish base histogram plot of daily returns, split across 100 buckets.
    plt.hist(daily_ret, 100, range=[-1, 1])

    # Set plot title, x and y labels, etc. Nice-to-haves for looking at plots.
    plt.title("Distribution of returns on investment at position = ${}".format(position))
    plt.xlabel("Returns relative to position")
    plt.ylabel("Outcome Frequency")
    plt.grid(True)

    # Save figure to appropriate file location. Note: we utilize string
    # formatting on the filename in order to appropriately fill the
    # position identifier with zeros.
    plt.savefig("histogram_{}_pos.pdf".format(str(position).zfill(4)))

    # Close plot to release memory required for current figure.
    plt.close()


if __name__ == '__main__':
    main()
