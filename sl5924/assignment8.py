
'''
This is the main module of the program
Created on 2016/11/22
Version: 1.0
@author: liusheng
ShengLiu Copyright 2016-2017
'''
from investiment_simulation import *
import sys
if __name__ == '__main__':
	while True:
		try:
			input_positions = input('Please input a list of the number shares buy in parallel, such as [1, 10, 100, 1000] \n')
			if input_positions == 'quit':
				print ('You have quitted the simulation')
				sys.exit(1)

			if not ([element.isdigit() for element in input_positions.replace(" ", "")[1:-1].split(',')] ) or '.' in input_positions or input_positions[0] != '[' or input_positions[-1] != ']':
				raise ValueError('Invalid input! \n')
			num_trials = input('Please input how many times to randomly repeat the test: \n')
			if num_trials == 'quit':
				print ('You have quitted the simulation')
				sys.exit(1)
			if not (num_trials.isdigit) or int(num_trials) < 1:
				raise ValueError('Invalid input! \n')

			positions = map(int, input_positions[1:-1].split(','))
			print(positions)
			num_trials = int(num_trials)
			invest_simulation(positions, num_trials).invest_simu()
			break
		except KeyboardInterrupt:
			sys.exit(1)
		except Exception:
			raise
