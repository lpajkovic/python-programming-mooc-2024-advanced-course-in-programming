# Write your solution here:

def sort_by_seasons(items:list)->list:
    
    def ret_seasons(item:str):
        return item["seasons"]
    
    return sorted(items, key=ret_seasons)