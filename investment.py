#author: Julie Cachia

class investment: 
    """
    Create class for simulating a series of investements
    """
    def __init__(self, positions, num_trials):
        self.positions = positions
        self.num_trials = num_trials
        self.position_value = 1000 / positions
        
    def invest(self):
        """
        This function simulates an investment
        """
        for inv in range(num_trials):
            result = rand.choice([position_value*2, 0],size=[int(position)],p=[0.51, 0.49])
            cumu_ret[inv] = result.sum()
        daily_ret = (cumu_ret/1000)-1
        return daily_ret

    def results(self, positions, num_trials):
        file = open('results.txt','w')
        for i in positions:

            daily_ret = investment.invest(investment(i, num_trials))
            hist = plt.figure()
            plt.hist(daily_ret, 100, range=[-1, 1])
            
            plt.title('Histogram of position ' + str(i))
            plt.xlabel('Trials')
            plt.ylabel("daily_ret")
    
            hist.savefig('histogram_%04d_pos.pdf' % i)

            file.write("For position " + str(i) + ", the mean or expected value of the daily return is " + str(np.mean(daily_ret)) + "\n")
            file.write("For position  " + str(i) + ", the standard deviation of the daily return is " + str(np.std(daily_ret)) + "\n")
        plt.close('all')
        file.close()

    


            
