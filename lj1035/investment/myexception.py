# The NotIntegerError class extends from the Exception class.
class NotIntegerError(Exception):
    def __str__(self):
        return 'The input contains non-integer values. Please enter a valid input.\n'


# The NotPositiveIntegerError class extends from the Exception class.
class NotPositiveIntegerError(Exception):
    def __str__(self):
        return 'The input contains non-positive integers. Please enter a valid input.\n'


# The FormattingError class extends from the Exception class.
class FormattingError(Exception):
    def __str__(self):
        return 'This input is not in the correct format. Please enter a valid input.\n'


# The NotNumericError class extends from the Exception class.
class NotNumericError(Exception):
    def __str__(self):
        return 'This input contains non-numeric characters. Please enter a valid input.\n'
