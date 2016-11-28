'''This is the module for the simulation class, user defined error  
   and correct input check function
   Author:Liwei Song
   NetID:ls4408
   Creation date: 11/28/2016
 '''
import numpy 
import matplotlib.pyplot as plt

'''define a new class for simulation'''

class simulation(object): 
    #initial function for simulation
    def __init__(self,position,numb):
        self.diff_posit_ret={}
        self.position=position
        self.numb=numb
    
    def get_simulation(self): 
        #generate daily return rate for different position
        for diff_position in self.position:
            cumu_ret=numpy.zeros(self.numb)
            daily_ret=numpy.zeros(self.numb)
            for trial in range(self.numb):
                    for i in range(diff_position):
                        toss_list = numpy.random.uniform()
                        if toss_list <= 0.49:
                            cumu_ret[trial]=cumu_ret[trial]
                        else:
                            position_value=1000/diff_position
                            cumu_ret[trial]=cumu_ret[trial]+position_value*2
                    daily_ret[trial]=(cumu_ret[trial]/1000)-1
            self.diff_posit_ret[diff_position]=daily_ret
    
    def get_txt_hist(self):
        #generate txt and histograms for different position
        f=open('results.txt','w')
        for diff_position in self.position:
            if diff_position==1:
                save_name='histogram_'+'0001'+'_pos.pdf'
            elif diff_position==10:
                save_name='histogram_'+'0010'+'_pos.pdf'
            elif diff_position==100:
                save_name='histogram_'+'0100'+'_pos.pdf'
            else:
                save_name='histogram_'+'1000'+'_pos.pdf'
                #generate names for different positions
            plt.figure()
            plt.hist(self.diff_posit_ret[diff_position],100,range=[-1,1])
            plt.xlabel('daily_ret')
            plt.ylabel('frequency')
            plt.savefig(save_name)
            plt.close()
            #generate plots with plt
            each_mean=numpy.mean(self.diff_posit_ret[diff_position])
            each_stdev=numpy.std(self.diff_posit_ret[diff_position])
            f.write('For position '+str(diff_position)+', the mean is '+str(each_mean)+'.\n'
                   +'The standard deviation is '+ str(each_stdev)+'.\n'+'\n')
            #write statistical summaries for all positions
            f.flush()
        f.close()
            
            
'''define an exception for input error'''
class inputError(Exception):
    def __str__(self):
        return("input error")
    
'''define a function for a correct input of a list of positions'''
def correct_input_position(position):
    if len(position)==0:
        raise inputError
    if position[0] !='[':
        raise inputError
    if position[-1] !=']':
        raise inputError
        #raise error for invalid input symbol
    position_string=position[1:-1]
    position_list_str=position_string.split(",")
    position_list=[]
    for number in position_list_str:
        if number.isdigit()==False:
            raise inputError
        if int(number) not in [1,10,100,1000]:
            raise inputError
            #raise error for invalid input numbers
        else:
            position_list.append(int(number))
    if len(position_list)==0:
        raise inputError
        #raise error for empty list
    return position_list
    #return a list


'''define a function for a correct input of a valid number for simulation'''
def correct_input_numb(numb):
    if numb.isdigit()==False:
        raise inputError
    if int(numb) <= 0:
        raise inputError
        # raise errot if the input is not an integer
    else:
        return int(numb)