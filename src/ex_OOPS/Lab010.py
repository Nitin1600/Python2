# class Student:
#     pass
# obj1 = Student()
# obj2 = Student()

class Pen:
    def __init__(self,name,color):
        self.name=name
        self.color=color
obj1 = Pen("Reynolds", "Blue")
# print(obj1)

# class Pen:
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color
#     def printDetails(self):
#         print(self.name, self.color)
# obj1=Pen("Reynolds", "Blue")
# obj2=Pen("Cello", "Black")
# obj1.printDetails()
# obj2.printDetails()

# class Facebook:
#     def __init__(self,username,password):
#         self.username = username
#         self.password = password
#     def login(self):
#         print(self.username, "logged in successfully")
#     def logout(self):
#         print(self.username, "logged out successfully")
# obj = Facebook("Raj", "abc@123")
# obj.login()
# obj.logout()

class Pen:
    material = "pen"
    def __init__(self,name,color,brand):
        self.name = name
        self.color = color
        self.brand = brand

    def printDetails(self):
        a = 10
        b = 20
        print(self.material)
        print(self.name, self.color, self.brand)

obj1 = Pen("Reynolds", "Blue", "Britania")
obj2 = Pen("Cello", "Black", "b")
obj1.printDetails()
obj2.printDetails()
obj1.material='ttt'