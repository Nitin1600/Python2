# a = 5
# def abc():
#     b = 10
#     print(b)
# print(a)
# abc()

# a = 5
# def abc():
#     print(a)
# print(a)
# abc()

# a = 5
# def sum():
#     a = a + 2
#     print(a)
#
# print(a)
# sum()

# a = 5
# def sum():
#     global a
#     a = a+2
#
# print(a)
# sum()
# print(a)

# def foo():
#     x = 20
#     def bar():
#         global x
#         x = 25
#         #print(x)
#     print("Before calling bar: ",x)
#     print("Calling bar now")
#     bar()
#     print("After calling bar: ",x)
# #(x)
# foo()
# print("x in main: ",x)

# def A():
#     print("How are you")
#     def B():
#         print("Hello World")
#     print("Nested function is executing")
#     B()
# A()

# def outer():
#     x = "local"
#     def inner():
#         nonlocal x
#         x = "nonlocal"
#         print("inner:", x)
#
#     inner()
#     print("a:", x)
# outer()

# def addtwonumbers(a,b):
#     #a=5
#     #b=10
#     c=a+b
#     print(c)
# addtwonumbers(1,4)

# def oddoreven(num):
#     #num=4
#     if num % 2 == 0:
#         print(num, "is even number")
#     else:
#         print(num, "is odd number")
# oddoreven(9)