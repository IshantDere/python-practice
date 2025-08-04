class bankaccount:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance

    def deposite(self, amount):
        self.balance += amount
        # print(self.balance)
        return self.balance
        
    def withdraw(self, amount):
        if self.balance < amount:
            # print("Insufficient funds")
            return "Insufficient funds"
        else:
            self.balance -= amount
            # print(self.balance)
            return self.balance
            
    
acc = bankaccount("Ishant", 1000)
x = acc.withdraw(5)
print(x)