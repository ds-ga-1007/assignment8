
class UserError(Exception):
    """Base user-defined exception class."""
    pass


class InvalidPositionException(UserError):
    """Raised when user-provided position is invalid"""

    def __init__(self, position):
        self.invalid_position = position

    def __str__(self):
        return "You've provided an invalid position: '{}'. " \
               "Try passing a list of positive integers (e.g. '1, 10, 100').".format(self.invalid_position)


class InvalidTrialException(UserError):
    """Raised when user-provided trial number is invalid"""

    def __init__(self, trial):
        self.invalid_trial = trial

    def __str__(self):
        return "You've provided an invalid simulation count: '{}'. " \
               "Try passing a positive integer (e.g. '1', '1000', '10000').".format(self.invalid_trial)
