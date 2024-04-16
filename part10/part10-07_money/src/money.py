# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        self._euros = euros
        self._cents = cents

    def __str__(self):
        print_cents=""
        if self._cents<10:
            print_cents=0
        return f"{self._euros}.{print_cents}{self._cents} eur"

    def __eq__(self, another):
        
        if self._euros == another._euros and self._cents==another._cents:
            return True
        
        return False
    
    def __ne__(self, another):
        
        if self._euros!= another._euros or self._cents!=another._cents:
            return True
        
        return False
    
    def __gt__(self, another):
        
        if self._euros>another._euros:
            return True
        elif self._euros<another._euros:
            return False
        elif self._euros==another._euros:
            if self._cents>another._cents:
                return True
            else:
                return False
            
    def __lt__(self, another):
        
        if self._euros<another._euros:
            return True
        elif self._euros>another._euros:
            return False
        elif self._euros==another._euros:
            if self._cents<another._cents:
                return True
            else:
                return False
    
    def __add__(self, another):
        
        new_euros=self._euros+another._euros
        new_cents=self._cents+another._cents
        if new_cents>=100:
            new_euros+=1
            new_cents-=100
        
        return Money(new_euros, new_cents)
    
    def __sub__(self, another):
        
        new_euros=self._euros-another._euros
        new_cents=self._cents-another._cents
        if new_cents<0:
            new_cents=100-abs(new_cents)
            new_euros-=1
        if new_euros<0:
            raise ValueError("a negative value is not allowed")
        else:
            return Money(new_euros, new_cents)

if __name__=="__main__":
    e1 = Money(4, 5)
    e2 = Money(2, 95)

    e3 = e1 + e2
    e4 = e1 - e2

    print(e3)
    print(e4)

    e5 = e2-e1