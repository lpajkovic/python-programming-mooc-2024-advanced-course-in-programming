# WRITE YOUR SOLUTION HERE:

def remove_smaller_than(numbers:list, limit:int)->list:
    
    return [num for num in numbers if num>=limit]