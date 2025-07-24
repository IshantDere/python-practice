class movieticket:
    def __init__(self, movie_name, age):
        self.movie_name = movie_name
        self.age = age

    def get_price(self):
        if self.age < 13:
            return "100 rs"
        elif 60 > self.age > 13:
            return "200 rs"
        elif self.age > 60:
            return "150 rs"
        
    def get_info(self):
        return "movie name: ", self.movie_name , "age: ", self.age ,  "Price: ", str(self.get_price())
    

movie_1 = movieticket("Spiderman", 10)
print(movie_1.get_info())