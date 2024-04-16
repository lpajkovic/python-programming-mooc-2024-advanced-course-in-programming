# Write your solution here

def prime_numbers():
    
    yield 2
    num=3
    while True:
        flag=True
        for i in range(2, num-1):
            if num%i==0:
                flag=False
                break
        if flag is True:
            yield num
        num+=1