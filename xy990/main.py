from investment import *

#This is the main function which the user can interact with the program.
def main():
    #Users can input a list of positions until the input is valid, otherwise raise some specific errors.
    while True:
        try:
            user_input = str(input("Please input a list of positions:"))
            if user_input.lower() =="quit":
                return
            if user_input[0] != "[" or user_input[-1] != "]":
                raise InputError("The input is not a list!")
            
            user_input = user_input.strip()[1:-1].split(",")
            positions =[]
            for i in user_input:
                positions.append(int(i))
            break
        except InputError:
            print("Invalid positions input!")
        except KeyboardInterrupt:
            print("keyboard interrupt error")
        except EOFError:
            print("Value error")
    
        #Users can input number of trials until the input is valid, otherwise raise some specific errors.        
    while True:
        try:
            num_trials = int(input("Please input number of trials:"))
            
            if num_trials <1:
                raise InputError("The number of trials is invalid!")
            investment.results(positions, num_trials)
            break
        except InputError:
            print("Invalid number of trials input!")
        except KeyboardInterrupt:
            print("keyboard interrupt error")
        except EOFError:
            print("Value error")
        
        
        
if __name__ =="__main__":
    main()
        
                
class InputError(Exception):
    pass          
