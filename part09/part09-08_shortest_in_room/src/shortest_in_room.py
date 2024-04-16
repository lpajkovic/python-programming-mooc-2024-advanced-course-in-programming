# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return f"{self.name} ({self.height} cm)"


class Room:
    
    def __init__(self):
        self.persons=[]
        
    def add(self, person: Person):
        self.persons.append(person)
        
    def is_empty(self):
        if len(self.persons)==0:
            return True
        return False
    
    def print_contents(self):
        
        combined=0
        for person in self.persons:
            combined+=person.height
        
        print(f"There are {len(self.persons)} in the room, and their combined height is {combined} cm")
        
        for person in self.persons:
            print(person)
          
    def shortest(self):
        
        shortest=None
        shortest_height=1000
        
        for person in self.persons:
            if person.height<shortest_height:
                shortest=person
                shortest_height=person.height
                
        return shortest
    
    def remove_shortest(self):
        
        removed=None
        if len(self.persons)>0:
            removed=self.shortest()
            self.persons.remove(self.shortest())
            
            
        return removed   
    
    
if __name__=="__main__":
    room = Room()

    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Nina", 162))
    room.add(Person("Ally", 166))
    room.print_contents()

    print()

    removed = room.remove_shortest()
    print(f"Removed from room: {removed.name}")

    print()

    room.print_contents()