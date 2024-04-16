from functools import reduce

class CourseAttempt:
    def __init__(self, course_name: str, grade: int, credits: int):
        self.course_name = course_name
        self.grade = grade
        self.credits = credits

    def __str__(self):
        return f"{self.course_name} ({self.credits} cr) grade {self.grade}"

# Write your solution

def sum_of_all_credits(course_list:list)->int:
    
    return reduce(lambda credit_sum, credit: credit_sum+credit.credits, course_list, 0)

def sum_of_passed_credits(course_list:list)->int:
    
    return reduce(lambda credit_sum, credit: credit_sum+credit.credits, filter(lambda course : course.grade>0, course_list), 0)

def average(course_list:list)->float:
    
    passed=list(filter(lambda course : course.grade>0, course_list))
    sum_of_passed=reduce(lambda credit_sum, credit: credit_sum+credit.grade, filter(lambda course : course.grade>0, course_list), 0)
    
    return sum_of_passed/len(passed)



if __name__=="__main__":
    
    s1 = CourseAttempt("Introduction to Programming", 5, 5)
    s2 = CourseAttempt("Advanced Course in Programming", 0, 4)
    s3 = CourseAttempt("Data Structures and Algorithms", 3, 10)
    ag = average([s1, s2, s3])
    print(ag)