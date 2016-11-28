'''
Created on Nov 27, 2016

@author: Caroline
'''
import unittest
import validate_input as i
import Investment as Inv
import invest as v

#Investment class test

class Investment_test_case(unittest.TestCase):
    def setUp(self):
        print('In investment setUp')
        self.test_investment = Inv.Investment(10)
    def tearDown(self):
        print('In investment tearDown')
        del self.test_investment

class Test_investment(Investment_test_case):
    def test_investment_exception(self):
        self.assertEqual(self.test_investment.position_value, 100)

#validate_input tests

class Reject_irregular_characters_test_case(unittest.TestCase):
    def setUp(self):
        print('In reject irregular characters setUp')
        self.invalid_input = '[1, 10, 1OO, 1000]'
        
    def tearDown(self):
        print('In reject irregular characters tearDown')
        del self.invalid_input

class Test_reject_irregular_characters(Reject_irregular_characters_test_case):
        def test_exception(self):
            self.failUnlessRaises(Exception, i.reject_irregular_characters, self.invalid_input)

class Parse_input_test_case(unittest.TestCase):
    def setUp(self):
        print('In parse input setUp')
        self.valid_input = '[1, 10, 100, 1000]'
        self.valid_output = ['1', '10', '100', '1000']
        self.invalid_input = '1 10 100 1000'
    
    def tearDown(self):
        print('In parse input tearDown')
        del self.valid_input
        del self.invalid_input
        
class Test_parse_input(Parse_input_test_case):
    def test_exception(self):
        self.failUnlessRaises(Exception, i.parse_input, self.invalid_input)
        
    def test_valid(self):
        self.assertEqual(i.parse_input(self.valid_input), self.valid_output)
        
#invest tests

class invest_test_case(unittest.TestCase):
    def setUp(self):
        print('In invest setUp')
        self.test_investment = Inv.Investment(10)
    
    def tearDown(self):
        print('In invest tearDown')
        del self.test_investment

class Invest_test(invest_test_case):
    def test_invest(self):
        self.assertTrue(v.invest(self.test_investment) >= 0 and v.invest(self.test_investment) <= 2000)

class simulate_trials_test_case(unittest.TestCase):
    def setUp(self):
        print('In simulate trials setUp')
        self.num_trials = 100
        self.test_investment = Inv.Investment(10)
        
    def tearDown(self):
        print('In simulate trials tearDown')
        del self.test_investment
        del self.num_trials
        
class Simulate_trials_test(simulate_trials_test_case):
    def test_simulate_trials(self):
        self.assertTrue(len(v.simulate_trials(self.test_investment, self.num_trials))==self.num_trials)
        self.assertTrue(-1 not in v.simulate_trials(self.test_investment, self.num_trials)) #make sure that all initial -1 values were replaced