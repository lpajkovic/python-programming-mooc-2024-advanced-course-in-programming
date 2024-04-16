# WRITE YOUR SOLUTION HERE:

class LotteryNumbers:
    
    def __init__(self, week:int, numbers:list):
        self.week=week
        self.numbers=numbers
        
    def number_of_hits(self, numbers:list):
        
        return len([num for num in numbers if num in self.numbers])
    
    def hits_in_place(self, numbers:list):
        
        return [num if num in self.numbers else -1 for num in numbers]