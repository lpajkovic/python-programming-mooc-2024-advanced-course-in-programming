# WRITE YOUR SOLUTION HERE:

def filter_forbidden(string:str, forbidden:str)->str:
    
    return "".join(letter for letter in string if letter not in forbidden)