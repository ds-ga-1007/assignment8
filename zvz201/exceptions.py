""" This module contains user-defined exceptions"""
#all exceptions have to do with the user input (+KeyboardInterrupt or SystemExit)

class Error(Exception):
    """Base class for other exceptions"""
    pass

class TWoconsecutiveCommas(Error):
    """Raised when the input contains at least 2 consecutive commas"""
    pass

class ContainsPeriod(Error):
    """Raised when the input contains dots/periods (e.g., a decimal number is entered)"""
    pass

class ElementsOtherThanDigits(Error):
    """Raised when the input contains elements other than digits (letters, #,},-, etc.)"""
    pass

class LastElementIsComma(Error):
    """Raised when the last element in the input is a comma"""
    pass

class NotCorrectInput(Error):
    """Raised when the element of the input is neither 1, nor 10, nor 100, nor 1000"""
    pass

class NoInput(Error):
    """Raised when the input is empty"""
    pass

class Quit(Error):
    """Quit the program"""
    pass

class NotNumber(Error):
    """Raised when the input for the number of simulations is not a number"""
    pass

