class Bike:
    def __init__(self,name,color,brand):
        self.name = name
        self.color = color
        self.brand = brand

    def printdetails(self):
        print(self.name, self.color, self.brand)

obj = Bike("NS200", "White", "Pulsar")
obj.printdetails()

class Animal:
    def __init__(self,name,significance):
        self.name = name
        self.significance = significance
    def printdetails(self):
        print(self.name, self.significance)
obj1 = Animal("Tiger:", "It's our national animal")
obj1.printdetails()