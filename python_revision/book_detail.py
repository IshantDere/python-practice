class book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def is_long_book(self):
        if self.pages > 300:
            return True
        else:
            return False
        
    def get_summary(self):
        return "Tiltle : ", self.title, "Author : ", self.author, "Pages : ", self.pages
        
book_1 = book("Jimmy's house", "Jimmy", 350)
print(book_1.get_summary())
