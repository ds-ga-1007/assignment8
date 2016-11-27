# -*- coding: utf-8 -*-

import Utils as ut
import matplotlib.pyplot as plt
import numpy as np
import sys

def InitialQuestion():
    
    ''' Functionn to ask the initial question, parse the results, and define each one to their respective classes'''
    
    positions = str(input("Please give a list of positions: "))
    num_trials = str(input("Please give number of times to simulate: ")) 
    
    positions = positions.replace("[", "")
    positions = positions.replace("]", "")
    
    positions = positions.split(",")
    toFillPositions = []
    
    for pos in range(0, len(positions)):
        toFillPositions.append(ut.singlePosition(positions[pos]))
        
    num_trials = ut.number_trials(num_trials)
   
    return toFillPositions, num_trials

''' Peace of code to repeat the above function when an exception is rissen'''
inputIsOk = False
while inputIsOk is False:
    try:   
        positions, num_trials = InitialQuestion()
        inputIsOk = True
    except ut.textInputedException:
        print("Text inputed in one of your positions. Please try again")
        pass
    except ut.negativeNumber:
        print("A negative number was inputed. Please try again")
        pass
    except ut.positionOver1000:
        print("You have at least one position over 1000. Please try again")
        pass
    except ut.textTrialInputedException:
        print("Text inputed in your interval. Please try again")
        pass
 
''' Plot an histogram for all possible positions passed as a list simulated n times'''
for x in range(0, len(positions)):
    plt.close("all")
    myPosition = positions[x]
    daily_ret = (ut.positionGainMultipleSimulation(myPosition, num_trials.number)/1000) - 1
    plt.hist(daily_ret, 100, range=[-1,1], color="#225ea8")
    plt.xlabel('Daily return', size=10)
    plt.ylabel('Occurrences', size=10)
    plt.yticks(size=8)
    plt.xticks(size=8)
    # Peace of code to set the position of the desired text: 
    # Soruce: http://stackoverflow.com/questions/7045729/automatically-position-text-box-in-matplotlib - Joe Kington in stackoverflow.
    plt.annotate(r"$\mu={},\ \sigma={}$".format('{:05.4f}'.format(np.mean(daily_ret)), '{:05.4f}'.format(np.std(daily_ret))), xy=(0.01, 0.95), xycoords='axes fraction', size=8)
    plt.title("Histogram daily return out of {} simulations for position {}".format(num_trials.number, myPosition.numShares), size=10)
    plt.savefig("histogram_{}_pos.pdf".format('{:04.0f}'.format(myPosition.numShares)))
    plt.close("all")    

''' Write a .txt file with the results for each array with the simulations'''
myFile = open("results.txt", "w")
np.set_printoptions(threshold=np.nan)
for x in range(0, len(positions)):
    myPosition = positions[x]
    myFile.write("\n")
    myFile.write("Data on returns from {} simulations for position {}: ".format(num_trials.number, myPosition.numShares))
    myFile.write("\n")
    daily_ret = (ut.positionGainMultipleSimulation(myPosition, num_trials.number)/1000) - 1
    myFile.write(np.array_str(daily_ret))
    myFile.write("\n")   
    
print("Please find the output plots and data in your local computer. Goodbye.")
        
sys.exit()        
