'''Return "Invalid Input" when the input is invalid'''
class InvalidInput(Exception):
    def __repr__(self):
        return "Invalid Input!\n"

'''Check validity of position input'''
class PositionInput:
    def __init__(self,positions):
        positions = positions.strip()[1:-1]
        positions = positions.split(',')
        if int(positions[0]) != 1 or int(positions[1]) != 10 or int(positions[2]) != 100 or int(positions[3]) != 1000:
            raise InvalidInput
        else:
            self.positions = [int(positions[0]),int(positions[1]),int(positions[2]),int(positions[3])]

'''Check validity of num_trials input'''        
class TrialInput:
    def __init__(self,num_trials):
        if int(num_trials) <= 0:
            raise InvalidInput
        else:
            self.num_trials = int(num_trials)