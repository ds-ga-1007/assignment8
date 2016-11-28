'''
Author: Weiwei Xu
Net ID: wx433

This program is a simulation of different investments.
The total investment stays unchanged. 
But an investor can dicide if he or she want to all in or break the risk down.
The program also engages test repitition to reduce the error.

'''



from Investment import InvSimulation
import sys

while True:

	
'''
Investors want to test on different investment plans, e.g. 1 share of $1000, or 10 shares of $100,
or 100 shares of $10, etc.
So the input here is a list of positions that investors want to test out.
The out put will be statistical summary and charts to see the distribution.
'''
	try:
		posIn = input("Please give a list of positions.\n")
		if posIn[0] == "[" and posIn[-1] == "]":
			posIn = posIn[1:-1]
			myList = posIn.split(',')
			positions = []
			for each_num in myList:
				positions.append(int(each_num))

			break
		else:
			print("Not a List")

	except ValueError:
		print ("Invalid Input")

	except (KeyboardInterrupt, SystemExit):
		sys.exit()

	# except IOError:
	# 	sys.exit()

	else:
		print("Invalid Input")

while True:
	
	try:
		trials = int(input('Please input how many trials you want to simulate.\n'))
		
		break

	except ValueError:
		print ("Please enter an integer.")

	except (KeyboardInterrupt, SystemExit):
		sys.exit()

	# except IOError:
	# 	sys.exit()

	else:
		print("Invalid Input")

for each_position in positions:
	instance = InvSimulation(each_position, trials)
	instance.result()




if __name__ == '__main__':
    pass

