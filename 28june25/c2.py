class car_brand:
    def __init__(self, name, color, is_4wheeldrive, avg):
        self.name = name
        self.color = color
        self.is_4wheeldrive = is_4wheeldrive
        self.avg = avg

    def above_avg(self):
        if self.avg < 16:
            return "below average car"
        else:
            return "above average car"



car1 = car_brand("Toyota", "red", True, 16)
print(car1.above_avg())