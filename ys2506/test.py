import unittest
from exceptions import InvalidInputException
from investiment import InvestmentInstrument
from assignment8 import validTrials, validPosition

#Unit tests are provided with the solution code
#The unit tests pass correctly
class Test(unittest.TestCase):
    #test function validPosition
    def test_validPosition(self):
        self.assertEqual(validPosition('[1,10,100,1000]'),[1,10,100,1000])
        with self.assertRaises(InvalidInputException):
            validPosition('abc')
            validPosition('(1,10,100,1000)')
    #test function validTrials
    def test_validTrials(self):
        self.assertEqual(validTrials('1000'),1000)
        with self.assertRaises(InvalidInputException):
            validPosition('abc')
            validPosition([1,a,d,c])
'''
    #test function outcome
    def test_outcome(self):
        self.assertEqual(len(Investiment.outcome(Investiment(1,100))),100)
        self.assertTrue(all(Investiment.outcome(Investiment(1,100)) >= -1))
        self.assertTrue(all(Investiment.outcome(Investiment(1,100)) <= 1))
'''

if __name__ == "__main__":
    unittest.main()