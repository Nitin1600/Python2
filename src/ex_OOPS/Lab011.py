# class Student:
#     pass
# obj1 = Student()
# obj2 = Student()
#
# class Pen:
#     def __init__(self,name,color):
#         self.name=name
#         self.color=color
# obj1 = Pen("Reynolds", "blue")
#
# class Pen:
#     def __init__(self,name,color):
#         self.name=name
#         self.color=color
# obj1 = Pen("Reynolds", "Blue")

class Pen:
    def __init__(self,name,color):
        self.name = name
        self.color = color
    def printdetails(self):
        print(self.name,self.color)

obj1 = Pen("Reynolds", "Blue")
obj2 = Pen("Cello", "Black")
obj1.printdetails()
obj2.printdetails()

class Facebook:
    def __init__(self,username,password):
        self.username = username
        self.password = password
    def login(self):
        print(self.username, "logged in successfully")
    def logout(self):
        print(self.username, "logged out successfully")
obj1 = Facebook("Raj", "abc@123")
obj1.login()
obj1.logout()

