'''
Created on Nov 24, 2016

@author: danielamaranto
'''
from investment import investment_position
import matplotlib.pyplot as plt

def generate_statistics(investment):
    '''I referred to python documentation to write to the text file.
    https://docs.python.org/3/tutorial/inputoutput.html''' 
    with open('Portfolio Statistics.txt', 'a') as file:
        data =  'Number of shares: ' + str(investment.position) + \
                '\nValue of each share: $' + str(investment.position_value) + \
                '\nMean: ' + str(investment.mean()) + \
                '\nStandard Deviation: ' + str(investment.stdev()) + '\n\n'
        file.write(data)
        
def generate_histogram(investment):
    '''I referred to python documentation to properly format the histogram filenames (zfill)
    and to generate individual plots (savefig). 
    https://docs.python.org/2/library/string.html
    http://matplotlib.org/api/pyplot_api.html'''
    plt.hist(investment.daily_ret(),100, range=[-1,1])
    plt.xlabel('Daily Return')
    plt.ylabel('Number of Trials')
    plt.title('Histogram of investment trials')
    plt.grid(True)
    name = str(investment.position).zfill(4)
    plt.savefig('histogram_'+ name +'_pos.pdf', format='pdf')
    plt.close('all')
