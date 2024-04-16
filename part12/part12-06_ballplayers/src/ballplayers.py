class BallPlayer:
    def __init__(self, name: str, number: int, goals: int, passes: int, minutes: int):
        self.name = name
        self.number = number
        self.goals = goals
        self.passes = passes
        self.minutes = minutes

    def __str__(self):
        return (f'BallPlayer(name={self.name}, number={self.number}, '
            f'goals={self.goals}, passes={self.passes}, minutes={self.minutes})')


# Write your solution here

def most_goals(players:list)->str:
    
    most_sorted=sorted(players, key=lambda play : play.goals)
    return most_sorted[-1].name

def most_points(players:list)->tuple:
    
    most_sorted=sorted(players, key=lambda play: play.goals + play.passes)
    return (most_sorted[-1].name, most_sorted[-1].number)

def least_minutes(players:list)->BallPlayer:
    
    least_sorted=sorted(players, key=lambda play: play.minutes)
    return least_sorted[0]