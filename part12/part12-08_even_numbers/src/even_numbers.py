# Write your solution here

def even_numbers(beginning:int, maximum:int):
    
    num=beginning
    while num<=maximum:
        if num%2==0:
            yield num
        num+=1
        
