'''
Created on Nov 29, 2016

@author: felix
'''
import matplotlib.pyplot as plt

def plot_simulation(plot_data, position_int):
    fig = plt.figure()
    plt.hist(plot_data, 100, range = [-1,1])
    plt.title("Position = " + str(position_int))
    plt.xlabel('Daily Returns')
    plt.ylabel('Frequency')
    this_filename = ('histogram_' + '{:04d}'.format(position_int) + '_pos.pdf')
    plt.savefig(this_filename)
    print(this_filename + ' saved.')
    
def write_simulation(a_file, position_int, a_mean, a_std):
    first_line = 'Position: ' + '{:04d}'.format(position_int) +'\n'
    second_line = 'Mean: ' + str(a_mean) + ', ' + 'SD: ' + str(a_std) + '\n\n' 
    a_file.write(first_line)
    a_file.write(second_line)