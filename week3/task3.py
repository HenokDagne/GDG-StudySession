class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def describe(self):
        return f'This is a {self.make} {self.model} vehicle.'

    def start_engine(self):
        return f'The engine of the {self.make} {self.model} is now running.'

    def stop_engine(self):
        return f'The engine of the {self.make} {self.model} has been turned off.'

class Car(Vehicle):
    def __init__(self, make, model, num_doors):
        super().__init__(make, model)
        self.num_doors = num_doors
    
    def describe(self):
        return f'This is a {self.make} {self.model} car with {self.num_doors} doors.'

    def open_trunk(self):
        return f'The trunk of the {self.make} {self.model} car is now open.'

class Bike(Vehicle):
    def describe(self):
        return f'This is a {self.make} {self.model} bike.'

    def kickstand(self):
        return f'The kickstand of the {self.make} {self.model} bike is now down.'