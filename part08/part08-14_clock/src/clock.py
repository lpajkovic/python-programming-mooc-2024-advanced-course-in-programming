# Write your solution here:
# Write your solution here:
class Clock:
    def __init__(self, hours:int, minutes:int, seconds:int):
        self.seconds = seconds
        self.minutes = minutes
        self.hours=hours
        
    def set(self, hours:int, minutes:int):
        self.hours=hours
        self.minutes=minutes
        self.seconds=0

    def tick(self):
        
        self.seconds+=1
        
        if self.seconds==60:
            self.seconds=0
            self.minutes+=1
            if self.minutes==60:
                self.minutes=0
                self.hours+=1
                if self.hours==24:
                    self.hours=0
                    
    
    def __str__(self):
        
        if self.hours<10:
            if self.minutes<10:
                if self.seconds<10:
                    return f"0{self.hours}:0{self.minutes}:0{self.seconds}"
                else:
                    return f"0{self.hours}:0{self.minutes}:{self.seconds}"
            else:
                if self.seconds<10:
                    return f"0{self.hours}:{self.minutes}:0{self.seconds}"
                else:
                    return f"0{self.hours}:{self.minutes}:{self.seconds}"
        else:
            if self.minutes<10:
                if self.seconds<10:
                    return f"{self.hours}:0{self.minutes}:0{self.seconds}"
                else:
                    return f"{self.hours}:0{self.minutes}:{self.seconds}"
            else:
                if self.seconds<10:
                    return f"{self.hours}:{self.minutes}:0{self.seconds}"
                else:
                    return f"{self.hours}:{self.minutes}:{self.seconds}"
       
        
        
        
if __name__=="__main__":
    clock = Clock(23, 59, 55)
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)

    clock.set(12, 5)
    print(clock)