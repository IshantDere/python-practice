class character:
    def __init__(self, health, damage, speed):
        self.health = health
        self.damage = damage
        self.speed = speed

        def double_mspeed(self):
            self.speed *= 2

        

a = character(100, 50, 4)
b = character(100, 40, 2)

print(f"health of a : {a.speed} km/h")
print(f"b speed : {b.speed} km/h")