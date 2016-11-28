'''
Created on 2016.11.23

@author: xulei
'''
    
class listException(Exception):
    def __str__(self):
        return 'This is not a valid list!'
    
class divisionException(Exception):
    def __str__(self):
        return 'The int is a factor of the 1000'
    
    

