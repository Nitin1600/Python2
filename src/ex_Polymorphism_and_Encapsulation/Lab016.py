# print(len("learn"))
# print(len([10, 20, 30]))

# def add(x,y,z=0):
#     return x+y+z
#
# print(add(2,3))
# print(add(2,3,4))

# class India():
#     def capital(self):
#         print("New Delhi is the capital of india")
#
#     def language(self):
#         print("Hindhi is widely spoken language")
#
#     def type(self):
#         print("India is a developing country")

# class USA():
#     def capital(self):
#         print("Washington D.C is the capital of usa")
#
#     def language(self):
#         print("English is widely spoken language")
#
#     def type(self):
#         print("USA is a developed country")
#
# obj_india = India()
# obj_usa = USA()
# for country in (obj_india, obj_usa):
#     country.capital()
#     country.language()
#     country.type()

# class Bird:
#     def intro(self):
#         print("There are many types of birds")
#
#     def flight(self):
#         print("Most of them can fly, few cannot")
#
# class Sparrow(Bird):
#     def flight(self):
#         print("Sparrows can fly")
#
# class Ostrich(Bird):
#     def flight(self):
#         print("Ostriches cannot fly")
#
# obj_bird = Bird()
# obj_sparrow = Sparrow()
# obj_ostrich = Ostrich()
#
# obj_bird.intro()
# obj_bird.flight()
#
# obj_sparrow.intro()
# obj_sparrow.flight()
#
# obj_ostrich.intro()
# obj_ostrich.flight()

# def func(obj):
#     obj.capital()
#     obj.language()
#     obj.type()
#
# obj_india = India()
# obj_usa = USA()
#
# func(obj_india)
# func(obj_usa)

# class India:
#     def capital(self):
#         print("New delhi is the capital city")
#
#     def language(self):
#         print("Hindhi is widely spoken language")
#
#     def type(self):
#         print("India is a developing country")
#
# class USA:
#     def capital(self):
#         print("Washington D.C., is the capital of usa")
#
#     def language(self):
#         print("English is widely spoken")
#
#     def type(self):
#         print("usa is developrd country")
#
# def func(obj):
#     obj.capital()
#     obj.language()
#     obj.type()
#
# obj_india = India()
# obj_usa = USA()
#
# func(obj_india)
# func(obj_usa)

class Animal:
    def speak(self):
        raise NotImplementedError("Subclass must implement this method")

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow"

animals = [Dog(), Cat()]

for animal in animals:
    print(animal.speak())