'''
Created on 2016.11.23

@author: xulei
'''

'''
This file is the main class which will be excuted when called in python. It would ask the user for a number as the number
of trails, then proceed to ask for a list of share numbers once the trail number is in the right format. The procedure 
will go on, which means it will keep asking number of trails and position list in turn. It will only stop when user calls
'quit' , through keyboard interuption, or press stop buttion if using Eclipse.
'''

from Exception_class import *
from input_object import *
from methods import *


def main():
    
    while True:
        print('Investment simulation starts! Input quit to exit the game')
        #The first loop get the number of trials until it is int
        while True:        
            try: 
                input_trial_num=input('Number of Trails?\n')
                if input_trial_num.upper()== 'QUIT':
                    print()
                    print('End of game')
                    raise SystemExit()
                else:
                    int_trial_num=int(input_trial_num)
                    break
            except ValueError:  #for input is not int
                print('This is not an int,Please enter again')
            except KeyboardInterrupt:
                print('End of game')
                raise SystemExit()
           
        #The loop of keeping getting new interval until it is right format
        while True:
            try: 
                input_pos_list=input('Please enter a list of numbers which is the factor of 1000. The list should start&end with [] and comma should be used to separate each elements. For example, [1,4,5]\n')
                if input_pos_list.upper()== 'QUIT':
                    print()
                    print('End of game')
                    raise SystemExit()
                else:
                    int_pos_list=ListPos(input_pos_list)
                    revenue_pos_list=allSimulation(int_pos_list.int_list,int_pos_list.pos_value,int_trial_num)
                    plot(revenue_pos_list,int_pos_list.int_list)
                    break
            except KeyboardInterrupt:
                print('End of game')
                raise SystemExit()
            except listException:
                print('Invalid positions, please check the format')
            except divisionException:
                print('The position is not factor of 1000')
        
    
    

if __name__ == "__main__":
    try:
        print('')
        print('Hint: Exit by QUIT')
        main()
    except EOFError:
        print()
        print('End of Game') # 
        raise SystemExit()
