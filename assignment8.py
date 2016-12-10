'''
Created on Nov 24, 2016
@author: danielamaranto
This program accepts a list of integers from a user and assumes the user enters the list with surrounding brackets,
as indicated in the instructions.  For any set of integers, it will create an array of individual trials of 
daily return on investment for each position entered by the user.  It will generate 1 text file of the mean and
standard deviation of each position, and it will generate a separate histogram for each position.

I am the sole author of this program, but I have included my references where applicable.
'''

#Import functions and a class from separate modules
import outputs
from investment import investment_position

def main():
    complete = False
    while complete is False:
        # Get input from user: 1 list of positions and the number of trials
        position_input = input('Enter a list of investments:').replace(' ','')[1:-1]  #Surrounding brackets deleted
        trials_input = input('Enter a number of trials:').replace(' ','')
        
        try:
            investments = [int(i) for i in position_input.split(sep=',')]
            num_trials = int(trials_input)
            files = 1
            with open('results.txt', 'w') as file:    #If user is re-running, this will wipe the 
                file.write('')                                     #text file clean
            print('Generating output...')
            for i in investments:
                files = files + 1                                  #A histogram is generated for each position and a text
                position = investment_position(i,num_trials)       #file is generated for all positions collectively.
                outputs.generate_statistics(position)
                outputs.generate_histogram(position)
            print(str(files) + ' files generated.')
            complete = True
        
        # All invalid entries are handled here, including floats, alphabetical entries, etc.
        except ValueError:
            print('Invalid input\n')
        except IndexError:
            print('Invalid input\n')
        except UnboundLocalError:
            print('Invalid input\n')
        except TypeError:
            print('Invalid input\n')
        except KeyboardInterrupt:
            print('Invalid input\n')


if __name__ == '__main__':
    main() 