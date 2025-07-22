class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_grade(self):
        i = self.marks
        if i > 90:
            return self.name ,"A"
        elif i >= 75 & i <= 89:
            return self.name ,"B"
        elif i >= 50 & i <= 70:
            return self.name ,"C"
        elif i < 50:
            return self.name ,"D"
            
s1 = student("Jimmy", 92)
print(s1.get_grade())