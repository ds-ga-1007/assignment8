import numpy as np
import matplotlib.pyplot as plt

'''User-Defined Exceptions'''

class NonPositiveInteger(Exception):
    def __str__(self):
        return 'The "number of trials" must be a positive integer.\n'
      
class InvalidInvestmentValue(Exception):
    def __str__(self):
        return 'Investments must be made in $1, $10, $100, or $1000 denominations.\n'
    
class NoSquareBrackets(Exception):
    def __str__(self):
        return 'Input must be surrounded by square brackets.\n'


class Investment():
    '''This class defines an investment approach for one day of trading. The two inputted attributes are "position" 
    (the number of shares to be purchased) and "amount" (the amount of money to be invested that day). Note that
    "position" is inversely related to "position_value", such that position * position_value
    equals "amount".'''
    
    def __init__(self, amount, position):
        self.position = int(position)
        self.amount = int(amount)
        self.position_value = amount/position
        if self.position_value not in [1, 10, 100, 1000]:
            raise InvalidInvestmentValue

class Number_Trials():
    '''This class represents the number of trials (or trading days) to be run by the program.'''
    def __init__(self, number):
        self.number = int(number)
        if int(self.number) < 1:
            raise NonPositiveInteger

def determine_if_outcome_is_positive():
    '''This function randomly assigns investments to either a positive outcome (with 51% probability)
    or a negative outcome (with 49% probability). The function returns True if the outcome is positive,
    False if the outcome is negative.'''
    value = np.random.rand()
    if value > 0.49:
        return True
    else:
        return False

def simulate_bet(position_value):
    '''This function takes the amount invested (the "position_value" for a particular position) as input,
    and returns the amount remaining once the result of the bet is known. If the outcome is positive, the
    initial amount doubles; if the outcome is negative, the amount drops to 0.'''
    if determine_if_outcome_is_positive() == True:
        result = position_value*2
    else:
        result = 0
    return result

def convert_input_to_integer_list(string):
    '''This function takes a string with brackets and converts it into a list of integers.'''
    if string[0] != '[' or string[-1] != ']':
        raise NoSquareBrackets
    string = string[1: -1]
    new_list = string.split(',')
    for i in range(len(new_list)):
        new_list[i] = int(new_list[i])
    return new_list

def remove_duplicates(position_list):
    '''This function removes any duplicate elements in a list. For example, if the input for positions 
    is [1, 10, 10, 100, 1000], this function will transform the list to [1, 10, 100, 1000].'''
    position_array = np.array(position_list)
    new_position_list = list(np.unique(position_array))
    return new_position_list

def convert_results_to_string(position, position_value, daily_ret_array):
    '''This function converts the mean and standard deviation of a position's daily returns into a 
    text string.'''
    first_line = 'Position of {0}, each bet is ${1}'.format(position, position_value)
    second_line = 'Mean = {0}'.format(daily_ret_array.mean())
    third_line = 'Standard Deviation = {0}'.format(daily_ret_array.std())
    sequence = first_line + '\n' + second_line + '\n' + third_line
    return sequence

def add_string_to_file(position, position_value, daily_ret_array, file):
    '''This function writes a string into a text file.'''
    string_block = convert_results_to_string(position, position_value, daily_ret_array)
    file.writelines(string_block + '\n \n')

def generate_histogram(position, daily_ret_array):
    '''This function generates a histogram for the distribution of daily returns for a particular position.'''
    plt.figure()
    plt.hist(daily_ret_array, bins = 100, range = [-1, 1])
    plt.title('Distribution of Return for Position = {0}'.format(position))
    plt.xlabel('Return')
    plt.ylabel('Count')
