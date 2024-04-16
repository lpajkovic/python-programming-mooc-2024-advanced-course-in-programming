# Write your solution here:

def word_generator(characters:str, length:int, amount:int)->list:
    
    return (characters[i:i+length] for i in range(amount))