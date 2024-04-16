# WRITE YOUR SOLUTION HERE:
class Employee:
    def __init__(self, name: str):
        self.name = name
        self.subordinates = []

    def add_subordinate(self, employee: 'Employee'):
        self.subordinates.append(employee)


def count_subordinates(employee: Employee):
    counter=len(employee.subordinates)
    
    if len(employee.subordinates)!=0:
        for subordinate in employee.subordinates:
            counter+=count_subordinates(subordinate)
            
    return counter