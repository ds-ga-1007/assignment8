'''
This module contains specific self-defined exceptions/errors.

Author: Xianzhi Cao (xc965)
'''


# Error: Input is empty.
class EmptyInputError(Exception):
    def __str__(self):
        return 'Input Error! Empty input.\n'


# Error: Yes or No Error.
class YesOrNoError(Exception):
    def __str__(self):
        return 'Input Error! Please enter \'Y\' or \'N\'.\n'


# Error: positions set input does not match format.
class InputFormatError(Exception):
    def __str__(self):
        return 'Input Format Error! Please enter a list of positive numbers, eg.[1, 10, 100, 1000].\n'


# Error: positions set input does not match format.
class ZeroPositionError(Exception):
    def __str__(self):
        return 'Zero Position Error! Positions can only be positive integers.\n'


# Error: Number of trials should be numeric; float will be rounded to integer.
class NonNumericError(Exception):
    def __str__(self):
        return 'Non Numeric Error! Please enter a number.\n'


# Error: Number of trials should only be a positive integer.
class NonPositiveIntegerError(Exception):
    def __str__(self):
        return 'Non Positive Integer Error! Please enter a positive integer.\n'
