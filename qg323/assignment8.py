# Copyright (C) Quan Gan <qg323@nyu.edu>

# Runs simulations to determine how to make investments on a day: given
# some budget, shall we put everything in one basket, or buy a lot of
# small-value shares?

# There are not very much comments because I think the code is already pretty
# self-descriptive.

# To run tests, run the following in the qg323 directory:
# $ python -m unittest discover

import sys
from trial import Trial

# Enter number of trials until user aborts or entered valid stuff
while True:
    try:
        num_trial = int(
                input('Enter how many times to repeat test for each position ')
                )
        break
    except ValueError as e:
        print(str(e))
    except (EOFError, KeyboardInterrupt):
        print()
        sys.exit(1)

# The same for positions
positions = []
try:
    while True:
        p = input('Enter number of shares to buy (Ctrl+D to end) ')
        try:
            positions.append(int(p))
        except ValueError as e:
            print(str(e))
except KeyboardInterrupt:
    print()
    sys.exit(1)
except EOFError:
    print()
    # Continue execution

if len(positions) == 0:
    print('No number of shares specified, exiting')
    sys.exit(2)

output_file = open('result.txt', 'w')

for p in positions:
    trial = Trial(p, num_trial)
    trial.plot('histogram_%04d_pos.pdf' % p)
    output_file.write(
            'Position %d: Mean %f, STD %f\n' % (p, trial.mean, trial.std)
            )

output_file.close()
