import unittest
import validate_input as i
import investment.py as Inv


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

