
class InvestmentError(Exception):
    """Base Investment exception class."""
    pass


class InvestmentPositionException(InvestmentError):
    """Raised when attempting to set an invalid position on an Investment."""

    def __init__(self, position):
        self.invalid_position = position

    def __str__(self):
        return "Attempted to hold an invalid investment amount '{}'. " \
               "Make sure investment is a positive value.".format(self.invalid_position)
