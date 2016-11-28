import sys
from investment import *
from input_error import *

def main():
    while True:

        
        try:
            inpt1=input("Please enter a list of the number of shares to buy in parallel, e.g. [1, 10, 100, 1000]")
            inpt1=inpt1.replace(' ','')
            if inpt1=='quit':
                break
            else:
                positions=input_positions(inpt1)
                
        except KeyboardInterrupt:
            sys.exit(0)
        except EOFError:
            sys.exit(0)
            
  #  while True:

        try:
            inpt2=input("Please input number of trials (a positive integer).")
            inpt2=int(inpt2)
            if inpt1=='quit':
                sys.exit()
            else:
                num_trials=input_trials(inpt2)
            
        except KeyboardInterrupt:
            sys.exit(0)
        except EOFError:
            sys.exit(0)
            
        inv=user_input(positions,num_trials)
        result(inv)
    
if __name__ == "__main__":
    main()
