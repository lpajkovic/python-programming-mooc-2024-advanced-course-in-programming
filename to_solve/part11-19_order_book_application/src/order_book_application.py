# Write your solution here
# If you use the classes made in the previous exercise, copy them here

# Write your solution here:

class Task:
    
    id=0
    
    def __init__(self, description:str, programmer:str, workload:int):
        self.description=description
        self.programmer=programmer
        self.workload=workload
        Task.id+=1
        self.id=Task.id
        self.finished=False
        
    def mark_finished(self):
        self.finished=True
        
    def is_finished(self):
        return self.finished
    
    def __str__(self):
        finished="NOT FINISHED"
        if self.finished is True:
            finished="FINISHED"
        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {finished}"
    
class OrderBook:
    id=0
    def __init__(self):
        self.orders=[]
        OrderBook.id+=1
        self.id=OrderBook.id
        
    def add_order(self, description:str, programmer:str, workload:int):
        self.orders.append(Task(description, programmer, workload))
        
    def all_orders(self):
        ret_list=[]
        for order in self.orders:
            ret_list.append(order)
        return ret_list
       
    def programmers(self):
        ret_list=[]
        for order in self.orders:
            if order.programmer not in ret_list:
                ret_list.append(order.programmer) 
            
        return ret_list
    
    def mark_finished(self, id:int):
        not_found=True
        for order in self.orders:
            if order.id==id:
                order.mark_finished()
                not_found=False
                
        if not_found is True:
            raise ValueError("order not found")
        
    def finished_orders(self):
        ret_list=[]
        for order in self.orders:
            if order.finished is True:
                ret_list.append(order)
                
        return ret_list
    
    def unfinished_orders(self):
        ret_list=[]
        for order in self.orders:
            if order.finished is False:
                ret_list.append(order)
                
        return ret_list
    
    def status_of_programmer(self, programmer:str):
        
        if programmer not in self.programmers():
            raise ValueError("no programmer")
        
        finished=0
        unfinished=0
        workload_finished=0
        workload_unfinished=0
        
        for order in self.orders:
            if order in self.finished_orders() and order.programmer==programmer:
                workload_finished+=order.workload
                finished+=1
            elif order in self.unfinished_orders() and order.programmer==programmer:
                workload_unfinished+=order.workload
                unfinished+=1
                
        return (finished, unfinished, workload_finished, workload_unfinished)
        
        
if __name__=="__main__":    
    orders = OrderBook()
    orders.add_order("program webstore", "Adele", 10)
    orders.add_order("program mobile app for workload accounting", "Eric", 25)
    orders.add_order("program app for practising mathematics", "Adele", 100)

    for order in orders.all_orders():
        print(order)

    print()

    for programmer in orders.programmers():
        print(programmer)