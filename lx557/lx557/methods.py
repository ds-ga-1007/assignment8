'''
Created on 2016.11.23

@author: xulei
'''

from input_object import ListPos
import numpy as np
import matplotlib.pyplot as plt

def singlePosSimulation(pos,pos_value,trial_num):
    revenue_day=[]
    for i in range(trial_num):
        bernoulli_sample = (np.random.rand(pos) >= 0.49).astype('int64')   #because 0.51 to be 1  
        cumu_ret=(bernoulli_sample*2)*(np.ones(pos)*pos_value)
        revenue_day.append(np.sum(cumu_ret)*0.001-1)
    return revenue_day

def allSimulation(pos_list,pos_value_list,trial_num):
    revenue_poslist=[] #so it will be list of lists later
    for i in range(len(pos_list)):
        revenue_i_pos=singlePosSimulation(pos_list[i], pos_value_list[i], trial_num)
        revenue_poslist.append(revenue_i_pos)
    return revenue_poslist

def plot(list_of_lists,pos_list):
    f = open('results.txt', 'w')
    for i in range(len(list_of_lists)):
        fig=plt.figure()
        plt.hist(list_of_lists[i],100,range=[-1,1])
        plt.savefig('histogram_{}_pos.pdf'.format(pos_list[i])) 
        f.write(' The mean of buying {} shares is {} with standard deviation as {}\n'.format(pos_list[i],np.mean(list_of_lists[i]),np.std(list_of_lists[i])))
    f.flush()
    


            
        
    

