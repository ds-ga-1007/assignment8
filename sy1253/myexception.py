
class FormatError(Exception):
    def __str__(self):
        return 'your input is not in the correct format, please enter again: '




class invalidPositionError(Exception):
    def __str__(self):
        return 'all the positions have to be in a positive integer form, please enter again.'

