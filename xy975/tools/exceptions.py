'''
Check if the input arguments valid.
'''
def positioins_valid(positions):
    """
    To check if the input positions is a list of valid integer, 
    i.e. 1, 10, 100 or 1000.
    """
    if type(positions) != list:
        raise ValueError("Input positions should be a list.")
    else:
        for i in positions:
            if i not in [1, 10, 100, 1000]:
                raise ValueError("Elements in positions should be 1, 10, 100 or 1000.")
                
def num_trials_valid(num_trials):
    """
    To check if the input num_trials is a positive integer. 
    """
    if type(num_trials) != int:
        raise ValueError("Input num_trials should be an integer.")
    elif num_trials <= 0:
        raise ValueError("Input num_trials should be positive.")
        