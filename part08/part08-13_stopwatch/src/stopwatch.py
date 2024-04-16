# Write your solution here:
class Stopwatch:
    def __init__(self):
        self.seconds = 0
        self.minutes = 0

    def tick(self):
        if self.seconds==59:
            if self.minutes==59:
                self.minutes=0
                self.seconds=0
            else:
                self.minutes+=1
                self.seconds=0
        else:
            self.seconds+=1
    
    def __str__(self):
        if self.minutes<10 and self.seconds<10:
            return f"0{self.minutes}:0{self.seconds}"
        elif self.minutes<10 and self.seconds>=10:
            return f"0{self.minutes}:{self.seconds}"
        elif self.minutes>=10 and self.seconds<10:
            return f"{self.minutes}:0{self.seconds}"
        else:
            return f"{self.minutes}:{self.seconds}"
        
        
        
if __name__=="__main__":
    watch = Stopwatch()
    for i in range(3600):
        print(watch)
        watch.tick()