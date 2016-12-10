'''
This is the main program for investment.
'''

from investment import Investment
from exception import InputTypeException, InputValueException, checkInput

# Takes user input as a list of shares to buy
def main():
    inputPositions = input('Please give a list of shares that you would like to buy. The input can be something like [1, 10, 100, 1000]. Type in \'quit\' to quit the program.\n')
    if inputPositions == 'quit':
        return
    # check 1st input string
    checkInput(inputPositions)
    # convert 1st input string to a list
    inputStrSplit = inputPositions[1:-1].strip().split(',')
    shares_list = []
    for share in inputStrSplit:
        shares_list.append(int(share))

    # check 2nd input string
    num_trails = input('Please give a number of trails that you would like to simulate. For example, 10000.Type in \'quit\' to quit the program.\n')
    if num_trails == 'quit':
        return

    # run Investment class
    print('Calculating...')
    inv = Investment(shares_list, int(num_trails))
    inv.calcPositionValue()
    inv.calcCumulativeReturn()
    inv.calcDailyReturn()
    inv.calcDailyReturnMean()
    inv.calcDailyReturnStd()
    inv.saveResults()
    print('Done. Results are saved.')

if __name__ == '__main__':
    main()