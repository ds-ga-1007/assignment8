from investiment import Investiment
from exceptions import InvalidInputException
import sys

#check wether the input positions is valid
def validPosition(inp):
    if inp[0] != '[' or inp[-1] != ']':
        raise InvalidInputException
    if any(num not in [1, 10, 100, 1000] for num in [int(e) for e in inp[1:-1].split(",")]):
        raise InvalidInputException
    return [int(e) for e in inp[1:-1].split(",")]

#check wether the input trials is valid
def validTrials(inp):
    if not inp.isdigit():
        raise InvalidInputException
    return int(inp)


def main():
    while True:
        try:
            #Accept the following inputs from the user, empty line for break:
            inp1 = input("Input a list of a list of the number of shares to buy in parallel, empty line for break: e.g. [1, 10, 100, 1000]\n")
            if len(inp1) == 0:
                break
            #Repeat num_trials times
            inp2 = input("how many times to randomly repeat the test\n")
            positions = validPosition(inp1)
            num_trials = validTrials(inp2)
            Investiment.invest(positions, num_trials)
            break
    
    
        #Invalid user input is handled correctly (when input is required by the assignment)
        #User defined exception(s) are employed for indicating error conditions rather than raising generic exceptions

        except InvalidInputException:
            print("Invalid input")
        except KeyboardInterrupt:
            print("Quited  by user")
        except:
            print('something bad happens')



if __name__ == "__main__":
    main()
