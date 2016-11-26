class InvalidListError(Exception):
    
    def __init__(self, format):
        self.format = format
        
    def __str__(self):
        return "You entered {}. Invalid list format. Try again.".format(self.format)

class InvalidPositionError(Exception):    
    def __init__(self, share_count):
        self.share_count = share_count
        
    def __str__(self):
        return "You entered the invalid position {}. Try again".format(self.share_count)