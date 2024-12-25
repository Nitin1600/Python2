# class Base:
#     d = 10
#     def __init__(self):
#         self._a = 2
#         self.b = 5
#
#
# obj = Base()
# print(obj._a)
# print(obj.b)
# print(obj.d)

# class Base:
#     def __init__(self):
#         self.__a = 2
#         self.b = 5
#
# obj = Base()
# print(obj._Base__a)
# print(obj.b)

class Base:
    def __init__(self):
        self.a = "Geeksforgeeks"
        self.__b = "HellOnFire"
        self._c = "Hype"

    def _pen(self):
        self.d = "Hyper"
        return self.d

    def __pencil(self):
        self.e = "clan"
        return self.e

    def eraser(self):
        self.f = "Khen"
        return self.f

obj = Base()
print(obj.a)
print(obj._c)
print(obj._Base__b)
print(obj._pen())
print(obj._Base__pencil())
print(obj.eraser())