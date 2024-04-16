# Write your solution here:

class Item:
    
    def __init__(self, name:str, weight:int):
        self.__name=name
        self.__weight=weight
        
    def name(self):
        return self.__name
    
    def weight(self):
        return self.__weight
    
    def __str__(self):
        return f"{self.name()} ({self.weight()} kg)"
    
    
class Suitcase:
    
    def __init__(self, max_weight:int):
        self.__max_weight=max_weight
        self.__curr_weight=0
        self.__suit_items=[]

    def add_item(self, item:Item):
        if item.weight()+self.__curr_weight>self.__max_weight:
            pass
        else:
            self.__suit_items.append(item)
            self.__curr_weight+=item.weight()
            
    def print_items(self):
        if len(self.__suit_items)==0:
            pass
        else:
            for item in self.__suit_items:
                print(item)
            
    def weight(self):
        return self.__curr_weight
    
    def heaviest_item(self):
        
        heaviest=None
        heaviest_weight=0
        
        if len(self.__suit_items)!=0:
            
            for item in self.__suit_items:
                if item.weight()>heaviest_weight:
                    heaviest=item
                    heaviest_weight=item.weight()
                    
        return heaviest
        
        
            
    def __str__(self):
        if len(self.__suit_items)==1:
            return f"{len(self.__suit_items)} item ({self.__curr_weight} kg)"
        else:
            return f"{len(self.__suit_items)} items ({self.__curr_weight} kg)"


class CargoHold:
    
    def __init__(self, max_weight:int):
        self.__max_weight=max_weight
        self.__curr_weight=0
        self.__cargo_items=[]
        
    def add_suitcase(self, suitcase: Suitcase):
        if suitcase.weight()+self.__curr_weight>self.__max_weight:
            pass
        else:
            self.__cargo_items.append(suitcase)
            self.__curr_weight+=suitcase.weight()
     
    def print_items(self):
        if len(self.__cargo_items)==0:
            print("")
        else:
            for suitcase in self.__cargo_items:
                if suitcase.print_items()!=None:
                    print(suitcase.print_items()) 
            
    def __str__(self):
        
        if len(self.__cargo_items)==1:
            return f"1 suitcase, space for {self.__max_weight-self.__curr_weight} kg"
        else:
            return f"{len(self.__cargo_items)} suitcases, space for {self.__max_weight-self.__curr_weight} kg"



if __name__=="__main__":
    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    adas_suitcase = Suitcase(10)
    adas_suitcase.add_item(book)
    adas_suitcase.add_item(phone)

    peters_suitcase = Suitcase(10)
    peters_suitcase.add_item(brick)

    cargo_hold = CargoHold(1000)
    cargo_hold.add_suitcase(adas_suitcase)
    cargo_hold.add_suitcase(peters_suitcase)

    print("The suitcases in the cargo hold contain the following items:")
    cargo_hold.print_items()