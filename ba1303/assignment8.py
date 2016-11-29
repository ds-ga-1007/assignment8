from Classes_and_Functions import *

print('\nThis program simulates the one-day performance of an investment, assuming\nthat we invest $1000. Specifically, the program will simulate\ninvestment returns for a range of position sizes.')


'''First step: user must input a list of positions'''
print('\nSince we start with $1000, and the only possible denominations are $1000,\n$100, $10, and $1, you must enter a subset of [1, 10, 100, 1000].')
print('Input for the list of positions must be bracketed by [].\n')
while True:
    try: 
        position_string = input('Please enter list of positions: ')
        positions = convert_input_to_integer_list(position_string)
        positions = remove_duplicates(positions)
        position_values = np.zeros(len(positions))
        for i in range(len(positions)):
            positions[i] = Investment(1000, positions[i]).position
            position_values[i] = Investment(1000, positions[i]).position_value
        break
        
    except NoSquareBrackets:
        print('Input must be surrounded by square brackets')      
    except InvalidInvestmentValue:
        print('Investments must be made in $1, $10, $100, or $1000 denominations - pick subset of [1, 10, 100, 1000]')
    except ValueError:
        print('Please enter only integers, with each integer separated by a comma.')


'''Second step: user must input the number of trials'''
while True:
    try:
        num_trials = Number_Trials(int(input('Please enter the number of trials to randomly repeat the test: '))).number
        break
    except (NonPositiveInteger, ValueError):
        print('The "number of trials" must be a positive integer.')


'''Final steps: histograms and text file produced'''
with open('results.txt', mode = 'w') as f:  #create new file "results.txt"
    #For each position (1, 10, 100, 1000)
    for i in range(len(positions)):
        daily_ret = np.zeros(num_trials)
        cumu_ret = np.zeros(num_trials)
        for trial in range(num_trials): # For each day of investing:
            for simulation in range(positions[i]): #For each bet simulated that day: 
                single_bet_payout = simulate_bet(position_values[i])
                cumu_ret[trial] = cumu_ret[trial] + single_bet_payout
            daily_ret[trial] = (cumu_ret[trial]/1000) - 1    
        
        add_string_to_file(positions[i], position_values[i], daily_ret, f) 
        generate_histogram(positions[i], daily_ret)
        plt.savefig('histogram_{:04.0f}_pos.pdf'.format(positions[i]))
