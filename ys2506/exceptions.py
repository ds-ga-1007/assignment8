#User defined exception(s) are employed for indicating error conditions
class InvalidInputException(Exception):
    def __str__(self):
        #the innput is not valid
        return 'Invalid input'