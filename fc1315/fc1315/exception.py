
class InputError(Exception):
    '''
    Exception raised for errors in the input.
    '''
    def __str__(self):
        return 'Invalid input'
