class InvalidListError(Exception):
    """Exception raised for errors in the input."""
    def __str__(self):
        return 'The position list you input is invalid. Please try again.'

class PositionError(Exception):
    def __str__(self):
        return 'The positions in your list is invalid. Please try again.'

class IntegerError(Exception):
    def __str__(self):
        return 'The number of trial must be an integer. Please try again.'