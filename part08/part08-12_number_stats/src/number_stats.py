# Write your solution here!
class  NumberStats:
    def __init__(self):
        self.numbers = 0
        self.sum_nums=0

    def add_number(self, number:int):
        self.numbers+=1
        self.sum_nums+=number

    def count_numbers(self):
        return self.numbers
    
    def get_sum(self):
        return self.sum_nums
    
    def average(self):
        if self.numbers!=0:
            return self.get_sum()/self.numbers
    
def userInput()->None:
    
    print("Please type in integer numbers:")
    stats=NumberStats()
    stats_even=NumberStats()
    stats_odd=NumberStats()
    
    while True:
        num=int(input())
        if num==-1:
            print("Sum of numbers:", stats.get_sum())
            print("Mean of numbers:", stats.average())
            print("Sum of even numbers:", stats_even.get_sum())
            print("Sum of odd numbers:", stats_odd.get_sum())
            break
        elif num%2==0:
            stats_even.add_number(num)
        else:
            stats_odd.add_number(num)
        stats.add_number(num)


def main():
    userInput()

main()