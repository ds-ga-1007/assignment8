"""
Author: Luyu Jin
This program simulates an investment instrument in the case that we have 1000 dollars to invest on the first day.
It contains an instrument module, a myexception module, and a test module.
"""
from investment import instrument, myexception
import sys

# The main function collects user inputs, handle exceptions, and generates required outputs (txt and pdf).
def main():
    num_trials = 0
    positions = []
    while True:
        try:
            positions_input = input('Please enter a list of the number of shares to buy in parallel: e.g. [1, 10, 100, 1000]\n')
            if positions_input == 'quit':
                sys.exit(1)
            positions = instrument.positions_to_list(positions_input)
            break
        except myexception.FormattingError as e:
            print(e)
        except myexception.NotIntegerError as e:
            print(e)
        except myexception.NotPositiveIntegerError as e:
            print(e)
        except myexception.NotNumericError as e:
            print(e)
    while True:
        try:
            num_trials_string = input('Please enter the number of times to randomly repeat the test.\n')
            if num_trials_string == 'quit':
                sys.exit(1)
            num_trials = instrument.num_trials_to_int(num_trials_string)
            break
        except myexception.NotIntegerError as e:
            print(e)
        except myexception.NotPositiveIntegerError as e:
            print(e)
        except myexception.NotNumericError as e:
            print(e)

    file = open('results.txt', 'w')
    for pos in positions:
        invest = instrument.Instrument(pos, num_trials)
        invest.visualize_invest()
        mean = invest.get_mean()
        std = invest.get_std()
        file.write('For position = ' + str(pos) + ':\n')
        file.write('The mean of the daily return is: ' + str(mean) + '\n')
        file.write('The standard deviation of the daily return is: ' + str(std) + '\n')
    file.close()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)
    except EOFError:
        sys.exit(1)
