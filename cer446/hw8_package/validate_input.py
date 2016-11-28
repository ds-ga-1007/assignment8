'''
Created on Nov 22, 2016

@author: Caroline
'''
import re

#functions related to the position input

def take_position():
    '''Accepts user input for investment positions'''
    position_input = str(input("List of positions? "))
    return position_input
    
#helper functions for make_positions
    
def reject_irregular_characters(position_input):
    '''Raise error if unusual characters found'''
    normal_characters = '''[0-9] #numbers
                            |\s   #whitespace
                            |,    #commas
                            |\]   #forward bracket
                            |\[   #backwards bracket'''
    irregular_characters = len(position_input) - len(re.findall(normal_characters, position_input, re.X))
    if irregular_characters > 0:
        raise TypeError('Found {0} irregular character(s) that were not integers, commas, blanks, brackets'.format(irregular_characters))
    else:
        pass

def parse_input(position_input):
    if len(position_input) > 4 and ',' not in position_input:
        raise Exception ('Positions should be separated by commas')
    else:
        parsed_input = re.sub('[^0-9|,|.]', '', position_input)
        parsed_input = re.split(',', parsed_input)
        return parsed_input
    
def round_input(parsed_input):
    '''Round input to integer if possible'''
    positions = []
    for i in parsed_input:
        try:
            int(round(float(i)))
            positions.append(int(round(float(i))))
        except ValueError:
            print('Not all positions convert to integer. Failed input: \'{0}\''.format(str(i)))
            pass
    return positions
        
def check_positions(positions):
    '''confirm that there are values in the positions array'''
    if not positions:
        raise Exception('No valid integers identified')
    if positions:
        return positions

#make_positions uses preceding 4 helper functions

def make_positions(position_input):
    '''make positions from user input, raising errors where needed'''
    try:
        reject_irregular_characters(position_input)
        try:
            positions = round_input(parse_input(position_input))
            try:
                check_positions(positions)
                return positions
            except Exception as err3:
                print(err3)
        except ValueError as err2:
            print(err2)
    except TypeError as err1:
        print(err1)

#functions related to trial input

def take_trials():
    '''Accepts user input for number of trials'''
    trials = input('Number of trials? ')
    return trials

def validate_trials(num_trials):
    '''Verifies that the number of trials input is reasonable'''
    if num_trials >= 1000000:
        raise ValueError('Number of trials should be less than 1 million')
    if num_trials <= 0:
        raise ValueError('Number of trials must be more than 0')