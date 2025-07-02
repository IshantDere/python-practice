class car_comp:
    def __init__(self, brand, color, is_4wheel_drive):
        self.brrand = brand
        self.color = color
        self.is_4wheel_drive = is_4wheel_drive

car1 = car_comp("Toyota", "Red", False)

print(car1.color)