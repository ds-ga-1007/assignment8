class MyException(Exception):
    def __str__(self):
        return 'Invalid position in the input list, choose from 1, 10, 100, 1000'