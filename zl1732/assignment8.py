import sys
from investment import investment
from check_error import *
'''
main function of the program, call functions in investment class
'''
def main():
    while 1:
        '''
        input the positions from users
        '''
        try:
            positions = input("input the position: ")
            if (positions == 'quit' or positions == 'Quit'):
                print("Quit the Game")
                sys.exit()
            check_positions(positions)
            break
        except ValueError as error:
            print(error)
        except EOFError:
            sys.exit()
            
    while 1:
        '''
        input the num_trails from users
        '''
        try:    
            num_trails = input("input the trails: ")
            if (positions == 'quit' or positions == 'Quit'):
                print("Quit the Game")
                sys.exit()
            check_trails(num_trails)
            break
        except ValueError as error:
            print(error)
        except EOFError:
            sys.exit()
            
    i = investment(positions,num_trails)
    position_num, trails = i.str2num(positions, num_trails) #convert positions and trails from string format to list of integer and integer
    daily_ret = i.simulation(position_num, trails)          #calculation
    i.plot_result(daily_ret)                                #write to result.txt and pdf
    return
    
if __name__ == "__main__":
    main()