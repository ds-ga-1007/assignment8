'''
    This module includes classes that defines exception types.
'''

class InputTypeException(Exception):
    pass

class InputValueException(Exception):
    pass


'''
    Check if the input string is valid.
'''
def checkInput(positions):
    positions = positions.strip()
    if (positions[0] != '[') or (positions[-1] != ']'):
        raise InputTypeException('Input is not a list. A valid input can be something like \"[1, 10, 100, 1000]\".')
    for s in positions[1:-1].split(','):
        if not s.strip().isdigit():
            raise InputValueException('Input contains invalid values. A valid input can be something like \"[1, 10, 100, 1000]\".')