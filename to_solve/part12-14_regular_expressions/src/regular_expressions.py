# Write your solution here
import re

def is_dotw(my_string:str)->bool:
    
    return bool(re.search("Mon|Tue|Wed|Thu|Fri|Sat|Sun", my_string))

def all_vowels(my_string:str)->bool:
    
    for letter in my_string:
        if bool(re.search("[aeiou]", letter)) is False:
            return False
        
    return True

def time_of_day(my_string:str)->bool:
    
    return bool(re.search("[0-23]:[0-59]:[0-59]", my_string))

if __name__=="__main__":
    print(all_vowels("eioueioieoieou"))
    print(all_vowels("autoooo"))