'''
This module handles user defined exceptions/errors. 
Two classes are defined to read input from user and check if it is valid.
They can be easily modified to indicate more specific error conditions.
'''

class InvalidInput(Exception):
	'''User defined exceptions'''
	def __repr__(self):
		return "Invalid Input!\n"

class Positions:
	'''This class reads positions string from user input, and check if it is valid'''
	def __init__(self,positions):
		if positions[0]!='[' and positions[-1]!=']':
			raise InvalidInput
		try:
			positions = [int(i.strip()) for i in positions[1:-1].split(',')]
			if set(positions) != set([1,10,100,1000]):
				raise InvalidInput
			else:
				self.positions = positions
		except:
			raise InvalidInput

class Num_trials:
	'''This class reads num_trials string from user input, and check if it is valid'''
	def __init__(self, num_trials):
		try:
			num_trials = int(num_trials)
			if num_trials < 1:
				raise InvalidInput
			else:
				self.num_trials = num_trials
		except:
			raise InvalidInput

