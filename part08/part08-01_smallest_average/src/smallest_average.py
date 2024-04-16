# Write your solution here

def smallest_average(person1:dict, person2:dict, person3:dict)->dict:
    
    avgs=[]
    
    avg1=(person1["result1"]+person1["result2"]+person1["result3"])/3
    avgs.append(avg1)
    avg2=(person2["result1"]+person2["result2"]+person2["result3"])/3
    avgs.append(avg2)
    avg3=(person3["result1"]+person3["result2"]+person3["result3"])/3
    avgs.append(avg3)
    
    smallest_idx=avgs.index(min(avgs))
    
    if smallest_idx==0:
        return person1
    elif smallest_idx==1:
        return person2
    else:
        return person3

if __name__=="__main__":
    person1 = {"name": "Mary", "result1": 2, "result2": 3, "result3": 3}
    person2 = {"name": "Gary", "result1": 5, "result2": 1, "result3": 8}
    person3 = {"name": "Larry", "result1": 3, "result2": 1, "result3": 1}

    print(smallest_average(person1, person2, person3))