class rectangle:
    def __init__(self, lenght, width):
        self.lenght = lenght
        self.width = width

    def area(self):
        return self.lenght * self.width
    
    def perimeter(self):
        return 2 * (self.lenght * self.width)
    
rectangle_1 = rectangle(10, 5)
print(rectangle_1.perimeter())