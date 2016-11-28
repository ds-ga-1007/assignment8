
import unittest
from Classes_and_Methods import *

class Test(unittest.TestCase):

    def setUp(self):
        pass

    def test_investment_1(self):
        investment1 = Investment(1000, 10)
        self.assertEqual(investment1.position_value, 100)

    def test_investment_2(self):
        with self.assertRaises(InvalidInvestmentValue) as cm:
            Investment(1000, 20)
        self.assertTrue('Investments must be made in $1, $10, $100, or $1000 denominations' in str(cm.exception))

        '''20 cannot be a position when we have $1000 to invest, because $1000/20 = $50. The assignment stipulates that investments can only be made in increments of $1, $10, $100, and $1000.'''
        
    def test_num_trials_1(self):
        num_trials1 = Number_Trials(10000)
        self.assertEqual(num_trials1.number, 10000)

    def test_num_trials_2(self):
        with self.assertRaises(NonPositiveInteger) as cm:
            Number_Trials(0)
        self.assertTrue('The "number of trials" must be a positive integer' in str(cm.exception))
   
    def convert_input_to_integerlist_test1(self):
        string = '[3,4,5]'
        self.assertEqual(convert_input_to_integer_list(string), [3,4,5])

    
    
    def convert_input_to_integerlist_test1(self): #NOT COUNTED
        string = '[3, 4, 5]'
        self.assertEqual(convert_input_to_integer_list(string), [3, 4, 5])

    def convert_input_to_integerlist_test2(self): #NOT COUNTED
        string2 = '3, 4, 5]'
        self.assertRaises(NoSquareBrackets, convert_input_to_integer_list, string2)

    def remove_duplicates_test(self): #NOT COUNTED
        position_list = [1, 10, 100, 10]
        self.assertEqual(remove_duplicates(position_list), [1, 10, 100])

    def convert_results_to_string_test(self): #Not
        position = 10
        position_value = 100
        daily_ret_array = np.array([0, 1])
        self.assertEqual(convert_results_to_string(position, position_value, daily_ret_array), 'Position of 10, each bet is $100\nMean = 0.5\nStandard Deviation = 0.5') 

    def simulate_bet_test(self): #Not
        position_value0 = 1000
        position_value1 = 100
        position_value2 = 10
        position_value3 = 1
        self.assertIn(simulate_bet(position_value0), [0, 2000])
        self.assertIn(simulate_bet(position_value1), [0, 200])
        self.assertIn(simulate_bet(position_value2), [0, 20])
        self.assertIn(simulate_bet(position_value3), [0, 2])

    def test_reasonableness_of_returns(self):
        '''
        The expected return is 0.02. To illustrate, if I bet $100, then my expected wealth
        after the bet is 0.51(200) + 0.49(0) = $102.
        If the observed mean for daily returns lands too far from 0.02, we've likely done something wrong.
        
        '''
        cum_array = np.zeros(10000)
        position_value = 1000
        #Let's set the bounds to 0.02 +/- 0.20.
        #This is a healthy margin, especially if we conduct 10,000 simulations.  
        upper_bound = 0.22
        lower_bound = -0.18
        for x in range(10000):
            cum_array[x] = simulate_bet(1000)
        daily_ret_mean = cum_array.mean()/1000 - 1
        self.assertTrue(daily_ret_mean < upper_bound and daily_ret_mean > lower_bound)
        

if __name__ == '__main__':
    unittest.main()
