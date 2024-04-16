# Write your solution here:

class Series:
    
    def __init__(self, title:str, seasons:int, genres:list):
        self.title=title
        self.seasons=seasons
        self.genres=genres
        self.rating=[]
        
    def rate(self, rating:int):
        if rating>=0 and rating <=5:
            self.rating.append(rating)
      
    def average(self):
        if len(self.rating)!=0:
            return sum(self.rating)/len(self.rating)  
        else:
            return 0
        
    
    def __str__(self):
        
        title_str=f"{self.title} ({self.seasons} seasons)"
        genre=", ".join(self.genres)
        genre_str=f"genres: {genre}"
        rating_str=""
        if len(self.rating)>0:
            rating_str=f"{len(self.rating)} ratings, average {self.average():.1f} points"
        else:
            rating_str=f"no ratings"
        return (title_str + "\n" + genre_str +"\n" + rating_str)
        
def minimum_grade(rating: float, series_list:list):
        
    ret_list=[]
        
    for series in series_list:
        if series.average()>=rating:
            ret_list.append(series)
                
    return ret_list
    
def includes_genre(genre:str, series_list:list):
        
    ret_list=[]
        
    for series in series_list:
        if genre in series.genres:
            ret_list.append(series)
                
    return ret_list        
        
if __name__=="__main__":
    s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    s1.rate(5)

    s2 = Series("South Park", 24, ["Animation", "Comedy"])
    s2.rate(3)

    s3 = Series("Friends", 10, ["Romance", "Comedy"])
    s3.rate(2)

    series_list = [s1, s2, s3]

    print("a minimum grade of 4.5:")
    for series in minimum_grade(4.5, series_list):
        print(series.title)

    print("genre Comedy:")
    for series in includes_genre("Comedy", series_list):
        print(series.title)
    
