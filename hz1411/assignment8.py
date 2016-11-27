'''
author: Han Zhao 
email: hz1411@nyu.edu

This is the main program that keep prompting for user input until the input is valid, 
or the user enters "quit" to exit. Then it calls the trail class and do the investment
trail, calculate mean & std, plot histogram and write output to txt file.

'''

from trial import *
from exceptions import *

while True:
# keep reading positions from user input until the input is valid or input == 'quit'
	try:
		positions_input = input("Enter positions or 'quit' to exit:")
		if positions_input == 'quit':
			break
		else:
			try:
				positions = Positions(positions_input).positions
				break
			except InvalidInput:
				print('Invalid Input!')
				continue
	except KeyboardInterrupt:
		print('User Interrupt')
	except EOFError:
		print('Input Error')

while True:
# keep reading num_trials from user input until the input is valid or input == 'quit'
	try:
		num_trials_input = input("Enter Num of trials or 'quit' to exit:")
		if num_trials_input == 'quit':
			break
		else:
			try:
				num_trials = Num_trials(num_trials_input).num_trials
				break
			except InvalidInput:
				print('Invalid Input!')
				continue
	except KeyboardInterrupt:
		print('User Interrupt')
	except EOFError:
		print('Input Error')

f = open("results.txt","w")
for position in positions:
	t = trial(position, num_trials)
	t.plot_hist()
	mean = t.mean_std()[0]
	std = t.mean_std()[1]
	f.write("Position = {}: mean = {:.4f}, std = {:.4f} \n".format(position, mean, std))
f.close()

		




