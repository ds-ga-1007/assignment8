from investment.investment import *
import sys

def main():
    
    """
    Function main takes a list of the number of shares to buy in parallel
    as positions and how many times to randomly repeat the test as num_trials
    """
    
    while True:
        try:
            position = input('Please input a list of shares to buy:\n')
            if (position == 'quit'):
                sys.exit()
            
            position = position.replace(' ', '')
            positions = position[1:-1].split(',')
            for i, item in enumerate(positions):
                positions[i] = int(item)
            
            break
        
        except ValueError:
            print('Invalid input')
        except KeyboardInterrupt:
            sys.exit()
        except EOFError:
            sys.exit()
            
    while True:
        try:
            num_trials = int(input('Please input how many times you want to repeat the test'))
            break
        
        except ValueError:
            print('Invalid input')
        except KeyboardInterrupt:
            sys.exit()
        except EOFError:
            sys.exit()  
            
    # call the class investment constructor to create an object t
    t = investment(positions, num_trials)
    
    # call the function 'present_results' in class investment to do the simulation and 
    # produce the result
    t.present_results(positions, num_trials)      
                
if __name__ == "__main__":
    main()