class charge:
    def __init__(self, name, bank_balance):
        self.name = name
        self.bank_balance = bank_balance
        
    def pay_charge(self):
        if self.bank_balance < 15000:
            return "You have to pay charge!"
        else:
            return "You dont need to pay any kind of charge"
        
customer1 = charge("jimmy", 12500)
customer2 = charge("jim", 15001)

print(customer2.pay_charge())