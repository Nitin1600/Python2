# class A:
#     pass
#
# class B(A):
#     pass

# class A:
#     pass
#
# class B:
#     pass
#
# class C(A,B):
#     pass
#
# class A:
#     pass
#
# class B(A):
#     pass
#
# class C(B):
#     pass

# class Student:
#     def printdetails(self):
#         print("Hello Raj, good morning")
#
# class Main(Student):
#     pass
#
# obj = Main()
# obj.printdetails()

# class Student:
#     def printdetails(self):
#         print("Hello Raj, good morning")
#
# class Address:
#     def printaddress(self):
#         print("I am from bengaluru")
#
# class Main(Student,Address):
#     pass
#
# obj = Main()
# obj.printdetails()
# obj.printaddress()

# class Student:
#     def printdetails(self):
#         print("Hello Raj, good morning")
#
# class Address(Student):
#     def printaddress(self):
#         print("I am from bengaluru")
#
# class Main(Address):
#     pass
#
# obj = Main()
# obj.printdetails()
# obj.printaddress()

class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def printdetails(self):
        print(self.name,self.age)

class Address(Student):
    def __init__(self,name,age,address):
        self.address = address
        Student.__init__(self,name,age)

    def printfulldetails(self):
        print(self.name,self.age,self.address)

class City(Address):
    def __init__(self,name,age,address,city):
        self.city = city
        Address.__init__(self,name,age,address)

    def printfulldetails1(self):
        print(self.name,self.age,self.address,self.city)

class Main(City):
    pass

obj1 = Main("Raj", "29", "Kuvempu_nagar", "Hungundh")
obj2 = Main("Akshith", "32", "Vidya_giri", "Ilkal")
obj1.printfulldetails1()
obj2.printfulldetails1()
obj1.printfulldetails()
obj1.printdetails()