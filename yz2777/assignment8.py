""" Main program for checking user input and connect class invest """

from class_invest import invest
import numpy as np
import matplotlib.pyplot as plt


# give a constraint of input for the positions list such that
# we can only input number,comma and space

numbers = list(range(10))  # list the numbers
    
# convert to a list of number strings
initial_num = []
for i in numbers:
    initial_num.append(str(i))
numbers_string = initial_num
    
# add comma and space to our constraint
constraint = numbers_string + [' '] + [',']
    

# Check whether the positions list is input correct

def pos_input_correct(positions_string):
     
    # check whether each element from input fulfill the constraint
    positions_string_list = list(positions_string)
    check_list=[]
    for element in positions_string_list:
        if element in constraint:
            flag = 0    # fulfill the constraint
        else:
            flag = 1    # not fulfill 
        check_list.append(flag)
    final_list = check_list
    
    # set a comparison group assuming all elements from the input are correct, that is, all flags are zeros
    comparison = list(np.zeros(len(final_list)))
    
    # if the positions are input correctly, split the string by ","
    if check_list == comparison:
        positions_split = positions_string.split(',')
    else:
        positions_split = ['wrong']
    
    return positions_split



# check whether the number of trials is correct

def num_input_correct(num_string):
    list_number = list(num_string)
    check_number = []
    for element in list_number:
        if element in numbers_string:
            flag = 0    # fulfill the number requirement
        else:
            flag = 1    # not fulfill 
        check_number.append(flag)
    final_number = check_number
    
    # set a comparison group assuming all elements from the input are correct, that is, all flags are zeros
    comparison = list(np.zeros(len(final_number)))
    
    if final_number == comparison:
        integer = int(num_string)
    else:
        integer = -9999 # using negative number to indicate invalid input 
    return integer



# user input
def inpt():
    
    #### part 1 input positions list
    position_input = input('Please enter a list of the number of shares (positions) to buy, for example, 1,10,100,1000; Or enter Q to quit \n')
    
    indicator_1 = 1   # first, give an indicator for input, 0 means incorrect input and 1 means correct 
    
    # if user doesn't input 'Q' to quit, we first convert the user input (e.g. "1,10,100") to what we need (e.g., ['1','10','100'])
    # And, check whether the input is correct or not
    if position_input != 'Q':
        convert_input = pos_input_correct(position_input)
        for i in range(len(convert_input)):
            ind = convert_input[i]
            if num_input_correct(ind) == -9999:  # if any element in the list is invalid, indicator=0
                indicator_1 = 0
                break
    
    # this while loop will check whether the user input is correct again and again until the input is correct
    while position_input != 'Q' and indicator_1 == 0:
        position_input = input('Your input is incorrect. Please enter a list of the number of shares (positions) to buy, for example, 1,10,100,1000; Or enter Q to quit \n')
        
        if position_input != 'Q':
            convert_input = pos_input_correct(position_input)
            for i in range(len(convert_input)):
                ind = convert_input[i]
                if num_input_correct(ind) == -9999:
                    indicator_1 = 0
                    break
                else:
                    indicator_1 = 1
                    
    #### part 2 input number of trials and check the correct
    # this part will be executed when part 1 complete and not enter 'Q'
    if position_input != 'Q':
        indicator_2 = 1;      # again, first set an indicator to indicate correct (1) or incorrect input (0) 
        trials_input = input('Enter the number of times to randomly repeat the test; Or enter Q to quit \n')
        
        if num_input_correct(trials_input) == -9999:
            indicator_2 = 0
        
        while trials_input != 'Q' and indicator_2 == 0:
            indicator_2 = 1
            print('Invalid input')   # print invalid when incorrect input occur and ask user input again 
            trials_input = input('Enter the number of times to randomly repeat the test; Or enter Q to quit \n')
            if num_input_correct(trials_input) == -9999:
                indicator_2 = 0
            if trials_input == 'Q':
                break
            
    #### part 3, if there is no invalid input we will output the histogram and results.txt 
    if position_input != 'Q' and trials_input != 'Q':
        new_position_list = []
        for position in pos_input_correct(position_input):
            new_position_list.append(int(position))
        final_position_list = new_position_list
        invest(final_position_list,int(trials_input)).bet() # use the class invest to get plots and results
    
if __name__ == "__main__":
    try:
        inpt()
    except KeyboardInterrupt:     # based on the assignment require, set exception for KeyboardInterrupt
        print('Interrupted by the keyboard')
