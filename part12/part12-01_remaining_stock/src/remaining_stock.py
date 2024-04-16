# Write your solution here:

def sort_by_remaining_stock(items:list)->list:
    
    def order_by_value(item:tuple):
        return item[2]
    
    return sorted(items, key=order_by_value)