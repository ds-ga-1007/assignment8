"""
Utilities for Simulation class.
"""


def check_positions_instance(positions):
    if not isinstance(positions, list):
        raise ValueError("\"positions\" should be a list of positive integers.")
    for i, p in enumerate(positions):
        if not isinstance(p, int):
            raise ValueError("Elements in \"positions\" should be integers.")


def check_positions_value(positions):
    valid_positions = [1, 10, 100, 1000]
    for i, p in enumerate(positions):
        if p not in valid_positions:
            raise ValueError("Not a valid position. The allowed positions are [1, 10, 100, 1000].")


def check_trials_instance(num_trials):
    if not isinstance(num_trials, int):
        raise ValueError("The number of \"trials\" should be an integer.")


def check_trials_positive(num_trials):
    if num_trials <= 0:
        raise ValueError(
            "The number of \"trials\" should be greater than 0. The current value passed is \"%s\" " % str(
                num_trials))
