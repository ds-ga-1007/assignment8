import sys
from investment import total_gain
import matplotlib.pyplot as plt
import numpy as np

if __name__=="__main__":
    while True:
        try:
            inputstring = raw_input("Enter a list of the number of shares to buy in parallel:")
            positions_cleaned = []
            for thisnum in inputstring.split(','):
                thisnum = thisnum.strip("'[]{}()")
                positions_cleaned.append(int(thisnum)) 
            break
        except KeyboardInterrupt:
            sys.exit()
        except Exception:
            print ('Invalid input')
            pass
   
    while True:
        try:
            num_trials = raw_input('How many times to randomly repeat the test? ')
            
            if num_trials.isdigit():
                if int(num_trials) == 0:
                    print('Invalid number')
                else:
                    num_trials = int(num_trials)
                break
            else: 
                print('Invalid number')
                
        except KeyboardInterrupt:
            sys.exit()
results = open("results.txt", "w")
for position in positions_cleaned:
    this_total_gain = total_gain(position, num_trials) #find the total gain for any position in the input list
    mean_position = np.mean(this_total_gain) 
    std_postion = np.std(this_total_gain)
    
    with open('results.txt', 'a') as myfile:
        myfile.write('Mean for position ' + str(position) + 
                    ' is: ' + str(mean_position) + '. Standard deviation is ' + str(std_postion) + "\n")
        plt.clf()
        plt.hist(this_total_gain, 100, range=[-1,1])
        plt.xlim([-1,1])
        plt.xlabel('Daily gain')
        plt.title('Daily gain frequencies over ' + str(num_trials)+ ' days, for position ' + str(position))
        filename = 'histogram_' + str(position) + '_pos.pdf'
        plt.savefig(filename)