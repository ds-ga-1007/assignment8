from Position import *
import matplotlib.pyplot as plt

def main() :
    """Reads a list of positions and the number of trials from the user
    and outputs statistics to results.txt and histogram_####_pos.pdf"""
    try :
        resFile = open('results.txt','w')
        #Fixed bias at .51 as specified in the assigment
        bias = .51
        #Expects a comma-delimited list of numbers
        inp = input("Give a list of positions (comma-separated, e.g., 1, 5, 10): ")
        positions = [int(x) for x in inp.split(",")]
        numTrials =  int(input("Give the number of trials (integer at least 1): "))
        for p in positions :
            position = Position(p,numTrials,bias)
            position.computeAllTrials()
            resFile.write("Position = %d, Mean = %f, Std = %f\n"%(p,position.getMean(),position.getStd()))
            plt.figure()
            plt.hist(position.daily_ret,100,range=[-1,1])
            plt.xlabel('Daily Returns')
            plt.ylabel('Trials')
            plt.title('Histogram of Daily Returns')
            plt.savefig("histogram_%04d_pos.pdf" % p)
        resFile.close()
    except IOError as ioerr :
        print("Error with file: %s" % ioerr)
    except PositionError as perr:
        print("PositionError: %s" % perr)
        return
    except ValueError :
        print('Error in input!')
        return



if __name__ == "__main__" :
    main()
