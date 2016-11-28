'''
Created on 2016.11.23

@author: xulei
'''

from Exception_class import listException, divisionException
import numpy as np

class ListPos:       
    def __repr__(self):
        return self.content

    def __init__(self, input_content):
        self.content=input_content
        
        if (self.content[0] !='[' or self.content[-1]!=']'):
            raise listException()
        
        #convert the list of string into int
        self.list_str=input_content.split(',')
        self.list_str[0]= self.list_str[0][1:]  #remove the left square bracket in the first element
        self.list_str[-1]=self.list_str[-1][:-1]  #remove the right square bracket in the first element
        
        self.float_list=[float(i) for i in self.list_str] #for calculate the reciprocal so instead of int, do it as float
        
        #check if they are factors of 1000 
        for i in self.float_list:
            if 1000 %i !=0:
                raise divisionException()
            
        self.int_list=[int(i) for i in self.float_list] 
           
        self.pos_value=1000*np.reciprocal(self.float_list)
            
        
        

