class product:
    def __init__(self, name, price, discount_percent = 0):
        self.name = name
        self.price = price
        self.discount_percent = discount_percent

    def get_final_price(self):
        self.price = self.price - (self.price * self.discount_percent / 100)
        return self.price
    
product_1 = product("Jimmy", 2000, 10)
print(product_1.get_final_price())