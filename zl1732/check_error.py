'''
this program is responsible for error_checking
all errors are specified here
'''

def check_positions(positions):
    '''
    Check error in positions
    '''
    if positions=="":
        raise ValueError("Empty! you need to input positions")
    # check if the input is empty
    
    splited_positions = positions[1:-1].split(', ')
    if positions[0] != "[" or positions[-1] != "]":
        raise ValueError("Invalid positions format, positions need to be a list capped with [ and ]")
    # if the input is not in a square bracket
    
    if len(splited_positions)==1:
        raise ValueError("Invalid positions delimiter, need to use ', '")
    # if the input is not correctly delimited
    
    for item in splited_positions:
        try:
            int(item)
        except:
            raise ValueError("Invalid positions input, all positions should be number")
        if int(item)<0:
            raise ValueError("Invalid positions input, all positions should be positive")
    # check if each element in the list are positive integers
    
    
def check_trails(trails):
    '''
    Check error in num_trails
    '''
    if trails=="":
        raise ValueError("Empty! you need to input trails")
    # check if the input is empty
    
    try:
        int(trails)
    except:
        raise ValueError("Invalid trails input, trails should be a number")
    if int(trails)<0:
        raise ValueError("Invalid trails input, trails should be positive")
    # check if each element in the list are positive integers