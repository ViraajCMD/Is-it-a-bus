class Vehicle:

    def __init__(self, name, mileage, max_speed):

        self.name = name
        self.mileage = mileage
        self.max_speed = max_speed

class Bus(Vehicle):
    pass


School_bus = Bus("School Volvo", 60, 280)
print(f"Vehicle Name: {School_bus.name} Mileage: {School_bus.mileage} Max_speed: {School_bus.max_speed}")