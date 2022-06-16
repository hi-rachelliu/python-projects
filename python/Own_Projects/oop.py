class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
    
    def seating_capacity(self, capacity):
        print (f"The seating capacity of a {self.name} is {capacity} passengers")

class Bus(Vehicle):
        pass

v1 = Bus("bus", 180, 12)
v1.seating_capacity(50)
# print (f"Vehicle Name: {v1.name} Speed: {v1.max_speed} Mileage: {v1.mileage}")