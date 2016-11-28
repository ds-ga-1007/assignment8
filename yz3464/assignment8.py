'''
Created on Nov 28, 2016

@author: twff
'''
from assignment8.investment import *
import sys

if __name__ == "__main__":
    while True:
        try:
            num_trials = int(input('Please enter how many times to randomly repeat the test '))
            break
        except ValueError as e:
            print(str(e))
        except (EOFError, KeyboardInterrupt):
            print()
            sys.exit(1)
            
    positions = []
    try:
        while True:
            p = input('Please enter the number of shares ')
            p = int(p)
            print(p)
            try:
                positions.append(p)
                print(positions)
            except ValueError as e:
                print(str(e))
    except KeyboardInterrupt:
        print()
        sys.exit(1)
    except EOFError:
        print()
    
    if len(positions) < 1:
        raise ValueError
    
    investment.showResult(positions, num_trials)
    for p in positions:
        filename = 'histogram_%04d_pos.pdf' % p
        investment.plotFigures(p, num_trials, filename)
        
    print('finished')