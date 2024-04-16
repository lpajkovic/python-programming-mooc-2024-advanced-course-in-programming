# WRITE YOUR SOLUTION HERE:

class SimpleDate:
    
    def __init__(self, day:int, month:int, year:int):
        self._day=day
        self._month=month
        self._year=year
        
    def __str__(self):
        return f"{self._day}.{self._month}.{self._year}"
    
    def __lt__(self, another):
        
        if self._year<another._year:
            return True
        elif self._year==another._year:
            if self._month<another._month:
                return True
            elif self._month==another._month:
                if self._day<another._day:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
        
    def __gt__(self, another):
        
        if self._year>another._year:
            return True
        elif self._year==another._year:
            if self._month>another._month:
                return True
            elif self._month==another._month:
                if self._day>another._day:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
        
    def __eq__(self, another):
        
        if self._year==another._year and self._month==another._month and self._day==another._day:
            return True
        return False
    
    def __ne__(self, another):
        
        if self._year!=another._year or self._month!=another._month or self._day!=another._day:
            return True
        return False 
    
    def __add__(self, number:int):
        
        new_day=self._day+number
        new_month=self._month
        new_year=self._year
        if new_day>30:
            new_month+=new_day//30
            new_day=new_day%30
            if new_month>12:
                new_year+=new_month//12
                new_month=new_month%12
        
        return SimpleDate(new_day, new_month, new_year)
    
    def __sub__(self, another):
        
        self_days=self._day+(self._month*30)+(360*self._year)
        
        another_days=another._day+(another._month*30)+(360*another._year)
        
        
        return abs(self_days-another_days)
        
    
    
if __name__=="__main__":
    d1 = SimpleDate(4, 10, 2020)
    d2 = SimpleDate(2, 11, 2020)
    d3 = SimpleDate(28, 12, 1985)

    print(d2-d1)
    print(d1-d2)
    print(d1-d3)