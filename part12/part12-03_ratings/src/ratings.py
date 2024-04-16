# TEE RATKAISUSI TÄHÄN:

# Write your solution here:

def sort_by_ratings(items:list)->list:
    
    def ret_raiting(item:str):
        return item["rating"]
    
    return sorted(items, key=ret_raiting, reverse=True)