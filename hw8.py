# Author: Yang Sun
import sys
from simulation import *

'''Users should input a list of numbers of shares to buy, and a number of times to repeat to do the
simulation of the investment. The program will yield mean and standard deviation of each position,
and histogram of daily return.'''

while True:
    try:
        pos_num = raw_input('A list of number of shares to buy in parallel? '
                            'Valid numbers to input are 1,10,100 and 1000\n')
        positions = pos_num.split()
        for i, position in enumerate(positions):
            positions[i] = int(position)
        break
    except EOFError:
        sys.exit(1)
    except KeyboardInterrupt:
        sys.exit(2)

while True:
    try:
        num_trials = int(raw_input('How many times to randomly repeat the test?\n'))
        break
    except ValueError:
        print('Invalid number!')
    except EOFError:
        sys.exit(3)
    except KeyboardInterrupt:
        sys.exit(4)

f = open ('results.txt','w')
for i in positions:
    s = simulation(i, num_trials)
    f.write('Position: ' + str(i) + ', Mean: ' + str(s.mean)+ ', Std:  ' + str(s.std) + "\r\n")
    s.histogram('Histogram_' + str(i) + '_pos.pdf')

f.close()
