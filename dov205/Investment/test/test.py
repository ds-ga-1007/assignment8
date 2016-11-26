import unittest
from assignment8 import *


class InvestmentTest(unittest.TestCase):
    """Unit-testing class that allows us to run tests with expected outcomes.

    Run the test in the project's root directory (e.g. pwd should be '.../dov205/')
    with the following command:

        $ python -m unittest discover
    """

    def test_valid_creation(self):
        """Test the acceptance of valid inputs to Investment constructor."""

        # Initialize list of values we would expect to be valid Investments.
        valid = [i for i in range(1, 1000)] + [float(i) for i in range(1, 1000)]

        # Create valid Investment objects for each value in our :valid string list.
        investments = [Investment(position) for position in valid]

        # Assert that all values in :valid were passed into
        # Investment objects in :investments.
        self.assertEqual(len(valid), len(investments), 'Error: invalid investment value in :valid list.')

    def test_invalid_create(self):
        """Test the rejection of invalid inputs to Investment constructor."""

        # Initialize list of values we would expect to be invalid Investments.
        invalid = [4j, -1, -000000.00001, -.1, -0.4]

        # Container for any valid Investments.
        investments = []

        # Attempt to create invalid Investment objects for each string in our :invalid field.
        for candidate in invalid:
            with self.assertRaises(InvestmentPositionException):
                investment = Investment(candidate)
                investments.append(investment)

        # Assert that not a single Investment was instantiated.
        self.assertEqual(0, len(investments), 'Error: valid investment input in :invalid list.')

    def test_valid_position(self):
        """Test the acceptance of valid inputs to the Investment position parser."""

        # Initialize list of positions we would expect to be valid.
        valid = ['1, 10, 100, 1000',                 # Nice input
                 '1, 10, 100 ,       1000   ',       # Whitespace
                 '+1,   +10,   +100    ,+1000',      # Sign, whitespace
                 '1, 2, 3, 4, 5, 100, +1000'         # Mix
                 ]

        # Correctly parse and validate position list for each value in our
        # :valid string list.
        positions = [parse_positions(candidate) for candidate in valid]

        # Assert that all positions in :valid were valid position inputs.
        self.assertEqual(len(valid), len(positions), 'Error: invalid position input in :valid list.')

    def test_invalid_position(self):
        """Test the rejection of invalid inputs to the Investment position parser."""

        # Initialize list of positions we would expect to be invalid.
        invalid = ['', '  ', 'invalid',         # Empty string errors
                   '1,', '-1, 1', '1.0',        # Mix
                   '1.0, 10.0, 100.0, 1000.0',  # Floats
                   '-0', '0', '0.100'           # Zeros
                   ]

        # Container for any valid positions
        positions = []

        # Attempt to validate invalid position inputs for each string in our
        # :invalid container.
        for candidate in invalid:
            with self.assertRaises(InvalidPositionException):
                position = parse_positions(candidate)
                positions.append(position)

        # Assert that not a single position was accepted.
        self.assertEqual(0, len(positions), 'Error: valid position input in :invalid list.')

    def test_valid_trial(self):
        """Test the acceptance of valid inputs to the Investment trial parser."""

        # Initialize list of trials we would expect to be valid.
        valid = ['1', '10', '1000', '10000',  # Nice inputs
                 '+1', '+10000',              # Leading sign
                 '01', '01111',               # Leading zero
                 ' +01', '+11 ', ' +010000 '  # Whitespace
                 ]

        # Correctly parse and validate trial list for each value in our :valid string list.
        trials = [parse_trial(candidate) for candidate in valid]

        # Assert that all trials in :valid were valid trial inputs.
        self.assertEqual(len(valid), len(trials), 'Error: invalid trial input in :valid list.')

    def test_invalid_trial(self):

        # Initialize list of trials we would expect to be invalid.
        invalid = ['-1', '-001', ' -01', '-1.0',   # Gauntlet of -1s
                   '0', '0.0', '  00.0    '        # Gauntlet of 0s
                   ]

        # Container for any valid trials.
        trials = []

        # Attempt to validate invalid trial inputs for each string in our
        # :invalid container.
        for candidate in invalid:
            with self.assertRaises(InvalidPositionException):
                trial = parse_positions(candidate)
                trials.append(trial)

        # Assert that not a single trial was accepted.
        self.assertEqual(0, len(trials), 'Error: valid position input in :invalid list.')
