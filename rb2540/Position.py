import numpy as np

class PositionError(Exception) :
    """Raised when errors occur in the Position class"""
    pass

class Position(object): 
    """Used to track returns for a given position over a number of trials
    Must call computeAllTrials before accessing statistics"""
    def __init__(self,position,numTrials,bias) :
        """Initializes class and checks for valid inputs"""
        if position <= 0 or position > 1000 or not isinstance(position,int) :
            raise PositionError('position is invalid: '+str(position))
        if bias < 0 or bias > 1 :
            raise PositionError('bias is invalid')
        if numTrials <= 0 :
            raise PositionError('numTrials is invalid')
        self.position = position
        self.value = 1000/position
        self.bias = bias
        self.numTrials = numTrials
        self.cumu_ret = np.zeros(self.numTrials)
        self.daily_ret = np.zeros(self.numTrials)
    
    def computeAllTrials(self) :
        """Computes all of the trials and populates the _ret arrays"""
        for i in range(self.numTrials) :
            self.computeTrial(i)

    def computeTrial(self,index) :
        """Computes the returns for a single trial and populates the 
        corresponding array location"""
        flips = np.random.rand(self.position)
        self.cumu_ret[index] = np.sum(flips <= self.bias)*2*self.value
        self.daily_ret[index] = (self.cumu_ret[index]/1000.0)-1

    #Must call computeAllTrials before this
    def getMean(self) :
        """Returns the mean daily return"""
        return np.mean(self.daily_ret)

    #Must call computeAllTrials before this
    def getStd(self) :
        """Returns the standard deviation of the daily returns"""
        return np.std(self.daily_ret)
