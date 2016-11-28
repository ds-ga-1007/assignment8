from investiment import InvestmentInstrument
from exceptions import InvalidInputException
import matplotlib.pyplot as plt
import numpy as np
import sys

#check wether the input positions is valid
def validPosition(inp):
    #valid list with []
    if inp[0] != '[' or inp[-1] != ']':
        print("not a valid list")
        raise InvalidInputException
    #the number of list should be a factor of 1000
    if any(1000 % num != 0  for num in [int(e) for e in inp[1:-1].split(",")]):
        print("the number of list should be a factor of 1000")
        raise InvalidInputException
    return [int(e) for e in inp[1:-1].split(",")]

#check wether the input trials is valid
def validTrials(inp):
    if not inp.isdigit():
        raise InvalidInputException
    return int(inp)


def simulate(positions, num_trials):
    
    instrument = InvestmentInstrument(positions)
    daily_ret = instrument.investment_simulate(1000, num_trials)
    position_ret = daily_ret.transpose()
    
    #For each position, the mean or expected value of the daily return.
    #For each position, the standard deviation of the daily return.
    means = [np.mean(p) for p in position_ret]
    stds = [np.std(p) for p in position_ret]
    
    #results.txt includes the numerical results described above
    with open('results.txt', 'w') as f:
        f.write('{:10s} {:7s} {:7s}\n'.format('position', 'mean', 'stddev'))
        f.write(''.join('{:8d}   {:.5f} {:.5f}\n'.format(pos, mean, std)
                          for (pos, mean, std) in zip(positions, means, stds)))
    
    #For each position, plot of the result of the trials in a histogram with X axis from -1.0 to +1.0, and Y axis as the number of trials with that result. [Hint: use the matplotlib function plt.hist(daily_ret,100,range=[-1,1])]
    for idx in range(len(positions)):
        fig = plt.figure()
        plt.hist(position_ret[idx], 100, range = [-1, 1])
        plt.xlabel("result of the trials")
        plt.ylabel("number of trials with that result")
        name = 'histogram_' + str(positions[idx]).rjust(4, '0') + '_pos'
        plt.title(name)
        plt.savefig(name + '.pdf')
    plt.show()
    plt.close()

def main():
    #At first, we would Run the program with positions set to [1, 10, 100, 1000] and num_trials set to 10000.
    print("At first, we would Run the program with positions set to [1, 10, 100, 1000] and num_trials set to 10000. ")
    simulate([1, 10, 100, 1000], 10000)
    
    #Then we would Run the program with user input:
    print("Then we would Run the program with user input:")
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
            simulate(positions, num_trials)
            print(" Happily finished ;-) ")
            break
    
    
        #Invalid user input is handled correctly (when input is required by the assignment)
        #User defined exception(s) are employed for indicating error conditions rather than raising generic exceptions

        except InvalidInputException:
            # Exit if the user enter invalid input
            print("Invalid input")
            sys.exit(0)
        except KeyboardInterrupt:
            # Exit if the user enter Ctrl+C
            sys.exit(0)
            print("Quited  by user")
        except EOFError:
            # Exit if the user enter Ctrl+D
            sys.exit(0)
        except:
            print('exception happens')



if __name__ == "__main__":
    main()
